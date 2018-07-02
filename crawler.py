import urllib
from bs4 import BeautifulSoup
import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from create_db import CrawlerData

engine = create_engine("sqlite:///crawler_data.db")
Session = sessionmaker(bind=engine)
session = Session()

request = urllib.request.Request("http://register.start.bg/")
response = urllib.request.urlopen(request)
soup = BeautifulSoup(response)

for link in soup.find_all('a'):
    tmp_link = link.get('href')
    if tmp_link != None:
        if tmp_link.startswith("link"):
            _id = tmp_link[12:]
            payload = {'id': _id}
            r = requests.get('http://register.start.bg/link.php', params=payload)
            server = r.headers["Server"]
            tmp_link = r.url
        elif tmp_link.startswith("http"):
            r = requests.head(tmp_link)
            server = r.headers["Server"]
        else:
            tmp_link = None
            server = None
        if server != None and server.startswith("Apache"):
            server = "Apache"

    if tmp_link != None and server != None:
        data = CrawlerData(site=tmp_link, server=server)
        session.add(data)
        session.commit()

