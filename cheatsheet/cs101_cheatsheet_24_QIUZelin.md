cheatsheet 2400011884 邱泽霖

队列操作

```python
import queue
q=queue.Queue()
q.put('加入元素')
a=q.get()#取出元素，先进先出
while not q.empty():#判断是否有元素
    break
```

deque

```python
from collections import deque
deque.append()
deque.appendleft()
deque.pop()
deque.popleft()
```

Time and Date

```python
import calendar, datetime
print(calander.isleap(2020))
print(datetime.datetime(2023,10,5).weekday())#输出星期几[0,星期一]
```

heapq

```python
import heapq
l=[1,2,3,4]
l.heapify()
l.heappush(5)
#若需要最大堆则使用相反数
```

permutation

```python
from itertools import permutations
for i in permutations([1,2,3,4]):
	print(i)
#dfs写法
def dfs(n,path,used,res):
    if len(path)==n:
        res.append(path[:])
        return
   for i in range(1,n+1):
    if not used[i]:
        used[i]=True
        path.append(i)
        dfs(n,path,used,res)
        path.pop()
        used[i]=False
def print_permutations(n):
    res=[]
    dfs(n,[],[False]*(n+1),res)
    for perm in sorted(res):
        print(' '.join(map(str,perm)))
```

defaultdict

```python
from collections import defaultdict
a=defaultdict(int)
```

冒泡排序

```python
list=[1,4,5,9,3,5,2,6]
for i in range(len(list)):
    for j in range(i):
        if list[i]<list[j]:
            list[i],list[j]=list[j],list[i]
print(list)
#输出[1, 2, 3, 4, 5, 5, 6, 9]
```

bfs

蟹

```python
import queue
dx=[1,0,-1,0]
dy=[0,1,0,-1]
n=int(input())
beach=[]
for i in range(n):
    beachp=list(map(int,input().split()))
    beach.append([])
    for j in range(n):
        beach[-1].append([beachp[j],True])
q=queue.Queue()
found=False
for i in range(n):
    for j in range(n):
        if beach[i][j][0]==5:
            q.put([i,j])
            try:
                if beach[i][j+1][0]==5:
                    crab=[0,1]
                else:
                    crab=[1,0]
            except:
                crab=[1,0]
            found=True
            break
    if found:
        break
reach=False
while not q.empty():
    t=q.get()
    x=t[0]
    y=t[1]
    beach[x][y][1]=False
    for k in range(4):
        xp=x+dx[k]
        yp=y+dy[k]
        xpc=xp+crab[0]
        ypc=yp+crab[1]
        if 0<=xp<n and 0<=yp<n and 0<=xpc<n and 0<=ypc<n and beach[xp][yp][1]:
            if beach[xp][yp][0]!=1 and beach[xpc][ypc][0]!=1:
                #print(xp,yp)
                #print(beach)
                if beach[xpc][ypc][0]==9 or beach[xp][yp][0]==9:
                    reach=True
                    break
                q.put([xp,yp])
    if reach:
        break
if reach:
    print('yes')
else:
    print('no')
```

剪枝bfs(变换的迷宫)

```python
import queue
T=int(input())
DX=[1,0,-1,0]
DY=[0,1,0,-1]
for i in range(T):
    R,C,K=map(int,input().split())
    ditu=[]
    q=queue.Queue()
    for i in range(R):
        ditup=input()
        ditu.append([])
        for j in range(C):
            if ditup[j]=='.':
                ditu[-1].append([0,0])
            elif ditup[j]=='S':
                ditu[-1].append([0,0])
                q.put([i,j])
            elif ditup[j]=='#':
                ditu[-1].append([1,0])
            elif ditup[j]=='E':
                ditu[-1].append([0,0])
                endpoint=[i,j]
    #print(ditu)
    tmin=[]
    while not q.empty():
        l=q.get()
        xn=l[0]
        yn=l[1]
        for d in range(4):
            xp=xn+DX[d]
            yp=yn+DY[d]
            t=ditu[xn][yn][1]+1
            if 0<=xp<R and 0<=yp<C:
                #print(xp,yp)
                if (ditu[xp][yp][0]==0 or (ditu[xp][yp][0]==1 and t%K==0)) and (-(t%K)-1 not in ditu[xp][yp]):
                    #print('A')
                    ditu[xp][yp][1]=t
                    ditu[xp][yp].append(-(t%K)-1)
                    q.put([xp,yp])
                    #print(ditu)
                if xp==endpoint[0] and yp==endpoint[1]:
                    tmin.append(t)
    if len(tmin)>0:
        print(min(tmin))
    else:
        print("Oop!")
```

dijkstra

```python
import heapq
def find_min_cost_path(n,m,mat,queries):
    directions=[(1,0),(0,1),(0,-1),(-1,0)]
    results=[]
    for x,y,xx,yy in queries:
        if mat[x][y] == '#' or mat[xx][yy]=='#':
            results.append('NO')
            continue
        dist={(x,y):0}
        heap=[(0,x,y)]
        found=False
        while heap:
            cost,i,j=heapq.heappop(heap)
            if (i,j)==(xx,yy):
                results.append(cost)
                found=True
                break
            for di,dj in directions:
                ni,nj=i+di,j+dj
                if 0<=ni<n and 0<=nj<m and mat[ni][nj]!='#':
                    new_cost=cost+abs(int(mat[ni][nj]-int(mat[i][j])))
                    if (ni,nj) not in dist or new_cost < dist[(ni,nj)]:
                        dist[(ni,nj)]=new_cost
                        heapq.heappush(heap,(new_cost,ni,nj))
       if not found:
           results.append("NO")
	return results
```

dp

小偷背包

```python
n,b=map(int, input().split())
price=[0]+[int(i) for i in input().split()]
weight=[0]+[int(i) for i in input().split()]
bag=[[0]*(b+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,b+1):
        if weight[i]<=j:
            bag[i][j]=max(price[i]+bag[i-1][j-weight[i]], bag[i-1][j])
        else:
            bag[i][j]=bag[i-1][j]
print(bag[-1][-1])
#遍历所有物品，并判断以前若干个物品为选择时每个质量可能的最大价值。
```

```python
N,B = map(int, input().split())
*p, = map(int, input().split())
*w, = map(int, input().split())

dp=[0]*(B+1)
for i in range(N):
    for j in range(B, w[i] - 1, -1):
        dp[j] = max(dp[j], dp[j-w[i]]+p[i])
            #对物品遍历，再从大到小遍历质量（从小到大应该也可以）
print(dp[-1])
```


