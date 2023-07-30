import requests,json
from bs4 import BeautifulSoup
bin = input('INSIRA SUA BIN:')
headers = {
    'authority': 'ccbins.pro',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'referer': 'https://ccbins.pro/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
}

params = {
    'bins': bin,
}

response = requests.get('https://ccbins.pro/', params=params,headers=headers)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table')

card_info = {}

for row in table.find_all('tr'):

    label = row.find('th').text.strip()
    value = row.find('td').text.strip()
    card_info[label] = value


for label, value in card_info.items():
    print(f"{label} {value}")