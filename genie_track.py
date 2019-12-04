import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import re

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.3'}#user info

url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20191128&hh=18&rtm=Y&pg={}'#page move

songid = []#songid

#앨범  번호 크롤링
for n in range(1,3):
    link = url.format(n)
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

