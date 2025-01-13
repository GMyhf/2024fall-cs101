# Cheating Sheet

## 前置

1. Lists

```python
                               Complexity
Operation     | Example      | Class         | Notes
--------------+--------------+---------------+-------------------------------
Index         | l[i]         | O(1)	     |
Store         | l[i] = 0     | O(1)	     |
Length        | len(l)       | O(1)	     |
Append        | l.append(5)  | O(1)	     | mostly: ICS-46 covers details
Pop	          | l.pop()      | O(1)	     | same as l.pop(-1), popping at end
Clear         | l.clear()    | O(1)	     | similar to l = []

Slice         | l[a:b]       | O(b-a)	     | l[1:5]:O(l)/l[:]:O(len(l)-0)=O(N)
Extend        | l.extend(...)| O(len(...))   | depends only on len of extension
Construction  | list(...)    | O(len(...))   | depends on length of ... iterable

check ==, !=  | l1 == l2     | O(N)          |
Insert        | l[a:b] = ... | O(N)	     | 
Delete        | del l[i]     | O(N)	     | depends on i; O(N) in worst case
Containment   | x in/not in l| O(N)	     | linearly searches list 
Copy          | l.copy()     | O(N)	     | Same as l[:] which is O(N)
Remove        | l.remove(...)| O(N)	     | 
Pop	      	  | l.pop(i)     | O(N)	     | O(N-i): l.pop(0):O(N) (see above)
Extreme value | min(l)/max(l)| O(N)	     | linearly searches list for value
Reverse	      | l.reverse()  | O(N)	     |
Iteration     | for v in l:  | O(N)          | Worst: no return/break in loop

Sort          | l.sort()     | O(N Log N)    | key/reverse mostly doesn't change
Multiply      | k*l          | O(k N)        | 5*l is O(N): len(l)*l is O(N**2)
```

2. Sets

```python
                               Complexity
Operation     | Example      | Class         | Notes
--------------+--------------+---------------+-------------------------------
Length        | len(s)       | O(1)	     |
Add           | s.add(5)     | O(1)	     |
Containment   | x in/not in s| O(1)	     | compare to list/tuple - O(N)
Remove        | s.remove(..) | O(1)	     | compare to list/tuple - O(N)
Discard       | s.discard(..)| O(1)	     | 
Pop           | s.pop()      | O(1)	     | popped value "randomly" selected
Clear         | s.clear()    | O(1)	     | similar to s = set()

Construction  | set(...)     | O(len(...))   | depends on length of ... iterable
check ==, !=  | s != t       | O(len(s))     | same as len(t); False in O(1) if
      	      	     	       		       the lengths are different
<=/<          | s <= t       | O(len(s))     | issubset
>=/>          | s >= t       | O(len(t))     | issuperset s <= t == t >= s
Union         | s | t        | O(len(s)+len(t))
Intersection  | s & t        | O(len(s)+len(t))
Difference    | s - t        | O(len(s)+len(t))
Symmetric Diff| s ^ t        | O(len(s)+len(t))

Iteration     | for v in s:  | O(N)          | Worst: no return/break in loop
Copy          | s.copy()     | O(N)	     |
```

3. Dictionaries: dict and defaultdict

```python
                               Complexity
Operation     | Example      | Class         | Notes
--------------+--------------+---------------+-------------------------------
Index         | d[k]         | O(1)	     |
Store         | d[k] = v     | O(1)	     |
Length        | len(d)       | O(1)	     |
Delete        | del d[k]     | O(1)	     |
get/setdefault| d.get(k)     | O(1)	     |
Pop           | d.pop(k)     | O(1)	     | 
Pop item      | d.popitem()  | O(1)	     | popped item "randomly" selected
Clear         | d.clear()    | O(1)	     | similar to s = {} or = dict()
View          | d.keys()     | O(1)	     | same for d.values()

Construction  | dict(...)    | O(len(...))   | depends # (key,value) 2-tuples

Iteration     | for k in d:  | O(N)          | all forms: keys, values, items
	      	      	       		     | Worst: no return/break in loop
```





## 一、

### 1.输入输出和字符串

```python
# 输入
a = int(input()) ; string = str(input())
a, b = map(int, input().split()) # 还是str？要不要转化？
nums = [int(x) for x in input().split()] # split()里面也可以加参数
# 字符串的处理
string.title() # 每个单词的首字母大写
string.lower() ; string.upper() ; string.swapcase() # 转大写；转小写；大转小小转大
# 字符串之间的空格记得小心处理；字符串是不可变对象，可以索引、切片、连接（'+'），不能修改，修改要创一个列表
ord() ; chr() # 可以转化ACSII码与字符
string.find() # 查找指定字符，有就返回第一个找到的index，没有会返回-1
string.zfill() # 自动在前面补0补到所需位数
str.strip() ; string.rstrip() ; string.lstrip() #去掉空格；去掉头部/尾部的空格
# 输出
''.join(list) # 注意list里面要是str类型。或者str(x) for x in list
print(*ans) ; print(a, b, end="\n") # 换行
print('{},{:.1f}'.format(ans,res)) ; print(f'{ans},{res:.1f}')
```

### 2.math

```python
# 进制转化：bin, oct, hex 注意得到的是带前缀的字符串
# 二进制转十进制
binary_str = "1010"
decimal_num = int(binary_str, 2) # 第一个参数是字符串类型的某进制数，第二个参数是他的进制，最终转化为整数
print(decimal_num)  # 输出 10
```

## 二、Tools

#### 埃氏筛

```python
primecheck = [1] * (10**6 + 1)     #数据上限
primecheck[0] = primecheck[1] = 0    #初始化0和1的数组
p = 2      #初始化 p
while p * p <= 10**6:
    if primecheck[p] == 1:   
        for i in range(p * p, 10**6 + 1, p):
            primecheck[i] = 0
    p += 1
primes = set()   #收集标记的质数
for i in range(2, 10**6 + 1):
    if primecheck[i] == 1:
        primes.add(i)  #注意集合用add    
```

### 正则表达式

```python
import re
pattern = re.compile(r'       ')  #编译正则表达式，注意''之前的r以及空格处的正则表达式
'''
^ 匹配字符串的开头   $ 匹配字符串的末尾
. 匹配任意字符，除了换行符
[   ] 用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
[^   ] 不在[ ]中的字符：[^abc] 匹配除了a,b,c之外的字符。
re*	匹配0个或多个的表达式  re+ 匹配1个或多个的表达式  re? 匹配0个或1个表达式
re{n}	匹配n个前面表达式。"o{2}"不能匹配"Bob"中的"o"，但是能匹配"food"中的两个o
\w	匹配数字字母下划线
\W	匹配非数字字母下划线
\s	匹配任意空白字符，等价于 [\t\n\r\f\v]
\S	匹配任意非空字符
\d	匹配任意数字，等价于 [0-9]
\D	匹配任意非数字
举例子：
[Pp]ython	匹配 "Python" 或 "python"
rub[ye]	匹配 "ruby" 或 "rube"
[aeiou]	匹配中括号内的任意一个字母
[0-9]	匹配任何数字。类似于 [0123456789]
[a-z]	匹配任何小写字母
[A-Z]	匹配任何大写字母
[a-zA-Z0-9]	匹配任何字母及数字
[^aeiou]	除了aeiou字母以外的所有字符
[^0-9]	匹配除了数字外的字符
'''
pattern.findall(string[, pos[, endpos]])
#在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果有多个匹配模式，则返回元组列表，如果没有找到匹配的，则返回空列表。
#pattern 匹配模式  string 待匹配的字符串。
#pos 可选参数，指定字符串的起始位置，默认为 0。
#endpos 可选参数，指定字符串的结束位置，默认为字符串的长度。
```

## 三、Dynamic Programming

**<u>动态规划五部曲：</u>**

1. 确定dp数组（dp table）以及下标的含义
2. 确定递推公式
3. dp数组如何初始化
4. 确定遍历顺序
5. 举例推导dp数组

### 背包专题注意事项：

问能否能装满背包（或者最多装多少）：dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])

问装满背包有几种方法：dp[j] += dp[j - nums[i]]

问背包装满最大价值：dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

问装满背包所有物品的最小个数：dp[j] = min(dp[j - coins[i]] + 1, dp[j])

### 0-1背包--吊饰手链

贝茜去了商场的 珠宝店和间谍吊饰手镯。当然，她想填补 它具有 *N*（1 ≤ *N*≤ 3,402） 可用魅力中最好的魅力。提供列表中的每个魅力 i 都有一个权重 W i（1 ≤ W i≤ 400）、一个“可取性”因子 D i（1 ≤ *D* *i*≤ 100），最多可以使用一次。贝茜只能支撑重量不超过*M*（1 ≤ *M*≤ 12,880）的吊饰手链。鉴于 该重量限制作为约束和带有其的魅力列表 权重和合意性评级，推导出最大可能的总和 评级。 

#### 二维dp数组

```python
N , M = map(int,input().split())
charms = []
for _ in range(N):
    charms.append([int(x) for x in input().split()])
charms.sort(key = lambda x : x[0])  # 注意排序
dp = [[0]*(M+1) for _ in range(N)]  # dp数组的建立
start_weight = charms[0][0]
start_value = charms[0][1]
for i in range(start_weight,M+1):  # 初始化dp数组
    dp[0][i] = start_value
for i in range(1,N):   # 遍历物品
    for j in range(1,M+1):  # 遍历背包重量
        if j - charms[i][0] >= 0 :
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-charms[i][0]]+charms[i][1])  # 先写这个，不放or放进
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N-1][M])
```

#### 一维dp数组

```python
N , M = map(int,input().split())
charms = []
for _ in range(N):
    charms.append([int(x) for x in input().split()])
charms.sort(key = lambda x : x[0])
dp = [0]*(M+1)
for i in range(N):  #一定先遍历物品 
    for j in range(M,0,-1):  #再 倒序 遍历背包重量
        if j - charms[i][0] >= 0 :
            dp[j] = max(dp[j],dp[j-charms[i][0]] + charms[i][1])
        else:
            dp[j] = dp[j]
print(dp[M])
```

### 完全背包（来自代码随想录）--装满背包的最大价值

```python
def test_CompletePack():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagWeight = 4
    dp = [0] * (bagWeight + 1)
    for i in range(len(weight)):  # 遍历物品
        for j in range(weight[i], bagWeight + 1):  # 遍历背包容量，正向遍历即可
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    print(dp[bagWeight])
```

### 完全背包--组合or排列的方案数

```python
def change(self, amount: int, coins: List[int]) -> int: # 组合的情况
    dp = [0]*(amount + 1)
    dp[0] = 1 # 注意初始化
    for i in range(len(coins)): # 遍历物品
        for j in range(coins[i], amount + 1): # 遍历背包
            dp[j] += dp[j - coins[i]]  # 注意，如果求排列的结果要将遍历物品和背包的顺序交换
    return dp[amount]
```

### 恰好装满的0-1背包--二维

```python
T, n = map(int, input().split())
training = [[int(x) for x in input().split()] for _ in range(n)]
training.sort(key = lambda x : x[0])
dp = [[float('-inf')]*(T + 1) for _ in range(n + 1)] 
for i in range(n + 1): # 初始化将物品变为1至n的index，只有第一列合法的令为0，其他负无穷。
    dp[i][0] = 0
for i in range(1, n + 1):
    for j in range(1, T+1):
        if j - training[i-1][0] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-training[i-1][0]] + training[i-1][1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][T] if dp[n][T] != float('-inf') else -1)
```

### 恰好装满的完全背包--一维（组合）

```python
t = int(input())
for _ in range(t):
    e, f = map(int, input().split())
    w = f - e
    
    n = int(input())
    coins = [[-1,-1]]
    for k in range(n):
        coins.append([int(x) for x in input().split()])
        
    dp = [float('inf')]*(w+1)
    dp[0] = 0
    for i in range(1, n+1):
        for j in range(coins[i][1], w + 1):
            dp[j] = min(dp[j], dp[j - coins[i][1]] + coins[i][0])
    print(f'The minimum amount of money in the piggy-bank is {dp[w]}.' if dp[w] != float('inf') else 'This is impossible.')
```

### 交错辅助背包

```python
t, m = map(int, input().split())
gain = []
for _ in range(t):
    gain.append([int(x) for x in input().split()])
dp0 = [0]*t
dp0[0] = gain[0][0]
dp1 = [0]*t
dp1[0] = gain[0][1]
for i in range(1, t):
    dp0[i] = max(dp0[i-1] + gain[i][0], dp1[i-1] + gain[i][0] - m) # 双转移，从两边来，并且要两边都更新
    dp1[i] = max(dp0[i-1] + gain[i][1] - m, dp1[i-1] + gain[i][1])
print(max(dp0[t-1], dp1[t-1]))
```

## 四、图搜索

### 深度优先搜索DFS

#### 1.地图迷宫型搜索

```python
# 没有另外开一个visited的数组的方法
directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)] #方向标记
s = 0
def dfs(x,y):
    global s
    #1.终止条件：搜过或者遇到陆地
    if matrix[x][y] == '.' : 
        return
    #2.标记 以及相应需求的变化
    matrix[x][y] = '.' #符合先标记
    s += 1      #面积自增
    #3.进行后续的搜索
    for direction in directions:   #八个方向搜索
        nextx = x + direction[0]   
        nexty = y + direction[1]
        dfs(nextx,nexty)     #递归后面的  
#输入
T = int(input())
for _ in range(T):
    N , M = map(int,input().split())
    
    matrix = [['.']*(M+2)]  #这种方法注意要加保护圈
    for m in range(N):
        matrix.append(['.']+[str(x) for x in input()]+['.'])
    matrix.append(['.']*(M+2))
    
    result = 0
    for i in range(1,N+1):
        for j in range(1,M+1):
            if matrix[i][j] == 'W' : #遇到能搜索的就开始
                s = 0     #初始化面积
                dfs(i,j)   
                result = max(result,s)
    print(result)
```

#### 2.二叉树树型图的搜索

```python
matrix = [[0]*10 for _ in range(10)]
def check(x,j):      #检查的函数模块
    for i in range(1,9):
        if matrix[i][j] == 1:
            return False
    for i in range(1,9):
        if x+i-j >= 1 and x+i-j <= 8 :
            if matrix[x+i-j][i] == 1:
                return False
    for i in range(1,9):
        if x-i+j >= 1 and x-i+j <= 8 :
            if matrix[x-i+j][i] == 1:
                return False
    return True
result = [] ; path = []  #结果收集和中间路径
def dfs(matrix,x):
    if x == 9:
        result.append(''.join(str(x) for x in path))  #deep copy!!!!!
        return
    for j in range(1,9):
        if check(x,j) == True:  #能开始搜索
            path.append(j)  #加入队列
            matrix[x][j] = 1 #标记
            dfs(matrix,x+1)  #递归
            path.pop()   #回溯
            matrix[x][j] = 0  #回溯
dfs(matrix,1)
n = int(input())
for _ in range(n):
    print(result[int(input())-1])
```

#### 3.排列组合型dfs

e.g.全排列      *注意排列和组合的区别，能不能重复取决定要不要加入startindex的参数

```python
letters = [str(x) for x in input()]
n = len(letters)
result, path = [], []
def dfs(letters, l):
    if l == n: # 确定的深度
        result.append(''.join(str(x) for x in path))
        return
    for i in range(n):
        if letters[i] in path: #去重，全遍历
            continue
        path.append(letters[i])
        dfs(letters, l+1)
        path.pop()
dfs(letters, 0)
result.sort()
for k in result:
    print(k)
```

#### 4.dfs similar + dp （记忆化搜索？+递归）

滑雪。

```python
r, c = map(int, input().split())
m = [[int(i) for i in input().split()] for _ in range(r)]
dp = [[0]*c for _ in range(r)] # dp矩阵建立

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x, y):
    if dp[x][y]:  # 检查算没算过，算过就不算了
        return dp[x][y]
    if not (0 <= x < r and 0 <= y < c): # 判断是否越界
        return 0
    ma = 0   # 寻找比当前矮的地方的最长路径
    for i in range(4):
        if 0 <= x + dx[i] < r and 0 <= y + dy[i] < c and m[x+dx[i]][y+dy[i]] < m[x][y]:
            ma = max(ma, dfs(x + dx[i], y + dy[i])) # 递归下一个
    dp[x][y] = ma + 1 # 多1
    return dp[x][y] # 注意要返回当前的值，便于递归

ans = 1
for i in range(r):
    for j in range(c):
        ans = max(ans, dfs(i, j))     # 搜索每个点
print(ans)
```

### 广度优先搜索BFS

#### 1.标准化bfs简单模版

```python
from collections import deque
dx = [0 , 0 , 1 , -1]
dy = [1 , -1 , 0 , 0]
def can_visit(x , y):
    return 0 <= x < n and 0 <= y < m and maze[x][y] == 0 and not in_queue[x][y]

def bfs(x , y):
    q = deque() # 初始化队列
    q.append((x , y))  # 放入第一个元素/起点，注意可以加上参数，比如方向？体力？
    in_queue[x][y] = True # 标记为访问过的节点
    step = 0 # optional 计算步数
    while q:
        for _ in range(len(q)): # 先不用写这个
            curx , cury = q.popleft() # 取出元素
            
            if curx == n - 1 and cury == m - 1: # 只要到达就是最短路径，收集结果
                return step
            
            for direction in range(4): # 四个方向遍历
                nextx = curx + dx[direction]
                nexty = cury + dy[direction]
                if can_visit(nextx, nexty): # 可以到达
                    in_queue[nextx][nexty] = True # 标记
                    q.append((nextx,nexty)) #入队   *注意，标记和入队的操作交换会造成时间的差异
        step += 1
    return -1
```

#### 2.有参数稍稍复杂版bfs

```python
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
m, n, t = map(int, input().split())
matrix = [[str(x) for x in input()] for _ in range(m)]

for i in range(m):
    for j in range(n):
        if matrix[i][j] == '@' :
            x1, y1 = i, j
        elif matrix[i][j] == '+' :
            x2, y2 = i, j
    
visited, result = set(), [] # 创建结果和访问数组
q = deque() # 创建队列
q.append((0, x1, y1, t)) # 起点入队，加入了体力和时间的参数
visited.add((x1, y1, t))  # 在访问的队列里面只需要加入体力的不同来标记

while q:
    time, curx, cury, cha = q.popleft() # 队列取出元素
    
    if curx == x2 and cury == y2 : # 终点记录，收集数据
        result.append(time)
        
    for d in range(4): # 四个方向
        nextx, nexty = curx + dx[d], cury + dy[d]
        if 0 <= nextx < m and 0 <= nexty < n and (nextx, nexty, cha) not in visited: # 能够到达
            if matrix[nextx][nexty] == '#' : # 分类，需要消耗体力时
                if cha > 0 :
                    nextcha = cha - 1 # 尽量都这样使用新的变量而不要自增自减
                    nexttime = time + 1
                    q.append((nexttime, nextx, nexty, nextcha)) # 下一个入队
                    visited.add((nextx, nexty, nextcha)) # 标记
                else:
                    pass
            else:
                nexttime = time + 1
                q.append((nexttime, nextx, nexty, cha)) # 下一个入队
                visited.add((nextx, nexty, cha)) # 标记
print(min(result) if result else -1)
```

#### 3.bfs+heapq，带权重的bfs

```python
import heapq
dx = [0,0,1,-1]
dy = [1,-1,0,0]
m, n, p = map(int, input().split())
matrix = [[str(x) for x in input().split()] for _ in range(m)]
for _ in range(p):
    x1, y1, x2, y2 = map(int, input().split())
    
    if matrix[x1][y1] == '#' or matrix[x2][y2] == '#' : # 特判
        print('NO')
        continue
        
    visited, heap, result = set(), [], []
    heapq.heappush(heap, (0, x1, y1)) 
    # 入队，应该是以体力大小构造小顶堆
    visited.add((x1, y1, -1)) 
    # 标记起点，方向为-1，使用方向应该是保证可以多次到达一个点，但是以不同方向到达
    
    while heap:
        tire, curx, cury = heapq.heappop(heap) #堆顶弹出
        
        if curx == x2 and cury == y2 : #终点记录，收集数据
            result.append(tire)
            
        for d in range(4): #四个方向
            nextx, nexty = curx + dx[d], cury + dy[d]
            if 0 <= nextx < m and 0 <= nexty < n and  matrix[nextx][nexty] != '#' \
            and (nextx, nexty, d) not in visited:
                #能够到达
                nexttire = tire + abs(int(matrix[nextx][nexty]) - int(matrix[curx][cury]))
                heapq.heappush(heap, (nexttire, nextx, nexty)) #下一个入队
                visited.add((nextx, nexty, d)) #标记
    print(min(result) if result else 'NO')
```

## 五、二分查找

## 六、递归（注意从最简单的情况思考）

## 七、数据结构

### 单调栈--滑动窗口最大值

```python
from collections import deque
queue = deque()
n, k = map(int,input().split())
nums = [int(x) for x in input().split()]
result = []

for i in range(k): # 预先处理前k个要进入窗口的值
    while queue and nums[i] > queue[-1]: # 确保了栈是单调非增的，即最大值在队列头部
        queue.pop()
    queue.append(nums[i])
result.append(queue[0])

for i in range(k,n): 
    if queue and nums[i - k] == queue[0]: # 判断是否是要出窗口的值，是的话就把队列头部弹出
        queue.popleft()
    while queue and nums[i] > queue[-1]: # 确保了栈是单调非增的，即最大值在队列头部
        queue.pop()
    queue.append(nums[i])
    result.append(queue[0])
print(*result)
```

### 堆

heapq最重要的功能是“分摊”**插入**与**查找最小值**的复杂度。heappush和heappop的复杂度都是O(logn)，对于需要**不断更新**且**不断查找**的问题，heap常常是值得考虑的数据结构（OJ27256 当前队列中位数，OJ27384 候选人追踪）

对于降序序列需要将列中每个数取相反数再使用；如果要按指定的key排序，可以将每个元素变为元组，把key放到元组的第一个形成元组序列（bfs+heap的时候使用这个来判断参数的选择）

#### 懒删除

注意使用heap时**不能使用通常列表的方法**，这样会破坏堆结构；只能使用heap库中的操作。无法简便删除heap中任何一个数。

这里通常的解决方法是所谓“懒删除”，也即“逻辑删除”：需要删除一个元素时先对其打上标记，等到操作到该元素时再将其弹出去。打上标记后元素仍在序列中，但我们将其**视作已经不存在**进行操作；等到需要真正操作该元素（该元素已到堆顶）时，再做实质上的删除，这样实质上没有改变总的复杂度，但避免了从heap中直接删除元素。

```python
#e.g.最佳候选人
#每次要删除x时out[x]+=1
outcnt = [0]*314160 # 也可以用字典
for i in range(N):
    outcnt[timeact[i][1]] += 1 # 缓存要干什么，累加？删掉的标记？
    while outcnt[heap[0][1]]: # 检查堆顶的缓存有没有to do list
        k = heapq.heappop(heap) # 弹出来
        k = [k[0] + outcnt[k[1]], k[1]] # 操作
        heapq.heappush(heap, k) # optional 塞回去
        outcnt[k[1]] = 0 # 清理缓存
```

## 八、散题

### 移动路线--数学

```python
import math    # 只能一个趋势跑，已知矩阵，数学题，注意组合数的comb
m, n = map(int,input().split())
if m == 1 or n == 1:
    print(1)
else:
    print(math.comb(m+n-2, n-1))
```

### 装箱子--正难则反

```python
import math   # 注意math.ceil()的应用
mol3_2 = [0,5,3,1]
while True:
    packs = [int(x) for x in input().split()]
    if packs == [0,0,0,0,0,0] :
        break
    boxes = packs[5] + packs[4] + packs[3] + math.ceil(packs[2]/4)
    empty_2 = 5*packs[3] + mol3_2[packs[2]%4] # 剩给2的
    if packs[1] > empty_2:
        boxes += math.ceil((packs[1]-empty_2)/9)
    empty_1 = 36*boxes-4*packs[1]-9*packs[2]-16*packs[3]-25*packs[4]-36*packs[5] # 剩给1的
    if packs[0] > empty_1:
        boxes += math.ceil((packs[0]-empty_1)/36)
    print(boxes)
```

### 数学游戏--正难则反

```python
t = int(input())
s = 1 + 2 + 3 # 最大公因数，数字不同，说明每个数字除以最大公因数以后都只剩下最小的数字，分配律可以知道最小的商之和为6
while True:
    while t%s !=0:
        s += 1
    found = False # 置标记便于break
    for x in range(1, s):
        for y in range(x+1, s):
            if y==x: # 去重
                continue
            for z in range(y+1, s):
                if s - x - y != z: # 保证对应
                    continue
                if z==y or z==x: # 去重
                    continue
                found = True
                break
            if found:
                break
        if found:
            break
    if found:
        break
print(t//s)
```

## 注意

1.读题**仔细** *wrong answer 先看看有没有弱智错误

2.**边界**情况：例如空数组、数组中只有一个元素、最大值和最小值等

3.**循环**条件和边界： 检查循环的条件和边界是否正确。确保不会死循环。保证在while的语境下要有**自增**。

4.变量名千万别重，注意**变量名**哪个是哪个，**行和列**要分清楚。

5.逻辑错误：尝试分析代码中的逻辑错误，可以手动模拟算法的执行步骤，或者使用示例输入数据来验证。

6.标志性打印语句：在代码中插入标志性的打印语句，以追踪代码的执行流程，找到问题所在。或者看**变量器**

（但是提交前别忘了注释掉）

7.正难则反：乌鸦坐飞机，剪绳子

8.确保输入和输出**格式正确**

9.回想一下有没有类似题做过，但不要生搬硬套

10.心态要稳，两个小时其实并不短，不急不躁正常发挥就问题不大。

11.注意输入的时候变量类型是str/float/int，是否需要**转化**？

12.if语句中使用and来并列的时候注意顺序，**管边界的要放在前面**。
