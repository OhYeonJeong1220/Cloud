import requests
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request

headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
                }
mellon=requests.get("https://www.melon.com/chart/index.htm",headers=headers)
mellonsoup=BeautifulSoup(mellon.text,"html.parser")

titles=mellonsoup.find_all('div',{'class':'ellipsis rank01'})
title=[]
for t in titles:
    title.append(t.find('a').text)
for i in titles:
    youtube_url='https://www.youtube.com/results?search_query='
    url2=urllib.parse.quote_plus(i.find('a').text)
    full_url=youtube_url+url2
    youtube = requests.get(full_url, headers=headers)
    print(full_url)
