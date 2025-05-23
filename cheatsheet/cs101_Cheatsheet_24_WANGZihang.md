# Cheatsheet

## 机考前我主要是在刷题，没有准备Cheatsheet，这一份是在考后总结的，回忆一下知识点。

### 1.Python基本语法

1. 变量和数据类型

   一些基本的内容见菜鸟教程。核心的要点

   六个数据类型：

   1. 可变数据（3个）：List（列表）、Dictionary（字典）、Set（字典）；
   2. 不可变数据（3个）：Number（数字）、String（字符串）、Tuple（元组）。

   要点：

   1. 时间复杂度：在如果找 index 是否在一个内容中，知道位置，用List快；如果不知道位置，只知道在内部，可以一开始就用Set存储，效率会更高。在一些问题中这个可能有影响。比如bfs记录的问题。
   2. bool和int可以相互转化，True视为1，False视为0，而判断过程中，非零就是True，0就是False。这在一些问题中可以精简代码，但是在转化过程的耗时  

   数和字符串的定义和用法比较基本，就不列出。 要注意的还是时间复杂度问题：pop（0）的复杂度较高，如果需要输出列表前段，可以考虑用deque，其的popleft速度较快。相较而言，append等处理的速度较快。

2. 控制结构

   1. for循环 

      一般两种：

      `for i in range(n):`

      `for index in f:`

       else 语句：不break就执行

   2. while循环

      可以和for转换，要点类似

   3. if语句

   ​       正常判断，如果在非的情况下进一步讨论用elif

   3. 函数

      函数用 def 定义。如果要用函数外部的内容，list可以正常调用，参数需要global处理，如果是OJ要特别处理，补充说明一下。有时候定义函数会比正常写更快。

### 2.算法与数据结构

1. 贪心算法

   贪心算法的本质是数学归纳法。实际过程中可以先在草稿纸上推一下，看一下有没有什么特点，或者从一头开始想，看有没有什么最佳策略。从个人的经验而言，最怕的是想到的贪心有错误，这个只能找特例处理，比较麻烦。

2. 背包问题

   背包问题：0/1背包或者完全背包。

   1. 0/1背包（参考同学笔记）

      考虑取前i个物品用t时间所能得到的最大值，枚举第i个物品是否取完成转移。注意这里**加上时间参数t**，因为转移过程中t的限定可能会变。“加参数”是DP问题中最重要的技巧之一。

      ```python
      dp = [0]*T
      for i in range(n):
          for t in range(T,time[i]-1,-1):
              dp[t] = max(dp[t],dp[t-time[i]]+value[i])
      ans = dp[T]
      ```

      这里采用“**滚动数组**”的方法将二维数组压缩成一维，是DP问题中常用的技巧。这基于选前i个物品的状态仅依赖于选前i-1个物品的状态。注意**内层循环要倒着遍历**（避免同一个物品被重复考虑）！

   2. 完全背包

      只需将之前的遍历改为正向即可。这样实际上就考虑到了每个物品用多次的情况。

   不完全背包问题的处理可以用2进制简化。也就是分别考虑1,2,4...个物品的情况，最后考虑$x-2^{[log_{2}x]}$个物品的情况（x为物品个数上限），这样一些数的组合就可以表达从1到x个物体的情况，在一些特定题目中是关键的避免超时的操作。

3. 动态规划（dp）

   动态规划的核心是状态转移方程，也就是找到一个推导的过程，按着写即可。其是一个从处理小问题逐渐解决问题的过程。

   经典的最长单调子序列

   ```python
   dp = [1]*n
   for i in range(1,n):
       for j in range(i):
           if A[j]<A[i]:
               dp[i] = max(dp[i],dp[j]+1)
   ans = sum(dp)
   ```

4. 深度优先搜索（DFS）&广度优先搜索（BFS）

   DFS是在每一个岔路口，依次沿着每一条路径走，走到头再回来，而BFS是在每一次操作后，记录所有的操作后结果，再等待下一步操作。DFS的一些问题需要回溯，也就是有一步路走错了要回头一步，同时是依次进行的，不会超内存。这是DFS的特点。但是DFS相当于是很强行的枚举，所以可能会导致时间复杂度较高，需要用缓存等方式进行处理。BFS的优势在于因为记录的是个数，所以在最短路径等问题中会有优势。

   一个简单的模型

   ```python
   def dfs(x):
       if ...:
           ...
           return
       ...
       ...
       dfs(x+1)
       
   ```

   ```python
   bfs:
   a = deque([...])
   while a:
       b = a.popleft()
       ...
       ...
       a.append(...)
   
   ```

   如果要进一步升级，就需要用到heapq（最小堆），或者是dijkstra，其是一种优化过后的bfs，优化体现在优先考虑最短的。同时不考虑已经被迭代删去的。

### 3.实战技巧

1. 看到题目后，一定要认真读题，了解题目的意思，如果题目比较容易计算，可以算一下样例，看一下原理。然后可以自己找一些极端一些的例子，看一下有没有什么特点。
2. 考虑用什么方法实现，注意题目强调需要完成的功能有哪些，在能够实现的方式中哪一种最方便，时间复杂度最低，以及会不会存在bug。如果题目有一些明确的方向，要注意在套模版的过程中有没有什么要调整、修改的地方。
3. 在完成后一定要调试代码。如果什么位置有问题，就可以通过显示中间结果的方式来辨别是在什么地方出现的问题。如果不能完全理解，就从代码实现的逻辑中一步步地排查，看有没有可能存在问题。







  

  







 















 











  

