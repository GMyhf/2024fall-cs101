# 杂项

```python
print(bin(9)) #bin函数返回二进制，形式为0b1001
dict.items()#同时调用key和value
print(round(3.123456789,5)# 3.12346
print("{:.2f}".format(3.146)) # 3.15
a,b=b,a
dict.get(key,default=None) # 其中，my_dict是要操作的字典，key是要查找的键，default是可选参数，表示当指定的键不存在时要返回的默认值
ord() # 字符转ASCII
chr() # ASCII转字符
for index,value in enumerate([a,b,c]): # 每个循环体里把索引和值分别赋给index和value。如第一次循环中index=0,value="a" 
# 二进制转十进制
binary_str = "1010"
decimal_num = int(binary_str, 2) # 第一个参数是字符串类型的某进制数，第二个参数是他的进制，最终转化为整数
print(decimal_num)  # 输出 10
```

字符串比较大小：按位比较，两个字符串第一位字符的ASCII码谁大，字符串就大，不再比较后面的；第一个字符相同的情况下，就比第二个字符串，以此类推。

常见ASCII码的大小规则：0～9　<　A～Z　<　a～z

## 列表的常用操作

在列表的指定位置插入元素：listname.insert(index , obj)

根据索引值删除元素：del listname[index] 或 del listname[start : end]（不包括end）或 listname.pop(index)

根据元素值删除元素：listname.remove(obj)

查找元素：listname.index(obj , start , end)

## 字符串常用操作

全部大写：s.upper()	全部小写：s.lower()

首字母大写，其他全部小写：s.capitalize()	每个单词的首字母大写，其他全部小写：s.title()

查找子字符串：s.find(substring , start , end)（没有的话返回-1）	s.index(substring , start , end)

替换子字符串：new_string = old_string.replace(old_substring , new_substring , count)

字符串拆分：s.split(separator, maxsplit)

去除首尾指定字符：s.strip()（默认为空格）    前面补0到所需位数：s.zfill()

## 字典的常用操作

dict.items() dict.keys() dict.values()

del dict['a']    dict.get(key,default=None)   dict.pop(key,default=None)

## 欧拉筛

```python
def Euler_sieve(n):
    primes = [True for _ in range(n+1)]
    p = 2
    while p*p <= n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1
    primes[0]=primes[1]=False
    return primes
```

## 哈希表

求得一个数组最长的和为0的连续子序列的方法（实例为求最长平均值为a的字串）

```python
def longest_subarray_with_avg(arr, a):
    # 步骤 1: 将每个元素减去a
    diff = [x - a for x in arr]
    
    # 步骤 2: 使用哈希表存储前缀和
    prefix_sum = 0
    prefix_map = {0: -1}  # 前缀和为0时，起始索引为-1
    max_len = 0
    start_index = -1

    # 步骤 3: 遍历数组并计算前缀和
    for i in range(len(diff)):
        prefix_sum += diff[i]
        
        # 步骤 4: 如果前缀和已经出现过，计算子数组的长度
        if prefix_sum in prefix_map:
            length = i - prefix_map[prefix_sum]
            if length > max_len:
                max_len = length
                start_index = prefix_map[prefix_sum] + 1
        else:
            prefix_map[prefix_sum] = i
    
    # 返回最长子数组
    if max_len > 0:
        return arr[start_index:start_index + max_len]
    else:
        return []
```

# 拓展包

## math

```python
import math
print(math.ceil(1.5)) # 2
print(math.pow(2,3)) # 8.0
print(math.pow(2,2.5)) # 5.656854249492381
print(9999999>math.inf) # False
print(math.sqrt(4)) # 2.0
print(math.log(100,10)) # 2.0  math.log(x,base) 以base为底，x的对数
print(math.comb(5,3)) # 组合数，C53
print(math.factorial(5)) # 5！
# 判断完全平方数
import math
def isPerfectSquare(num):
    if num < 0:
        return False
    sqrt_num = math.isqrt(num)
    return sqrt_num * sqrt_num == num
print(isPerfectSquare(97)) # False
sqrt(num).is_integer()
```

## 年份与日期

```python
import calendar
print(calendar.isleap(2020)) # True
import datetime
print(datetime.datetime(2023,10,5).weekday()) # 3 (星期四)
```

n正好是一年天数m的k倍时应该是第k-1年的最后一天，所以应该用(n-1)//m而不是n//m

## counter

```python
from collections import Counter 
# O(n)
# 创建一个待统计的列表
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# 使用Counter统计元素出现次数
counter_result = Counter(data) # 返回一个字典类型的东西
# 输出统计结果
print(counter_result) # Counter({'apple': 3, 'banana': 2, 'orange': 1})
print(counter_result["apple"]) # 3
```

## itertools

```python
import itertools
my_list = ['a', 'b', 'c']
permutation_list1 = list(itertools.permutations(my_list))
permutation_list2 = list(itertools.permutations(my_list, 2))
combination_list = list(itertools.combinations(my_list, 2))
bit_combinations = list(itertools.product([0, 1], repeat=4))

print(permutation_list1)
# [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
print(permutation_list2)
# [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
print(combination_list)
# [('a', 'b'), ('a', 'c'), ('b', 'c')]
print(bit_combinations)
# [(0, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0), (0, 0, 1, 1), (0, 1, 0, 0), (0, 1, 0, 1), (0, 1, 1, 0), (0, 1, 1, 1), (1, 0, 0, 0), (1, 0, 0, 1), (1, 0, 1, 0), (1, 0, 1, 1), (1, 1, 0, 0), (1, 1, 0, 1), (1, 1, 1, 0), (1, 1, 1, 1)]
```

## defaultdict

defaultdict是Python中collections模块中的一种数据结构，它是一种特殊的字典，可以为字典的值提供默认值。当你使用一个不存在的键访问字典时，defaultdict会自动为该键创建一个默认值，而不会引发KeyError异常。

defaultdict的优势在于它能够简化代码逻辑，特别是在处理字典中的值为可迭代对象的情况下。通过设置一个默认的数据类型，它使得我们不需要在访问字典中不存在的键时手动创建默认值，从而减少了代码的复杂性。

使用defaultdict时，首先需要导入collections模块，然后通过指定一个默认工厂函数来创建一个defaultdict对象。一般来说，这个工厂函数可以是int、list、set等Python的内置数据类型或者自定义函数。

```python
from collections import defaultdict
from itertools import permutations
a = defaultdict(int)
for i in input():
    a[i] += 1
dicts = [a, b, c, d]
def check(word):
    for perm in permutations(dicts, len(word)):
        for i, d in enumerate(perm):
            if word[i] not in d:
                break
        else:
            return 'YES'
    else:
        return 'NO'
#对字符串，元组，列表，字典不进行格式化输出的话，全是以元组形式输出 ''.join(perm)
#字典只对键进行排列组合
aa = defaultdict(lambda:1)
print(aa['a']) # 1
```

```python
# 分类
from collections import defaultdict
n = int(input())
d = defaultdict(list)
for _ in range(n):
    name, para = input().split('-')
    if para[-1]=='M':
        d[name].append((para, float(para[:-1])/1000) )
    else:
        d[name].append((para, float(para[:-1])))
sd = sorted(d)
for k in sd:
    paras = sorted(d[k],key=lambda x: x[1])
    value = ', '.join([i[0] for i in paras])
    print(f'{k}: {value}')
# 计数器
text = "hello world"
char_count = defaultdict(int)
for char in text:
    char_count[char] += 1
print(dict(char_count))  # 输出: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```

# 区间问题

（1）区间合并：给出一堆区间，要求**合并**所有**有交集的区间** （端点处相交也算有交集）。最后问合并之后的**区间**。

【**步骤一**】：按照区间**左端点**从小到大排序。

【**步骤二**】：维护前面区间中最右边的端点为ed。从前往后枚举每一个区间，判断是否应该将当前区间视为新区间。

假设当前遍历到的区间为第i个区间 [li,ri]，有以下两种情况：

- li≤ed：说明当前区间与前面区间**有交集**。因此**不需要**增加区间个数，但需要设置 ed=max(ed,ri)。
- li>ed: 说明当前区间与前面**没有交集**。因此**需要**增加区间个数，并设置 ed=max(ed,ri)。

（2）选择不相交区间：给出一堆区间，要求选择**尽量多**的区间，使得这些区间**互不相交**，求可选取的区间的**最大数量**。这里端点相同也算有重复

【**步骤一**】：按照区间**右端点**从小到大排序。

【**步骤二**】：从前往后依次枚举每个区间。

假设当前遍历到的区间为第i个区间 [li,ri]，有以下两种情况：

- li≤ed：说明当前区间与前面区间有交集。因此直接跳过。
- li>ed: 说明当前区间与前面没有交集。因此选中当前区间，并设置 ed=ri。

（3）区间选点：给出一堆区间，取**尽量少**的点，使得每个区间内**至少有一个点**（不同区间内含的点可以是同一个，位于区间端点上的点也算作区间内） 同（2）

```python
l.sort(key=lambda x: x[0])
        d=l[0][1]
        ans=1
        for i in range(1,n):
            if l[i][0]<=d:
                if l[i][1]<d:
                    d=l[i][1]
            else:
                d=l[i][1]
                ans+=1
```

（4）区间覆盖：给出一堆区间和一个目标区间，问最少选择多少区间可以**覆盖**掉题中给出的这段目标区间

【**步骤一**】：按照区间左端点从小到大排序。

【**步骤二**】：**从前往后**依次枚举每个区间，在所有能覆盖当前目标区间起始位置start的区间之中，选择**右端点**最大的区间。

假设右端点最大的区间是第i个区间，右端点为 ri。

最后将目标区间的start更新成ri

```python
l.sort(key=lambda x:x[0])
i=0
left=1
ans=0
while left<=n
    right=1
    while i<=n-1 and l[i][0]<=left:
        right=max(right,l[i][1])
        i+=1
    left=right+1
    ans+=1
print(ans)
```

# 二分查找

bisect包

```python
import bisect
sorted_list = [1,3,5,7,9] #[(0)1, (1)3, (2)5, (3)7, (4)9]
position = bisect.bisect_left(sorted_list, 6)
print(position)  # 输出：3，因为6应该插入到位置3，才能保持列表的升序顺序

bisect.insort_left(sorted_list, 6)
print(sorted_list)  # 输出：[1, 3, 5, 6, 7, 9]，6被插入到适当的位置以保持升序顺序

sorted_list=(1,3,5,7,7,7,9)
print(bisect.bisect_left(sorted_list,7))
print(bisect.bisect_right(sorted_list,7))
# 输出：3 6
```

bisect_left:

```python
lo,hi=0,len(a)
while lo < hi:
	mid = (lo + hi) // 2
    if a[mid] < x:
        lo = mid + 1
    else:
        hi = mid
```

bisect_right:

```python
lo,hi=0,len(a)
while lo < hi:
    mid = (lo + hi) // 2
    if x < a[mid]:
        hi = mid
    else:
        lo = mid + 1
```

```python
from bisect import bisect_left
# 开餐馆
dp=[0]*(n+1)
for i in range(1,n+1):
	j=bisect_left(m,m[i-1]-k)
	dp[i]=max(dp[i-1],dp[j]+p[i-1])
```

# 排序

```python
l.sort(key=lambda x:(x[0],x[1]),reverse=True)
```

## 冒泡排序

```python
for i in range(n-1):
    for j in range(n-i-1):
        if l[j+1]+l[j]>l[j]+l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
```

```python
import functools
def rule(x,y):
    a,b=x+y,y+x
    if a>b:
        return -1
    elif a<b:
        return 1
    else:
        return 0
print(sorted(['4','2','1','2'],key=functools.cmp_to_key(rule))) #['4', '2', '2', '1']
```

## mergesort

```python
# 求排列的逆序数
ans=0
def mergesort(arr):
    global ans
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        mergesort(left)
        mergesort(right)
        li=ri=i=0
        while len(left)>li and len(right)>ri:
            if left[li]<=right[ri]:
                arr[i]=left[li]
                li+=1
            else:
                arr[i]=right[ri]
                ri+=1
                ans+=len(left)-li
            i+=1
        while len(left)>li:
            arr[i]=left[li]
            i+=1
            li+=1
        while len(right)>ri:
            arr[i]=right[ri]
            i+=1
            ri+=1
```

# dp

## 最长下降子序列

**Dilworth定理**，最小的链覆盖数等于最长反链长度

```python
#寻找最长下降子序列
dp=[1]*k
for i in range(1,k):
    for j in range(i):
        if h[i]<=h[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))
# 二分查找做法
from bisect import bisect_left
n=int(input())
h=list(map(int,input().split()))
h.reverse()
l=[]
for ht in h:
    position=bisect_left(l,ht)
    if position<len(l):
        l[position]=ht
    else:
        l.append(ht)
print(len(l))
```

```python
# 最大连续子序列和
dp = [0]*n
dp[0] = a[0]
for i in range(1, n):
    dp[i] = max(dp[i-1]+a[i], a[i])
print(max(dp))
```

## 背包问题

```python
# 0-1背包
bag=[[0]*(b+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,b+1):
        if weight[i]<=j:
            bag[i][j]=max(price[i]+bag[i-1][j-weight[i]], bag[i-1][j])
        else:
            bag[i][j]=bag[i-1][j]
```

```python
# 0-1背包 压缩矩阵/滚动数组 方法
dp=[0]*(B+1)
for i in range(N):
    for j in range(B, w[i] - 1, -1):
        dp[j] = max(dp[j], dp[j-w[i]]+p[i])
```

```python
# 0-1恰好型背包
dp=[[0]+[-1]*T for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,T+1):
        if t[i]<=j and dp[i-1][j-t[i]]!=-1:
            dp[i][j]=max(w[i]+dp[i-1][j-t[i]],dp[i-1][j])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[-1][-1])
```

多重背包

![image-20241226101013624](C:\Users\wudaoning\AppData\Roaming\Typora\typora-user-images\image-20241226101013624.png)

```python
# 零钱兑换
dp=[float('inf')]*(m+max(l))
for i in l:
    dp[i-1]=1
for j in range(m):
    if dp[j]!=float('inf'):
        for i in l:
            dp[j+i]=min(dp[j+i],dp[j]+1)
if dp[m-1]==float('inf'):
    print('-1')
else:
    print(dp[m-1])
```

```python
# 最长公共子序列
la=len(a)
lb=len(b)
dp=[[0]*(lb+1) for _ in range(la+1)]
for i in range(1,la+1):
    for j in range(1,lb+1):
        if a[i-1]==b[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[la][lb])
```

# dfs

```python
# Lake Counting 用栈实现
direction=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
ans=0
def dfs(x,y):
    stack=[(x,y)]
    while stack:
        x,y=stack.pop()
        if l[x][y]=='.':
            continue
        l[x][y]='.'
        for dirx,diry in direction:
            dx=x+dirx
            dy=y+diry
            if dx>=0 and dx<=n-1 and dy>=0 and dy<=m-1 and l[dx][dy]=='W':
                stack.append((dx,dy))
for i in range(n):
    for j in range(m):
        if l[i][j]=='W':
            dfs(i,j)
            ans+=1
```

```python
def dfs(x,y):
    field[x][y]='.'
    for k in range(8):
        nx,ny=x+dx[k],y+dy[k]
        if 0<=nx<n and 0<=ny<m and field[nx][ny]=='W':
            dfs(nx,ny)
```

```python
# 递归优化
# 被缓存的函数的参数必须是可哈希的，这意味着参数中不能包含可变数据类型，如列表或字典。
import sys
from functools import lru_cache
sys.setrecursionlimit(1 << 30)
@lru_cache(maxsize=None)
```

```python
# dfs+回溯 马走日
direction=[(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
ans=0
def dfs(x,y,n,m):
    global ans
    if len(used)==m*n:
        ans+=1
        return
    for dirx,diry in direction:
        dx=x+dirx
        dy=y+diry
        if dx>=0 and dx<=n-1 and dy>=0 and dy<=m-1 and (dx,dy) not in used:
            used.add((dx,dy))
            dfs(dx,dy,n,m)
            used.remove((dx,dy))
```

矩阵最大权值路径：复制记录路径的列表要用copy.deepcopy()

迷宫最大权值

```python
directions=[(0,1),(0,-1),(1,0),(-1,0)]
ans=float('-inf')
cnt=weight[0][0]
used=set()
used.add((0,0))
def dfs(x,y):
    global cnt,ans
    if x==n-1 and y==m-1:
        ans=max(ans,cnt)
        return
    for dx,dy in directions:
        nx=x+dx
        ny=y+dy
        if 0<=nx<=n-1 and 0<=ny<=m-1 and (nx,ny) not in used:
            if maze[nx][ny]==0:
                used.add((nx,ny))
                cnt+=weight[nx][ny]
                dfs(nx,ny)
                used.remove((nx,ny))
                cnt-=weight[nx][ny]
dfs(0,0)
print(ans)
```

滑雪

```python
dp=[[0]*c for _ in range(r)]
def dfs(x,y):
    global dp
    if dp[x][y]>0:
        return dp[x][y]
    for dx,dy in directions:
        nx=x+dx
        ny=y+dy
        if 0<=nx<=r-1 and 0<=ny<=c-1:
            if region[x][y]>region[nx][ny]:
                dp[x][y]=max(dp[x][y],dfs(nx,ny)+1)
    return dp[x][y]
ans=0
for i in range(r):
    for j in range(c):
        ans=max(ans,dfs(i,j))
print(ans+1)
```

# bfs

```python
from collections import deque
def bfs(x,y):
    if matrix[x][y]==1:
        return 0
    inq.add((x,y))
    q=deque()
    q.append((x,y))
    step=0
    while q:
        for _ in range(len(q)):
            front=q.popleft()
            for i in range(4):
                nx=front[0]+dx[i]
                ny=front[1]+dy[i]
                if matrix[nx][ny]==1:
                    return step+1
                if matrix[nx][ny]==0 and (nx,ny) not in inq:
                    inq.add((nx,ny))
                    q.append((nx,ny))
        step+=1
    return 'NO'
```

变换的迷宫

```python
def bfs(x,y):
    inq=set()
    inq.add((0,x,y))
    q=deque()
    q.append((0,x,y))
    while q:
        t,x,y=q.popleft()
        if maze[x][y]=='E':
            return t
        for dx,dy in directions:
            nx=x+dx
            ny=y+dy
            nt=(t+1)%k
            if 0<=nx<=r-1 and 0<=ny<=c-1 and (nt,nx,ny) not in inq and (maze[nx][ny]!='#' or nt==0):
                q.append((t+1,nx,ny))
                inq.add((nt,nx,ny))
    return 'Oop!'
```

## 使用heapq

```python
import heapq # 优先队列可以实现以log复杂度拿出最小（大）元素
lst=[1,2,3]
heapq.heapify(lst) # 将lst优先队列化
heapq.heappop(lst) # 从队列中弹出树顶元素（默认最小，相反数调转）
heapq.heappush(lst,element) # 把元素压入堆中
```

```python
import heapq
directions=[(0,1),(0,-1),(1,0),(-1,0)]
def bfs(x,y):
    pq=[(0,x,y)]
    inq=set()
    inq.add((x,y))
    while pq:
        time,x,y=heapq.heappop(pq)
        for dx,dy in directions:
            nx=x+dx
            ny=y+dy
            if 0<=nx<=n-1 and 0<=ny<=m-1 and (nx,ny) not in inq:
                if maze[nx][ny]=='a':
                    return time+1
                elif maze[nx][ny]=='@':
                    heapq.heappush(pq,(time+1,nx,ny))
                    inq.add((nx,ny))
                elif maze[nx][ny]=='x':
                    heapq.heappush(pq,(time+2,nx,ny))
                    inq.add((nx,ny))
    return 'Impossible'
```

### dijkstra

```python
import heapq
def dijkstra(n,edges,s,t):
    graph=[[] for _ in range(n)]
    for u,v,w in edges:
        graph[u].append((v,w))
        graph[v].append((u,w))
    pq=[(0,s)]
    visited=set()
    distances=[float('inf')]*n
    distances[s]=0
    while pq:
        distance,node=heapq.heappop(pq)
        if node==t:
            return distance
        if node in visited:
            continue
        visited.add(node)
        for neighbor,weight in graph[node]:
            if neighbor not in visited:
                new_distance=distance+weight
                if new_distance<distances[neighbor]:
                    distances[neighbor]=new_distance
                    heapq.heappush(pq,(new_distance,neighbor))
    return -1
n,m,s,t=map(int,input().split())
edges=[list(map(int,input().split())) for _ in range(m)]
print(dijkstra(n,edges,s,t))
```

走山路

```python
import heapq
directions=[(0,1),(0,-1),(1,0),(-1,0)]
def dijkstra(s1,s2,t1,t2):
    pq=[(0,s1,s2)]
    visited=set()
    distances=[[float('inf')]*n for _ in range(m)]
    distances[s1][s2]=0
    while pq:
        distance,x,y=heapq.heappop(pq)
        if x==t1 and y==t2:
            return distance
        if (x,y) in visited:
            continue
        visited.add((x,y))
        for dx,dy in directions:
            nx=x+dx
            ny=y+dy
            if 0<=nx<=m-1 and 0<=ny<=n-1 and matrix[nx][ny]!='#' and (nx,ny) not in visited:
                new_distance=distance+abs(int(matrix[nx][ny])-int(matrix[x][y]))
                if new_distance<distances[nx][ny]:
                    distances[nx][ny]=new_distance
                    heapq.heappush(pq,(new_distance,nx,ny))
    return 'NO'
```

# 经典题目

### 八皇后：dfs全排列

```python
l=[]
def function(s,n):
    if len(s)==n:
        l.append(s)
        return
    for i in range(1,n+1):
        if str(i) not in s and all(len(s)-j!=abs(i-int(s[j])) for j in range(len(s))):
            function(s+str(i),n)
function('',8)
for k in range(int(input())):
    print(l[int(input())-1])
```

### 开餐馆：dp+二分查找

```python
from bisect import bisect_left
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    m=list(map(int,input().split()))
    p=list(map(int,input().split()))
    dp=[0]*(n+1)
    for i in range(1,n+1):
        j=bisect_left(m,m[i-1]-k)
        dp[i]=max(dp[i-1],dp[j]+p[i-1])
    print(dp[n])
```

### 最大子矩阵：kadane算法

```python
def kadane(arr):
        max_end_here = max_so_far = arr[0]
        for x in arr[1:]:
            max_end_here = max(x, max_end_here + x)
            max_so_far = max(max_so_far, max_end_here)
        return max_so_far
for left in range(cols):
        temp = [0] * rows
        for right in range(left, cols):
            for row in range(rows):
                temp[row] += matrix[row][right]
            max_sum = max(max_sum, kadane(temp))
    return max_sum
```

### aggressive cows：二分查找

aggressive cows、河中跳房子：求最小间隔最大是多少

月度开销：最大开销最小是多少

```python
def can_reach(d):
    count=1
    cur=l[0]
    for i in range(1,n):
        if l[i]-cur>=d:
            count+=1
            cur=l[i]
    return count>=c

def binary_search():
    low=0
    high=(l[-1]-l[0])//(c-1)
    while low<=high:
        mid=(low+high)//2
        if can_reach(mid):
            low=mid+1
        else:
            high=mid-1
    return high
n,c=map(int,input().split())
l=sorted([int(input()) for _ in range(n)])
print(binary_search())
```

### 堆猪：辅助栈

```python
pig=[]
pigmin=[]
while True:
    try:
        s=input().split()
        if s[0]=='pop':
            if pig:
                pig.pop()
                if pigmin:
                    pigmin.pop()
        elif s[0]=='min':
            if pigmin:
                print(pigmin[-1])
        else:
            new_pig=int(s[1])
            pig.append(new_pig)
            if not pigmin:
                pigmin.append(new_pig)
            else:
                pig_min=pigmin[-1]
                pigmin.append(min(pig_min,new_pig))
    except EOFError:
        break
```

### 剪绳子

```python
heapq.heapify(a)
ans = 0
for i in range(n-1):
    x = heapq.heappop(a)
    y = heapq.heappop(a)
    z = x + y
    heapq.heappush(a, z)
    ans += z
```

### potions

```python
import heapq
n=int(input())
a=list(map(int,input().split()))
health=0
consumed=[]
for ai in a:
    health+=ai
    heapq.heappush(consumed,ai)
    if health<0:
        health-=consumed[0]
        heapq.heappop(consumed)
print(len(consumed))
```

### 熄灯问题

```python
from itertools import product
from copy import deepcopy
change={0:1,1:0}
m0=[[0,0,0,0,0,0,0,0]]
for _ in range(5):
    m0.append([0]+[int(x) for x in input().split()]+[0])
m0.append([0,0,0,0,0,0,0,0])
for t in product(range(2),repeat=6):
    m=deepcopy(m0)
    answer=[list(t)]
    for i in range(1,6):
        for j in range(1,7):
            if answer[i-1][j-1]:
                m[i][j]=change[m[i][j]]
                m[i-1][j]=change[m[i-1][j]]
                m[i+1][j]=change[m[i+1][j]]
                m[i][j-1]=change[m[i][j-1]]
                m[i][j+1]=change[m[i][j+1]]
        answer.append(m[i][1:7])
    if m[5][1:7]==[0,0,0,0,0,0]:
        for a in answer[:-1]:
            print(' '.join(map(str,a)))
```

### heapq+懒删除

```python
import heapq
from collections import defaultdict
q=int(input())
left=[]
right=[]
ldict=defaultdict(int)
rdict=defaultdict(int)
for _ in range(q):
    sign,l,r=input().split()
    l=int(l)
    r=int(r)
    if sign=='+':
        ldict[l]+=1
        rdict[r]+=1
        heapq.heappush(left,-l)
        heapq.heappush(right,r)
    else:
        ldict[l]-=1
        rdict[r]-=1
    while len(left)>0>=ldict[-left[0]]:
        heapq.heappop(left)
    while len(right)>0>=rdict[right[0]]:
        heapq.heappop(right)
    if len(left)>0 and len(right)>0 and right[0]<-left[0]:
        print('YES')
    else:
        print('NO')
```

### 无重复字符的最长字串

```python
n=len(s)
start=-1
ans=0
char={}
for i in range(n):
    if s[i] in char and char[s[i]]>start:
        start=char[s[i]]
    char[s[i]]=i
    ans=max(ans,i-start)
```

### 下k个排列

```python
for ki in range(k):
    i=n-2
    while i>=0 and l[i]>l[i+1]:
        i-=1
    if i>=0:
        j=n-1
        while l[j]<l[i]:
            j-=1
        l[i],l[j]=l[j],l[i]
    left=i+1
    right=n-1
    while left<right:
        l[left],l[right]=l[right],l[left]
        left+=1
        right-=1
print(*l)
```

