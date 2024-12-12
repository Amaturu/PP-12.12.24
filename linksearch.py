import requests
from bs4 import BeautifulSoup

url = 'https://www.py4e.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
set = set(link for link in links if link.get('href').startswith('https'))

print(len(set))