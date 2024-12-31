

# 暂且cheatsheet

by 2024 生命科学学院 本科生 李婧涵

#### **阅读提示**

这是我个人对于这一个学期的练习题/知识点的一个总结，含有极强主观因素，不具有复制性。

cheat（？）成果：押中了这次机考的一道中等难度题目（分苹果的变形：分割数字）



#### **正文部分**

一直记不得的（eg.字符串不可修改）

```python
print('%.5f'%(num))#浮点数输出
chr()#ascii转换 A 65 a 97
d.values()#字典中的元素
d.items()#变为元组
zip()#分离字典中键和值
my_dict = dict(zip(keys, values))# 使用 zip() 将两个列表配对，然后用 dict() 转换为字典
a = tuple()

#前缀和使用
S[i] = (S[i - 1] + dp[i])%(10**9 + 7)
begin, end = map(int, input().split())
print((S[end] - S[begin - 1] + 10**9 + 7)%(10**9 + 7))

#defaultdict 可以访问不存在的键
from collections import defaultdict
dd = defaultdict(int)
dd['a'] += 1
dd['b'] += 2

#存内存 `functools.lru_cache` 是 Python 标准库 `functools` 模块中的一个装饰器，用于实现带有缓存功能的函数。LRU 是 Least Recently Used（最近最少使用）的缩写，这种缓存策略会保留最近最常使用的数据，而当缓存达到其设定的最大容量后，会移除最近最少使用的数据以腾出空间。不可变的数据类型
from functools import lru_cache
@lru_cache(maxsize=128)  # 默认最大缓存条目数为128，也可以设置为None表示无限制
```

**数学筛**

```python
primes = []
is_prime = [True]*N
is_prime[0] = False;is_prime[1] = False
for i in range(1,N):
    if is_prime[i]:
        primes.append(i)
        for k in range(2*i,N,i): #用素数去筛掉它的倍数
            is_prime[k] = False
           
primes = []
is_prime = [True]*N
is_prime[0] = False;is_prime[1] = False
for i in range(2,N):
    if is_prime[i]:
        primes.append(i)
    for p in primes: #筛掉每个数的素数倍
        if p*i >= N:
            break
        is_prime[p*i] = False
        if i % p == 0: #这样能保证每个数都被它的最小素因数筛掉！
            break
```

**bruteforce**

假币问题：枚举[-1, 0, 1]三种情况

熄灯问题：根据提示（对第1行中每盏点亮的灯，按下第2行对应的按钮，就可以熄灭第1行的全部灯。如此重复下去，可以熄灭第1、2、3、4行的全部灯。），枚举第一行熄灯状态，最后检查状态：最后一行是不是全部熄灭。

```python
from copy import deepcopy ###重要
from itertools import product
D = [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]
lamps = [[0]*8]
for i in range(5):
    lamps.append([0] + list(map(int, input().split())) + [0])
lamps.append([0]*8)
for test in product(range(2), repeat=6):
    matrix = deepcopy(lamps)
    triggers = [list(test)]
    for i in range(1, 6):
        for j in range(1, 7):
            if triggers[i - 1][j - 1] != 0:
                for ele in D:
                    di, dj = i + ele[0], j + ele[1]
                    matrix[di][dj] = 1 - matrix[di][dj]
        triggers.append(matrix[i][1:7])
    if matrix[5][1:7] == [0]*6:
        for lines in triggers[:-1]:
            print(' '.join(map(str, lines)))
```

**双指针**

移动零：在不复制列表的情况下把所有0移动到最后

思路：j代表实际有意义的元素，i遍历nums中所有元素，遇到nums[i]为非零数值时，交换两个元素，j向右移动

```python
nums = list(map(int, input().split()))
j = 0
for i in range(len(nums)):
	if nums[i] != 0:
		nums[i], nums[j] = nums[j], nums[i]
        j += 1
print(nums)
```

相似思路：滑动窗口

XXXXX：寻找一个序列的子序列的最长子序列使其和不被X整除//基本思路：如果所有数的和不是x的倍数则不用去。现在设所有和是x倍数，如果头尾各去一段，设这两段的和分别为A, B。A和B一定至少有一个不是x倍数，那么去一头（不是x倍数的那头）就够了。

```python
from itertools import accumulate
def prefix_sum(nums):
    return list(accumulate(nums))#(返回前n项和)
def suffix_sum(nums):
    return list(accumulate(reversed(nums)))[::-1]
for _ in range(int(input())):
    N, x = map(int, input().split())
    a = [int(i) for i in input().split()]
    aprefix_sum = prefix_sum(a)
    asuffix_sum = suffix_sum(a)
    if N == 1:
        print(-1 if a[0]%x == 0 else 1)
    	continue
    leftmax, rightmax = 0, 0
    
    while left != right:
        total = asuffix_sum[left]
        if total % x != 0:
            leftmax = right - left + 1
            break
        else:
            left += 1

    left, right = 0, N - 1
    while left != right:
        total = aprefix_sum[right]
        if total % x != 0:
            rightmax = right - left + 1
            break
        else:
            right -= 1

    if leftmax == 0 and rightmax == 0:
        print(-1)
    else:
        print(max(leftmax, rightmax))
```

**二分查找**

```python
n = int(input())
shop = sorted(list(map(int,input().split())))
m = int(input())
for i in range(m):
    a, l, r = int(input()), 0, n - 1
    while l <= r:
        mid = (l+r)//2
        if a < shop[mid]:
            r = mid-1
        elif a >= shop[mid]:
            l = mid + 1
    print(r+1)
#cmp_to_key 函数：:将 compare_items 转换为 key 函数，传递给 bisect_left
```

河中跳房子：

```python
l, n, m  = map(int, input().split())
stones = [0]
for i in range(n):
    stones.append(int(input()))
stones.append(l)

def remove(l, m):
    count, d = 0, 0
    for i in range(1, n + 2):
        if stones[i] - d < l:
            count += 1
        else:
            d = stones[i]
    return count > m

left, right = 0, l + 1
while left < right:
    mid = (left + right)//2
    if remove(mid, m):
        right = mid
    else:
        ans = mid
        left = mid + 1
print(ans)
```

**greedy**

假设有n个正整数，将它们连成一片，能组成的最大最小整数。eg.23，9，182，79:最大整数是97923182，最小的整数是18223799。

```python
from math import ceil
input()
lt = input().split()
max_len = len(max(lt, key = lambda x:len(x)))
lt.sort(key = lambda x: x * ceil(2*max_len/len(x)))
lt1 = lt[::-1]
print(''.join(lt1),''.join(lt))
```

扫区域类问题：比如现在这一轮结束之后**第一个没被盖住的**是x,你就继续扫能盖住x的, 在所有能盖住x的里面挑**右端点最靠右边**的，把它选进来，然后更新第一个没被盖住的点，进入下一轮

```python
N = int(input())
a = list(map(int, input().split()))
intervals = sorted([(max(0, i-a[i]), min(N-1, i+a[i])) for i in range(N)])
ans = 0
right = 0
temp = -1
index = 0
while index < N and right < N:
    while index < N and intervals[index][0] <= right:
        temp = max(temp, intervals[index][1])
        index += 1
    right = temp + 1
    ans += 1
print(ans)
```

打怪兽：利用字典存储数据

```python
for _ in range(int(input())):
    n, m, b = map(int, input().split())
    kill = {}
    for i in range(n):
        t, x = map(int, input().split())
        if t in kill.keys():
            kill[t].append(x)
        else:
            kill[t] = [x]
    for t in kill.keys():
        kill[t].sort(reverse = True)
        kill[t] = sum(kill[t][:m])
    d = sorted(kill.items())
    for i in d:
        b -= i[1]
        if b <= 0:
            print(i[0])
            break
    if b > 0:
        print('alive')
```

垃圾炸弹：给出每个点可以清扫垃圾的量

```python
d = int(input())
n = int(input())
screen = [[0]*1025 for _ in range(1025)]
for i in range(n):
    x, y, v = map(int, input().split())
    for j in range(max(x - d, 0), min(x + d, 1024) + 1):
        for k in range(max(y - d, 0), min(y + d, 1024) + 1):
            screen[j][k] += v#垃圾周围d的区域都有清扫v个垃圾的潜力
res_max = 0
count = 0
for l in range(1025):
    for m in range(1025):
        if screen[l][m] > res_max:
            res_max = screen[l][m]
            count = 1
        elif screen[l][m] == res_max:
            count += 1
print('%d %d' %(count, res_max))
```

田忌赛马：高级双指针，找到恰好能赢的马（即左右两边弱对弱强对强），如果找不到就拿他对决对方最强的

```python
while True:
    n = int(input())
    if n==0: 
        break
    Tian = sorted(list(map(int, input().split())))
    King = sorted(list(map(int, input().split())))  
    lTian = 0; rTian = n - 1
    lKing = 0; rKing = n - 1
    ans = 0
    while lTian <= rTian:
        if Tian[lTian] > King[lKing]:
            ans += 1
            lTian += 1
            lKing += 1
        elif Tian[rTian] > King[rKing]:
            ans += 1
            rTian -= 1
            rKing -= 1
        else:
            if Tian[lTian] < King[rKing]:
                ans -= 1 
            lTian += 1
            rKing -= 1 
    print(ans*200)
```

建筑：根据**结束值，开始值**进行排序，将区间排序（注意按左端点和右端点排序是有区别的！通常在**从左往右扫的时候按右端点排序**）

```python
def generate_intervals(x, width, m):
    temp = []
    for start in range(max(0, x-width+1), min(m, x+1)):
        end = start+width
        if end <= m:
            temp.append((start, end))
    return temp

n, m = map(int, input().split())
plans = [tuple(map(int, input().split())) for _ in range(n)]
intervals = []
for x, width in plans:
    intervals.extend(generate_intervals(x, width, m))
intervals.sort(key=lambda x: (x[1], x[0]))
cnt = 0
last_end = 0
#核心逻辑
for start, end in intervals:
    if start >= last_end:
        last_end = end
        cnt += 1
print(cnt)
```

世界杯只因：类似于滑动窗口？将区间排序（注意按左端点和右端点排序是有区别的！通常在**从左往右扫的时候按右端点排序**）

```python
def calculate_min_coverage(n, points):	
    # 将每个点的可覆盖范围转化为区间 [max(0, i - points[i]), min(n, i + points[i] + 1))
    clips = [(max(0, i - points[i]), min(n, i + points[i] + 1)) for i in range(n)]
    clips.sort()  # 按区间左端点从小到大排序

    st, ed = 0, n  # st: 当前目标起始位置, ed: 结束位置是n（全覆盖范围）
    res = 0        # 记录安装摄像头的数量
    current_index = 0  # 当前枚举到的区间索引
    while st < ed:
        maxR = -1  # 当前轮次中能覆盖的最远右端点
        # 遍历所有左端点 <= st 的区间，并找到覆盖范围最远的区间
        while current_index < n and clips[current_index][0] <= st:
            maxR = max(maxR, clips[current_index][1])
            current_index += 1
        # 如果无法推进覆盖范围，说明无法覆盖目标区域，返回 -1
        if maxR <= st:
            return -1
        res += 1  # 安装一个摄像头
        st = maxR  # 更新目标区间的起始位置   
        # 如果当前区间的右端点已经覆盖到ed，结束循环
        if st >= ed:
            break   
    return res

if __name__ == "__main__":
    N = int(input())
    points = list(map(int, input().split()))
    print(calculate_min_coverage(N, points))
```

利用heap实现：

（背景知识）heapq ：堆队列是一种特殊的树形数据结构，堆顶（即根节点）总是最小的元素。

```python
`import heapq`
`heapq.heapify(data) #将可迭代对象转化为堆
`heapq.heappush(data, 3) #将一个元素添加到堆中，并保持堆的性质。
`min_element = heapq.heappop(heap) #从堆中弹出并返回最小的元素，同时保持堆的性质。
`smallest_three = heapq.nsmallest(3, data)#返回可迭代对象中最小的 n 个元素，可以指定一个 key 函数来定制排序规则。
```

懒更新，懒删除：需要删除一个元素时先对其打上标记，等到操作到该元素时再将其弹出去，但我们将其**视作已经不存在**进行操作；等到需要真正操作该元素（该元素已到堆顶）时，再做实质上的删除。  懒更新，每次只更新到堆中的最小值是实际的最小值

```python
#每次要删除x时out[x]+=1
from heapq import heappop,heappush
while ls:
    x = heappop(ls)
    if not out[x]:
        new_min = x
        heappush(ls,x) #不需要弹出的，记得压回去
        break
    out[x]-=1
```

魔法：

```python
import heapq
def max_potions(n, potions):
    health, consumed = 0, []
    for potion in potions:
        health += potion
        heapq.heappush(consumed, potion)
        if health < 0 and consumed:
            health -= consumed[0]
            heapq.heappop(consumed) #把最毒的排除掉，保证health成为最大正值
    return len(consumed)
```

割绳子：始终保证拼接的是最短的两根绳子

```python
import heapq
n = int(input())
length = list((map(int, input().split())))
heapq.heapify(length)
cut = 0
for i in range(n - 1):
    x1 = heapq.heappop(length)
    x2 = heapq.heappop(length)
    x = x1 + x2
    heapq.heappush(length, x)
    cut += x
print(cut)
```

is love：

```python
'''
按照区间右端点从小到大排序。从前往后依次枚举每个区间。
假设当前遍历到的区间为第i个区间 [li, ri]，如果有li > ed，
说明当前区间与前面没有交集。
'''
import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline
 
minH = [] #右端点最小堆
maxH = [] #左端点最大堆（通过负数存储）
 
ldict = defaultdict(int)#左端点出现次数
rdict = defaultdict(int)
 
n = int(input())
for _ in range(n):
    op, l, r = map(str, input().strip().split())
    l, r = int(l), int(r)
    if op == "+":
        ldict[l] += 1
        rdict[r] += 1
        heapq.heappush(maxH, -l)
        heapq.heappush(minH, r)
    else:
        ldict[l] -= 1
        rdict[r] -= 1
    #使用 while 循环，将最大堆 maxH 和最小堆 minH 中出现次数为 0 的边界移除。
    #通过比较堆顶元素的出现次数，如果出现次数为 0，则通过 heappop 方法将其从堆中移除。
    while len(maxH) > 0 >= ldict[-maxH[0]]:
        heapq.heappop(maxH)
    while len(minH) > 0 >= rdict[minH[0]]:
        heapq.heappop(minH)
    #判断堆 maxH 和 minH 是否非空，并且最小堆 minH 的堆顶元素是否小于
    #最大堆 maxH 的堆顶元素的相反数。
    if len(maxH) > 0 and len(minH) > 0 and minH[0] < -maxH[0]:
        print("Yes")
    else:
        print("No")
```

排序（难）：可以移到最前端的都pop掉了，剩下的pop后重新补到列表尾部，恰好实现了一轮筛选，并且剩下的保持原来的排列顺序

```python
from collections import deque
n, d = map(int, input().split())
h = deque(int(input()) for _ in range(n))
ans = []
while h:
    inlist = []
    max_val = h[0]
    min_val = h[0]
    for _ in range(len(h)):
        height = h.popleft()
        if abs(height - max_val) <= d and abs(height - min_val) <= d:
            inlist.append(height)
        else:
            h.append(height)
        min_val = min(min_val, height)
        max_val = max(max_val, height)
ans += sorted(inlist)
print(*ans, sep='\n')
```

最小猪：辅助栈，一个栈用来存储实际数据，一个同步更新最小的猪的数据

```python
real, pro = [], []#real，pro长度始终相同！！！
while True:
    try:
        if input() == "pop":
            if real:
                real.pop()
                if pro:
                    pro.pop()
        elif input() == "min":
            if pro:
                print(pro[-1])
        else:
            num = int(list(input().split())[1])
            real.append(num)
            if not pro or pro[-1] >= num:
                pro.append(num)
            else:
                pro.append(pro[-1]) #最小值未改变，加入在第i-1次操作时的最小值
    except EOFError:
        break
```

严格数学证明类：

炸鸡排：首先，**所有鸡肉的总时长是固定的sum(t)**，每次炸k个，最多sum(t)/k秒就一定会结束，无论什么方案。此时就会出现两种情况，第一种情况是所有t[i]<sum(t)/k，这种情况可以直接给构造，具体构造类似于题目里给出的1 1 1的例子。第二种情况是存在一个大于sum(t)/k，那么意味着就算炸了理论最长时间都不能炸熟它，那么就直接把它丢进锅里不管了，考虑一个k-1的问题即可

电池寿命：**理想的最优结果是所有电池总电量的一半。**一个很明显达不到理想结果的例子是当寿命最长的电池寿命高于其他所有电池寿命之和时，此时最优结果是其他所有电池寿命之和。猜测其他情况下，理想的最优结果是成立的，即: (1)情况一：寿命最长的电池寿命高于其他所有电池寿命之和，此时答案是其他所有电池寿命之和; (2)情况二：寿命最长的电池寿命小于或等于其他所有电池寿命之和，此时猜测答案就是总的电量/2。

愉悦旋律：要去寻找这个“未出现的序列"的最短长度，不妨这样去看待一个问题，以M=3为例，既有3种音符 123。首先这样去想，长度为1的子序列，是不是 1和2和3？长度为2的子序列 是不是[123]和[123]两个集合中任选一个？按照前后顺序排起来？长度为3的子序列，是不是集合[123] 和[123] 和[123]三个集合从前往后，每次取一个，按照前后顺序排起来？采用分块出现的思想，那么本题就很清晰了，例如，对于1523444512533，可以分成几个部分，15234/4451253/3，发现，第一个分隔号前，已经出现了1,2,3,4,5一次全部数字，第一个分隔号到第二个分隔号，又出现了1,2,3,4,5，完整的一次？那么我们可以肯定，长度为1和为2的全部子序列已经可以得到，所以只有长度为3的子序列没有被全部枚举，答案就是3。

```python
N, M = map(int, input().split())
*melody, = map(int, input().split())
cnt = 1
note = set()
for i in melody:
    note.add(i)
    if len(note) == M:
        cnt += 1
        note.clear()
print(cnt)
```

**dp**

找一个序列元素个数：确定数据范围后空间换时间

```python
n,m = map(int,input().split())
seq = [int(x) for x in input().split()]
dp = [0]*(n-1)+[1]
barrel = [False]*(100000+1)
barrel[seq[n-1]] = True
for i in reversed(range(n-1)):
    if barrel[seq[i]]:        
        dp[i] = dp[i+1]
    else:        
        dp[i] = dp[i+1]+1        
        barrel[seq[i]] = True
for i in range(m):
    print(dp[int(input())-1])
```

最长递增/减序列：

```python
n = int(input())
num = list(map(int, input().split()))
dp = [0]*n
for i in range(n - 1, -1, -1):
    count = 1
    for j in range(n - 1, i, -1):
        if num[i] < num[j]：
       		dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
#如遇到登山问题（类似），反着来一遍，把两个和相加
```

背包问题：

完全背包：![image-20241224162322156](C:\Users\lijh\AppData\Roaming\Typora\typora-user-images\image-20241224162322156.png)

宝可梦:n精灵球数量、m初始的体力值、k野生小精灵的数量,目标是收服最多小精灵；如可收服小精灵数一样，希望剩余体力越大

```python
n, m, k = map(int, input().split())
data = []
for i in range(k):
    data.append(list(map(int, input().split())))
dp = [[-1] * (m + 1) for _ in range(k + 1)]
#dp[i][j] 表示在收服了 i 个小精灵且皮卡丘剩余 j 体力的情况下，小智还剩下的精灵球数量
dp[0][m] = n
for i in range(k):
    for p in range(m):
        for q in range(i + 1, 0, -1): ##非常重要，防止被多次放入
            if p + data[i][1] <= m and dp[q - 1][p + data[i][1]] != -1:
                dp[q][p] = max(dp[q][p], dp[q - 1][p + data[i][1]] - data[i][0])
def capture():
    for i in range(k, -1, -1):
        for j in range(m, -1, -1):
            if dp[i][j] != -1:
                return '%d %d' %(i, j)
print(capture())
```

引入bisect库，零钱兑换

```python
import bisect
n, m = map(int, input().split())
coin = sorted(map(int, input().split()))
dp = [float('inf')] * (m + 1)
dp[0] = 0
for i in range(1, m + 1):
    w = bisect.bisect_right(coin, i)
    if w != 0:
        dp[i] = min(dp[i - coin[k]] for k in range(w)) + 1
print(dp[m] if dp[m] != float('inf') else -1)
```

开数组存储重复已有数据进行计数（类似于垃圾炸弹）

```python
n = int(input())
nums = list(map(int, input().split()))
data = [0]*100001
dp = [0]*100001
for ele in nums:
    data[ele] += ele
```

本质是递归的题（完美立方）：

```python
import math

def square(y):
    x = int(y)
    if x != 0 and math.sqrt(x) == int(math.sqrt(x)):
        return True
    
def div(x):
    if square(x):
        return True
    for i in range(1, len(x)):
        if square(x[: - i]):
            if div(x[len(x) - i:]):
                return True
            else:
                continue
print('Yes' if div(input()) else 'No')
```

最长回文序列：

```python
def palidrome(s, l, r):#从0开始向外衍生的回文序列
	while l >= 0 and r < len(s) and s[l] == s[r]:
		l -= 1
        r += 1
	return s[l+1:r]
max_str = ''
max_num = 0
for i in range(len(s)):
    dan_str = palidrome(s, i, i)#奇数个数
    if len(dan_str) > max_num:
        max_num = len(dan_str)
        max_str = dan_str
    ou_str = palidrome(s, i, i+1)#偶数个数
    if len(ou_str) > max_num:
        max_num = len(ou_str)
        max_str = ou_str
    return max_str
```

核电站：无论如何都不会炸的方法数 - 连续放的方法数(果第i位是不能放的，那么说明i-m这段区间肯定全放了)

```python
n, m = map(int, input().split())
DP = [0] * 60
DP[0] = 1 #DP[i]是第i个位置的方案数。
for i in range(1, n + 1):
    if i < m: #达不到连续放置m个的情况
        DP[i] = DP[i - 1] * 2  # 从第1个到第m-1个，方案都可以选择放/不放
    elif i == m: #第m个要小心了
        DP[i] = DP[i - 1] * 2 - 1
    else:#i>m
        DP[i] = DP[i - 1] * 2 - DP[i - m - 1]
print(DP[n])
```

放苹果：分类讨论

```python
def apple(m, n):
    if m == 0:
        return 1
    if n == 1:
        return 1
    if m < n:
        return apple(m, m)
    else:
        return apple(m, m - 1) + apple(m - n, n)
#dp[m][n−1] 表示至少有一个盘子空着的情况。, dp[m−n][n] 表示每个盘子至少放一个苹果的情况（这里分类讨论第n个盘子放不放苹果）
```

区间dp:![image-20241224233258777](C:\Users\lijh\AppData\Roaming\Typora\typora-user-images\image-20241224233258777.png)

处理环状：枚举分开位置/将链条延长2倍

树形状：

```python
m = 10**9+7
n, k, d = map(int, input().split())
#A[i]：总权重为i的路径数 ； B[i]：总权重为i且所有边权重小于d的路径数，本题即求用不大于k的正整数划分i，用小于d的正整数划分i的方法数之差
normal = [1] + [0]*n
produce = [1] + [0]*n
for i in range(1, n + 1):
    normal[i] = sum(normal[max(i - k, 0): i])%m
    produce[i] = sum(produce[max(i - d + 1, 0): i])%m
print((normal[i] - produce[i] + m)%m)
```

分割成k个和相同子集：第 *i* 位为 0 则表示数字 *nums*[*i*] 可以使用,*dp*[*U*] 即可，其中 *U* 表示全部数字使用的集合状态。

```python
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        per = sum(nums) // k
        nums.sort()
        if nums[-1] > per:
            return False
        n = len(nums)
        dp = [False] * (1 << n)#将 1 左移 n 位后，相当于在 1 的后面添加了 n 个 0。二进制。2^n
        dp[0] = True
        cursum = [0] * (1 << n)
        for i in range(0, 1 << n):
            if not dp[i]:
                continue
            for j in range(n):
                if cursum[i] + nums[j] > per:
                    break
                if (i >> j & 1) == 0:
                    next = i | (1 << j)
                    if not dp[next]:
                        cursum[next] = (cursum[i] + nums[j]) % per
                        dp[next] = True
        return dp[(1 << n) - 1]
```

**二进制分解法**：对于每种票，如果剩余票数 `n_i` 大于1，我们可以将其按二进制分解为多个“包”，从而有效减少每次计算的重复性。

```python
max_count = tickets_remaining[i]
        k = 1
        while k <= max_count:
            # 处理 k 张票
            for j in range(N, price * k - 1, -1):
                dp[j] = min(dp[j], dp[j - price * k] + k)
            max_count -= k
            k *= 2  
        # 处理剩余的票
        if max_count > 0:
            for j in range(N, price * max_count - 1, -1):
                dp[j] = min(dp[j], dp[j - price * max_count] + max_count)
```

**dfs**

基本套路（本质，递归）

权值相加：动脑筋的模板题

```python
D = [[1, 0], [0, 1], [-1, 0], [0, -1]]
def dfs(temp, count, x, y):
    if (x, y) == (n - 1, m - 1):
        global path, max_v
        if count > max_v:
            max_v, path = count, temp[:]
        return
    for ele in D:
        nx, ny = x + ele[0], y + ele[1]
        if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny]:
            vis[nx][ny] = True
            temp.append([nx + 1, ny + 1])
            dfs(temp, count + maps[nx][ny], nx, ny)
            temp.pop()
            vis[nx][ny] = False

n, m = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))
vis = [[False for _ in range(m)] for _ in range(n)]
vis[0][0] = True
max_v, path = - float('inf'), [[1, 1]]
dfs([[1, 1]], maps[0][0], 0, 0)
for ele in path:
    print(' '.join(map(str, ele)))
```

全排列：标记某一个数是否被使用过，注意回溯

```python
def array(n, count, status, vis, result):
    if count == n + 1:
        result.append(status[:])
        return
    for i in range(1, n + 1):
        if not vis[i]:
            status.append(i)
            vis[i] = True
            array(n, count + 1, status, vis, result)
            status.pop()
            vis[i] = False

def g(n):
    result = []
    vis = [False]*(n + 1)
    array(n, 1, [], vis, result)
    return result

n = int(input())
for ele in g(n):
    print(' '.join(list(map(str, ele))))
```

和brute force结合：双十二，把所有用券方式都枚举出来

```python
def plans(n, price, count, all_plans, plan):  # 递归列出所有购买方案
    if count == n + 1:
        all_plans.append(plan[:])
        return
    for i in price[count].keys():
        plan.append(i)
        plans(n, price, count + 1, all_plans, plan)
        plan.pop()
    return

def buy(n, m, price, coupon):
    all_plans = list()  # 列出所有购买方案
    plans(n, price, 1, all_plans, [])
    # for i in all_plans:
    #     print(i)
    final_price = list()  # 每个方案的最终价格
    for plan in all_plans:  # 对每个购买方案
        totals_rsp = list()  # 每个店铺的总价
        prices = [price[i][plan[i - 1]] for i in range(1, n + 1)]  # 每个商品的价格
        total = sum(prices)  # 所有商品的总价
        total -= total // 300 * 50  # 跨店满减
        for i in range(1, m + 1):  # 对每个店铺
            prices_rsp = [price[j + 1][plan[j]]
                          for j in range(n) if plan[j] == i]  # 每个商品在该店铺的价格
            totals_rsp.append(sum(prices_rsp))  # 该店铺的总价
        store = 0
        for total_rsp in totals_rsp:
            store += 1
            discount = 0
            for j in coupon[store]:
                if total_rsp >= j[0]:
                    discount = max(j[1], discount)
            total -= discount
        final_price.append(total)
    # print(final_price)
    return min(final_price)

n, m = map(int, input().split())
price = dict()
coupon = dict()
for i in range(n):
    price_i = dict()
    price_raw = list(input().split())
    for j in price_raw:
        price_i[int(list(j.split(':'))[0])] = int(list(j.split(':'))[1])
    price[i + 1] = price_i
for i in range(m):
    coupon_i = list()
    coupon_raw = list(input().split())
    for j in range(len(coupon_raw)):
        coupon_i.append(tuple(map(int, coupon_raw[j].split('-'))))
    coupon[i + 1] = coupon_i
# print(n, m, price, coupon)
print(buy(n, m, price, coupon))
```

滑雪问题：和dp结合，对于四周满足条件的点：`dp[x][y] = max(dfs(nx, ny) + 1, dp[x][y])`，最后返回`dp[x][y]`

**bfs**

 Dijkstra

```python
import heapq
m, n, p = map(int, input().split())
maps = [list(input().split())for _ in range(m)]
D = [[-1, 0], [1, 0], [0, 1], [0, -1]]
for _ in range(p):
    bx, by, ex, ey = map(int, input().split())
    if maps[bx][by] == '#' or maps[ex][ey] == '#':
        print('NO')
        continue
    queue, visit, res = [(0, bx, by)], set((bx, by, -1)), []
    visit.add((bx, by, -1))
    while queue:
        steps, x, y = heapq.heappop(queue)
        if (x, y) == (ex, ey):
            res.append(steps)
        for i in range(4):
            nx, ny = x + D[i][0], y + D[i][1]
            if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] != '#' and (nx, ny, i) not in visit:
                energy = steps + abs(int(maps[nx][ny]) - int(maps[x][y]))
                heapq.heappush(queue, (energy, nx, ny))
                visit.add((nx, ny, i))
    print(min(res) if res else 'NO')
```

```python
from collections import deque
def bfs(x, y):
    queue, vis = deque([(status, x, y)]), set((status, x, y))
    while queue:
        status, sx, sy = queue.popleft()
        if flag:
            return a#what you want
        else:
            for ele in D:
                nx, ny = x + ele[0], y + ele[1]
                if nx, ny in boundaries and (status, nx, ny) not in vis and others:
                    queue.append((status, nx, ny))
                    vis.add((status, nx, ny))
```

综合：水淹七军，先dfs模拟水流

```python
#dfs
import sys
sys.setrecursionlimit(300000)
input = sys.stdin.read
# 判断坐标是否有效
def is_valid(x, y, m, n):
    return 0 <= x < m and 0 <= y < n
# 深度优先搜索模拟水流
def dfs(x, y, water_height_value, m, n, h, water_height):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if is_valid(nx, ny, m, n) and h[nx][ny] < water_height_value:
            if water_height[nx][ny] < water_height_value:
                water_height[x][y] = water_height_value
                dfs(nx, ny, water_height_value, m, n, h, water_height)
# 主函数
def main():
        for _ in range(p):
            x, y = map(int, data[idx:idx + 2])
            idx += 2
            x, y = x - 1, y - 1
            if h[x][y] <= h[i][j]:
                continue

            dfs(x, y, h[x][y], m, n, h, water_height)
        results.append("Yes" if water_height[i][j] > 0 else "No")

if __name__ == "__main__":
    main()
```

```python
#bfs   
from collections import deque
def bfs(start_x, start_y, start_height, m, n, h, water_height):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([(start_x, start_y, start_height)])
    water_height[start_x][start_y] = start_height
    while q:
        x, y, height = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if is_valid(nx, ny, m, n) and h[nx][ny] < height:
                if water_height[nx][ny] < height:
                    water_height[nx][ny] = height
                    q.append((nx, ny, height))

def main():
        for _ in range(p):
            x, y = map(int, data[idx:idx + 2])
            idx += 2
            x, y = x - 1, y - 1
            if h[x][y] <= h[i][j]:
                continue
            bfs(x, y, h[x][y], m, n, h, water_height)
        results.append("Yes" if water_height[i][j] > 0 else "No") #其余同上
```

不知道算啥但是就放着：

```python
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x]) #使用路径压缩技术将 x 直接连接到其根节点
    return parent[x]
def union(x, y):
    root_x, root_y = find(x), find(y)
    if root_x != root_y:
        parent[root_x] = root_y
        size[root_y] += size[root_x]#将 x 所属连通分量的根节点的父节点设置为 y 所属连通分量的根节点。
n, m = map(int, input().split())
parent = list(range(n + 1))
size = [1] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b) #对于每条边 (a, b)，调用 union(a, b) 将节点 a 和 b 所属的连通分量合并为一个。
classes = [size[x] for x in range(1, n + 1) if x == parent[x]]
print(len(classes))
```

接雨水：

单调栈方法通过维护一个递减栈来找到每个位置左侧和右侧的第一个更高柱子，进而计算该位置上方能接住的雨水量。

```python
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
```

双指针方法则是通过两个指针从数组的两端向中间移动，同时记录左右两边的最大高度。在每一步中，选择较短的一边进行处理

```python
ans = left = pre_max = suf_max = 0
right = len(height) - 1
while left < right:
	pre_max = max(pre_max, height[left])
	suf_max = max(suf_max, height[right])
	if pre_max < suf_max:
		ans += pre_max - height[left]
		left += 1
	else:
		ans += suf_max - height[right]
		right -= 1
```

三数之和

```python
def threeSum(nums):
    nums.sort()
    res = set()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        d = {}
        for x in nums[i + 1:]:
            if x not in d:
                d[-nums[i] - x] = 1
            else:
                res.add((nums[i], -nums[i] - x, x))
    return len(res)
n = list(map(int, input().split()))
print(threeSum(n))
```

