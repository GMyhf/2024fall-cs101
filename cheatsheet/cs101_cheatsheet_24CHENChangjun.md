开头模板

```python
    # pylint: skip-file
    import sys
    sys.setrecursionlimit(1<<30)
    from functools import lru_cache
    @lru_cache(maxsize=None)
    def dfs():

```

#### 无穷大:`float('inf')`

#### 循环正常结束后执行的语句:`while...else...`

#### lru_cache(用来存储每次递归的结果,遇到相同自变量的递归时直接返回这个结果,因此它不能在此时再进行更新其中的全局变量的操作):

```py
from functools import lru_cache
@lru_cache(maxsize = 128)
```

### 四舍五入和位数保留

```python
result = round(3.14159, 2)  # 结果为 3.14（遵循四舍六入五凑偶）
number = 3.14159
print(f'{number:.2f}')  # 输出结果为 "3.14"
```

### 进制转化

```py
#二进制
decimal_number = 10
binary_string = bin(decimal_number)  # 结果为 '0b1010'
print(binary_string)
#八进制
decimal_number = 10
octal_string = oct(decimal_number)  # 结果为 '0o12'
print(octal_string)
#十六进制
decimal_number = 10
hexadecimal_string = hex(decimal_number)  # 结果为 '0xa'
print(hexadecimal_string)
#转化为十进制
binary_string = '1010'
decimal_number = int(binary_string, 2)  # 结果为 10，基底可以为2（即进制数）
print(decimal_number)
#请注意，所有的转换都要求输入是一个有效的表示形式，并且基数必须在2到36之间（因为这是所有可用数字和字母能表示的最大进制）。如果输入非法或者基数超出范围，将会抛出异常。
```

### 判断全真和全假

`all()`函数用于检查可迭代对象的所有元素是否都为真，如果都为真则返回`True`，否则返回`False`。

`any()`函数用于检查可迭代对象中是否有任何一个元素为真，如果至少有一个元素为真，则返回`True`，否则返回`False`。

下面是如何使用这两个函数来判断一个列表中的元素是否全为真或全为假：

```python
def check_all_elements(iterable):
    # 判断是否全为真
    all_true = all(iterable)
    # 判断是否全为假
    all_false = not any(iterable)
    
    if all_true:
        return "All elements are true."
    elif all_false:
        return "All elements are false."
    else:
        return "Elements are mixed."

# 示例
elements = [True, True, True]
print(check_all_elements(elements))  # 输出: All elements are true.

elements = [False, False, False]
print(check_all_elements(elements))  # 输出: All elements are false.

elements = [True, False, True]
print(check_all_elements(elements))  # 输出: Elements are mixed.
```

这个函数首先检查所有元素是否都为真，如果不是，则检查是否有任何元素为真。根据这两个条件的结果，它返回相应的信息。注意这里的“假”是指Python中视为`False`的任何东西，包括但不限于`0`, `None`, `False`, 空序列（如`[]`, `{}`, `''`等）。

### 对数运算

看起来您可能想要使用Python来计算自然对数。在Python中，您可以使用`math`模块里的`log()`函数来计算一个数的自然对数。下面是一个简单的例子：

```python
import math

# 计算 e 的自然对数，其中 e 是自然对数的底数，大约等于 2.71828
ln_e = math.log(math.e)
print(ln_e)  # 输出应该是 1.0，因为 log(e, e) = 1

# 计算 10 的自然对数
ln_10 = math.log(10)
print(ln_10)  # 输出结果将接近 2.302585092994046
```

如果您想计算以其他底数的对数，可以这样写：

```python
# 计算 16 以 2 为底的对数
log2_16 = math.log(16, 2)
print(log2_16)  # 输出应该是 4.0，因为 2^4 = 16

# 或者使用 log() 的变种 log2() 来计算以 2 为底的对数
log2_16b = math.log2(16)
print(log2_16b)  # 同样输出 4.0
```

### 质数筛选：

欧拉筛法（Euler Sieve）是一种改进的筛法，相比传统的埃拉托斯特尼筛法，它减少了不必要的操作，从而提高了效率。欧拉筛法的核心思想是利用已知的质数来标记合数，并且每个合数只被标记一次。

以下是使用欧拉筛法在Python中筛选质数的基本步骤：

1. 初始化一个布尔数组 `is_prime[]`，表示每个位置上的数是否为质数。
2. 遍历数组，对于每一个当前位置 `i`，如果 `is_prime[i]` 为 `True`，则认为 `i` 是一个质数。
3. 对于每个质数 `i`，遍历 `i` 的倍数，并标记这些倍数为合数。为了避免重复标记，从 `i * i` 开始标记。
4. 记录每个质数及其倍数的最小质因数（最小的能够整除该数的质数）。

下面是使用欧拉筛法实现的Python代码：

```python
def euler_sieve(limit):
    if limit < 2:
        return []
    
    # 初始化数组
    is_prime = [True] * (limit + 1)
    min_prime_factor = [0] * (limit + 1)
    
    # 0 和 1 不是质数
    is_prime[0] = is_prime[1] = False
    
    # 遍历数组，找出质数并标记它们的倍数
    for i in range(2, limit + 1):
        if is_prime[i]:  # 如果 i 是质数
            min_prime_factor[i] = i
            # 标记 i 的倍数
            for j in range(i * i, limit + 1, i):
                if is_prime[j]:
                    is_prime[j] = False
                    min_prime_factor[j] = i
    
    # 收集所有质数
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

# 示例：找出小于等于100的所有质数
primes = euler_sieve(100)
print(primes)
```

在这个实现中，我们不仅标记了合数，还记录了每个合数的最小质因数。这在某些情况下可能会有用，比如在分解质因数时。

需要注意的是，虽然欧拉筛法在理论上减少了不必要的操作，但在实际应用中，其效率提升相对于标准的埃拉托斯特尼筛法并不是特别显著。然而，在处理较大范围的数据时，这种减少冗余的操作可以带来一定的性能改善。

### 双关键词排序

如果你想根据多个键来排序列表，可以在 `key` 参数中提供一个函数，该函数返回一个包含所有排序依据的元组。Python 的排序算法是稳定的，因此它会在第一个排序键相同的情况下保持原有的顺序，或者根据第二个排序键继续排序。

假设你有一个列表，其中每个元素都是一个字典，包含了姓名和年龄，你想首先按年龄排序，然后在年龄相同时再按姓名排序：

```python
people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'David', 'age': 30},
    {'name': 'Carol', 'age': 25}
]

# 按年龄排序，在年龄相同时按姓名排序
sorted_people = sorted(people, key=lambda person: (person['age'], person['name']))
print(sorted_people)

# 输出:
# [
#     {'name': 'Bob', 'age': 25},
#     {'name': 'Carol', 'age': 25},
#     {'name': 'Alice', 'age': 30},
#     {'name': 'David', 'age': 30}
# ]
```

在这个例子中，`lambda person: (person['age'], person['name'])` 返回一个元组 `(age, name)`，用于排序。这会让列表首先按照 `age` 进行排序，当 `age` 相同时，则按照 `name` 排序。

### 二分查找

```py
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# 示例
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
result = binary_search(arr, target)
if result != -1:
    print("元素在数组中的索引为 %d" % result)
else:
    print("数组中没有此元素")
```

### 深拷贝

```py
import copy
original_list = [[1, 2], [3, 4]]
copied_list = copy.deepcopy(original_list)
```

### 双端队列

下面是一个简单的使用例子：

```python
from collections import deque

# 创建一个空的双端队列
d = deque()

# 在右端添加元素
d.append(1)
d.append(2)

# 在左端添加元素
d.appendleft(0)

print(d)  # 输出: deque([0, 1, 2])

# 移除右端元素
print(d.pop())  # 输出: 2

# 移除左端元素
print(d.popleft())  # 输出: 0

print(d)  # 输出: deque([1])
```

`deque`对象提供了多种方法来处理队列中的数据，包括但不限于`append()`、`appendleft()`、`pop()`、`popleft()`等。这些方法使得双端队列非常灵活，可以在需要快速插入和删除元素的应用场景中使用，如构建滑动窗口算法等。

需要注意的是，`deque`内部使用列表实现，但是它优化了两端的操作，使得`append()`、`appendleft()`、`pop()`以及`popleft()`的时间复杂度为O(1)，即它们都是常数时间操作。这使得`deque`比普通的列表更适用于需要频繁进行插入和删除操作的情况。

`heapq` 是 Python 的一个内置模块，它实现了最小堆（Min-Heap）的数据结构。最小堆是一种特殊的二叉树，其中父节点的值总是小于或等于其子节点的值。这使得我们可以高效地访问最小元素，这对于优先队列和某些算法（如Dijkstra最短路径算法）非常有用。

### 堆

以下是 `heapq` 模块的一些常用函数及其用法：

#### 创建堆
- **heapify(iterable)**: 将列表转换为堆，原地操作，时间复杂度为 O(n)。
```python
import heapq
lst = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapq.heapify(lst)
print(lst)  # 输出可能为 [0, 1, 2, 6, 3, 5, 4, 7, 8, 9] 或其他有效堆排列
```

#### 插入元素

- **heappush(heap, item)**: 向堆中插入元素，并保持堆的性质。
```python
heapq.heappush(lst, -1)
print(lst)  # 输出将包含新插入的元素 -1，并且是有效的最小堆
```

#### 弹出最小元素
- **heappop(heap)**: 弹出并返回堆中的最小元素，即根元素。
```python
min_element = heapq.heappop(lst)
print(min_element)  # 输出将是之前堆中的最小元素
```

#### 弹出最小元素并插入新元素
- **heapreplace(heap, item)**: 弹出最小元素后，将新元素插入堆中。等价于 `heappop()` 后 `heappush(item)`，但效率更高。
```python
new_min = heapq.heapreplace(lst, 10)
print(new_min)  # 输出将是弹出的最小元素
print(lst)      # 列表现在包含新插入的元素 10
```

#### 获取最小元素而不弹出
-  **nlargest(n, iterable, key=None)** 和 **nsmallest(n, iterable, key=None)**: 分别返回最大的 n 个数和最小的 n 个数组成的列表。key 参数可以指定一个函数来提取比较关键字。
```python
largest_three = heapq.nlargest(3, lst)
smallest_three = heapq.nsmallest(3, lst)
print(largest_three)  # 输出列表中最大的三个元素
print(smallest_three) # 输出列表中最小的三个元素
```

### 迭代神器：`enumerate()` 

#### 语法：

```python
enumerate(iterable, start=0)
```

- `iterable`：要枚举的可迭代对象。
- `start`：索引的起始值，默认为 0。

#### 示例：

```python
# 使用 enumerate() 遍历列表并打印索引和对应的值
fruits = ['apple', 'banana', 'orange']
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
```

#### 输出：

```
Index 0: apple
Index 1: banana
Index 2: orange
```

#### 指定起始索引：

```python
# 使用不同的起始索引
for index, fruit in enumerate(fruits, start=1):
    print(f"Item {index}: {fruit}")
```

#### 输出：

```
Item 1: apple
Item 2: banana
Item 3: orange
```

### 二分查找

以下是 `bisect` 模块的主要函数：

- `bisect.bisect_left(a, x, lo=0, hi=len(a))`: 查找在排序列表 `a` 中插入元素 `x` 的位置。如果 `x` 已经存在，则返回第一个 `x` 出现的位置。可以指定查找范围 `lo` 和 `hi`。
- `bisect.bisect_right(a, x, lo=0, hi=len(a))` 或者 `bisect.bisect(a, x, lo=0, hi=len(a))`: 这两个函数功能相同，都是查找在排序列表 `a` 中插入元素 `x` 的位置。如果 `x` 已经存在，则返回最后一个 `x` 之后的位置。
- `bisect.insort_left(a, x, lo=0, hi=len(a))`: 将元素 `x` 插入到排序列表 `a` 中，并保持 `a` 的排序。如果 `x` 已经存在，则插入在所有已存在元素之前。
- `bisect.insort_right(a, x, lo=0, hi=len(a))` 或者 `bisect.insort(a, x, lo=0, hi=len(a))`: 这两个函数功能相同，都是将元素 `x` 插入到排序列表 `a` 中，并保持 `a` 的排序。如果 `x` 已经存在，则插入在所有已存在元素之后。

下面是一些使用 `bisect` 模块的例子：

```python
import bisect

# 已排序的列表
sorted_list = [1, 3, 4, 7, 8]

# 查找插入位置
position = bisect.bisect_left(sorted_list, 5)
print(position)  # 输出: 3

# 插入元素并保持排序
bisect.insort(sorted_list, 5)
print(sorted_list)  # 输出: [1, 3, 4, 5, 7, 8]
```

<mark>需要注意目标列表已经被排好序</mark>

```py
def times(a,b):
  a,b=list(str(a)),list(str(b))
  a.reverse()
  b.reverse()
  ans=[0 for i in range(10002)]
  for j in range(len(b)):
      for i in range(len(a)):
          ans[j+i]+=int(b[j])*int(a[i])%10
          ans[j+i+1]+=ans[j+i]//10
          ans[j+i]%=10
          ans[j+i+1]+=int(b[j])*int(a[i])//10
  i=0
  while i==0 and ans:
      i=ans.pop()
  ans.append(i)
  res=''
  for i in ans[-1::-1]:
      res+=str(i)
  return int(res)
```

### 生成全排列

```py
import itertools

elements = [1, 2, 3]
permutations = list(itertools.permutations(elements))
print(permutations)
```

