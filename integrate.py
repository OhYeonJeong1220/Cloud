from mellonlyrics import M_matrix
from genie_lyrics import G_matrix
from bugs import B_matrix
from operator import itemgetter

I_matrix = [[0  for x in range(6)] for y in range(300)]
num = 0
index = 0
I_index = 0

song1 = ''
song2 = ''

#Melon을 기준으로 Bugs와 비교
for i in range(0,100):
    for j in range(0,len(B_matrix)):
        #노래와 앨범 제목이 사이트마다 다르므로 사전 처리
        if(M_matrix[i][0].find('(') > 0):
            song1 = M_matrix[i][0].split('(')
        else:
           song1 = M_matrix[i][0]

        if(B_matrix[j][0].find('(') > 0):
            song2 = B_matrix[j][0].split('(')
        else:
            song2 = B_matrix[j][0]

        if(song1 == song2):
            #노래같으면 통합해서1개만 저장
            I_matrix[i][0] = M_matrix[i][0]
            I_matrix[i][1] = M_matrix[i][1]
            I_matrix[i][2] = M_matrix[i][2]
            I_matrix[i][3] = (M_matrix[i][3]*M_matrix[i][4]) + (B_matrix[j][3]*B_matrix[j][4])#가중치와 순위를 곱해서 저장i
            I_matrix[i][4] = M_matrix[i][5]
            index = j
            num = num + 1
        
        
    if(num == 0):
        #노래가 다를 때 mellon 노래 저장
        I_matrix[i][0] = M_matrix[i][0]
        I_matrix[i][1] = M_matrix[i][1]
        I_matrix[i][2] = M_matrix[i][2]
        I_matrix[i][3] = M_matrix[i][3]*M_matrix[i][4]
        I_matrix[i][4] = M_matrix[i][5]
    else:
        del B_matrix[index]#mwllon과 같은 노래면 벅스 차트에서 노래 삭제
    num = 0

#mellon 노래와 겹치는 노래 빼고 bugs 노래 저장
for i in range(100,100+len(B_matrix)):
    I_matrix[i][0] = B_matrix[i-100][0]
    I_matrix[i][1] = B_matrix[i-100][1]
    I_matrix[i][2] = B_matrix[i-100][2]
    I_matrix[i][3] = B_matrix[i-100][3]*B_matrix[i-100][4]
    I_matrix[i][4] = B_matrix[i-100][5]

num = 0
index = 0

I_index = 100 + len(B_matrix)


for i in range(0,I_index):
    I_matrix[i][4] = i+1

#통합차트에서 같은 노래가 있는지 비교
for i in range(0,I_index):
    for j in range(0,len(G_matrix)):
        if(I_matrix[i][0].find('(') > 0):
            song1 = I_matrix[i][0].split('(')

        else:
            song1 = I_matrix[i][0]

        if(G_matrix[j][0].find('(') > 0):
            song2 = G_matrix[j][0].split('(')

        else:
            song2 = G_matrix[j][0]

        if((song1 == song2)):
            #지니에도 같은 노래가 있으면 가중치 값만 변경
            I_matrix[i][3] =  I_matrix[i][3] + (G_matrix[j][3]*G_matrix[j][4])
            index = j
            num = num +1
    #통합차트와 같은 노래면 지니 차트에서 삭제
    if(num > 0):
        del G_matrix[index]
    num = 0


#통합차트와  겹치는 노래 빼고 ginie 노래 저장
for i in range(0,len(G_matrix)):
    I_matrix[I_index][0] = G_matrix[i][0]
    I_matrix[I_index][1] = G_matrix[i][1]
    I_matrix[I_index][2] = G_matrix[i][2]
    I_matrix[I_index][3] = G_matrix[i][3]*G_matrix[i][4]
    I_matrix[I_index][4] = G_matrix[i][5]
    I_index = I_index +1


I_index = I_index + len(G_matrix)
I_matrix.sort(key=itemgetter(3), reverse=True)#3번째 원소로 정렬

print('I_index' , I_index)

#print(I_matrix[0])
for i in range(0,100):
    print(i+1,'위 : ',I_matrix[i])

#I_matrx 전체  출력
#for x,y,z,r,b in I_matrix:
    #print(x,y,z,r,b)
