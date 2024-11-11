# 20241112-Week10 线段树和树状数组

Updated 0018 GMT+8 Nov 12 2023

2024 fall, Complied by Hongfei Yan





> Log:
>
> 2024/11/09 部分内容取自, https://github.com/GMyhf/2023fall-cs101/blob/main/20231031_SegmentTree_BIT.md



通常11月份前两周是各科密集期中考试时间，我们讲点拓展知识，月考/作业相应降低难度，便于同学均衡各科学习时间。



**本周主要内容：**

理解时间复杂度 $O(1)$ 和 $O(n)$ 权衡处理方法，有的题目 $O(n^2)$ 算法超时，需要把时间复杂度降到$O(nLogn)$才能AC。

例如：27018:康托展开，http://cs101.openjudge.cn/practice/27018/

假如有一个数组 $arr[0 ... n-1]$，需要：1）计算前 i 个元素的和。2）修改数组 $arr[i] = x$ 中指定元素的值，其中$0 \leq i \leq n-1$。
一个**简单的解决方案**是运行一个从 0 到 i-1 的循环，并计算元素的和。要更新一个值，只需执行 $arr[i] = x$。前者操作需要 $O(n)$ 时间，后者需要 $O(1)$ 时间。另一个简单的解决方案是创建一个额外的数组，并将前第 i 个元素的和存储在这个新数组的第 i 个索引处。给定范围的求和现在可以在 O(1) 时间内计算，但是更新操作现在需要 $O(n)$ 时间。如果有大量的查询（读）操作，但很少的更新（写）操作，那么这种方法可以很好地工作。

是否可以在 $O(log n)$ 时间内同时执行查询和更新操作? 一个有效的解决方案是使用**线段树 (Segment Tree)** 分别在 $O(Logn)$ 时间内执行这两个操作的。另一种解决方案是**二叉索引树（Fenwick Tree/Binary Indexed Tree）**，它的两种操作时间复杂度也是 $O(Logn)$。与线段树相比，二叉索引树需要更少的空间，更容易实现。



组合数学是对于计数问题的研究，数论就是对于整除性问题的研究，组合与数论是程序中的常见考点。题目背景知识，数学思维。

因为整数除法具有分配律的性质，单项整除可以等价于各项求和最后整除。



# Recap



## R1. 题目

### E07618: 病人排队

sorttings, http://cs101.openjudge.cn/practice/07618/

病人登记看病，编写一个程序，将登记的病人按照以下原则排出看病的先后顺序：

1. 老年人（年龄 >= 60岁）比非老年人优先看病。
2. 老年人按年龄从大到小的顺序看病，年龄相同的按登记的先后顺序排序。
3. 非老年人按登记的先后顺序看病。

**输入**

第1行，输入一个小于100的正整数，表示病人的个数；
后面按照病人登记的先后顺序，每行输入一个病人的信息，包括：一个长度小于10的字符串表示病人的ID（每个病人的ID各不相同且只含数字和字母），一个整数表示病人的年龄，中间用单个空格隔开。

**输出**

按排好的看病顺序输出病人的ID，每行一个。



把老人和年轻人用两个列表储存，如果不确定sort是不是稳定的可以自行编入一个数据然后用sort输出看看顺序会不会变。有一个坑点是b要提前转成int，否则后续排序的时候会按照b的字典序而不是大小来排序。

```python
# Read the number of patients
n = int(input())

# Initialize lists for elderly and non-elderly patients
elderly = []
non_elderly = []

# Read patient information
for _ in range(n):
    patient_id, age = input().split()
    age = int(age)
    if age >= 60:
        elderly.append((patient_id, age))
    else:
        non_elderly.append((patient_id, age))

# Sort elderly patients by age in descending order
elderly.sort(key=lambda x: -x[1])

# Concatenate elderly and non-elderly lists
sorted_patients = elderly + non_elderly

# Print the sorted patient IDs
for patient in sorted_patients:
    print(patient[0])
```

Python 自带的 list.sort() 方法和内置的 sorted() 函数都是使用 Timsort 算法实现的。Timsort 是一种混合排序算法，源自归并排序和插入排序，由 Tim Peters 在 2002 年为 Python 编程语言发明。它是一种稳定的排序算法。

稳定性意味着如果两个元素具有相同的值，它们在排序后的列表中的相对位置不会改变。例如，如果有一个列表，其中包含多个具有相同值的元素，稳定排序会确保这些元素在排序后保持原有的顺序。

Merge sort很重要，有的题目就是在考merge sort。例如：07622:求排列的逆序数，http://cs101.openjudge.cn/practice/07622/



### E23555: 节省存储的矩阵乘法

implementation, matrices, http://cs101.openjudge.cn/practice/23555/

由于矩阵存储非常耗费空间，一个长度n宽度m的矩阵需要花费n*m的存储，因此我们选择用另一种节省空间的方法表示矩阵。一个矩阵X可以表示为三元组的序列，每个三元组代表（行号，列号，元素值），如果元素值是0则我们不存储这个三元组，这样对于0很多的大型矩阵，我们节省了很多存储空间。现在我们有两个用这种方式表示的矩阵X和Y，我们想要计算这两个矩阵的乘积，并且也用三元组形式表达，该如何完成呢。

如果不知道矩阵如何相乘，可以参考：http://cs101.openjudge.cn/practice/18161

**输入**

输入第一行是三个整数n，m1, m2，两个矩阵X，Y的维度都是n*n，m1是矩阵X中的非0元素数，m2是矩阵Y中的非0元素数。
之后是m1行，每行是一个三元组（行号，列号，元素值），代表X矩阵的元素值，注意行列编号都从0开始。
之后是m2行，每行是一个三元组（行号，列号，元素值），代表Y矩阵的元素值，注意行列编号都从0开始。

**输出**

输出是m3行，代表X和Y两个矩阵乘积中的非0元素的数目，按照先行号后列号的方式递增排序。
每行仍然是前述的三元组形式。





> 18161:矩阵运算。http://cs101.openjudge.cn/practice/18161
>
> 矩阵乘法运算必须要前一个<mark>矩阵的列数与后一个矩阵的行数相同</mark>，
> 如m行n列的矩阵A与n行p列的矩阵B相乘，可以得到m行p列的矩阵C，
> 矩阵C的每个元素都由A的对应行中的元素与B的对应列中的元素一一相乘并求和得到，
> 即`C[i][j] = A[i][0]*B[0][j] + A[i][1]*B[1][j] + …… +A[i][n-1]*B[n-1][j]`
>
> (`C[i][j]`表示C矩阵中第i行第j列元素)。
>
> 即，$c_{ij}=\Sigma a_{ik}b_{kj}$

输入放到矩阵里面就好了，在计算乘法之后一旦有值不是0就可以在遍历中直接把位置和值输出。

```python
# 汤伟杰，24信息管理系
n, m1, m2 = map(int, input().split())
a = [[0] * n for _ in range(n)]
b = [[0] * n for _ in range(n)]
for _ in range(m1):
    x, y, v = map(int, input().split())
    a[x][y] = v
for _ in range(m2):
    x, y, v = map(int, input().split())
    b[x][y] = v
c = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        c[i][j] = sum(a[i][k] * b[k][j] for k in range(n))
        if c[i][j] != 0:
            print(i, j, c[i][j])
```



使用字典来存储稀疏矩阵。读取 `m2` 行输入，每行包含三个整数 `i`, `j`, `val`，表示矩阵 `Y` 中第 `i` 行第 `j` 列的元素值为 `val`。注意这里将 `Y` 存储为转置形式，即 `Y[j][i]` 而不是 `Y[i][j]`，这是为了方便后续的矩阵乘法计算。

```python
# 焦玮宸 24数学科学学院
n, m1, m2 = map(int, input().split())
X, Y = [{} for i in range(n)], [{} for i in range(n)]
for _ in range(m1):
    i, j, val = map(int, input().split())
    X[i][j] = val
for _ in range(m2):
    i, j, val = map(int, input().split())
    Y[j][i] = val
for i in range(n):
    for j in range(n):
        res = 0
        for ind in range(n):
            if ind in X[i] and ind in Y[j]:
                res += X[i][ind] * Y[j][ind]
        if res:
            print(i, j, res)
```





### M18182: 打怪兽 

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/

Q神无聊的时候经常打怪兽。现在有一只怪兽血量是b，Q神在一些时刻可以选择一些技能打怪兽，每次释放技能都会让怪兽掉血。
现在给出一些技能t~i~,x~i~，代表这个技能可以在ti时刻使用，并且使得怪兽的血量下降x~i~。这个打怪兽游戏有个限制，每一时刻最多可以使用m个技能（一个技能只能用一次）。如果技能使用得当，那么怪兽会在哪一时刻死掉呢？

**输入**

第一行是数据组数nCases, nCases≤ 100
对于每组数据，第一行是三个整数n,m,b，n代表技能的个数，m代表每一时刻可以使用最多m个技能，b代表怪兽初始的血量。
1≤ n≤ 1000，1≤ m≤ 1000，1≤ b≤ 10^9^
接下来n行，每一行一个技能t~i~,x~i~，1≤ t~i~≤ 10^9^，1≤ x~i~≤ 10^9^

**输出**

对于每组数据，输出怪兽在哪一时刻死掉，血量小于等于0就算挂，如果不能杀死怪兽，输出alive





用了字典，注意字典本身无序，只能对 keys 或 values 排序。

用defaultdict，就不用判断key是否在字典中了。defaultdict会自动为这个键创建一个默认值。

```python
from collections import defaultdict

cases = int(input())

for _ in range(cases):
    situation = "alive"
    n, m, b = map(int, input().split())
    a = defaultdict(list)
    
    # Input coordinates
    for _ in range(n):
        x, y = map(int, input().split())
        a[x].append(y)
        
    # Process coordinates
    for x in sorted(a):
        if m >= len(a[x]):
            b -= sum(a[x])
        else:
            a[x].sort(reverse=True)
            b -= sum(a[x][:m])
        if b <= 0:
            situation = x
            break
    
    print(situation)
```



如果 `m` 比较大的话，`heapq.nlargest` 可能会比较慢。可以考虑在收集数据时直接维护一个大小为 `m` 的堆。

```python
# 韩博文，24城市与环境学院
from collections import defaultdict
import heapq

for _ in range(int(input())):
    n, m, b = map(int, input().split())
    d = defaultdict(list)

    # Collect all the damage values for each time point
    for _ in range(n):
        t, x = map(int, input().split())
        d[t].append(x)

    # Calculate the total damage for each time point using a heap
    for t in d:
        if len(d[t]) > m:
            d[t] = sum(heapq.nlargest(m, d[t]))
        else:
            d[t] = sum(d[t])

    # Sort the time points by their occurrence
    dp = sorted(d.items())

    # Apply the damage and check if the blood is depleted
    for t, damage in dp:
        b -= damage
        if b <= 0:
            print(t)
            break
    else:
        print('alive')
```

在收集数据时直接维护一个大小为 `m` 的堆，这样可以减少后续的计算开销。如果堆的大小已经达到 `m`，则使用 `heapq.heappushpop` 将新值加入堆，并弹出最小值。这样可以确保堆中始终保留最大的 `m` 个值。

```python
# 韩博文，24城市与环境学院
from collections import defaultdict
import heapq

for _ in range(int(input())):
    n, m, b = map(int, input().split())
    d = defaultdict(list)

    # Collect all the damage values for each time point and maintain a heap of size m
    for _ in range(n):
        t, x = map(int, input().split())
        if len(d[t]) < m:
            heapq.heappush(d[t], x)
        else:
            heapq.heappushpop(d[t], x)

    # Calculate the total damage for each time point
    for t in d:
        d[t] = sum(d[t])

    # Sort the time points by their occurrence
    dp = sorted(d.items())

    # Apply the damage and check if the blood is depleted
    for t, damage in dp:
        b -= damage
        if b <= 0:
            print(t)
            break
    else:
        print('alive')
```





### M28780: 零钱兑换3

dp, http://cs101.openjudge.cn/practice/28780/

给定一组n种不同面额的硬币，以及要支付的总金额

计算并返回可以凑成总金额所需的 **最少的硬币个数** 。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。

输入

输入为两行

第一行为两个整数n（1 ≤ n ≤ 100），m（0 ≤ m ≤ 10^6），其中n表示硬币的种类数，m表示要凑的总金额

第二行为n个整数，表示硬币的面值

输出

可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，则输出 -1。

样例输入

```
sample1 input:
3 11
1 2 4

sample1 output:
4
```

样例输出

```
sample2 input:
1 3
2

sample2 output:
-1
```

提示

dp

来源

2024 TA-Lhw



完全背包，类似于剪彩 189A. Cut Ribbon，https://codeforces.com/problemset/problem/189/A



时间：16875ms

```python
n, m = map(int, input().split())
coins = list(map(int, input().split()))
dp = [float("inf")] * (m + 1)
dp[0] = 1
for i in coins:
    dp[i] = 1
for i in range(1, m + 1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i - coin] + 1)

#print(dp)
if dp[m] == float("inf"):
    print(-1)
else:
    print(dp[m])
```



```python
from math import inf
n, m = map(int, input().split())
coins = list(map(int, input().split()))
dp = [0] + [inf for _ in range(m)]
for i in range(n):
    for j in range(coins[i], m + 1):
        dp[j] = min(dp[j], dp[j - coins[i]] + 1)
print(dp[m] if dp[m] != inf else -1)
```



时间：5210ms

```python
# 2400010989	韩宇宸 工学院
import bisect

# 读取输入
n, m = map(int, input().split())
face = sorted(map(int, input().split()))  # 直接排序后使用
coins = [float('inf')] * (m + 1)
coins[0] = 0  # 初始值

# 动态规划计算最小硬币数
for i in range(1, m + 1):
    w = bisect.bisect_right(face, i)

    #for k in range(w):
    #    coins[i] = min(coins[i], coins[i - face[k]] + 1)
    if w != 0:
        coins[i] = min(coins[i - face[k]] for k in range(w)) + 1

# 输出结果
print(coins[m] if coins[m] != float('inf') else -1)
```



### T12757: 阿尔法星人翻译官

implementation, http://cs101.openjudge.cn/practice/12757

阿尔法星人为了了解地球人，需要将地球上所有的语言转换为他们自己的语言，其中一个小模块是要将地球上英文表达的数字转换为阿尔法星人也理解的阿拉伯数字。 请你为外星人设计这个模块，即给定一个用英文表示的整数，将其转换成用阿拉伯数字表示的整数。这些数的范围从－999,999,999到＋999,999,999。 下列单词是你的程序中将遇到的所有有关数目的英文单词：

negative, zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety, hundred, thousand, million

**输入**

输入一行，由几个表示数目的英文单词组成(长度不超多200)。注意：负号将由单词negative表示。
当数的大小超过千时，并不用完全单词hundred表示。例如1600将被写为"one thousand six hundred", 而不是"sixteen hundred"。

**输出**

输出一行，表示答案。



这题就恶心在 hundred 可能在千和百万之前，所以要暂时储存出现的一百，等后边出现千或百万的时候就好处理了。

```python
tokens = [str(i) for i in input().split()]
dic={"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, 
     "seven":7, "eight":8, "nine":9, "ten":10, "eleven":11, "twelve":12, 
     "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16, "seventeen":17, 
     "eighteen":18, "nineteen":19, "twenty":20, "thirty":30, "forty":40, 
     "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90, 
     "hundred":100, "thousand":1000, "million":1000000}

sign = 1
if tokens[0]=="negative":
    sign = -1
    del tokens[0]

total = 0
tmp = 0
for i in tokens:
    if i in ("thousand", "million"):
        total += tmp*dic[i]
        tmp = 0
        continue
    if i == "hundred":
        tmp *= dic[i]
    else:
        tmp += dic[i]
        
print( sign * (total + tmp) )
```

2021fall-cs101，李佳霖。对上面程序解读：可以把hundred，thousand，million 这些看成是计量单位，而其他的具体的数当作系数。由于这道题不需要考虑如one thousand million 而只存在one hundred million 这样的情况，因此可以把thousand 和million 看成是一类。t 作为累计计数单位，对具体的数字进行加和处理。而遇到hundred 时便进行释放，成100 处理；遇到thousand 和million则需要考虑前面是否存在hundred million 这样的情况，并做对应的加和处理。最终输出带有正负号的数字。

2021fall-cs101，龚靖淞。one thousand million就是one billion来着。

2021fall-cs101，侯勇启。思路：用字典实现即可，易知不会出现thousand million 这样的数据，只会存在hundred million 和hundred thousand 数据，从而每次遍历到thousand、million 都可以结算；用cnt 滚动记录阶段值，结算后清零。



递归实现

```python
# 焦玮宸 24数学科学学院
dictionary = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90}
def convert(words):
    if words[0] == "negative":
        return -convert(words[1:])
    if "million" in words:
        ind = words.index("million")
        return convert(words[:ind]) * (10 ** 6) + (convert(words[ind + 1:]) if ind < len(words) - 1 else 0)
    if "thousand" in words:
        ind = words.index("thousand")
        return convert(words[:ind]) * (10 ** 3) + (convert(words[ind + 1:]) if ind < len(words) - 1 else 0)
    if "hundred" in words:
        ind = words.index("hundred")
        return convert(words[:ind]) * (10 ** 2) + (convert(words[ind + 1:]) if ind < len(words) - 1 else 0)
    return sum(list(map(lambda s: dictionary[s], words)))


print(convert(list(input().split())))
```





### T16528: 充实的寒假生活

greedy/dp, cs10117 Final Exam, http://cs101.openjudge.cn/practice/16528/

寒假马上就要到了，龙傲天同学获得了从第0天开始到第60天结束为期61天超长寒假，他想要尽可能丰富自己的寒假生活。
现提供若干个活动的起止时间，请计算龙同学这个寒假至多可以参加多少个活动？注意所参加的活动不能有任何时间上的重叠，在第x天结束的活动和在第x天开始的活动不可同时选择。

**输入**

第一行为整数n，代表接下来输入的活动个数(n < 10000)
紧接着的n行，每一行都有两个整数，第一个整数代表活动的开始时间，第二个整数代表全结束时间

**输出**

输出至多参加的活动个数



区间问题，Greedy。按照结束时间排序，然后看找下一个起始时间不超过结束时间的区间，一直贪心。

```python
n = int(input())
events = [list(map(int, input().split())) for _ in range(n)]
cur, ans = -1, 0
for event in sorted(events, key=lambda x: x[1]):
    if event[0] > cur:
        cur = event[1]; ans += 1
print(ans)
```



数据量过小，可以$O(nm)$dp。这个+1，设置的很巧妙。

```python
# 高景行 24数学科学学院
n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append((x + 1, y + 1))
a = sorted(a, key = lambda _: _[0])
dp = [0] * 65
for i in range(n):
    for j in range(a[i][1], 62):
        dp[j] = max(dp[j], dp[a[i][0] - 1] + 1)
print(dp[61])
```





## R2. 学习总结和收获

> 焦玮宸 数学科学学院。Assignment #7: Nov Mock Exam立冬

复习了一下 dp 的一些基础算法。

额外练习：每⽇选做的所有题，以及 LeetCode 上⼀些题⽬，⽐如 509, 70, 62, 1137, 650, 264, 279, 343, 416, 494, 1049。





# 1 Narayana Pandita’s algorithm & Cantor Expansion

## 示例 01833: 排列

Math, http://cs101.openjudge.cn/practice/01833

大家知道，给出正整数n，则1到n这n个数可以构成n！种排列，把这些排列按照从小到大的顺序（字典顺序）列出，如 n=3 时，列出1 2 3，1 3 2，2 1 3，2 3 1，3 1 2，3 2 1六个排列。

任务描述：
给出某个排列，求出这个排列的下k个排列，如果遇到最后一个排列，则下1排列为第1个排列，即排列1 2 3…n。
比如：n = 3，k=2 给出排列2 3 1，则它的下1个排列为3 1 2，下2个排列为3 2 1，因此答案为3 2 1。

**输入**

第一行是一个正整数m，表示测试数据的个数，下面是m组测试数据，每组测试数据第一行是2个正整数n( 1 <= n < 1024 )和k(1<=k<=64)，第二行有n个正整数，是1，2 … n的一个排列。

**输出**

对于每组输入数据，输出一行，n个数，中间用空格隔开，表示输入排列的下k个排列。

样例输入

```
3
3 1
2 3 1
3 1
3 2 1
10 2	
1 2 3 4 5 6 7 8 9 10
```

样例输出

```
3 1 2
1 2 3
1 2 3 4 5 6 7 9 8 10
```

来源

qinlu@POJ



这三个题目是相同的，tags: two pointers

01833: 排列

http://cs101.openjudge.cn/practice/01833/

02996: 选课

http://cs101.openjudge.cn/practice/02996/

LeetCode31.下一个排列

https://leetcode.cn/problems/next-permutation/





### 1.1 思路一：Narayana Pandita’s algorithm (Next Permutation)

Wikipedia has a nice article on lexicographical order generation. It also describes an algorithm to generate the next permutation.

https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order

Quoting:

The method goes back to Narayana Pandita in 14th century India, and has been rediscovered frequently.

> https://en.wikipedia.org/wiki/Narayana_Pandita_(mathematician)
>
> Narayana's cows sequence
>
> ​	$N_n = N_{n-1} + N_{n-3}$ for n > 2,
>
> with initial values
>
> $N_0 = N_1 = N_2 = 1$.
>
> The first few terms are 1, 1, 1, 2, 3, 4, 6, 9, 13, 19, 28, 41, 60, 88,... (sequence [A000930](https://oeis.org/A000930) in the OEIS). 
>
> The On-Line Encyclopedia of Integer Sequences (OEIS), https://oeis.org/

The following algorithm generates the next permutation lexicographically after a given permutation. It changes the given permutation in-place. 

1. Find the highest index `i` such that `s[i] < s[i+1]`. If no such index exists, the permutation is the last permutation.
2. Find the highest index` j > i` such that `s[j] > s[i]`. Such a `j` must exist, since` i+1` is such an index.
3. Swap `s[i]` with `s[j]`.
4. Reverse the order of all of the elements after index i till the last element.

> 以下算法生成给定排列的下一个字典序排列。该算法会就地修改给定的排列。
>
> 1. 找到最高的索引 `i`，使得 `s[i] < s[i+1]`。如果不存在这样的索引，则该排列已经是最后一个排列。
> 2. 找到最高的索引 `j > i`，使得 `s[j] > s[i]`。这样的 `j` 必然存在，因为 `i+1` 就是一个这样的索引。
> 3. 交换 `s[i]` 和 `s[j]`。
> 4. 反转索引 `i` 之后的所有元素，直到最后一个元素。

即：

1）从后往前找第一组相邻的升序数对，记录左边的位置p。
2）从后往前找第一个比p位置的数大的数，将两个数交换。
3）把p位置后所有数字逆序。

举例：

1.从数列的右边向左寻找连续递增序列, 例如对于：1,3,5,4,2，其中5-4-2即为递增序列。

2.从上述序列中找一个比它前面的数（3）大的最小数（4），并将且交换这两个数。于是1,3,5,4,2->1,4,5,3,2，此时交换后的依然是递增序列。

3.新的递增序列逆序，即：1,4,5,3,2 => 1,4,2,3,5



```python
from typing import List


def nextPermutation(nums: List[int]) -> None:
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        
        nums[i], nums[j] = nums[j], nums[i]
    
    left, right = i + 1, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


# =============================================================================
# n = int(input())
# m = int(input())
# arr = list(map(int, input().split()))
# for k in range(m):
#     nextPermutation(arr)
# print(*arr)
# =============================================================================

m = int(input())
for _ in range(m):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    for _ in range(k):
        nextPermutation(a)

    print(*a)
```



### 1.2 思路二：康托展开

康托展开（Cantor Expansion）来解决问题。康托展开是一种将排列映射到唯一整数的方法，可以用来快速找到某个排列的字典序编号，以及根据编号恢复排列。

```python
# 2022fall-cs101，陈勃宇
# cantor expansion

aa = [1]
c = 1
for i in range(1,1025):
    c = c * i
    aa.append(c)

for _ in range(int(input())):
    n,k = map(int,input().split())
    *cc, = map(int,input().split())
    *bb, = range(1,n + 1)
    
    d = 0
    l = n - 1
    for j in cc:
        d = d + bb.index(j) * aa[l]
        bb.remove(j)
        l -= 1
    
    d += k
    while d >= aa[n]:
        d -= aa[n]
        
    dd = []
    *bb, = range(1,n + 1)
    for p in range(n - 1,-1,-1):
        t = d // aa[p]
        dd.append(bb[t])
        del(bb[t])
        d -= t * aa[p]
    print(*dd)
```



程序中用到了remove，pop操作，gpt提醒是否用OrderedDict能优化。

```
# 计算阶乘
aa = [1]
for i in range(1, n+1):
    aa.append(aa[-1] * i)

# 初始化 bb 和 pos（bb中每个元素的位置）
pos = [0] * (n+1)
bb = list(OrderedDict.fromkeys(range(1, n+1)))
```





## 示例27018: 康托展开

http://cs101.openjudge.cn/practice/27018/

总时间限制: 3000ms 单个测试点时间限制: 2000ms 内存限制: 90112kB
描述
求 1∼N 的一个给定全排列在所有 1∼N 全排列中的排名。结果对 998244353取模。

**输入**
第一行一个正整数 N。

第二行 N 个正整数，表示 1∼N 的一种全排列。
**输出**
一行一个非负整数，表示答案对 998244353 取模的值。
样例输入

```
Sample1 in:
3
2 1 3

Sample1 output:
3
```

样例输出

```
Sample2 in:
4
1 2 4 3

Sample2 output:
2
```

提示: 对于100%数据，$1≤N≤1000000$。
来源: https://www.luogu.com.cn/problem/P5367



思路：容易想到的方法是把所有排列求出来后再进行排序，但事实上有更简单高效的算法来解决这个问题，那就是康托展开。

> **康托展开**是一个全排列到一个自然数的双射，常用于构建特定哈希表时的空间压缩。 康托展开的实质是计算当前排列在所有由小到大全排列中的次序编号，因此是可逆的。即由全排列可得到其次序编号（康托展开），由次序编号可以得到对应的第几个全排列（逆康托展开）。
>
> 康托展开的**表达式为**：
>
> $X＝a_n×(n-1)!＋a_{n-1}×(n-2)!＋…＋a_i×(i-1)!＋…＋a_2×1!＋a_1×0!$
>
> 其中：X 为比当前排列小的全排列个数（X+1即为当前排列的次序编号）；n 表示全排列表达式的字符串长度；$a_i$ 表示原排列表达式中的第 i 位（由右往左数），前面（其右侧） i-1 位数有多少个数的值比它小。

例如求 5 2 3 4 1 在 {1, 2, 3, 4, 5} 生成的排列中的次序可以按如下步骤计算。
从右往左数，i 是5时候，其右侧比5小的数有1、2、3、4这4个数，所以有4×4！。
是2，比2小的数有1一个数，所以有 1×3！。
是3，比3小的数有1一个数，为1×2！。
是4，比4小的数有1一个数，为1×1！。
最后一位数右侧没有比它小的数，为 0×0！＝0。
则 4×4！＋1×3！＋1×2！＋1×1！＝105。
这个 X 只是这个排列之前的排列数，而题目要求这个排列的位置，即 5 2 3 4 1排在第 106 位。

同理，4 3 5 2 1的排列数：3×4!＋2×3!＋2×2!＋1×1!＝89，即 4 3 5 2 1 排在第90位。
因为比4小的数有3个：3、2、1；比3小的数有2个：2、1；比5小的数有2个：2、1；比2小的数有1个：1。

参考代码如下。



```python
MOD = 998244353								# Time Limit Exceeded, 内存7140KB, 时间18924ms
fac = [1]

def cantor_expand(a, n):
    ans = 0
    
    for i in range(1, n + 1):
        count = 0
        for j in range(i + 1, n + 1):
            if a[j] < a[i]:
                count += 1				# 计算有几个比他小的数
        ans = (ans + (count * fac[n - i]) % MOD) % MOD
    return ans + 1

a = [0]
N = int(input())		# 用大写N，因为spyder的debug，执行下一条指令的命令是 n/next。与变量n冲突。

for i in range(1, N + 1):
    fac.append((fac[i - 1] * i) % MOD)		# 整数除法具有分配律

*perm, = map(int, input().split())
a.extend(perm)

print(cantor_expand(a, N))
```



用C++也是超时

```c++
#include<iostream>							// Time Limit Exceeded, 内存960KB, 时间1986ms
using namespace std;

const long long MOD = 998244353;
long long fac[1000005]={1};

int cantor_expand (int a[],int n){
    int i, j, count;
    long long ans = 0 ;

    for(i = 1; i <= n; i ++){
        count = 0;
        for(j = i + 1; j <= n; j ++){
            if(a[j] < a[i]) count ++;						// 计算有几个比它小的数
        }
        ans = (ans + (count * fac[n-i]) % MOD ) % MOD;
    }
    return ans + 1;
}


int a[1000005];

int main()
{
  int N;
  //cin >> N;
  scanf("%d", &N);
  for (int i=1; i<=N; i++){
      fac[i] = (fac[i-1]*i)%MOD;
  }

  for (int i=1; i<=N; i++)
      //cin >> a[i];
      scanf("%d",&a[i]);
  cout << cantor_expand(a,N) << endl;
  return 0;
}
```



### 树状数组或线段树来优化

康托展开用 $O(n^2)$ 算法超时，需要把时间复杂度降到$O(nLogn)$。“计算有几个比他小的数”，时间复杂度由 $O(n)$ 降到 $O(Logn)$。

#### 树状数组（Binary Indexed Tree）

实现树状数组的核心部分，包括了三个重要的操作：lowbit、修改和求和。

1. lowbit函数：`lowbit(x)` 是用来计算 `x` 的二进制表示中最低位的 `1` 所对应的值。它的运算规则是利用位运算 `(x & -x)` 来获取 `x` 的最低位 `1` 所对应的值。例如，`lowbit(6)` 的结果是 `2`，因为 `6` 的二进制表示为 `110`，最低位的 `1` 所对应的值是 `2`。

   > `-x` 是 `x` 的补码表示。
   >
   > 对于正整数 `x`，`-x` 的二进制表示是 `x` 的二进制表示取反后加 1。
   >
   > `6` 的二进制表示为 `110`，取反得到 `001`，加 1 得到 `010`。
   >
   > `-6` 的二进制表示为 `11111111111111111111111111111010`（假设 32 位整数）。
   >
   > `6 & -6` 的结果：
   >
   > `110` 与 `11111111111111111111111111111010` 按位与运算，结果为 `010`，即 `2`。

2. update函数：这个函数用于修改树状数组中某个位置的值。参数 `x` 表示要修改的位置，参数 `y` 表示要增加/减少的值。函数使用一个循环将 `x` 的所有对应位置上的值都加上 `y`。具体的操作是首先将 `x` 位置上的值与 `y` 相加，然后通过 `lowbit` 函数找到 `x` 的下一个需要修改的位置，将该位置上的值也加上 `y`，然后继续找下一个位置，直到修改完所有需要修改的位置为止。这样就完成了数组的修改。

3. getsum函数：这个函数用于求解树状数组中某个范围的前缀和。参数 `x` 表示要求解前缀和的位置。函数使用一个循环将 `x` 的所有对应位置上的值累加起来，然后通过 `lowbit` 函数找到 `x` 的上一个位置（即最后一个需要累加的位置），再将该位置上的值累加起来，然后继续找上一个位置，直到累加完所有需要累加的位置为止。这样就得到了从位置 `1` 到位置 `x` 的前缀和。

这就是树状数组的核心操作，通过使用这三个函数，我们可以实现树状数组的各种功能，如求解区间和、单点修改等。

```python
n, MOD, ans = int(input()), 998244353, 1						# 内存69832KB, 时间2847ms
a, fac = list(map(int, input().split())), [1]

tree = [0] * (n + 1)

def lowbit(x):
    return x & -x

def update(x, y):
    while x <= n:
        tree[x] += y
        x += lowbit(x)

def getsum(x):
    tot = 0
    while x:
        tot += tree[x]
        x -= lowbit(x)
    return tot


for i in range(1, n):
    fac.append(fac[i-1] * i % MOD)

for i in range(1, n + 1):
    cnt = getsum(a[i-1])
    update(a[i-1], 1)
    ans = (ans + ((a[i-1] - 1 - cnt) * fac[n - i]) % MOD) % MOD
    
print(ans)
```



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231029152322373.png" alt="image-20231029152322373" style="zoom:67%;" />



#### 线段树（Segment tree）

线段树 segment tree 来计算第i位右边比该数还要小的数的个数。

```python
n, MOD, ans = int(input()), 998244353, 1					# 内存69900KB, 时间5162ms
a, fac = list(map(int, input().split())), [1]

tree = [0] * (2*n)


def build(arr):

    # insert leaf nodes in tree
    for i in range(n):
        tree[n + i] = arr[i]

    # build the tree by calculating parents
    for i in range(n - 1, 0, -1):
        tree[i] = tree[i << 1] + tree[i << 1 | 1]


# function to update a tree node
def updateTreeNode(p, value):

    # set value at position p
    tree[p + n] = value
    p = p + n

    # move upward and update parents
    i = p
    while i > 1:

        tree[i >> 1] = tree[i] + tree[i ^ 1]
        i >>= 1


# function to get sum on interval [l, r)
def query(l, r):

    res = 0

    l += n
    r += n

    while l < r:

        if (l & 1):
            res += tree[l]
            l += 1

        if (r & 1):
            r -= 1
            res += tree[r]

        l >>= 1
        r >>= 1

    return res


#build([0]*n)

for i in range(1, n):
    fac.append(fac[i-1] * i % MOD)

for i in range(1, n + 1):
    cnt = query(0, a[i-1])
    updateTreeNode(a[i-1]-1, 1)
    
    ans = (ans + (a[i-1] -1 - cnt) * fac[n - i]) % MOD
    
print(ans)

```



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231029161854925.png" alt="image-20231029161854925" style="zoom: 50%;" />







# 2 数据结构：线段树和树状数组

线段树（Segment Tree）和树状数组（Binary Indexed Tree）的区别和联系：1）时间复杂度相同, 但是树状数组的常数优于线段树。2）树状数组的作用被线段树完全涵盖, 凡是可以使用树状数组解决的问题, 使用线段树一定可以解决, 但是线段树能够解决的问题树状数组未必能够解决。3）树状数组的代码量比线段树小很多。



Segment Tree and Its Applications

https://www.baeldung.com/cs/segment-trees#:~:text=The%20segment%20tree%20is%20a,structure%20such%20as%20an%20array.

The segment tree is a type of data structure from computational geometry. [Bentley](https://en.wikipedia.org/wiki/Bentley–Ottmann_algorithm) proposed this well-known technique in 1977. A segment tree is essentially a binary tree in whose nodes we store the information about the segments of a linear data structure such as an array.

> 区间树是一种来自计算几何的数据结构。Bentley 在 1977 年提出了这一著名的技术。区间树本质上是一棵二叉树，在其节点中存储了关于线性数据结构（如数组）的区段信息。
>

Fenwick tree

https://en.wikipedia.org/wiki/Fenwick_tree#:~:text=A%20Fenwick%20tree%20or%20binary,in%20an%20array%20of%20values.&text=This%20structure%20was%20proposed%20by,further%20modification%20published%20in%201992.

A **Fenwick tree** or **binary indexed tree** **(BIT)** is a data structure that can efficiently update values and calculate [prefix sums](https://en.wikipedia.org/wiki/Prefix_sum) in an array of values.

This structure was proposed by Boris Ryabko in 1989 with a further modification published in 1992. It has subsequently become known under the name Fenwick tree after Peter Fenwick, who described this structure in his 1994 article.

> Fenwick 树 或 二叉索引树 (BIT) 是一种数据结构，可以高效地更新数组中的值并计算前缀和。
>
> 这种结构由 Boris Ryabko 于 1989 年提出，并在 1992 年进行了进一步的修改。此后，这种结构以其在 1994 年的文章中描述它的 Peter Fenwick 的名字而广为人知，被称为 Fenwick 树。



### Segment tree | Efficient implementation

https://www.geeksforgeeks.org/segment-tree-efficient-implementation/

Let us consider the following problem to understand Segment Trees without recursion.
We have an array $arr[0 . . . n-1]$. We should be able to, 

1. Find the sum of elements from index `l` to `r` where $0 \leq l \leq r \leq n-1$
2. Change the value of a specified element of the array to a new value `x`. We need to do $arr[i] = x$ where $0 \leq i \leq n-1$. 

A **simple solution** is to run a loop from `l` to `r` and calculate the sum of elements in the given range. To update a value, simply do $arr[i] = x$. The first operation takes **O(n)** time and the second operation takes **O(1)** time.

> **简单解决方案** 是从 `l` 到 `r` 运行一个循环，计算给定范围内的元素之和。要更新一个值，只需执行 `arr[i] = x`。第一个操作（查询）的时间复杂度为 **O(n)**，第二个操作（更新）的时间复杂度为 **O(1)**。

**Another solution** is to create another array and store the sum from start to `i` at the ith index in this array. The sum of a given range can now be calculated in O(1) time, but the update operation takes O(n) time now. This works well if the number of query operations is large and there are very few updates.

> **另一种解决方案** 是创建另一个数组，并在该数组的第 `i` 个索引处存储从起始位置到 `i` 的元素之和。现在可以在 O(1) 时间内计算给定范围的和，但更新操作现在需要 O(n) 时间。如果查询操作的数量很大而更新操作很少，这种方法效果很好。

What if the number of queries and updates are equal? Can we perform both the operations in O(log n) time once given the array? We can use a [Segment Tree](https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/) to do both operations in O(logn) time. We have discussed the complete implementation of segment trees in our [previous](https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/) post. In this post, we will discuss the easier and yet efficient implementation of segment trees than in the previous post.

> 但如果查询和更新操作的数量相等呢？我们能否在给定数组的情况下，使两个操作都在 O(log n) 时间内完成？我们可以使用 线段树 来在 O(log n) 时间内完成这两个操作。我们在之前的帖子中详细讨论了线段树的完整实现。在这篇文章中，我们将讨论比之前更简单且高效的线段树实现方法。

Consider the array and segment tree as shown below:  叶子是数组值，非叶是和

![img](https://media.geeksforgeeks.org/wp-content/uploads/excl.png)



You can see from the above image that the original array is at the bottom and is 0-indexed with 16 elements. The tree contains a total of 31 nodes where the leaf nodes or the elements of the original array start from node 16. So, we can easily construct a segment tree for this array using a `2*N` sized array where N is the number of elements in the original array. The leaf nodes will start from index N in this array and will go up to index `(2 * N – 1)`. Therefore, the element at index `i` in the original array will be at index `(i + N)` in the segment tree array. Now to calculate the parents, we will start from the index `(N – 1)` and move upward. For index `i` , the left child will be at `(2 * i)` and the right child will be at `(2*i + 1)` index. So the values at nodes at `(2 * i)` and `(2*i + 1)` are combined at i-th node to construct the tree. 

> 从上图可以看出，原始数组位于底部，是 0 索引的，包含 16 个元素。树总共有 31 个节点，其中叶节点或原始数组的元素从节点 16 开始。因此，我们可以使用一个大小为 2*N 的数组轻松构建这个数组的线段树，其中 N 是原始数组中的元素数量。叶节点将从该数组的索引 N 开始，一直到索引 (2 * N - 1)。因此，原始数组中索引 i 处的元素将在线段树数组中的索引 (i + N) 处。现在，为了计算父节点，我们将从索引 (N - 1) 开始向上移动。对于索引 i，左孩子将位于 (2 * i) 索引处，右孩子将位于 (2 * i + 1) 索引处。因此，节点 (2 * i) 和 (2 * i + 1) 处的值将在 i 索引处组合以构建树。

As you can see in the above figure, we can query in this tree in an interval `[L,R)` with left index (L) included and right (R) excluded.
We will implement all of these multiplication and addition operations using bitwise operators.

> 如上图所示，我们可以在区间 [L, R) 中查询这棵树，其中左索引 L 包含在内，右索引 R 排除在外。
> 我们将使用位运算符实现所有的乘法和加法操作。

Let us have a look at the complete implementation: 

```python
# Python3 Code Addition 

# limit for array size 
N = 100000; 

# Max size of tree 
tree = [0] * (2 * N); 

# function to build the tree 
def build(arr) : 

	# insert leaf nodes in tree 
	for i in range(n) : 
		tree[n + i] = arr[i]; 
	
	# build the tree by calculating parents 
	for i in range(n - 1, 0, -1) : 
    # tree[i] = tree[2*i] + tree[2*i+1]
		tree[i] = tree[i << 1] + tree[i << 1 | 1]; 	

# function to update a tree node 
def updateTreeNode(p, value) : 
	
	# set value at position p 
	tree[p + n] = value; 
	p = p + n; 
	
	# move upward and update parents 
	i = p; 
	
	while i > 1 : 
		
		tree[i >> 1] = tree[i] + tree[i ^ 1]; 
		i >>= 1; 

# function to get sum on interval [l, r) 
def query(l, r) : 

	res = 0; 
	
	# loop to find the sum in the range 
	l += n; 
	r += n; 
	
	while l < r : 
	
		if (l & 1) : 
			res += tree[l]; 
			l += 1
	
		if (r & 1) : 
			r -= 1; 
			res += tree[r]; 
			
		l >>= 1; 
		r >>= 1
	
	return res; 

if __name__ == "__main__" : 

	a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]; 

	n = len(a); 
	
	build(a); 
	
	# print the sum in range(1,2) index-based 
	print(query(1, 3)); 
	
	# modify element at 2nd index 
	updateTreeNode(2, 1); 
	
	# print the sum in range(1,2) index-based 
	print(query(1, 3)); 

```



**Output:** 

```
5
3
```

Yes! That is all. The complete implementation of the segment tree includes the query and update functions. Let us now understand how each of the functions works: 


1. The picture makes it clear that the leaf nodes are stored at i+n, so we can clearly insert all leaf nodes directly. 

   > 图片清楚地表明叶节点存储在i+n的位置，因此我们可以直接明确地插入所有叶节点。

2. The next step is to build the tree and it takes O(n) time. The parent always has its less index than its children, so we just process all the nodes in decreasing order, calculating the value of the parent node. If the code inside the build function to calculate parents seems confusing, then you can see this code. It is equivalent to that inside the build function. 

   > 下一步是构建树，这需要O(n)的时间。父节点的索引总是小于其子节点的索引，所以我们只需按递减顺序处理所有节点，计算父节点的值。如果构建函数中用于计算父节点的代码看起来令人困惑，那么你可以参考这段代码。它与构建函数内部的代码等效。

   `tree[i] = tree[2*i] + tree[2*i+1]`

 

3. Updating a value at any position is also simple and the time taken will be proportional to the height （“高度”这个概念，其实就是从下往上度量，树这种数据结构的高度是从最底层开始计数，并且计数的起点是0） of the tree. We only update values in the parents of the given node which is being changed. So to get the parent, we just go up to the parent node, which is `p/2` or `p>>1`, for node `p`. `p^1` turns `(2*i`) to `(2*i + 1)` and vice versa to get the second child of p.

   > 在任意位置更新一个值也非常简单，所需时间将与树的高度成正比。我们只更新给定节点（即正在更改的节点）的父节点中的值。为了得到父节点，我们只需向上移动到节点p的父节点，该父节点为p/2或p>>1。p^1将`(2*i)`转换为`(2*i + 1)`反之亦然，以获得p的第二个子节点。

4. Computing the sum also works in $O(Logn)$ time. If we work through an interval of [3,11), we need to calculate only for nodes 19,26,12, and 5 in that order.  要演示这个索引上行的求和过程，前面程序数组是12个元素，图示是16个元素，需要稍作修改。增加了print输出，便于调试。



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/202310312148391.png" alt="image-20231031214814445" style="zoom:50%;" />



The idea behind the query function is whether we should include an element in the sum or whether we should include its parent. Let’s look at the image once again for proper understanding. 

![img](https://media.geeksforgeeks.org/wp-content/uploads/excl.png)

Consider that `L` is the left border of an interval and `R` is the right border of the interval `[L,R)`. It is clear from the image that if `L` is odd, then it means that it is the right child of its parent and our interval includes only `L` and not the parent. So we will simply include this node to sum and move to the parent of its next node by doing `L = (L+1)/2`. Now, if L is even, then it is the left child of its parent and the interval includes its parent also unless the right borders interfere. Similar conditions are applied to the right border also for faster computation. We will stop this iteration once the left and right borders meet.

> 假设`L`是一个区间的左边界，而`R`是区间`[L,R)`的右边界。从图中可以明显看出，如果`L`是奇数，这意味着它是其父节点的右孩子，并且我们的区间仅包含`L`而不包括其父节点。因此，我们将简单地把这个节点加到总和中，并通过执行`L = (L+1)/2`移动到下一个节点的父节点。现在，如果`L`是偶数，那么它是其父节点的左孩子，除非右边界干涉，否则区间也包括其父节点。对于右边界也有类似的条件，以便更快地计算。一旦左右边界相遇，我们就会停止这次迭代。

The theoretical time complexities of both previous implementation and this implementation is the same, but practically, it is found to be much more efficient as there are no recursive calls. We simply iterate over the elements that we need. Also, this is very easy to implement.

> 这两种实现的理论时间复杂度是相同的，但在实际应用中，后者被发现要高效得多，因为没有递归调用。我们只是迭代我们需要的元素。此外，这种方法非常容易实现。

**Time Complexities:**

- Tree Construction: O( n )
- Query in Range: O( Log n )
- Updating an element: O( Log n ).

**Auxiliary Space:** O(2*N)



#### 1364A: A. XXXXX

brute force/data structures/number theory/two pointers, 1200, https://codeforces.com/problemset/problem/1364/A

Ehab loves number theory, but for some reason he hates the number 𝑥. Given an array 𝑎, find the length of its longest subarray such that the sum of its elements **isn't** divisible by 𝑥, or determine that such subarray doesn't exist.

An array 𝑎 is a subarray of an array 𝑏 if 𝑎 can be obtained from 𝑏 by deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.

**Input**

The first line contains an integer 𝑡 (1≤𝑡≤5) — the number of test cases you need to solve. The description of the test cases follows.

The first line of each test case contains 2 integers 𝑛 and 𝑥 (1≤𝑛≤10^5^, 1≤𝑥≤10^4^) — the number of elements in the array 𝑎 and the number that Ehab hates.

The second line contains 𝑛 space-separated integers $𝑎_1, 𝑎_2, ……, 𝑎_𝑛 (0≤𝑎_𝑖≤10^4)$ — the elements of the array 𝑎.

**Output**

For each testcase, print the length of the longest subarray whose sum isn't divisible by 𝑥. If there's no such subarray, print −1.

Example

input

```
3
3 3
1 2 3
3 4
1 2 3
2 2
0 6
```

output

```
2
3
-1
```

Note

In the first test case, the subarray \[2,3\] has sum of elements 5, which isn't divisible by 3.

In the second test case, the sum of elements of the whole array is 6, which isn't divisible by 4.

In the third test case, all subarrays have an even sum, so the answer is −1.



Pypy3 可以AC。使用tree segment，时间复杂度是O(n*logn)

```python
# CF 1364A
 
# def prefix_sum(nums):
#     prefix = []
#     total = 0
#     for num in nums:
#         total += num
#         prefix.append(total)
#     return prefix
 
# def suffix_sum(nums):
#     suffix = []
#     total = 0
#     # 首先将列表反转
#     reversed_nums = nums[::-1]
#     for num in reversed_nums:
#         total += num
#         suffix.append(total)
#     # 将结果反转回来
#     suffix.reverse()
#     return suffix
 
 
t = int(input())
ans = []
for _ in range(t):
    n, x = map(int, input().split())
    a = [int(i) for i in input().split()]


# Segment tree | Efficient implementation
# https://www.geeksforgeeks.org/segment-tree-efficient-implementation/

    # Max size of tree 
    tree = [0] * (2 * n); 

    def build(arr) : 

        # insert leaf nodes in tree 
        for i in range(n) : 
            tree[n + i] = arr[i]; 
        
        # build the tree by calculating parents 
        for i in range(n - 1, 0, -1) : 
            tree[i] = tree[i << 1] + tree[i << 1 | 1]; 

    # function to update a tree node 
    def updateTreeNode(p, value) : 
        
        # set value at position p 
        tree[p + n] = value; 
        p = p + n; 
        
        # move upward and update parents 
        i = p; 
        
        while i > 1 : 
            
            tree[i >> 1] = tree[i] + tree[i ^ 1]; 
            i >>= 1; 

    # function to get sum on interval [l, r) 
    def query(l, r) : 

        res = 0; 
        
        # loop to find the sum in the range 
        l += n; 
        r += n; 
        
        while l < r : 
        
            if (l & 1) : 
                res += tree[l]; 
                l += 1
        
            if (r & 1) : 
                r -= 1; 
                res += tree[r]; 
                
            l >>= 1; 
            r >>= 1
        
        return res; 
    #aprefix_sum = prefix_sum(a)
    #asuffix_sum = suffix_sum(a)
 
    build([i%x for i in a]);
    
    left = 0
    right = n - 1
    if right == 0:
        if a[0] % x !=0:
            print(1)
        else:
            print(-1)
        continue
 
    leftmax = 0
    rightmax = 0
    while left != right:
        #total = asuffix_sum[left]
        total = query(left, right+1)
        if total % x != 0:
            leftmax = right - left + 1
            break
        else:
            left += 1
 
    left = 0
    right = n - 1
    while left != right:
        #total = aprefix_sum[right]
        total = query(left, right+1)
        if total % x != 0:
            rightmax = right - left + 1
            break
        else:
            right -= 1
    
    if leftmax == 0 and rightmax == 0:
        #print(-1)
        ans.append(-1)
    else:
        #print(max(leftmax, rightmax))
        ans.append(max(leftmax, rightmax))

print('\n'.join(map(str,ans)))
```



如果用sum求和，O(n^2)，pypy3也会在test3 超时。







#### Benifits of segment tree usage

https://www.geeksforgeeks.org/segment-tree-sum-of-given-range/

- **Range Queries:** One of the main use cases of segment trees is to perform range queries on an array in an efficient manner. The query function in the segment tree can return the ==minimum, maximum, sum, or any other aggregation== of elements within a specified range in the array in O(log n) time.

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231031140857139.png" alt="image-20231031140857139" style="zoom:50%;" />



假设根节点下标从0开始，左子节点 = 2\*父节点+1，右子节点  = 2\*父节点+2

二叉树的父子节点位置关系，https://zhuanlan.zhihu.com/p/339763580

```python
class SegmentTree:
	def __init__(self, array):
		self.size = len(array)
		self.tree = [0] * (4 * self.size)
		self.build_tree(array, 0, 0, self.size - 1)

	def build_tree(self, array, tree_index, left, right):
		if left == right:
			self.tree[tree_index] = array[left]
			return
		mid = (left + right) // 2
		self.build_tree(array, 2 * tree_index + 1, left, mid)
		self.build_tree(array, 2 * tree_index + 2, mid + 1, right)
		self.tree[tree_index] = min(self.tree[2 * tree_index + 1], self.tree[2 * tree_index + 2])

	def query(self, tree_index, left, right, query_left, query_right):
		if query_left <= left and right <= query_right:
			return self.tree[tree_index]
		mid = (left + right) // 2
		min_value = float('inf')
		if query_left <= mid:
			min_value = min(min_value, self.query(2 * tree_index + 1, left, mid, query_left, query_right))
		if query_right > mid:
			min_value = min(min_value, self.query(2 * tree_index + 2, mid + 1, right, query_left, query_right))
		return min_value

	def query_range(self, left, right):
		return self.query(0, 0, self.size - 1, left, right)


if __name__ == '__main__':
	array = [1, 3, 2, 5, 4, 6]
	st = SegmentTree(array)
	print(st.query_range(1, 5)) # 2

```

如果要返回区间最大值，只需要修改第14、20、22、24行程序为求最大相应代码

```python
        #self.tree[tree_index] = min(self.tree[2 * tree_index + 1], self.tree[2 * tree_index + 2])
        self.tree[tree_index] = max(self.tree[2 * tree_index + 1], self.tree[2 * tree_index + 2])
...
				#min_value = float('inf')
        min_value = -float('inf')
        if query_left <= mid:
            #min_value = min(min_value, self.query(2 * tree_index + 1, left, mid, query_left, query_right))
            min_value = max(min_value, self.query(2 * tree_index + 1, left, mid, query_left, query_right))
        if query_right > mid:
            #min_value = min(min_value, self.query(2 * tree_index + 2, mid + 1, right, query_left, query_right))
            min_value = max(min_value, self.query(2 * tree_index + 2, mid + 1, right, query_left, query_right))
        return min_value
   ....
   print(st.query_range(1, 5)) # 6   
      
```

如果要返回区间 求和，只需要修改第14、20、22、24行程序为求和代码。



### 树状数组

树状数组或二叉索引树（英语：Binary Indexed Tree），又以其发明者命名为Fenwick树，最早由Peter M. Fenwick于1994年以A New Data Structure for Cumulative Frequency Tables为题发表。其初衷是解决数据压缩里的累积频率（Cumulative Frequency）的计算问题，现多用于高效计算数列的前缀和， 区间和。



#### Binary Indexed Tree or Fenwick Tree

https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/

Let us consider the following problem to understand Binary Indexed Tree.
We have an array $arr[0 . . . n-1]$. We would like to 
**1** Compute the sum of the first i elements. 
**2** Modify the value of a specified element of the array arr[i] = x where $0 \leq i \leq n-1$.
A **simple solution** is to run a loop from 0 to i-1 and calculate the sum of the elements. To update a value, simply do arr[i] = x. The first operation takes O(n) time and the second operation takes O(1) time. Another simple solution is to create an extra array and store the sum of the first i-th elements at the i-th index in this new array. The sum of a given range can now be calculated in O(1) time, but the update operation takes O(n) time now. This works well if there are a large number of query operations but a very few number of update operations.
**Could we perform both the query and update operations in O(log n) time?** 
One efficient solution is to use [Segment Tree](https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/) that performs both operations in O(Logn) time.
An alternative solution is Binary Indexed Tree, which also achieves O(Logn) time complexity for both operations. Compared with Segment Tree, Binary Indexed Tree requires less space and is easier to implement.

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231031141452788.png" alt="image-20231031141452788" style="zoom:50%;" />



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231031141531597.png" alt="image-20231031141531597" style="zoom:50%;" />



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231031141548736.png" alt="image-20231031141548736" style="zoom:50%;" />

**Representation** 
Binary Indexed Tree is represented as an array. Let the array be BITree[]. Each node of the Binary Indexed Tree stores the sum of some elements of the input array. The size of the Binary Indexed Tree is equal to the size of the input array, denoted as n. In the code below, we use a size of n+1 for ease of implementation.

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231031141831067.png" alt="image-20231031141831067" style="zoom:50%;" />



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231031141629059.png" alt="image-20231031141629059" style="zoom:50%;" />




**Construction** 
We initialize all the values in BITree[] as 0. Then we call update() for all the indexes, the update() operation is discussed below.
**Operations** 


> ***getSum(x): Returns the sum of the sub-array arr[0,…,x]*** 
> // Returns the sum of the sub-array arr[0,…,x] using BITree[0..n], which is constructed from arr[0..n-1] 
>
> 1) Initialize the output sum as 0, the current index as x+1. 
> 2) Do following while the current index is greater than 0. 
>
> …a) Add BITree[index] to sum 
> …b) Go to the parent of BITree[index]. The parent can be obtained by removing 
> the last set bit from the current index, i.e., index = index – (index & (-index)) 
>
> 3) Return sum.

 

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/BITSum.png" alt="BITSum" style="zoom: 67%;" />



getsum(7)

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231031142037881.png" alt="image-20231031142037881" style="zoom:50%;" />

getsum(8)

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231031142146355.png" alt="image-20231031142146355" style="zoom:50%;" />



**整数的二进制表示常用的方式之一是使用补码**

补码是一种表示有符号整数的方法，它将负数的二进制表示转换为正数的二进制表示。补码的优势在于可以使用相同的算术运算规则来处理正数和负数，而不需要特殊的操作。

在补码表示中，最高位用于表示符号位，0表示正数，1表示负数。其他位表示数值部分。

具体将一个整数转换为补码的步骤如下：

1. 如果整数是正数，则补码等于二进制表示本身。
2. 如果整数是负数，则需要先将其绝对值转换为二进制，然后取反，最后加1。

例如，假设要将-5转换为补码：

1. 5的二进制表示为00000101。

2. 将其取反得到11111010。

3. 加1得到11111011，这就是-5的补码表示。

   

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231031142210011.png" alt="image-20231031142210011" style="zoom:50%;" />



The diagram above provides an example of how getSum() is working. Here are some important observations.
BITree[0] is a dummy node. 
BITree[y] is the parent of BITree[x], if and only if y can be obtained by removing the last set bit from the binary representation of x, that is y = x – (x & (-x)).
The child node BITree[x] of the node BITree[y] stores the sum of the elements between y(inclusive) and x(exclusive): arr[y,…,x). 


> ***update(x, val): Updates the Binary Indexed Tree (BIT) by performing arr[index] += val*** 
> // Note that the update(x, val) operation will not change arr[]. It only makes changes to BITree[] 
>
> 1) Initialize the current index as x+1. 
> 2) Do the following while the current index is smaller than or equal to n. 
>
> …a) Add the val to BITree[index] 
> …b) Go to next element of BITree[index]. The next element can be obtained by incrementing the last set bit of the current index, i.e., index = index + (index & (-index))

 

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/BITUpdate12.png" alt="BITUpdate1" style="zoom:67%;" />

update(4, 10)

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231031142428708.png" alt="image-20231031142428708" style="zoom:50%;" />



The update function needs to make sure that all the BITree nodes which contain arr[i] within their ranges being updated. We loop over such nodes in the BITree by repeatedly adding the decimal number corresponding to the last set bit of the current index.
**How does Binary Indexed Tree work?** 
The idea is based on the fact that all positive integers can be represented as the sum of powers of 2. For example 19 can be represented as 16 + 2 + 1. Every node of the BITree stores the sum of n elements where n is a power of 2. For example, in the first diagram above (the diagram for getSum()), the sum of the first 12 elements can be obtained by the sum of the last 4 elements (from 9 to 12) plus the sum of 8 elements (from 1 to 8). The number of set bits in the binary representation of a number n is O(Logn). Therefore, we traverse at-most O(Logn) nodes in both getSum() and update() operations. The time complexity of the construction is O(nLogn) as it calls update() for all n elements. 
**Implementation:** 
Following are the implementations of Binary Indexed Tree.

```python
# Python implementation of Binary Indexed Tree 

# Returns sum of arr[0..index]. This function assumes 
# that the array is preprocessed and partial sums of 
# array elements are stored in BITree[]. 
def getsum(BITTree,i): 
	s = 0 #initialize result 

	# index in BITree[] is 1 more than the index in arr[] 
	i = i+1

	# Traverse ancestors of BITree[index] 
	while i > 0: 

		# Add current element of BITree to sum 
		s += BITTree[i] 

		# Move index to parent node in getSum View 
		i -= i & (-i) 
	return s 

# Updates a node in Binary Index Tree (BITree) at given index 
# in BITree. The given value 'val' is added to BITree[i] and 
# all of its ancestors in tree. 
def updatebit(BITTree , n , i ,v): 

	# index in BITree[] is 1 more than the index in arr[] 
	i += 1

	# Traverse all ancestors and add 'val' 
	while i <= n: 

		# Add 'val' to current node of BI Tree 
		BITTree[i] += v 

		# Update index to that of parent in update View 
		i += i & (-i) 


# Constructs and returns a Binary Indexed Tree for given 
# array of size n. 
def construct(arr, n): 

	# Create and initialize BITree[] as 0 
	BITTree = [0]*(n+1) 

	# Store the actual values in BITree[] using update() 
	for i in range(n): 
		updatebit(BITTree, n, i, arr[i]) 

	# Uncomment below lines to see contents of BITree[] 
	#for i in range(1,n+1): 
	#	 print BITTree[i], 
	return BITTree 


# Driver code to test above methods 
freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9] 
BITTree = construct(freq,len(freq)) 
print("Sum of elements in arr[0..5] is " + str(getsum(BITTree,5))) 
freq[3] += 6
updatebit(BITTree, len(freq), 3, 6) 
print("Sum of elements in arr[0..5]"+
					" after update is " + str(getsum(BITTree,5))) 

# This code is contributed by Raju Varshney 
 
```

**Output**

```
Sum of elements in arr[0..5] is 12
Sum of elements in arr[0..5] after update is 18
```

**Time Complexity:** O(NLogN)
**Auxiliary Space:** O(N)

**Can we extend the Binary Indexed Tree to computing the sum of a range in O(Logn) time?** 
Yes. rangeSum(l, r) = getSum(r) – getSum(l-1).
**Applications:** 
The implementation of the arithmetic coding algorithm. The development of the Binary Indexed Tree was primarily motivated by its application in this case. See [this ](http://en.wikipedia.org/wiki/Fenwick_tree#Applications)for more details.
**Example Problems:** 
[Count inversions in an array | Set 3 (Using BIT)](https://www.geeksforgeeks.org/count-inversions-array-set-3-using-bit/) 
[Two Dimensional Binary Indexed Tree or Fenwick Tree](https://www.geeksforgeeks.org/two-dimensional-binary-indexed-tree-or-fenwick-tree/) 
[Counting Triangles in a Rectangular space using BIT](https://www.geeksforgeeks.org/counting-triangles-in-a-rectangular-space-using-2d-bit/)

**References:** 
http://en.wikipedia.org/wiki/Fenwick_tree 
http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=binaryIndexedTrees



[力扣307] 线段树&树状数组，https://zhuanlan.zhihu.com/p/126539401



#### 307.区域和检索 - 数组可修改

https://leetcode.cn/problems/range-sum-query-mutable/

给你一个数组 `nums` ，请你完成两类查询。

1. 其中一类查询要求 **更新** 数组 `nums` 下标对应的值
2. 另一类查询要求返回数组 `nums` 中索引 `left` 和索引 `right` 之间（ **包含** ）的nums元素的 **和** ，其中 `left <= right`

实现 `NumArray` 类：

- `NumArray(int[] nums)` 用整数数组 `nums` 初始化对象
- `void update(int index, int val)` 将 `nums[index]` 的值 **更新** 为 `val`
- `int sumRange(int left, int right)` 返回数组 `nums` 中索引 `left` 和索引 `right` 之间（ **包含** ）的nums元素的 **和** （即，`nums[left] + nums[left + 1], ..., nums[right]`）

 

**示例 1：**

```
输入：
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
输出：
[null, 9, null, 8]

解释：
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // 返回 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1,2,5]
numArray.sumRange(0, 2); // 返回 1 + 2 + 5 = 8
```



# 3 康托展开逆运算(cantor 2)

给出一个数N，再给出N的全排列的某一个排列的次序数，输出该排列。
**Input**
第1行为一个数$N(N≤9)$，第2行为N的全排列的某一个排列的次序数。

**Output**

一行字符串，即该排列。
Sample in
3
1
Sample out
123



思路：可以用康托展开的逆运算来求解。假设已有{1,2,3,4,5}的全排列，并且已经从小到大排序完毕，现要找出第96个数的排列是什么，则康托展开逆运算的具体计算过程如下：
首先用 96-1 得到 95；
用 95 去除 4! 得到 3 余 23，商为 3 表示有 3 个数比它小，则该数是 4，所以第 1 位是 4；
用 23 去除3! 得到 3 余 5，商为 3，表示有 3 个数比它小，即该数是 4，但4前面已经出现过了，所以第2位是5；
用 5 去除 2! 得到 2 余 1，商为 2，表示有 2 个数比它小，即该数是 3，所以第 3 位是 3；
用 1 去除 1! 得到 1 余 0，表示有 1 个数比它小，即该数是 2，所以第 4 位是 2；
最后一个数只能是 1。
所以这个排列是 4 5 3 2 1。
又如找出第 16 个数的排列的计算过程如下：
首先用 16-1 得到 15；
用 15 去除 4! 得到 0余 15，表示有 0 个数比它小，即该数是 1，第 1 位是 1；
用 15 去除 3! 得到 2 余 3，表示有 2 个数比它小，即该数是 3，但由于1已经在之前出现过了，所以第 2 位是 4（因为1在之前出现过了，所以实际上比4小的数是2）；
用 3 去除 2! 得到 1 余 1，表示有 1 个数比它小，即该数是 2，但由于 1 已经在之前出现过了，所以第 3 位是 3（因为 1 在之前出现过了，所以实际上比 3 小的数是1）；
用 1 去除 1! 得到 1 余 0，表示有 1 个数比它小，即该数是 2，但由于 1、3、4已经在之前出现过了，所以第 4 位是 5（因为1、3、4在之前出现过了，所以实际上比 5 小的数是1）。
最后一个数只能是 2，所以这个数是 14352。
参考代码如下。



```python
import math

def cantor(m, n):
    fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]   # 预处理求出阶乘的值
    hash = [0] * 10

    num = 0
    m -= 1
    for i in range(n - 1, 0, -1):
        used = 0
        digit = m // fac[i] + 1                             # 计算有几个数比它小后加1
        m %= fac[i]                                         # 更新m
        for j in range(1, used + digit + 1):                # 查找之前有哪些数已被用过
            if hash[j]:
                used += 1
        num += (used + digit) * math.pow(10, i)
        hash[used + digit] = 1                              # 标记该数被使用过

    for i in range(1, n + 1):                               # 取出最后的未被使用的数
        if hash[i] == 0:
            return int(num + i)

    return -1

num, n = map(int, input().split())
perm = cantor(n, num)
print(' '.join(str(perm)))

```



![image-20231029141904258](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231029141904258.png)



```c++
//康托展开逆运算
#include <bits/stdc++.h>
using namespace std;

int fac[10]= {1,1,2,6,24,120,720,5040,40320,362880};   //预处理求出阶乘的值
int Hash[10];

int Cantor(int m,int n)
{
  int num=0;
  int used,digit;
  m--;
  for(int i=n-1; i>0; i--)
  {
    used=0;
    digit = m/fac[i] + 1;                           //计算有几个数比它小后加1
    m %= fac[i];                                    //更新m
    for(int j=1; j<=used+digit; j++)                //查找之前有哪些数已被用过
      if(Hash[j])
        used++;
    num += (used+digit)*pow(10,i);
    Hash[used + digit]=1;                           //标记该数被使用过
  }
  for(int i=1; i<=n; i++)                           //取出最后的未被使用的数
    if(Hash[i] == 0)
      return num+i;

  return -1;
}

int main()
{
  int num,n;
  cin >> num >> n;
  printf("%d\n",Cantor(n,num));
  return 0;
}
```









# 4 读题 

## 545C. Woodcutters

dp/greedy, 1500, https://codeforces.com/problemset/problem/545/C

Little Susie listens to fairy tales before bed every day. Today's fairy tale was about wood cutters and the little girl immediately started imagining the choppers cutting wood. She imagined the situation that is described below.

There are *n* trees located along the road at points with coordinates *x*~1~, *x*~2~, ..., *x~n~*. Each tree has its height *h~i~*. Woodcutters can cut down a tree and fell it to the left or to the right. After that it occupies one of the segments [*x~i~* - *h~i~*, *x~i~*] or [*x~i~*;*x~i~* + *h~i~*]. The tree that is not cut down occupies a single point with coordinate *x~i~*. Woodcutters can fell a tree if the segment to be occupied by the fallen tree doesn't contain any occupied point. The woodcutters want to process as many trees as possible, so Susie wonders, what is the maximum number of trees to fell.

**Input**

The first line contains integer *n* (1 ≤ *n* ≤ 10^5^) — the number of trees.

Next *n* lines contain pairs of integers *x~i~*, *h~i~* (1 ≤ *x~i~*, *h~i~* ≤ 10^9^) — the coordinate and the height of the *і*-th tree.

The pairs are given in the order of ascending *x~i~*. No two trees are located at the point with the same coordinate.

**Output**

Print a single number — the maximum number of trees that you can cut down by the given rules.

Examples

input

```
5
1 2
2 1
5 10
10 9
19 1
```

output

```
3
```

input

```
5
1 2
2 1
5 10
10 9
20 1
```

output

```
4
```

Note

In the first sample you can fell the trees like that:

- fell the 1-st tree to the left — now it occupies segment [ - 1;1]
- fell the 2-nd tree to the right — now it occupies segment [2;3]
- leave the 3-rd tree — it occupies point 5
- leave the 4-th tree — it occupies point 10
- fell the 5-th tree to the right — now it occupies segment [19;20]

In the second sample you can also fell 4-th tree to the right, after that it will occupy segment [10;19].



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231026190820436.png" alt="image-20231026190820436" style="zoom:50%;" />



## 1793C. Dora and Search

constructive algorithms, data structures, two pointers, 1200, 

https://codeforces.com/problemset/problem/1793/C

As you know, the girl Dora is always looking for something. This time she was given a permutation, and she wants to find such a subsegment of it that none of the elements at its ends is either the minimum or the maximum of the entire subsegment. More formally, you are asked to find the numbers 𝑙 and 𝑟 (1≤𝑙≤𝑟≤𝑛) such that $𝑎𝑙≠min(𝑎_𝑙,𝑎_{𝑙+1},…,𝑎_𝑟)$, $𝑎𝑙≠max(𝑎_𝑙,𝑎_{𝑙+1},…,𝑎_𝑟)$ and $𝑎𝑟≠min(𝑎_𝑙,𝑎_{𝑙+1},…,𝑎_𝑟)$, $𝑎𝑟≠max(𝑎_𝑙,𝑎_{𝑙+1},…,𝑎_𝑟)$.

A permutation of length 𝑛 is an array consisting of 𝑛 distinct integers from 11 to 𝑛 in any order. For example, \[2,3,1,5,4] is a permutation, but \[1,2,2] is not a permutation (2 occurs twice in the array) and \[1,3,4][1,3,4] is also not a permutation (𝑛=3, but 4 is present in the array).

Help Dora find such a subsegment, or tell her that such a subsegment does not exist.

**Input**

Each test consists of multiple test cases. The first line contains a single integer $𝑡 (1≤𝑡≤10^4)$ — the number of test cases. Description of the test cases follows.

For each test case, the first line contains one integer $𝑛(1≤𝑛≤2⋅10^5)$ — the length of permutation.

The second line contains 𝑛 distinct integers $𝑎_1,𝑎_2,…,𝑎_𝑛 (1≤𝑎_𝑖≤𝑛)$ — the elements of permutation.

It is guarented that the sum of 𝑛 over all test cases doesn't exceed 2⋅1052⋅105.

**Output**

For each test case, output −1−1 if the desired subsegment does not exist.

Otherwise, output two indexes 𝑙,𝑟 such that $[𝑎_𝑙,𝑎_{𝑙+1},…,𝑎_𝑟]$ satisfies all conditions.

If there are several solutions, then output any of them.

Example

input

```
4
3
1 2 3
4
2 1 4 3
7
1 3 2 4 6 5 7
6
2 3 6 5 4 1
```

output

```
-1
1 4
2 6
-1
```

Note

In the first and fourth test cases, it can be shown that there are no desired subsegments.

In the second test case, the subsegment \[1,4] satisfies all the conditions, because $max(𝑎_1,𝑎_2,𝑎_3,𝑎_4)=4,min(𝑎_1,𝑎_2,𝑎_3,𝑎_4)=1$, as we see, all the conditions are met.

In the third test case, the subsegment \[2,6] also satisfies all the conditions described.



<img src="/Users/hfyan/Library/Application Support/typora-user-images/image-20231026190955752.png" alt="image-20231026190955752" style="zoom:50%;" />





**数学思维**

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231026102551375.png" alt="image-20231026102551375" style="zoom:50%;" />



https://baike.baidu.com/item/戴德金原理/18881836

戴德金原理（Dedekind principle）亦称[戴德金分割](https://baike.baidu.com/item/戴德金分割/6095064?fromModule=lemma_inlink)，是保证直线连续性的基础，其内容为：如果把直线的所有点分成两类，使得：1.每个点恰属于一个类，每个类都不空。2.第一类的每个点都在第二类的每个点的前面，那么，或者在第一类里存在着这样的点，第一类中所有其余的点都在它的前面；或者在第二类里存在着这样的点，它在第二类的所有其余的点的前面 [3]。这个点决定直线的戴德金割切，此点称为戴德金点(或界点)，戴德金原理是戴德金((J.W.)R.Dedekind)于1872年提出来的，在构造欧氏几何的公理系统时，可以选取它作为连续公理，在希尔伯特公理组Ⅰ，Ⅱ，Ⅲ的基础上，[阿基米德公理](https://baike.baidu.com/item/阿基米德公理/1797603?fromModule=lemma_inlink)和康托尔公理合在一起与戴德金原理等价。



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231026103418567.png" alt="image-20231026103418567" style="zoom:50%;" />



https://zhuanlan.zhihu.com/p/528662514?utm_id=0

图兰定理（Turan's graph theorem）图论（graph theory）的一条基本定理，它是极值图论（extremal graph theory）的开端。此定理有很多种证明方法，我们将要介绍其中的五个。在陈述图兰定理前，我们先介绍一些背景知识。令 G 为一个简单图（simple graph），即不包含多重边（multiple edges）也不包含自环（loop）。令 G 的顶点（vertex）集为 $V={v_1,...,v_n}$，边（edge）集为 E。若一个图的每对顶点都被唯一的一条边相连，则成此图为一个完全图（complete graph），而一个图的完全子图（complete subgraph）叫作团（clique）。我们将包含 p 的顶点的 p-团写作$K_p$。



## 803A. Maximal Binary Matrix

constructive algorithms, 1400, https://codeforces.com/problemset/problem/803/A

You are given matrix with *n* rows and *n* columns filled with zeroes. You should put *k* ones in it in such a way that the resulting matrix is symmetrical with respect to the main diagonal (the diagonal that goes from the top left to the bottom right corner) and is lexicographically maximal.

One matrix is lexicographically greater than the other if the first different number in the first different row from the top in the first matrix is greater than the corresponding number in the second one.

If there exists no such matrix then output -1.

**Input**

The first line consists of two numbers *n* and *k* (1 ≤ *n* ≤ 100, 0 ≤ *k* ≤ 106).

**Output**

If the answer exists then output resulting matrix. Otherwise output -1.

Examples

input

```
2 1
```

output

```
1 0 
0 0 
```

input

```
3 2
```

output

```
1 0 0 
0 1 0 
0 0 0 
```

input

```
2 5
```

output

```
-1
```



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231026190632627.png" alt="image-20231026190632627" style="zoom:50%;" />



# 5 题目都有背景知识

## 12560: 生存游戏

matrices, http://cs101.openjudge.cn/practice/12560/

有如下生存游戏的规则：

给定一个n*m(1<=n,m<=100)的数组，每个元素代表一个细胞，其初始状态为活着(1)或死去(0)。

每个细胞会与其相邻的8个邻居（除数组边缘的细胞）进行交互，并遵守如下规则：

任何一个活着的细胞如果只有小于2个活着的邻居，那它就会由于人口稀少死去。

任何一个活着的细胞如果有2个或者3个活着的邻居，就可以继续活下去。

任何一个活着的细胞如果有超过3个活着的邻居，那它就会由于人口拥挤而死去。

任何一个死去的细胞如果有恰好3个活着的邻居，那它就会由于繁殖而重新变成活着的状态。



请写一个函数用来计算所给定初始状态的细胞经过一次更新后的状态是什么。

注意：所有细胞的状态必须同时更新，不能使用更新后的状态作为其他细胞的邻居状态来进行计算。

**输入**

第一行为n和m，而后n行，每行m个元素，用空格隔开。

**输出**

n行，每行m个元素，用空格隔开。

样例输入

```
3 4
0 0 1 1
1 1 0 0
1 1 0 1
```

样例输出

```
0 1 1 0
1 0 0 1
1 1 1 0
```

来源：cs10116 final exam



康威生命游戏(Game of Life)  https://baike.baidu.com/item/康威生命游戏/22668799?fr=ge_ala

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231026190204167.png" alt="image-20231026190204167" style="zoom: 50%;" />



细胞自动机

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231026190253685.png" alt="image-20231026190253685" style="zoom:50%;" />



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231026190315997.png" alt="image-20231026190315997" style="zoom:50%;" />





# 6 语法

## 6.1 逻辑删除

在Python中，执行删除操作通常建议使用logic删除，而不是physic删除。也就是说，不直接从列表中删除元素，而是标记它已经删除了。删除操作消耗的时间更少。

布尔代数（Boolean Algebra）是一种数学上的代数系统，用于处理逻辑运算和关系。它涉及布尔值（true和false）以及与、或、非等逻辑运算符。在逻辑删除中，布尔代数的概念被用于标记和操作数据行的删除状态，因此可以说逻辑删除涉及布尔代数的使用。

> 布尔代数
> 世界上不可能有比二进制更简单的计数方法了，它只有两个数字:0和1。从单纯数学的角度讲，它甚至比我们的十进制更合理。但是我们人有十个手指，使用起来比二进制(或者八进制)方便得多，所以在进化和文明发展过程中人类采用了十进制。二进制的历史其实也很早，中国古代的阴阳学说可以认为是最早二进制的雏形。而二进制作为一个计数系统公元前 2-5 世纪时由印度学者完成，但是他们没有使用0和 1计数。到17 世纪，德国伟大的数学家莱布尼兹(Gottfried Leibniz)把它完善，并且用0和 1表示它的两个数字，成为我们今天使用的二进制。二进制除了是一种计数的方式外，它还可以表示逻辑的“是”与“非”。这第二个特性在索引中非常有用。布尔运算是针对二进制，尤其是二进制第二个特性的运算，它很简单，可能没有比布尔运算更简单的运算了。尽管今天每个搜索引擎都官称自己如何聪明、多么智能(这个词非常忽悠人)其实从根本上讲都没有逃出布尔运算的框框。
> 布尔( George Boole)是19 世纪英国的一位中学数学老师，还创办过一所中学。后来在爱尔兰科克( Cork)的一所学院当教授。生前没有人认为他是数学家，虽然他曾经在剑桥大学数学杂志( Cambridge Mathematical Journal)上发表过论文。(英国另一位生前没有被公认为科学家的是著名物理学家焦耳，虽然他生前已经是英国皇家科学院院士，但是他的公认身份是啤酒商。)布尔在工作之余，喜欢阅读数学论著，思考数学问题。1854 年，布尔的《思维规律》(An Investigation ofthe Laws of Thought, on which are founded the Mathematical Theories ofLogic and Probabilities)一书，第一次向人们展示了如何用数学的方法解决逻辑问题。在此之前，人们普遍的认识是数学和逻辑是两个不同的学科今天联合国教科文组织依然把它们严格分开。
> 布尔代数简单得不能再简单了。运算的元素只有两个:1(TRUE，真 )和0(FALSE，假)。基本的运算只有“与”(AND)、“或”(OR)和“非”(NOT) 三种(后来发现，这三种运算都可以转换成“与非”AND-NOT 一种运算)。全部运算只用下列几张真值表就能完全描述清楚。
>
> 表 8.1 与运算真值表
>
> | AND  | 1    | 0    |
> | ---- | ---- | ---- |
> | 1    | 1    | 0    |
> | 0    | 0    | 0    |
>
> 
>
> 表 8.1 说明，如果 AND 运算的两个元素有一个是 0，则运算结果总是 0。如果两个元素都是 1，运算结果是 1。例如，“太阳从西边升起”这个判断是假的(0)，“水可以流动”这个判断是真的(1)，那么，“太阳从西边升起并且水可以流动”就是假的(0)。
>
> 表 8.2 或运算真值表
>
> | OR   | 1    | 0    |
> | ---- | ---- | ---- |
> | 1    | 1    | 1    |
> | 0    | 1    | 0    |
>
>
> 表 8.2 说明，如果 OR 运算的两个元素有一个是 1，则运算结果总是 1。
>
> 如果两个元素都是 0，则运算结果是 0。比如说，“张三是比赛第一名“李四是比赛第一名”是真的(1)，那么“张这个结论是假的(0) 三或者李四是第一名”就是真的(1)。
>
> 表8.3非运算真值表
>
> | NOT  |      |
> | ---- | ---- |
> | 1    | 0    |
> | 0    | 1    |
>
> 
>
> 表 8.3 说明，NOT 运算把 1变成 0，把0变成 1。比如，如果“象牙是白的”是真的(1)，那么“象牙不是白的”必定是假的(0)。
> 这么简单的理论能解决什么实际问题。和布尔同时代的数学家们也有同样的疑问。事实上，在布尔代数提出后 80 多年里，它确实没有什么像样的应用，直到 1938 年香农在他的硕士论文中指出用布尔代数来实现开关电路，才使得布尔代数成为数字电路的基础。所有的数学和逻辑运算，加、减、乘、除、乘方、开方等等，全都能转换成二值的布尔运算。数学的发展实际上是不断地抽象和概括的过程，这些抽象了的方法看似离生活越来越远，但是它们最终能找到适用的地方，布尔代数便是如此。
>
> if控制语句在程序中用于根据条件的真假来进行逻辑推理和计算，并根据条件的结果选择性地执行特定的代码块。，就是逻辑推理与计算合二为一。

 

## 6.2 高效数组，array类

https://baijiahao.baidu.com/s?id=1770291275843443574&wfr=spider&for=pc

```python
import sys
import array

a = array.array('i', [0]*1000000)
size = sys.getsizeof(a)//(1024*1024) + 1

print(f'signed int: {size}MB')

b = [0]*1000000
size = sys.getsizeof(b)//(1024*1024) + 1
print(f'list: {size}MB')

for code in array.typecodes:
    arr = array.array(code)
    print(code, arr.itemsize)
```

```
signed int: 4MB
list: 8MB
b 1
B 1
u 4
h 2
H 2
i 4
I 4
l 8
L 8
q 8
Q 8
f 4
d 8
```









OrderedDict。但是Python标准库中的OrderedDict删除元素的复杂度是O(1)。

from collections import OrderedDict

for _ in range(int(input())):
    n, k = map(int, input().split())
    cc = list(map(int, input().split()))
    



# 7 DFS模版



## 示例02386: Lake Counting

dfs similar, http://cs101.openjudge.cn/practice/02386

Due to recent rains, water has pooled in various places in Farmer John's field, which is represented by a rectangle of N x M (1 <= N <= 100; 1 <= M <= 100) squares. Each square contains either water ('W') or dry land ('.'). Farmer John would like to figure out how many ponds have formed in his field. A pond is a connected set of squares with water in them, where a square is considered adjacent to all eight of its neighbors.

Given a diagram of Farmer John's field, determine how many ponds he has.

输入

\* Line 1: Two space-separated integers: N and M

\* Lines 2..N+1: M characters per line representing one row of Farmer John's field. Each character is either 'W' or '.'. The characters do not have spaces between them.

输出

\* Line 1: The number of ponds in Farmer John's field.

样例输入

```
10 12
W........WW.
.WWW.....WWW
....WW...WW.
.........WW.
.........W..
..W......W..
.W.W.....WW.
W.W.W.....W.
.W.W......W.
..W.......W.
```

样例输出

```
3
```

提示

OUTPUT DETAILS:

There are three ponds: one in the upper left, one in the lower left,and one along the right side.

来源: USACO 2004 November



```python
#1.dfs
import sys
sys.setrecursionlimit(20000)
def dfs(x,y):
	#标记，避免再次访问
    field[x][y]='.'
    for k in range(8):
        nx,ny=x+dx[k],y+dy[k]
        #范围内且未访问的lake
        if 0<=nx<n and 0<=ny<m\
                and field[nx][ny]=='W':
            #继续搜索
            dfs(nx,ny)
n,m=map(int,input().split())
field=[list(input()) for _ in range(n)]
cnt=0
dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]
for i in range(n):
    for j in range(m):
        if field[i][j]=='W':
            dfs(i,j)
            cnt+=1
print(cnt)
```



## 示例05585: 晶矿的个数

matrices/dfs similar, http://cs101.openjudge.cn/practice/05585

在某个区域发现了一些晶矿，已经探明这些晶矿总共有分为两类，为红晶矿和黑晶矿。现在要统计该区域内红晶矿和黑晶矿的个数。假设可以用二维地图m[][]来描述该区域，若m[i][j]为#表示该地点是非晶矿地点，若m[i][j]为r表示该地点是红晶矿地点，若m[i][j]为b表示该地点是黑晶矿地点。一个晶矿是由相同类型的并且上下左右相通的晶矿点组成。现在给你该区域的地图，求红晶矿和黑晶矿的个数。

**输入**

第一行为k，表示有k组测试输入。
每组第一行为n，表示该区域由n*n个地点组成，3 <= n<= 30
接下来n行，每行n个字符，表示该地点的类型。

**输出**

对每组测试数据输出一行，每行两个数字分别是红晶矿和黑晶矿的个数，一个空格隔开。

样例输入

```
2
6
r##bb#
###b##
#r##b#
#r##b#
#r####
######
4
####
#rrb
#rr#
##bb
```

样例输出

```
2 2
1 2
```



```python
dire = [[-1,0], [1,0], [0,-1], [0,1]]

def dfs(x, y, c):
    m[x][y] = '#'
    for i in range(len(dire)):
        tx = x + dire[i][0]
        ty = y + dire[i][1]
        if m[tx][ty] == c:
            dfs(tx, ty, c)

for _ in range(int(input())):
    n = int(input())
    m = [[0 for _ in range(n+2)] for _ in range(n+2)]

    for i in range(1, n+1):
        m[i][1:-1] = input()

    r = 0 ; b=0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if m[i][j] == 'r':
                dfs(i, j, 'r')
                r += 1
            if m[i][j] == 'b':
                dfs(i,j,'b')
                b += 1
    print(r, b)
```



## 示例23937: 逃出迷宫

http://cs101.openjudge.cn/practice/23937/

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



这是模版题目，涉及到 递归/dfs/回溯。一旦出现模版题目，最多是中等难度，要求必须会。

```python
def dfs(mx, visited, x, y):
    # 如果到达右下角，返回True
    if x == n - 1 and y == n - 1:
        return True

    # 定义向右和向下的移动方向
    directions = [(0, 1), (1, 0)]

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        # 检查新坐标是否在矩阵范围内，是否已经访问过，以及是否可以通过
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and mx[nx][ny] == 0:
            visited[nx][ny] = True
            if dfs(mx, visited, nx, ny):
                return True
            visited[nx][ny] = False

    return False

# 读取输入
n = int(input())
mx = [list(map(int, input().split())) for _ in range(n)]

# 初始化访问标记数组
visited = [[False] * n for _ in range(n)]

# 起始点 (0, 0) 必须是可以通过的
if mx[0][0] == 1:
    print('No')
else:
    visited[0][0] = True
    if dfs(mx, visited, 0, 0):
        print('Yes')
    else:
        print('No')
```





