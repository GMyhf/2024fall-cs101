

# Cheat Sheet For Algo CS

Compiled by Charlie Wei;PKU CUES

## 1.基础语法部分

---

1. `for` 和 `if` 加冒号, `break` 是可以退出整个循环，而 `continue` 则是跳过当前部分的剩余部分, 继续向下遍历，`for i in range`是索引不加`range`是`i`依次取`list`的值，注意`len(list)`以及`range`函数只读取整数，`[start,end,step]`要考虑左开右闭

2. `a % b` 返回 a 除以 b 的余数（注意判断奇偶用这个 还有就是记得如果只要整数加`int`）。`a // b` 返回 a 除以 b 的整数结果(向下取整后的整数部分), 使用 `math.sqrt(x)` 计算 x 的平方根。`a ** b` 表示 a 的 b 次幂。开其他次根使用分层运算符如 `x ** (1/n)` 可以计算 x 的 n 次根。

3. `Math.ceil()` 向上取整 `strip` 去除字符串两端的空白字符 `split` 分开 `map` 类似于重置字符类型 `upper` 大写 `lower` 小写 `range` 范围类只能读取整数

4. 第⼀行输入 n, 第二行输入 n 个结果的做法: 第二行创个列表 `a = list(map(int, input().split()))`

    或者直接例如这样：`n, *rib = map(int, input().split())`

    第一行输入n，n行一直输入的做法：

    ```python
    n = input() 
    compress = [] 
    for _ in range(n):
        a = input().split() # 后面括号可有可无 
        compress.append(a)
    ```

5. 列表内容⾏内输出。直接 `print` 或者...

     如 `my_list = ['apple', 'banana', 'cherry']`

    ```python
    result = " ".join(my_list) # 用空格连接
    print(result) # 输出: apple banana cherry
    ```

6. 列表内容多行输出: 已有列表 `results` 然后 `for result in results: print(result)`

7. 指针计数器 Count 进⾏比较可以考虑设定一个前置指针(位置一定是1) 然后遍历循环变量 i 从第二个元素开始 注意从 0 开始哈 若有交集问题可以考虑布尔值

8. `while True:` 创建一个无限循环:
   
    ```python
    While True:
    n = int(input()) # 从用户输入读取一个整数并将其赋值给 n
    if n == 0: # 检查 n 是否为 0
        break # 如果 n 等于 0, 则退出循环
    ```
    
9. `f-string` 格式化字符串 `f"{变量:.nf}"` 来保留 `n` 位小数

10. 编码字符串题目中 比如 `aaabbbccceeee` 若没有最后一步的代码 在 `c` 不等于 `e` 时最后存储的信息会有遗漏(左闭右开)因为没有更新，因为没有进入 `else` 部分

    ```python
    for i in range(1, len(str1)):
        if str1[i] == last_str:
            count += 1
        else:
            compressed.append(f"{last_str}{count}")
            last_str = str1[i]
            count = 1
    compressed.append(f"{last_str}{count}")
    ```

11.以这串行为例子,`key=lambda`表示的是设置一个隐函数 意思是 这个`student_dict`是一个字典 `.items()`是一个字典的方法，它返回字典中的键值对，形式是 `(key, value)` 的元组。`x[1]`指的是`value`也就是对于元组中的变量`x`，有`x[0]`和`x[1]`分别代表`key`和`value`，要对`value`排序，调用外层的`sorted`函数

```python
sorted_students = sorted(student_dict.items(), key=lambda x: x[1])
```

```python
numbers = [5, 2, 9, 1, 7]
sorted_numbers = sorted(numbers) #升序
sorted_numbers = sorted(numbers, reverse=True) #降序
```

12.矩阵其实是n维数组 可以用None表示尚未赋值

```python
matrix = [ ] # 初始化一个 5x5 矩阵
for _ in range(5):# 输入矩阵
  row = list(map(int, input().split()))
  matrix.append(row)
```

13.计算曼哈顿距离：$$ D_{\text{Manhattan}}(P, Q) = \sum_{i=1}^{n} |p_i - q_i| $$

```python
#这里是二维
def manhattan_distance_2d(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)
# 示例
point1 = (1, 2)
point2 = (4, 6)
distance = manhattan_distance_2d(point1, point2)
print(f"曼哈顿距离: {distance}")  # 输出: 曼哈顿距离: 7
```

14.堆 (Heap)：适用于需要频繁插入和删除最小或最大元素的场景，heapq 模块提供了最小堆的实现。
栈 (Stack)：后进先出（LIFO）（正常的电梯）的数据结构，Python 列表（list）可以视作栈。
队列 (Queue)：先进先出（FIFO）（物美的电梯）的数据结构，collections.deque 提供了高效的双端队列实现。
heapq 模块：提供了**最小堆**的实现，适用于优先队列、Top K 问题(找到前 K 个最大或最小的元素)等

```python
#heapq.heappush(heap, item)：将 item 添加到堆中，并保持堆的性质 heapq.heappop(heap)：弹出并返回堆中的最小元素，并保持堆的性质 heapq.heapify(heap)：将一个普通列表转换为最小堆 heapq.heappushpop(heap, item)：先将 item 添加到堆中，然后弹出并返回堆中的最小元素 heapq.nsmallest(n, iterable)：返回 iterable 中最小的 n 个元素 heapq.nlargest(n, iterable)：返回 iterable 中最大的 n 个元素。
```

deque 模块：提供了**双端**队列，适用于需要从两端高效操作的场景，如队列、栈和滑动窗口

```python
#deque.append(x)：将元素 x 添加到队列的末尾 deque.appendleft(x)：将元素 x 添加到队列的开头 deque.pop()：移除并返回队列的最后一个元素 deque.popleft()：移除并返回队列的第一个元素 deque[0]：访问队列的第一个元素（不移除）len(deque)：获取队列的长度deque.clear()：清空队列
```

```python
#集合 (Set)：无序且不重复的元素集合，适合用于去重和集合运算。普通集合是可变的，而 frozenset 是不可变的集合，适用于需要不可变集合的场景。frozenset 是不可变的集合，一旦创建后，不能添加或删除元素。frozenset 支持集合运算，但不支持修改操作。
set1 = {1, 2, 3, 4, 5}# 使用花括号创建集合
set2 = {1, 2, 2, 3, 3, 4, 5} print(set2) # 重复的元素会被自动去除 # 输出: {1, 2, 3, 4, 5}
set3 = set()# 空集合必须使用 set() 函数创建，因为 {} 表示空字典
set4 = set([1, 2, 3, 4, 5]) set5 = set("hello") 
# 使用 set() 函数从其他可迭代对象创建集合 # 输出: {'h', 'e', 'l', 'o'}
#下列是集合的运算
set_a = {1, 2, 3, 4} set_b = {3, 4, 5, 6}
union_set = set_a | set_b print(union_set)  # 并集 # 输出: {1, 2, 3, 4, 5, 6}
intersection_set = set_a & set_b print(intersection_set) # 交集 # 输出: {3, 4}
difference_set = set_a - set_b print(difference_set) # 差集 # 输出: {1, 2}
# 对称差集（只包含两个集合中不同的元素） # 输出: {1, 2, 5, 6}
symmetric_difference_set = set_a ^ set_b print(symmetric_difference_set) 
```

```python
#元组 (Tuple)：有序且不可变的序列，适合用于存储不需要更改的数据。元组的不可变性使其在某些场景下具有性能优势，且可以作为字典的键
tuple1 = (1, 2, 3, 4, 5)# 使用圆括号创建元组
tuple2 = (1,) # 单个元素的元组需要加逗号 # 注意：(1) 不是元组，而是整数 1
tuple3 = ()# 空元组
tuple4 = tuple([1, 2, 3]) # 使用 tuple() 函数创建元组 # 从列表创建元组
# 尝试修改元组会导致错误
# tuple1[0] = 10  # TypeError: 'tuple' object does not support item assignment
# 修改元组的正确方式
new_tuple = list(tuple1)  # 将元组转换为列表   new_tuple[0] = 10         # 修改列表中的元素
tuple1 = tuple(new_tuple) # 将列表转换回元组   print(tuple1)  # 输出: (10, 2, 3, 4, 5)
```

15.深拷贝和浅拷贝

```python
import copy
# 定义一个包含子列表的原始列表
original_list = [[1, 2, 3], [4, 5, 6]]
# 使用浅拷贝复制原始列表
shallow_copied_list = copy.copy(original_list)
# 使用深拷贝复制原始列表
deep_copied_list = copy.deepcopy(original_list)
# 修改原始列表中的一个元素
original_list[0][0] = 'changed'
# 打印原始列表和深拷贝后的列表
print("Original list:", original_list)
print("Shallow copied list:", shallow_copied_list)
print("Deep copied list:", deep_copied_list)
#Output
Original list: [['changed', 2, 3], [4, 5, 6]]
Shallow copied list: [['changed', 2, 3], [4, 5, 6]]
Deep copied list: [[1, 2, 3], [4, 5, 6]]
```

16.在 Python 中，`<<` 是按位左移运算符（Bitwise Left Shift Operator）。它用于将一个数的二进制表示向左移动指定的位数，并在右侧填充0。这个操作等价于将该数乘以2的幂。按位左移运算符的工作原理：假设我们有一个整数 `x` 和一个非负整数 `n`，那么 `x << n` 的含义是将 `x` 的二进制表示向左移动 `n` 位。每次左移一位，相当于将 `x` 乘以2；左移 `n` 位，相当于将 `x` 乘以 `2^n`。

应用：1.快速乘法：按位左移可以用来快速实现乘以2的幂的操作。例如，x << n 等价于 x * (2 ** n)，但通常更快，因为它是直接操作二进制位。2.位掩码操作：在处理位掩码时，按位左移常用于生成特定的位模式。例如，如果你想设置某个整数的第 n 位为1，可以使用 1 << n。3.优化算法：在某些算法中，特别是涉及二进制操作或位运算的场景下，按位左移可以提高性能。例如，在动态规划问题中，二进制分解法就使用了按位左移来减少状态更新次数。

17.前缀和与后缀和

```python
#前缀和常用于快速计算子数组的和。通过预先计算前缀和数组，可以在常数时间内计算任意子数组的和。具体来说，子数组 arr[i:j+1] 的和可以通过以下公式快速计算：
#sum(arr[i:j+1]) = prefix_sum[j] - prefix_sum[i-1] （当 i > 0 时）
#sum(arr[0:j+1]) = prefix_sum[j] （当 i = 0 时）
#注意start，end，step是左开右闭
def prefix_sum(arr):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    return prefix
# 示例
arr = [1, 2, 3, 4, 5]
prefix = prefix_sum(arr)
print(prefix)  # 输出: [1, 3, 6, 10, 15]
# 计算子数组 [2, 3, 4] 的和
subarray_sum = prefix[4] - prefix[1]
print(subarray_sum)  # 输出: 12 (2 + 3 + 4 = 9)

#后缀和
def suffix_sum_optimized(arr):
    n = len(arr)
    suffix_sum = [0] * n
    suffix_sum[-1] = arr[-1]  # 最后一个元素的后缀和就是它自己
    for i in range(n - 2, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + arr[i]
    return suffix_sum
# 示例
arr = [1, 2, 3, 4, 5]
print(suffix_sum_optimized(arr))  # 输出: [15, 14, 12, 9, 5]
```

18.`permutation`

```python
#全排列
def permute(arr, start, end):
    if start == end:
        print(arr)
    else:
        for i in range(start, end + 1):
            # 交换当前元素与起始元素
            arr[start], arr[i] = arr[i], arr[start]
            # 递归生成剩余元素的排列
            permute(arr, start + 1, end)
            # 回溯，恢复原始顺序
            arr[start], arr[i] = arr[i], arr[start]
# 生成集合 [1, 2, 3] 的全排列
arr = [1, 2, 3] permute(arr, 0, len(arr) - 1)

#部分排列
import itertools
#生成集合 {1, 2, 3} 的部分排列，每次选取 2 个元素
arr = [1, 2, 3]
permutations = list(itertools.permutations(arr, 2))
print("部分排列 (每次选取 2 个元素):")
for p in permutations:
    print(p)
```

19.一些判断

```python
#判断数据类型：isupper() islower() isdigit()（判断数字）isalpha()（判断字母）isalnum()（判断是否为字母或数字）isspace()（判断是否为空格）
#判断素数：
def is_prime(n):# 判断一个数很便捷
    if n <= 1:  # 素数必须大于 1
        return False
    for i in range(2, int(n ** 0.5) + 1):  # 只需要判断到平方根
        if n % i == 0:  # 如果能被整除，说明不是素数
            return False
return True  # 如果没有能整除的数，则是素数
#若要找出一个区间内的所有素数，则用埃拉托斯特尼筛法：
def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 和 1 不是素数
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]
print(sieve_of_eratosthenes(100)) # 获取 100 以内的所有素数
#判断完全平方数：
import math #返回的是布尔值
def is_perfect_square(n):
    if n < 0:
        return False  # 负数不是完全平方数
    sqrt_n = int(math.sqrt(n))  # 计算平方根并取整
return sqrt_n * sqrt_n == n  # 如果平方根的平方等于原数，则是完全平方数

```

20.`collection`中的`counter`可以统计字符串的出现频次，输出将会是字典，其中键是字符，值是该字符在字符串中出现的次数`Counter`还提供了一个`.most_common()` 方法，可以用来获取最常见的 `N` 个元素和它们的频次

21.进制转换：int（要转换的字符串型，该字符串的原本进制）（可转化为十进制数，转化后为整型）`bin(number)[2:]`（去掉 '0b' 前缀）（二）/`oct(number)[2:]`（去掉 '0o' 前缀）（八）/`hex(number)[2:]`（去掉 '0x' 前缀）（十六）ASCII表转换：使用 `ord() `将字符转换为 ASCII 码值 使用` chr()` 将 ASCII 码值转换为字符

22.得到一个数所有的质因数：

```python
#返回的是一个列表，如：输入60，返回[2,2,3,5]
def prime_factors(n):
    factors = []
    while n % 2 == 0: # 处理2这个特殊情况
        factors.append(2)
        n //= 2
    divisor = 3 # 处理奇数质因数，从3开始
    while divisor * divisor <= n:  # 只需要检查到 sqrt(n)
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 2  # 只检查奇数
    # 如果剩下的是一个大于2的质数
    if n > 2:
        factors.append(n)
    return factors
```



## 2.算法部分

### 2.1 二分查找(Binary Search)和线性查找(Linear Search)

线性查找适用于较小或无序的数据集，而二分查找适用于较大的有序数据集。二分查找容易理解，但是细节部分不容易写对（while的条件是<=，还是<；折半后是mid+1，mid-1，还是mid）BS时间复杂度为O(log n) LS时间复杂度为O(n)

Attention:所有的索引都是从0开始，len(arr)-1用作索引的指针时正好表示最后一个

#### 2.1.1 二分查找

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
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

1. 初始化：
   - 设置左边界 `left` 为 0，右边界 `right` 为数据集的最后一个索引。
2. 查找过程：
   - 计算中间位置 `mid`。
   - 如果中间位置的元素等于目标元素，返回其索引。
   - 如果中间位置的元素小于目标元素，调整左边界 `left` 为 `mid + 1`。
   - 如果中间位置的元素大于目标元素，调整右边界 `right` 为 `mid - 1`。
   - 重复上述步骤，直到找到目标元素或左边界超过右边界。
3. 未找到目标元素：
   - 如果左边界超过右边界，返回 -1。

#### 2.1.2 线性查找

```python
def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i  # 返回目标元素的索引
    return -1  # 如果未找到目标元素，返回 -1

# 示例
arr = [3, 5, 2, 8, 1, 9, 4]
target = 8
result = linear_search(arr, target)
print(f"Target {target} found at index {result}")
# Target 8 found at index 3
```

#### 2.1.3 最长不下降子序列

最长不下降序列（Longest Non-Decreasing Subsequence, LNDS）是动态规划中一个经典的算法问题。它要求在一个给定的序列中找到一个最长的子序列，使得这个子序列中的元素按照非严格递增的顺序排列。换句话说，子序列中的每个元素都大于或等于前一个元素。

**动态规划解法**

我们可以使用动态规划来解决这个问题。设 `dp[i]` 表示以 `a[i]` 结尾的最长不下降子序列的长度。那么，状态转移方程可以表示为：

```python
dp[i] = max(dp[j] + 1) for all j < i and a[j] ≤ a[i]
```

初始时，`dp[i] = 1`，因为每个元素本身都可以构成一个长度为1的不下降子序列。

最终的结果是 `dp` 数组中的最大值，即 `max(dp)`。

```python
def longest_non_decreasing_subsequence(arr):
    if not arr:
        return 0

    n = len(arr)
    dp = [1] * n  # 初始化 dp 数组，每个元素至少可以构成长度为1的子序列

    # 动态规划求解
    for i in range(1, n):
        for j in range(i):
            if arr[j] <= arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    # 返回 dp 数组中的最大值
    return max(dp)

# 示例
arr = [10, 9, 2, 5, 3, 7, 101, 18]
print("最长不下降子序列的长度是:", longest_non_decreasing_subsequence(arr))
```

在这个例子中，最长的不下降子序列是 `[2, 3, 7, 18]` 或 `[2, 5, 7, 101]`，它们的长度都是4。

对于更长的序列，`O(n^2)` 的时间复杂度可能会显得不够高效。我们可以通过二分查找和贪心算法将时间复杂度优化到 `O(n log n)`。

我们可以维护一个数组 `tails`，其中 `tails[i]` 表示长度为 `i+1` 的不下降子序列的最小末尾元素。通过二分查找，我们可以快速找到 `tails` 中第一个大于或等于当前元素的位置，并更新 `tails`。

```python
from bisect import bisect_left

def longest_non_decreasing_subsequence_optimized(arr):
    if not arr:
        return 0

    tails = []  # 用于存储不同长度的不下降子序列的最小末尾元素

    for num in arr:
        # 使用二分查找找到 tails 中第一个大于或等于 num 的位置
        idx = bisect_left(tails, num)
        
        # 如果 num 比 tails 中所有元素都大，则将其添加到 tails 的末尾
        if idx == len(tails):
            tails.append(num)
        else:
            # 否则，用 num 替换 tails[idx]，以保持 tails 的单调性
            tails[idx] = num

    # tails 的长度即为最长不下降子序列的长度
    return len(tails)

# 示例
arr = [10, 9, 2, 5, 3, 7, 101, 18]
print("最长不下降子序列的长度是:", longest_non_decreasing_subsequence_optimized(arr))
```

总结

- **`O(n^2)` 动态规划解法**：适用于较小规模的问题，易于理解和实现。
- **`O(n log n)` 优化解法**：适用于较大规模的问题，利用二分查找和贪心思想提高了效率。

### 2.2 穷举(Brute Force)

#### 2.2.1 Brute Force法解决八皇后问题

```python
from itertools import permutations
def solve_n_queens(n):
    solutions = []
    cols = range(n)
    # 生成每一行皇后位置的排列
    for perm in permutations(cols):
        # 检查是否有两个皇后在同一对角线上
        if n == len(set(perm[i] + i for i in cols)) == len(set(perm[i] - i for i in cols)):
            # 如果满足条件，加入解
            solutions.append(perm)
    return solutions
solutions = solve_n_queens(8)
for _ in range(int(input())):
    n = int(input())
    queen_string = ''.join(str(col + 1) for col in solutions[n - 1])
    print(queen_string)
```

首先`permutations`函数已经生成了八皇后中满足所有的皇后都在不同的行和列上的排列(也就是全排列)，检查主副对角线的方法是观察到主副对角线的规律(主对角线上的位置具有相同的 `i - j` 值;副对角线上的位置具有相同的 `i + j` 值)

#### 2.2.2 递归(Recursion)

2.2.3.1 0-1背包问题

1.确定dp数组以及下标的含义

对于背包问题，有一种写法，是使用二维数组，即`dp[i][j]`表示从下标为0~i的物品里任意取，放进容量为j的背包，价值总和最大是多少。

2.确定递推公式

再回顾一下`dp[i][j]`的含义：从下标为[0-i]的物品里任意取，放进容量为j的背包，价值总和最大是多少。

那么可以有两个方向推出来`dp[i][j]`，

- 由`dp[i - 1][j]`推出，即背包容量为j，里面不放物品i的最大价值，此时`dp[i][j]`就是`dp[i - 1][j]`
- 由`dp[i - 1][j - weight[i]]`推出，`dp[i - 1][j - weight[i]]` 为背包容量为`[j - weight[i]]`的时候不放物品i的最大价值，那么`dp[i - 1][j - weight[i]] + value[i] `（物品i的价值），就是背包放物品i得到的最大价值

所以递归公式`dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])`

3.初始化

`dp[i][j]`在推导的时候一定是取价值最大的数，如果题目给的价值都是正整数那么非0下标都初始化为0就可以了，因为0就是最小的了，不会影响取最大价值的结果。如果题目给的价值有负数，那么非0下标就要初始化为负无穷了。例如：一个物品的价值是-2，但对应的位置依然初始化为0，那么取最大值的时候，就会取0而不是-2了，所以要初始化为负无穷。

### 2.3 深度优先搜索(Depth-First Search)

#### 2.3.1 模版

##### 2.3.1.1 输入

要求是给定n*m的矩阵，随后的n行输入矩阵中的内容，并加上-1的外层保护圈

```python
#使用sys.stdin一键调取所有数据后，将标准输入中的所有内容一次性读取为字符串。用 splitlines() 将输入字符串按行分割为列表，适合多行输入场景。
import sys
if __name__ == "__main__":
    input = sys.stdin.read
    data = input().splitlines()
    # 读取迷宫大小
    n, m = map(int, data[0].split())
    # 初始化迷宫，添加保护圈
    maze = [[-1 for _ in range(m + 2)]]
    for i in range(1, n + 1):
        maze.append([-1] + list(map(int, data[i].split())) + [-1])
    maze.append([-1 for _ in range(m + 2)])
    
#正常输入
n, m = map(int, input().split())
maze = []
maze.append( [-1 for x in range(m+2)] ) #最上面的一行-1
for _ in range(n):
    maze.append([-1] + [int(_) for _ in input().split()] + [-1])
maze.append( [-1 for x in range(m+2)] ) #最下面的一行-1
```

##### 2.3.1.2 具体题目

例题 1：岛屿数量（LeetCode 200）

**题目描述**：给定一个由 `'1'`（陆地）和 `'0'`（水）组成的二维网格，计算岛屿的数量。岛屿总是被水包围，并且每个岛屿只能由水平方向或垂直方向上相邻的陆地连接形成。

**解答**：我们可以使用 DFS 或 BFS 来解决这个问题。每次遇到一个未访问的陆地时，启动一次搜索，标记所有相连的陆地为已访问，直到无法继续扩展为止。（DFS）

```python
def numIslands(grid):
    if not grid:
        return 0

    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':#边界条件
            return
        grid[i][j] = '0'  # 标记为已访问
        dfs(i + 1, j)#继续在这一点上dfs
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count
# 示例
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(numIslands(grid))  # 输出: 3
```

（BFS）

```python
from collections import deque
def numIslands(grid):
    if not grid:
        return 0
    def bfs(i, j):
        queue = deque([(i, j)])
        while queue:
            x, y = queue.popleft()
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
                grid[x][y] = '0'  # 标记为已访问
                queue.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                bfs(i, j)
                count += 1
    return count
# 示例
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(numIslands(grid))  # 输出: 3
```



## 3.积累

#### 3.1 矩阵简单的遍历加法

方法一 遍历 时间复杂度$o(n^2)$ 

```python
def calculate_maxlayers(n, matrix):
    total_sums = []
    layer = 0

    while layer < n // 2:
        single_layer = []
        # 上边
        for i in range(layer, n - layer):
            single_layer.append(matrix[layer][i])
        # 右边
        for i in range(layer + 1, n - layer):
            single_layer.append(matrix[i][n - layer - 1])
        # 下边
        for i in range(n - layer - 2, layer - 1, -1):
            single_layer.append(matrix[n - layer - 1][i])
        # 左边
        for i in range(n - layer - 2, layer, -1):
            single_layer.append(matrix[i][layer])
        total_sums.append(sum(single_layer))
        layer += 1

    # 如果n为奇数，处理中心元素
    if n % 2 == 1:
        center = n // 2
        total_sums.append(matrix[center][center])

    return max(total_sums)

n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print(calculate_maxlayers(n, matrix))
```

核心思想：layer是指一个外层洋葱圈，在这一个layer里面，不管在上下左右哪一边，真正变化的是变量i。同时从一些简单的矩阵入手，发现奇数有中心点，偶数没有，但不管怎样层数都是：n//2+1(若为奇数则+1)，所以存在while layer<n//2这样的语句。然后注意不同边的方向（正向1 反向-1）然后是range的左闭右开性质。

```python
from collections import deque

n = int(input())
sl = deque()
for _ in range(n):
    sl.append(deque(map(int, input().split())))

nl = []

while True:
    if n == 0:
        break
    elif n == 1:
        nl.append(sl[0][0])  # 只剩一个元素时，直接添加并结束
        break

    # 计算当前矩阵外圈的元素和
    z = sum(sl[0]) + sum(sl[-1])  # 顶部和底部行
    for i in range(1, n - 1):
        z += sl[i][0] + sl[i][-1]  # 左右两列

    # 添加当前外圈的总和
    nl.append(z)

    # 去除当前外圈
    sl.popleft()  # 删除顶部行
    sl.pop()      # 删除底部行
    for i in range(len(sl)):
        sl[i].popleft()  # 删除每行的左侧元素
        sl[i].pop()      # 删除每行的右侧元素

    # 矩阵维度减小
    n -= 2

# 输出结果
print(max(nl))
```

#### 3.2 滑雪

Michael想知道载一个区域中最长的滑坡。区域由一个二维数组给出。数组的每个数字代表点的高度。下面是一个例子

```
 1  2  3  4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
```

一个人可以从某个点滑向上下左右相邻四个点之一，当且仅当高度减小。在上面的例子中，一条可滑行的滑坡为24-17-16-1。当然25-24-23-...-3-2-1更长。事实上，这是最长的一条。

输入 输入的第一行表示区域的行数R和列数C(1 <= R,C <= 100)。下面是R行，每行有C个整数，代表高度h，0<=h<=10000。

输出 输出最长区域的长度。

样例输入

```
5 5
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
```

样例输出

```
25
```

容易爆栈，记得调栈的深度

```python
sys.setrecursionlimit(1<<30)
```

functools.lru_cache（dfs超时的时候可用）是一个装饰器,用来缓存函数的返回结果，以优化递归和重复计算的性能

```python
import functools(首先引入)@functools.lru_cache(maxsize=128) # 缓存最多 128 个结果
```

我的clumsy的算法

存储一个`meow`数组用来记忆最长路径

```python
import sys
def ski(i,j):
    if meow[i][j]!= -1:
        return meow[i][j]
    max_length = 1
    for dx,dy in dire:
        nx = i+dx
        ny = j+dy
        if 0<=nx<R and 0<=ny<C and heights[nx][ny] < heights[i][j]:
            length = 1+ ski(nx,ny)
            max_length = max(max_length,length)
    meow[i][j] = max_length
    return max_length

data = sys.stdin.read().splitlines()
R,C = map(int,data[0].split())
heights = []
for i in range(1,R+1):
    heights.append(list(map(int,data[i].split())))
meow = [[-1]*C for _ in range(R)]
dire = [(0,1),(0,-1),(1,0),(-1,0)]
longest = max(max(ski(i,j) for j in range(C)) for i in range(R))
print(longest)
```

用heap

```python
import heapq
rows, cols = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(rows)]
# 使用最小堆存储元素及其坐标
heap = [(matrix[i][j], i, j) for i in range(rows) for j in range(cols)]
heapq.heapify(heap)
# 每个点的L值初始化为1
dp = [[1] * cols for _ in range(rows)]
# 定义方向数组，用于遍历上下左右
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# 记录最长递增路径长度
longest_path = 1
# 遍历堆中的元素，按高度从小到大处理
while heap:
    height, x, y = heapq.heappop(heap)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] < height:#边界检查和主要的递增条件判断
            dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)
    longest_path = max(longest_path, dp[x][y])
print(longest_path)
```

#### 3.3 给植物浇水(bisect)

Alice 和 Bob 打算给花园里的 n 株植物浇水。植物排成一行，从左到右进行标记，编号从 0 到 n - 1，每一株植物都需要浇特定量的水。Alice 和 Bob 每人有一个水罐，容量分别为 a 和 b，最初是满的。他们按下面描述的方式完成浇水：

- 每株植物都可以由 Alice 或者 Bob 来浇水。Alice 按从左到右的顺序从植物 0 开始浇水；Bob 按从右到左的顺序从植物 n - 1 开始浇水。二人同时开始。
- 不管植物需要多少水，浇水所耗费的时间都是一样的。
- 如果没有足够的水完全浇灌下一株植物，他 / 她会立即重新灌满浇水罐，再给下一株植物浇水。不能提前重新灌满水罐。保证 a 和 b 均大于任意一株植物需要浇水的量。
- 如果 Alice 和 Bob 到达同一株植物，那么当前水罐中水更多的人会给这株植物浇水。如果他俩水量相同，那么 Alice 会给这株植物浇水。

请你写一个程序，计算两人浇灌所有植物过程中重新灌满水罐的总次数。

输入 第一行为三个正整数 n, a, b，分别表示植物个数，Alice 和 Bob 的水罐容量。n <= 100第二行为 n 个空格分隔的正整数，表示每株植物需要的浇水量。

输出 一个正整数，表示 Alice 和 Bob完成浇水所需要重新灌满水罐的总次数。

样例输入

```
Sample1 Input:
4 3 4
2 2 3 3

Sample1 Output:
2

解释：Alice 和 Bob 分别给第 0 和 n-1 株植物浇水后剩余水量均为 1，
不足以给第 1 和 n-2 株植物浇水，于是各重新灌满一次。
```

```python
n,a,b = map(int,input().split())
plants = list(map(int,input().split()))
left,right = 0,n-1
count = 0
renewa，renewb = a,b
while left< right :
    if plants[left] > a:#只处理特殊情况 也就是水桶正常的水不够浇花的时候
        count += 1
        a = renewa
    a -= plants[left]#注意缩进 这里是正常的while循环过程
    left += 1
    if plants[right] > b:#两端不一定需要同步
        count += 1
        b = renewb
    b -= plants[right]
    right -= 1

if left == right:
    if max(a,b)<plants[left]:
        count += 1
print(count)
```

#### 3.4 字符串连接位置

描述 给定两个字符串A和B，如果A的某一后缀恰好和B的某一前缀相同，则定义字符串A可以连接到B。

例如，字符串 xxxxxabc 可以连接到字符串 abc******** ，因为xxxxxabc   abc********

输入 输入为两行，分别为字符串A和B。输入保证A和B是可连接的。

输出 字符串连接的位置，从0开始计数。如果存在多个可连接位置，则输出值最大的位置。

样例输入

```
Sample Input1:
xxxxxabc
abc********

Sample Output1:
5
```

需要思考一些特殊情况(thanks to HBW)

`**aaaa`和`aab********`索引应该是4而不是5

```python
#my version（AC but not perfect）
a = list(input())
b = list(input())
for i in range(1,len(b)+1):
    if a[len(a)-i:]==b[:i:]:
        print(len(a)-i)
        break
#HBW补充
result = []
result.append(len(A)-i)
print(max(result)) #例如****aa和aab*****
```

