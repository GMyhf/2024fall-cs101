# CheatSheet

Updated 2028 GMT+8 Dec 25,2024

Compiled by HUJingyao

## **基本格式**

1. 浮点数保留几位小数输出：number是变量

```python
print('{:.1f}'.format(number))
print(f’{number:.1f}’)
```

2. 正无穷大：float(‘inf’) 负无穷大：float(‘-inf’)
3. def一般写在最前面保证可读性 主函数写后面
4. 创建二维数组

 ```python
 m,n=map(int,input().split())
 a=[[0]*n for i in range(m)]
 a=[0 for i in range(n) for j in range(m)]
 ```

5. return可以通过表达式来隐性判断True/False

```python
return n % 2 == 0    return nun>m
```

   6.迭代器 一次遍历

```python
*a, = map(int, input().split()) 相当于 a = list(map(int, input().split())) 转换成列表
a = map(int, input().split()) 是一个迭代器
h.append([10001] + list(map(int, input().split())) + [10001]) 正确
h.append([10001] + [map(int, input().split())] + [10001]) 错误
```

   7.字典初始化 dict={}  集合初始化 c=set() 或者c={1,2,3}

   8.调用主程序

```python
def main():
    ...
if __name__=='__main__':
    main()
```

   9.函数返回值

```python
def print_greeting(name):
    print(f"Hello, {name}!")
print(print_greeting("Bob"))
Hello, Bob!  #调用函数的输出
None  #打印返回值的输出
```

```python
def process_data(data):
    if not data: #数据为空 
        return #提前退出函数 直接调用函数并不会有输出 因为函数内部没有print('None') 只有print(process_data)才会输出None
    print('process data...')
```

10.f-string 格式化字符串字面量

```python
print(f"You {'passed' if score >= 60 else 'failed'} the exam.")
print(f"Hello, my name is {name} and I am {age} years old.")
```

   11.接收一组数字 输出这些数字按升序排列后原来的位置

```python
a=list(map(int,input().split()))
b=range(len(a))
c=sorted(b,key=lambda[i]:a[i])
d=[str(i+1) for i in c]
e=' '.join(d)
```

```python
t=sorted(enumerate(input().split(),1),key=lambda x:int(x[1]))
ans=[i[0] for i in t]
print(*ans)
```

   12.*解包操作

```python
ans=[1,2,3,4,5]
print(*ans) #输出：1 2 3 4 5
print(*ans,sep=',') #输出：1，2，3，4，5
```

   13.循环控制语句

```python
break #完全退出循环
continue #进入下一次循环
pass #占位符
exit() #退出整个程序
```

## 特殊输入输出处理

1.输入多组数据同时输出多组数据：用while True:创建一个无限循环

 ```python
 while True:
     n, m = map (int,input(). split())
     if n == 0 and m == 0:  #输入0 0表示结束
         break
     print (joseph(n, m))
 ```

2.不定行输入

```python
#使用 try-except 捕获 EOFError
try:
    while True:
        line = input()
        lines.append(line)
except EOFError:
    pass
```

```python
#快速堆猪
while True:
    try:
        s=input().split()
        if s[0]=='pop':
            if a:
                a.pop()
                if m:
                    m.pop()
        elif s[0]=='min':
            if m:
                print(m[-1])
        else:
            h=int(s[1])
            a.append(h)
            if not m:
                m.append(h)
            else:
                k=m[-1]
                m.append(min(k,h))
    except EOFError:
        break
```

3.一次性读取

```python
import sys
input=sys.stdin.readline
```

## 内置方法和函数

1.列表：sort() 和sorted()

```python
list.sort(key=None, reverse=False) #直接修改原列表 默认升序 reverse=True降序
words = ['apple', 'banana', 'cherry', 'date']
words.sort(key=len) #按字符串长度排序
a=sorted(list) #返回一个新的列表 不改变原始对象
```

2.列表：append() extend()

```python
numbers = [1, 2, 3]
more_numbers = [4, 5, 6]
numbers.extend(more_numbers)
print(numbers)  # 输出: [1, 2, 3, 4, 5, 6]
numbers.append(more_numbers)
print(numbers)  # 输出: [1, 2, 3, [4, 5, 6]]
```

3.匿名函数 lambda表达式

```python
sorted_data = sorted(data, key=lambda x: x['age'])
data = [1, 2, 3, 4, 5]
result = list(map(lambda x: x**2, data))
#与filter()函数结合返回一个【迭代器】
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出: [2, 4, 6]
```

4.enumerate() 获取元素及索引

```python
for index,fruit in enumerate(fruits):
for index,fruit in enumerate(fruits,start=1):
    print(index,fruit)
#生成的是迭代器 可以转换成列表
en_fruits=list(enumerate(fruits))
```

5.字典：setdefault()和get() 

```python
get()：仅获取键的值，如果键不存在则返回默认值，但不会修改字典。
setdefault()：如果键不存在，则会将键添加到字典中并设置默认值。
c[(p,q)]=c.setdefault((p,q),0)+i
```

6.字典：values() keys() items()

```python
a=list(c.values())
```

7.字符串、列表：count()

```python
string.count('l')   lst.count(s)
```

8.字符串：strip() lstrip() rstrip() split()

```python
text.strip() #默认移除空白字符 如开头结尾的空格
text.strip('.') #指定移除.   
a=list(map(int,input().strip().split()))
```

9.字符串：join()

```python
a=[(1,A),(2,B),(3,C)]
b=[num for num,letter in a] 
ans=' '.join(map(str,b))
```

10.集合 remove(element) 列表 del list[index] remove(value) pop()

11.bin(n) 用于将整数 n 转换为其二进制表示的字符串。以 '0b' 为前缀，表示这是一个二进制数。通过切片操作去掉前缀：s = bin(n)[2:]

##  模块

#### 注意：引入整个模块时需要有模块名前缀 导入特定的类或函数就不用

```python
import collections
q=collections.deque()
from collections import deque
q=deque()
```

####  1.copy 浅拷贝和深拷贝

```python
import copy
a=[1,2,3]
b=a #浅拷贝
c=copy.copy(a) #浅拷贝
d=copy.deepcopy(a) #深拷贝
```

```python
#熄灯问题 深拷贝
import copy
......
A = copy.deepcopy(X)
B = copy.deepcopy(Y)
```

####   2.math

```python
import math
a=math.ceil(3.14)
math.ceil(x)  math.floor(x)  math.trunc(x) 返回x的整数部分  math.pow(x, y) 返回x的y次幂
math.sqrt(x) 返回x的浮点数平方根  math.isqrt(x) 返回x的整数平方根 math.log(x[, base]) 返回以base为底的对数，默认是e
```

####   3.itertools

```python
#手搓前缀和
def pre_sum(lst):
    pre_sums=[]
    cur_sum=0
    for num in lst:
        cur_sum+=num
        pre_sums.append(cur_sum)
    return pre_sums
#计算前缀和
import itertools
import operator
numbers=[1,2,3,4,5]
pre_sum=list(itertools.accumulate(numbers))
#自定义前缀积
pre_pro=list(itertools.accumulate(numbers,func=operator.mul))
#自定义最大值
pre_max=list(itertools.accumulate(numbers,func=max)
```

```python
#计算笛卡尔积 两个或多个集合的所有可能的有序组合 注意直接生成的都是迭代器
import itertools
cartesian_product = list(itertools.product(list_a, list_b))
cartesian_product_repeated = list(itertools.product([1, 2], repeat=2)) #和自身作笛卡尔积
```

```python
#排列
from itertools import permutations
elements=['a','b','c']
p1=list(permutations(elements))
p2=list(permutations(elements,2))
print(' '.join(p1))
```

#### 4.collections

```python
#deque 双端队列 从前端后端添加删除元素
from collections import deque
d=deque()
d.append(i)        d.pop(i)
d.appendleft(j)    d.popleft(j)
#defaultdict 访问一个不存在的键时会自动创建 默认赋值 e.g.list-空列表 int-0
from collections import defaultdict
d=defaultdict(int)
d[i]+=1
```

#### 5.heapq

```python
#heapq 堆 优先队列 默认最小堆 取负值实现最大堆
import heapq
heap=[]
heapq.heappush(heap,1)
min_element=heapq.heappop(heap)
data=[1,3,2,4]
heapq.heapify(data)
```

```python
#In Love
import sys
import heapq
from collections import defaultdict
input=sys.stdin.readline
minh=[] #最小堆 现存区间右端点的最小值
maxh=[] #取反最大堆 现存区间左端点的最大值
ldict=defaultdict(int)
rdict=defaultdict(int)
n=int(input())
for _ in range(n):
    op,l,r=map(str,input().strip().split())
    l,r=int(l),int(r)
    if op=='+':
        ldict[l]+=1
        rdict[r]+=1
        heapq.heappush(maxh,-l)
        heapq.heappush(minh,r)
    else:
        ldict[l]-=1
        rdict[r]-=1
#清理堆中无效的元素 堆不空时 查看堆顶元素对应的计数值 若为0则pop
    while len(maxh)>0>=ldict[-maxh[0]]:
        heapq.heappop(maxh)
    while len(minh)>0>=rdict[minh[0]]:
        heapq.heappop(minh)
    if len(maxh)>0 and len(minh)>0 and minh[0]<-maxh[0]:
        print('yes')
    else:
        print('no')
```

#### 6.stack

```python
#滑雪 辅助栈
r,c=map(int,input().split())
h=[]
h.append([10001 for _ in range(c+2)])
for _ in range(r):
    h.append([10001]+list(map(int,input().split()))+[10001])
h.append([10001 for _ in range(c+2)])
dp=[[1]*(c+2) for _ in range(r+2)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
stack=[]
for i in range(1,r+1):
    for j in range(1,c+1):
        stack.append((h[i][j],i,j)) #先把整个数组压入栈中
stack.sort(reverse=True) #从大到小处理 reverse=True是降序
for high,x,y in stack:
    for k in range(4):
        if h[x+dx[k]][y+dy[k]]<h[x][y]:
            dp[x+dx[k]][y+dy[k]]=max(dp[x+dx[k]][y+dy[k]],dp[x][y]+1) 
 #从高处向低处移动时，当前高度较高的位置 (x, y) 已经计算好了它的最大路径长度 dp[x][y]，所以可以安全地用它来更新较低的位置。
ans=0
for i in range(1,r+1):
    for j in range(1,c+1):
        ans=max(ans,dp[i][j])
print(ans)
```

#### 7.functools

```python
from functools import lru_cache #缓存
@lru_cache(maxsize=None/4096/2048/1024/...)
def function_a():
```

 ```python
 from functools import cmp_to_key #将一个比较函数转换为键函数
 def compare_tuples(a,b):
     if a[1]<b[1]:
         return -1
     elif a[1]>b[1]:
         return 1
     else:
         return 0
 tuples = [(1, 'c'), (2, 'a'), (3, 'b')]
 sorted_tuples = sorted(tuples, key=cmp_to_key(compare_tuples))
 ```

```python
#病人排队
from functools import cmp_to_key
def cmp(x,y):
    if x[0]>=60 and y[0]>=60:
        return x[0]-y[0] #x,y都是老年人时按照大小比较
    if x[0]>=60 and y[0]<60:
        return 1 #x在前
    if x[0]<60 and y[0]>=60:
        return -1 #y在前
    return 0 #表示顺序不变
n=int(input())
p=[]
for _ in range(n):
    i,a=input().split()
    a=int(a)
    p.append((a,i))
p.sort(key=cmp_to_key(cmp),reverse=True)
for x in p:
    print(x[1]) 
```

## 算法

#### 矩阵*

```python
#加保护圈 假币问题
r,c=map(int,input().split())
h=[]
h.append([10001 for _ in range(c+2)])
for _ in range(r):
    h.append([10001]+list(map(int,input().split()))+[10001])
h.append([10001 for _ in range(c+2)])
```

```python
#range中使用min max 垃圾炸弹
d=int(input())
n=int(input())
c={}
for i in range(n):
    x,y,i=map(int,input().split())
    for p in range(max(0,x-d),min(1024,x+d)+1): #对每一个垃圾点枚举所有可能的炸弹投放点 max min防止越界
        for q in range(max(0,y-d),min(1024,y+d)+1):
            c[(p,q)]=c.setdefault((p,q),0)+i
a=list(c.values())
s=max(a)
print(a.count(s),s)
```

#### 双指针

```python
#接雨水
ans=0
left,right=0,len(height-1)
lmax=rmax=0
while left<right:
    lmax=max(lmax,height[left])
    ramx=max(rmax,height[right])
    if height[left]<height[right]:
        ans+=lmax-height[left]
        left+=1
    else:
        ans+=rmax-height[right]
        right-=1
print(ans)
```

#### 二分查找

```python
a=list(map(int,input().split()))
low=0
high=len(a）
while low<high:
    mid=(low+high)//2
    if a[mid]<x:
        low=mid+1
    else:
        high=mid-1
print(low)
```

```python
#河中跳房子 max(min)
L,N,M=map(int,input().split())
stones=[0]
for _ in range(N):
    stones.append(int(input()))
stones.append(L)
left,right=0,L
while left<right:
    mid=(left+right)//2
    cnt,pos=0,0
    for i in range(1,len(stones)):
        if stones[i]-stones[pos]<mid:
            cnt+=1
        else:
            pos=i
    if cnt>M:
        right=mid
    else:
        left=mid+1
print(left-1)
```

```python
#aggressive cows max(min)
n,c=map(int,input().split())
stalls=[]
for _ in range(n):
    stalls.append(int(input()))
stalls.sort()

left,right=0,(stalls[n-1]-stalls[0])//(c-1)
while left<right:
    cnt, pos = 0, 0
    mid=(left+right)//2
    for i in range(1,n):
        if stalls[i]-stalls[pos]<mid:
            cnt+=1
        else:
            pos=i
    if cnt>n-c:
        right=mid
    else:
        left=mid+1
print(left-1)
```

```python
#月度开销 min(max)
n,m=map(int,input().split())
exp=[]
for _ in range(n):
    exp.append(int(input())) #先把序列给放进来
def check(x):
    num,sum=1,0 #num是组数 sum是一段的总花销
    for i in range(n):
        if sum+exp[i]>x: #超过了规定的x就计数并重开
            num+=1
            sum=exp[i]
        else:
            sum+=exp[i] #没超就加入
    return num>m
lo=max(exp)
hi=sum(exp)
while lo<hi:
    mid=(lo+hi)//2
    if check(mid): #如果num>m说明mid定小了
        lo=mid+1
    else:
        hi=mid-1
print(lo) #最终会收敛到一个值
```

```python
#拦截导弹bisect做法 寻找最长不增子序列
from bisect import bisect_right
def max_intercepted(scores):
    scores.reverse()  # 反转序列 因为bisect要求递增序列！
    lis=[]  # 用于存储最长不减子序列
    for score in scores:
        pos=bisect_right(lis,score)
        if pos<len(lis):
            lis[pos]=score #确保 lis 数组中的每个元素都是当前长度的最长递增子序列的末尾元素的最小值。
        else:
            lis.append(score)
    return len(lis)
k=int(input())
scores=list(map(int,input().split()))
print(max_intercepted(scores))
#求最长不升，可以相等，所以用bisect_right。如果不能相等，用bisect_left
```

#### greedy

```python
#买卖股票的最佳时机
minprice=int(1e9)
maxprofit=0
for price in prices:
    maxprofit=max(maxprofit,price-minprice)
    minprice=min(minprice,price)
print(maxprofit)
```

```python
#跳跃游戏
def canJump(nums):
    n,rightmost=len(nums),0
    for i in range(n):
        if i<=rightmost:
            rightmost=max(rightmost,i+nums[i])
            if rightmost>=n-1:
                return True
    return False
print(canJump(nums))
```

```python
#跳跃游戏II
nums=list(map(int,input().split()))
n=len(nums)
maxpos,end,step=0,0,0
for i in range(n-1):
    if maxpos>=i:
        maxpos=max(maxpos,i+nums[i]) #在得到一个maxpos之后看它之前一段的数字能够达到的最远距离作为下一个end
        if i==end:
            end=maxpos #维护一定的步数能够到达的最远位置
            step+=1
print(step)
```

```python
#划分字母区间
s=str(input())
last=[0]*26
for i,ch in enumerate(s):
    last[ord(ch)-ord('a')]=i
partition=list()
start=end=0
for i,ch in enumerate(s):
    end=max(end,last[ord(ch)-ord('a')])
    if i==end:
        partition.append(end-start+1)
        start=end+1
print(partition)
```

```python
#世界杯只因
def min_cameras(n,ranges):
    pt=0 #指针 上一个的最远位置
    num=0
    mx=max(ranges)
    while pt<n:
        nxt=pt+ranges[pt]+1 #下一个的最远位置
        for i in range(max(0,pt-mx),min(n,pt+mx+1)):
            if 0<=i<n and i-ranges[i]<=pt and i+ranges[i]+1>nxt:
                nxt=i+ranges[i]+1
        num+=1
        pt=nxt
    return num
n=int(input())
ranges=list(map(int,input().split()))
print(min_cameras(n,ranges))
```

#### dp

```python
#核电站 最长连续长度限制
n,m=map(int,input().split())
dp=[0]*(n+1)
dp[0]=1
for i in range(1,n+1):
    if i<m:
        dp[i]=dp[i-1]*2
    elif i==m:
        dp[i]=dp[i-1]*2-1
    else:
        dp[i]=dp[i-1]*2-dp[i-m-1] #对于(i-1)的情况，最后(m-1)个一定放了，倒数第m个一定没放
print(dp[n])       
```

```python
#拦截导弹
def max_intercepted(k,heights):
    dp=[1]*k #dp[i] 表示以第i个导弹为结尾的最长非递增子序列的长度
    for i in range(1,k):
        for j in range(i):
            if heights[i]<=heights[j]:
                dp[i]=max(dp[i],dp[j]+1)
    return max(dp)
k = int(input())
heights = list(map(int, input().split()))
print(max_intercepted(k, heights))
```

```python
#变形 leetcode矩阵
m,n=len(matrix),len(matrix[0])
        dist=[[10**9]*n for i in range(m)]
......  for i in range(m-1,-1,-1): #注意向下移动需要先算出i+1的数据 所以是range(m-1,-1,-1)倒序遍历
            for j in range(n):
                if i+1<m:
                    dist[i][j]=min(dist[i][j],dist[i+1][j]+1)
                if j+1<n:
                    dist[i][j]=min(dist[i][j],dist[i][j-1]+1)
        return dist
```

```python
#打家劫舍 不能同时选连续两个
nums=list(map(int,input().split()))
if not nums:
    return 0
size=len(nums)
if size==1:
    print(nums[0])
dp=[0]*size
dp[0]=nums[0]
dp[1]=max(nums[0],nums[1])
for i in range(2,size):
    dp[i]=max(dp[i-2]+nums[i],dp[i-1])
print(dp[size-1])
#滚动数组
first,second=nums[0],max(nums[0],nums[1])
for i in range(2,size):
    first,second=second,max(first+nums[i],second)
print(second)
```

```python
#完全平方数
import math
n=int(input())
dp=[float('inf')]*(n+1)
dp[0]=0
for i in range(1,n+1):
    for j in range(1,int(math.sqrt(i)+1)):
        dp[i]=min(dp[i],dp[i-j*j]+1)
print(dp[n])
```

```python
#乘积最大子数组 因为有负数所以要同时维护最大最小值
maxf=minf=ans=nums[0]
for i in range(1,len(nums)):
    mx,mn=maxf,minf #保留旧值
    maxf=max(mx*nums[i],nums[i],mn*nums[i])
    minf=min(mx*nums[i],nums[i],mn*nums[i])
    ans=max(maxf,ans)
print(ans)
```

```python
#编辑距离 插入 删除 替换
n=len(a)
m=len(b)
if n*m==0:
    print(n+m)
dp=[[0]*(m+1) for _ in range(n+1)] #dp[i][j]表示a的前i个字母和b的前j个字母的编辑距离
for i in range(n+1):
    dp[i][0]=i
for j in range(m+1):
    dp[0][j]=j
for i in range(1,n+1):
    for j in range(1,m+1):
        r,s,t=dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]
        if a[i-1]!=b[j-1]:
            t+=1 #替换
        dp[i][j]=min(r,s,t)
print(dp[n][m])
```

```python
#宠物小精灵之收服 二维费用01背包
n,m,k=map(int,input().split())
pokemon=[]
for _ in range(k):
    balls,damage=map(int,input().split())
    pokemon.append((balls,damage))
pokemon.sort(key=lambda x:x[1])
dp=[[0,0] for _ in range(n+1)]
for balls,damage in pokemon:
    for i in range(n,balls-1,-1):
        pre_num,pre_damage=dp[i-balls]
        if pre_damage+damage>=m:
            continue
        if pre_num+1>dp[i][0]:
            dp[i]=[pre_num+1,pre_damage+damage]
        elif pre_num+1==dp[i][0]:
            dp[i][1]=min(dp[i][1],pre_damage+damage)
max_cap,tot_da=dp[-1]
print(max_cap,m-tot_da)
```

#### dfs

```python
#核电站
from functools import lru_cache
@lru_cache(maxsize=None)
def dfs(i,j,n,m): #i表示正在处理的位置，j表示最近一段连续放置的个数
    if j==m:
        return 0
    if i==n:
        return 1 #表示可以到达第n个，方法数+1
    no_place=dfs(i+1,0,n,m) #不放
    place=dfs(i+1,j+1,n,m) #放
    return no_place+place
n,m=map(int,input().split())
print(dfs(0,0,n,m))
```

```python
#滑雪
r,c=map(int,input().split())
h=[]
h.append([10001 for _ in range(c+2)])
for _ in range(r):
    h.append([10001]+list(map(int,input().split()))+[10001])
h.append([10001 for _  in range(c+2)])
dp=[[1]*(c+2) for _ in range(r+2)] #dp记录的就是从当前位置开始的最长递减路径
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def dfs(i,j):
    if dp[i][j]>1: #记忆化 检查是否已经计算过
        return dp[i][j] #如果计算过就返回结果
    for k in range(4): #将四个方向都试一遍 max中的dp[i][j]就是前面已经试过的最大值
        if h[i+dx[k]][j+dy[k]]<h[i][j]:
            dp[i][j]=max(dp[i][j],dfs(i+dx[k],j+dy[k])+1) #递归 一直找直到不能再往下走
    return dp[i][j] #记得return
ans=1
for i in range(1,r+1):
    for j in range(1,c+1):
        ans=max(ans,dfs(i,j)) #遍历dp数组 找最大值
print(ans)
```

#### bfs

```python
#LC矩阵
from collections import deque
m,n=len(matrix),len(matrix[0])
dist=[[0]*n for i in range(m)]
zeroes_pos=[(i,j) for i in range(m) for j in range(n) if matrix[i][j]==0]
q=deque(zeroes_pos)
visited=set(zeroes_pos)
while q:
    i,j=q.popleft()
    for ni,nj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
        if 0<=ni<m and 0<=nj<n and (ni,nj) not in visited:
            dist[ni][nj]=dist[i][j]+1
            q.append((ni,nj))
            visited.add((ni,nj))
```

```python
#螃蟹采蘑菇
from collections import deque
n=int(input())
maze=[list(map(int,input().split())) for _ in range(n)]
start=[] #用来储存起始位置
for i in range(n):
    for j in range(n):
        if maze[i][j]==5:
            start.append((i,j)) #遍历矩阵找到两个5并加入start
delta_x=start[1][0]-start[0][0] #1或0
delta_y=start[1][1]-start[0][1] #0或1 用来判断横放还是竖放
visited=set() #是否入过队
visited.add((start[0][0],start[0][1])) #只关心第一个5 也就是上面的或者左边的 集合用add
def is_valid(r,c):
    if 0<=r<n and 0<=c<n and (r,c) not in visited and maze[r][c]!=1 and 0<=r+delta_x<n and 0<=c+delta_y<n and maze[r+delta_x][c+delta_y]!=1:
        return 1 #1和0就是True和False
    else:
        return 0
dx=[0,0,1,-1]
dy=[1,-1,0,0]
stack=deque()
stack.append((start[0][0],start[0][1]))
while stack:
    front_x,front_y=stack.popleft()
    if maze[front_x][front_y]==9 or maze[front_x+delta_x][front_y+delta_y]==9:
        print('yes')
        exit() #停止整个程序 如果是break的话只跳出while循环 还会print('no')
    for i in range(4):
        nx,ny=front_x+dx[i],front_y+dy[i]
        if is_valid(nx,ny):
            visited.add((nx,ny))
            stack.append((nx,ny))
print('no')
```

#### 哈希表

```python
#完美的爱 前缀和+哈希表 O(n)
from collections import defaultdict
def f(n,gifts):
    gifts_off=[x-520 for x in gifts] #转化为和为0
    pre_sum=0
    max_len=0
    sum_in=defaultdict(list)
    sum_in[0].append(-1) #用于解决前i个数之和就是0的情况
    for i,gift in enumerate(gifts_off):
        pre_sum+=gift
        if pre_sum in sum_in:
            length=i-sum_in[pre_sum][0]
            max_len=max(max_len,length)
        sum_in[pre_sum].append(i)
    max_value=max_len*520 if max_len>0 else 0
    return max_value
n=int(input())
gifts=list(map(int,input().split()))
print(f(n,gifts))
```

## 数学

1.Dilworth定理：上升子序列的最小数量等于最长下降子序列的长度

```python
#跳高 跟拦截导弹很像 bisect_left返回的是新元素应该插入的位置！
from bisect import bisect_left
def min_testers_needed(scores):
    scores.reverse()  
    lis = []  
    for score in scores:
        pos = bisect_left(lis, score)
        if pos < len(lis):
            lis[pos] = score
        else:
            lis.append(score)
    return len(lis)
N = int(input())
scores = list(map(int, input().split()))
print(min_testers_needed(scores))
```

##  坑点&细节

1.创建dp列表时小心数组越界 e.g.dp=[0]*(n+1)

OJ的pylint是静态检查，有时候报的不对。解决方法有两种，如下：
1）第⼀行加# pylint: skip-file 
2）如果函数内使⽤全局变量（变量类型是immutable，如int），则需要在程序最开始声明⼀下。如果是全局变量是list类型，则不受影响。

3.print(n) (maya canlendar)

4.radar installation循环内最后加一句input()读取空行



 

 

 

 

 

 