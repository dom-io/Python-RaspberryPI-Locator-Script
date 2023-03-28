from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

url = "https://rpilocator.com/"
request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
page = urlopen(request_site)
html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

table = soup.table.find('tbody')

table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]

print(row)

