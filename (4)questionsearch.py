import requests
from bs4 import BeautifulSoup

query = input('Поиск по слову: ')
blocks = list()
for i in range(1,6):
    url = f'https://stackoverflow.com/questions/?page={i}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    blocks += list(x for x in [y.find('a', {'class', 's-link'}) for y in soup.find_all('h3', {'class': 's-post-summary--content-title'})] if query in x.contents[0])

print('Результаты поиска:')
for i in range(len(blocks)):
  print(f"{i+1}.{blocks[i].contents[0]}\n{'https://stackoverflow.com' + blocks[i].get('href')}")
