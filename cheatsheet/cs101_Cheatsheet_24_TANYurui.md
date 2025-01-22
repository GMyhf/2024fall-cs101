Cheatsheet(巨人的肩膀上)
# **一、语法糖**和常用函数

## 1. Part 1

```python
"""语法糖和常用函数"""
except (EOFError,ValueError)#元组
lst.insert(index,value)指定位置插入
eval()#去除''，可用于计算字符串
print(bin(9)) #bin函数返回二进制，形式为0b1001
dict.items()#同时调用key和value
print(round(3.123456789,5)# 3.12346
print("{:.2f}".format(3.146)) # 3.15
a,b=b,a
dict.get(key,default=None) # 其中，my_dict是要操作的字典，key是要查找的键，default是可选参数，表示当指定的键不存在时要返回的默认值
ord() # 字符转ASCII
chr() # ASCII转字符
for index,value in enumerate([a,b,c]): # 每个循环体里把索引和值分别赋给index和value。如第一次循环中index=0,value="a" 
```

## 2.part 2

```python
# 二进制转十进制
binary_str = "1010"
decimal_num = int(binary_str, 2) # 第一个参数是字符串类型的某进制数，第二个参数是他的进制，最终转化为整数
print(decimal_num)  # 输出 10
```

# **二、工具**

## 0.Kadane algrithom

**Kadane****算法**

最大连续子序列之和

```python
def max_subarray_sum(nums):

max_sum = current_sum = nums[0]

for num in nums[1:]:
    
    current_sum = max(num, current_sum + num)#是否舍弃前缀和

    max_sum = max(max_sum, current_sum)

return max_sum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(max_subarray_sum(nums)) # 输出: 6
```



## Manacher algrithom

```python
    ns='#'.join(s)  #防止偶数
    n = len(ns)
    dp = [0] * n
    mid = 0
    right = 0
    center = 0
    max_r = 0
    for i in range(n):
        if i < right:
            mirror = 2 * mid - i
            dp[i] = min(dp[mirror], right - i)#镜像对称
        lt = i - dp[i]
        rt = i + dp[i]
        while 0 <= lt - 1 <= rt + 1 < n and ns[lt - 1] == ns[rt + 1]:
            lt -= 1
            rt += 1
            dp[i] += 1
        if dp[i] + i > right:
            right = rt
            mid = i
        if dp[i] > max_r:
            max_r = dp[i]
            center = i
    return ns[center - max_r : center + max_r + 1].replace("#", "")

```



## 分治算法（求排列的逆序数）

```python
def merge_sort(num):#num表示一个数组，我们把它一分为二，再分别排序
    if len(num)==1:
        return num
    mid=len(num)//2
    left_num=num[:mid]
    right_num=num[mid:]
    left_num=merge_sort(left_num)
    right_num=merge_sort(right_num)
    return merged(left_num,right_num,res)
def merged(lst1,lst2,ans):#我们把先前分开的再合拢，同时计算逆序数(子数组内部变换顺序不会影响它们与外界的逆序数)
    l,r=0,0
    merged_lst=[]
    while l<len(lst1) and r<len(lst2):
        if lst1[l]<lst2[r]:
            merged_lst.append(lst1[l])
            l+=1
        else:
            merged_lst.append(lst2[r])
            r+=1
            ans[0]+=len(lst1)-l
    merged_lst.extend(lst1[l:])
    merged_lst.extend(lst2[r:])
    return merged_lst
```



## 1. **欧拉筛**（）

```python
# 胡睿诚 23数院 
N=20
primes = []
is_prime = [True]*N
is_prime[0] = False;is_prime[1] = False
for i in range(2,N):
    if is_prime[i]:
        primes.append(i)
    for p in primes: #筛掉每个数的素数倍
        if p*i >= N:
            break
        is_prime[p*i] = False
        if i % p == 0: #这样能保证每个数都被它的最小素因数筛掉！
            break
print(primes)
# [2, 3, 5, 7, 11, 13, 17, 19]
```



## 2. 简单题可以多循环（提醒）

例：完美立方

```python
x=int(input())
cube=[i**3 for i in range(x+1)]
for a in range(3,x+1):
    for b in range(2,a):
        for c in range(b,a):
            for d in range(c,a):
                if cube[a] ==cube[b]+cube[c]+cube[d]:
                    print("Cube = "+str(a)+", Triple = ("+str(b)+","+str(c)+","+str(d)+")")

#以下是第二种优化方案
n=int(input())
import math
for a in range(2,n+1):
    for b in range(2,int(math.pow(a**3/3,1/3))+1):
        for c in range(b,int(math.pow(a**3/2,1/3))+1):
            for d in range(c,a):
                if a**3==b**3+c**3+d**3:
                    print('Cube = '+str(a)+', Triple = ('+str(b)+','+str(c)+','+str(d)+')')
```

## 3. 拓展包

### （1） math

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
```

### （2） lru_cache

```python
# 需要注意的是，使用@lru_cache装饰器时，应注意以下几点：
# 1.被缓存的函数的参数必须是可哈希的，这意味着参数中不能包含可变数据类型，如列表或字典。
# 2.缓存的大小会影响性能，需要根据实际情况来确定合适的大小或者使用默认值。
# 3.由于缓存中存储了计算结果，可能导致内存占用过大，需谨慎使用。
# 4.可以是多参数的。
```

### （3）bisect（二分查找）

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

### （4）年份calendar包

```python
import calendar
print(calendar.isleap(2020)) # True
---------------------------------------------
from datetime import timedelta,datetime
Day=list(map(int,input().split('-')))
n=int(input())
a,b,c=Day
L=datetime(a,b,c)+timedelta(days=n)
print(L.strftime("%Y-%m-%d"))
```

### （5）heapq 优先队列

```python
import heapq # 优先队列可以实现以log复杂度拿出最小（大）元素
lst=[1,2,3]
heapq.heapify(lst) # 将lst优先队列化
heapq.heappop(lst) # 从队列中弹出树顶元素（默认最小，相反数调转）
heapq.heappush(lst,element) # 把元素压入堆中
```

### （6）Counter包

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

## (7) itertools包 (排列组合等)

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

## 4. 判断完全平方数

```python
import math
def isPerfectSquare(num):
    if num < 0:
        return False
    sqrt_num = math.isqrt(num)
    return sqrt_num * sqrt_num == num
print(isPerfectSquare(97)) # False
```

## 5.Data Structure

### (1).heapq(potions,剪绳子)用于找到最小值

```python
from heapq import heappop,heappush
n=int(input())
potions=list(map(int,input().split()))
heap=[]
life=0
for potion in potions:
    life+=potion
    heappush(heap,potion)
    if life<0:
        life-=heappop(heap)
print(len(heap))
```

### (2).deque

### (3).defaultdict(完美的爱)

```python
from collections import defaultdict
n=int(input())
gifts=list(map(int,input().split()))
lst=[gifts[i]-520 for i in range(n)]
arr=[lst[0]]*n
value=defaultdict(list)
value[0].append(-1)
value[lst[0]].append(0)
ans=(1 if lst[0]==0 else 0)
for i in range(1,n):
    arr[i]=arr[i-1]+lst[i]
    value[arr[i]].append(i)
    ans=max(ans,value[arr[i]][-1]-value[arr[i]][0])
print(520*ans)
```

### (4).set(最短的愉悦旋律；非重叠美丽子序列最大数)

```python
    n=int(input())
    lst=list(map(int,input().split()))
    for i in range(1,n):
        lst[i]+=lst[i-1]
    seen={0}
    res=0
    for i in range(n):
        if lst[i] in seen:
            res+=1
            seen.clear()#初始化
        seen.add(lst[i])
```



# 三、递归与DFS（常用模版）

```python
import sys
sys.setrecursionlimit(1<<30)
from functools import lru_cache
@lru_cache(maxsize=None)
```

由于是按照个人习惯写的，可能与标准模板差异比较大。

## **1. 八皇后的回溯算法：**

```python
def dfs_place(current,n,take,temp,result,forbid):
    if current==n+1:#basecase
        result.append(temp[:])
        return
    for i in range(1,n+1):
        if not take[i] and not forbid[0][7+i-current] and not forbid[1][i+current-2]:
            take[i]=forbid[0][7+i-current]=forbid[1][-2+i+current]=1
            temp.append(i)
            dfs_place(current+1,n,take, temp, result, forbid)
            temp.pop()#开始回溯
            take[i]=forbid[0][7+i-current]=forbid[1][-2+i+current]=0
k=int(input())
taked=[0]*9
result=[]
forbid=[[0 for _ in range(15)],[0 for _ in range(15)]]#分别用于判断斜率为1与-1
dfs_place(1,8,taked,[],result,forbid)
for _ in range(k):
    x=int(input())
    print(''.join(map(str,result[x-1])))
```

## **2. 最大通域面积（DFS）**

```python
dr=[-1,-1,-1,0,0,1,1,1]
dc=[-1,0,1,-1,1,-1,0,1]
nums=0
def dfs(start_r,start_c,rows,cols,matrix):
    global nums
    for k in range(8):
        nr=dr[k]+start_r
        nc=dc[k]+start_c
        if 0<=nr<rows and 0<=nc<cols and matrix[nr][nc]=='W':
            matrix[nr][nc]='.'
            nums+=1
            dfs(nr,nc,rows,cols,matrix)

t=int(input())
ans=[]
for _ in range(t):
    row,col=map(int,input().split())
    area=[list(input())for _ in range(row)]
    res=0
    for i in range(row):
        for j in range(col):
            if area[i][j]=='W':
                nums=1
                area[i][j]='.'
                dfs(i,j,row,col,area)
                res=max(res,nums)
    ans.append(res)
print(*ans,sep='\n')
```

## 3. 迷宫路径数（DFS）（单次dfs创建形参，step到step+1，总体dfs用global）

```python
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def dfs(maze,x,y):
    global cnt
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if maze[nx][ny]=='e':#出口
            cnt+=1
            continue

        if maze[nx][ny]==0:
            maze[x][y]=1
            dfs(maze,nx,ny)
            maze[x][y]=0
    return
n,m=map(int,input().split())
maze=[[-1]*(m+2)]
for _ in range(n):
    temp=[-1]+list(map(int,input().split()))+[-1]
    maze.append(temp)
maze.append([-1]*(m+2))#加保护圈,也可以用切片赋值来完成
maze[1][1]="s"
maze[n][m]="e"
cnt=0
dfs(maze,1,1)
print(cnt)
```

## 4.其他较为抽象的涉及多情况模拟的(将一个数组划分为k个总和相等的子集)

```python
        target,mod=divmod(sum(nums),k)
        if mod:
            return False
        buckets=[0]*k
        nums.sort(reverse=True)
        def dfs(n):
            if n==len(nums):
                return True
            for i in range(k):
                if (i and buckets[i]==buckets[i-1]) or buckets[i]==target:
                    continue
                buckets[i]+=nums[n]
                if buckets[i]<=target and dfs(n+1):
                    return True
                buckets[i]-=nums[n]#回溯
            return False
        return dfs(0)
```



# 四、dp问题

## 1. 背包问题

### 0，1背包（完全背包则改成顺序,多重背包可看做0,1背包，必要时二进制优化；如果必须装满加一个判断)

组合问题公式

如零钱兑换的方法数

dp[i] += dp[i-num]

```python
        dp=[0]*(amount+1)
        dp[0]=1
        n=len(coins)
        for i in range(n):#注意内外层循环顺序，本题只考虑组合，不考虑排列，因此外层循环为硬币
            for j in range(coins[i],amount+1):
                dp[j]+=dp[j-coins[i]]
        return dp[-1]
```

True、False问题公式

dp[i] = dp[i] or dp[i-num]



最大最小问题公式

dp[i] = min(dp[i], dp[i-num]+1)或者dp[i] = max(dp[i], dp[i-num]+1)

如cut ribbon，零钱兑换

以上三组公式是解决对应问题的核心公式。

```python
t,m=map(int,input().split())
grass=[list(map(int,input().split())) for _ in range(m)]
dp=[0]*(t+1)
for time,value in grass:
    for j in range(t,time-1,-1):#倒序保证只采一次
        dp[j]=max(dp[j],dp[j-time]+value)
print(dp[-1])
```

## 2.带权重的区间问题

###   逆向思维

```python
        n=len(questions)
        dp=[0 for _ in range(n+1)]
        questions.reverse()
        for i in range(1,n+1):
            dp[i]=max(dp[i-1],dp[max(0,i-questions[i-1][1]-1)]+questions[i-1][0])
        return dp[-1]
  ----------------------------------------------
         n=len(days)
        date=[1,7,30]
        INF=float('inf')
        dp=[INF for _ in range(n+1)]
        dp[0]=0
        for i in range(1,n+1):
            end=i
            end_date=days[i-1]
            for k in range(3):
                start_date=end_date-date[k]+1
                start=bisect_left(days,start_date)+1
                for j in range(start,end+1):
                    dp[j]=min(dp[j],dp[start-1]+costs[k])
        return dp[-1]

```

## 3.二维dp（多个限制条件）如：宠物小精灵

## 4.整数分割问题（放苹果，简单的整数分割问题）

```python
limit,blood,num=map(int,input().split())
INF=float('inf')
dp=[[INF for _ in range(blood+1)] for _ in range(num+1)]#值表示损失的精灵球，列坐标表示损失血量
dp[0][0]=0
for i in range(1,num+1):
    cost,harm=map(int,input().split())
    for j in range(i,-1,-1):
        for k in range(blood,harm-1,-1):
            if 0<=dp[j-1][k-harm]<=limit-cost:
                dp[j][k]=min(dp[j-1][k-harm]+cost,dp[j][k])
for i in range(num,-1,-1):
    for j in range(blood+1):
        if dp[i][j]!=INF:
            print(i,blood-j)
            exit()
--------------------------------------
    dp=[[0 for _ in range(n+1)]for _ in range(m+1)]#值表示放法，行数表示苹果数，列数表示盘子数
    for i in range(1,n+1):
        dp[0][i]=1#零个苹果，放法均为1
    for i in range(1,m+1):
        if i>=n:#如果苹果数多于盘子数
            for j in range(1,n+1):
                dp[i][j]+=dp[i][j-1]+dp[i-j][j]#放n-1个盘子的情况加上放n个盘子的情况，后者等价于先在这n个盘子上各放一个，再将i-j个苹果放在n个盘子上
        else:
            for j in range(1,i+1):
                dp[i][j]+=dp[i][j-1]+dp[i-j][j]
            for j in range(i+1,n+1):#盘子数多于苹果数，直接等于盘子数与苹果数相同
                dp[i][j]+=dp[i][j-1]
    return dp
-----------------------------------------
def partition_count(n):
    # 初始化dp数组，dp[i][j] 表示数字i划分成不超过j的数的划分方式数
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    # 数字0没有实质内容的划分，所以设置dp[0][j]为1
    for j in range(n + 1):
        dp[0][j] = 1
    # 填充dp数组
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i < j:
                dp[i][j] = dp[i][i]
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - j][j]
    # 返回dp[n][n]即为n的划分数
    return dp[n][n]

```

## 5.双dp（土豪购物，红蓝玫瑰，Basketball Exercise）适用于那种两种状态杂糅的玩意

```python
dp1 = [0] * n
dp2 = [0] * n
dp1[0] = h1[0]
dp2[0] = h2[0]
for i in range(1, n):
    dp1[i] = max(dp2[i - 1] + h1[i], dp1[i - 1])#下一个得选二队
    dp2[i] = max(dp1[i - 1] + h2[i], dp2[i - 1])#下一个得选一队
print(max(dp1[-1], dp2[-1]))
```



# 五、BFS

## 1. 变换的迷宫

```python
def bfs(rows, cols, k, maze, start_x, start_y):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    visited=set()
    visited.add((0,start_x,start_y))
    stack=deque()
    stack.append((0,start_x,start_y))
    while stack:
        num=len(stack)
        while num:
            num-=1
            cnt,front_x,front_y=stack.popleft()
            if maze[front_x][front_y]== 'E':
                return cnt
            temp=(cnt+1)%k
            for o in range(4):
                nx,ny= front_x + dx[o], front_y + dy[o]
                if 0<=nx<rows and 0<=ny<cols and (maze[nx][ny] != '#' or temp == 0) and(temp, nx, ny) not in visited:
                    stack.append((cnt+1,nx,ny))
                    visited.add((temp,nx,ny))
    return 'Oop!'
```

## 2.DIJ算法

### dijkstra模板(走山路)

```python
def dij(start_x, start_y, end_x, end_y):
    if matrix[start_x][start_y]=='#':
        return 'NO'
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = set()   
    stack = [(0, start_x, start_y)]
    while stack:
        hp, front_x, front_y = heappop(stack)
        if (front_x, front_y) in visited:
            continue
        visited.add((front_x, front_y))#出入栈的方式有所不同
        if front_x == end_x and front_y == end_y:
            return hp
        for i in range(4):
            nx = front_x + dx[i]
            ny = front_y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and matrix[nx][ny] != '#':
                cost = abs(int(matrix[nx][ny]) -int(matrix[front_x][front_y]))
                heappush(stack, (hp + cost, nx, ny))
    return 'NO'
```

# 六.区间问题

**按照右端点排序**：

（1）不相交区间数目最大,如：建筑修建

```python
n,length=map(int,input().split())
possible_architects=[]
for _ in range(n):
    center,width=map(int,input().split())
    min_start=max(0,center-width+1)
    max_start=center
    for start in range(min_start,max_start+1):
        end=start+width
        if end<=length:
            possible_architects.append((start,end))#存储所有可能的区间，化动为静
possible_architects.sort(key=lambda x:x[1])
pre_end=0
ans=0
for start,end in possible_architects:
    if start<pre_end:
        continue
    ans+=1
    pre_end=end
print(ans)
```

（2）区间选点问题（给出一堆区间，取**尽量少**的点，使得每个区间内**至少有一个点**）——尽量选择当前区间最右

边的点，同不相交区间数目最大

(3)区间覆盖问题：给出一堆区间和一个目标区间，问最少选择多少区间可以**覆盖**掉题中给出的这段目标区间。

(世界杯只因，对区间的预处理特别重要)

```python
n=int(input())
stalls=list(map(int,input().split()))
--------------------------------------------
ends=[0]*(n+1)
for i in range(1,n+1):
    start=max(i-stalls[i-1],1)
    end=min(i+stalls[i-1],n)
    ends[start]=max(ends[start],end)
for i in range(1,n+1):
    ends[i]=max(ends[i],ends[i-1])#对区间实现预处理，ends[i]表示的是涵盖了第i个鸡窝的摄像头所能达到的最远距离
------------------------------------------
ans=0;pre_end=0
while pre_end<n:
    pre_end=ends[pre_end+1]
    ans+=1
print(ans)
```

**按照左端点排序**：

（1）区间合并（左端点由小到大排序，维护前面区间右端点ed）

如进程检测，雷达安装（感觉两种排序都用到了）

```python
k=int(input())
ans=[]
for _ in range(k):
    n=int(input())
    L=[]
    for n in range(n):
        a,b=map(int,input().split())
        L.append((a,b))
    L.sort(reverse=False)#问题是b不一定顺序
    l=sorted(L,key=lambda x:x[1])
    m=len(L)-1
    result=0
    while m>=0:
        while L[m][0] > l[0][1]:
            m -= 1
        result+=1
        L=L[m+1:]
        l = sorted(L, key=lambda x: x[1])
        m=len(L)-1
    ans.append(result)
for i in ans:
    print(i)
```



（2）区间分组问题：从**前往后**依次枚举每个区间，判断当前区间能否被放到某个现有组里面。

# 七、 逃生指南

## 1. 除法是否使用地板除得到整数？（否则 4/2=2.0）

## 2. 是否有缩进错误？

## 3. 用于调试的print是否删去？

## 4. 非一般情况的边界情况是否考虑？（参考取模,序列中连续相等,0）

## 5. 递归中return的位置是否准确？（缩进问题,逻辑问题）

## 6. 贪心是否最优？有无更优解？

## 7. 正难则反（参考 #蒋子轩 23工院# 乌鸦坐飞机）

## 8. 审题是否准确？ 是否漏掉了输出？（参考简单的整数划分）

## 9.注意字符串输入的整体性，可以选择用逗号，空格分割单位（参考文字排版）

## 10.PE：空格；RE：break 打乱输入;TLE:while陷入无限循环。while过程中，一定要注意参数变化

## 11.dp是否注意了循环内外层，有没有预留0条件，数据会不会需要预处理

## 12.搜索，有没有注意bfs中q-1，有没有加入visited辅助剪枝

## 13.矩阵行列不要搞错了

## 14.浅拷贝与深拷贝

