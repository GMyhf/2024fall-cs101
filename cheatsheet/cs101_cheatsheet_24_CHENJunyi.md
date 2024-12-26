# 计算概论期末考试总结

2024.12.26：发现考前一个高效复习的办法。bilibili搜左程云，这个up的算法更新的很全，自己哪块薄弱就看哪块，可以快速大量云刷题

## 一·函数

### 输出

print(f'{ans},{res:.1f}')print是可以带sep和end参数的

### 字符串

str.title()首字母大写（每个单词）  str.lower()/upper()每个字母小/大写  str.strip()去除空格，有rstrip/lstrip去掉尾部/头部的空格

ord() chr() 可以完成字符与ASCII码的转化

str.find()查找指定字符，注意如果有的话会返回第一个找到的，如果没有会返回-1

### 运算

Python的float有精度问题，尽量用int运算，或用//代替/。

除法还要注意是否可能出现除以0的情况。

舍入时注意round不是严格意义上的四舍五入，遇到恰好.5会向偶数舍入。

floor和ceil是安全的。float的等于判断不能用“==”，要用绝对值的差小于某个极小量（或者用math库中的isclose）

***math库***：最常用的sqrt,对数log(x[,base])、三角sin()、反三角asin()也都有；还有e,pi等常数，inf表示无穷大；返回小于等于x的最大整数floor（）,大于等于ceil（）,判断两个浮点数是否接近isclose（a，b，*, rel_tol=1e-09, abs_tol=0.0）；一般的取幂pow（x，y）,阶乘factorial（x）如果不符合会ValueError,组合数comb（n，k）`math.radians()`将度数转换为弧度，或者使用`math.degrees()`将弧度转换为度数。

### 列表，字典

append以及pop（都是O(1)的）。但是注意del，remove，pop(0)，insert，index等都是O(n)的！反复remove很有可能导致超时，一般开一个真值表先打标记

切片操作关于所切长度是线性复杂度，反复切片很可能超时；切片list[k:l]当k>=l时不会报错而是返回空列表

in list也是线性复杂度！尽量避免in list的判断，必要时最好用dict或set代替。

list.index()慎用，不仅是线性复杂度，而且在找不到的时候会抛出IndexError

Python特性：允许负数下标，正数越界才会报错。

注意函数有无返回值：list.sort(),list.reverse()都是原地修改而不返回，如要用返回值需用sorted()和reversed()（注意reversed()返回的不是列表而是reversed对象，如需用列表要用list转换类型，但是for循环则不需要转换）

排序list.sort(key=lambda x:x[0],reverse=True) True :3 2 1

list.sort(key=lambda x:（x[0],x[1]）)现根据x[0]排序，再根据x[1]排序 

sum([])会返回0，但是min/max([])会报错！

列表解析式：[f(x) for x in list (if P(x))] 创建列表

列表可以相加list.extend()

遍历列表的时候通常用for循环；但是尽量避免一边循环一边删除/添加元素。如果必须的话建议改用while循环。

zip函数

```python
a = [1, 2, 3]
b = ['a', 'b', 'c']
zipped = list(zip(a, b))
print(zipped) # 输出: [(1, 'a'), (2, 'b'), (3, 'c')]
```

**浅拷贝问题**：

基本原则：大于1维很可能出问题，尽量不要用*或者copy拷贝一个列表，不要在不同的地方引用同一个列表变量

例如[[0] * m]不会有问题，但是[[[0] * m] * n]会出问题，可以写成[[0] * m for  _  in  range(n)] 

拷贝一维列表可以a = b[:]复制一份，因为a=b的话a和b会指向同一个列表

二维使用copy模块中的deepcopy深拷贝

#### 字典

key和value都可以是任意类型的东西（不过key一定要是不可变的，比如list不能作为key；但用list作为value是非常常见的）。

把有些信息用字典提前存下来，在需要的时候直接访问，有时是降低时间复杂度的好办法。但是有MLE的风险

如果要按顺序遍历通常用for x in sorted(dict.keys()/values())

dict.keys()/values()/items()分别返回键/值/键值对列表

dict.get(key,default=None)查找指定key的value，如果key不存在不会报错而是返回给定的默认值

dict.pop(key,default=None)弹出指定键值对

如果key已经存在，再赋值时会直接覆盖。

#### 枚举enumerate

for i,x in enumerate(list),遍历list中的（下标，值）对

## 二·算法

### 质数：

欧拉筛（线性筛）

```python
def oula(a):
    zhishu=[]
    zhishu1=[True]*(a+1)
    for i in range(2,a+1):
        if zhishu1[i]:
            zhishu.append(i)
        for h in zhishu:
            if h*i<=a:
                zhishu1[h*i]=False
    zhishu=set(zhishu)
    return zhishu
```



### dp

#### 最长公共子序列

```python
for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
```

#### 最长单调子序列

```python
dp = [1]*n
for i in range(1,n):
    for j in range(i):
        if A[j]<A[i]:
            dp[i] = max(dp[i],dp[j]+1)
ans = sum(dp)
```

#### 背包问题

##### 0-1背包

![image-20241226090713633](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241226090713633.png)

考虑取前i个物品用t时间所能得到的最大值，枚举第i个物品是否取完成转移。注意这里**加上时间参数t**，因为转移过程中t的限定可能会变。“加参数”是DP问题中最重要的技巧之一。

```python
dp = [0]*T
for i in range(n):
    for t in range(T,time[i]-1,-1):
        dp[t] = max(dp[t],dp[t-time[i]]+value[i])
ans = dp[T]
```

这里采用“**滚动数组**”的方法将二维数组压缩成一维，是DP问题中常用的技巧。这基于选前i个物品的状态仅依赖于选前i-1个物品的状态。注意**内层循环要倒着遍历**！

##### 完全背包

将0-1背包中内层循环改为正着遍历即可（这里其实就利用了**先前已经得到的信息**来简化转移：在先前的转移中物品i可能已经用过若干次了）

**多重背包**

最简单的思路是将多个同样的物品看成多个不同的物品，从而化为0-1背包。稍作优化：可以改善拆分方式，譬如将m个1拆成x_1,x_2,……,x_t个1，只需要这些x_i中取若干个的和能组合出1至m即可。最高效的拆分方式是尽可能拆成2的幂，也就是所谓“二进制优化”

```python
dp = [0]*T
for i in range(n):
    all_num = nums[i]
    k = 1
    while all_num>0:
        use_num = min(k,all_num) #处理最后剩不足2的幂的情形
        for t in range(T,use_num*time[i]-1,-1):
            dp[t] = max(dp[t-use_num*time[i]]+use_num*value[i],dp[t])
        k *= 2
        all_num -= use_nume
```

注：背包问题的DP解法需要时间T不太大，因为要遍历每个可能的T。如果T很大而物品数量很少，采用DFS枚举物品的选法有时是更好的选择。

### 区间问题

#### 1 区间合并

给出一堆区间，要求**合并**所有**有交集的区间** （端点处相交也算有交集）。最后问合并之后的**区间**。

![img](https://pic4.zhimg.com/80/v2-6e3bb59ed6c14eacfa1331c645d4afdf_1440w.jpg)

<center>区间合并问题示例：合并结果包含3个区间</center>

【**步骤一**】：按照区间**左端点**从小到大排序。

【**步骤二**】：维护前面区间中最右边的端点为ed。从前往后枚举每一个区间，判断是否应该将当前区间视为新区间。

假设当前遍历到的区间为第i个区间 [l_i,r_i]，有以下两种情况：

- l_i <=ed：说明当前区间与前面区间**有交集**。因此**不需要**增加区间个数，但需要设置 ed = max(ed, r_i)。

- l_i > ed: 说明当前区间与前面**没有交集**。因此**需要**增加区间个数，并设置 ed = max(ed, r_i)。

  ```python
  list.sort(key=lambda x:x[0])
  st=list[0][0]
  ed=list[0][1]
  ans=[]
  for i in range(1,n):
  	if list[i][0]<=ed:
          ed=max(ed,list[i][1])
      else:
          ans.append((st,ed))
          st=list[i][0]
          ed=list[i][1]
  ans.append((st,ed))
  ```

  

#### 2 选择不相交区间

给出一堆区间，要求选择**尽量多**的区间，使得这些区间**互不相交**，求可选取的区间的**最大数量**。这里端点相同也算有重复。

![img](https://pic1.zhimg.com/80/v2-690f7e53fd34c39802f45f48b59d5c5a_1440w.webp)

<center>选择不相交区间问题示例：结果包含3个区间</center>

【**步骤一**】：按照区间**右端点**从小到大排序。

【**步骤二**】：从前往后依次枚举每个区间。

假设当前遍历到的区间为第i个区间 [l_i,r_i]，有以下两种情况：

- l_i <= ed：说明当前区间与前面区间有交集。因此直接跳过。

- l_i > ed: 说明当前区间与前面没有交集。因此选中当前区间，并设置 ed = r_i。

  ```python
  list.sort(key=lambda x:x[1])
  ed=list[0][1]
  ans=[list[0]]
  for i in range(1,n):
  	if list[i][0]<=ed:
          continue
      else:
          ans.append(list[i])
          ed=list[i][1]
  ```

  

#### 3 区间选点问题

给出一堆区间，取**尽量少**的点，使得每个区间内**至少有一个点**（不同区间内含的点可以是同一个，位于区间端点上的点也算作区间内）。

![img](https://pica.zhimg.com/80/v2-a7ef021e1191ec53f20609ba870b44ba_1440w.webp)

<center>区间选点问题示例，最终至少选择3个点</center>



这个题可以转化为上一题的**求最大不相交区间**的数量。

【**步骤一**】：按照区间右端点从小到大排序。

【**步骤二**】：从前往后依次枚举每个区间。

假设当前遍历到的区间为第i个区间 [l_i,r_i]，有以下两种情况：

- l_i <=ed：说明当前区间与前面区间有交集，前面已经选点了。因此直接跳过。

- l_i > ed: 说明当前区间与前面没有交集。因此选中当前区间，并设置 ed = r_i。

  ```python
  list.sort(key=lambda x:x[1])
  ed=list[0][1]
  ans=[list[0][1]]
  for i in range(1,n):
  	if list[i][0]<=ed:
          continue
      else:
          ans.append(list[i][1])
          ed=list[i][1]
  ```

  

#### 4 区间覆盖问题

给出一堆区间和一个目标区间，问最少选择多少区间可以**覆盖**掉题中给出的这段目标区间。

如下图所示： 

![img](https://pic3.zhimg.com/80/v2-66041d9941667482fc51adeb4a616f64_1440w.webp)

<center>区间覆盖问题示例，最终至少选择2个区间才能覆盖目标区间</center>

【**步骤一**】：按照区间左端点从小到大排序。

**步骤二**】：**从前往后**依次枚举每个区间，在所有能覆盖当前目标区间起始位置start的区间之中，选择**右端点**最大的区间。

假设右端点最大的区间是第i个区间，右端点为 r_i。

最后将目标区间的start更新成r_i

```python
q.sort(key=lambda x:x[0])
#start,end 给定
ans=0
ed=q[0][1]
for i in range(n):
    if q[i][0]<=start<=q[i][1]:
        ed=max(ed,q[i][1])
        if ed>=end:
            ans+=1
			break
    else:
        ans+=1
        start=0
        start+=ed
```

#### 5 区间分组问题

给出一堆区间，问最少可以将这些区间分成多少组使得每个组内的区间互不相交。 

![img](https://pic2.zhimg.com/80/v2-6c6a045d481ddc44c66b046ef3e7d4cd_1440w.webp)

<center>区间分组问题示例，最少分成3个组</center>

【**步骤一**】：按照区间左端点从小到大排序。

【**步骤二**】：从**前往后**依次枚举每个区间，判断当前区间能否被放到某个现有组里面。

（即判断是否存在某个组的右端点在当前区间之中。如果可以，则不能放到这一组）

假设现在已经分了 m 组了，第 k 组最右边的一个点是 r_k，当前区间的范围是 [L_i,R_i] 。则：

如果L_i <r_k 则表示第 i 个区间无法放到第 k 组里面。反之，如果 L_i > r_k， 则表示可以放到第 k 组。

- 如果所有 m 个组里面没有组可以接收当前区间，则当前区间新开一个组，并把自己放进去。
- 如果存在可以接收当前区间的组 k，则将当前区间放进去，并更新当前组的 r_k = R_i。

**注意：**

为了能快速的找到能够接收当前区间的组，我们可以使用**优先队列 （小顶堆）**。

优先队列里面记录每个组的右端点值，每次可以在 O(1) 的时间拿到右端点中的的最小值。

```python
import heapq
list.sort(key=lambda x: x[0])
min_heap = [list[0][1]]    
for i in range(1, n):
    if list[i][0] >= min_heap[0]:
        heapq.heappop(min_heap)
    heapq.heappush(min_heap, list[i][1])
num=len(min_heap)
```



### BFS

BFS通常用来处理最短路问题（连通分支、走迷宫等问题一般用DFS解决；对于最短路问题，由于用DFS可能需要遍历所有可能路径，BFS的时间复杂度常常会小得多）

变形：

​	小游戏：以拐弯此处作为bfs下一层的条件

剪枝：
	变换的迷宫：重复一个周期啥也没干的就可以删了（需要额外的一个列表去判断上一个周期的状态）

queue中的元素：
	不一定只是坐标对，有时间参量的时候要考虑加上时间的三元元组

模板：

```python
from collections import deque
directions=[...]
queue=deque([(x0,y0)])
visited=set()
visited.add((x0,y0))
while queue:
	x,y=queue.popleft()
    for dx,dy in directions:
		nx,ny=x+dx,y+dy
        if -1<nx<n and -1<ny<m and ... and ma[nx][ny] not in visited:
            visited.add((nx,ny))
            queue.append((nx,ny))
            ...
#对while这一块，有时需要这样写：
while queue:
    for _ in range(len(queue)):
        x,y=queue.popleft()
    	for dx,dy in directions:
		nx,ny=x+dx,y+dy
        if -1<nx<n and -1<ny<m and ... and ma[nx][ny] not in visited:
            visited.add((nx,ny))
            queue.append((nx,ny))
            ...
```

![image-20241225095808023](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241225095808023.png)

#### **dijkstra**（bfs变形）

![image-20241225105822799](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241225105822799.png)

```python
import heapq#小顶堆
#走山路为例，queue中有三个量，时间和坐标
directions=[...]
ditu = []
tl=[[float('inf')]*n for _ in range(m)]
tl[sx][sy]=0
queue = []
heapq.heappush(queue,(0,sx, sy))
while queue:
    t, x, y= heapq.heappop(queue)
    if x==ex and y==ey:
        ...
        break
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and ...:
            ...
            if ...:
                ...
               	heapq.heappush(queue,(tl[nx][ny],nx, ny))
```



### DFS

有时要剪枝，很多时候要回溯

#### 迷宫问题

问能否走到出口、输出可行路径、输出连通分支数、输出连通块大小等。这种问题应用经典的图搜索DFS即可解决，不需要回溯，**每个点只需要搜到一次**，所以**不需要撤销标记**。

```python
directions = [...]
...
visited = [[False]*n for _ in range(m)]
def dfs(x,y):
    global area
    if vis[x][y]:
        return
    visited[x][y] = True
    ...
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<m and 0<=ny<n and vis[nx][ny] and ...:
            dfs(nx,ny)
#此处还可以在dfs前不用标记vis，在for循环里：
#vis[nx][ny]=1
#dfs(nx,ny)
#vis[nx][ny]=0
#这样自身形成回溯
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
```

#### **回溯**（例子）

其实搜索很多时候都要回溯

```python
#马走日
directions=[[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]
def dfs(n,m,x,y,ma,step,p):
    if step==n*m:
        p[0]+=1
        return
    for dx,dy in directions:
        if -1<x+dx<n and -1<y+dy<m and ma[x+dx][y+dy]:
            ma[x+dx][y+dy]=0
            dfs(n,m,x+dx,y+dy,ma,step+1,p)
            ma[x+dx][y+dy]=1#here
case=int(input())
for _ in range(case):
    n,m,x,y=map(int,input().split())
    ma=[[1 for _ in range(m)] for _ in range(n)]
    ma[x][y]=0
    p=[0]
    dfs(n,m,x,y,ma,1,p)
    print(p[0])
#八皇后
import copy
def t(row,col,pp):
    p=copy.deepcopy(pp)
    for i in range(1,9):
        p[i][col]=False
        if 0<col+(i-row)<9:
            p[i][col+(i-row)]=False
        if 0<col-(i-row)<9:
            p[i][col - (i - row)] = False
    for i in range(1, 9):
        p[row][i] = False
        if 0<row+(i-col)<9:
            p[row+(i-col)][i]=False
        if 0 < row - (i - col) < 9:
            p[row - (i - col)] [i]= False
    return p
def search(a,p,s,answer):
    for i in range(1,9):
        if p[a][i]:
            s+=str(i)
            if a==8:
                answer.append(s)
            else:
                search(a + 1,t(a, i, p), s, answer)
            s=s[:-1]
    return answer
s=''
p=[[True for i in range(9)] for j in range(9)]
answer=[]
answer=search(1,p,s,answer)
n=int(input())
for i in range(n):
    shuru=int(input())
    print(answer[shuru-1])
```

### 二分

![image-20241225165242146](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241225165242146.png)

#### bisect库

python内置二分查找工具

注意bisect库只适用于**升序序列**，对于降序序列需要将列中每个数取相反数再使用；如果要按指定的key排序，可以将每个元素变为元组，把key放到元组的第一个形成元组序列（这种方法在接下来的单调队列优化中也有应用）

bisect_left和bisect_right分别表示插入可能位置中最靠左/右的位置；注意返回的是下标。

insort函数实现插入功能，原地修改列表而不返回值；但是**它是O(n)的**！

```python
import bisect
bisect.bisect_right(a,6)#返回在a列表中若要插入6的index（有重复数字会插在右边）
bisect.insort(a,6)#返回插入6后的列表a
```

#### 应用

一是方程求解问题。注意这个时候while循环的退出条件应当是l和r的差小于所需精度。

二是一类最优化问题，特别是“最值的最值”问题。这类问题所求的最优值通常具有”单调性质“，即小于某个数的都可以但大于它的都不行。对于这种问题，可以考虑**直接去枚举**最优值的可能取值。利用单调性质采用二分算法，这一步只有logn的复杂度；接下来的问题转化为**判断该最优值**是否满足要求。这样就把最优化问题转化为了判定问题，而判定问题有时有比较好的办法解决。所谓“0-1分数规划问题”也能用类似方法解决。

### Kadane's(最大子数组)

```python
def max_subarray_sum(arr):
    if not arr:
        return 0
    max_current=max_global=arr[0]
    for num in arr[1:]:
        max_current =max(num,max_current+num)
        if max_current>max_global:
			max_global= max_current
    return max_global
```

推广：最大子矩阵

```python
'''
为了找到最大的非空子矩阵，可以使用动态规划中的Kadane算法进行扩展来处理二维矩阵。
基本思路是将二维问题转化为一维问题：可以计算出从第i行到第j行的列的累计和，
这样就得到了一个一维数组。然后对这个一维数组应用Kadane算法，找到最大的子数组和。
通过遍历所有可能的行组合，我们可以找到最大的子矩阵。
'''
def max_submatrix(matrix):
    def kadane(arr):
      	# max_ending_here 用于追踪到当前元素为止包含当前元素的最大子数组和。
        # max_so_far 用于存储迄今为止遇到的最大子数组和。
        max_end_here = max_so_far = arr[0]
        for x in arr[1:]:
          	# 对于每个新元素，我们决定是开始一个新的子数组（仅包含当前元素 x），
            # 还是将当前元素添加到现有的子数组中。这一步是 Kadane 算法的核心。
            max_end_here = max(x, max_end_here + x)
            max_so_far = max(max_so_far, max_end_here)
        return max_so_far

    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float('-inf')

    for left in range(cols):
        temp = [0] * rows
        for right in range(left, cols):
            for row in range(rows):
                temp[row] += matrix[row][right]
            max_sum = max(max_sum, kadane(temp))
    return max_sum

n = int(input())
nums = []

while len(nums) < n * n:
    nums.extend(input().split())
matrix = [list(map(int, nums[i * n:(i + 1) * n])) for i in range(n)]

max_sum = max_submatrix(matrix)
print(max_sum)
```



### 小技巧（加速）

#### 递归加速

```python
from functools import lru_cache
@lru_cache(maxsize=None)
def ...
```

#### 前缀和

O（n2）降到O（n）

#### 懒删除

需要删除一个元素时先对其打上标记，等到操作到该元素时再将其弹出去（由于一般list中删除的复杂度是线性的，操作时跳过打了标记的元素；但这种方法在heap中的运用更为典型）。打上标记后元素仍在序列中，但我们将其**视作已经不存在**进行操作；等到需要真正操作该元素（该元素已到堆顶）时，再做实质上的删除，这样避免了从heap中直接删除元素。

```python
#每次要删除x时out[x]+=1
from heapq import heappop,heappush
while ls:
    x = heappop(ls)
    if not out[x]:
        new_min = x
        heappush(ls,x) #不需要弹出的，记得压回去
        break
    out[x]-=1
```

#### heapq小顶堆

`heappush(heap, item)`：将 `item` 的值加入 `heap` 中，保持堆的性质。

`heappop(heap)`：从 `heap` 中弹出并返回最小的元素，保持堆的性质。如果堆为空，则会引发 IndexError。

`heapify(data)`:将data变成小顶堆

#### 单调栈

```python
#比它大的数在几位数后出现
p=list(map(int,input().split()))
index=[0]*len(p)
stack=[]
for i in range(len(p)-1,-1,-1):
    t=p[i]
    while stack and t>p[stack[-1]]:
        stack.pop()
    if stack:
        index[i]=stack[-1]-i
    stack.append(i)
print(index)
```

#### 日期与时间

 import calendar, datetime print(calendar.isleap(2020)) # 输出: True 

print(datetime.datetime(2023, 10, 5).weekday()) # 输出: 3 (星期四)

### Manacher（回文）

![image-20241222173715671](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241222173715671.png)

