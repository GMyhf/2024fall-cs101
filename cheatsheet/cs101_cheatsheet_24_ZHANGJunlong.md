
# Cheatsheet

## 1. Dijkstra 算法（用堆来实现）
```python
import heapq
m, n, p = map(int, input().split())
l = [input().split() for _ in range(m)]
di = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def solve(x1, y1, x2, y2):
    heap = []
    la = [[float('inf')] * n for _ in range(m)]
    if l[x1][y1] == '#' or l[x2][y2] == '#':
        return 'NO'
    la[x1][y1] = 0
    heapq.heappush(heap, (0, x1, y1))
    while heap:
        d, x, y = heapq.heappop(heap)
        if x == x2 and y == y2:
            return d
        k = int(l[x][y])
        for dx, dy in di:
            nx, ny = dx + x, dy + y
            if 0 <= nx < m and 0 <= ny < n and l[nx][ny] != '#':
                if la[nx][ny] > d + abs(k - int(l[nx][ny])):
                    la[nx][ny] = d + abs(k - int(l[nx][ny]))
                    heapq.heappush(heap, (la[nx][ny], nx, ny))
    return 'NO'

for _ in range(p):
    x1, y1, x2, y2 = map(int, input().split())
    print(solve(x1, y1, x2, y2))
```

## 2. 并查集 + 路径压缩优化
```python
def f(x):
    if x != s[x]:
        s[x] = f(s[x])
    return s[x]
```

## 3. 将一个数组划分为 k 份，求最小最大和（用二分优化暴力查找）
```python
while start < end:
    t = (start + end) // 2
    if can(t):
        end = t
    else:
        start = t + 1
print(end)
```

## 4. 超级源点，BFS 水波扩展优化
```python
m, n = len(grid), len(grid[0])
fresh = 0
q = []
for i, row in enumerate(grid):
    for j, x in enumerate(row):
        if x == 1:
            fresh += 1
        elif x == 2:
            q.append((i, j))  # 一开始的预处理

ans = 0
while q and fresh:
    ans += 1
    tmp = q
    q = []
    for x, y in tmp:
        for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                fresh -= 1
                grid[i][j] = 2
                q.append((i, j))
return -1 if fresh else ans
```

## 5. 求所有排列时防止重复
```python
s = set()
for i in range(index, n):
    if candidates[i] in s:
        continue
    s.add(candidates[i])
    k = sum1 + candidates[i]
```

或者：
```python
if i > index and candidates[i - 1] == candidates[i]:
    continue
```

## 6. 贪心后悔解法
```python
import heapq

def max_potions(n, potions):
    health = 0
    consumed = []
    for potion in potions:
        health += potion
        heapq.heappush(consumed, potion)
        if health < 0:
            if consumed:
                health -= heapq.heappop(consumed)
    return len(consumed)
```

## 7. 递归改缓存
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def func(...):
    pass
```

## 8. 辅助栈同时操作，记录最小或最大
...

## 9. 单词拆分之类的也可以用递归（加缓存）
...

## 10. 不想交的线可以转化为公共子序列
...

## 11. 最大正方形：确定右下角，取周围三个最小 + 1
```python
for i in range(m):
    if matrix[0][i] == '1':
        la[0][i] = 1
        ans = 1
for i in range(1, n):
    if matrix[i][0] == '1':
        la[i][0] = 1
        ans = max(ans, la[i][0])
    for j in range(1, m):
        if matrix[i][j] == '1':
            la[i][j] = min(la[i-1][j], la[i-1][j-1], la[i][j-1]) + 1
            ans = max(ans, la[i][j])
return ans**2
```

## 12. 小游戏方向升维
...

## 13. 宠物精灵之收服（三维问题）
```python
n, m, k = map(int, input().split())
la = [[-1] * (m + 1) for _ in range(k + 1)]
la[0][m] = n
for q in range(1, k + 1):
    a, b = map(int, input().split())
    for j in range(m + 1):
        for i in range(q, 0, -1):
            if j + b <= m and la[i-1][j+b] != -1:
                la[i][j] = max(la[i-1][j+b] - a, la[i][j])

def solve():
    for i in range(k, -1, -1):
        for j in range(m, -1, -1):
            if la[i][j] != -1:
                print(i, j)
                return
solve()
```

## 14. 差分化（区间操作）
...

## 15. 三数之和（双指针）
```python
nums.sort()
for i in range(n-2):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    left, right = i + 1, n - 1
    k = -nums[i]
    while left < right:
        if nums[left] + nums[right] == k:
            ans.append([nums[i], nums[left], nums[right]])
            left += 1
            while nums[left] == nums[left-1] and left < right:
                left += 1
        elif nums[left] + nums[right] > k:
            right -= 1
        else:
            left += 1
```

... (More sections follow)

## 16. 用栈实现字符串的解码
```python
stack = []
res, multi = '', 0
for i in s:
    if i == '[':
        stack.append((res, multi))
        res, multi = '', 0
    elif i == ']':
        res1, multi1 = stack.pop()
        res = res1 + multi1 * res
    elif '0' <= i <= '9':
        multi = multi * 10 + int(i)
    else:
        res += i
return res
```

## 17. 在不单独创一个组的情况下将从 i 到 j 的数 reverse
```python
def reverse(nums, i, j):
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

# 关键代码处理
for i in range(n - 2, -1, -1):
    if nums[i] < nums[i + 1]:
        firstIndex = i
        break
if firstIndex == -1:
    reverse(nums, 0, n - 1)
    return
secondIndex = -1
for i in range(n - 1, firstIndex, -1):
    if nums[i] > nums[firstIndex]:
        secondIndex = i
        break
nums[firstIndex], nums[secondIndex] = nums[secondIndex], nums[firstIndex]
reverse(nums, firstIndex + 1, n - 1)
```

## 18. 双指针，不额外开创空间的情况下将同类数分在一起
```python
start = 0
for i in range(n):
    if nums[i] == 0:
        nums[i], nums[start] = nums[start], nums[i]
        start += 1
for j in range(start, n):
    if nums[j] == 1:
        nums[j], nums[start] = nums[start], nums[j]
        start += 1
```

## 19. Counter 使用
```python
l = Counter(nums)
a = l.most_common(1)  # 1 表示返回个数（返回的是元组）

# 对 Counter 形成的字典进行排序
l = sorted(l.items())  # 默认以 key 排序
sorted_items = sorted(counter.items(), key=lambda x: x[1], reverse=True)  # 按 value 排序
```

## 20. 异或操作
- 有结合性，且 a^0 = a, a^a = 0

## 21. 跳跃游戏 2
```python
n = len(nums)
end, k, far, ans = 0, 0, 0, 0
for i in range(n - 1):
    far = max(far, i + nums[i])
    if i == end:
        end = far
        ans += 1
return ans
```

## 22. 跳跃游戏 1
```python
n, rightmost = len(nums), 0
for i in range(n):
    if i <= rightmost:
        rightmost = max(rightmost, i + nums[i])
        if rightmost >= n - 1:
            return True
return False
```

## 23. 划分字母区间
```python
l = defaultdict(int)
n = len(s)
for i in range(n):
    l[s[i]] = i
k = 0
end = 0
start = 0
ans = []
while k < n:
    end = max(l[s[k]], end)
    if k == end:
        ans.append(end - start + 1)
        start = k + 1
    k += 1
```

## 24. 双指针实现求长度最短的子数组（有 DP 的思想）
```python
while e < n:
    k += nums[e]
    while k >= target:
        ans = min(ans, e - s + 1)
        k -= nums[s]
        s += 1
    e += 1
```

## 25. 滑动窗口（仅关键部分）
```python
for i in range(k, len(nums)):
    while q and nums[q[-1]] <= nums[i]:
        q.pop()
    q.append(i)
    while q[0] <= i - k:
        q.popleft()
    la.append(nums[q[0]])
```

## 26. 和为 k 的子数组
```python
ans = s = 0
cnt = defaultdict(int)
cnt[0] = 1  # s[0] = 0 单独统计
for x in nums:
    s += x
    ans += cnt[s - k]
    cnt[s] += 1
return ans
```

## 27. 旋转矩阵
```python
rows, columns = len(matrix), len(matrix[0])
visited = [[False] * columns for _ in range(rows)]
total = rows * columns
order = [0] * total
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
row, column = 0, 0
directionIndex = 0
for i in range(total):
    order[i] = matrix[row][column]
    visited[row][column] = True
    nextRow, nextColumn = row + directions[directionIndex][0], column + directions[directionIndex][1]
    if not (0 <= nextRow < rows and 0 <= nextColumn < columns and not visited[nextRow][nextColumn]):
        directionIndex = (directionIndex + 1) % 4
    row += directions[directionIndex][0]
    column += directions[directionIndex][1]
return order
```

## 28. 整数划分问题：确定上界的组合
```python
n = int(input())
l = [1] * (n + 1)
for i in range(1, n):
    for j in range(i + 1, n + 1):
        l[j] = l[j] + l[j - i - 1]
print(l[n])
```

## 29. 以一点为单位的 DP
- 一般用前 i 个来弄比较好。
- 但如果是多维的，只能用第 i 个，因为要考虑尾部是否可以合并。

## 30. 修改递归深度
```python
import sys
sys.setrecursionlimit(20000)
```
