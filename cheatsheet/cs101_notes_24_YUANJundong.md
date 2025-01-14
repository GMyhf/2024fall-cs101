---
author: Jundong Yuan
---
### A 语法板块
#### 1 函数的耗时与选择
1. Pop（）函数非常耗时
2. 关于索引，往往集合（set）会比列表（list ）索引快，这是用储存空间换的
3. List.extend () 可以把一组数都加入列表
#### 2 数据类型和控制结构
1. 常见的数据类型：
	1. **不可变数据（3 个）**：Number（数字）、String（字符串）、Tuple（元组）；
	2. **可变数据（3 个）**：List（列表）、Dictionary（字典）、Set（集合）。
	3. 其中 bool（布尔类型）是 int（整数）的子类
		- True== 1；False== 0
		- **注意:** 在 Python 中，所有非零的数字和非空的字符串、列表、元组等数据类型都被视为 True，只有 **0、空字符串、空列表、空元组**等被视为 False。因此，在进行布尔类型转换时，需要注意数据类型的真假性。
	4. 数字
		- 复数用 a+bj 或complex（a, b）表示
		- 无穷大：`float('inf')`
	1. 集合
		- 用{...}表示，创建一个空集合要用 set ()
		- 
		* 顾名思义, 集合中不能有重复的元素, 否则会自动去重.
		* **集合内的元素只能是"零维的"标量.**
		* 添加: `s.add(x)`
		* 查询: `x (not) in s`,**O (1)**
		* 删除:
		  * `s.remove(x)`,**O (1)**
		  * `s.discard(x)`,**O (1)**: 删除 x, 如果没找到 x 就无事发生
		* 弹出: `s.pop()`, O (1): 随弹出一项
		* 清空: `s.clear()`, O (1)
		* 集合运算:
		  * 并: `a|b`, O (len (a)+len (b))
		  * 交: `a&b`, O (len (a)+len (b))
		  * 差:
		    * `a-b`, O (len (a)+len (b)), 注意这是表示∈a 且∉b 的元素的集合,
		      如 `{1}-{1,2}==set(),{1,2}-{1}=={2}`
		    * `a^b`, 对称差, 等于 a|b-a&b
		  * `a>=b,a>b,a<=b,a<b`, O (len (小的那个)) 表示集合的包含关系, 如果既不是子集也不是超集也返回 False
		* 构建集合:
		  * 空集: `a=set()`
		  * 集合化: set (x), x 是列表\元组\字典 (a 是字典则会返回所有键组成的集合)
	1. 字典
		- 字典是一种映射类型，字典用 { } 标识，它是一个无序的 **键(key) : 值(value)** 的集合
		- * **字典的键只能是"零维"标量 (int, float 这种), 而非"一维"以上的复合数据类型.**
		* 删除: `del d[key]`
		* 弹出:
		* `d.pop(key)`, O (1)
		* `d.popitem()`, O (1), 随机弹出一个键值对元组
		* 获取: `d.get(key)`, O (1), 如果 key 不在字典则返回 None 而不报错
		* `d.get(key,dft)` 可以在 key 不在字典时返回默认值 dft
		* 清空: `d.clear()`, O (1)
		* 键 or 值们: `d.keys()`, `d.values()`, O (1).
	2. 堆
		- 堆主要表示优先级队列，每次弹出最小元素同时保持堆结构
		- 创建：**import heapq  heapq.heapify (iterable)
		- 操作：（追加和弹出）
			- **heappush（heap， ele）**：此函数用于将参数中提到的元素插入堆中。
			- **heappop（heap）**：此函数用于从堆中删除并返回最小的元素。
		- 同时追加和弹出：
			- **heappushpop（heap， ele）**：此函数将 push 和 pop 操作的功能合并到一个语句中，从而提高了效率。
			- **heapreplace（heap， ele）**：这个函数也在一条语句中插入和弹出元素，首先弹出元素，然后推送元素。即，可以返回大于推送值的值。heapReplace（） 返回堆中最初存在的最小值，而不管推送的元素是什么，而不是 heappushpop（）。
		- 查询最大最小元素
			- **nlargest（k， iterable， key = fun）**：此函数用于返回指定的可迭代对象中 k 个最大的元素，并满足 key（如果提到）。
			- **nsmallest（k， iterable， key = fun）**：此函数用于从指定的可迭代对象中返回 k 个最小元素。
		- 注：堆的优点是高效灵活地管理数据；缺点是无法随机访问，无法特定排序
	- deque（双向列表）
		- 减小pop () 和append () 的时间复杂度
		- 同时增加了 popleft ()
#### 3 常用处理数据的函数
1. 读取列表切片时可以设置步长 list[2:6:2]，特别的，list.reverse ()=list[-1::-1]
2. :=  海象运算符，这个运算符的主要目的是在表达式中同时进行赋值和返回赋值的值。**Python3.8 版本新增运算符**。
3. 按位运算符是把数字看作二进制来进行计算的。Python中的按位运算法则如下：
	下表中变量 a 为 60，b 为 13二进制格式如下
	a = 0011 1100
	b = 0000 1101
4. 字符串格式化
	1. %s：格式化字符串
	2. %d：格式化整数
	3. %f：格式化浮点数，可指定小数位数
5. Strip (): 清楚字符串的首（lstrip）和尾（rsplit）的空格或指定字符
6. 将对象插入列表：list.insert (index,...)
7. 列表推导式：【f (i) for i in ... if i ...】
8. 能用内置函数尽量用，速度快（用 C 实现的）
9. List. sort (reverse=True)
10. 字典{key: value}
	1. In 索引只能索引 key 值；如果要索引 value 要 in dictionary. Value ()
	2. 字典查找：value=dictionary【key】
	3. 字典反转：{v: k for k, v in dictionary. Item ()}
	4. 增加元素：dict. Setdefault (key, value)（如果 key 有了就更新 value，如果没有就增加索引）
11. Print (f'...') 用{name: . 2 f}可以是输出字符串,: 后的为输出格式
12. Counter 函数（from collections）可以统计列表中的词频，并返回一个字典
13. 正则表达式
14. 二分查找（bisect. bisct_left(right)(arr, x)）
	1. Left：输出第一个>=x 的 index
	2. Right：输出第一个>x 的 index
16. Leetcode 的函数调用
```python
if __name__ == "__main__":
    sol = Solution()
    print(sol.xxxx()) 
```
17. enumerate (list)：可以在循环中同时返回索引和值
```python
for index,element in enumerate(list):
```
18. permutations (list, length): 返回列表的长度为 length 的全排序（itertools）
19. 深拷贝 
```python
import copy
a=copy.deepcopy()
```
20. 自定义列表排序方式：
```python
from functools import cmp_to_key

def compare(a,b):
	return 1 #交换a，b
	return 0 #相等
	return -1 #不操作
arr.sort(key=cmp_to_key(compare))

arr.sort(key=lambda x:x[1],reverse=True)
```
1. `str.lstrip() / str.rstrip()`: 移除字符串左侧/右侧的空白字符。
2. `str.find(sub)`: 返回子字符串 `sub` 在字符串中首次出现的索引，如果未找到，则返回-1。
3. `str.replace(old, new)`: 将字符串中的 `old` 子字符串替换为 `new`。
4. `str.startswith(prefix) / str.endswith(suffix)`: 检查字符串是否以 `prefix` 开头或以 `suffix` 结尾。
5. `str.isalpha() / str.isdigit() / str.isalnum()`: 检查字符串是否全部由字母/数字/字母和数字组成。

| 运算符 | 描述                                                 | 实例                                                 |
| --- | -------------------------------------------------- | -------------------------------------------------- |
| &   | 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0           | (a & b) 输出结果 12 ，二进制解释： 0000 1100                  |
| \|  | 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。                    | (a \| b) 输出结果 61 ，二进制解释： 0011 1101                 |
| ^   | 按位异或运算符：当两对应的二进位相异时，结果为1                           | (a ^ b) 输出结果 49 ，二进制解释： 0011 0001                  |
| ~   | 按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1      | (~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。 |
| <<  | 左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。 | a << 2 输出结果 240 ，二进制解释： 1111 0000                  |
| >>  | 右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数     | a >> 2 输出结果 15 ，二进制解释： 0000 1111                   |
### B 算法基础
#### 1 双指针 
##### 1.1  二分查找
**思路：** 把一个求值问题变成一个逼近问题，试探找最优解

二分查找最关键的是**边界控制**，由此可以引申出两种写法：

一、记录答案法
（l和r代表的“值”均可行，且有一个ans变量记录当前的最优）
```python
while l<=r:
	mid=(l+r)//2
	if check(mid):
		ans=mid
		r=mid-1
	else:
		l=mid+1
return ans
```
即当 mid可行时，就记录 mid，并且缩小范围，找有没有最优的（就不用考虑 mid 对应的值）

二、不记录法
（l和r代表的“成本值”均可行，最后的答案是l或r）
```python
while l<r:
	mid=(l+r)//2
	if check(mid):
		r=mid
	else:
		l=mid+1
return l
```
当 l=r 时循环停止，此时输出 l 或 r 都可以
这种写法的关键是我们要保证 **l 和 r 都是暂时可行的且 l 要极小，r 要极大**

**注意！** 此时有一个非常容易出错的地方
当我们想找到不符合条件的最大时（和上面相反）
r=mid-1（false）/l=mid（true）
但是有一种特殊情况：**如果l=2，r=3，mid=5/2=2，此时测试的check(mid)如果为true，那么l和r将永远卡在2和3，所以在此处，我们取的中点要靠右，也就是 mid=(l+r+1)/2，这样就能保证l和r不死循环**

Check()的时候一定要注意最后边界的处理

n 数之和问题
##### 1.2 快慢指针
##### 1.3滑动窗口
```python
#外层循环扩展右边界，内层循环扩展左边界
l=0
for r in range(len()):
	//当前考虑的元素
	while l<=r and check():
		l+=1
		#扩展左边界
    //区间[left,right]符合题意，统计相关信息
```
 
#### 2 矩阵处理
 1. 加保护圈 （防止在一个大范围内处理时，value error）
 2. Range 中用 min、max
 3. 定义 visit 函数
#### 3 线段树
#### 4 排序
##### 4.1 冒泡排序
方法： 在无序区通过反复交换找到最大元素放在队首（比较次数多，交换次数多） 
主要思想： 前后两两比较，大小顺序错误就交换位置
```python
def BubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```
##### 4 2 选择排序
方法：在无序区找到最小的元素放到有序区的队尾（比较次数多，交换次数少） 
主要思想：水果摊挑苹果，先选出最大的，再选出次大的，直到最后。选择是对冒泡的优化，比较一轮只交换一次数据。
```python
def SelectSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
               minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr
```
##### 4 3 插入排序 
方法：把无序区的第一个元素插入到有序区的合适位置（比较次数少，交换次数多） （反向选择排序）
主要思想：扑克牌打牌时的插入思想，逐个插入到前面的有序数中。
```python
def InsertSort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr
```

##### 4 4 快速排序
原理：快速排序的基本思想是选取一个基准元素，将数组分成两部分，使得左边部分的元素都小于等于基准元素，右边部分的元素都大于等于基准元素，然后对左右两部分分别递归进行排序，最终得到一个有序数组

```python
def quick_sort(arr):
"""
快速排序算法的实现函数
Parameters:
    arr (list): 要排序的数组
Returns:
    list: 排序后的数组
"""
# 如果数组长度小于等于1，则直接返回
if len(arr) <= 1:
    return arr

# 选择基准元素
pivot = arr[0]

# 分割数组
left = [x for x in arr[1:] if x <= pivot]
right = [x for x in arr[1:] if x > pivot]

# 递归调用快速排序算法，并将分割后的数组合并起来
return quick_sort(left) + [pivot] + quick_sort(right)
```

##### 4 5 归并排序
原理：归并排序（Merge Sort）是一种基于分治思想的排序算法，它将待排序的数组分成两部分，分别对这两部分递归地进行排序，最后将两个有序子数组合并成一个有序数组

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
 
    # 将数组分成两个部分
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
 
    # 对左右两部分分别递归调用归并排序
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
 
    # 合并左右两部分
    return merge(left_half, right_half)
 
def merge(left_half, right_half):
    i = j = 0
    merged = []
 
    # 比较左右两部分的元素，将较小的元素添加到 merged 中
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1
 
    # 将左右两部分中剩余的元素添加到 merged 中
    merged += left_half[i:]
    merged += right_half[j:]
 
    return merged
```
#### 5 区间问题
##### 5.1 区间合并
- 给出一堆区间，要求**合并**所有**有交集的区间** （端点处相交也算有交集）。最后问合并之后的**区间**。
- 如下图所示：

![img](https://pic4.zhimg.com/80/v2-6e3bb59ed6c14eacfa1331c645d4afdf_1440w.jpg)

<center>区间合并问题示例：合并结果包含 3 个区间</center>
- 解题步骤
	- 【**步骤一**】：按照区间**左端点**从小到大排序。
	- 【**步骤二**】：维护前面区间中最右边的端点为 ed。从前往后枚举每一个区间，判断是否应该将当前区间视为新区间。
	- 假设当前遍历到的区间为第 i 个区间 $[l_i,r_i]$，有以下两种情况：
		- $l_i \le ed$：说明当前区间与前面区间**有交集**。因此**不需要**增加区间个数，但需要设置 $ed = max(ed, r_i)$。
		- $l_i > ed$: 说明当前区间与前面**没有交集**。因此**需要**增加区间个数，并设置 $ed = max(ed, r_i)$。
##### 5.2 选择不相交区间
- 给出一堆区间，要求选择**尽量多**的区间，使得这些区间**互不相交**，求可选取的区间的**最大数量**。这里端点相同也算有重复。
- 如下图所示：

![img](https://pic1.zhimg.com/80/v2-690f7e53fd34c39802f45f48b59d5c5a_1440w.webp)

<center>选择不相交区间问题示例：结果包含 3 个区间</center>
- 【**步骤一**】：按照区间**右端点**从小到大排序。
- 【**步骤二**】：从前往后依次枚举每个区间。
	- 假设当前遍历到的区间为第 i 个区间 $[l_i,r_i]$，有以下两种情况：
		- $l_i \le ed$：说明当前区间与前面区间有交集。因此直接跳过。
		- $l_i > ed$: 说明当前区间与前面没有交集。因此选中当前区间，并设置 $ed = r_i$。
##### 5.3 区间选点问题
- 给出一堆区间，取**尽量少**的点，使得每个区间内**至少有一个点**（不同区间内含的点可以是同一个，位于区间端点上的点也算作区间内）
- 如下图所示：

![img](https://pica.zhimg.com/80/v2-a7ef021e1191ec53f20609ba870b44ba_1440w.webp)

<center>区间选点问题示例，最终至少选择 3 个点</center>
- 解题方法：同上找出最大不相交区间，会有一个点
##### 5.4 区间覆盖问题
- 给出一堆区间和一个目标区间，问最少选择多少区间可以**覆盖**掉题中给出的这段目标区间。
- 如下图所示： 
![img](https://pic3.zhimg.com/80/v2-66041d9941667482fc51adeb4a616f64_1440w.webp)

<center>区间覆盖问题示例，最终至少选择 2 个区间才能覆盖目标区间</center>
- 【**步骤一**】：按照区间左端点从小到大排序。
- 【**步骤二**】：**从前往后**依次枚举每个区间，在所有能覆盖当前目标区间起始位置 start 的区间之中，选择**右端点**最大的区间：
	- 假设右端点最大的区间是第 $i$ 个区间，右端点为 $r_i$。
	- 最后将目标区间的 start 更新成 $r_i$
- 注：考虑是否可以单序扫过整个片段
##### 5.5 区间分组问题
- **区间分组**问题大概题意就是：给出一堆区间，问最少可以将这些区间分成多少组使得每个组内的区间互不相交。
- 如下图所示： 

![img](https://pic2.zhimg.com/80/v2-6c6a045d481ddc44c66b046ef3e7d4cd_1440w.webp)

<center>区间分组问题示例，最少分成 3 个组</center>
- 【**步骤一**】：按照区间左端点从小到大排序。
- 【**步骤二**】：从**前往后**依次枚举每个区间，判断当前区间能否被放到某个现有组里面。
	- （即判断是否存在某个组的右端点在当前区间之中。如果可以，则不能放到这一组）
	- 假设现在已经分了 m 组了，第 k 组最右边的一个点是 $r_k$，当前区间的范围是 $[L_i,R_i]$ 。则：
		- 如果 $L_i \le r_k$ 则表示第 i 个区间无法放到第 k 组里面。反之，如果 $L_i > r_k$，则表示可以放到第 k 组。
		- 如果所有 m 个组里面没有组可以接收当前区间，则当前区间新开一个组，并把自己放进去。
		- 如果存在可以接收当前区间的组 k，则将当前区间放进去，并更新当前组的 $r_k = R_i$。
- **注意：**
	- 为了能快速的找到能够接收当前区间的组，我们可以使用**优先队列 （小顶堆）**。
	- 优先队列里面记录每个组的右端点值，每次可以在 O (1) 的时间拿到右端点中的的最小值

#### 6 递归算法
##### 6.0 引言
什么是递归？ 实际上就是一个函数重复调用自身
注意死循环——递归要有出口
递归往往有副作用——递过去途中的和归来途中, 其中递过去往往是**问题规模缩小**的过程, 归来过程是已经触及到出口后的返回

##### 6.1 如何设计递归 
1. 找重复/递推式，思考问题规模如何变小
2. 找变化
3. 找边界，就是递归出口

> Example 1：求 n 阶乘
>1. 找重复: n的阶乘 = n * (n - 1的阶乘), 那么 **求 "n - 1的阶乘"就是原问题的重复** -- **子问题**
>2. 找变化: 这里就是n的量越变越小 -- 变化的量往往作为参数
>3. 找边界: 出口, 找一个数的阶乘, 不可能小于1

```python
def jiecheng(n):
    if(n == 1 ):
        return 1
    return n * jiecheng(n - 1)
```

>Example 2：顺序打印 i 到 j ( i <= j , 包含j)
>1. 找重复:
>2. 找变化: 这里就是n的量越变越小 -- 变化的量往往作为参数
>3. 找边界: 出口, 即 i = j 时

```python
def print_i_j(i , j ):
    if(i > j):
        return
    print(i)
    print_i_j(i +1 , j)
```

>Example 3：倒序打印 i 到 j ( i <= j , 包含j)

```python
def print_i_j(i , j ):
    if(i > j):
        return
    print_i_j(i +1 , j)
    print(i, end=" ")
```
- 顺序打印: 先打印出i ,再自身调用小一号规模的子问题, 这就相当于是自己先处理一些,剩下的交给其他人处理(先花1元钱, 剩下的交给下一个人花) . 这也就是所谓的 **在递出去时产生的副作用**  
- 倒序打印: 先调用小一号的子问题, 由于在自身调用前, 也就是"递出去时"没有其余动作, 重复调用会直至递归出口, 然后依次返回, 子函数在反回到父函数时会接着父函数调用位置的下一行继续执行, 这就是所谓的 **在归回来的产生的副作用** .

关键是**找变化**，变化的量往往作为参数和返回判据
同时，**在变化中如何添加参数**也是递归设计的难点
**变化中寻找重复构以成递归, 重复中寻找变化以靠近出口**

前面的递归设计中, 我们可以将其统称为: **求解f(N),我们自己做一部分x, 其他的交给和我同样功能的人做f(N- 1),直到分不了为止. 换句话说, 为求解f(N),我们可以先求解缩小一次规模的问题f(N-1), 加之一些副作用x**. 如下:

```text
f(N) = x + f(N - 1)
```

在递归中, 除了上面那种缩小一点问题规模,带点副作用,再缩小 ... 还有将问题 拆分成两个子问题去分别求解的,比如:

```text
f(N) = f(N/2) + f(N/2) + X          
#将问题N拆成两半,分别求解f(N/2)
f(N) = f(N - 1) + f(N - 2) + x      
#为求解f(N),需要的比现在小1号的子问题f(N-1)和小2号的子问题f(N-2)
f(N) = f(N/k) + f(N/k) + f(N/k) + ...
```

>Example 4：斐波那契数列
```python
def fibo(n):
    if n <= 2:
        return 1
    return  fibo(n -1) + fibo(n -2)
```

>Example 5：求解最大公因数（辗转相除）
```python
def gcd(m ,n ):
    if n == 0:
       return m
    return gcd(n , m%n)
```
**_递归设计思路小结:_**
**_找重复:_**
1. **_找到一种划分成更小规模问题的方法, 或者是单个划分,或者是多个划分, 另外也可能选择划分_**
2. **_找到递推公式或者等价转换_**

**_找变化:_**
​ **_变化的量通常会作为参数,(循环的过程也是变化)_**

**_找出口:_**
​ **_变化的极限往往就是出口.(循环的终点就是出口)，递归一定是缩小范围的，朝着出口走的_**

**一定要相信自己的函数是正确的并依据此推导，同时要搞清楚函数是在该层干啥的

##### 递归优化
**增加递归深度限制**：使用 `sys.setrecursionlimit` 来增加 Python 的递归深度限制。
```python
import sys
sys.setrecursionlimit(1 << 30)  # 将递归深度限制设置为 2^30
```

**缓存中间结果**：使用 `functools.lru_cache` 或其他形式的 memoization（记忆化）来避免重复计算。
```python
from functools import lru_cache
@lru_cache(maxsize=None)
```
#### 7 dfs（深度优先搜索）
为了避免重复子问题，应建立一个数组存放状态，并且及时更新状态
这时候可以建立一个函数，判断是否符合条件（辅助 visited 空间）
```python
visited = [[False for _ in range(m)] for _ in range(n)]

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m and maze[x][y] == 0 and not visited[x][y]
```

利用栈来模拟递归
#### 8 动态规划
##### 理解
**将一个问题拆成几个子问题***，分别求解这些子问题，比较后得到最优解，即可推断出大问题的解
**尽可能地缩小可能的解空间**，即 dp 自带剪枝
牺牲空间换时间


##### 前提
1. **无后效性**：一旦f(n)确定，“我们如何凑出f(n)”就再也用不着了，
	- 严格定义：如果给定某一阶段的状态，则在这一阶段以后过程的发展不受这阶段以前各段状态的影响
2. **最优子结构**：大问题的**最优解**可以由小问题的**最优解**推出

##### 设计 dp 算法
- **设计状态**：我们把面对的局面用参量表示，记为 x，把要求解的东西记为 f (x)
- **设计状态转移**：
	- **找出f(x)与哪些局面有关（记为p）**，写出一个式子（称为**状态转移方程**），通过f(p)来推出f(x)
	- 自下而上推导：递推实现
	- 自上而下搜索：递归实现（往往要记忆化搜索，即开一个数组）

##### 8.1 01 背包：
$CELL[i][j] = max(CELL[i−1][j]; V_i + CELL[i−1][j− W_i])$
注意：由于 CELL i 处的值只与 i-1 有关，我们可以采用滚动数组的方法，只用一个数组并且**倒序**更新

**二维 01 背包**（即有两个限制条件）
采用一个二维数组（x, y, 中间的数为两个限制条件+更新条件的组合，应当挑选合适的组合使得二维数组空间最小）

**多重背包问题**（每个物品有上限）
二进制优化

##### 8.2 完全背包 ：
允许在不超容量的前提下无限次选取
思路：自下而上更新

```python
def knapsack_complete(weights, values, capacity):
    dp = [0] * (capacity + 1)  # dp[j]为当背包容量为j时,背包所能容纳的最大价值
    dp[0] = 0
    for i in range(len(weights)):  # 遍历所有物品
        for j in range(weights[i], capacity + 1):  # 从当前物品的重量开始，计算每个容量的最大价值
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
    return dp[capacity]
```

必须装满的类型:（可以采用字典记录装满的部分，只对字典中的元素迭代）
```python
def knapsack_complete_fill(weights, values, capacity):
    dp = [-float('inf')] * (capacity + 1)  # 初始值为负无穷，表示不能达到该容量
    dp[0] = 0  # 容量为 0 时，价值为 0
    for i in range(len(weights)):  # 遍历所有物品
        for w in range(weights[i], capacity + 1):  # 遍历所有容量，从 weights[i] 开始 
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    # 如果 dp[capacity] 仍为 -inf，说明无法填满背包
    return dp[capacity] if dp[capacity] != -float('inf') else 0
```

##### 8.3 整数划分 ：
```python
from functools import lru_cache

while True:
    try:
        @lru_cache(maxsize=None)
        def did(n,m):#不大于m划分n
            if n==1 or m==1:
                return 1
            elif n==m:
                return 1+did(n,n-1)
            elif n>m:
                return did(n,m-1)+did(n-m,m)
            else:
                return did(n,n)
        k=int(input())
        print(did(k,k))
    except EOFError:
        break
```

##### 8.4 Kadane 算法
* `max_cur=max(max_cur+v[i],v[i])`.如果 `max_cur` (已经买到的商品总价值)已经为负,就把它们全扔了重买第i个.否则不扔,并买第i个.
* 每次买之后都要更新一下商品的最大总价值(max_all).

```python
def kadane(v):#卡丹算法求最大子序列
    max_cur=0
    max_all=0
    for i in range(len(v)):
        max_cur=max(v[i],max_cur+v[i])
        max_all=max(max_all,max_cur)
    return max_all
```

* 通过这种算法进行衍生,可以类似地求**最大子矩阵**.具体思路是:

  1. 选出矩阵的第l至r列作为一个**切片**,对于这个切片的每一行,**求出其和**,以这些**和**构建一个列表a,这样就把第l至r列的矩阵切片一维化了.
  2. 用Kadane算法求出这个**列表a的最大子串的值,这就是第l~r列的最大子矩阵的值**.如图.
  3. 遍历所有可能的l,r,然后求出全局的最大子矩阵的值.

  * 求切片的和时可以用前缀和:
    1. 构建一个前缀和矩阵qzh,每一行的第i个元素是这一行第0~i元素的和
    2. 某一行l~r列的元素的元素和就是qzh[r]-qzh[l-1].前缀和矩阵需要在左边加一列0做保护层
```python
def qzh(mat,n,m):#前缀和
    qzh=[]
    for i in range(n):
        qzh.append([0])
        for j in range(m):qzh[i].append(qzh[i][-1]+mat[i][j])
    return qzh
def kadane(a):#卡丹算法求最大子序列
    max_cur=0
    max_all=0
    for i in range(len(a)):
        max_cur=max(a[i],max_cur+a[i])
        max_all=max(max_all,max_cur)
    return max_all
def max_submat(qzh,n,m):
    #现在我要算每个对于左边界为l，右边界为r的，上下浮动和伸缩的一系列子矩阵的最大值
    maxn=0
    for l in range(1,m+1):
        for r in range(l,m):
            a=list(qzh[i][r]-qzh[i][l-1] for i in range(n))
            maxn=max(maxn,kadane(a))
    return(maxn)
#主函数
n,m=map(int,input().split())#行数:n,列数:m
mat=[]
for i in range(n):
    mat.append(list(map(int,input().split())))
qzh=qzh(mat,n,m)
print(max_submat(qzh,n,m))
```

#### 9 BFS（宽度优先搜索）
广度优先搜索 (BFS) 一般由队列实现, 且总是按层次的顺序进行遍历，其基本写法如下 (可作模板用):

```python
from collections import deque
  
def bfs(s, e):
    inq = set()
    inq.add(s)
      
    q = deque()
    q.append((0, s))

    while q:
        now, top = q.popleft() # 取出队首元素
        if top == e:
            return now # 返回需要的结果，如：步长、路径等信息

        # 将 top 的下一层结点中未曾入队的结点全部入队q，并加入集合inq设置为已入队
  
```



下面是对该模板中每一个步骤的说明, 请结合代码一起看: 

① 定义队列 q，并将起点 (0, s) 入队，0 表示步长目前是 0。
② 写一个 while 循环，循环条件是队列 q 非空。
③ 在 while 循环中，先取出队首元素 top。
④ 将 top 的下一层结点中所有**未曾入队**的结点入队，并标记它们的层号为 now 的层号加 1，并加入集合 inq 设置为已入队。
⑤ 返回 ② 继续循环。


为了防止走回头路，一般可以设置一个 bool 类型数组 inq（即 in queue 的简写）来记录每个位置是否在 BFS 中已入过队。再强调一点，在 BFS 中设置的 inq 数组的含义是判断结点是否已入过队，而不是**结点是否已被访问**。区别在于：如果设置成是否已被访问，有可能在某个结点正在队列中（但还未访问）时由于其他结点可以到达它而将这个结点再次入队，导致很多结点反复入队，计算量大大增加。因此 BFS 中让每个结点只入队一次，故需要设置 inq 数组的含义为**结点是否已入过队**而非结点是否已被访问。

同时建立一个函数来帮助判断

**记忆化搜索**：如果我们只关注终点的值，我们固然可以只用搜索寻找，但是，当我们需要进行比较或者需要保留中间值时，我们就需要开一个 dp 数组记录状态

如果是处理**有权图问题**，则可以令 deque 为 heap 处理，按步长排序
#### 10 单调栈，辅助栈
想清楚维护一个单调栈是要干什么，即当元素不是符合单调性时，要对弹出的元素进行什么操作

>[!example] 接雨水
>monotonic stack, https://leetcode.cn/problems/trapping-rain-water/
>给定 `n` 个非负整数表示每个宽度为 `1` 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                bounded_height = min(height[i], height[stack[-1]]) - height[top]
                water += distance * bounded_height
            stack.append(i)
        return water

```

关键就是 while 循环的设计，当不单调的时候依次比较末尾元素，并弹出操作
#### 11 dijkstra 算法（dp+greedy+BFS）
##### 1 基本思想
Dp：维护一个从起点到各点的路径序列
Greedy：从当前 open 节点中最短的路径考虑
BFS：把当前考虑的与列表中的进行比较

##### 2 具体步骤 ：
1. 设置两个集合 open 和 close 分别存放未找到最短路径的节点和找到最短路径的节点，并且设置一个数组记录父子节点（回溯路径用）
2. 从起点开始拓展，每一步为一个节点找到最佳路径
	1. 每当 close 中加入一个新节点 i，以该节点为起点更新所有 open 中的节点距离信息：$d(s,j)=min(d(s,j),d(s,i)+d(i,j))$，同时更新父节点
	2. 找到距离最小的节点，将其添加到 close 中

##### 3 具体实现
- 初始化时：$d(s,i)=+inf，d(s,s)=0$，close 中加入 s
- 为了保证距离最小，可以采用优先队列（heap）
- 但是 heap 中无法对距离进行操作，因此要记录距离和 visit（访问过的节点）

>[!example] 20106: 走山路
>Dijkstra, http://cs101.openjudge.cn/practice/20106/
>思路：
>Dijkstra 在 visited 的更新上还有 while 的结束方式上，都和 bfs 有很大区
别，清楚这两点感觉就分的清了

```python
import heapq

m,n,p=map(int,input().split())
mat=[]
for i in range(m):
    mat.append(list(input().split()))
visited=set()
def visit(x,y):
    return 0<=x<m and 0<=y<n and mat[x][y]!='#' and (x,y) not in visited
def shortroad(a,b,c,d):
    global visited
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    pq=[(0,(a,b))]
    visited.clear()
    visited.add((a,b))
    if mat[a][b]=='#':
        return 'NO'
    while pq:
        dis,node=heapq.heappop(pq)
        if node==(c,d):
            return dis
        visited.add(node)
        x,y=node
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if visit(nx,ny):
                hp=abs(int(mat[nx][ny])-int(mat[x][y]))
                heapq.heappush(pq,(dis+hp,(nx,ny)))
    return 'NO'

for _ in range(p):
    a,b,c,d=map(int,input().split())
    print(shortroad(a,b,c,d))
```


注：该算法是为了求到任意节点的最短距离，如果是特定起点和终点，则可以用 BFS+heap
#### 12 路径回溯
```python
parent={start:None}
if goal in parent:
        path = []
        step = goal
        while step is not None:
            path.append(step)
            step = parent[step]
        path.reverse()  # 因为我们是从目标节点回溯到起始节点，所以需要反转路径
        return path
```

#### 13 懒更新
### 数学知识
#### 1 拓展欧几里得（生理周期）
#### 2 dilworth 定理
最小覆盖整个数组的不减子序列数等于最长严格上升子序列长度
#### 3 欧拉筛
* 筛出 1<=i<=n 所有的素数
* 输入范围 n, 输出 1~n 的素数列表
* 如果你想查询一个很大的数是不是素数, 把里面 prime 一开始做成集合再返回用来查询
  ```python
  def ES(n):
    isprime=[True for _ in range(n+1)]
    prime=[]
    for i in range(2,n+1):
        if isprime[i]:
            prime.append(i)
        for j in range(len(prime)):
            if  i*prime[j]>n:break
            isprime[i*prime[j]]=False
            if i%prime[j]==0 :break

    return prime
  ```

