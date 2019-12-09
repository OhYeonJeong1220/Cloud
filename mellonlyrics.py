import requests
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import re
from mellonchart import M_matrix

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.3'}
mellon=requests.get("https://www.melon.com/chart/index.htm",headers=headers)
soup=BeautifulSoup(mellon.text,"html.parser")
RANK=100

lric=[]
lic=[]
lric2=[]
lic2=[]
lyrics=soup.find_all('tr',{'class':'lst50'})
lyrics2=soup.find_all('tr',{'class':'lst100'})
a=0
for tr in lyrics:
    lyrics_url='https://www.melon.com/song/detail.htm?songId={}'
    lyrics_add=lyrics_url.format(tr.get('data-song-no'))
    manylyrics=requests.get(lyrics_add,headers=headers)
    lyrics_soup=BeautifulSoup(manylyrics.text,'html.parser')
    lyric=str(lyrics_soup.find('div',{'id':'d_video_summary'}))
    lic = lyric.strip('<div class="lyric" id="d_video_summary"><!-- height:auto; 로 변경시, 확장됨 -->')
    M_matrix[a][5]=lic.strip('</')
    a = a + 1

tr2=50
for tr2 in lyrics2:
    lyrics2_url='https://www.melon.com/song/detail.htm?songId={}'
    lyrics2_add=lyrics2_url.format(tr2.get('data-song-no'))
    manylyrics2=requests.get(lyrics2_add,headers=headers)
    lyrics_soup2=BeautifulSoup(manylyrics2.text,'html.parser')
    lyric2=str(lyrics_soup2.find('div',{'id':'d_video_summary'}))
    lic2= lyric2.strip('<div class="lyric" id="d_video_summary"><!-- height:auto; 로 변경시, 확장됨 -->')
    M_matrix[a][5] = lic2.strip('</div>')
    a=a+1

i=0
if(__name__=="__main__"):
    for i in range(0,100):
        print(M_matrix[i])

