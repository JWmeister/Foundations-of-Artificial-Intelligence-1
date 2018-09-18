import time
import timeit
import numpy as np
from itertools import combinations

import itertools
start = timeit.default_timer()
f=open('input.txt', 'r')
lines = f.read().splitlines()
n = int(lines[0])
p = int(lines[1])

nur = [[0 for col in range(n)]for row in range(n)]

for line in lines[3:len(lines)]:
     data =line.split(",")
     a = int(data[1])
     b = int(data[0])
     nur[a][b] += 1
ress=[]
for i in range(n):
     for j in range(n):
          ress.append(nur[i][j])
arr= np.array(ress).argsort()[-len(ress):][::-1]

cols = [False] * n
rows = [False] * n
dig = [False] * (2 * n - 1)
digs = [False] * (2 * n - 1)
ans=[]
maxpts=0

def classicSearch( n, p, extra, row, pts ) :
    global maxpts
    assert row<=n
    if(getIdealPts(pts,p)<maxpts):
        return
    if p<1:
        maxpts=max(pts,maxpts)
        return

    for offset in range(0, extra+1):
            realrow = row+offset
            for column in range(n):
                if realrow<n:
                    if cols[column]== False and rows[realrow]== False and dig[realrow + column]== False and digs[row - column + n - 1] == False:
                        cols[column] = rows[realrow] = dig[realrow + column] = digs[row - column+ n - 1] = True
                        #print realrow,column
                        updatepts= pts + nur[realrow][column]
                        classicSearch(n,p-1,extra-offset,realrow+1,updatepts)
                        cols[column] = rows[realrow] = dig[realrow + column] = digs[row - column + n - 1] = False
def getIdealPts(pts,p):
    usedrows= rows[:]
    for i in arr:
        y = i // n
        x= i % n
        if( p<1 ):
            break
        elif usedrows[y]==False and cols[x]== False and rows[y]== False and dig[x+ y]== False and digs[y - x + n - 1] == False:
            usedrows[y]=True
            pts+=nur[y][x]
    return pts
start = time.time()

classicSearch(n,p,n-p,0,0)

end = time.time()
b=start - end
print  b

