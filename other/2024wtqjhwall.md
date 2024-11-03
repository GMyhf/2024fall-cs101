

# 文科计算机基础实验班

Updated 1125 GMT+8 Nov 3, 2024

2024 fall, Complied by Hongfei Yan



# 2024问题求解作业汇总

http://wjjc.openjudge.cn/2024wtqjhwall/



## 24830: 最长下坡 done

http://cs101.openjudge.cn/practice/24830/

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



## 002 递归的二分查找 done

http://wjjc.openjudge.cn/2024wtqjhwall/002/

不得使用循环，只能使用递归，填空完成二分查找函数.

```
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

http://cs101.openjudge.cn/practice/08210/



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

http://wjjc.openjudge.cn/2024wtqjhwall/004/



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

http://cs101.openjudge.cn/practice/27528/



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







## 007	逃出迷宫





```python

```





## 008	简单的整数划分问题





## 009	The Sierpinski Fractal





```python

```





## 010	最值钱的背包





```python

```





## 011	复杂的整数划分问题





```python

```





## 012	时间处理





```python

```







## 013	条件排名(交能print输出结果的程序）





```python

```





## 014	条件排名(交原始程序)





```python

```





## 015	交易统计(交能print输出结果的程序）





```python

```





## 016	交易统计(交原始程序）





```python

```

