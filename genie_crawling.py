import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib

import pymysql

#mysql ##
conn = pymysql.connect(
        host = '52.231.160.91',
        user = 'oyj',
        port = 3306,
        password = '1234',
        db = 'Cloud',
        charset = 'utf8'
        )

curs = conn.cursor()

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.3'}#user info

url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20191128&hh=18&rtm=Y&pg={}'#page move


#곡제목, 가수, 앨범 이름 크롤링
for n in range(1,3):
    link = url.format(n)
    resp = requests.get(link,headers = headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
    print("page: ",n,"=====================================================")
    
    for song in songs:
        title = song.find('td',{'class':'info'}).find('a',{'class':'title ellipsis'}).text
        singer = song.find('td',{'class':'info'}).find('a',{'class':'artist ellipsis'}).text
        album = song.find('td',{'class':'info'}).find('a',{'class':'albumtitle ellipsis'}).text
        #print(title.strip(),"  ",singer.strip(),"  ",album.strip())#use strip() -> delete blank space

        sql  = "INSERT INTO  song (title,singer,albumName) VALUES (%s,%s,%s)"
        #sql = 'select * from song'
        curs.execute(sql,('test2','test2','test2'))        
        #curs.execute(sql)
        #print(curs.fetchone())
        conn.commit()
#앨범 사진 크롤링
for i in soup.find_all('a',class_='cover'):
    img_url = link + i.find('img').get('src') 
    img_name = i.find('img').get('alt')
    #print(img_url)
   # print(img_name+'.jpg')
    
    #파일로 저장 
    #urllib.request.urlretrieve(img_url,img_name+'.jpg')


