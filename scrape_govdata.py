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
print(df)
