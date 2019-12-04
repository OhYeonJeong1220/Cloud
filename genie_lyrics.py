import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.3'}#user info

url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20191128&hh=18&rtm=Y&pg={}'#page move

songid = []#songid

#곡 번호 크롤링
for n in range(1,3):
    link = url.format(n)
    resp = requests.get(link,headers = headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    #songs = soup.select('#body-content > div.newest-list > div > table')
    print('page',n,'====================================================') 
    #trs=xxxxxii  songs.find_all('tr',class_='list')
    i = 0
    for tr in soup.find_all('tr',class_='list'):
        #print(tr.get('songid'))
        i = i+1
        print(i)
        lyrics_url = 'https://www.genie.co.kr/detail/songInfo?xgnm={}'
        lyrics_link = lyrics_url.format(tr.get('songid'))
        lyrics_resp = requests.get(lyrics_link,headers = headers)
        lyrics_soup = BeautifulSoup(lyrics_resp.text,'html.parser')

        #lyrics = lyrics_soup.select('#pLyrics')
        
        print(lyrics_soup.find('pre',{'id':'pLyrics'}).find({'div'}).text)
        print(lyrics_soup.find('pre',{'id':'pLyrics'}).find({'p'}).text)
