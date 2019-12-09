import requests
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
RANK=100
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.3'}
mellon=requests.get("https://www.melon.com/chart/index.htm",headers=headers)
soup=BeautifulSoup(mellon.text,"html.parser")

titles=soup.find_all('div',{'class':'ellipsis rank01'})
singers=soup.find_all('div',{'class':'ellipsis rank02'})
imgs=soup.find_all('a',{'class':'image_typeAll'})
alts=soup.find_all('a',{'class':'image_typeAll'})
albums=soup.find_all('div',{'class':'ellipsis rank03'})

title=[]
singer=[]
img=[]
alt=[]
name=[]
album=[]

M_matrix = [[0 for x in range(6)] for y in range(100)]#100*3 리스트 생성
col = 0

for t in titles:
    title.append(t.find('a').text.strip())  
for s in singers:
    singer.append(s.find('span',{'class':'checkEllipsis'}).text.strip())
for j in imgs:
    img.append(j.find('img')['src'])
for k in alts:
    alt.append(k.find('img')['alt'])
for t in range(RANK):
    name.append(t)
for a in albums:
    album.append(a.find('a').text.strip())

str = "hello,world".replace(',','&')


for i in range(0,100):
    tit=title[i].replace(',','')
    sing_n=singer[i].replace(',','&')
    album_n=album[i].replace(',','')
    M_matrix[i][0] = tit
    M_matrix[i][1] = sing_n
    M_matrix[i][2] = album_n
    #if(title[i].find(',')>0):
        #만약 제목에 ,가 있다면
        #print('title 수정:',title[i])
    
        #print('title:',title[i])
    #if(singer[i].find(',')>0):
        #만약 가수에 ,가 있다면
        #singer[i]
    #if(album[i].find(',')>0):
        #만약 앨범에 ,가 있다면
        #album[i].replace(',','&')
    M_matrix[i][3] = 45
    M_matrix[i][4] = 100-i

if(__name__ == "__main__"):    
    for i in range(0,100):
            print(M_matrix[i])


#for i in range(RANK):
    #print('%d title:%s singer:%s album:%s imgsrc:%s'%(i,title[i].strip(),singer[i].strip(),album[i].strip(),img[i].strip()))
    #urllib.request.urlretrieve(img[i],str(name[i])+'.jpg')
