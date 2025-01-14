### **Cheat Sheet 重置&回忆版**

（原版是手写的而且放在学校了）

#### 一、内置函数用法

1. math

​      用于一些计算和数据处理

​      常用的一些：

​      向上取整：math. ceil(x)

​      向下取整：math. floor(x)

​      开方：math. sqrt(x)

​      方幂：math. pow(x,y)   #x的y次方

​      阶乘：math. factorial(n)

2. format

​       用于格式化处理字符串

​       常用的一些：

​       将参数按格式插入：f"I'm {} years old"

​       小数点保留：’{ :.2f }'. format(x) #保留两位小数

3. 正则表达式（re）

   用于提取字符串中的特定字符

   提取数字 result=re. findall(r'\d+',strings)

   提取字母 result=re. findall(r'[a-zA-Z]',strings)

   #提取出来的是列表

4. collections

   Counter：用于列表计数

   ​           eg：t=Counter(s)  #t是一个字典

   defaultdict：给予字典一个默认值

   ​          eg：d=defaultdict(int) #默认值为0

   deque：双端队列（在bfs中常用）

5. heapq

   含有关于堆的一些操作

   heapqpop：推出

   heapqpush：推入

6. bisect

   用于二分查找，分为left和right两种

#### 二、特殊模板：

1. dfs：以全排列为例

   ```python
   def dfs(s,p):
       if len(s)==n:
           r.append('')
           return
       for x in range(1,n+1):
           if x in s:continue
           s.append(x)
           dfs(s,p)
           s.pop()
   ```

2. bfs：以寻宝为例 

```python
from collections import deque
k=[[-1,0],[1,0],[0,-1],[0,1]]
def bfs(w,p,r,step):
    while r:
      for _ in range(len(r)):
         i,j=r.popleft()
         if p[i][j]==1:
             return step
         for x in k:
             ii,jj=i+x[0],j+x[1]
             if 0<=ii<m and 0<=jj<n and w[ii][jj]==0 and p[ii][jj]!=2:
                 w[ii][jj]=1
                 r.append((ii,jj))
      step+=1
    return -1
```

3. dijkstra：以走山路为例

```python
from heapq import heappush,heappop
k=[[-1,0],[1,0],[0,1],[0,-1]]
def walk(s1,s2,e1,e2):
    r=[(0,s1,s2)]
    w=[]
    while r:
        d,a,b=heappop(r)
        if (a,b) in w:
            continue
        w.append((a,b))
        if a==e1 and b==e2:
            return d
        for x in k:
            aa,bb=a+x[0],b+x[1]
            if 0<=aa<m and 0<=bb<n and q[aa][bb]!='#' and (aa,bb) not in w:
                dd=d+abs(int(q[aa][bb])-int(q[a][b]))
                heappush(r,(dd,aa,bb))
    return 'NO'
```

4. 二分查找：以河中跳房子为例

```Python
def binary(s):
    l,r=0,L
    while l<r:
        mid=(l+r)//2
        if move(mid)>m:
            r=mid
        else:
            l=mid+1
    return l-1
```

5. 二分归并排序：以求逆序数为例

   ```python
   def mid(p):
       if len(p)<=1:
           return p,0
       m=len(p)//2
       left,l=mid(p[:m])
       right,r=mid(p[m:])
       Q,q=cnt(left,right)
       ans=l+r+q
       return Q,ans
   def cnt(left,right):
       c=[]
       i,j=0,0
       v=0
       while i < len(left) and j <len(right):
           if left[i]<=right[j]:
               c.append(left[i])
               i+=1
           else:
               c.append(right[j])
               j+=1
               v+=len(left)-i
       c.extend(left[i:])
       c.extend(right[j:])
       return c,v
   ```

#### 三、其他

（此类为在题中遇到的零散的一些语句或操作）

序列（或字符串）反转：s=s[::-1]

增加回溯深度：sys. setrecursionlimit()

按要求排序：s=sorted(key=lambda  x:#填充要求)

退出程序：exit()

清空集合：set.clear()

#### 四、针对题型

1. dp

   动态规划的题目基本变化较大，但掌握几种背包的题型比较重要

   重点：推出状态变化式

2. 搜索

   主要是dfs和bfs，这两种依赖模板，也要考虑题中的一些特殊要求

3. 贪心

   这类题可能比较困难，但也有可能一“蒙”就中，考验数学功底

   要敢想敢试，指不定就蒙对了（）

4. 暴力实现题

   这类题只要按题目要求来就行，如果超时就说明需要优化

5. 二分查找

   比较少见，遇到了也要根据题目调整模板























