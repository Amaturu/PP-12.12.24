import requests
from bs4 import BeautifulSoup

url = 'https://py4e-data.dr-chuck.net/comments_42.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
comments = soup.find_all('span', {'class': 'comments'})

print(sum(list(int(tag.contents[0]) for tag in comments)))