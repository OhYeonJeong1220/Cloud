import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import re
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

#앨범  번호 크롤링
for n in range(1,3):
    #요소 분리
    parts_ = urlparse('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20191206&hh=19&rtm=Y&pg=1')
    #parse_sql의 결과를 딕셔너리로 캐스팅
    qs_ = dict(parse_qsl(parts_.query))
    #수정
    qs_['pg'] = n
    parts_ = parts_._replace(query=urlencode(qs_))
    link = urlunparse(parts_)

    resp = requests.get(link,headers = headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
    print('page',n,'====================================================')
    #trs=xxxxxii  songs.find_all('tr',class_='list')
    i = 0

    for album in songs:
        i = i+1
        print(i)
        track_url = 'https://www.genie.co.kr/detail/albumInfo?axnm={}'

        album_number = re.findall('\d+',album.find('a',{'class':'cover'}).get('onclick'))
        #print(album_number)

        track_link = track_url.format(album_number[0])
        track_resp = requests.get(track_link,headers = headers)
        track_soup = BeautifulSoup(track_resp.text,'html.parser')

        #tracks  = track_soup.select('#body-content > div.album-detail-infos')

        print(track_soup.find('div',{'class':'info-zone'}).find('h2',{'class':'name'}).text)#song name
        
        trackss = track_soup.select('#listContainer > div.songlist-box > div.music-list-wrap.none-album-list2 > table > tbody > tr')#track
        
        for m in trackss:
            print(m.find('td',{'class':'info'}).find('a',{'class':'title ellipsis'})['title'])
        #print(lyrics_soup.find('pre',{'id':'pLyrics'}).find({'div'}).text)
        #print(lyrics_soup.find('pre',{'id':'pLyrics'}).find({'p'}).text)

