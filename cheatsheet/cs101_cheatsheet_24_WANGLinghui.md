一、1、浅拷贝和深拷贝，二维数组需要深度拷贝：
        import copy
        A=copy.deepcopy(X)

    2、语法和函数
        *1、import math
            x = 3
            print(f"Square root of {x} is {math.sqrt(x):.2f}")
            得到Square root of 3 is 1.73， .2f表示保留两位小数
        *2、output = ' '.join(map(str,[1, 2, 3]))
            或者print（*lst）
            输出1 2 3
        *3、kk = int(binary_str, 2) 
           # 第一个参数是字符串类型的某进制数，第二个参数是进制，转化为整数
        *4、ord() # 字符转ASCII  chr() # ASCII转字符
        *5、print(bin(9)) #bin函数返回二进制，形式为0b1001
        *6、import itertools
            my_list = ['a', 'b', 'c']
            k1 = list(itertools.permutations(my_list))# [('a', 'b', 'c'),..]元素所有排列
            k2 = list(itertools.permutations(my_list, 2))# [('a', 'b'), ...]二元排列
            k3 = list(itertools.combinations(my_list, 2))# [('a', 'b'),...]二元组合
            k4 = list(itertools.product([0, 1], repeat=4))# [(0, 0, 0, 0)...],4个0或1的所有排列
        *7、import bisect #二分查找
            sorted_list = [1,3,5,7,9] #[(0)1, (1)3, (2)5, (3)7, (4)9]
            position = bisect.bisect_left(sorted_list, 6)
            print(position)  # 输出：3，因为6应该插入到位置3，才能保持列表的升序顺序
            bisect.insort_left(sorted_list, 6)
            print(sorted_list)#输出：[1, 3, 5, 6, 7, 9]，6被插入到适当的位置以保持升序顺序
        *8、排序intervals.sort(key=lambda x: x[1]，reverse = True)按数组第二个元素倒序排列
            对字典的键值对进行排序，与列表存储元组差不多
            d={3:34,2:23,9:33,10:33}
            dd=dict(sorted(d.items(),key=lambda x:(x[1],-x[0]))) #{2: 23, 10: 33, 9: 33, 3: 34}
        *9、import math
            print(math.ceil(1.5)) # 2
            print(math.pow(2,3)) # 8.0
            print(math.pow(2,2.5)) # 5.656854249492381
            print(9999999>math.inf) # False
            print(math.sqrt(4)) # 2.0
            print(math.log(100,10)) # 2.0  math.log(x,base) 以base为底，x的对数
            print(math.comb(5,3)) # 组合数，C53
            print(math.factorial(5)) # 5！
        *10、列表切片  lst[start:stop:step]，默认值为0， len（lst）， 1
            包含start对应元素，不包含stop对应元素
        *11、k = lst.index(a, m)
            k表示列表lst中a的位置，其中a在m之后

    3、数据结构
        *1、字典相关
            字典推导式 l = {key: value for key, value in my_dict.items() if value > 10}
            del my_dict['key1']  # 删除键为'key1'的键值对
            my_dict.pop('key2')  # 弹出键为'key2'的键值对，并返回其值
            my_dict.popitem()  # 弹出一个随机的键值对，并返回其值和键
        *2、import heapq # 优先队列可以实现以log复杂度拿出最小（大）元素
            lst=[1,2,3]
            heapq.heapify(lst) # 将lst优先队列化
            heapq.heappop(lst) # 从队列中弹出树顶元素（默认最小，相反数调转）
            heapq.heappush(lst,element) # 把元素压入堆中
        *3、from collections import deque

        *4、缓存最多储存k个最近的结果
            from functools import lru_cache
            @lru_cache(maxsize=k) #如果k设置为None，则缓存可以无限大
            

二、1、判断素数，欧拉筛                           2、二分查找
        def Euler_sieve(n):                         def binary_search(arr, target):
            primes = [True for _ in range(n+1)]         left, right = 0, len(arr) - 1 
            p = 2                                       while left <= right:
            while p*p <= n:                                mid = (left + right) // 2
                if primes[p]:                              if arr[mid] == target:
                    for i in range(p*p, n+1, p):               return mid返回目标元素索引
                        primes[i] = False                  elif arr[mid] < target:
                p += 1                                         left = mid + 1
            primes[0]=primes[1]=False                      else:
            return primes                                      right = mid - 1
                                                        return -1  # 无目标元素，返回 -1
    3、区间问题 （指针选取）
        *1、区间合并,比较左端点                   *2、选择不相交区间，比较右端点
        import sys                               def f(intervals):
        def merge(intervals):                        intervals.sort(key=lambda x: x[1])
            intervals.sort()                         res, ed = 0, -sys.maxsize
            res = []                                 for v in intervals:
            st, ed = -sys.maxsize, -sys.maxsize          if ed <= v[0]:
            for v in intervals:                              res += 1
                if ed == -sys.maxsize:                       ed = v[1]
                    st, ed = v[0], v[1]              return len(intervals) - res
                elif v[0] <= ed:                  #res是被移除的区间数量，端点相同算重复，
                    ed = max(v[1], ed)            所以是ed <= v[0]
                elif v[0] > ed:                   
                    res.append([st, ed])          *3、区间选点问题
                    st, ed = v[0], v[1]           与*2一致，每个不相交区间内至少有一个
            if ed != -sys.maxsize:                雷达问题
                res.append([st, ed])
            return res

        *4、区间覆盖问题，体育视频剪辑
        def videoStitching(clips, time):
            clips.sort()# 对 clips 按起点升序排序
            st, ed = 0, time
            res, i = 0, 0
            while i < len(clips) and st < ed:
                maxR = 0 # 找到所有起点小于等于 st 的片段，并记录这些片段的最大终点 maxR
                while i < len(clips) and clips[i][0] <= st:
                    maxR = max(maxR, clips[i][1])
                    i += 1
                if maxR <= st:# 无法继续覆盖
                    return -1
                st = maxR
                res += 1 # 更新 st 为 maxR，并增加结果计数
                if maxR >= ed:# 已经覆盖到终点
                    return res
            # 如果没有成功覆盖到终点
            return -1

        *5、区间分组问题，主持人主持
        import heapq
        def minmumNumberOfHost(n, startEnd): # 按左端点从小到大排序
            startEnd.sort(key=lambda x: x[0])
            q = []# 创建小顶堆
            for i in range(n):
                if not q or q[0] > startEnd[i][0]:
                    heapq.heappush(q, startEnd[i][1])
                else:
                    heapq.heappop(q)
                    heapq.heappush(q, startEnd[i][1])
            return len(q)

    4、归并排序
        def MergeSort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = MergeSort(arr[:mid])
            right = MergeSort(arr[mid:])
            return merge(left, right)

        def merge(left, right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

三、dp
    1、背包问题
        *1. **01背包** --> 每个物品只能拿一次
        def zero_one_bag():# V-总容量,n-物品个数,# cost=[0,     ],price=[0,     ]
            dp=[0]*(V+1)
            for i in range(1,n+1):           #每个物品
                for j in range(V,cost[i]-1,-1):    #逆向遍历每个容量
                    dp[j]=max(dp[j],price[i]+dp[j-cost[i]])
            return dp[-1]

        *2. **完全背包** --> 每个物品可以拿无限次
        def total_bag():
            dp=[0]*(V+1)
            for i in range(1,n+1):           #每个物品
                for j in range(1,cost[i]+1):       #正向遍历每个容量
                    dp[j]=max(dp[j],price[i]+dp[j-cost[i]])
            return dp[-1]

        *3. **多重背包** --> 每个物品的个数有限制,把每个物品的个数拆成1 2 4等转化为01背包
        def many_bag(): #s=[0,   ]为每个物品的个数
            dp=[0]*(V+1)
            for i in range(1,n+1):
                k=1
                while s[i]>0:
                    cnt=min(k,s[i])
                    for j in range(V,cnt*cost[i]-1,-1):
                        dp[j]=max(dp[j],cnt*price[i]+dp[j-cnt*cost[i]])
                    s[i]-=cnt
                    k*=2
            return dp[-1]
        
    2、整数分割问题
        *1. 把n划分为若干个正整数，不考虑顺序 --> 完全背包
        4：4=3+1=2+2=2+1+1=1+1+1+1 共5种
        def divide1(n):
            dp=[1]+[0]*n    #把0划分只有0这一种
            for i in range(1,n+1):           #每个数字
                for j in range(i,n+1):             #正向遍历每个容量（每个n）
                    dp[j]+=dp[j-i]
            return dp[-1]

        *2. 把n划分为若干个正整数，考虑顺序
        def divide2(n):
            dp=[1]+[0]*n
            for i in range(1,n+1):           #每个容量（每个n）
                for j in range(1,i+1):             #每个可能划分出的数字
                    dp[i]+=dp[i-j]
            return dp[-1]

        *3. 把n划分为若干个不同的正整数，不考虑顺序 --> 01背包
        4：4=3+1 共1种
        def divide3(n):
            dp=[1]+[0]*n
            for i in range(1,n+1):
                for j in range(n,i-1,-1):
                    dp[j]+=dp[j-i]
            return dp[-1]

        *4. 把n划分为k个正整数，不考虑顺序
        #dp[n][k]:把n分成k组
        def divide4(n,k):
            dp=[[0]*(k+1) for _ in range(n+1)]
            #每个数字分成1组都是1种
            for i in range(n+1):
                dp[i][1]=1
            for i in range(1,n+1):
                for j in range(2,k+1):
                    #i<j时无法划分
                    #i>=j时分为两种：若分组中有1，则为dp[i-1][j-1]
                    #若无1，先把每组放进去1，则为dp[i-j][j]
                    if i>=j:
                        dp[i][j]=dp[i-1][j-1]+dp[i-j][j]
            return dp[n][k] #dp[-1][-1]

    3、分类
        *1、核电站
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

        *2.回文
            def min_operations(s):
                n = len(s)
                dp = [[0]*n for _ in range(n)]
                for i in range(n-1, -1, -1):
                    for j in range(i+1, n):
                        if s[i] == s[j]:
                            dp[i][j] = dp[i+1][j-1]
                        else:
                            dp[i][j] = min(dp[i+1][j], dp[i][j-1], dp[i+1][j-1]) + 1
                return dp[0][n-1]

    4、单调递增或递减序列， Dilworth Theory
        最少单调链个数===最长反单调链长度
        找最长上升子序列的长度，用left
        找最长下降子序列，先reverse，再用left
        如果是不降，用right
        如果是不升，先reverse，再用right
        看题目要求的最终结果是否需要相同元素的考虑，需要考虑用left，不需要用right
        from bisect import bisect_left,bisect_right
        def d(s): #求最长上升子链长度
            lst=[]
            for i in s:
                pos=bisect_left(lst,i)
                if pos<len(lst):
                    lst[pos]=i
                else:
                    lst.append(i)
            return len(lst)

    4、双dp，红蓝玫瑰，一个是前n朵玫瑰全变红，记为Rn，一个是前n朵玫瑰全变蓝，记为Bn
        r=list(input())
        n=len(r)
        R=[0]*n
        B=[0]*n
        if r[0]=="R":R[0]=0;B[0]=1
        else:R[0]=1;B[0]=0
        for i in range(n-1):
            if r[i+1]=="R":
                R[i+1]=R[i]
                B[i+1]=min(R[i],B[i])+1
            else:
                R[i+1]=min(R[i],B[i])+1
                B[i+1]=B[i]
        print(R[-1])

四、DFS
    1、八皇后
        list1 = []
        def queen(s):
            if len(s) == 8:
                list1.append(s)
                return
            for i in range(1, 9):
                if all(str(i) != s[j] and abs(len(s) - j) != abs(i - int(s[j])) for j in range(len(s))):
                    queen(s + str(i))
        queen('')
        samples = int(input())
        for k in range(samples):
        print(list1[int(input()) - 1])

    2、最大连通域面积
        def dfs(matrix, row, col, visited):
            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) \
               or matrix[row][col] != 'W' or visited[row][col]:
                return 0
            visited[row][col] = True
            size = 1
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    size += dfs(matrix, row + dr, col + dc, visited)
            return size
        不用回溯，因为不连通的区域不会相交

    3、迷宫步数
        MAXN = 5
        n, m, k = map(int, input().split())
        maze = []
        for _ in range(n):
            row = list(map(int, input().split()))
            maze.append(row)
        visited = [[False for _ in range(m)] for _ in range(n)]
        canReach = False
        MAXD = 4
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < m and maze[x][y] == 0 and not visited[x][y]
        def DFS(x, y, step):
            global canReach
            if canReach:
                return
            if x == n - 1 and y == m - 1:
                if step == k:
                    canReach = True
                return
            visited[x][y] = True
            for i in range(MAXD):
                nextX = x + dx[i]
                nextY = y + dy[i]
                if step < k and is_valid(nextX, nextY):
                    DFS(nextX, nextY, step + 1)
            visited[x][y] = False
        DFS(0, 0, 0)
        print("Yes" if canReach else "No")

    4、最大权值路径
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右、下、左、上
        visited = [[False] * m for _ in range(n)]  # 标记访问
        max_path = []
        max_sum = -float('inf')  # 最大权值初始化为负无穷
        def dfs(x, y, current_path, current_sum):
            global max_path, max_sum
            if (x, y) == (n - 1, m - 1):
                if current_sum > max_sum:
                    max_sum = current_sum
                    max_path = current_path[:]
                return
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    visited[nx][ny] = True
                    current_path.append((nx, ny))
                    dfs(nx, ny, current_path, current_sum + maze[nx][ny])
                    current_path.pop()
                    visited[nx][ny] = False
        visited[0][0] = True
        dfs(0, 0, [(0, 0)], maze[0][0])

五、BFS
        1、模板
        from collections import deque
        def bfs(start, end):    
            q = deque([(0, start)])  # (step, start)
            in_queue = {start}
            while q:
                step, front = q.popleft() # 取出队首元素
                if front == end:
                    return step # 返回需要的结果，如：步长、路径等信息
        # 将 front 的下一层结点中未曾入队的结点全部入队q，并加入集合in_queue设置为已入队

        2、矩阵的块数
        def bfs(x, y):
            q = deque([(x, y)])
            inq_set.add((x,y))
            while q:
                front = q.popleft()
                for i in range(MAXD):
                    next_x = front[0] + dx[i]
                    next_y = front[1] + dy[i]
                    if matrix[next_x][next_y] == 1 and (next_x,next_y) not in inq_set:
                        inq_set.add((next_x, next_y))
                        q.append((next_x, next_y))
        inq_set = set()
        counter = 0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if matrix[i][j] == 1 and (i,j) not in inq_set:
                    bfs(i, j)
                    counter += 1

