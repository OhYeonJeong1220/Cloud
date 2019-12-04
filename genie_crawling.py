import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.3'}#user info

url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20191128&hh=18&rtm=Y&pg={}'#page move


for n in range(1,2):
    link = url.format(n)
    resp = requests.get(link,headers = headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
    print("page: ",n,"=====================================================")
    for song in songs:
        title = song.find('td',{'class':'info'}).find('a',{'class':'title ellipsis'}).text
        singer = song.find('td',{'class':'info'}).find('a',{'class':'artist ellipsis'}).text
        album = song.find('td',{'class':'info'}).find('a',{'class':'albumtitle ellipsis'}).text
        imgurl = song.find('a',{'class':'cover'}).find('img')['src']
        print(imgurl)
        #imgfile = open(title.strip()+'.jpg','wb')#파일 생성
        #imgfile.write(imgurl.content)
        #imgfile.close()
        print('이미지 파일을 생성하였습니다.')
        print(title.strip(),"  ",singer.strip(),"  ",album.strip())#use strip() -> delete blank space
