# **Cheat Sheet**

李皓翔 24物院

# 笔试

## acsll

![1-851-jpg_6_0_______-784-0-0-784](C:\Users\15143\Desktop\1-851-jpg_6_0_______-784-0-0-784.jpg)

## 程序框图

![image-20241204231156542](.\pic\CS0.png)



## ip

ABC类，掩码

![](.\pic\CS3.jpg)



在Python中True等价于1



![](.\pic\CS1.jpg)

![](.\pic\CS2.jpg)





请列举出你所知道的三种互联网通讯协议的名称：TCP，UDP和HTTP。

> TCP（Transmission Control Protocol）：传输控制协议
>
> UDP（User Datagram Protocol）：用户数据报协议
>
> HTTP（Hypertext Transfer Protocol）：超文本传输协议



根据**（空间）局部性原理**，在程序执行时，如果一个信息项正在被访问，那么近期它很可能也会被再次访问，存储在它附近的信息也很可能被访问到。



根据计算机信息的**分层存储原理**，在存储器硬件的金字塔结构中，从上到下，容量越来越大，速度 越来越慢。







在计算机硬件系统中，连接主板和外部设备之间的硬件设备是

A) 总线 B) 芯片组 C) 内存 **D) 适配器**

> 适配器（如网卡、声卡等）用于连接主板和外部设备。



根据冯·诺伊曼结构，计算机由运算器，控制器，存储器，输入设备和输出设备五个部分相互连接组成。



CPU内部包含的四个主要部件是：算术逻辑运算器（ALU）、寄存器组、中断处理器、和程序控制器。

> 算术逻辑运算器（ALU）：执行算术和逻辑运算
>
> 寄存器组：临时存储数据
>
> 中断处理器：处理中断请求
>
> 程序控制器：控制程序执行



32位CPU可以直接寻址的最大物理内存容量是4 GB

> CPU 通过数据总线，控制总线以及地址总线和其它部件进行各种信息的传递。为了保证性能，数据总线的宽度应该与 CPU 字长一致。
>
> 数据总线的宽度通常与CPU的字长（Word Size）一致是为了保证性能和效率。这里有几个关键点：
>
> **CPU 字长**：指的是CPU一次能够处理的数据量大小，它决定了CPU内部寄存器、算术逻辑单元（ALU）等组件的操作数宽度。比如32位CPU的一次操作可以处理32位的数据，而64位CPU则可以处理64位的数据。
>
> **数据总线宽度**：是指数据总线一次能传输的数据量，它直接影响到CPU与内存或其他外部设备之间数据交换的速度。如果数据总线的宽度与CPU字长相同，那么在进行数据读写时，就不需要分多次传输，从而提高了数据传输的效率。
>
> **地址总线宽度**：决定了CPU可以直接寻址的地址空间大小。例如，32位地址总线可以访问(2^{32} )个不同的地址，即4GB的物理地址空间；而64位地址总线理论上可以访问(2^{64})个地址，这远远超过了目前大多数系统的实际需求。
>
> **控制总线**：它不直接与性能或数据量相关，而是用于传递控制信号，如读/写命令、中断信号等，以协调CPU与其他系统组件之间的操作。
>
> 为了最大化性能，理想情况下，数据总线的宽度应该匹配CPU的字长，这样每次内存访问都可以最有效地利用CPU的能力。不过，在实际设计中，也会考虑到成本、功耗等因素来决定总线宽度。有时，为了降低成本或出于其他考虑，可能会选择较窄的数据总线，但这通常会导致性能上的妥协。



为现代电子计算机的出现作出了重要贡献的两位科学家分别是 阿兰·图灵 和 冯·诺伊曼



计算机程序中的 3 种基本控制结构是： 顺序结构 、分支结构 和 循环结构



在计算机系统中，是通过文件和文件系统来组织和管理存储在外存储设备(硬件)上的信息的。











# 内置问题速查

最大公因数 遍历序列 快速查找 math **二进制遍历（优化重复背包问题） **

## gcd

```python
from math import gcd
gcd(a,b)#最大公因数
#最小公倍数*最大公因数=a*b
```

##  permutations

```python
from itertools import permutations

for i in itertools.permutations([1, 2, 3]):
	print(i, end="  ")
#(1, 2, 3)  (1, 3, 2)  (2, 1, 3)  (2, 3, 1)  (3, 1, 2)  (3, 2, 1)

for i in itertools.permutations([1, 2, 3], 2):
    print(i, end="  ")
    print(type(i))
#(1, 2)  <class 'tuple'>
#(1, 3)  <class 'tuple'>
#(2, 1)  <class 'tuple'>
#(2, 3)  <class 'tuple'>
#(3, 1)  <class 'tuple'>
#(3, 2)  <class 'tuple'>

```

## combinations

```python
from itertools import combinations
combinations(list,k)		#生成list的k元组合（无序）（每个以元组形式存在）
```

## math

```python
math.pow(x, y) == x**y
math.factorial(n) == n!
```

## 二进制遍历

```python
cur_num=int(input())
k = 1
while cur_num>0:
    use_num = min(cur_num, k)
    cur_num -= use_num
    #use_num
    k*=2
#use_nums可以用二进制表示input内的所有数
# 二进制优化
dp = [float('inf')] * (n + 1)
dp[0] = 0
for i in range(7):
    cur_price = price[i]
    cur_num = nums[i]
    k = 1
    while cur_num > 0:
        use_num = min(cur_num, k)
        cur_num -= use_num
        for j in range(n, cur_price * use_num - 1, -1):
            dp[j] = min(dp[j], dp[j - cur_price * use_num] + use_num)
        k *= 2
if dp[-1] == float('inf'):
    print('Fail')
else:
    print(dp[-1])
```

# 输出

## 保留小数

```python
f = 2.3456789

print('%.2f'%f)
print('%.3f'%f)
print('%.4f'%f)

#2.35
#2.346
#2.3457
```

## 大小写转换

```python
a.upper()
a.lower()
```

## f'  '

```python
f"{s:.2f}"#保留两位小数
```

## join

```python
print(' '.join(['1','2','3']))
print(' '.join(map(str,p)))
```

## 字符串处理

## acsll

![1-851-jpg_6_0_______-784-0-0-784](C:\Users\15143\Desktop\1-851-jpg_6_0_______-784-0-0-784.jpg)

## 进制

2进制`bin()`输出0b...，八进制`oct()`输出0o...，十六进制`hex()`输出0x...，`int(str,base)`可以把字符串按照指定进制转为十进制默认base=10

## 浅拷贝

```python
p[:] #消除浅拷贝

import copy
tem=copy.deepcopy(fill)#消除多层浅拷贝
```

## all

```python
all(iterable) #等价于快速 False in iterable
```

## zip

```python
a=['1','2']
b=[1,2]
l=zip(a,b)
print(list(l))
#[('1',1),('2',2)]
```

## sorted

```python
###1###
combined = sorted(zip(a, b), key=lambda x: (x[0], -x[1]),reverse=True)
a, b = zip(*combined)

###2###
a=list(map(int,input().split()))
b=list(map(int,input().split()))
combined = sorted(zip(a, b), key=lambda x: (x[0]+x[1])%4,reverse=True)
a, b = zip(*combined)
```

## lru_cache

```python
from functools import lru_cache
from math import sin

@lru_cache(maxsize=4096)#(maxsize=None)
def sin_half(x):
    return sin(x)/2

print('first call result:',sin_half(60))
print('second call result:',sin_half(60))
#……
print()
```

## bisect

```python
import bisect

# 已排序的列表
a = [1, 2, 4, 7]

# 查找元素 3 应该插入的位置
index = bisect.bisect_left(a, 3)
print(index)  # 输出: 2

# 插入元素 3 到列表 a 中
bisect.insort_left(a, 3)
print(a)  # 输出: [1, 2, 3, 4, 7]

#自己的代码
l=max(it)
r=sum(it)+1
k=0
while l<r : #1
    p=(l+r)//2
    s=1
    su=0
    for i in it:
        if su+i>p:
            su=i
            s+=1
        else:
            su+=i
    if s>M: #2
        l=p+1
    else:
        r=p
print(l) #3        
```

## enumerate

```python
fruits = ['apple', 'banana', 'cherry']
for index, value in enumerate(fruits,1): #start value = 1
    print(index, value)
#1 apple
#2 banana
#3 cherry
```

# 数据结构

## set

```python
p=set()
#集合，快速查找的无重复元素集
p.add(1)
in p #快速判断
p.remove(元素名)
p.discard(元素名)#不会报错
a|b #并
a&b #交
a-b #表示∈a且∉b的元素的集合
a^b #等于a|b-a&b
a>b a<=b #比较从属关系，若无则为False
```

## defaultdit

```python
from collections import defaultdict
#这是一种"如果访问的key不存在与字典中,就给它新建一个默认值 dict[key]=default_value 的字典
vd=defaultdict(int) #以0为默认值的defaultdict
a=defaultdict(list) #以空列表为默认值的defaultdict
#类似地,括号里是int,set也可以
```

## deque

```python
import deque
```

## heapq

```python
import heapq
a = []   #创建一个空堆
heapq.heappush(a,18)

heapq.heappop(h) #输出最小值
```

