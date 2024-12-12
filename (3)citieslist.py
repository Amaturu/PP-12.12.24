import requests
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/jobs/companies'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
info = soup.find_all('div', {'class': 'flex--item fl1 text mb0'})
cities_raw =  set(city_list for city_list in [tag.find('div', {'class': 'flex--item fc-black-500 fs-body1'}).contents[1].strip() for tag in info] if city_list != 'No office location')
cities = list()
lst = list([cities.append(city.strip()) for city in city_block.split(';')] for city_block in cities_raw)
cities = sorted(list(set(cities)))
print(cities)
