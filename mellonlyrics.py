import requests
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request

headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
                }
mellon=requests.get("https://www.melon.com/chart/index.htm",headers=headers)
soup=BeautifulSoup(mellon.text,"html.parser")
RANK=100

lric=[]
lic=[]
lric2=[]
lic2=[]
lyrics=soup.find_all('tr',{'class':'lst50'})
lyrics2=soup.find_all('tr',{'class':'lst100'})

for tr in lyrics:
    lyrics_url='https://www.melon.com/song/detail.htm?songId={}'
    lyrics_add=lyrics_url.format(tr.get('data-song-no'))
    manylyrics=requests.get(lyrics_add,headers=headers)
    lyrics_soup=BeautifulSoup(manylyrics.text,'html.parser')
    lyric=lyrics_soup.find('div',{'id':'d_video_summary'})
    lric.append(lyric.text)

tr2=50
for tr2 in lyrics2:
    lyrics2_url='https://www.melon.com/song/detail.htm?songId={}'
    lyrics2_add=lyrics2_url.format(tr2.get('data-song-no'))
    manylyrics2=requests.get(lyrics2_add,headers=headers)
    lyrics_soup2=BeautifulSoup(manylyrics2.text,'html.parser')
    lyric2=lyrics_soup2.find('div',{'id':'d_video_summary'})
    lric.append(lyric2.text)

for t in range(RANK):
    print('%d %s'%(t,lric[t].strip()))

