import httpx
from bs4 import BeautifulSoup

response = httpx.get("https://breadcrumbscollector.tech/")
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

all_links = soup.find_all('a')
for link in all_links:
    href = link.get('href')
    print(href)

