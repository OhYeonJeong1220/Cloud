#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
import urllib.request
req = requests.get('https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01')

html = req.text

soup = BeautifulSoup(html,'html.parser')

#top_list = soup.select('#CHARTrealtime > table > tbody > tr')
#top_list2 = soup.select('#CHARTrealtime > table > tbody > tr')
f_song = open("bugs_song.txt","w") #노래 차트 텍스트 파일
f_singer = open("bugs_singer.txt","w") #가수 차트 텍스트 파일

title = [None]*100
n = 0

for i in soup.find_all('p',class_='title'):
    song = i.find('a')
    # print(song.text)
    data_song = "%s\n" % song.text
    f_song.write(data_song) #텍스트파일에 노래 이름 저장
    title[n] = song.text #배열에 노래 이름 저장
    n = n+1

#for i in top_list2:
 #   singer = i.find('td').find('p').find('a')
  #  print(singer.text)
   # data_singer = "%s\n" % singer.text
    #f_singer.write(data.singer)

m = 0
singer2 = [None]*100

for z in soup.find_all('p',class_='artist'):
    singer = z.find('a')
    data_singer = "%s\n" % singer.text
    f_singer.write(data_singer)
    singer2[m] = singer.text #배열에 가수 이름 저장
    m = m+1

#for i in range(0,100):
#    print("%d위 : %s - %s" %(i+1,title[i],singer2[i]))

#가사 크롤링(코딩할 땐 웬만하면 주석처리.. 오래걸려요)
#for i in soup.find_all('a', class_='trackInfo'):
#    lyrics_url = i.get('href')
#    req2 = requests.get(lyrics_url) #가사 url 요청
#    html2 = req2.text
#    soup_lyrics = BeautifulSoup(html2,'html.parser')
#    j = soup_lyrics.find('div',class_='lyricsContainer')
#    lyrics = j.find('xmp')
    #print(lyrics.text)

#앨범 사진 크롤링
num = 1
for i in soup.find_all('a',class_='thumbnail'):
    img_url = i.find('img').get('src')
#    img_name = i.find('img').get('alt')
#    print(img_url)
#    print(img_name)
    
    urllib.request.urlretrieve(img_url,str(num)+'.jpg')
    num = num+1
    #urllib.requests.urlretrieve(img_url,i.find('img').get('alt')+'.jpg')

#수록곡 크롤링
for i in soup.find_all('a', class_='album'):
    list_url = i.get('href')
    req3 = requests.get(list_url)   #수록곡 url 요청
    html3 = req3.text
    soup_list = BeautifulSoup(html3,'html.parser') # 수록곡 나오는 페이지로 이동
    # 각 앨범에 대해 수록곡들 크롤링
    for j in soup_list.find_all('p',class_='title'):
            list_song = j.find('a')
            if list_song:
                print(list_song.text)
