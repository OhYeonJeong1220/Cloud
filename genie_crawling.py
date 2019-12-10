import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
from datetime import datetime
#import pymysql
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse


##mysql ##
#conn = pymysql.connect(
#        host = '52.231.160.91',
#        user = 'oyj',
#        port = 3306,
#        password = '1234',
#        db = 'Cloud',
#        charset = 'utf8'
#        )

now=datetime.today()
#curs = conn.cursor()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.3'}#user info

G_matrix = [[0 for x in range(6)] for y in range(100)]#100*4리스트 생성
nt = now.hour + 9

hour = ''
print('nt:',nt)
if(nt > 24):
    nt=0
    hour = str(nt)
if(nt <10):
    hour = '0' +str(nt) 
if(nt>10 and nt<24):
    hour=str(nt)

#print('hour:',hour)
today = datetime.today().strftime("%Y%m%d")#오늘 날짜

#hour = '22'

hour = ''


if(nt == 24):
    nt = 0
    hour = str(nt)
if(nt <10):
    hour = '0' +str(nt)
if(nt>10 and nt <24):
    hour = str(nt)
print(hour)
today = datetime.today().strftime("%Y%m%d")#오늘 날짜


parts = urlparse('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20191206&hh=22&rtm=Y&pg=1')
#요소 분리
qs = dict(parse_qsl(parts.query))
#parse_sql의 결과를 딕셔너리로 캐스팅
qs['ymd'] = today
qs['hh'] = hour
#수정
parts = parts._replace(query=urlencode(qs))

new_url = urlunparse(parts)
print(new_url)
#print(qs)

http = 'https:'
img_link1 = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20191206&hh=22&rtm=Y&pg=1'
#top1-50 page 
img_link2 = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20191206&hh=22&rtm=Y&pg=2'
#top50-100 page

col = 0
#곡제목, 가수, 앨범 이름 크롤링
for n in range(1,3):
    #요소 분리
    parts_ = urlparse(new_url)
    #parse_sql의 결과를 딕셔너리로 캐스팅
    
    qs_ = dict(parse_qsl(parts_.query))
    #수정
    qs_['pg'] = n
    parts_ = parts_._replace(query=urlencode(qs_))
    link = urlunparse(parts_)

    resp = requests.get(link,headers = headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
    #print("page: ",n,"=====================================================")
    
    for song in songs:#노래 제못, 가수, 앨범
        title = song.find('td',{'class':'info'}).find('a',{'class':'title ellipsis'}).text

        #print(tit);
        singer = song.find('td',{'class':'info'}).find('a',{'class':'artist ellipsis'}).text
        album = song.find('td',{'class':'info'}).find('a',{'class':'albumtitle ellipsis'}).text
        tit=title.replace(',','');
        sing=singer.replace(',','&');
        alb=album.replace(',','');
        #2차원 배열에 곡제목, 가수, 앨범 이름 저장
        G_matrix[col][0]=tit.strip()
        G_matrix[col][1]=sing.strip()
        G_matrix[col][2]=alb.strip()
        G_matrix[col][3]=30#지분율
        G_matrix[col][4]= 100-col#순위
        col = col +1
        #print('col:',col)
        #sql  = "INSERT INTO  song (title,singer,albumName) VALUES (%s,%s,%s)"
        #sql = 'select * from song'
        #curs.execute(sql,('test2','test2','test2'))        
        #curs.execute(sql)
        #print(curs.fetchone())
        #conn.commit()
#if(__name__=="__main__"):
    #for i in range(0,100):
            #print(G_matrix[i])
#앨범 사진 크롤링

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent','Mozilla/5.0')]

urllib.request.install_opener(opener)

resp = requests.get(new_url,headers = headers)
soup = BeautifulSoup(resp.text, 'html.parser')

num = 0
j=0
for i in soup.find_all('a',class_='cover'):
    img_url = http + i.find('img').get('src') 
    img_name = G_matrix[num][2]
    #print(img_url)
    #print(img_name+'.jpg')
    
    #파일로 저장 
    urllib.request.urlretrieve(img_url,'Gimg/' + img_name + '.jpg')
    num = num +1
    
resp = requests.get(new_url,headers = headers)
soup = BeautifulSoup(resp.text, 'html.parser')

num = 50

for i in soup.find_all('a',class_='cover'):
    img_url = http +i.find('img').get('src')
    img_name = G_matrix[num][2]
    #print(img_url)
    #print(img_name+'.jpg')

    #파일로 저장
    urllib.request.urlretrieve(img_url,'Gimg/' + img_name + '.jpg')
    j=j+1
    num = num +1


