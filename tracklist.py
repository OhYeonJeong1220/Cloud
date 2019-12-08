import requests
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import re
headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        }
mellon=requests.get("https://www.melon.com/chart/index.htm",headers=headers)
soup=BeautifulSoup(mellon.text,"html.parser")

others=soup.find_all('a',{'class':'image_typeAll'})

for tr in others:
    tracks_url = 'https://www.melon.com/album/detail.htm?albumId={}'
    track_num = re.findall('\d+', tr.get('href'))
    track_url=tracks_url.format(track_num[0])
    track_res=requests.get(track_url,headers=headers)
    track_soup=BeautifulSoup(track_res.text,'html.parser')
    
    for j in track_soup.find_all('div',{'class':'ellipsis'}):
        if(j!=track_soup.find('div',{'class':'ellipsis rank02'})):
            if(j.find('a')):
                list_song=j.find('a').text
                print(list_song)
