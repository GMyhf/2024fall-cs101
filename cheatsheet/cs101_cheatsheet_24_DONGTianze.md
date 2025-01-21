

#### 一、基本语法以及一些特殊函数

##### 1.ASCLL表

![](https://raw.githubusercontent.com/xwk-tomorin/picture/main/20241220123842.png)

```
ord('A')==65,chr(65+32)=='a','A'.lower()->'a','a'.upper()->'A'
```

##### 2.counter()

记录各个元素记录的个数，本质是字典

```
from collections import Counter
a = [12, 3, 4, 3, 5, 11, 12, 6, 7]
x=Counter(a)
for i in x.keys():
      print(i, ":", x[i])
x_keys = list(x.keys()) #[12, 3, 4, 5, 11, 6, 7]
x_values = list(x.values()) #[2, 2, 1, 1, 1, 1, 1]
for i in x.elements():
    print ( i, end = " ") #[12,12,3,3,4,5,11,6,7]
c=Counter('1213123343521231255555555')
cc=sorted(c.items(),key=lambda x:x[1],reverse=True) 
#[('5', 9), ('1', 5), ('2', 5), ('3', 5), ('4', 1)]
```

##### 3.enumerate() 索引和函数一起出现

```
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
##[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
for i,element in enumerate(seasons):
    print(i,element)
```

```
全排列
from itertools import permutations

# 生成 [1, 2, 3] 的所有排列
perm = permutations([1, 2, 3])
print(list(perm))  # 输出：[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
```

```
from itertools import permutations

# 生成 'ABC' 中选取 2 个字符的所有排列
perm = permutations('ABC', 2)
print(list(perm))  # 输出：[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
```

##### 4.判断质数：（只用最快的线性筛）

```
def euler_sieve(n):
    is_prime = [True] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
        for p in primes:
            if i * p > n:
                break
            is_prime[i * p] = False
            if i % p == 0:
                break
    return primes
```

##### 5.cmp_to_key

如果你的 `key` 函数比较复杂，可以考虑使用 `functools.cmp_to_key` 来定义一个比较函数。这样可以更灵活地处理复杂的比较逻辑。

**详细解释**

1. **`compare_items` 函数**：
   - 定义一个比较函数 `compare_items`，用于比较两个元组的第二个元素。
2. **`cmp_to_key` 函数**：
   - 将 `compare_items` 转换为 `key` 函数，传递给 `bisect_left`。
3. **`if index < len(arr) and key(arr[index], (0, target)) == 0`**：
   - 使用 `key` 函数比较 `arr[index]` 和 `(0, target)`，确保它们的第二个元素相等。

```
from functools import cmp_to_key
def compar(a,b):
    if a>b:
        return 1#大的在后
    if a<b:
        return -1#小的在前
    else:
        return 0#返回零不变位置
l=[1,5,2,4,6,7,6]
l.sort(key=cmp_to_key(compar))
print(l)#[1,2,4,5,6,6,7]
```

##### 6.lambda函数的使用（主要是在字典排序中）

基本模板：lambda arguments: expression #参数：对参数进行的操作 

在字典排序中： 

sorted_dict = sorted(my_dict.items(), key=lambda x: x[1]) 

\#按值升序排序，注意sorted得到的是一个列表! 

\#如果想要降序并转化为字典格式如下： 

sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True)) 

与map结合： 

\# 对列表中的每个元素进行平方操作 

squared_numbers = list(map(lambda x: x ** 2, numbers))

```
def binary_search_with_key(arr, target, key):
    index = bisect_left(arr, target, key=key)
    if index != len(arr) and key(arr[index]) == target:
        return index  # 返回目标值的索引
    else:
        return -1  # 如果未找到目标值，返回 -1

# 示例
arr = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
target = 'c'
result = binary_search_with_key(arr, target, key=lambda x: x[1])
print(f"Target {target} found at index {result}")
```

##### 7.sys读入输出

取代input(),print()

```
import sys
#输入
input = sys.stdin.read
data = input().split()
#输出
sys.stdout.write('\n'.join(map(str, results)) + '\n')
```

还可以替代：

```
while(True):
	try:
		...
	except EOFError:
		break
```

##### 8.defaultdict

有默认值的字典

```
from collections import defaultdict
d = defaultdict(int)
L = [1, 2, 3, 4, 2, 4, 1, 2]
for i in L:
    d[i] += 1
print(d)##defaultdict(<class 'int'>, {1: 2, 2: 3, 3: 1, 4: 2})

d = defaultdict(list)
for i in range(5):
    d[i].append(i)
print(d)##defaultdict(<class 'list'>, {0: [0], 1: [1], 2: [2], 3: [3], 4: [4]})

d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2
print(d["a"])#1
print(d["b"])#2
print(d["c"])#Not Present
```

##### 9.冒泡排序

```
for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

#### 二、三种常用数据结构

##### 1.只有一端能进出stack

使用list，并且只用pop(),append()进行出栈入栈即可实现

##### 2.两端都能进出的deque

两端进出都是O(1)

```
from collections import deque
de=deque([1,2,3])
de.append(4)
de.appendleft(5)
de.extend([6,7,8])
de.extendleft([9,10,11])
de.pop()
de.popleft()
print(de)##deque([10, 9, 5, 1, 2, 3, 4, 6, 7])
```

##### 3.维护第一个最小的小顶堆heapq

```
import heapq
li = [5, 7, 9, 1, 3]
heapq.heapify(li)
heapq.heappush(li,4)
heapq.heappop(li) #1
print(li) #[3, 5, 4, 7, 9]
n_smallest = heapq.nsmallest(3, li) #[3,4,5]
n_largest = heapq.nlargest(2, li) #[9,7]
```



`heapq`模块中的主要操作函数的时间复杂度如下：

- `heapify`: 将列表转换为堆的时间复杂度为O(N)，其中N是列表的长度。
- `heappush`: 向堆中插入元素的时间复杂度为O(logN)，其中N是堆的大小。
- `heappop`: 从堆中弹出最小元素的时间复杂度为O(logN)，其中N是堆的大小。
- `heappushpop`: 向堆中插入元素并弹出最小元素的时间复杂度为O(logN)，其中N是堆的大小。
- `heapreplace`: 弹出最小元素并插入新元素的时间复杂度为O(logN)，其中N是堆的大小。

#### 三、贪心和矩阵

贪⼼算法是⽤来解决⼀类最优化问题，并希望由局部最优策略来推得全局最优结果

双指针（略）和⼆分查找是贪⼼算法中常⽤的技巧

对于矩阵有加保护圈这一技巧（太简单略）

##### 1.二分查找：

```
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

**二分查找**

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

也可以直接引库

```
import bisect
bisect.bisect(a,x)
bisect.bisect_left(a,x)
bisect_insort(a,x)(直接利用insect(lo,x))
bisect.bisect_left(a,x)
```

##### 二分查找序列合并

再来看序列合并问题。假设有两个递增序列A 与B，要求将它们合并为一个递增序列C。同样的，可以设置两个下标i和j，初值均为 0，表示分别指向序列 A 的第一个元素和序列B的第一个元素，然后根据 A[i]与 B[i]的大小来决定哪一个放入序列 C。

① 若 A[i] < B[ì]，说明 A[i]是当前序列 A 与序列 B 的剩余元素中最小的那个，因此把A[i]加入序列 C 中，并让i加1（即让i右移一位）。

② 若 A[ì] > B[j]，说明 B[i]是当前序列 A 与序列B 的剩余元素中最小的那个，因此把B[i]加入序列C 中，并让j加1（即让j右移一位）。

③ 若 Aí] == B[j]，则任意选一个加入到序列 C 中，并让对应的下标加 1。上面的分支操作直到i、j中的一个到达序列末端为止，然后将另一个序列的所有元素依次加入序列C 中，代码如下:

```
def merge(A, B):
    i, j = 0, 0
    c = []

    # 合并两个有序数组
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            c.append(A[i])
            i += 1
        else:
            c.append(B[j])
            j += 1

    # 将 A 的剩余元素加入 c
    c.extend(A[i:])

    # 将 B 的剩余元素加入 c
    c.extend(B[j:])

    return len(c), c

# 示例
A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

length, c = merge(A, B)
print(c)
```

##### 2.经典案例：

###### 1.区间合并

给出⼀堆区间，要求合并所有有交集的区间 （端点处相交也算有交集）。最后问合并之后的区间。

![](https://raw.githubusercontent.com/xwk-tomorin/picture/main/20241220170414.png)

```
intervals.sort()
res = []
st, ed = -sys.maxsize, -sys.maxsize
for v in intervals:
	if ed == -sys.maxsize:
		st, ed = v[0], v[1]
	elif v[0] <= ed:
		ed = max(v[1], ed)
	elif v[0] > ed:
		res.append([st, ed])
		st, ed = v[0], v[1]
if ed != -sys.maxsize:
	res.append([st, ed])
	return res
```

###### 2.选择不相交区间

给出⼀堆区间，要求选择尽量多的区间，使得这些区间互不相交，求可选取的区间的最⼤数量。这⾥端点相同也算有重复。

![](https://raw.githubusercontent.com/xwk-tomorin/picture/main/20241220170932.png)

```
intervals.sort(key=lambda x: x[1])
res = 0
ed = -sys.maxsize
for v in intervals:
	if ed < v[0]:
		res += 1
		ed = v[1]
print(res)
```

###### 3.区间选点问题

给出⼀堆区间，取尽量少的点，使得每个区间内⾄少有⼀个点（不同区间内含的点可以是同⼀个，位于区间端点上的点也算作区间内）。

![](https://raw.githubusercontent.com/xwk-tomorin/picture/main/20241220171302.png)

###### 4.区间覆盖问题

给出⼀堆区间和⼀个⽬标区间，问最少选择多少区间可以覆盖掉题中给出的这段⽬标区间。

![](https://raw.githubusercontent.com/xwk-tomorin/picture/main/20241220172310.png)

```
cnt=0
st=0
ed=time
clips.sort()
i=0
while True:
	edm=st
	while i<len(clips) and clips[i][0]<=st:
		edm=max(edm,clips[i][1])
		i=i+1
	if edm==st:
		return -1
	st=edm
	cnt+=1
	if st>=ed:
		return cnt

```

###### 5.区间分组问题

给出⼀堆区间，问最少可以将这些区间分成多少组使得每个组内的区间互不相交。

![](https://raw.githubusercontent.com/xwk-tomorin/picture/main/20241220174706.png)

```
import heapq
l=[[1, 5], [2, 7], [4, 5]]
q=[]
for st,ed in l:
    if not q or st<q[0]:
        heapq.heappush(q,ed) # 一个区间的起始点低于最早结束的区间，因此应该多开一个序列
    else:
        heapq.heappop(q) # 对同一个序列做坐标更替
        heapq.heappush(q,ed)
print(len(q))
```

###### 6.最长下降子序列

```
from bisect import bisect_right
def min_testers_needed(scores):
	scores.reverse() # 反转序列以找到最⻓下降⼦序列的⻓度
	lis = [] # ⽤于存储最⻓上升⼦序列
	for score in scores:
		pos = bisect_right(lis, score)
	if pos < len(lis):
		lis[pos] = score
	else:
		lis.append(score)
	return len(lis)
N = int(input())
scores = list(map(int, input().split()))
result = min_testers_needed(scores)
print(result)
```

附dp解法：O(n^2)

```
n = int(input())
*b, = map(int, input().split())
dp = [1]*n
for i in range(1, n):
	for j in range(i):
		if b[j] < b[i]:
			dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
```



#### 四、递归：

递归是⼀种解决问题的⽅法，它涉及将⼀个问题分解成越来越⼩的⼦问题，直到得到⼀个⾜够⼩的问题，可
以轻易地解决。递归涉及到⼀个函数调⽤⾃身。虽然表⾯上看起来可能没什么特别之处，但递归使我们能够
编写出优雅的解决⽅案，来解决那些可能⾮常难以编程的问题。

##### 1.递归三法则

###### 1.递归算法必须有⼀个基准情形

###### 2.递归算法必须改变其状态并朝着基准情形前进。

###### 3.递归算法必须调⽤⾃身，即进⾏递归调⽤。

##### 2.典中典

进制换算

```
def to_str(n, base):
    # 定义用于转换的字符序列
    convert_string = "0123456789ABCDEF"

    # 基准情形：如果 n 小于基数，则直接返回对应的字符
    if n < base:
        return convert_string[n]
    else:
        # 递归调用：先处理商，再处理余数
        # 通过延迟连接操作，确保结果的顺序是正确的
        return to_str(n // base, base) + convert_string[n % base]


# 示例
print(to_str(10, 2))  # 输出: "1010"
print(to_str(255, 16))  # 输出: "FF"
```

###### 1.八皇后

```
ans = []
def queen_dfs(A, cur=0): #考虑放第cur⾏的皇后
	if cur == len(A): #如果已经放了n个皇后，⼀组新的解产⽣了
		ans.append(''.join([str(x+1) for x in A])) #注意避免浅拷⻉
		return
	for col in range(len(A)): #将当前皇后逐⼀放置在不同的列，每列对应⼀组解
		for row in range(cur): #逐⼀判定，与前⾯的皇后是否冲突
			#因为预先确定所有皇后⼀定不在同⼀⾏，所以只需要检查是否同列，或者在同⼀斜线上
			if A[row] == col or abs(col - A[row]) == cur - row:
				break
			else: #若都不冲突
				A[cur] = col #放置新皇后，在cur⾏，col列
				queen_dfs(A, cur+1) #对下⼀个皇后位置进⾏递归
queen_dfs([None]*8)
for _ in range(int(input())):
print(ans[int(input()) - 1])
```

###### 2.全排列

```
hashTable = [False] * maxn # 当整数i已经在数组 P中时为 true
#@recviz
def increasing_permutaions(n, prefix=[]):
	if len(prefix) == n: # 递归边界，已经处理完排列的1~位
		return [prefix]
	result = []
	for i in range(1, n + 1):
		if hashTable[i]:
			continue
		hashTable[i] = True # 记i已在prefix中
		# 把i加⼊当前排列，处理排列的后续号位
		result += increasing_permutaions(n, prefix + [i])
		hashTable[i] = False # 处理完为i的⼦问题，还原状态
	return result
n = int(input())
result = increasing_permutaions(n)
for r in result:
print(' '.join(map(str,r)))
```

##### 3.递归程序优化两板斧

###### 1.增加递归深度限制

```
import sys
sys.setrecursionlimit(1 << 30) # 将递归深度限制设置为 2^30
```

###### 2.缓存中间结果

之间建个列表or字典调用或者直接内置函数

缓存中间结果缓存中间结果缓存中间结果

```
from functools import lru_cache
@lru_cache(maxsize=None)
```

#### 五、动态规划(dp)

动态规划(Dynamic Programming，DP)是⼀种⽤来解决⼀类最优化问题的算法思想。简单来说，动态规划将⼀个复杂的问题分解成若⼲个⼦问题，通过综合⼦问题的最优解来得到原问题的最优解。需要注意的是，动态规划会将每个求解过的⼦问题的解记录下来，这样当下⼀次碰到同样的⼦问题时，就可以直接使⽤之前记录的结果，⽽不是重复计算。⼀般可以使⽤递归或者递推的写法来实现动态规划，其中递归写法在此处⼜称作记忆化搜索。

如果⼀个问题可以被分解为若⼲个⼦问题，且这些⼦问题会重复出现，那么就称这个问题拥有重叠⼦问题动态规划通过记录重叠⼦问题的解，来使下次碰到相同的⼦问题时直接使⽤之前记录的结果以此避免⼤量重复计算。因此，⼀个问题必须拥有重叠⼦问题，才能使⽤动态规划去解决。

如果⼀个问题的最优解可以由其⼦问题的最优解有效地构造出来，那么称这个问题拥有最优⼦结构。需要指出，⼀个问题必须拥有重叠⼦问题和最优⼦结构，才能使⽤动态规划去解决。

dp是由状态转移⽅程和底端结果而得到的，事实上，如何设计状态和状态转移⽅程，才是动态规划的核⼼，⽽它们也是动态规划最难的地⽅。

##### 1.最大连续子序列和

dp方法

```
n = int(input())
*a, = map(int, input().split())
dp = [0]*n
dp[0] = a[0]
for i in range(1, n):
	dp[i] = max(dp[i-1]+a[i], a[i])
print(max(dp))
```

Kadane's 算法

```
def max_subarray_sum(arr):
	if not arr:
		return 0
	max_current = max_global = arr[0]
	for num in arr[1:]:
		max_current = max(num, max_current + num)
		if max_current > max_global:
			max_global = max_current
	return max_global
# 测试⽤例
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("最⼤⼦数组和为:", max_subarray_sum(arr)) # 输出: 最⼤⼦数组和为: 6
```

变体（土豪购物）双dp

```
a=list(map(int,input().split(",")))
n=len(a)
dp1,dp2=a[0],a[0]
ans=0
for i in range(1,n):
    dp1,dp2=max(a[i],dp1+a[i]),max(dp1,dp2+a[i])
    ans=max(ans,dp2)
print(ans)
```

##### 2.背包

###### 1.0-1背包

n个物品，b容量，价值p，重量w

```
n,b=map(int,input().split())
p=list(map(int,input().split()))
w=list(map(int,input().split()))
dp=[0]*(b+1)
for i in range(n):
    for j in range(b,w[i]-1,-1):
        dp[j]=max(dp[j],dp[j-w[i]]+p[i])
print(dp[-1])
```

枚举顺序不可以错，要不然视为多次放入

###### 2.完全背包

只需修改遍历顺序

```
n,b=map(int,input().split())
p=list(map(int,input().split()))
w=list(map(int,input().split()))
dp=[0]*(b+1)
for i in range(n):
 ***for j in range(w[i]，b+1):***##(从小容量到大容量遍历，即可装多个物品)
        dp[j]=max(dp[j],dp[j-w[i]]+p[i])
print(dp[-1])
```

对于可以多次放入则正常枚举

###### 3.必须填满完全背包(剪丝带)

只需修改初始dp数值（只有剩0容量为0，剩下都是-float('inf')）

```
n,a,b,c=map(int,input().split())
***dp=[0]+[-float('inf')]*n***##(必须一点不剩才有真值)
for i in (a,b,c):
    for j in range(i,n+1):
        dp[j]=max(dp[j],dp[j-i]+1)
print(dp[-1])
```

###### 4.多重背包(每个物品有上限)

最简单的思路是将多个同样的物品看成多个不同的物品，从⽽化为0-1背包。稍作优化：可以改善拆分⽅式，譬如将m个1拆成x_1,x_2,……,x_t个1，只需要这些x_i中取若⼲个的和能组合出1⾄m即可。最⾼效的拆分⽅式是尽可能拆成2的幂，也就是所谓“⼆进制优化”

```
多重背包问题 (二进制优化)
多重背包问题通常可转化成01背包问题求解。但若将每种物品的数量拆分成多个1的话，时间复杂度会很高，
从而导致TLE。所以，需要利用二进制优化思想。即:一个正整数n，可以被分解成1,2,4,...,2^(k-1),
n-2^k+1的形式。其中，k是满足n-2^k+1>0的最大整数。
例如，假设给定价值为2，数量为10的物品，依据二进制优化思想可将10分解为1+2+4+3，则原来价值为2,
数量为10的物品可等效转化为价值分别为1*2，2*2，4*2，3*2，即价值分别为2，4，8，6，数量均为1的物品。

def sum_2(x):
    s = 0
    while x > 0:
        s += (x & 1)
        x = x >> 1
    return s

'''
import math

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    ls = list(map(int, input().split()))
    w = (1 << (m + 1)) - 1                  #e.g., m=10, w=2047
    result = 1
    for i in range(n):
        number = ls[i+n] + 1                # e.g., number = 10
        limit = int(math.log(number, 2))    # limit = 3
        rest = number - (1 << limit)        # rest = 3
        for j in range(limit):
            result = (result | (result << (ls[i] * (1 << j)))) & w
        if rest > 0:
            result = (result | (result << (ls[i] * rest))) & w
    #print(sum_2(result) - 1)
    print(bin(result).count('1') - 1)
```

##### 5.最长公共子序列

其中i,j是两个字符串取到i, j相同的位数

```
while True:
    try:
        a, b = input().split()
    except EOFError:
        break
    
    alen = len(a)
    blen = len(b)
    
    dp = [[0]*(blen+1) for i in range(alen+1)]

    for i in range(1, alen+1):
        for j in range(1, blen+1):
            if a[i-1]==b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])


    print(dp[alen][blen])
```

#### 六、搜索(dfs，bfs)

##### 1、dfs

从起点开始前进，当碰到岔道⼝时，总是选择其中⼀条岔路前进(例如图中总是先选择最右⼿边的岔
路)，在岔路上如果⼜遇到新的岔道⼝，仍然选择新岔道⼝的其中⼀条岔路前进，直到碰到死胡同才回退到最近的岔道⼝选择另⼀条岔路。也就是说，当碰到岔道⼝时，总是以“深度”作为前进的关键词，不碰到死胡同就不回头，因此把这种搜索的⽅式称为深度优先搜索(Depth First Search，DFS)。

从迷宫的例⼦还应该注意到，深度优先搜索会⾛遍所有路径，并且每次⾛到死胡同就代表⼀条完整路径的形成。这就是说，深度优先搜索是⼀种枚举所有完整路径以遍历所有情况的搜索⽅法。

###### 1、数个数（数湖）

使用deque使得弹入弹出都是O(1)

```
from collections import deque
n,m=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
d=[(0,1),(0,-1),(1,0),(-1,0)]
cnt=0
inq=set()
def bfs(x,y):
    q=deque([])
    q.append([x,y])
    inq.add((x,y))
    while q:
        x,y=q.popleft()
        for i,j in d:
            nx=x+i
            ny=y+j
            if 0<=nx<n and 0<=ny<m and l[nx][ny]==1 and (nx,ny) not in inq:
                q.append([nx,ny])
                inq.add((nx,ny))

for i in range(n):
    for j in range(m):
        if l[i][j]==1 and (i,j) not in inq:
            bfs(i,j)
            cnt+=1
print(cnt)
```

###### 2.迷宫最短路径

使用heapq以得到最短路径

```
import heapq
d=[(0,-1),(0,1),(1,0),(-1,0)]
n,m=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
q=[]
heapq.heappush(q,(0,0,0))
inq=set()
inq.add((0,0))
while q:
    s,x,y=heapq.heappop(q)
    if (x,y)==(n-1,m-1):
        print(s)
        break
    for i,j in d:
        nx,ny=x+i,y+j
        if 0<=nx<n and 0<=ny<m and l[nx][ny]!=1 and (nx,ny) not in inq:
            inq.add((nx,ny))
            heapq.heappush(q,(s+1,nx,ny))
else:
    print(-1)
```

###### 3.最短路径Dijkstra

以走山路为例

此算法即使用一个二维数组储存到达某处的最小用力，将判断是否到达变为判断是否用了更小的力，以找到到达终点所需最小力。

```
import heapq
n,m,p=map(int,input().split())
l=[list(input().split()) for i in range(n)]
d=[(0,1),(0,-1),(1,0),(-1,0)]
for _ in range(p):
    x1,y1,x2,y2=map(int,input().split())
    if l[x1][y1]=='#' or l[x2][y2]=='#':
        print("NO")
        continue
    q=[]
    force=[[float('inf') for i in range(m)] for j in range(n)]
    heapq.heappush(q,(0,x1,y1))
    force[x1][y1]=0
    while q:
        f,x,y=heapq.heappop(q)
        if (x,y)==(x2,y2):
            print(f)
            break
        for i,j in d:
            nx,ny=x+i,y+j
            if 0<=nx<n and 0<=ny<m and l[nx][ny]!='#':

                if  f+abs(int(l[x][y])-int(l[nx][ny]))<force[nx][ny]:
                    force[nx][ny]=f+abs(int(l[x][y])-int(l[nx][ny]))
                    heapq.heappush(q,(force[nx][ny],nx,ny))

    else:
        print('NO')
```

##### 补充 bfs模板

```
from collections import deque
  
def bfs(start, end):    
    q = deque([(0, start)])  # (step, start)
    in_queue = {start}


    while q:
        step, front = q.popleft() # 取出队首元素
        if front == end:
            return step # 返回需要的结果，如：步长、路径等信息

        # 将 front 的下一层结点中未曾入队的结点全部入队q，并加入集合in_queue设置为已入队
```

#### 七、特殊技巧

##### 1.滑动窗口

滑动窗⼝是⼀个队列，⽐如例题中的 abcabcbb，进⼊这个队列（窗⼝）为 abc 满⾜题⽬要求，当再进⼊ a，队列变成了 abca，这时候不满⾜要求。所以，我们要移动这个队列！如何移动？我们只要把队列的左边的元素移出就⾏了，直到满⾜题⽬要求！⼀直维持这样的队列，找出队列出现最⻓的⻓度时候！时间复杂度：O(n)

```
d={}
ma=0
start=0
for i,ele in enumerate(s):
	if ele in d and d[ele]>=start:
		start=d[ele]+1
	d[ele]=i
	ma=max(ma,i-start+1)
return ma
```



##### 2.并查集

⽤于存储⾮重叠或不相交⼦集元素的数据结构被称为不相交集合数据结构（disjoint set data structure）。不相交集合数据结构⽀持以下操作：
1.向不相交集合中添加新的集合。
2.使⽤并（Union）操作将不相交集合合并为⼀个单⼀的不相交集合。
3.使⽤查找（Find）操作找到不相交集合的代表元素。

4.检查两个集合是否不相交。

所使⽤的数据结构：
数组： ⼀个整数数组被称为 Parent[]。如果我们处理的是 N 个元素，那么数组的第 i 个元素代表第 i 个
项。更准确地说，Parent[] 数组的第 i 个元素是第 i 个项的⽗节点。这些关系创建了⼀个或多个虚拟树。

树： 它是⼀个 不相交集合（Disjoint set）。如果两个元素位于同⼀棵树中，则它们属于同⼀个 不相交
集合。每棵树的根节点（或最顶层节点）称为该集合的 代表元（representative）。每个集合总是有⼀
个唯⼀的代表元。⼀个简单的规则来识别代表元是：如果 ‘i’ 是⼀个集合的代表元，则 Parent[i] = i。如
果 i 不是其集合的代表元，则可以通过沿着树向上遍历直到找到代表元来确定它。

我知道有点抽象，上例题：

![](https://raw.githubusercontent.com/xwk-tomorin/picture/main/20241223212759.png)

```
n,m=map(int,input().split())
p=[i for i in range(n+1)]
def find(x):
    if p[x]==x:
        return x
    else:
        p[x]=find(p[x])
        return p[x]
def union(x,y):
    p[find(x)]=find(y)
for _ in range(m):
    x,y=map(int,input().split())
    union(x,y)
se={find(x) for x in range(1,n+1)}
print(len(se))
```

若要给出班级人数则可给出人数数组size，在合并时也将人数合并

```
n,m=map(int,input().split())
p=[i for i in range(n+1)]
size=[1 for i in range(n+1)]
def find(x):
    if p[x]==x:
        return x
    else:
        p[x]=find(p[x])
        return p[x]
def union(x,y):
    x1=find(x)
    y1=find(y)
    if x1!=y1:
        p[x1]=y1
        size[y1]+=size[x1]
for _ in range(m):
    x,y=map(int,input().split())
    union(x,y)
se=[size[x] for x in range(1,n+1) if x==p[x]]
se.sort(reverse=True)
print(len(se))
print(' '.join(map(str,se)))
```



##### 3.单调栈

即人为控制栈内元素单调，找某侧最近⼀个⽐其⼤的值，使⽤单调栈维持栈内元素递减；找某侧最近⼀个⽐其⼩的值使⽤单调栈，维持栈内元素递增 ….

例子：接雨水

在这道题，由于需要找某个位置两侧⽐其⾼的柱⼦（只有两侧有⽐当前位置⾼的柱⼦，当前位置才能接
下⾬⽔），我们可以维持栈内元素的单调递减。

```
stack=[]
water=0
n=len(height)
for i in range(n):
	while stack and height[stack[-1]]<height[i]:
		top=stack.pop()
		if not stack:
			break
		d=i-stack[-1]-1
		h=min(height[stack[-1]],height[i])-height[top]
		water+=d*h
	stack.append(i)
return water

```

滑动窗口最大值（长度为k的滑动窗口，给出每次窗口中最大值）：同样是维护递减双端序列

```
from collections import deque
res=[]
de=deque()
if not nums or k==0:
	return []
if k==1:
	return nums
for i in range(len(nums)):
	if de and de[0]<i-k+1:
		de.popleft()
	while de and nums[de[-1]]<nums[i]:
		de.pop()
	de.append(i)
	if i>=k-1:
		res.append(nums[de[0]])
return res
```

