from  genie_crawling import G_matrix 
from  mellonchart import M_matrix
from bugs import B_matrix
from operator import itemgetter

I_matrix = [[0  for locix in range(5)] for y in range(300)]
num = 0
index = 0
I_index = 0

song1 = ''
song2 = ''
singer1=''
singer2=''
loc1=0
loc2=0
loc31=0
loc32=0
loc33=0
loc41=0
loc42=0
loc43=0
f= True
#Melon을 기준으로 Bugs와 비교
for i in range(0,100):
    for j in range(0,len(B_matrix)):
        #노래와 앨범 제목이 사이트마다 다르므로 사전 처리
        loc1=M_matrix[i][0].find('(')
        loc31=M_matrix[i][1].find('(')
        loc32=M_matrix[i][1].find('&')
        loc33=M_matrix[i][1].find(',')
        #print('loc1',loc1)
        #print('original:',M_matrix[i][0])
        if(loc1 > 0):
            original = M_matrix[i][0]
            song1 = original[:loc1]
            #print('song1:',song1)

        else:
            song1 = M_matrix[i][0]
        
        if((loc31>0)or(loc32>0)or(loc33>0)):
            original = M_matrix[i][1]
            if(loc31 == -1):
                if(loc32>0):
                    singer1=original[:loc32]
                else:
                    singer1=original[:loc33]
            else:
                singer1=original[:loc31]
        else:
            singer1=M_matrix[i][1]
            #elif(loc32 == -1):
                #singer1=original[:loc31]
            #elif((loc31 > 0 and loc32 >0)and(loc31 < loc32)):
                #singer1=original[:loc31]
            #elif((loc31 > 0 and loc32 >0)and(loc31 > loc32)):
                #singer1=original[:loc32]

        loc2=B_matrix[j][0].find('(')
        loc41=B_matrix[j][1].find('(')
        loc42=B_matrix[j][1].find('&')
        loc43=B_matrix[j][1].find(',')
        if(loc2 > 0):
            original =  B_matrix[j][0]
            song2 = original[:loc2]
        else:
            song2 = B_matrix[j][0]
        
        if((loc41>0)or(loc42>0)or(loc43>0)):
            original = B_matrix[j][1]
            if(loc41 == -1):
                if(loc42>0):
                    singer2=original[:loc42]
                else:
                    singer2=original[:loc43]
            else:
                singer2=original[:loc41]
        else:
            singer2=B_matrix[j][1]
            
            #elif(loc42 == -1):
                #singer2=original[:loc41]
            #elif((loc41 > 0 and loc42 >0)and(loc41 < loc42)):
                #singer2=original[:loc31]
            #elif((loc41 > 0 and loc42 >0)and(loc41 > loc42)):
                #singer2=original[:loc42]
        #if(i == 3 and j ==0):
           # print('song1:',song1)
           # print('singer1:',singer1)
           # print('song2:',song2)
           # print('singer2:',singer2) 
        
        if((song1.strip() == song2.strip()) and (singer1.strip()==singer2.strip())):
            
            #if(i == 3 and j ==0):
               # print('song1:',song1)
               # print('singer1:',singer1)

                #print('song2:',song2)
                #print('singer2:',singer2)

            #노래같으면 통합해서1개만 저장
            #print('11','song1:',song1)
            #print('singer1:',singer1)
            #print('11','song2:',song2)
            #print('singer2:',singer2)
            I_matrix[i][0] = M_matrix[i][0]
            I_matrix[i][1] = M_matrix[i][1]
            I_matrix[i][2] = M_matrix[i][2]
            I_matrix[i][3] = M_matrix[i][3] + M_matrix[i][4] + B_matrix[j][3]+B_matrix[j][4]#가중치와 순위를 곱해서 저장i
            #print('dvd:',I_matrix[i][3])
            #print('j:',j)
            index = j
            num = num + 1
        
    
    if(num == 0):
        #노래가 다를 때 mellon 노래 저장
        I_matrix[i][0] = M_matrix[i][0]
        I_matrix[i][1] = M_matrix[i][1]
        I_matrix[i][2] = M_matrix[i][2]
        I_matrix[i][3] = M_matrix[i][3] + M_matrix[i][4]
    
    else:
        #print(index)
        #print(B_matrix[index])
        del B_matrix[index]#mwllon과 같은 노래면 벅스 차트에서 노래 삭제
        
    num = 0


#for i in range(0,len(B_matrix)):
    #print(i+1,':',B_matrix[i])

#mellon 노래와 겹치는 노래 빼고 bugs 노래 저장
for i in range(100,100+len(B_matrix)):
    I_matrix[i][0] = B_matrix[i-100][0]
    I_matrix[i][1] = B_matrix[i-100][1]
    I_matrix[i][2] = B_matrix[i-100][2]
    I_matrix[i][3] = B_matrix[i-100][3]+B_matrix[i-100][4]
    

num = 0
index = 0

I_index = 100 + len(B_matrix)

#for i in range(0,I_index):
    #print(I_matrix[i])
#for i in range(0,I_index):
    #I_matrix[i][4] = i+1

#통합차트에서 같은 노래가 있는지 비교
for i in range(0,I_index):
    for j in range(0,len(G_matrix)):
        
        loc1 = I_matrix[i][0].find('(')
        loc31=I_matrix[i][1].find('(')
        loc32=I_matrix[i][1].find(',')
        #loc33=I_matrix[i][1].find(',')
       # print('original1:',I_matrix[i][0])
        if(loc1 > 0):
            original = I_matrix[i][0]
            song1 = original[:loc1]
            #print('song1:',song1)
        else:
            song1 = I_matrix[i][0]
        
        #if((loc31>0)or(loc32)or(loc33>0)):
            #original = I_matrix[i][1]
            #if(loc31 == -1):
                #if(loc32>0):
                    #singer1=original[:loc32]
                #else:
                #    singer1=original[:loc33]
            #else:
            #    singer1=original[:loc31]
        #else:
           # singer1 = I_matrix[i][1]

        if((loc31>0)or(loc32>0)):
            original = I_matrix[i][1]
            if(loc31 == -1):
                singer1=original[:loc32]
            elif(loc32 == -1):
                singer1=original[:loc31]
            elif((loc31 > 0 and loc32 >0)and(loc31 < loc32)):
                singer1=original[:loc31]
            elif((loc31 > 0 and loc32 >0)and(loc31 > loc32)):
                singer1=original[:loc32]
        else:
            singer1= I_matrix[i][1]
        loc2 = G_matrix[j][0].find('(')
        loc41=G_matrix[j][1].find('(')
        loc42=G_matrix[j][1].find('&')
    
        #print('original: ', G_matrix[j][0])
        if(loc2 > 0):
            original = G_matrix[j][0] 
            song2 = original[:loc2]
            #print('song2: ',song2)
        
        else:
            song2 = G_matrix[j][0]
        
        
        if((loc41>0)or(loc42>0)):
            original = G_matrix[j][1]
            if(loc41 == -1):
                singer2=original[:loc42]
            elif(loc42 == -1):
                singer2=original[:loc41]
            elif((loc41 > 0 and loc42 >0)and(loc41 < loc42)):
                singer2=original[:loc31]
            elif((loc41 > 0 and loc42 >0)and(loc41 > loc42)):
                singer2=original[:loc42]

        else:
            singer2= G_matrix[j][1]
        #if(song2 == "Into the Unknown"):
            #print('song1:',song1)
            #print('song2:',song2)
            #f = False
            #break
        if((song1.strip() == song2.strip())and (singer1.strip()==singer2.strip())):
            #지니에도 같은 노래가 있으면 가중치 값만 변경
            #print('22','song1:',song1)
            #print('22','song2:',song2)
            #print('sss*:',I_matrix[i][3])
            #print('gg:',G_matrix[j][3])
            #print('gg:',G_matrix[j][4])
            I_matrix[i][3] +=G_matrix[j][3] + G_matrix[j][4]
            #print('sss**:',I_matrix[i][3])
            index = j
            num = num +1
    #통합차트와 같은 노래면 지니 차트에서 삭제
    if(num > 0):
        del G_matrix[index]
    num = 0
    if(f == False):
        break
    
#통합차트와  겹치는 노래 빼고 ginie 노래 저장
for i in range(0,len(G_matrix)):
    I_matrix[I_index][0] = G_matrix[i][0]
    I_matrix[I_index][1] = G_matrix[i][1]
    I_matrix[I_index][2] = G_matrix[i][2]
    I_matrix[I_index][3] = G_matrix[i][3]+G_matrix[i][4]
    I_index = I_index +1


I_index = I_index + len(G_matrix)
I_matrix.sort(key=itemgetter(3), reverse=True)#3번째 원소로 정렬

#print('I_index' , I_index)

#print(I_matrix[0])
for i in range(0,100):
    print(i+1,'위 : ',I_matrix[i])

#I_matrx 전체  출력
#for x,y,z,r,b in I_matrix:
    #print(x,y,z,r,b)
