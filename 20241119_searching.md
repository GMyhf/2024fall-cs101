# 20241119-Week11 搜索专题

Updated 2345 GMT+8 Nov 25 2024

2024 fall, Complied by Hongfei Yan



> Log:
>
> 2024/11/19 bfs示例代码尽量都在做优化：in_queue用集合实现，step也收到queue里面作为一个参数。这样与bfs模版就一致了。
>
> 2024/11/13 部分内容取自, https://github.com/GMyhf/2023fall-cs101/blob/main/searching_questions.md



## 0 Introduction

矩阵、迷宫和树都是图的特例。图搜索包括深度优先搜索（Depth First Search, DFS）和广度优先搜索（Breath First Search, BFS），是通过穷举法的思路来教电脑如何最有效地走迷宫。

在解决如何避免漏算或者陷入无限循环的问题时，DFS是从起点开始走，遇到分岔路进行标记，并沿着第一个分岔路继续前进；遇到死路则返回上一个分岔路口，选择下一个分叉路继续探寻，这样最终能够达到终点。这里使用了递归的概念，通过将“路口”、“分叉路”和“死路”等条件编写成代码，指导电脑走迷宫。这种一路走到底，撞到障碍才回头的方式称为深度优先搜索。BFS则是一种“探路型”走迷宫的策略，首先找到与入口相连的所有分叉路，然后逐一探寻这些分叉路所连接的分叉路，以此类推，直到找到出口位置。找出所有可能的分叉路，就称为广度优先搜索。如果搜索超时，可以考虑进行剪枝，以避免搜索不满足约束条件的路径。



当讨论图论时，矩阵、迷宫和树都是图的特例。

1. **矩阵**:
   - **说明**: 在图论中，矩阵通常指邻接矩阵或者关联矩阵，它们用于表示图的结构和连接关系。
   - **示例**: 例如，以下是一个简单的无向图的邻接矩阵表示：
   
   ```
       | 1 | 2 | 3 | 4 |
   ---------------------
     1 | 0 | 1 | 1 | 0 |
   ---------------------
     2 | 1 | 0 | 1 | 1 |
   ---------------------
     3 | 1 | 1 | 0 | 1 |
   ---------------------
     4 | 0 | 1 | 1 | 0 |
   ---------------------
   ```
   在这个邻接矩阵中，行和列代表图中的节点，相应的值表示节点之间的连接关系。

2. **迷宫**:
   - **说明**: 迷宫可以被视为一个特殊的图，其中包含了节点（代表迷宫的房间或位置）和边（代表可通行的路径）。
   - **示例**: 以下是一个简单的迷宫示例：
   
   ```
   ┌───┬───┬───┬───┐
   │S  │   │   │   │
   ├───┼───┼───┼───┤
   │   │██ │██ │   │
   ├───┼───┼───┼───┤
   │   │██ │   │██ │
   ├───┼───┼───┼───┤
   │   │   │   │E  │
   └───┴───┴───┴───┘
   ```
   在这个迷宫中，S代表起点，E代表终点，█代表墙壁，玩家需要在迷宫中寻找一条从起点到终点的路径。

3. **树**:
   - **说明**: 树是一种无环连通图，其中任意两个顶点间存在唯一路径。
   - **示例**: 以下是一个简单的树示例：

   ```
       1
      / \
     2   3
    / \  
   4   5
   ```
   这是一个简单的树，其中每个节点具有唯一的父节点（除了根节点），并且形成了一个无环的结构。



当讨论图论时，除了矩阵、迷宫和树，还有一些其他常见的图的特例，包括：

4. **完全图（Complete Graph）**：

- 完全图是指每一对不同的顶点之间都有一条边相连的图。
- 示例：如果一个图有 n 个顶点，并且每一对顶点之间都有一条边相连，那么这个图就是一个完全图，通常用 Kn 表示，其中 n 表示顶点的个数。

5. **二部图（Bipartite Graph）**：

- 二部图是指图的所有顶点可以被分成两个不相交的子集，使得同一个子集内的顶点不相连。
- 示例：下图就是一个简单的二部图，它的顶点可以被分成两个子集 {A, B, C} 和 {D, E, F}，使得同一个子集内的顶点不相连。

```
   A----D
   |    |
   B----E
   |    |
   C----F
```

6. **有向无环图（Directed Acyclic Graph，DAG）**：

- 有向无环图是指图中的边都是有方向的，并且不存在任何环路的图。
- 示例：许多调度和计划问题都可以建模为有向无环图，例如任务的依赖关系图。





《算法笔记》第8章

## 1 深度优先搜索(DFS)

设想我们现在以第一视角身处一个巨大的迷宫当中，没有上帝视角，没有通信设施，更没有热血动漫里的奇迹，有的只是四周长得一样的墙壁。于是，我们只能自己想办法走出去。如果迷失了内心，随便乱走，那么很可能被四周完全相同的景色绕晕在其中，这时只能放弃所谓的侥幸，而去采取下面这种看上去很盲目但实际上会很有效的方法。

以当前所在位置为起点，沿着一条路向前走，当碰到岔道口时，选择其中一个岔路前进如果选择的这个岔路前方是一条死路，就退回到这个岔道口，选择另一个岔路前进。如果岔路中存在新的岔道口，那么仍然按上面的方法枚举新岔道口的每一条岔路。这样，只要迷宫存在出口，那么这个方法一定能够找到它。可能有读者会问，如果在第一个岔道口处选择了一条没有出路的分支，而这个分支比较深，并且路上多次出现新的岔道口，那么当发现这个分支是个死分支之后，如何退回到最初的这个岔道口?其实方法很简单，只要让右手始终贴着右边的墙壁一路往前走，那么自动会执行上面这个走法，并且最终一定能找到出口。图 8-1 即为使用这个方法走一个简单迷宫的示例。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231126163735204.png" alt="image-20231126163735204" style="zoom:50%;" />



从图 8-1 可知，从起点开始前进，当碰到岔道口时，总是选择其中一条岔路前进(例如图中总是先选择最右手边的岔路)，在岔路上如果又遇到新的岔道口，仍然选择新岔道口的其中一条岔路前进，直到碰到死胡同才回退到最近的岔道口选择另一条岔路。也就是说，当碰到岔道口时，总是以“**深度**”作为前进的关键词，不碰到死胡同就不回头，因此把这种搜索的方式称为**深度优先搜索**(Depth First Search，**DFS**)。
从迷宫的例子还应该注意到，深度优先搜索会走遍所有路径，并且每次走到死胡同就代表一条完整路径的形成。这就是说，**深度优先搜索是一种枚举所有完整路径以遍历所有情况的搜索方法**。



深度优先搜索 (DFS)可以使用栈来实现。但是实现起来却并不轻松，有没有既容易理解又容易实现的方法呢?有的——递归。现在从 DFS 的角度来看当初求解 Fibonacci 数列的过程。
回顾一下 Fibonacci数列的定义: $F(0)=1,F(1)=1,F(n)=F(n-1)+F(n-2)(n≥2)$。可以从这个定义中挖掘到，每当将 F(n)分为两部分 F(n-1)与 F(n-2)时，就可以把 F(n)看作迷宫的岔道口，由它可以到达两个新的关键结点 F(n-1)与 F(n-2)。而之后计算 F(n-1)时，又可以把 F(n-1)当作在岔道口 F(n)之下的岔道口。
既然有岔道口，那么一定有死胡同。很容易想象，当访问到 F(0)和 F(1)时，就无法再向下递归下去，因此 F(0)和 F(1)就是死胡同。这样说来，==递归中的递归式就是岔道口，而递归边界就是死胡同==，这样就可以把如何用递归实现深度优先搜索的过程理解得很清楚。为了使上面的过程更清晰，可以直接来分析递归图 (见图 4-3)：可以在递归图中看到，只要n > 1，F(n)就有两个分支，即把 F(n)当作岔道口；而当n为1或0时，F(1)与F(0)就是迷宫的死胡同，在此处程序就需要返回结果。这样当遍历完所有路径（从顶端的 F(4)到底层的所有 F(1)与 F(0)）后，就可以得到 F(4)的值。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231126164549437.png" alt="image-20231126164549437" style="zoom: 50%;" />

因此，使用递归可以很好地实现深度优先搜索。这个说法并不是说深度优先搜索就是递归，只能说递归是深度优先搜索的一种实现方式，因为使用非递归也是可以实现 DFS 的思想的~~，但是一般情况下会比递归麻烦~~。不过，使用递归时，系统会调用一个叫系统栈的东西来存放递归中每一层的状态，因此使用递归来实现 DFS 的本质其实还是栈。



### 示例：sy313迷宫可行路径数 简单

https://sunnywhy.com/sfbj/8/1/313

现有一个 n*m 大小的迷宫，其中`1`表示不可通过的墙壁，`0`表示平地。每次移动只能向上下左右移动一格（不允许移动到曾经经过的位置），且只能移动到平地上。求从迷宫左上角到右下角的所有可行路径的条数。

**输入**

第一行两个整数 $n、m \hspace{1em} (2 \le n \le5, 2 \le m \le 5)$，分别表示迷宫的行数和列数；

接下来 n 行，每行 m 个整数（值为`0`或`1`），表示迷宫。

**输出**

一个整数，表示可行路径的条数。

样例1

输入

```
3 3
0 0 0
0 1 0
0 0 0
```

输出

```
2
```

解释

假设左上角坐标是(1,1)，行数增加的方向为增长的方向，列数增加的方向为增长的方向。

可以得到从左上角到右下角有两条路径：

1. (1,1)=>(1,2)=>(1,3)=>(2,3)=>(3,3)
2. (1,1)=>(2,1)=>(3,1)=>(3,2)=>(3,3)



#### 加保护圈，原地修改

```python
dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0, -1]

def dfs(maze, x, y):
    global cnt
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
            
        if maze[nx][ny] == 'e':
            cnt += 1
            continue
            
        if maze[nx][ny] == 0:
            maze[x][y] = 1
            dfs(maze, nx, ny)
            maze[x][y] = 0
    
    return
            
n, m = map(int, input().split())
maze = []
maze.append( [-1 for x in range(m+2)] )
for _ in range(n):
    maze.append([-1] + [int(_) for _ in input().split()] + [-1])
maze.append( [-1 for x in range(m+2)] )

maze[1][1] = 's'
maze[n][m] = 'e'

cnt = 0
dfs(maze, 1, 1)
print(cnt)
```



> OJ的pylint是静态检查，有时候报的编译错误Compile Error不对。解决方法有两种，如下：
> 1）第一行加# pylint: skip-file
> 2）方法二：如果函数内使用全局变量（变量类型是immutable，如int），则需要在程序最开始声明一下。如果是全局变量是list类型，则不受影响。



#### 辅助visited空间

```python
MAXN = 5
n, m = map(int, input().split())
maze = []
for _ in range(n):
    row = list(map(int, input().split()))
    maze.append(row)

visited = [[False for _ in range(m)] for _ in range(n)]
counter = 0

MAXD = 4
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m and maze[x][y] == 0 and not visited[x][y]

def DFS(x, y):
    global counter
    if x == n - 1 and y == m - 1:
        counter += 1
        return
    visited[x][y] = True
    for i in range(MAXD):
        nextX = x + dx[i]
        nextY = y + dy[i]
        if is_valid(nextX, nextY):
            DFS(nextX, nextY)
    visited[x][y] = False

DFS(0, 0)
print(counter)

```





### 示例：sy314指定步数的迷宫问题 中等

https://sunnywhy.com/sfbj/8/1/314

现有一个 n*m 大小的迷宫，其中`1`表示不可通过的墙壁，`0`表示平地。每次移动只能向上下左右移动一格（不允许移动到曾经经过的位置），且只能移动到平地上。现从迷宫左上角出发，问能否在恰好第步时到达右下角。

**输入**

第一行三个整数$n、m、k \hspace{1em} (2 \le n \le5, 2 \le m \le 5, 2 \le k \le n*m)$，分别表示迷宫的行数、列数、移动的步数；

接下来行，每行个整数（值为`0`或`1`），表示迷宫。

**输出**

如果可行，那么输出`Yes`，否则输出`No`。

样例1

输入

```
3 3 4
0 1 0
0 0 0
0 1 0
```

输出

```
Yes
```

解释

假设左上角坐标是(1,1)，行数增加的方向为增长的方向，列数增加的方向为增长的方向。

可以得到从左上角到右下角的步数为`4`的路径为：(1,1)=>(2,1)=>(2,2)=>(2,3)=>(3,3)。

样例2

输入

```
3 3 6
0 1 0
0 0 0
0 1 0
```

输出

```
No
```

解释

由于不能移动到曾经经过的位置，因此无法在恰好第`6`步时到达右下角。



#### 加保护圈，原地修改

```python
dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0, -1]

canReach = False
def dfs(maze, x, y, step):
    global canReach
    if canReach:
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if maze[nx][ny] == 'e':
            if step==k-1:
                canReach = True
                return
            
            continue
            
        if maze[nx][ny] == 0:
            if step < k:
                maze[x][y] = -1
                dfs(maze, nx, ny, step+1)
                maze[x][y] = 0
    

n, m, k = map(int, input().split())
maze = []
maze.append( [-1 for x in range(m+2)] )
for _ in range(n):
    maze.append([-1] + [int(_) for _ in input().split()] + [-1])
maze.append( [-1 for x in range(m+2)] )

maze[1][1] = 's'
maze[n][m] = 'e'

dfs(maze, 1, 1, 0)
print("Yes" if canReach else "No")
```



#### 辅助visited空间

```python
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

```





### 示例：sy315矩阵最大权值 中等

https://sunnywhy.com/sfbj/8/1/315

现有一个 n*m 大小的矩阵，矩阵中的每个元素表示该位置的权值。现需要从矩阵左上角出发到达右下角，每次移动只能向上下左右移动一格（不允许移动到曾经经过的位置）。求最后到达右下角时路径上所有位置的权值之和的最大值。

**输入**

第一行两个整数 $n、m \hspace{1em} (2 \le n \le5, 2 \le m \le 5)$，分别表示矩阵的行数和列数；

接下来 n 行，每行 m 个整数（$-100 \le 整数 \le 100$），表示矩阵每个位置的权值。

**输出**

一个整数，表示权值之和的最大值。

样例1

输入

```
2 2
1 2
3 4
```

输出

```
8
```

解释

从左上角到右下角的最大权值之和为。



#### 加保护圈，原地修改

```python
dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0, -1]

maxValue = float("-inf")
def dfs(maze, x, y, nowValue):
    global maxValue
    if x==n and y==m:
        if nowValue > maxValue:
            maxValue = nowValue
        
        return
  
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
  
        if maze[nx][ny] != -9999:
            tmp = maze[x][y]
            maze[x][y] = -9999
            nextValue = nowValue + maze[nx][ny]
            dfs(maze, nx, ny, nextValue)
            maze[x][y] = tmp
    

n, m = map(int, input().split())
maze = []
maze.append( [-9999 for x in range(m+2)] )
for _ in range(n):
    maze.append([-9999] + [int(_) for _ in input().split()] + [-9999])
maze.append( [-9999 for x in range(m+2)] )


dfs(maze, 1, 1, maze[1][1])
print(maxValue)
```



#### 辅助visited空间

```python
MAXN = 5
INF = float('inf')
n, m = map(int, input().split())
maze = []
for _ in range(n):
    row = list(map(int, input().split()))
    maze.append(row)

visited = [[False for _ in range(m)] for _ in range(n)]
maxValue = -INF

MAXD = 4
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m and not visited[x][y]

def DFS(x, y, nowValue):
    global maxValue
    if x == n - 1 and y == m - 1:
        if nowValue > maxValue:
            maxValue = nowValue
        return
    visited[x][y] = True
    for i in range(MAXD):
        nextX = x + dx[i]
        nextY = y + dy[i]
        if is_valid(nextX, nextY):
            nextValue = nowValue + maze[nextX][nextY]
            DFS(nextX, nextY, nextValue)
    visited[x][y] = False

DFS(0, 0, maze[0][0])
print(maxValue)

```



### 示例：sy316矩阵最大权值路径 中等

https://sunnywhy.com/sfbj/8/1/316

现有一个 n*m 大小的矩阵，矩阵中的每个元素表示该位置的权值。现需要从矩阵左上角出发到达右下角，每次移动只能向上下左右移动一格（不允许移动到曾经经过的位置）。假设左上角坐标是(1,1)，行数增加的方向为增长的方向，列数增加的方向为增长的方向。求最后到达右下角时路径上所有位置的权值之和最大的路径。

**输入**

第一行两个整数 $n、m \hspace{1em} (2 \le n \le5, 2 \le m \le 5)$，分别表示矩阵的行数和列数；

接下来 n 行，每行 m 个整数（$-100 \le 整数 \le 100$），表示矩阵每个位置的权值。

**输出**

从左上角的坐标开始，输出若干行（每行两个整数，表示一个坐标），直到右下角的坐标。

数据保证权值之和最大的路径存在且唯一。

样例1

输入

```
2 2
1 2
3 4
```

输出

```
1 1
2 1
2 2
```

解释

显然当路径是(1,1)=>(2,1)=>(2,2)时，权值之和最大，即 1+3+4 = 8。



样例2

输入

```
4 5
59 -62 -71 91 -12
-36 42 -32 -36 43
-68 -88 -94 -43 -39
48 -38 53 31 -92
```

输出

```
1 1
2 1
2 2
2 3
2 4
1 4
1 5
2 5
3 5
4 5
```



样例3

输入

```
3 4
-36 -10 -84 -28
12 94 95 22
61 -13 26 29
```

输出

```
1 1
1 2
2 2
2 1
3 1
3 2
3 3
2 3
2 4
3 4
```



**DFS辅助visited空间**

需要注意的地方是 current_path[:]那里，如果不用切片拷贝的话， max_path 会随着后续 current_path 改变，就会 WA。

max_path也需要global

理解为什么“回溯”这一步要把visited状态重新改回`False`，因为回溯顾名思义，实际上就是用另一种方法重走这一步，看看有没有其他的情况

```python
# 读取输入
n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]

# 定义方向
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右、下、左、上
visited = [[False] * m for _ in range(n)]  # 标记访问
max_path = []
max_sum = -float('inf')  # 最大权值初始化为负无穷

# 深度优先搜索
def dfs(x, y, current_path, current_sum):
    global max_path, max_sum

    # 到达终点，更新结果
    if (x, y) == (n - 1, m - 1):
        if current_sum > max_sum:
            max_sum = current_sum
            max_path = current_path[:]
        return

    # 遍历四个方向
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # 检查边界和是否访问过
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            # 标记访问
            visited[nx][ny] = True
            current_path.append((nx, ny))

            # 递归搜索
            dfs(nx, ny, current_path, current_sum + maze[nx][ny])

            # 回溯
            current_path.pop()
            visited[nx][ny] = False

# 初始化起点
visited[0][0] = True
dfs(0, 0, [(0, 0)], maze[0][0])

# 输出结果
for x, y in max_path:
    print(x + 1, y + 1)

```





### 示例：sy317迷宫最大权值 中等

https://sunnywhy.com/sfbj/8/1/317

题目描述

现有一个大小的迷宫，其中`1`表示不可通过的墙壁，`0`表示平地。现需要从迷宫左上角出发到达右下角，每次移动只能向上下左右移动一格（不允许移动到曾经经过的位置），且只能移动到平地上。假设迷宫中每个位置都有权值，求最后到达右下角时路径上所有位置的权值之和的最大值。

**输入**

第一行两个整数$n、m \hspace{1em} (2 \le n \le5, 2 \le m \le 5)$，分别表示矩阵的行数和列数；

接下来 n 行，每行个 m 整数（值为`0`或`1`），表示迷宫。

再接下来行，每行个整数（$-100 \le 整数 \le 100$），表示迷宫每个位置的权值。

**输出**

一个整数，表示权值之和的最大值。

样例1

输入

```
3 3
0 0 0
0 1 0
0 0 0
1 2 3
4 5 6
7 8 9
```

输出

```
29
```

解释：从左上角到右下角的最大权值之和为 1+4+7+8+9 = 29。



#### 加保护圈，原地修改

```python
dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0, -1]

maxValue = float("-inf")
def dfs(maze, x, y, nowValue):
    global maxValue
    if x==n and y==m:
        if nowValue > maxValue:
            maxValue = nowValue
        
        return
  
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
  
        if maze[nx][ny] == 0:
            maze[nx][ny] = -1
            tmp = w[x][y]
            w[x][y] = -9999
            nextValue = nowValue + w[nx][ny]
            dfs(maze, nx, ny, nextValue)
            maze[nx][ny] = 0
            w[x][y] = tmp
    

n, m = map(int, input().split())
maze = []
maze.append( [-1 for x in range(m+2)] )
for _ in range(n):
    maze.append([-1] + [int(_) for _ in input().split()] + [-1])
maze.append( [-1 for x in range(m+2)] )

w = []
w.append( [-9999 for x in range(m+2)] )
for _ in range(n):
    w.append([-9999] + [int(_) for _ in input().split()] + [-9999])
w.append( [-9999 for x in range(m+2)] )


dfs(maze, 1, 1, w[1][1])
print(maxValue)
```



#### 辅助visited空间

```python
MAXN = 5
INF = float('inf')
n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
w = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
maxValue = -INF

MAXD = 4
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m and not maze[x][y] and not visited[x][y]

def dfs(x, y, nowValue):
    global maxValue
    if x == n - 1 and y == m - 1:
        if nowValue > maxValue:
            maxValue = nowValue
        return
    visited[x][y] = True
    for i in range(MAXD):
        nextX = x + dx[i]
        nextY = y + dy[i]
        if is_valid(nextX, nextY):
            nextValue = nowValue + w[nextX][nextY]
            dfs(nextX, nextY, nextValue)
    visited[x][y] = False

dfs(0, 0, w[0][0])
print(maxValue)

```



### 练习: sy358受到祝福的平方 中等

https://sunnywhy.com/sfbj/8/3/539

在小元的世界里，任何人出生后会被世界分配一个随机`ID`，如果在被切割后，即`ID`满足按照从左至右顺序分割，且分割出来的数字都是某一个`正整数`的平方，分割时可以包括前导`0`，那么他就被这个世界祝福，最后获得快乐的数量和质量都比不满足这样的的人多的多。

令`ID`为`A`，且`A`是一个正整数，取值范围为$1 \le A \le 10^9$，问是否是一个被受到祝福的。

比如`A=8194`时，它是一个被受到祝福的`ID`，因为他可以被分割为$\{81,9,4\}=\{9^2,3^2,2^2\}$；

比如`A=1001`时，它是一个被受到祝福的`ID`，因为他可以被分割为$\{1,001\}=\{1^2,1^2\}$，或者$\{100,1\}=\{10^2,1^2\}$。注意$\{1,00,1\}=\{1^2,0^2,1^2\}$不是一个合法切割，因为分割出来的数字必须为正整数的平方；

比如`A=36`时，`36`已经是一个平方数了，所以它同样满足条件；

比如`A=54`，它不是一个被受到祝福的`ID`，因为他无法被切割为满足条件的集合。

**输入描述**

一个正整数A，无前导0。

其中$1 \le A \le 10^9$

**输出描述**

如果是一个满足题意的数字则输出`Yes`，否则`No`。



## 2 广度优先搜索(BFS)

前面介绍了深度优先搜索，可知 DFS 是以深度作为第一关键词的，即当碰到岔道口时总是先选择其中的一条岔路前进,而不管其他岔路,直到碰到死胡同时才返回岔道口并选择其他岔路。接下来将介绍的**广度优先搜索 (Breadth FirstSearch,BFS)**则是以广度为第一关键词，当碰到岔道口时,总是先依次访问从该岔道口能直接到达的所有结点,然后再按这些结点被访问的顺序去依次访问它们能直接到达的所有结点，以此类推,直到所有结点都被访问为止。这就跟平静的水面中投入一颗小石子一样,水花总是以石子落水处为中心,并以同心圆的方式向外扩散至整个水面(见图 8-2)，从这点来看和 DFS 那种沿着一条线前进的思路是完全不同的。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/202311262216546.png" alt="image-20231126221551540" style="zoom:50%;" />

广度优先搜索 (BFS)一般由队列实现,且总是按层次的顺序进行遍历，其基本写法如下(可作<mark>BFS模板</mark>用):

我们使用from collections import deque就满足要求，适用于需要频繁从队列的两端进行操作的场景，如广度优先搜索（BFS）、滑动窗口等问题。

> from queue import Queue适用于多线程编程中，需要在多个线程之间安全地共享和传递数据的场景。提供线程安全的特性，内置锁机制，可以在多线程环境中安全地使用。支持阻塞操作，如 `get` 和 `put` 方法可以设置超时时间，等待队列中有数据可用或空间可用。不支持从队列两端进行操作，只能从一端进行插入和删除。

```python
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

下面是对该模板中每一个步骤的说明,请结合代码一起看: 

① 定义队列 q，并将起点(0, start)入队，0表示步长目前是0。
② 写一个 while 循环，循环条件是队列q非空。
③ 在 while 循环中，先取出队首元素 front。
④ 将front 的下一层结点中所有**未曾入队**的结点入队，并标记它们的层号为 step 的层号加1，并加入集合in_queue设置为已入队。
⑤ 返回 ② 继续循环。



为了防止走回头路，一般可以设置一个set类型集合in_queue来记录每个位置是否在BFS中已入过队。再强调一点，在BFS 中设置的 in_queue 集合的含义是判断结点是否已入过队，而不是**结点是否已被访问**。区别在于：如果设置成是否已被访问，有可能在某个结点正在队列中（但还未访问）时由于其他结点可以到达它而将这个结点再次入队，导致很多结点反复入队，计算量大大增加。因此BFS 中让每个结点只入队一次，故需要设置 in_queue 集合的含义为**结点是否已入过队**而非结点是否已被访问。



### 示例：sy318数字操作（一维BFS）

https://sunnywhy.com/sfbj/8/2/318

从整数`1`开始，每轮操作可以选择将上轮结果加`1`或乘`2`。问至少需要多少轮操作才能达到指定整数。

输入描述

一个整数 $n \hspace{1em} (2 \le n \le 10^5)$，表示需要达到的整数。

输出描述

输出一个整数，表示至少需要的操作轮数。

样例1

输入

```
7
```

输出

```
4
```

解释

第`1`轮：1 + 1 = 2

第`2`轮：2 + 1 =3

第`3`轮：3 * 2 = 6

第`4`轮：6 + 1 = 7

因此至少需要操作`4`轮。



#### 数学思维

```python
'''
2023TA-陈威宇，思路：是n的二进制表示 里面 1的个数+1的个数+0的个数-2。
如果我们将 n 的二进制表示的每一位数从左到右依次编号为 0、1、2、...，那么：

1 的个数表示需要进行加 1 的操作次数；
0 的个数表示需要进行乘 2 的操作次数；
len(l) - 2 表示操作的总次数减去初始状态的操作次数 1，即剩余的操作次数；
sum(l) + len(l) - 2 表示所有操作次数之和。
'''
n = int(input())
s = bin(n)
l = [int(i) for i in s[2:]]
print(sum(l) + len(l) - 2)
```



#### 计算机思维

```python
from collections import deque


def bfs(n):
    inq = set()
    inq.add(1)
    q = deque()
    q.append((0, 1))
    while q:
        step, front = q.popleft()
        if front == n:
            return step

        if front * 2 <= n and front * 2 not in inq:
            inq.add(front * 2)
            q.append((step + 1, front * 2))
        if front + 1 <= n and front + 1 not in inq:
            inq.add(front + 1)
            q.append((step + 1, front + 1))


n = int(input())
print(bfs(n))


```





### 示例：sy319矩阵中的块

https://sunnywhy.com/sfbj/8/2/319

题目描述

现有一个 n*m 的矩阵，矩阵中的元素为`0`或`1`。然后进行如下定义：

1. 位置(x,y)与其上下左右四个位置 $(x,y + 1)、(x,y - 1)、(x + 1,y)、(x-1,y)$ 是相邻的；
2. 如果位置 (x1,y1) 与位置 (x2,y2) 相邻，且位置 (x2,y2) 与位置 (x3,y3) 相邻，那么称位置(x1,y1)与位置(x3,y3)也相邻；
3. 称个数尽可能多的相邻的`1`构成一个“块”。

求给定的矩阵中“块”的个数。

**输入**

第一行两个整数 n、m（$2 \le n \le 100, 2 \le m \le 100$），分别表示矩阵的行数和列数；

接下来 n 行，每行 m 个`0`或`1`（用空格隔开），表示矩阵中的所有元素。

**输出**

输出一个整数，表示矩阵中“块”的个数。

样例1

输入

```
6 7
0 1 1 1 0 0 1
0 0 1 0 0 0 0
0 0 0 0 1 0 0
0 0 0 1 1 1 0
1 1 1 0 1 0 0
1 1 1 1 0 0 0
```

输出

```
4
```

解释

矩阵中的`1`共有`4`块，如下图所示。

![矩阵中的块_样例.png](https://raw.githubusercontent.com/GMyhf/img/main/img/202311262246785.png)



#### 加保护圈，inq_set集合判断是否入过队

```python
from collections import deque

# Constants
MAXD = 4
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

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

# Input
n, m = map(int, input().split())
matrix=[[-1]*(m+2)]+[[-1]+list(map(int,input().split()))+[-1] for i in range(n)]+[[-1]*(m+2)]
inq_set = set()

# Main process
counter = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if matrix[i][j] == 1 and (i,j) not in inq_set:
            bfs(i, j)
            counter += 1

# Output
print(counter)
```



#### inq 数组，结点是否已入过队

```python
from collections import deque

# Constants
MAXN = 100
MAXD = 4
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# Functions
def can_visit(x, y):
    return 0 <= x < n and 0 <= y < m and matrix[x][y] == 1 and not in_queue[x][y]

def bfs(x, y):
    q = deque([(x, y)])
    in_queue[x][y] = True
    while q:
        front = q.popleft()
        for i in range(MAXD):
            next_x = front[0] + dx[i]
            next_y = front[1] + dy[i]
            if can_visit(next_x, next_y):
                in_queue[next_x][next_y] = True
                q.append((next_x, next_y))

# Input
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
in_queue = [[False] * MAXN for _ in range(MAXN)]

# Main process
counter = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and not in_queue[i][j]:
            bfs(i, j)
            counter += 1

# Output
print(counter)

```





### 示例：sy320迷宫问题

https://sunnywhy.com/sfbj/8/2/320

现有一个 n*m 大小的迷宫，其中`1`表示不可通过的墙壁，`0`表示平地。每次移动只能向上下左右移动一格，且只能移动到平地上。求从迷宫左上角到右下角的最小步数。

**输入**

第一行两个整数 $n、m \hspace{1em} (2 \le n \le 100, 2 \le m \le 100)$，分别表示迷宫的行数和列数；

接下来 n 行，每行 m 个整数（值为`0`或`1`），表示迷宫。

**输出**

输出一个整数，表示最小步数。如果无法到达，那么输出`-1`。

样例1

输入

```
3 3
0 1 0
0 0 0
0 1 0
```

输出

```
4
```

解释: 假设左上角坐标是(1,1)，行数增加的方向为增长的方向，列数增加的方向为增长的方向。

可以得到从左上角到右下角的前进路线：(1,1)=>(2,1)=>(2,2)=>(2,3)=>(3,3)。

因此最少需要`4`步。

样例2

输入

```
3 3
0 1 0
0 1 0
0 1 0
```

输出

```
-1
```

解释: 显然从左上角无法到达右下角。





#### 加保护圈，inq_set集合判断是否入过队

```python
from collections import deque

# 声明方向变化的数组，代表上下左右移动
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, n, m, maze):
    q = deque()
    q.append((0, (x, y)))  # (step, (x, y))
    inq_set = set()
    inq_set.add((x, y))
    
    while q:
        step, (cur_x, cur_y) = q.popleft()
        
        if cur_x == n and cur_y == m:
            return step
        
        for direction in range(4):
            next_x = cur_x + dx[direction]
            next_y = cur_y + dy[direction]
            
            if maze[next_x][next_y] == 0 and (next_x, next_y) not in inq_set:
                inq_set.add((next_x, next_y))
                q.append((step + 1, (next_x, next_y)))
    
    return -1

if __name__ == '__main__':
    n, m = map(int, input().split())
    
    # 初始化迷宫，增加边界
    maze = [[-1] * (m + 2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(n)] + [[-1] * (m + 2)]
    
    step = bfs(1, 1, n, m, maze)
    print(step)
```



#### inq 数组，结点是否已入过队

```python
from collections import deque

# 声明方向变化的数组，代表上下左右移动
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 检查是否可以访问位置 (x, y)
def can_visit(x, y):
    return 0 <= x < n and 0 <= y < m and maze[x][y] == 0 and not in_queue[x][y]

# BFS函数 实现广度优先搜索
def bfs(x, y):
    q = deque()
    q.append((0, (x, y)))
    in_queue[x][y] = True
    while q:
        for _ in range(len(q)):
            step, (cur_x, cur_y) = q.popleft()
            if cur_x == n - 1 and cur_y == m - 1:
                return step
            for direction in range(4):
                next_x = cur_x + dx[direction]
                next_y = cur_y + dy[direction]
                if can_visit(next_x, next_y):
                    in_queue[next_x][next_y] = True
                    q.append((step + 1, (next_x, next_y)))
    return -1

# 主函数
if __name__ == '__main__':
    # 读取 n 和 m
    n, m = map(int, input().split())
    maze = []
    in_queue = [[False] * m for _ in range(n)]

    # 填充迷宫和访问状态数组
    for i in range(n):
        maze.append(list(map(int, input().split())))

    # 执行BFS并输出步数
    step = bfs(0, 0)
    print(step)

```





### 示例：sy321迷宫最短路径

https://sunnywhy.com/sfbj/8/2/321

现有一个 n*m 大小的迷宫，其中`1`表示不可通过的墙壁，`0`表示平地。每次移动只能向上下左右移动一格，且只能移动到平地上。假设左上角坐标是(1,1)，行数增加的方向为增长的方向，列数增加的方向为增长的方向，求从迷宫左上角到右下角的最少步数的路径。

**输入**

第一行两个整数$n、m \hspace{1em} (2 \le n \le 100, 2 \le m \le 100)$，分别表示迷宫的行数和列数；

接下来 n 行，每行 m 个整数（值为`0`或`1`），表示迷宫。

**输出**

从左上角的坐标开始，输出若干行（每行两个整数，表示一个坐标），直到右下角的坐标。

数据保证最少步数的路径存在且唯一。

样例1

输入

```
3 3
0 1 0
0 0 0
0 1 0
```

输出

```
1 1
2 1
2 2
2 3
3 3
```

解释

假设左上角坐标是(1,)，行数增加的方向为增长的方向，列数增加的方向为增长的方向。

可以得到从左上角到右下角的最少步数的路径为：(1,1)=>(2,1)=>(2,2)=>(2,3)=>(3,3)。





```python
from collections import deque

# 声明方向变化的数组，代表上下左右移动
MAX_DIRECTIONS = 4
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def is_valid_move(x, y, n, m, maze, in_queue):
    return 0 <= x < n and 0 <= y < m and maze[x][y] == 0 and (x, y) not in in_queue

def bfs(start_x, start_y, n, m, maze):
    queue = deque()
    queue.append((start_x, start_y))
    
    in_queue = set()
    prev = [[(-1, -1)] * m for _ in range(n)]
    
    in_queue.add((start_x, start_y))
    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == m - 1:
            return prev
        for i in range(MAX_DIRECTIONS):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if is_valid_move(next_x, next_y, n, m, maze, in_queue):
                prev[next_x][next_y] = (x, y)
                in_queue.add((next_x, next_y))
                queue.append((next_x, next_y))
    return None

def print_path(prev, end_pos):
    path = []
    while end_pos != (-1, -1):
        path.append(end_pos)
        end_pos = prev[end_pos[0]][end_pos[1]]
    path.reverse()
    for pos in path:
        print(pos[0] + 1, pos[1] + 1)

if __name__ == '__main__':
    n, m = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(n)]
    
    prev = bfs(0, 0, n, m, maze)
    if prev:
        print_path(prev, (n - 1, m - 1))
    else:
        print("No path found")
```





### 示例：sy322跨步迷宫

https://sunnywhy.com/sfbj/8/2/322

现有一个n*m大小的迷宫，其中`1`表示不可通过的墙壁，`0`表示平地。每次移动只能向上下左右移动一格或两格（两格为同向），且只能移动到平地上（不允许跨越墙壁）。求从迷宫左上角到右下角的最小步数（假设移动两格时算作一步）。

**输入**

第一行两个整数 $n、m \hspace{1em} (2 \le n \le 100, 2 \le m \le 100)$，分别表示迷宫的行数和列数；

接下来n行，每行m个整数（值为`0`或`1`），表示迷宫。

**输出**

输出一个整数，表示最小步数。如果无法到达，那么输出`-1`。

样例1

输入

```
3 3
0 1 0
0 0 0
0 1 0
```

输出

```
3
```

解释

假设左上角坐标是，行数增加的方向为增长的方向，列数增加的方向为增长的方向。

可以得到从左上角到右下角的前进路线：=>=>=>。

因此最少需要`3`步。

样例2

输入

```
3 3
0 1 0
0 1 0
0 1 0
```

输出

```
-1
```

解释

显然从左上角无法到达右下角。





```python
from collections import deque

# 声明方向变化的数组，代表上下左右及四个斜向移动
MAXD = 8
dx = [0, 0, 0, 0, 1, -1, 2, -2]
dy = [1, -1, 2, -2, 0, 0, 0, 0]

def canVisit(x, y, n, m, maze, in_queue):
    return 0 <= x < n and 0 <= y < m and maze[x][y] == 0 and (x, y) not in in_queue

def bfs(start_x, start_y, n, m, maze):
    q = deque()
    q.append((0, start_x, start_y))  # (step, x, y)
    in_queue = {(start_x, start_y)}
    
    while q:
        step, x, y = q.popleft()
        
        if x == n - 1 and y == m - 1:
            return step
        
        for i in range(MAXD):
            next_x = x + dx[i]
            next_y = y + dy[i]
            next_half_x = x + dx[i] // 2
            next_half_y = y + dy[i] // 2
            
            if canVisit(next_x, next_y, n, m, maze, in_queue) and maze[next_half_x][next_half_y] == 0:
                in_queue.add((next_x, next_y))
                q.append((step + 1, next_x, next_y))
    
    return -1

if __name__ == '__main__':
    n, m = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(n)]
    
    step = bfs(0, 0, n, m, maze)
    print(step)
    
```



### 示例：sy323字符迷宫

https://sunnywhy.com/sfbj/8/2/323

现有一个n*m大小的迷宫，其中`*`表示不可通过的墙壁，`.`表示平地。每次移动只能向上下左右移动一格，且只能移动到平地上。求从起点`S`到终点`T`的最小步数。

**输入**

第一行两个整数 $n、m \hspace{1em} (2 \le n \le 100, 2 \le m \le 100)$，分别表示迷宫的行数和列数；

接下来n行，每行一个长度为m的字符串，表示迷宫。

**输出**

输出一个整数，表示最小步数。如果无法从`S`到达`T`，那么输出`-1`。

样例1

输入

```
5 5
.....
.*.*.
.*S*.
.***.
...T*
```

输出

```
11
```

解释

假设左上角坐标是，行数增加的方向为增长的方向，列数增加的方向为增长的方向。

起点的坐标为，终点的坐标为。

可以得到从`S`到`T`的前进路线：=>=>=>=>=>=>=>=>=>=>=>。

样例2

输入

复制

```
5 5
.....
.*.*.
.*S*.
.***.
..*T*
```

输出

```
-1
```

解释

显然终点`T`被墙壁包围，无法到达。





```python
from collections import deque

# 声明方向变化的数组，代表上下左右移动
MAXD = 4
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def canVisit(x, y, n, m, maze, in_queue):
    return 0 <= x < n and 0 <= y < m and maze[x][y] == 0 and (x, y) not in in_queue

def BFS(start, target, n, m, maze):
    q = deque([(0, start)])  # (step, (x, y))
    in_queue = {start}
    
    while q:
        step, (x, y) = q.popleft()
        
        if (x, y) == target:
            return step
        
        for i in range(MAXD):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if canVisit(next_x, next_y, n, m, maze, in_queue):
                in_queue.add((next_x, next_y))
                q.append((step + 1, (next_x, next_y)))
    
    return -1

if __name__ == '__main__':
    n, m = map(int, input().split())
    maze = []
    start, target = None, None
    
    for i in range(n):
        row = input().strip()
        maze_row = []
        for j in range(m):
            if row[j] == '.':
                maze_row.append(0)
            elif row[j] == '*':
                maze_row.append(1)
            elif row[j] == 'S':
                start = (i, j)
                maze_row.append(0)
            elif row[j] == 'T':
                target = (i, j)
                maze_row.append(0)
        maze.append(maze_row)
    
    if start is None or target is None:
        print(-1)
    else:
        step = BFS(start, target, n, m, maze)
        print(step)
```



### 示例：sy324多终点迷宫问题

https://sunnywhy.com/sfbj/8/2/324

现有一个 n*m 大小的迷宫，其中`1`表示不可通过的墙壁，`0`表示平地。每次移动只能向上下左右移动一格，且只能移动到平地上。求从迷宫左上角到迷宫中每个位置的最小步数。

**输入**

第一行两个整数  $n、m \hspace{1em} (2 \le n \le 100, 2 \le m \le 100)$，分别表示迷宫的行数和列数；

接下来n行，每行m个整数（值为`0`或`1`），表示迷宫。

**输出**

输出n行m列个整数，表示从左上角到迷宫中每个位置需要的最小步数。如果无法到达，那么输出`-1`。注意，整数之间用空格隔开，行末不允许有多余的空格。

样例1

输入

```
3 3
0 0 0
1 0 0
0 1 0
```

输出

```
0 1 2
-1 2 3
-1 -1 4
```

解释

假设左上角坐标是，行数增加的方向为增长的方向，列数增加的方向为增长的方向。

可以得到从左上角到所有点的前进路线：=>=>或=>=>。

左下角的三个位置无法到达。



```python
from collections import deque
import sys

INF = sys.maxsize
MAXD = 4

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def canVisit(x, y, n, m, maze, in_queue):
    return 0 <= x < n and 0 <= y < m and maze[x][y] == 0 and (x, y) not in in_queue

def BFS(start_x, start_y, n, m, maze):
    minStep = [[-1] * m for _ in range(n)]
    q = deque([(0, start_x, start_y)])  # (step, x, y)
    in_queue = {(start_x, start_y)}
    minStep[start_x][start_y] = 0
    
    while q:
        step, x, y = q.popleft()
        
        for i in range(MAXD):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if canVisit(next_x, next_y, n, m, maze, in_queue):
                in_queue.add((next_x, next_y))
                minStep[next_x][next_y] = step + 1
                q.append((step + 1, next_x, next_y))
    
    return minStep

n, m = map(int, input().split())
maze = []

for _ in range(n):
    maze.append(list(map(int, input().split())))

minStep = BFS(0, 0, n, m, maze)
for i in range(n):
    print(' '.join(map(str, minStep[i])))
```



### 示例：sy325迷宫问题-传送点

https://sunnywhy.com/sfbj/8/2/325

现有一个n*m大小的迷宫，其中`1`表示不可通过的墙壁，`0`表示平地，`2`表示传送点。每次移动只能向上下左右移动一格，且只能移动到平地或传送点上。当位于传送点时，可以选择传送到另一个`2`处（传送不计入步数），也可以选择不传送。求从迷宫左上角到右下角的最小步数。

**输入**

第一行两个整数$n、m \hspace{1em} (2 \le n \le 100, 2 \le m \le 100)$，分别表示迷宫的行数和列数；

接下来n行，每行m个整数（值为`0`或`1`或`2`），表示迷宫。数据保证有且只有两个`2`，且传送点不会在起始点出现。

**输出**

输出一个整数，表示最小步数。如果无法到达，那么输出`-1`。

样例1

输入

复制

```
3 3
0 1 2
0 1 0
2 1 0
```

输出

```
4
```

解释

假设左上角坐标是，行数增加的方向为增长的方向，列数增加的方向为增长的方向。

可以得到从左上角到右下角的前进路线：=>=>=>=>=>，其中=>属于传送，不计入步数。

因此最少需要`4`步。

样例2

输入

```
3 3
0 1 0
2 1 0
2 1 0
```

输出

```
-1
```

解释

显然从左上角无法到达右下角。



将 transVector 中的第一个位置映射到第二个位置，并将第二个位置映射到第一个位置。这样，就建立了传送门的双向映射关系。

在 BFS 函数中，当遇到传送门时，通过映射表 transMap 找到传送门的另一侧位置，并将其加入队列，以便继续进行搜索。

```python
from collections import deque

MAXD = 4

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def canVisit(x, y, n, m, maze, in_queue):
    return 0 <= x < n and 0 <= y < m and (maze[x][y] == 0 or maze[x][y] == 2) and (x, y) not in in_queue

def BFS(start_x, start_y, n, m, maze, transMap):
    q = deque([(0, start_x, start_y)])  # (step, x, y)
    in_queue = {(start_x, start_y)}

    while q:
        step, x, y = q.popleft()

        if x == n - 1 and y == m - 1:
            return step

        for i in range(MAXD):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if canVisit(next_x, next_y, n, m, maze, in_queue):
                in_queue.add((next_x, next_y))
                q.append((step + 1, next_x, next_y))

                if maze[next_x][next_y] == 2:
                    trans_position = transMap.get((next_x, next_y))
                    if trans_position:
                        in_queue.add(trans_position)
                        q.append((step + 1, trans_position[0], trans_position[1]))

    return -1

n, m = map(int, input().split())
maze = []
transMap = {}
transVector = []

for i in range(n):
    row = list(map(int, input().split()))
    maze.append(row)

    if 2 in row:
        for j, val in enumerate(row):
            if val == 2:
                transVector.append((i, j))

        if len(transVector) == 2:
            transMap[transVector[0]] = transVector[1]
            transMap[transVector[1]] = transVector[0]
            transVector = []  # 清空 transVector 以便处理下一对传送点

if transVector:
    print("Error: Unpaired teleportation point found.")
    exit(1)

step = BFS(0, 0, n, m, maze, transMap)
print(step)
```



### 示例：sy326中国象棋-马-无障碍

 https://sunnywhy.com/sfbj/8/2/326

现有一个n*m大小的棋盘，在棋盘的第行第列的位置放置了一个棋子，其他位置都未放置棋子。棋子的走位参照中国象棋的“马”。求该棋子到棋盘上每个位置的最小步数。

注：中国象棋中“马”的走位为“日”字形，如下图所示。

![image-20231213160152455](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231213160152455.png)

**输入**

四个整数$n、m、x、y \hspace{1em} (2 \le n \le 100, 2 \le m \le 100, 1 \le x \le n, 1\le y \le m)$，分别表示棋盘的行数和列数、棋子的所在位置。

**输出**

输出行列个整数，表示从棋子到棋盘上每个位置需要的最小步数。如果无法到达，那么输出`-1`。注意，整数之间用空格隔开，行末不允许有多余的空格。

样例1

输入

```
3 3 2 1
```

输出

```
3 2 1
0 -1 4
3 2 1
```

解释

共`3`行`3`列，“马”在第`2`行第`1`列的位置，由此可得“马”能够前进的路线如下图所示。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231213160421486.png" alt="image-20231213160421486" style="zoom:67%;" />





```python
from collections import deque

MAXD = 8

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def canVisit(x, y, n, m, in_queue):
    return 0 <= x < n and 0 <= y < m and (x, y) not in in_queue


def BFS(start_x, start_y, n, m):
    minStep = [[-1] * m for _ in range(n)]
    queue = deque([(0, start_x, start_y)])  # (step, x, y)
    in_queue = {(start_x, start_y)}
    minStep[start_x][start_y] = 0

    while queue:
        step, x, y = queue.popleft()

        for i in range(MAXD):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if canVisit(next_x, next_y, n, m, in_queue):
                in_queue.add((next_x, next_y))
                minStep[next_x][next_y] = step + 1
                queue.append((step + 1, next_x, next_y))

    return minStep


n, m, x, y = map(int, input().split())

minStep = BFS(x - 1, y - 1, n, m)
for row in minStep:
    print(' '.join(map(str, row)))
```



### 示例：sy327中国象棋-马-有障碍

https://sunnywhy.com/sfbj/8/2/327

现有一个大小的棋盘，在棋盘的第行第列的位置放置了一个棋子，其他位置中的一部分放置了障碍棋子。棋子的走位参照中国象棋的“马”（障碍棋子将成为“马脚”）。求该棋子到棋盘上每个位置的最小步数。

注`1`：中国象棋中“马”的走位为“日”字形，如下图所示。

![中国象棋-马-有障碍_题目描述1.png](https://raw.githubusercontent.com/GMyhf/img/main/img/405270a4-8a80-4837-891a-d0d05cc5577c.png)

注`2`：与“马”**直接相邻**的棋子会成为“马脚”，“马”不能往以“马”=>“马脚”为**长边**的方向前进，如下图所示。

![中国象棋-马-有障碍_题目描述2.png](https://raw.githubusercontent.com/GMyhf/img/main/img/0b79f8a0-7b3e-4675-899c-b44e86ee5e40.png)

**输入**

第一行四个整数$n、m、x、y \hspace{1em} (2 \le n \le 100, 2 \le m \le 100, 1 \le x \le n, 1\le y \le m)$，分别表示棋盘的行数和列数、棋子的所在位置；

第二行一个整数$k（1 \le k \le 10）$，表示障碍棋子的个数；

接下来k行，每行两个整数$x_i、y_i（1 \le x_i \le n, 1 \le y_i \le m）$，表示第i个障碍棋子的所在位置。数据保证不存在相同位置的障碍棋子。

**输出**

输出n行m列个整数，表示从棋子到棋盘上每个位置需要的最小步数。如果无法到达，那么输出`-1`。注意，整数之间用空格隔开，行末不允许有多余的空格。

样例1

输入

```
3 3 2 1
1
1 2
```

输出

```
3 -1 1
0 -1 -1
-1 2 1
```

解释

共`3`行`3`列，“马”在第`2`行第`1`列的位置，障碍棋子在第`1`行第`2`列的位置，由此可得“马”能够前进的路线如下图所示。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/f005a3c6-b042-471b-b10f-26daf7ff97fb.png" alt="中国象棋-马-有障碍_样例.png" style="zoom:67%;" />





<img src="/Users/hfyan/Library/Application Support/typora-user-images/image-20240525200326139.png" alt="image-20240525200326139" style="zoom: 50%;" />

```python
from collections import deque

MAXD = 8
dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [1, -1, -2, -2, -1, 1, 2, 2]


def canVisit(x, y):
    return 0 <= x < n and 0 <= y < m and (x, y) not in isBlock and (x, y) not in in_queue


def BFS(start_x, start_y):
    minStep = [[-1] * m for _ in range(n)]
    queue = deque([(0, start_x, start_y)])  # (step, x, y)
    in_queue.add((start_x, start_y))
    minStep[start_x][start_y] = 0

    while queue:
        step, x, y = queue.popleft()

        wx, wy = [-1, 0, 1, 0], [0, -1, 0, 1]
        for i in range(MAXD):
            nextX = x + dx[i]
            nextY = y + dy[i]
            footX, footY = x + wx[i//2], y + wy[i//2]

            if canVisit(nextX, nextY) and (footX, footY) not in isBlock:
                in_queue.add((nextX, nextY))
                minStep[nextX][nextY] = step + 1
                queue.append((step + 1, nextX, nextY))

    return minStep


n, m, x, y = map(int, input().split())
in_queue = set()
isBlock = {}

k = int(input())
for _ in range(k):
    blockX, blockY = map(int, input().split())
    isBlock[(blockX - 1, blockY - 1)] = True

minStep = BFS(x - 1, y - 1)

for row in minStep:
    print(' '.join(map(str, row)))
```





## 3 相关题目

### 02287: Tian Ji -- The Horse Racing

greedy, http://cs101.openjudge.cn/practice/02287

Here is a famous story in Chinese history.

That was about 2300 years ago. General Tian Ji was a high official in the country Qi. He likes to play horse racing with the king and others.

Both of Tian and the king have three horses in different classes, namely, regular, plus, and super. The rule is to have three rounds in a match; each of the horses must be used in one round. The winner of a single round takes two hundred silver dollars from the loser.

Being the most powerful man in the country, the king has so nice horses that in each class his horse is better than Tian's. As a result, each time the king takes six hundred silver dollars from Tian.

Tian Ji was not happy about that, until he met Sun Bin, one of the most famous generals in Chinese history. Using a little trick due to Sun, Tian Ji brought home two hundred silver dollars and such a grace in the next match.

It was a rather simple trick. Using his regular class horse race against the super class from the king, they will certainly lose that round. But then his plus beat the king's regular, and his super beat the king's plus. What a simple trick. And how do you think of Tian Ji, the high ranked official in China?

![img](https://raw.githubusercontent.com/GMyhf/img/main/img/2287_1.jpg)



Were Tian Ji lives in nowadays, he will certainly laugh at himself. Even more, were he sitting in the ACM contest right now, he may discover that the horse racing problem can be simply viewed as finding the maximum matching in a bipartite graph. Draw Tian's horses on one side, and the king's horses on the other. Whenever one of Tian's horses can beat one from the king, we draw an edge between them, meaning we wish to establish this pair. Then, the problem of winning as many rounds as possible is just to find the maximum matching in this graph. If there are ties, the problem becomes more complicated, he needs to assign weights 0, 1, or -1 to all the possible edges, and find a maximum weighted perfect matching...

However, the horse racing problem is a very special case of bipartite matching. The graph is decided by the speed of the horses -- a vertex of higher speed always beat a vertex of lower speed. In this case, the weighted bipartite matching algorithm is a too advanced tool to deal with the problem.

In this problem, you are asked to write a program to solve this special case of matching problem.

**输入**

The input consists of up to 50 test cases. Each case starts with a positive integer n ( n<=1000) on the first line, which is the number of horses on each side. The next n integers on the second line are the speeds of Tian's horses. Then the next n integers on the third line are the speeds of the king's horses. The input ends with a line that has a single `0' after the last test case.

**输出**

For each input case, output a line containing a single number, which is the maximum money Tian Ji will get, in silver dollars.

样例输入

```
3
92 83 71
95 87 74
2
20 20
20 20
2
20 19
22 18
0
```

样例输出

```
200
0
0
```

来源：Shanghai 2004



dfs

```python
# 赵时阳-数院23

from functools import lru_cache
import sys
sys.setrecursionlimit(1 << 30)


def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

while True:
    n = int(input())
    if n == 0: 
        break

    tian_values = list(map(int, input().split()))
    king_values = list(map(int, input().split()))
    tian_values.sort()
    king_values.sort()

    @lru_cache(maxsize=2048)
    def dfs(start, end, i):
        if i < n:
            tian_value = tian_values[i]
            king_value_start = king_values[start]
            x1 = dfs(start + 1, end, i + 1) + compare(tian_value, king_value_start)
            
            king_value_end = king_values[end]
            x2 = dfs(start, end - 1, i + 1) + compare(tian_value, king_value_end)  
            x = max(x1, x2)
            return x
        else:
            return 0

    result = dfs(0, n - 1, 0)
    print(200 * result)

```





### 20140: 今日化学论文

http://cs101.openjudge.cn/practice/20140/

常凯申同学发现自己今日化学论文字数抄上限了，决定采取如下的压缩方法萌混过关：

把连续的x个字符串s记为[xs]。(1 <= x <= 100)

但这样的方法当然骗不过lwh老师啦。老师非常生气，但出于好奇，还是想看一看常凯申同学写了什么。
请你帮老师还原出原始的论文。

**输入**

仅一行，由小写英文字母、数字和[]组成的字符串（其中不含空格）

**输出**

一行，原始的字符串。

样例输入

```
[2b[3a]c]
```

样例输出

```
baaacbaaac
```

来源: cs101-2019 柏敬尧v0.2



本地调试可以用sys.stderr.write(checkpoint)。如果精神不集中写程序太难受了，调试的print忘记注释造成WA，会耽误很久。

递归实现，避免使用全局变量。

```python
import sys

def recursive_decode(s, idx):
    stack = []
    numstr = ""

    while idx < len(s):
        sys.stderr.write(s)
        sys.stderr.write(s[idx])
        if s[idx] == "[":
            decoded_str, next_idx = recursive_decode(s, idx + 1)
            stack.extend(decoded_str)
            idx = next_idx
        elif s[idx] == "]":
            num = int(numstr)
            return stack * num, idx
        elif s[idx].isdigit():
            numstr += s[idx]
        else:
            stack.append(s[idx])
        idx += 1

    return stack, idx


s = input()
#s = "[2b[3a]c]"
decoded_str, _ = recursive_decode(s, 0)
print(*decoded_str, sep="")
```



### 27217: 有多少种合法的出栈顺序

http://cs101.openjudge.cn/practice/27217/

栈是计算机中经典的数据结构，简单的说，栈就是限制在一端进行插入删除操作的线性表。栈有两种最重要的操作，即 pop（从栈顶弹出一个元素）和 push（将一个元素进栈）。栈的重要性不言自明，任何一门数据结构的课程都会介绍栈。宁宁同学在复习栈的基本概念时，想到了一个书上没有讲过的问题，而他自己无法给出答案，所以需要你的帮忙。![img](http://media.openjudge.cn/images/upload/1576/1701440958.jpg)宁宁考虑的是这样一个问题：一个操作数序列，1,2,...,n（图示为 1 到 3 的情况），栈 A 的深度大于 n。现在可以进行两种操作，将一个数，从操作数序列的头端移到栈的头端（对应数据结构栈的 push 操作）将一个数，从栈的头端移到输出序列的尾端（对应数据结构栈的 pop 操作）使用这两种操作，由一个操作数序列就可以得到一系列的输出序列，下图所示为由 `1 2 3` 生成序列 `2 3 1`的过程。![img](http://media.openjudge.cn/images/upload/4265/1701441123.jpg)（原始状态如上图所示）你的程序将对给定的 n，计算并输出由操作数序列 1,2,...,n 经过操作可能得到的输出序列的总数。

**输入**

输入文件只含一个整数 n（1 <= n <= 1000）。

**输出**

输出文件只有一行，即可能输出序列的总数目。

样例输入

`3`

样例输出

`5`

来源：洛谷 1044



```python
'''
递归/记忆化搜索，https://www.luogu.com.cn/problem/solution/P1044
1）二维数组f[i,j]，用下标 i 表示队列里还有几个待排的数，j 表示栈里有 j 个数，
f[i,j]表示此时的情况数
2）那么，更加自然的，只要f[i,j]有值就直接返回；
3）然后递归如何实现呢？首先，可以想到，要是数全在栈里了，就只剩1种情况了，所以：i=0时，返回1；
4）然后，有两种情况：一种栈空，一种栈不空：在栈空时，我们不可以弹出栈里的元素，只能进入，
所以队列里的数−1，栈里的数+1，即加上 f[i−1,j+1] ；另一种是栈不空，
那么此时有出栈1个或者进1个再出1个 2种情况，分别加上 f[i−1,j+1] 和 f[i,j−1] 
'''
import sys
sys.setrecursionlimit(1<<30)

def dfs(i, j, f):
    if f[i][j] != -1:
        return f[i][j]
    
    if i == 0:
        f[i][j] = 1
        return 1
    
    if j == 0:
        f[i][j] = dfs(i - 1, j + 1, f)
        return f[i][j]
    
    f[i][j] = dfs(i - 1, j + 1, f) + dfs(i, j - 1, f)
    return f[i][j]

n = int(input())
f = [[-1] * (n + 1) for _ in range(n + 1)]

result = dfs(n, 0, f)
print(result)
```



### 20123: 7-友好数

brute force, math, dfs similar, http://cs101.openjudge.cn/practice/20123/

黑板上写了一个正整数N，其首位不为0，位数不超过10^5。

N被称为7-友好数，如果可以擦掉若干位，使得剩下的数字构成的数为7的倍数。

要求不能擦掉所有数字，但允许只剩下一个数字0。

请你编写程序，判断N是不是7-友好数。

**输入**

一个正整数N，其位数 ≤ 10^5。

**输出**

如果N是7-友好数，那么输出YES ； 否则输出 NO

样例输入

```
输入样例1：
123364315

输出样例1：
YES

解释：可以使得剩下的数为35，因此满足要求。
```

样例输出

```
输入样例2：
31116

输出样例2：
NO
```

来源：cs101-2019 金及凯



```python
#20123:7-友好数，http://cs101.openjudge.cn/practice/20123/
#
# 陈威宇：>=7位就一定YES了，因为所有后缀%7有两个相等的（抽屉原理），
# 取这两个后缀里长的那个去掉短的那个即可？
'''
通过递归地尝试不同的子串来寻找符合条件的解.
`dfs(n, i)` 函数是进行深度优先搜索的核心部分。它接受两个参数：`n`代表当前搜索到的子串，
`i`代表当前处理到的位置索引。在函数内部，通过不断拼接字符来生成不同的子串，
然后检查是否满足能够被7整除的条件。

'''
def dfs(n, i):
    global bo
    if len(n) > 0 and int(n) % 7 == 0:
        bo = True
    if bo:
        return
    if i >= l:
        return
    dfs(n, i+1)
    dfs(n+s[i], i+1)


s = input()
l = len(s)
if l >= 7:
    print('YES')
    exit()
bo = False
dfs('', 0)
if bo:
    print('YES')
else:
    print('NO')

```





### 550C. Divisibility by Eight

Brute force, dp, math, 1500, https://codeforces.com/contest/550/problem/C

You are given a non-negative integer *n*, its decimal representation consists of at most 100 digits and doesn't contain leading zeroes.

Your task is to determine if it is possible in this case to remove some of the digits (possibly not remove any digit at all) so that the result contains at least one digit, forms a non-negative integer, doesn't have leading zeroes and is divisible by 8. After the removing, it is forbidden to rearrange the digits.

If a solution exists, you should print it.

**Input**

The single line of the input contains a non-negative integer *n*. The representation of number *n* doesn't contain any leading zeroes and its length doesn't exceed 100 digits.

**Output**

Print "NO" (without quotes), if there is no such way to remove some digits from number *n*.

Otherwise, print "YES" in the first line and the resulting number after removing digits from number *n* in the second line. The printed number must be divisible by 8.

If there are multiple possible answers, you may print any of them.

Examples

input

```
3454
```

output

```
YES
344
```

input

```
10
```

output

```
YES
0
```

input

```
111111
```

output

```
NO
```



记忆式搜索，20-21行是分叉。

```python
'''
应该递归后三位，而不是所有的位数。因为
A number is divisible by 8 if its last three digits are also divisible by 8
'''
from functools import lru_cache

@lru_cache(maxsize=None)
def dfs(n, i, depth):
    global bo, result
    if depth > 3 or bo:
        return
    if len(n) > 0 and int(n) % 8 == 0:
        result = n
        bo = True
        return
    if bo:
        return
    if i >= l:
        return
    dfs(n, i+1, depth)
    dfs(n+s[i], i+1, depth+1)


s = input()
l = len(s)
bo = False
result = ""
dfs('', 0, 0)
if bo:
    print('YES\n', result)
else:
    print('NO')
```



### 1843D. Apple Tree

Combinatorics, dfs and similar, dp, math, trees, *1200

https://codeforces.com/problemset/problem/1843/D

Timofey has an apple tree growing in his garden; it is a rooted tree of 𝑛 vertices with the root in vertex 1 (the vertices are numbered from 1 to 𝑛). A tree is a connected graph without loops and multiple edges.

This tree is very unusual — it grows with its root upwards. However, it's quite normal for programmer's trees.

The apple tree is quite young, so only two apples will grow on it. Apples will grow in certain vertices (these vertices may be the same). After the apples grow, Timofey starts shaking the apple tree until the apples fall. Each time Timofey shakes the apple tree, the following happens to each of the apples:

Let the apple now be at vertex 𝑢.

- If a vertex 𝑢 has a child, the apple moves to it (if there are several such vertices, the apple can move to any of them).
- Otherwise, the apple falls from the tree.

It can be shown that after a finite time, both apples will fall from the tree.

Timofey has 𝑞 assumptions in which vertices apples can grow. He assumes that apples can grow in vertices 𝑥 and 𝑦, and wants to know the number of pairs of vertices (𝑎, 𝑏) from which apples can fall from the tree, where 𝑎 — the vertex from which an apple from vertex 𝑥 will fall, 𝑏 — the vertex from which an apple from vertex 𝑦 will fall. Help him do this.

**Input**

The first line contains integer 𝑡 (1≤𝑡≤10^4^) — the number of test cases.

The first line of each test case contains integer 𝑛 (2≤𝑛≤2⋅10^5^) — the number of vertices in the tree.

Then there are 𝑛−1 lines describing the tree. In line 𝑖 there are two integers 𝑢𝑖 and 𝑣𝑖 (1≤𝑢𝑖,𝑣𝑖≤𝑛, 𝑢𝑖≠𝑣𝑖) — edge in tree.

The next line contains a single integer 𝑞 (1≤𝑞≤2⋅10^5^) — the number of Timofey's assumptions.

Each of the next 𝑞 lines contains two integers 𝑥𝑖 and 𝑦𝑖 (1≤𝑥𝑖,𝑦𝑖≤𝑛) — the supposed vertices on which the apples will grow for the assumption .

It is guaranteed that the sum of  𝑛 does not exceed 2⋅10^5^. Similarly, It is guaranteed that the sum of 𝑞 does not exceed 2⋅10^5^.

**Output**

For each Timofey's assumption output the number of ordered pairs of vertices from which apples can fall from the tree if the assumption is true on a separate line.

Examples

input

```
2
5
1 2
3 4
5 3
3 2
4
3 4
5 1
4 4
1 3
3
1 2
1 3
3
1 1
2 3
3 1
```

output

```
2
2
1
4
4
1
2
```

input

```
2
5
5 1
1 2
2 3
4 3
2
5 5
5 1
5
3 2
5 3
2 1
4 2
3
4 3
2 1
4 2
```

output

```
1
2
1
4
2
```

Note

In the first example:

- For the first assumption, there are two possible pairs of vertices from which apples can fall from the tree: (4,4),(5,4)(4,4),(5,4).
- For the second assumption there are also two pairs: (5,4),(5,5)(5,4),(5,5).
- For the third assumption there is only one pair: (4,4)(4,4).
- For the fourth assumption, there are 44 pairs: (4,4),(4,5),(5,4),(5,5)(4,4),(4,5),(5,4),(5,5).

![img](https://espresso.codeforces.com/7c6d16e8362e76df883e925d30296fb28360d590.png)Tree from the first example.

For the second example, there are 44 of possible pairs of vertices from which apples can fall: (2,3),(2,2),(3,2),(3,3)(2,3),(2,2),(3,2),(3,3). For the second assumption, there is only one possible pair: (2,3)(2,3). For the third assumption, there are two pairs: (3,2),(3,3)(3,2),(3,3).



蒋子轩23工学院 清晰明了的程序，custom stack.

```python
def build_tree(edges):
    tree = {}
    for edge in edges:
        u, v = edge
        tree.setdefault(u, []).append(v)
        tree.setdefault(v, []).append(u)
    return tree

def count_leaves(tree, leaves_count):
    stack = [(1, 0, 0)] # 节点，阶段标志，父节点
    while stack:
        vertex, stage, parent = stack.pop()
        
        if stage == 0:
            stack.append((vertex, 1, parent))
            for child in tree[vertex]:
                if child != parent:
                    stack.append((child, 0, vertex))
        else:
            if len(tree[vertex]) == 1 and vertex != 1:
                leaves_count[vertex] = 1
            else:               
                child_count = 0
                for child in tree[vertex]:
                    if child != parent:
                        child_count += leaves_count[child]

                leaves_count[vertex] = child_count  # 当前节点的叶子节点数等于其子节点的叶子节点数之和

def process_assumptions(tree, leaves_count, assumptions):
    for x, y in assumptions:
        result = leaves_count[x] * leaves_count[y]
        print(result)

t = int(input())
for _ in range(t):
    n = int(input())
    edges = []
    for _ in range(n - 1):
        edges.append(tuple(map(int, input().split())))

    tree = build_tree(edges)
    leaves_count = {node: 0 for node in range(1, n + 1)}
    count_leaves(tree, leaves_count)  
    # print(tree, leaves_count)
    q = int(input())
    assumptions = []
    for _ in range(q):
        assumptions.append(tuple(map(int, input().split())))

    process_assumptions(tree, leaves_count, assumptions)

```

 

蒋子轩23工学院 清晰明了的程序，dfs with thread.

```python
import sys
import threading
sys.setrecursionlimit(1 << 30)
threading.stack_size(2*10**8)


def main():
    def build_tree(edges):
        tree = {}
        for edge in edges:
            u, v = edge
            tree.setdefault(u, []).append(v)
            tree.setdefault(v, []).append(u)
        return tree

    def count_leaves(tree, vertex, parent, leaves_count):
        child_count = 0
        for child in tree[vertex]:
            if child != parent:
                child_count += count_leaves(tree, child, vertex, leaves_count)
        #if len(tree[vertex]) == 1 and vertex != parent:  # 当前节点是叶子节点
        if len(tree[vertex]) == 1 and vertex != 1:
            leaves_count[vertex] = 1
            return 1
        leaves_count[vertex] = child_count  # 当前节点的叶子节点数等于其子节点的叶子节点数之和
        return leaves_count[vertex]

    def process_assumptions(tree, leaves_count, assumptions):
        for x, y in assumptions:
            result = leaves_count[x] * leaves_count[y]
            print(result)

    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = []
        for _ in range(n - 1):
            edges.append(tuple(map(int, input().split())))

        tree = build_tree(edges)
        leaves_count = {node: 0 for node in range(1, n + 1)}
        count_leaves(tree, 1, 0, leaves_count)  # 从根节点开始遍历计算叶子节点数量
        #print(tree, leaves_count)
        q = int(input())
        assumptions = []
        for _ in range(q):
            assumptions.append(tuple(map(int, input().split())))

        process_assumptions(tree, leaves_count, assumptions)


thread = threading.Thread(target=main)
thread.start()
thread.join()
```



### 02754: 八皇后

dfs and similar, http://cs101.openjudge.cn/practice/02754

描述：会下国际象棋的人都很清楚：皇后可以在横、竖、斜线上不限步数地吃掉其他棋子。如何将8个皇后放在棋盘上（有8 * 8个方格），使它们谁也不能被吃掉！这就是著名的八皇后问题。
对于某个满足要求的8皇后的摆放方法，定义一个皇后串a与之对应，即$a=b_1b_2...b_8~$,其中$b_i$为相应摆法中第i行皇后所处的列数。已经知道8皇后问题一共有92组解（即92个不同的皇后串）。
给出一个数b，要求输出第b个串。串的比较是这样的：皇后串x置于皇后串y之前，当且仅当将x视为整数时比y小。

八皇后是一个古老的经典问题：**如何在一张国际象棋的棋盘上，摆放8个皇后，使其任意两个皇后互相不受攻击。**该问题由一位德国**国际象棋排局家** **Max Bezzel** 于 1848年提出。严格来说，那个年代，还没有“德国”这个国家，彼时称作“普鲁士”。1850年，**Franz Nauck** 给出了第一个解，并将其扩展成了“ **n皇后** ”问题，即**在一张 n** x **n 的棋盘上，如何摆放 n 个皇后，使其两两互不攻击**。历史上，八皇后问题曾惊动过“数学王子”高斯(Gauss)，而且正是 Franz Nauck 写信找高斯请教的。





### 02773: 采药

dp, http://cs101.openjudge.cn/practice/02773

辰辰是个很有潜能、天资聪颖的孩子，他的梦想是称为世界上最伟大的医师。为此，他想拜附近最有威望的医师为师。医师为了判断他的资质，给他出了一个难题。医师把他带到个到处都是草药的山洞里对他说：“孩子，这个山洞里有一些不同的草药，采每一株都需要一些时间，每一株也有它自身的价值。我会给你一段时间，在这段时间里，你可以采到一些草药。如果你是一个聪明的孩子，你应该可以让采到的草药的总价值最大。”

如果你是辰辰，你能完成这个任务吗？

**输入**

输入的第一行有两个整数T（1 <= T <= 1000）和M（1 <= M <= 100），T代表总共能够用来采药的时间，M代表山洞里的草药的数目。接下来的M行每行包括两个在1到100之间（包括1和100）的的整数，分别表示采摘某株草药的时间和这株草药的价值。

**输出**

输出只包括一行，这一行只包含一个整数，表示在规定的时间内，可以采到的草药的最大总价值。

样例输入

```
70 3
71 100
69 1
1 2
```

样例输出

```
3
```

来源：NOIP 2005



记忆式搜索，13行是分叉。

```python
import math
from functools import lru_cache

@lru_cache(maxsize = None)
def fn(i, s):
  # i-th item, knapsack with available capacity s

  if (s < 0):
    return -math.inf
  if (i == len(vs)):
      return 0

  return max(fn(i+1, s), vs[i] + fn(i+1, s-ws[i]))


T, M = map(int, input().split())
ws = []
vs = []
for _ in range(M):
    t, v = map(int, input().split())
    ws.append(t)
    vs.append(v)

print(fn(0, T))
```





### 01661: Help Jimmy （难题）

dfs/dp, http://cs101.openjudge.cn/practice/01661

"Help Jimmy" 是在下图所示的场景上完成的游戏：
![img](https://raw.githubusercontent.com/GMyhf/img/main/img/2978_1-20230915145941944.jpg)
场景中包括多个长度和高度各不相同的平台。地面是最低的平台，高度为零，长度无限。

Jimmy老鼠在时刻0从高于所有平台的某处开始下落，它的下落速度始终为1米/秒。当Jimmy落到某个平台上时，游戏者选择让它向左还是向右跑，它跑动的速度也是1米/秒。当Jimmy跑到平台的边缘时，开始继续下落。Jimmy每次下落的高度不能超过MAX米，不然就会摔死，游戏也会结束。

设计一个程序，计算Jimmy到底地面时可能的最早时间。

**输入**

第一行是测试数据的组数t（0 ≤  t ≤  20）。每组测试数据的第一行是四个整数N，X，Y，MAX，用空格分隔。N是平台的数目（不包括地面），X和Y是Jimmy开始下落的位置的横竖坐标，MAX是一次下落的最大高度。接下来的N行每行描述一个平台，包括三个整数，X1[i]，X2[i]和H[i]。H[i]表示平台的高度，X1[i]和X2[i]表示平台左右端点的横坐标。1 ≤  N ≤  1000，-20000 ≤  X, X1[i], X2[i] ≤  20000，0 < H[i] < Y ≤  20000（i = 1..N）。所有坐标的单位都是米。

Jimmy的大小和平台的厚度均忽略不计。如果Jimmy恰好落在某个平台的边缘，被视为落在平台上。所有的平台均不重叠或相连。测试数据保证问题一定有解。

**输出**

对输入的每组测试数据，输出一个整数，Jimmy到底地面时可能的最早时间。

样例输入

```
1
3 8 17 20
0 10 8
0 10 13
4 14 3
```

样例输出

```
23
```

来源：POJ Monthly--2004.05.15, CEOI 2000, POJ 1661, 程序设计实习2007



```python
# 查达闻 2300011813
from functools import lru_cache

@lru_cache
def dfs(x, y, z):
    for i in range(z+1, N+1):
        if y - MaxVal > p[i][2]:
            return 1 << 30
        elif p[i][0] <= x <= p[i][1]:
            left = x - p[i][0] + dfs(p[i][0], p[i][2], i)
            right = p[i][1] - x + dfs(p[i][1], p[i][2], i)
            return min(left,right)
        
    if y <= MaxVal:
        return 0
    else:
        return 1 << 30


for _ in range(int(input())):
    N, ini_x, ini_y, MaxVal = map(int, input().split())
    
    p = []      #platform
    p.append( [0, 0, 1 << 30] ) # 1<<30 大于 20000*2*1000
    for _ in range(N):
        p.append([int(x) for x in input().split()])
    p.sort(key = lambda x:-x[2])

    print(ini_y + dfs(ini_x, ini_y, 0))
```





### 02386: Lake Counting

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



### 05585: 晶矿的个数

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





### 19930: 寻宝

bfs, http://cs101.openjudge.cn/practice/19930

Billy获得了一张藏宝图，图上标记了普通点（0），藏宝点（1）和陷阱（2）。按照藏宝图，Billy只能上下左右移动，每次移动一格，且途中不能经过陷阱。现在Billy从藏宝图的左上角出发，请问他是否能到达藏宝点？如果能，所需最短步数为多少？

**输入**

第一行为两个整数m,n，分别表示藏宝图的行数和列数。(m<=50,n<=50)
此后m行，每行n个整数（0，1，2），表示藏宝图的内容。

**输出**

如果不能到达，输出‘NO’。
如果能到达，输出所需的最短步数（一个整数）。

样例输入

```
样例输入1：
3 4
0 0 2 0
0 2 1 0
0 0 0 0

样例输出1：
5
```

样例输出

```
样例输入2：
2 2
0 2
2 1

样例输出2:
NO
```

提示

每张藏宝图有且仅有一个藏宝点。
输入保证左上角（起点）不是陷阱。

来源：by cs101-2009 邵天泽



其实所有求最短、最长的问题都能用heapq实现，在图搜索中搭配bfs尤其好用。

```python
#23 工学院 苏王捷
import heapq
def bfs(x,y):
    d=[[-1,0],[1,0],[0,1],[0,-1]]
    queue=[]
    heapq.heappush(queue,[0,x,y])
    check=set()
    check.add((x,y))
    while queue:
        step,x,y=map(int,heapq.heappop(queue))
        if martix[x][y]==1:
            return step
        for i in range(4):
            dx,dy=x+d[i][0],y+d[i][1]
            if martix[dx][dy]!=2 and (dx,dy) not in check:
                heapq.heappush(queue,[step+1,dx,dy])
                check.add((dx,dy))
    return "NO"
            
m,n=map(int,input().split())
martix=[[2]*(n+2)]+[[2]+list(map(int,input().split()))+[2] for i in range(m)]+[[2]*(n+2)]
print(bfs(1,1))
```



### 20106: 走山路

http://cs101.openjudge.cn/routine/20106/

某同学在一处山地里，地面起伏很大，他想从一个地方走到另一个地方，并且希望能尽量走平路。
现有一个m*n的地形图，图上是数字代表该位置的高度，"#"代表该位置不可以经过。
该同学每一次只能向上下左右移动，每次移动消耗的体力为移动前后该同学所处高度的差的绝对值。现在给出该同学出发的地点和目的地，需要你求出他最少要消耗多少体力。

**输入**

第一行是m,n,p，m是行数，n是列数，p是测试数据组数
接下来m行是地形图
再接下来n行每行前两个数是出发点坐标（前面是行，后面是列），后面两个数是目的地坐标（前面是行，后面是列）（出发点、目的地可以是任何地方，出发点和目的地如果有一个或两个在"#"处，则将被认为是无法达到目的地）

**输出**

n行，每一行为对应的所需最小体力，若无法达到，则输出"NO"

样例输入

```
4 5 3
0 0 0 0 0
0 1 1 2 3
# 1 0 0 0
0 # 0 0 0
0 0 3 4
1 0 1 4
3 4 3 0
```

样例输出

```
2
3
NO

解释：
第一组：从左上角到右下角，要上1再下来，所需体力为2
第二组：一直往右走，高度从0变为1，再变为2，再变为3，消耗体力为3
第三组：左下角周围都是"#"，不可以经过，因此到不了
```

来源: cs101-2019 张翔宇



注意 line 9: v.add(..)，在heappop之后，保证最优的才入v。

```python
# 23 蒋子轩
from heapq import heappop, heappush

def bfs(x1, y1):
    q = [(0, x1, y1)]
    v = set()
    while q:
        t, x, y = heappop(q)
        v.add((x, y))
        if x == x2 and y == y2:
            return t
        for dx, dy in dir:
            nx, ny = x+dx, y+dy
            if 0 <= nx < m and 0 <= ny < n and ma[nx][ny] != '#' and (nx, ny) not in v:
                nt = t+abs(int(ma[nx][ny])-int(ma[x][y]))
                heappush(q, (nt, nx, ny))
    return 'NO'


m, n, p = map(int, input().split())
ma = [list(input().split()) for _ in range(m)]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for _ in range(p):
    x1, y1, x2, y2 = map(int, input().split())
    if ma[x1][y1] == '#' or ma[x2][y2] == '#':
        print('NO')
        continue
    print(bfs(x1, y1))
```



```python
# 23 苏王捷

import heapq
m, n, p = map(int, input().split())
martix = [list(input().split())for i in range(m)]
dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for _ in range(p):
    sx, sy, ex, ey = map(int, input().split())
    if martix[sx][sy] == "#" or martix[ex][ey] == "#":
        print("NO")
        continue
    vis, heap, ans = set(), [], []
    heapq.heappush(heap, (0, sx, sy))
    vis.add((sx, sy, -1))
    while heap:
        tire, x, y = heapq.heappop(heap)
        if x == ex and y == ey:
            ans.append(tire)
        for i in range(4):
            dx, dy = dir[i]
            x1, y1 = dx+x, dy+y
            if 0 <= x1 < m and 0 <= y1 < n and martix[x1][y1] != "#" and (x1, y1, i) not in vis:
                t1 = tire+abs(int(martix[x][y])-int(martix[x1][y1]))
                heapq.heappush(heap, (t1, x1, y1))
                vis.add((x1, y1, i))
    print(min(ans) if ans else "NO")
```





### 04115: 鸣人和佐助

bfs, http://cs101.openjudge.cn/practice/04115/

佐助被大蛇丸诱骗走了，鸣人在多少时间内能追上他呢？

![image-20231025141449508](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231025141449508.png)

已知一张地图（以二维矩阵的形式表示）以及佐助和鸣人的位置。地图上的每个位置都可以走到，只不过有些位置上有大蛇丸的手下，需要先打败大蛇丸的手下才能到这些位置。鸣人有一定数量的查克拉，每一个单位的查克拉可以打败一个大蛇丸的手下。假设鸣人可以往上下左右四个方向移动，每移动一个距离需要花费1个单位时间，打败大蛇丸的手下不需要时间。如果鸣人查克拉消耗完了，则只可以走到没有大蛇丸手下的位置，不可以再移动到有大蛇丸手下的位置。佐助在此期间不移动，大蛇丸的手下也不移动。请问，鸣人要追上佐助最少需要花费多少时间？

**输入**

输入的第一行包含三个整数：M，N，T。代表M行N列的地图和鸣人初始的查克拉数量T。0 < M,N < 200，0 ≤ T < 10
后面是M行N列的地图，其中@代表鸣人，+代表佐助。*代表通路，#代表大蛇丸的手下。

**输出**

输出包含一个整数R，代表鸣人追上佐助最少需要花费的时间。如果鸣人无法追上佐助，则输出-1。

样例输入

```
样例输入1
4 4 1
#@##
**##
###+
****

样例输入2
4 4 2
#@##
**##
###+
****
```

样例输出

```
样例输出1
6

样例输出2
4
```



```python
# 2300011075	苏王捷	工学院
'''
这段代码是一个迷宫求解的问题。主要使用了广度优先搜索算法来找到从起点到终点的最短路径。

首先，代码导入了deque模块来实现队列数据结构。
然后，定义了一个Node类，表示迷宫中的一个节点。它有四个属性：x和y表示节点的坐标，
tools表示节点当前拥有的工具数，steps表示从起点到达该节点的步数。

接下来，读取输入的迷宫信息，包括迷宫的大小M和N，以及可以使用的工具数T。maze是一个二维列表，
表示迷宫的格子，其中'@'表示起点，'+'表示终点，'*'表示障碍物。

创建了一个visit列表，用于记录节点是否被访问过。visit是一个三维列表，
三个维度分别表示行、列和工具数。

定义了directions列表，包含四个方向的偏移量。

通过遍历迷宫，找到起点和终点的位置，并设置起点节点的属性。

使用广度优先搜索算法，通过一个队列queue来依次处理节点。从起点开始，判断四个方向的相邻节点：
如果是'*'表示可以直接通过，将其加入队列并标记为已访问；如果是'#'表示需要使用一个工具，
才能通过，判断当前节点是否还有工具可用，如果有则减少一个工具，并将该节点加入队列并标记为已访问。

如果队列为空，即无法到达终点，则输出"-1"；如果找到终点，输出步数，并将flag标记为1，退出循环。

最后，判断flag是否为0，如果是说明无法找到终点，输出"-1"。
'''

from collections import deque


class Node:
    def __init__(self, x, y, tools, steps):
        self.x = x
        self.y = y
        self.tools = tools
        self.steps = steps


M, N, T = map(int, input().split())
maze = [list(input()) for _ in range(M)]
visit = [[[0]*(T+1) for _ in range(N)] for _ in range(M)]
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
start = end = None
flag = 0
for i in range(M):
    for j in range(N):
        if maze[i][j] == '@':
            start = Node(i, j, T, 0)
            visit[i][j][T] = 1
        if maze[i][j] == '+':
            end = (i, j)
            maze[i][j] = '*'
            
queue = deque([start])
while queue:
    node = queue.popleft()
    if (node.x, node.y) == end:
        print(node.steps)
        flag = 1
        break
    for direction in directions:
        nx, ny = node.x+direction[0], node.y+direction[1]
        if 0 <= nx < M and 0 <= ny < N:
            if maze[nx][ny] == '*':
                if not visit[nx][ny][node.tools]:
                    queue.append(Node(nx, ny, node.tools, node.steps+1))
                    visit[nx][ny][node.tools] = 1
            elif maze[nx][ny] == '#':
                if node.tools > 0 and not visit[nx][ny][node.tools-1]:
                    queue.append(Node(nx, ny, node.tools-1, node.steps+1))
                    visit[nx][ny][node.tools-1] = 1
                    
if not flag:
    print("-1")

```





### 04116: 拯救行动

bfs, http://cs101.openjudge.cn/practice/04116/

公主被恶人抓走，被关押在牢房的某个地方。牢房用N*M (N, M <= 200)的矩阵来表示。矩阵中的每项可以代表道路（@）、墙壁（#）、和守卫（x）。
英勇的骑士（r）决定孤身一人去拯救公主（a）。我们假设拯救成功的表示是“骑士到达了公主所在的位置”。由于在通往公主所在位置的道路中可能遇到守卫，骑士一旦遇到守卫，必须杀死守卫才能继续前进。
现假设骑士可以向上、下、左、右四个方向移动，每移动一个位置需要1个单位时间，杀死一个守卫需要花费额外的1个单位时间。同时假设骑士足够强壮，有能力杀死所有的守卫。

给定牢房矩阵，公主、骑士和守卫在矩阵中的位置，请你计算拯救行动成功需要花费最短时间。

**输入**

第一行为一个整数S，表示输入的数据的组数（多组输入）
随后有S组数据，每组数据按如下格式输入
1、两个整数代表N和M, (N, M <= 200).
2、随后N行，每行有M个字符。"@"代表道路，"a"代表公主，"r"代表骑士，"x"代表守卫, "#"代表墙壁。

**输出**

如果拯救行动成功，输出一个整数，表示行动的最短时间。
如果不可能成功，输出"Impossible"

样例输入

```
2
7 8
#@#####@
#@a#@@r@
#@@#x@@@
@@#@@#@#
#@@@##@@
@#@@@@@@
@@@@@@@@ 
13 40
@x@@##x@#x@x#xxxx##@#x@x@@#x#@#x#@@x@#@x
xx###x@x#@@##xx@@@#@x@@#x@xxx@@#x@#x@@x@
#@x#@x#x#@@##@@x#@xx#xxx@@x##@@@#@x@@x@x
@##x@@@x#xx#@@#xxxx#@@x@x@#@x@@@x@#@#x@#
@#xxxxx##@@x##x@xxx@@#x@x####@@@x#x##@#@
#xxx#@#x##xxxx@@#xx@@@x@xxx#@#xxx@x#####
#x@xxxx#@x@@@@##@x#xx#xxx@#xx#@#####x#@x
xx##@#@x##x##x#@x#@a#xx@##@#@##xx@#@@x@x
x#x#@x@#x#@##@xrx@x#xxxx@##x##xx#@#x@xx@
#x@@#@###x##x@x#@@#@@x@x@@xx@@@@##@@x@@x
x#xx@x###@xxx#@#x#@@###@#@##@x#@x@#@@#@@
#@#x@x#x#x###@x@@xxx####x@x##@x####xx#@x
#x#@x#x######@@#x@#xxxx#xx@@@#xx#x#####@
```

样例输出

```
13
7
```

 

```python
# 用时间来扩展bfs的下一个节点
#from collections import deque
from heapq import heappush, heappop

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(matrix, start):
    n, m = len(matrix), len(matrix[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    #q = deque([(start[0], start[1], 0)])
    q = []
    heappush(q, (0, start[0], start[1]))
    visited[start[0]][start[1]] = True
    while len(q) != 0:
        #x, y, time = q.popleft()
        time, x, y = heappop(q)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if matrix[nx][ny] == "a":
                    #ans.append(time+1)
                    return time + 1
                elif matrix[nx][ny] == "@":
                    #q.append((nx, ny, time + 1))
                    heappush(q, (time + 1, nx, ny))
                    visited[nx][ny] = True
                elif matrix[nx][ny] == "x":
                    #q.append((nx, ny, time + 2))
                    heappush(q, (time + 2, nx, ny))
                    visited[nx][ny] = True

    return "Impossible"


S = int(input())
for _ in range(S):
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]
    start = None
    ans = []
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == "r":
                start = (i, j)
                break
    print(bfs(matrix, start))
    # if ans == []:
    #     print("Impossible")
    # else:
    #     print(min(ans))

```





### 04129: 变换的迷宫

bfs, http://cs101.openjudge.cn/practice/04129

你现在身处一个R*C 的迷宫中，你的位置用"S" 表示，迷宫的出口用"E" 表示。

迷宫中有一些石头，用"#" 表示，还有一些可以随意走动的区域，用"." 表示。

初始时间为0 时，你站在地图中标记为"S" 的位置上。你每移动一步（向上下左右方向移动）会花费一个单位时间。你必须一直保持移动，不能停留在原地不走。

当前时间是K 的倍数时，迷宫中的石头就会消失，此时你可以走到这些位置上。在其余的时间里，你不能走到石头所在的位置。

求你从初始位置走到迷宫出口最少需要花费多少个单位时间。

如果无法走到出口，则输出"Oop!"。

**输入**

第一行是一个正整数 T，表示有 T 组数据。
每组数据的第一行包含三个用空格分开的正整数，分别为 R、C、K。
接下来的 R 行中，每行包含了 C 个字符，分别可能是 "S"、"E"、"#" 或 "."。
其中，0 < T <= 20，0 < R, C <= 100，2 <= K <= 10。

**输出**

对于每组数据，如果能够走到迷宫的出口，则输出一个正整数，表示最少需要花费的单位时间，否则输出 "Oop!"。

样例输入

```
1
6 6 2
...S..
...#..
.#....
...#..
...#..
..#E#.
```

样例输出

```
7
```



容易想到广搜，但是数据大，会超时，需要剪枝。由于每过k单位时间，石头就会消失一次，那么当我们站在某点 (x,y) 时，时间为 t+k 和  t  时，它们之后行走面临的情境是完全一样的，那就意味着，对于某个状态的时间，我们可以取模后作为 visited\[x]\[y]\[time] 的第三个变量，如果取模后的值代入发现已经访问过，那说明之前已经有更优越的情况出现过，不必再继续搜索了.   思路参考：https://blog.csdn.net/dhc65376/article/details/101555903

```python
arr2 = lambda m,n : [ [' ' for j in range(n)] for i in range(m) ]
arr3 = lambda m,n,l : [ [ [False for k in range(l)] for j in range(n)] for i in range(m) ]

N = 100
K = 10

class Node:
    def __init__(self, r=0, c=0, t=0):
        self.row = r
        self.col = c
        self.time = t
        
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for _ in range(int(input())):
    maze = arr2(N, N)       # 注意不同数据组之间的初始化
    vis = arr3(N, N, K)
    q = []
    r,c,k = map(int, input().split())
    for i in range(r):
        maze[i][:c] = list(input())

    tr = tc = cnt = 0;
    for i in range(r):
        for j in range(c):
            if maze[i][j] == 'S':
                q.append(Node(i, j))
                vis[i][j][0] = True
                cnt += 1
                if cnt == 2: break
            elif maze[i][j] == 'E':
                tr = i
                tc = j
                cnt += 1
                if cnt == 2: break
            
    while(len(q)):
        t = q[0] # t : Node
        if t.row == tr and t.col == tc: break
        q.pop(0)
        for i in range(4):
            nrow = t.row + dr[i]
            ncol = t.col + dc[i]

            if nrow < 0 or nrow >= r or ncol < 0 or ncol >= c:
                 continue
                    
            # 剪枝很容易能知道，由于每过k单位时间，石头就会消失一次，那么当我们站在某点 (x,y) 时，
            # 时间为 t+k 和  t  时，它们之后行走面临的情境是完全一样的，那就意味着，
            # 对于某个状态的时间，我们可以取模后作为 visited[x][y][time] 的第三个变量，
            # 如果取模后的值代入发现已经访问过，那说明之前已经有更优越的情况出现过，不必再继续搜索了. 
            if vis[nrow][ncol][(t.time + 1) % k]:
                 continue
             
            # 时间是K 的倍数时，迷宫中的石头就会消失
            if (t.time + 1) % k and maze[nrow][ncol] == '#': 
                 continue;
            vis[nrow][ncol][(t.time + 1) % k] = True
            q.append(Node(nrow, ncol, t.time + 1))

    if len(q) == 0:
        print("Oop!")
    else:
        print(q[0].time)
```





