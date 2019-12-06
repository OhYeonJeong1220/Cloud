import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
from datetime import datetime
import pymysql
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse

##mysql ##
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


today = datetime.today().strftime("%Y%m%d")#오늘 날짜

print("date: ", today)

parts = urlparse('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20191206&hh=19&rtm=Y&pg=1')
#요소 분리
qs = dict(parse_qsl(parts.query))
#parse_sql의 결과를 딕셔너리로 캐스팅
qs['ymd'] = today
#수정
parts = parts._replace(query=urlencode(qs))
new_url = urlunparse(parts)

print(new_url)

img_link1 = 'https:'
img_link2 = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20191206&hh=19&rtm=Y&pg=2'

#곡제목, 가수, 앨범 이름 크롤링
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
    print("page: ",n,"=====================================================")
    
    for song in songs:#노래 제못, 가수, 앨범
        title = song.find('td',{'class':'info'}).find('a',{'class':'title ellipsis'}).text
        singer = song.find('td',{'class':'info'}).find('a',{'class':'artist ellipsis'}).text
        album = song.find('td',{'class':'info'}).find('a',{'class':'albumtitle ellipsis'}).text
        print(title.strip(),"  ",singer.strip(),"  ",album.strip())#use strip() -> delete blank space

        #sql  = "INSERT INTO  song (title,singer,albumName) VALUES (%s,%s,%s)"
        #sql = 'select * from song'
        #curs.execute(sql,('test2','test2','test2'))        
        #curs.execute(sql)
        #print(curs.fetchone())
        conn.commit()

    #앨범 사진 크롤링

    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent','Mozilla/5.0')]

    urllib.request.install_opener(opener)

num = 1

for i in soup.find_all('a',class_='cover'):
    img_url = img_link1 + i.find('img').get('src') 
    img_name = i.find('img').get('alt')
    #print(img_url)
   # print(img_name+'.jpg')
    
    #파일로 저장 
    urllib.request.urlretrieve(img_url,'Gimg/' + str(num) + '.jpg')
    num = num +1

num = 51

for i in soup.find_all('a',class_='cover'):
    img_url = img_link1 +i.find('img').get('src')
    img_name = i.find('img').get('alt')
        #print(img_url)
        #print(img_name+'.jpg')

    #파일로 저장
    urllib.request.urlretrieve(img_url,'Gimg/' + str(num) + '.jpg')
    num = num +1


