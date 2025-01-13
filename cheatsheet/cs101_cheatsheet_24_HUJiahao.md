# 期末机考复习

## Greedy

### two pointers:

two pointers 到底是怎样的一种思想？事实上，two pointers 最原始的含义就是针对本节第一个问题而言的，而广义上的 two pointers 则是利用问题本身与序列的特性，使用两个下标i、j对序列进行扫描（可以同向扫描，也可以反向扫描），以较低的复杂度（一般是 O(n)的复杂度）解决问题。在实际编程时要能够有使用这种思想的意识。

### binary search:

大的有序数集

```python
# 代码示例
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:  # 注意这里是<=
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # 返回目标元素的索引
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # 如果未找到目标元素，返回 -1

# 示例
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8
result = binary_search(arr, target)
print(f"Target {target} found at index {result}")
# Target 8 found at index 7
```

bisect的用法

bisect_left and bisect_right

**基本用法**

```python
import bisect

# 已排序的列表
arr = [1, 3, 4, 4, 5, 6]

# 使用 bisect_left 查找元素 4 应该插入的位置
index_left = bisect.bisect_left(arr, 4)
print(index_left)  # 输出: 2（4的第一个位置）

# 使用 bisect_right 查找元素 4 应该插入的位置
index_right = bisect.bisect_right(arr, 4)
print(index_right)  # 输出: 4（4的最后一个位置）

# 查找元素 2 应该插入的位置
index_insert = bisect.bisect(arr, 2)
print(index_insert)  # 输出: 1（2插入的位置）

```

**输出：**

```python
2
4
1
```



## enumerate

`enumerate` 是 Python 内置的一个函数，它用于将一个可迭代对象（如列表、元组或字符串）组合为一个索引序列，这个索引序列中的每个元素是一个元组，元组的第一个值是该元素的索引（位置），第二个值是该元素的值。

**基本用法**

```python
# 示例：使用 enumerate 遍历列表
my_list = ['apple', 'banana', 'cherry']

for index, value in enumerate(my_list):
    print(index, value)
```

**输出：**

```python
0 apple
1 banana
2 cherry
```



## 堆（heapq）

`heapq` 模块实现的是**最小堆**，即每次从堆中弹出最小的元素。

### `heapq` 的常用操作

**heapq.heappush(heap, item)**: 将元素 `item` 推入堆中。时间复杂度是 O(log n)。

**heapq.heappop(heap)**: 弹出堆中的最小元素，并保持堆的性质。时间复杂度是 O(log n)。

**heapq.heappushpop(heap, item)**: 推入新元素 `item` 并弹出堆中的最小元素。时间复杂度是 O(log n)。

**heapq.heapreplace(heap, item)**: 弹出堆中的最小元素，并将 `item` 推入堆中。时间复杂度是 O(log n)。

**heapq.nlargest(n, iterable)**: 返回 `iterable` 中的 n 个最大元素。

**heapq.nsmallest(n, iterable)**: 返回 `iterable` 中的 n 个最小元素。

```python
import heapq

# 创建一个空堆
heap = []

# 添加元素
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

# 弹出最小元素
print(heapq.heappop(heap))  # 输出 1
print(heapq.heappop(heap))  # 输出 2
print(heapq.heappop(heap))  # 输出 3
```

e.g 1526C1 CF



## Intervals

### 1 区间合并

#### 1.1 题意描述

区间合并问题大概**题意**就是：

给出一堆区间，要求**合并**所有**有交集的区间** （端点处相交也算有交集）。最后问合并之后的**区间**。

如下图所示：

[![img](https://camo.githubusercontent.com/0e350b8ff5ecaf8c148e015b6e421864e84d9a12386a9d63a71e29d3d16e1dbc/68747470733a2f2f706963342e7a68696d672e636f6d2f38302f76322d36653362623539656436633134656163666131333331633634356434616664665f31343430772e6a7067)](https://camo.githubusercontent.com/0e350b8ff5ecaf8c148e015b6e421864e84d9a12386a9d63a71e29d3d16e1dbc/68747470733a2f2f706963342e7a68696d672e636f6d2f38302f76322d36653362623539656436633134656163666131333331633634356434616664665f31343430772e6a7067)

区间合并问题示例：合并结果包含3个区间

#### 1.2 解题步骤

【**步骤一**】：按照区间**左端点**从小到大排序。

【**步骤二**】：维护前面区间中最右边的端点为ed。从前往后枚举每一个区间，判断是否应该将当前区间视为新区间。

假设当前遍历到的区间为第i个区间 [li,ri]，有以下两种情况：

- li≤ed：说明当前区间与前面区间**有交集**。因此**不需要**增加区间个数，但需要设置 ed=max(ed,ri)。
- li>ed: 说明当前区间与前面**没有交集**。因此**需要**增加区间个数，并设置 ed=max(ed,ri)。

### 2 选择不相交区间

#### 2.1 题意描述

**选择不相交区间问题**大概题意就是：

给出一堆区间，要求选择**尽量多**的区间，使得这些区间**互不相交**，求可选取的区间的**最大数量**。这里端点相同也算有重复。

如下图所示：

[![img](https://camo.githubusercontent.com/2dc533ce376bd15b39587b6618320d00e570ced6203accc4873315df133f4564/68747470733a2f2f706963312e7a68696d672e636f6d2f38302f76322d36393066376535336664333463333938303266343566343862353964356335615f31343430772e77656270)](https://camo.githubusercontent.com/2dc533ce376bd15b39587b6618320d00e570ced6203accc4873315df133f4564/68747470733a2f2f706963312e7a68696d672e636f6d2f38302f76322d36393066376535336664333463333938303266343566343862353964356335615f31343430772e77656270)

选择不相交区间问题示例：结果包含3个区间

#### 2.2 解题步骤

【**步骤一**】：按照区间**右端点**从小到大排序。

【**步骤二**】：从前往后依次枚举每个区间。

假设当前遍历到的区间为第i个区间 [li,ri]，有以下两种情况：

- li≤ed：说明当前区间与前面区间有交集。因此直接跳过。
- li>ed: 说明当前区间与前面没有交集。因此选中当前区间，并设置 ed=ri。

### 3 区间选点问题

#### 3.1 题意描述

**区间选点问题**大概题意就是：

给出一堆区间，取**尽量少**的点，使得每个区间内**至少有一个点**（不同区间内含的点可以是同一个，位于区间端点上的点也算作区间内）。

如下图所示：

[![img](https://camo.githubusercontent.com/66ab2da6ceb1201d6fe916fab8a0e81392c7d174caee8a288c148484aacb1c04/68747470733a2f2f706963612e7a68696d672e636f6d2f38302f76322d61376566303231653131393165633533663230363039626138373062343462615f31343430772e77656270)

**与上一问完全相同**

### 4 区间覆盖问题

#### 4.1 题意描述

**区间覆盖问题**大概题意就是：

给出一堆区间和一个目标区间，问最少选择多少区间可以**覆盖**掉题中给出的这段目标区间。

如下图所示：

[![img](https://camo.githubusercontent.com/04a9b706eb35a148dd3582449d774249276673c3f28d7d61d3a52f008849482d/68747470733a2f2f706963332e7a68696d672e636f6d2f38302f76322d36363034316439393431363637343832666335316164656234613631366636345f31343430772e77656270)](https://camo.githubusercontent.com/04a9b706eb35a148dd3582449d774249276673c3f28d7d61d3a52f008849482d/68747470733a2f2f706963332e7a68696d672e636f6d2f38302f76322d36363034316439393431363637343832666335316164656234613631366636345f31343430772e77656270)

区间覆盖问题示例，最终至少选择2个区间才能覆盖目标区间

#### 4.2. 解题步骤

【**步骤一**】：按照区间左端点从小到大排序。

**步骤二**】：**从前往后**依次枚举每个区间，在所有能覆盖当前目标区间起始位置start的区间之中，选择**右端点**最大的区间。

假设右端点最大的区间是第i个区间，右端点为 ri。

最后将目标区间的start更新成ri

### 5 区间分组问题

#### 5.1 题意描述

**区间分组**问题大概题意就是：给出一堆区间，问最少可以将这些区间分成多少组使得每个组内的区间互不相交。

如下图所示：

[![img](https://camo.githubusercontent.com/e9c9db829c87cffcfd601b481ece465482fb8f6a9a22a87cb2d0676ea85d70d5/68747470733a2f2f706963322e7a68696d672e636f6d2f38302f76322d36633661303435643438316464633434633636623034366566336537643463645f31343430772e77656270)](https://camo.githubusercontent.com/e9c9db829c87cffcfd601b481ece465482fb8f6a9a22a87cb2d0676ea85d70d5/68747470733a2f2f706963322e7a68696d672e636f6d2f38302f76322d36633661303435643438316464633434633636623034366566336537643463645f31343430772e77656270)

区间分组问题示例，最少分成3个组

#### 5.2. 解题步骤

【**步骤一**】：按照区间**左端点从小到大**排序。



## 进制转换

### 十进制转换成其他

#### bin()  return  '0bxxx'

#### oct()  return '0oxxx'

#### hex()  return '0xxxx'

### 其他转化为十进制

#### int()

int(n,base) base=2,8,16

**也可以自己定义函数**

```python
def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_str(n // base, base) + convert_string[n % base]
```



## 背包问题DP

### 5.1 0-1背包（每个物品选或者不选）

用子问题定义状态：即 CELL[i][j] 表示前 i 件物品恰放入一个容量为 j 的背包可以获得的最大价值。则其状态转移方程便是：

CELL[i] [j]=max(CELL [i−1] [j];CELL [i−1] [j−Wi]+Vi)

这个方程非常重要，基本上所有跟背包相关的问题的方程都是由它衍生出来的。所以有必要将它详细解释一下：“将前 `i` 件物品放入容量为 `j` 的背包中”这个子问题，若只考虑第 `i` 件物品的策略（放或不放），那么就可以转化为一个只和前 `i − 1` 件物品相关的问题。如果不放第 `i` 件物品，那么问题就转化为“前 `i − 1` 件物品放入容量为 j 的背包中”，价值为 CELL[i−1] [j]；如果放第 `i` 件物品，那么问题就转化为“前 `i − 1` 件物品放入剩下的容量为 j−Wi 的背包中”，此时能获得的最大价值就是 CELL[i−1] [j−Wi] 再加上通过放入第 `i` 件物品获得的价值 `Vi`。

### 滚动数组优化空间复杂度

由于对 f_i有影响的只有 f{i-1}，可以去掉第一维，直接用 f_{i}来表示处理到当前物品时背包容量为 i的最大价值，得出以下方程：

fj=max(fj,fj−wi+vi)

为了避免这种情况发生，我们可以改变枚举的顺序，从 W 枚举到 wi，这样就不会出现上述的错误，因为 fi,j 总是在 fi,j−wi 前被更新。

因此实际核心代码为

```python
for i in range(1, n + 1):
    for l in range(W, w[i] - 1, -1):
        f[l] = max(f[l], f[l - w[i]] + v[i])
```

### 5.2 完全背包（每种物品可以选0个-无限个）

将0-1背包中内层循环改为正着遍历即可（这里其实就利用了**先前已经得到的信息**来简化转移：在先前的转移中物品i可能已经用过若干次了）

**e.g.完全背包问题**

思路：就是一个需要刚好装满的完全背包问题，只有三种商品a, b, c，能取无限件物品，每件物品价值是1，求最大价值。

```python
n, a, b, c = map(int, input().split())
dp = [0]+[float('-inf')]*n

for i in range(1, n+1):
    for j in (a, b, c):
        if i >= j:
            dp[i] = max(dp[i-j] + 1, dp[i])

print(dp[n])
```



## 最大连续子序列和

通过设置这么一个 dp 数组，要求的最大和其实就是 dp[0],dp[1],··，dp[n-1]中的最大值，想办法求解 dp 数组。因为 dp[i]要求是必须以 A[i]结尾的连续序列，那么只有两种情况:

①这个最大和的连续序列只有一个元素，即以 A[i]开始，以 A[i]结尾。

②这个最大和的连续序列有多个元素，即从前面某处 A[p]开始(p<i)，一直到 A[i]结尾。

对第一种情况，最大和就是 A[i]本身。

对第二种情况，最大和是 dp[i-1]+A[i]，即 A[p]+...+A[i-1]+A[i]=dp[i-1]+A[i]。

由于只有这两种情况，于是得到**状态转移方程**:

dp[i]=max(A[i],dp[i−1]+A[i])

这个式子只和`i`与`i之前`的元素有关，且边界为 `dp[0]=A[0]`，由此从小到大枚举i，即可得到整个 dp 数组。接着输出 dp[0],dp[1]....,dp[n-1]中的最大值即为最大连续子序列的和。

```python
n = int(input())
*a, = map(int, input().split())

dp = [0]*n
dp[0] = a[0]

for i in range(1, n):
    dp[i] = max(dp[i-1]+a[i], a[i])

print(max(dp))
```

题目：最大子矩阵

**Kadane's Algorithm**

```python
'''
为了找到最大的非空子矩阵，可以使用动态规划中的Kadane算法进行扩展来处理二维矩阵。
基本思路是将二维问题转化为一维问题：可以计算出从第i行到第j行的列的累计和，
这样就得到了一个一维数组。然后对这个一维数组应用Kadane算法，找到最大的子数组和。
通过遍历所有可能的行组合，我们可以找到最大的子矩阵。
'''
def max_submatrix(matrix):
    def kadane(arr):
        max_end_here = max_so_far = arr[0]
        for x in arr[1:]:
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



## 最大上升子序列/字串

```python
n = int(input())
*b, = map(int, input().split())
dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if b[j] < b[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
```



## 最长公共子串

```python
if word_a[i]==word_b[j]:
    cell[i][j]=cell[i-1][j-1]+1
else:
    cell[i][j]=0
```

## 最长公共子序列

```python
if word_a[i]==word_b[j]:
    cell[i][j]=cell[i-1][j-1]+1
else:
    cell[i][j]=max(cell[i-1][j],cell[i][j-1])
```



## dfs 迷宫问题（模板）

```python
dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0, -1]

def dfs(maze, x, y):
    global cnt
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
            
        if maze[nx][ny] == 'e':
            cnt += 1
            continue
            
        if maze[nx][ny] == 0:
            maze[x][y] = 1
            dfs(maze, nx, ny)
            maze[x][y] = 0
    
    return
```

dfs辅助visited空间+如何标记路径

```python
# 读取输入
n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]

# 定义方向
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右、下、左、上
visited = [[False] * m for _ in range(n)]  # 标记访问
max_path = []
max_sum = -float('inf')  # 最大权值初始化为负无穷

# 深度优先搜索
def dfs(x, y, current_path, current_sum):
    global max_path, max_sum

    # 到达终点，更新结果
    if (x, y) == (n - 1, m - 1):
        if current_sum > max_sum:
            max_sum = current_sum
            max_path = current_path[:]
        return

    # 遍历四个方向
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # 检查边界和是否访问过
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            # 标记访问
            visited[nx][ny] = True
            current_path.append((nx, ny))

            # 递归搜索
            dfs(nx, ny, current_path, current_sum + maze[nx][ny])

            # 回溯
            current_path.pop()
            visited[nx][ny] = False

# 初始化起点
visited[0][0] = True
dfs(0, 0, [(0, 0)], maze[0][0])

# 输出结果
for x, y in max_path:
    print(x + 1, y + 1)
```



## bfs(模板)

```python
from collections import deque
def bfs(x, y):
    q = deque([(x, y)])
    inq_set.add((x,y))
    while q:
        front = q.popleft()
        for i in range(MAXD):
            next_x = front[0] + dx[i]
            next_y = front[1] + dy[i]
            if matrix[next_x][next_y] == 1 and (next_x,next_y) not in inq_set:
                inq_set.add((next_x, next_y))
                q.append((next_x, next_y))
```



## 深拷贝

 小知识：二维数组需要深度拷贝：import copy；A=copy.deepcopy(X)。



## 语法

### 一·函数

### 输出

print(f'{ans},{res:.1f}')print是可以带sep和end参数的

### 字符串

str.title()首字母大写（每个单词） str.lower()/upper()每个字母小/大写 str.strip()去除空格，有rstrip/lstrip去掉尾部/头部的空格

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

```
a = [1, 2, 3]
b = ['a', 'b', 'c']
zipped = list(zip(a, b))
print(zipped) # 输出: [(1, 'a'), (2, 'b'), (3, 'c')]
```

#### 字典

key和value都可以是任意类型的东西（不过key一定要是不可变的，比如list不能作为key；但用list作为value是非常常见的）。

把有些信息用字典提前存下来，在需要的时候直接访问，有时是降低时间复杂度的好办法。但是有MLE的风险

如果要按顺序遍历通常用for x in sorted(dict.keys()/values())

dict.keys()/values()/items()分别返回键/值/键值对列表

dict.get(key,default=None)查找指定key的value，如果key不存在不会报错而是返回给定的默认值

dict.pop(key,default=None)弹出指定键值对

如果key已经存在，再赋值时会直接覆盖。



## 欧拉筛和埃氏筛

**埃氏筛**

```python
s=[True]*int(pow(10,6)+1)
s[0]=s[1]=False
for i in range(2,int(pow(10,6)+1)):
    if s[i]:
        for j in range(int(pow(i,2)),int(pow(10,6)+1),i):
            s[j]=False
```



## 递归的两种优化方法（扩展深度和减少重复运算）

####  递归程序优化两板斧

递归程序在处理大规模问题时经常会遇到两个主要问题：**递归深度限制** 和 **重复计算子问题**。这两个问题可以通过以下两种方法来解决：

**增加递归深度限制**：使用 `sys.setrecursionlimit` 来增加 Python 的递归深度限制。

**缓存中间结果**：使用 `functools.lru_cache` 或其他形式的 memoization（记忆化）来避免重复计算。

Python 默认的递归深度限制是 1000，对于某些问题来说可能不够。你可以通过 `sys.setrecursionlimit` 来增加这个限制。

```python
import sys
sys.setrecursionlimit(1 << 30)  # 将递归深度限制设置为 2^30
```

使用 `functools.lru_cache` 可以缓存函数的返回值，从而避免重复计算相同的子问题。这对于递归算法尤其有用，可以显著提高性能。

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def recursive_function(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return recursive_function(n - 1) + recursive_function(n - 2)
```



## 题目

leetcode72.编辑距离 **dp**

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1,n2=len(word1),len(word2)
        dp=[[0 for _ in range(n2+1)] for _ in range(n1+1)]
        for j in range(1,n2+1):
            dp[0][j]=dp[0][j-1]+1
        for i in range(1,n1+1):
            dp[i][0]=dp[i-1][0]+1
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
        return dp[-1][-1]
```





