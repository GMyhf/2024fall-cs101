

# 文科计算机基础实验班

Updated 1125 GMT+8 Nov 3, 2024

2024 fall, Complied by Hongfei Yan



# 2024问题求解作业汇总

http://wjjc.openjudge.cn/2024wtqjhwall/



## 24830: 最长下坡

implementation, http://cs101.openjudge.cn/practice/24830/

小明天天沿着未名湖环湖路跑，有时候也觉得蛮累。
累的时候跑下坡就很开心。小明想知道最长的一段下坡有多长。
环湖路是个圆形，周长n米。每隔一米测一下路面高度，两个测高点之间的高度是单调变化或不变的。
问最长的一段下坡有多少米长。小明只能顺时针跑。下坡必须高度单调减少。

**输入**

第一行是整数n，表示环湖路一共n米长(2<=n<=100)。
第二行是n个整数，每个整数范围[0,10000]，按顺时针顺序给出了n个测高点的高度

**输出**

最长下坡路段的长度

样例输入

```
样例输入1:
5
2 1 5 6 3
样例输入2：
5
2 1 5 4 3
样例输入3:
4 
1 1 1 1
```

样例输出

```
样例输出1：
3
样例输出2
4
样例输出3
0
```

提示

这是个简单枚举题，枚举起点即可

来源

Guo Wei



```python
def longest_descending_segment(n, heights):
    max_length = 0
    current_length = 0

    # 我们将环形处理成一个线性遍历，复制一份高度数组来模拟环形
    extended_heights = heights + heights
    
    for i in range(2 * n - 1):  # 遍历两圈，确保环形特性
        if extended_heights[i] > extended_heights[i + 1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
            
    return max_length

# 输入
n = int(input().strip())
heights = list(map(int, input().strip().split()))

# 输出最长下坡路段的长度
print(longest_descending_segment(n, heights))
```



## 002: 递归的二分查找

binary search, http://wjjc.openjudge.cn/2024wtqjhwall/002/

不得使用循环，只能使用递归，填空完成二分查找函数.

```python
def binarySearch(a ,p,key = lambda x :x ):
	def search(L,R): #在a[L:R+1]范围内二分查找p
// 在此处补充你的代码
#下面这一行是函数binarySearch的最后一条语句
	return search(0,len(a) - 1)
a = [9, 12, 27, 33, 33, 41, 80]  #a有序
print(binarySearch(a,33)) #>>3
print(binarySearch(a,57)) #>>None
a.sort(key = lambda x: x % 10)  #按个位数从小到大排序
print(a)    #>>[80, 41, 12, 33, 33, 27, 9]
print(binarySearch(a,57,key = lambda x: x %10)) #>>5
```

**输入**

无

**输出**

3
None
[80, 41, 12, 33, 33, 27, 9]
5

样例输入

```
无
```

样例输出

```
3
None
[80, 41, 12, 33, 33, 27, 9]
5
```

来源

Guo Wei



因为OJ格式问题，提交代码search函数需要多一个tab缩进。

```python
def binarySearch(a ,p,key = lambda x :x ):
	def search(L,R): #在a[L:R+1]范围内二分查找p
            if L > R:
                return None
            mid = (L + R) // 2
            if key(a[mid]) == key(p):
                return mid
            elif key(a[mid]) > key(p):
                return search(L, mid - 1)
            else:
                return search(mid + 1, R)
#下面这一行是函数binarySearch的最后一条语句
	return search(0,len(a) - 1)
a = [9, 12, 27, 33, 33, 41, 80]  #a有序
print(binarySearch(a,33)) #>>3
print(binarySearch(a,57)) #>>None
a.sort(key = lambda x: x % 10)  #按个位数从小到大排序
print(a)    #>>[80, 41, 12, 33, 33, 27, 9]
print(binarySearch(a,57,key = lambda x: x %10)) #>>5
```





## 08210: 河中跳房子

binary search, http://cs101.openjudge.cn/practice/08210/



```python
L,n,m = map(int,input().split())
rock = [0]
for i in range(n):
    rock.append(int(input()))
rock.append(L)

def check(x):
    num = 0
    now = 0
    for i in range(1, n+2):
        if rock[i] - now < x:
            num += 1
        else:
            now = rock[i]
            
    if num > m:
        return True
    else:
        return False

# https://github.com/python/cpython/blob/main/Lib/bisect.py
'''
2022fall-cs101，刘子鹏，元培。
源码的二分查找逻辑是给定一个可行的下界和不可行的上界，通过二分查找，将范围缩小同时保持下界可行而区间内上界不符合，
但这种最后print(lo-1)的写法的基础是最后夹出来一个不可行的上界，但其实L在这种情况下有可能是可行的
（考虑所有可以移除所有岩石的情况），所以我觉得应该将上界修改为不可能的 L+1 的逻辑才是正确。
例如：
25 5 5
1
2
3
4
5

应该输出 25
'''
# lo, hi = 0, L
lo, hi = 0, L+1
ans = -1
while lo < hi:
    mid = (lo + hi) // 2
    
    if check(mid):
        hi = mid
    else:               # 返回False，有可能是num==m
        ans = mid       # 如果num==m, mid可能是答案
        lo = mid + 1
        
#print(lo-1)
print(ans)
```





## 004: 蜜蜂

dp, http://wjjc.openjudge.cn/2024wtqjhwall/004/



```python
def count_routes(a, b):
    # Initialize a list to store the number of ways to reach each hive
    dp = [0] * (b + 1)
    dp[a] = 1  # There's one way to be at the starting hive

    # Fill the dp array
    for i in range(a, b):
        dp[i + 1] += dp[i]
        if i + 2 <= b:
            dp[i + 2] += dp[i]

    return dp[b]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    results = []

    index = 1
    for _ in range(N):
        a = int(data[index])
        b = int(data[index + 1])
        results.append(count_routes(a, b))
        index += 2

    for result in results:
```





## 27528: 跳台阶

dp, http://cs101.openjudge.cn/practice/27528/



```python
def count_ways(N):
    if N == 1:
        return 1
    dp = [0] * (N + 1)
    dp[0] = 1  # Base case: 1 way to stay at the ground (0 steps)
    
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            dp[i] += dp[i - j]
    
    return dp[N]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    N = int(input().strip())
    print(count_ways(N))
```





## 006: 九宫格摆数

http://wjjc.openjudge.cn/2024wtqjhwall/006/

一个3×3的网格，共有9个格子，分为3行，每行3列。

输入9个整数，要求将这些整数摆放到网格里面，每个格子放一个数，使得每行的数的和都相等，且每列的数的和也都相等(行的和与列的和可以不相等）。问有多少种不同的摆法。虽然9个数里可能有大小相等的，但是9个数的颜色都不一样，所以应该视为这9个数都不相同。例如，即便输入9个1,由于这9个1颜色都不一样，所以不同的摆法共有9!种。

**输入**

9个整数

**输出**

合法的摆法数量

样例输入

```
#输入样例1：
1 1 1 1 1 1 1 1 1
#输入样例2
1 2 3 4 5 6 7 8 9
#输入样例3
1 2 3 4 5 6 7 8 100
```

样例输出

```
#输出样例1
362880
#输出样例2
72
#输出样例3
0
```

来源

Guo Wei



```python
from itertools import permutations

def is_valid_grid(grid):
    # Check rows
    row_sums = [sum(grid[i*3:(i+1)*3]) for i in range(3)]
    # Check columns
    col_sums = [sum(grid[i::3]) for i in range(3)]
    return len(set(row_sums)) == 1 and len(set(col_sums)) == 1

# Read the 9 integers
numbers = list(map(int, input().split()))

# Generate all permutations of the 9 integers
all_permutations = permutations(numbers)

# Count the number of valid permutations
valid_count = sum(1 for perm in all_permutations if is_valid_grid(perm))

# Print the count of valid permutations
print(valid_count)
```







## 007: 逃出迷宫

recursion, http://wjjc.openjudge.cn/2024wtqjhwall/007/

"Boom!" 小锅一觉醒来发现自己落入了一个N*N(2 <= N <= 20)的迷宫之中，为了逃出这座迷宫，小锅需要从左上角(0, 0)处的入口跑到右下角(N-1, N-1)处的出口逃出迷宫。由于小锅每一步都想缩短和出口之间的距离，所以**他只会向右和向下走**。假设我们知道迷宫的地图（以0代表通路，以1代表障碍），请你编写一个程序，判断小锅能否从入口跑到出口？

例如，对于下图所示的迷宫：

<img src="http://media.openjudge.cn/images/upload/6090/1639660715.png" alt="img" style="zoom:33%;" />

小锅可以如下图红线所示从迷宫左上角的入口抵达迷宫右下角的出口：

<img src="http://media.openjudge.cn/images/upload/2830/1639660728.jpg" alt="img" style="zoom:33%;" />

输入

第一行为一个整数N，代表迷宫的大小
接下来N行为迷宫地图，迷宫地块之间以空格分隔
输入保证(0, 0)和(N - 1, N - 1)处可以通过

输出

一行字符串，如果能跑到出口则输出Yes，否则输出No

样例输入

```
5
0 0 1 1 0
0 0 0 0 0
0 1 1 1 0
0 1 1 1 0
0 1 1 1 0
```

样例输出

```
Yes
```

提示

用递归解。设计函数ok(r,c)，返回True或False，表示从位置(r,c)出发能否走到终点。
从(r,c）出发可以想办法往前走一步，然后看问题变成什么

题目说了只能走到0的格子，不能走到1的格子



**Pseudocode:**

1. Define a function `ok(r, c)` that returns `True` if it is possible to reach the exit from position `(r, c)`.
2. Base case: If `(r, c)` is the exit `(N-1, N-1)`, return `True`.
3. If `(r, c)` is out of bounds or is an obstacle, return `False`.
4. Mark the current cell `(r, c)` as visited by setting it to 1.
5. Recursively check if it is possible to reach the exit by moving right or down.
6. If either move leads to the exit, return `True`.
7. If neither move leads to the exit, return `False`.

**Code:**
```python
def can_escape_maze(maze, N):
    def ok(r, c):
        # Base case: if we reach the exit
        if r == N - 1 and c == N - 1:
            return True
        # If out of bounds or on an obstacle, return False
        if r >= N or c >= N or maze[r][c] == 1:
            return False
        # Mark the current cell as visited
        maze[r][c] = 1
        # Recursively check right and down
        if ok(r, c + 1) or ok(r + 1, c):
            return True
        return False

    return "Yes" if ok(0, 0) else "No"

# Read input
N = int(input().strip())
maze = [list(map(int, input().strip().split())) for _ in range(N)]

# Output result
print(can_escape_maze(maze, N))
```



## 04117: 简单的整数划分问题

dp, http://cs101.openjudge.cn/practice/04117/



```python
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

# 输入处理部分
try:
    while True:
        N = int(input())
        print(partition_count(N))
except EOFError:
    pass
```







## 01941: The Sierpinski Fractal done

http://cs101.openjudge.cn/practice/01941/



```python
def f(n):
    if n == 1:
        return [' /\\ ', '/__\\']
    t = f(n - 1)
    x = 2 ** (n - 1)
    res = [' ' * x + u + ' ' * x for u in t]
    res.extend([u + u for u in t])
    return res


al = [f(i) for i in range(1, 11)]
while True:
    n = int(input())
    if n == 0:
        break
    for u in al[n - 1]:
        print(u)
    print()
```





## 010: 最值钱的背包

dp, http://wjjc.openjudge.cn/2024wtqjhwall/010/



阿里巴巴有一个背包，最多只能装下重量为M( 0 < M <=10000)的物品。他在山洞里发现N件宝贝（0<N<=100)，每件宝贝有一定的重量W和价值D(0<W<=400,0<D<=100)，问阿里巴巴的背包最多能装下价值多少的宝贝。

**输入**

第一行是N和M，分别代表宝贝数量和背包的承重
接下来有N行，每行是两个整数，代表一件宝贝的重量和价值

**输出**

阿里巴巴能够获取的最大宝贝价值之和

样例输入

```
4 6
1 4
2 6
3 12
2 7
```

样例输出

```
23
```



```python
# Read the number of items and the maximum weight capacity
N, M = map(int, input().split())

# Initialize a list to store the weights and values of the items
items = []

# Read the weights and values of the items
for _ in range(N):
    W, D = map(int, input().split())
    items.append((W, D))

# Initialize the dp list
dp = [0] * (M + 1)

# Iterate through each item
for W, D in items:
    # Iterate through the weight capacities from M down to W
    for j in range(M, W - 1, -1):
        dp[j] = max(dp[j], dp[j - W] + D)

# Print the maximum value that can be achieved with the given weight capacity
print(dp[M])
```





## 04119: 复杂的整数划分问题

dp, http://cs101.openjudge.cn/practice/04119/



```python
def partition_count(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - j][j]
    return dp[n][k]

def distinct_partition_count(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(n, i - 1, -1):
            dp[j] += dp[j - i]
    return dp[n]

def odd_partition_count(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1, 2):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]
    return dp[n]

# Read input
import sys
input = sys.stdin.read
data = input().strip().split()
test_cases = [(int(data[i]), int(data[i + 1])) for i in range(0, len(data), 2)]

# Process each test case
for N, K in test_cases:
    print(partition_count(N, K))
    print(distinct_partition_count(N))
    print(odd_partition_count(N))
```



```python
# https://blog.csdn.net/hejnhong/article/details/105211551
def divide_k(n, k):
    # dp[i][j]为将i划分为j个正整数的划分方法数量
    dp = [[0]*(k+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][1] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            if i >= j:
                # dp[i-1][j-1]为包含1的划分的数量
                # 若不包含1，我们对每个数-1仍为正整数，划分数量为dp[i-j][j]
                dp[i][j] = dp[i-j][j]+dp[i-1][j-1]
    return dp[n][k]


def divide_dif(n):
    # dp[i][j]表示将数字 i 划分，其中最大的数字不大于 j 的方法数量
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 比i大的数没用
            if i < j:
                dp[i][j] = dp[i][i]
            # 多了一种：不划分
            elif i == j:
                dp[i][j] = dp[i][j - 1] + 1
            # 用/不用j
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - j][j - 1]
    return dp[n][n]


# 关于分拆数的一个结论，https://zhuanlan.zhihu.com/p/21440865
# 一个数的奇分拆总是等于互异分拆
def divide_odd(n):
    # dp[i][j]整数i的划分里最大的数是j
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j % 2 == 0:
                dp[i][j] = dp[i][j-1]
            else:
                if i < j:
                    dp[i][j] = dp[i][i]
                elif i == j:
                    dp[i][j] = dp[i][j - 1] + 1
                # 用/不用j
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - j][j]

    return dp[n][n]


while True:
    try:
        n, k = map(int, input().split())
        print(divide_k(n, k))
        print(divide_dif(n))
        print(divide_odd(n))
    except EOFError:
        break

```





## 012: 时间处理

http://wjjc.openjudge.cn/2024wtqjhwall/012/

求从给定时刻开始过了给定时间后的时刻。

**输入**

有若干组数据。
每组数据有2行，第一行是给定时刻，可能有两种格式
格式1) 年 月 日 时 分(时是24小时制)
格式2) 月-日-年 时:分 上下午 （时是12小时制,注意没有秒)
第二行是时间增量，也可能有两种格式
格式1) 一个整数，代表多少秒
格式2) 日 时 分

**输出**

对每组数据，输出给定时刻加上时间增量后的新时刻,24小时制
格式如： 1982-12-10 12:12:28

样例输入

```
1982 12 1 23 0
737848
1982 12 1 23 15
180 2 18
12-01-1982 1:23 AM
737848
```

样例输出

```
1982-12-10 11:57:28
1983-05-31 01:33:00
1982-12-09 14:20:28
```

来源

Guo wei



```python
from datetime import datetime, timedelta
import sys

def parse_input_time(input_time):
    try:
        # 尝试解析格式1: 年 月 日 时 分
        return datetime.strptime(input_time, "%Y %m %d %H %M")
    except ValueError:
        # 如果失败，尝试解析格式2: 月-日-年 时:分 上下午
        return datetime.strptime(input_time, "%m-%d-%Y %I:%M %p")

def parse_time_increment(time_increment):
    parts = time_increment.split()
    
    if len(parts) == 1:
        # 格式1: 一个整数，代表多少秒
        return timedelta(seconds=int(parts[0]))
    else:
        # 格式2: 日 时 分
        days = int(parts[0])
        hours = int(parts[1])
        minutes = int(parts[2])
        return timedelta(days=days, hours=hours, minutes=minutes)

def main():
    for line in sys.stdin:
        # 读取给定时刻
        input_time = line.strip()
        input_time = parse_input_time(input_time)
        
        # 读取时间增量
        time_increment = input().strip()
        delta = parse_time_increment(time_increment)
        
        # 计算新的时刻
        new_time = input_time + delta
        
        # 输出结果
        print(new_time.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    main()

```







