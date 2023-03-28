from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

url = "https://rpilocator.com/feed/"
request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
page = urlopen(request_site)
html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

print(soup)