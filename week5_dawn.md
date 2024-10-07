# 20241008-Week5-黎明

Updated 2127 GMT+8 Oct 7, 2024

2024 fall, Complied by Hongfei Yan



已经进入第五周了，这标志着一个学期的时间已经过去了三分之一，真是光阴似箭。



# 模拟implementation 

模拟题是一类“题目怎么说，你就怎么做”的题目。这类题目通常不涉及复杂的算法，而是要求根据题目的描述进行代码的编写。考查的是代码的逻辑性和正确性，确保每一步都符合题目的要求。

下面是对这类题目的一些详细解释和示例。



## 02746: 约瑟夫问题

implementation, http://cs101.openjudge.cn/practice/02746

约瑟夫问题：有ｎ只猴子，按顺时针方向围成一圈选大王（编号从１到ｎ），从第１号开始报数，一直数到ｍ，数到ｍ的猴子退出圈外，剩下的猴子再接着从1开始报数。就这样，直到圈内只剩下一只猴子时，这个猴子就是猴王，编程求输入ｎ，ｍ后，输出最后猴王的编号。



> 模拟的方法直接按照题目描述的步骤进行操作，逐步移除报数到 \( m \) 的猴子，直到只剩下一个猴子为止。
>
> ### 模拟解法
> 1. **初始化**：
>    - 创建一个包含所有猴子编号的列表。
>    - 设置起始位置为 0（即第 1 号猴子）。
>
> 2. **模拟过程**：
>    - 每次从当前起始位置开始报数，数到 \( m \) 的猴子出圈。
>    - `pop` 操作会自动调整列表的索引，因此不需要显式地重置 `pos`。
>
> 3. **输出结果**：
>    - 输出最后剩下的猴子的编号。
>
> ### 代码实现
> 以下是使用模拟方法解决约瑟夫问题的代码实现：
>
> ```python
> def josephus(n, m):
>     if n == 0:
>         return 0
>     
>     monkeys = list(range(1, n + 1))  # 猴子的编号列表
>     pos = 0  # 当前起始位置
>     
>     while len(monkeys) > 1:
>         # 计算当前出圈的猴子的位置
>         pos = (pos + m - 1) % len(monkeys)
>         # 移除出圈的猴子
>         monkeys.pop(pos)
>     
>     return monkeys[0]  # 返回最后剩下的猴子的编号
> 
> while True:
>     n, m = map(int, input().split())
>     if n + m == 0:
>         break
>     result = josephus(n, m)
>     print(result)
> ```
>
> ### 代码解释
> 1. **初始化**：
>    - `monkeys = list(range(1, n + 1))`：创建一个包含所有猴子编号的列表。
>    - `pos = 0`：设置起始位置为 0（即第 1 号猴子）。
> 2. **模拟过程**：
>    - `pos = (pos + m - 1) % len(monkeys)`：计算当前出圈的猴子的位置。这里减1是因为我们从1开始报数，而列表索引是从0开始的。
> 3. **输出结果**：
>    - `print(result)`：输出最后剩下的猴子的编号。
>
> 



## 03253:约瑟夫问题No.2

http://cs101.openjudge.cn/practice/03253/

n 个小孩围坐成一圈，并按顺时针编号为1,2,…,n，从编号为 p 的小孩顺时针依次报数，由1报到m ，当报到 m 时，该小孩从圈中出去，然后下一个再从1报数，当报到 m 时再出去。如此反复，直至所有的小孩都从圈中出去。请按出去的先后顺序输出小孩的编号。



> 直接模拟这个过程，使用一个列表来表示小孩的编号，每次报数时移除对应的小孩。
>
> ```python
> def josephus(n, p, m):
>     if n == 0:
>         return []
>     
>     kids = list(range(1, n + 1))  # 孩子们的编号列表
>     pos = p - 1  # 将起始位置调整为0-based索引
>     out_order = []  # 记录出圈的顺序
>     
>     while kids:
>         pos = (pos + m - 1) % len(kids)  # 计算当前出圈的孩子的位置
>         out_order.append(kids.pop(pos))  # 将出圈的孩子添加到结果列表中
>     
>     return out_order
> 
> while True:
>     n, p, m = map(int, input().split())
>     if n + p + m == 0:
>         break
>     result = josephus(n, p, m)
>     print(','.join(map(str, result)))
> ```
>
> ### 代码解释
> 1. **初始化**：
>    - `kids = list(range(1, n + 1))`：创建一个包含所有孩子编号的列表。
>    - `pos = p - 1`：将起始位置调整为0-based索引。
>    - `out_order = []`：用于记录出圈的顺序。
>
> 2. **模拟过程**：
>    - `pos = (pos + m - 1) % len(kids)`：计算当前出圈的孩子的位置。这里减1是因为我们从1开始报数，而列表索引是从0开始的。
>    - `out_order.append(kids.pop(pos))`：将出圈的孩子添加到结果列表中，并从孩子列表中移除。
>
> 3. **输出结果**：
>    - `print(','.join(map(str, result)))`：将结果列表中的编号用逗号连接成字符串并输出。
>
> ### 其他模拟题的例子
> 1. **字符串操作**：如字符串反转、字符串替换等。
> 2. **数组操作**：如数组排序、数组旋转等。
>



# 查找元素

查找操作是编程中的基本技能，根据数据集的大小和结构选择合适的查找方法可以显著提高效率。线性查找适用于较小或无序的数据集，而二分查找适用于较大的有序数据集。



> ### 常见的查找方法
> 1. **线性查找（Linear Search）**：
>    - **适用范围**：适用于较小的数据集或无序的数据集。
>    - **原理**：逐个检查数据集中的每个元素，直到找到满足条件的元素或遍历完所有元素。
>    - **时间复杂度**：O(n)，其中 n 是数据集的大小。
>
> 2. **二分查找（Binary Search）**：
>    - **适用范围**：适用于有序的数据集。
>    - **原理**：通过将数据集分成两半，逐步缩小查找范围，直到找到满足条件的元素或确定不存在。
>    - **时间复杂度**：O(log n)，其中 n 是数据集的大小。
>
> ### 示例代码
>
> #### 线性查找
> ```python
> def linear_search(arr, target):
>     for i, element in enumerate(arr):
>         if element == target:
>             return i  # 返回目标元素的索引
>     return -1  # 如果未找到目标元素，返回 -1
> 
> # 示例
> arr = [3, 5, 2, 8, 1, 9, 4]
> target = 8
> result = linear_search(arr, target)
> print(f"Target {target} found at index {result}")
> # Target 8 found at index 3
> ```
>
> #### 二分查找
> ```python
> def binary_search(arr, target):
>     left, right = 0, len(arr) - 1
>     
>     while left <= right:
>         mid = (left + right) // 2
>         if arr[mid] == target:
>             return mid  # 返回目标元素的索引
>         elif arr[mid] < target:
>             left = mid + 1
>         else:
>             right = mid - 1
>     
>     return -1  # 如果未找到目标元素，返回 -1
> 
> # 示例
> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
> target = 8
> result = binary_search(arr, target)
> print(f"Target {target} found at index {result}")
> # Target 8 found at index 7
> ```
>
> ### 详细步骤
>
> #### 线性查找
> 1. **初始化**：
>    - 遍历数据集中的每个元素。
> 2. **查找过程**：
>    - 逐个检查每个元素是否等于目标元素。
>    - 如果找到目标元素，返回其索引。
>    - 如果遍历完所有元素仍未找到目标元素，返回 -1。
>
> #### 二分查找
> 1. **初始化**：
>    - 设置左边界 `left` 为 0，右边界 `right` 为数据集的最后一个索引。
> 2. **查找过程**：
>    - 计算中间位置 `mid`。
>    - 如果中间位置的元素等于目标元素，返回其索引。
>    - 如果中间位置的元素小于目标元素，调整左边界 `left` 为 `mid + 1`。
>    - 如果中间位置的元素大于目标元素，调整右边界 `right` 为 `mid - 1`。
>    - 重复上述步骤，直到找到目标元素或左边界超过右边界。
> 3. **未找到目标元素**：
>    - 如果左边界超过右边界，返回 -1。
>
> 



参考 bisect 源码的二分查找写法，

https://github.com/python/cpython/blob/main/Lib/bisect.py

> 当然可以！下面是一个基于 `bisect_left` 函数的实现，并提供一个详细的二分查找样例。
>
> **二分查找实现**
>
> ```python
> def bisect_left(a, x, lo=0, hi=None, *, key=None):
>     """Return the index where to insert item x in list a, assuming a is sorted.
> 
>     The return value i is such that all e in a[:i] have e < x, and all e in
>     a[i:] have e >= x.  So if x already appears in the list, a.insert(i, x) will
>     insert just before the leftmost x already there.
> 
>     Optional args lo (default 0) and hi (default len(a)) bound the
>     slice of a to be searched.
> 
>     A custom key function can be supplied to customize the sort order.
>     """
> 
>     if lo < 0:
>         raise ValueError('lo must be non-negative')
>     if hi is None:
>         hi = len(a)
>     # Note, the comparison uses "<" to match the
>     # __lt__() logic in list.sort() and in heapq.
>     if key is None:
>         while lo < hi:
>             mid = (lo + hi) // 2
>             if a[mid] < x:
>                 lo = mid + 1
>             else:
>                 hi = mid
>     else:
>         while lo < hi:
>             mid = (lo + hi) // 2
>             if key(a[mid]) < x:
>                 lo = mid + 1
>             else:
>                 hi = mid
>     return lo
> 
> # 二分查找函数
> def binary_search(arr, target):
>     index = bisect_left(arr, target)
>     if index != len(arr) and arr[index] == target:
>         return index  # 返回目标值的索引
>     else:
>         return -1  # 如果未找到目标值，返回 -1
> 
> # 示例
> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
> target = 8
> result = binary_search(arr, target)
> print(f"Target {target} found at index {result}")
> ```
>
> ### 详细步骤
>
> 1. **定义 `bisect_left` 函数**：
>    - **参数**：
>      - `a`：已排序的列表。
>      - `x`：要查找的目标值。
>      - `lo`：搜索范围的起始索引，默认为 0。
>      - `hi`：搜索范围的结束索引，默认为 `len(a)`。
>      - `key`：可选的键函数，用于自定义排序顺序。
>    - **逻辑**：
>      - 检查 `lo` 是否非负。
>      - 如果 `hi` 为 `None`，则设置 `hi` 为 `len(a)`。
>      - 使用二分查找算法找到目标值 `x` 应该插入的位置。
>      - 如果 `key` 为 `None`，直接比较 `a[mid]` 和 `x`。
>      - 如果 `key` 不为 `None`，比较 `key(a[mid])` 和 `x`。
>
> 2. **定义 `binary_search` 函数**：
>    - 使用 `bisect_left` 找到目标值在已排序列表中第一次出现的位置。
>    - 检查目标值是否存在于列表中：
>      - 如果 `index` 不等于列表的长度且 `arr[index]` 等于目标值，返回 `index`。
>      - 否则，返回 -1。
>
> 
>
> **自定义键函数示例**
>
> 假设你有一个包含元组的列表，并且你希望根据元组的第二个元素进行二分查找：
>
> ```python
> def binary_search_with_key(arr, target, key):
>     index = bisect_left(arr, target, key=key)
>     if index != len(arr) and key(arr[index]) == target:
>         return index  # 返回目标值的索引
>     else:
>         return -1  # 如果未找到目标值，返回 -1
> 
> # 示例
> arr = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
> target = 'c'
> result = binary_search_with_key(arr, target, key=lambda x: x[1])
> print(f"Target {target} found at index {result}")
> ```
>
> - **输入**：
>   ```python
>   arr = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
>   target = 'c'
>   ```
> - **输出**：
>   ```python
>   Target c found at index 2
>   ```
>
> ### 总结
>
> 二分查找是一种高效的查找算法，适用于已排序的数据集。你可以使用 `bisect` 模块中的 `bisect_left` 函数来快速实现二分查找，也可以手动实现以学习算法的细节。





# ASCII





# 知识点

## 浅拷贝

在 Python 中声明二维数组时，需要注意避免浅拷贝问题。浅拷贝会导致所有行引用同一个列表，从而在修改一个元素时影响到其他行。为了避免这个问题，可以使用嵌套的列表推导式或循环来创建独立的子列表

> **避免浅拷贝问题**：
>
> - 如果使用 `[[0] * n] * m` 这种方式创建二维数组，会导致所有行引用同一个列表，修改一个元素会影响所有行。例如：
>
> ```python
> matrix = [[0] * n] * m
> matrix[0][0] = 1
> print(matrix)
> # 输出: [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
> ```
>
> - 因此，推荐使用列表推导式或嵌套循环来创建独立的子列表。
>
> **使用列表推导式**
>
> ```python
> # 创建一个 m x n 的二维数组，所有元素初始化为 0
> m = 3
> n = 4
> matrix = [[0 for _ in range(n)] for _ in range(m)]
> print(matrix)
> # 输出: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
> ```
>
> **使用嵌套循环**
>
> ```python
> # 创建一个 m x n 的二维数组，所有元素初始化为 0
> m = 3
> n = 4
> matrix = []
> for i in range(m):
>     row = []
>     for j in range(n):
>         row.append(0)
>     matrix.append(row)
> print(matrix)
> # 输出: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
> ```
>
> ### 解释
> 1. **使用列表推导式**：
>    - `[[0 for _ in range(n)] for _ in range(m)]`：
>      - 外层的 `for _ in range(m)` 生成 `m` 个子列表。
>      - 内层的 `for _ in range(n)` 生成每个子列表中的 `n` 个元素，每个元素初始化为 `0`。
>    - 这种方法简洁且易于理解，适合快速创建多维数组。
>
> 2. **使用嵌套循环**：
>    - 外层的 `for i in range(m)` 循环 `m` 次，每次创建一个新的子列表 `row`。
>    - 内层的 `for j in range(n)` 循环 `n` 次，每次向 `row` 中添加一个 `0`。
>    - 最后将 `row` 添加到 `matrix` 中。
>    - 这种方法虽然代码稍长，但逻辑清晰，适合需要更复杂初始化的情况。
>
> 



请问一下完美立方为什么从a开始循环会少答案？

浮点数精度问题

python开三次方根的误差特别大

确实，处理浮点数时很容易因为精度问题而出现错误。因此，如果可以通过乘法实现的话，应尽量避免使用除法。这样可以减少由于浮点数运算带来的误差，提高计算的准确性。



## 无穷大

### 浮点数无穷大

> 在 Python 中，处理无穷大的概念时，浮点数和整数的行为有所不同。
>
> **浮点数无穷大**
>
> 对于浮点数，Python 支持表示正无穷大和负无穷大。可以使用 `float("inf")` 表示正无穷大，`float("-inf")` 表示负无穷大。例如：
>
> ```python
> positive_infinity = float("inf")
> negative_infinity = float("-inf")
> 
> print(positive_infinity)  # 输出: inf
> print(negative_infinity)  # 输出: -inf
> 
> # 使用 math.inf
> import math
> 
> positive_infinity_float = math.inf
> negative_infinity_float = -math.inf
> print(positive_infinity_float)	# 输出: inf
> print(negative_infinity_float)	# 输出: -inf
> ```
>
> **整数无穷大**
>
> 对于整数，Python 并没有直接支持表示无穷大的整数。整数类型 `int` 在 Python 中是没有固定大小限制的，可以表示任意大的整数，但仍然不是无穷大。如果你尝试将 `"inf"` 转换为整数，会引发一个 `ValueError`：
>
> ```python
> try:
>     int("inf")
> except ValueError as e:
>     print(e)  # 输出: invalid literal for int() with base 10: 'inf'
> ```
>
> 
>
> 

### 整数无穷大

> 在 Python 中，由于整数类型 `int` 没有固定的大小限制，理论上可以表示任意大的整数。但是，Python 并没有直接提供表示整数无穷大的语法或内置常量。如果你需要在程序中表示整数无穷大，可以考虑以下几种方法：
>
> **使用一个非常大的整数**
>
> 你可以选择一个足够大的整数来表示无穷大。这种方法简单直接，但需要注意选择的数值要足够大，以避免在实际计算中被误认为是一个普通的有限值。
>
> ```python
> INFINITY = 10**1000  # 选择一个非常大的整数
> NEGATIVE_INFINITY = -10**1000  # 选择一个非常小的整数
> ```
>
> 





## 函数

问一个初学者的问题:为什么在列表的方法中，有的方法可以连同列表本身作为一个“变量”，比如print(list1.pop())可以输出list1中最后一个元素，而有的方法却不行，比如print(list1.sort())会输出None（而不是排序后的list1）?区别这两种方法是只能靠记忆吗?

> 这是一个很好的问题，涉及到 Python 中列表方法的行为差异。实际上，这些方法之间的区别并不是只能靠记忆，而是可以通过理解它们的工作方式来掌握。
>
> 1. **返回值**：
>    - 一些列表方法，如 `pop()`，执行操作后会返回一个值。`pop()` 方法从列表中移除并返回指定位置的元素，默认情况下是最后一个元素。因此，当你调用 `print(list1.pop())` 时，你会看到被移除的元素被打印出来。
>    - 另一些方法，如 `sort()`，则是在原地对列表进行修改，并不返回任何值（或者更准确地说，返回 `None`）。这是因为 `sort()` 方法直接改变了列表本身的顺序，没有必要再返回整个列表。所以当你尝试 `print(list1.sort())` 时，实际上打印的是 `None`。
>
> 2. **原地操作 vs. 返回新对象**：
>    - 像 `sort()` 这样的方法是对列表进行原地修改的，即它们改变的是原始列表，而不是创建一个新的已排序列表。
>    - 相反，如果一个方法返回了一个新的对象，比如 `sorted(list1)`，它会返回一个新的排序后的列表，而原始列表 `list1` 不会发生变化。
>
> 3. **如何判断**：
>    - 要判断一个方法是否返回值，最好的办法是查阅官方文档或使用帮助功能（如 `help(list.sort)`）。文档通常会明确指出一个方法的行为，包括它是否修改了列表以及是否返回了值。
>    - 经验上，很多修改数据结构的方法（如 `append()`, `remove()`, `reverse()` 等）都是原地操作，而那些用于查询或生成新数据的方法（如 `count()`, `index()`, `copy()` 等）则会返回值。
>



需要熟悉常用函数的返回值。常用的函数有限的，刷30个CF题目基本就都知道了。例如：input,split map,join,enumerate, print,append,sort,remove, index,find,.......

想用的时候先在交互式窗口试一下，help(函数名)。



> 对于在Codeforces上写Python代码的程序，以下是一些常用的函数和功能：
>
> 1. 输入和输出：
>     - `input()`：从标准输入（键盘）获取一行输入
>     - `print()`：输出一个或多个表达式
>     - `map(func, *iterables)`：将函数应用于传入的每个可迭代对象的各个元素
>
> 2. 数学计算：
>     - `abs()`：计算绝对值
>     - `max()` 和 `min()`：分别获取最大值和最小值
>     - `sum()`：计算所有元素的总和
>     - `pow(x, y)`：计算x的y次方
>     - `math.floor()`：向下取整
>     - `math.ceil()`：向上取整
>
> 3. 列表操作：
>     - `len()`：返回列表长度
>     - `append()`：在列表末尾添加新的对象
>     - `extend()`：在列表末尾一次性追加另一个序列中的多个值
>     - `insert()`：将对象插入列表
>     - `sort()`：对列表进行排序
>     - `list()`：生成列表
>
> 4. 字符串操作：
>     - `str.replace()`：字符串替换
>     - `str.split()`：字符串分割
>     - `str.strip()`：移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
>     - `str.join()`：用于将序列中的元素以指定的字符连接生成一个新的字符串
>
> 5. 组合数据类型操作：
>     - `set()`：创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等
>     - `dict()`：创建一个字典
>     
> 6. 控制流：
>     - `if..elif..else`：条件判断
>     - `for...in`：循环
>     - `while`：循环
>     
> 7. 其他有用的内置函数：
>     - `range()`：生成一个数字序列
>     - `enumerate()`：为迭代器增加索引标签，常用于获取列表的元素及其索引
>     
>
> 以上是一些基础的Python函数，另外根据题目需要，可能需要用到其他Python标准库如`itertools`（作用于迭代器的函数），`collections`（高性能容器datatypes），`heapq`（提供堆数据结构的函数）等。



### 考试时候只有 G++,Python

OJ上面 Python的时限是10倍（因为Python程序跑的慢），C/C++是没有放宽的。洛古 上面Python吃亏，因为没有放宽时限，拼不过C/C++。



## T-prime

优化的埃式筛法、或者欧拉筛，可以到 998ms。https://codeforces.com/problemset/problem/230/B



## 时间复杂度

https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt



### 字典



```python
from collections import defaultdict

# 读取输入
m, n, k = map(int, input().split())

# 初始化字典
dict = defaultdict(list)
ans = False

# 处理每一对 (a, b)
for i in range(k):
    a, b = map(int, input().split())
    
    # 如果 b 不在 dict[a] 中，则添加
    if b not in dict[a]:
        dict[a].append(b)
    else:
        continue
    
    # 检查条件
    if (b - 1 in dict[a] and b in dict[a - 1] and b - 1 in dict[a - 1]) or \
       (b + 1 in dict[a] and b in dict[a - 1] and b + 1 in dict[a - 1]) or \
       (b - 1 in dict[a] and b in dict[a + 1] and b - 1 in dict[a + 1]) or \
       (b + 1 in dict[a] and b in dict[a + 1] and b + 1 in dict[a + 1]):
        print(i + 1)
        ans = True
        break

# 如果没有找到符合条件的情况，输出 0
if not ans:
    print(0)
```

CF Pasha and pixels，能否问下这个题用字典为啥会这么慢呢（虽然ac了），就是说什么时候列表快，什么时候字典快呢？

你这个相当于判断 item in alist，自然是慢的。O(1)时候都快。



### 02792: 集合加法

想问一下，集合加法这道题，参考答案似乎是直接暴力遍历，最坏情况复杂度应该是在O(ab)量级吧，但是a,b可以达到10E4量级，再考虑到有多组测试数据，为什么能不超时反而只用了48ms呢

为什么呢？答案相当于对每一个集合A的字典的键key，去找s-key是否in集合B的字典，那复杂度为啥不是a乘b呢？

> 当然，我可以帮你格式化并整理这段文字，使其更清晰易读。以下是格式化后的版本：
>
> ---
>
> **程序主要逻辑**
>
> 这个程序的主要逻辑是在 `calculate_pairs` 函数中实现的。该函数接收两个列表 `arr1` 和 `arr2` 以及一个目标和 `target_sum`。函数的具体步骤如下：
>
> 1. **统计元素出现次数**：
>    - 使用 `Counter` 分别统计两个列表中各元素出现的次数。
>    
> 2. **遍历并查找**：
>    - 遍历 `counter1` 中的每一个元素，检查 `target_sum - item` 是否存在于 `counter2` 中。
>    - 如果存在，则将两者出现次数的乘积累加到答案中。
>
> **时间复杂度分析**
>
> 1. **创建 `Counter` 对象**：
>    - 对于 `arr1` 和 `arr2` 创建 `Counter` 对象的时间复杂度分别是 O(a)和 O(b)，其中 a 和 b分别是 `arr1` 和 `arr2` 的长度。这是因为 `Counter` 在创建时需要遍历整个列表来统计每个元素的出现次数。
>
> 2. **遍历 `counter1` 并查找 `counter2`**：
>    - 这部分的核心操作是对 `counter1` 的每个元素执行一次 `counter2` 的查找操作。由于 `Counter` 是基于字典实现的，查找操作的平均时间复杂度为 O(1)。
>    - 因此，遍历 `counter1` 并进行查找的总时间复杂度为 O(a)。
>
> 综合以上两部分，对于单组测试数据，程序的时间复杂度为 O(a + b)。
>
> **多组测试数据的时间复杂度**
>
> 考虑到输入中可能有多组测试数据，假设最多有 n 组测试数据，每组数据的 a 和 b 的最大值都是 10000，那么最坏情况下的总时间复杂度为 $O(n \cdot (a + b))$。
>
> 
>
> 







# 参考

