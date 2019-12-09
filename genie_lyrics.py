import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
from  genie_crawling import G_matrix
from datetime import datetime
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.3'}#user info

today = datetime.today().strftime("%Y%m%d")#오늘 날짜

parts = urlparse('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20191206&hh=19&rtm=Y&pg=1')

#요소 분리
qs = dict(parse_qsl(parts.query))

#parse_sql의 결과를 딕셔너리로 캐스팅
qs['ymd'] = today

#수정
parts = parts._replace(query=urlencode(qs))
new_url = urlunparse(parts)

songid = []#songid
j=0
i=0
#곡 번호 크롤링
for n in range(1,3):
    parts_ = urlparse('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20191206&hh=19&rtm=Y&pg=1')
    #parse_sql의 결과를 딕셔너리로 캐스팅
    qs_ = dict(parse_qsl(parts_.query))
    #수정
    qs_['pg'] = n
    parts_ = parts_._replace(query=urlencode(qs_))
    link = urlunparse(parts_)
    
    resp = requests.get(link,headers = headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    #songs = soup.select('#body-content > div.newest-list > div > table')
    #print('page',n,'====================================================') 
    #trs=xxxxxii  songs.find_all('tr',class_='list')
    i = j
    for tr in soup.find_all('tr',class_='list'):
        #print(tr.get('songid'))
        lyrics_url = 'https://www.genie.co.kr/detail/songInfo?xgnm={}'
        lyrics_link = lyrics_url.format(tr.get('songid'))
        lyrics_resp = requests.get(lyrics_link,headers = headers)
        lyrics_soup = BeautifulSoup(lyrics_resp.text,'html.parser')
        lyric = lyrics_soup.find('pre', {'id': 'pLyrics'}).find({'p'}).text
        G_matrix[i][5] = lyric
        i=i+1
        j=i
        #lyrics = lyrics_soup.select('#pLyrics')
        
        #print(lyrics_soup.find('pre',{'id':'pLyrics'}).find({'div'}).text)
        #print(lyrics_soup.find('pre',{'id':'pLyrics'}).find({'p'}).text)
if (__name__ == "__main__"):
    for i in range(0, 100):
        print(G_matrix[i])
