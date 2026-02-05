import requests
from bs4 import BeautifulSoup # pip install beautifulsoup4
import pandas as pd
import matplotlib.pyplot as plt
import io

plt.rcParams['font.family'] = 'Microsoft JhengHei'
plt.rcParams['axes.unicode_minus'] = False

url = 'https://data.gov.tw/dataset/34811' # 替換成你要找的資料集網址
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
links = soup.find_all('a', attrs={'title': True}) # 找出所有 <a> 且有 title 屬性的
csv_link = ''
for a in links:
    if 'CSV' in a['title']: # 關鍵字找尋
        csv_link = a['href']
        break
html = requests.get(csv_link, verify=False)
df = pd.read_csv(io.StringIO(html.text))

# 針對讀取的csv資料(df變數)做後續自定義處理
latest = df.loc[0]['monitordate']
x = []
y = []
for i in range(len(df)):
    row = df.loc[i]
    if row['monitordate'] == latest:
        x.append(f"{row['itemengname']}({row['itemunit']})")
        if row['concentration'] != 'x':
            y.append(float(row['concentration']))
        else:
            y.append(0)

plt.barh(x, y, label='空氣')
plt.legend()
plt.title(f'{latest} 花蓮空氣品質')
plt.xlabel('氣體微粒')
# plt.xticks(rotation=270)
plt.ylabel('含量')
plt.show()