t-prime (binary search)

```
def euler_sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
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
    return is_prime
 
s = euler_sieve(1000000)
 
input()
for i in map(int,input().split()):
    sqrt_i = i**0.5
    if sqrt_i % 1 == 0:	# 对于浮点数，x % 1 == 0 用于检查 x 是否是一个整数。
        if s[int(sqrt_i)]:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
```

图的拉普拉斯矩阵, matrices

```
node,edge = map(int,input().split())
matrix_a = [[0]*node for i in range(node)] 
matrix_b = [[0]*node for i in range(node)] 

for i in range(edge):
    a,b= map(int,input().split())
    matrix_a[a][b]=1
    matrix_a[b][a]=1
for j in range(node):
    matrix_b[j][j] = sum(matrix_a[j])

l = [[matrix_b[l][k]-matrix_a[l][k] for k in range(node)] for l in range(node)]
for i in l:
    print(*i)
```



## 你和你比较熟悉的同学(bfs)

```
d,ans={-1:set()},[]
for _ in range(int(input())):
    l=input().split()
    d[int(l[0])]=set([int(i) for i in l[2:]])   
def bfs(i):
    queue,visited=[i],{i}
    while queue:
        node=queue.pop(0)
        visited.add(node)
        queue=queue+list(d.get(node,set())-visited)
    if len(d.get(node,set())-visited)==0:
        ans.append(len(visited-{-1}))
for i in d.keys():
    bfs(i)
print(max(ans))
```







## 计算鞍点 matrix
```
a = [[int(x) for x in input().split()] for _ in range(5)]
for i in range(5):
    maximum = a[i][0]
    maxindex = 0
    for j in range(1, 5):
        if a[i][j] > maximum:
            maximum = a[i][j]
            maxindex = j
    for j in range(5):
        if j != i and a[j][maxindex] <= maximum:
            break
    else:
        print(i+1, maxindex+1, maximum)
        break
else:
    print('not found')
```









------

## 1·함수

### 출력

```
print(f'{ans},{res:.1f}')
```

`print`는 `sep`와 `end` 매개변수를 지정할 수 있음

### 문자열

```
str.title()   # 각 단어의 첫 글자를 대문자로
str.lower()   # 모든 글자를 소문자로
str.upper()   # 모든 글자를 대문자로
str.strip()   # 양 끝 공백 제거 (rstrip/lstrip은 끝/앞 공백 제거)
ord(), chr()  # 문자와 ASCII 코드 상호 변환
str.find()    # 특정 문자 검색, 없으면 -1 반환
```

### 연산

- 파이썬의 `float`은 정밀도 문제가 있으므로, 가능하면 `int` 연산을 사용하거나 `/` 대신 `//`를 쓰는 편이 좋음.
- 나눗셈에서는 0으로 나누는 상황이 발생할 수 있으니 주의.
- 반올림 시 `round`는 엄밀한 사사오입이 아니며, `.5`인 경우 짝수 방향으로 반올림됨.
- `float`을 단순히 `==`로 비교하면 위험하므로, 절댓값 차이를 작은 오차 범위와 비교하거나 `math.isclose` 사용을 고려.
- `floor`, `ceil`은 안전.

**`math` 라이브러리**:

- `sqrt`, `log(x[, base])`, `sin()`, `asin()` 등 삼각함수와 역삼각함수 포함
- 상수 `e`, `pi`, 그리고 `inf`(무한대)
- `floor()`(x 이하 최대 정수), `ceil()`(x 이상 최소 정수)
- `isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)` 두 부동소수점의 근사 동등성 판정
- `pow(x, y)`, `factorial(x)`, `comb(n, k)`(조합수)
- `math.radians()`, `math.degrees()` 각도(도 ↔ 라디안) 변환

------

### 리스트, 딕셔너리

- `append`, `pop`은 모두 O(1).
   하지만 `del`, `remove`, `pop(0)`, `insert`, `index` 등은 모두 O(n)이므로 주의.
   반복적으로 리스트에서 요소를 제거해야 하는 상황이라면, 미리 불리언 배열로 표시만 해둔 뒤 한 번에 처리하는 등의 방법을 고려.

- 슬라이싱(`list[k:l]`)은 잘라낼 길이에 비례한 선형 복잡도를 지님.
   `k >= l`이면 빈 리스트를 반환하므로 에러는 아님.

- `in list`는 O(n)이므로, 빈도 높은 탐색 시 딕셔너리나 `set` 사용 고려.

- `list.index()` 역시 선형 탐색일 뿐 아니라, 실패 시 `IndexError` 발생.

- 파이썬 리스트 인덱스는 음수 사용이 가능하지만, 양수가 범위를 벗어나면 에러.

- `list.sort()`, `list.reverse()`는 리스트를 제자리에서 수정하며 반환값이 없음.
   필요하다면 `sorted()`나 `reversed()` 사용. 이때 `reversed()`는 `reversed object` 반환이므로 리스트가 필요하면 `list(...)`로 변환.

- 정렬 예시

  ```python
  list.sort(key=lambda x: x[0], reverse=True)  # 첫 번째 요소 기준 내림차순
  list.sort(key=lambda x: (x[0], x[1]))        # 첫 요소 → 둘째 요소 순으로 정렬
  ```

- `sum([])`는 0을 반환하지만 `min([])`나 `max([])`는 에러 발생.

- 리스트 내포: `[f(x) for x in list (if P(x))]`.

- 리스트 이어 붙이기는 `+`, `list.extend()` 사용.

- 리스트 순회 중 요소 추가/삭제는 가급적 피하고, 불가피하다면 `while` 사용.

#### 얕은 복사(Shallow Copy) 이슈

- 2차원 이상의 리스트에서 `*`나 `copy()` 등으로 복사하면 내부 리스트가 동일 객체를 가리킬 수 있음.

- 예) 

  ```
  [[0] * m]
  ```

  은 괜찮지만, 

  ```
  [[0] * m] * n
  ```

  은 내부 리스트가 전부 같은 객체.

  ```python
  # 올바른 2차원 리스트 초기화 예시
  arr = [[0] * m for _ in range(n)]
  ```

- 1차원은 `a = b[:]` 또는 `copy` 모듈의 `deepcopy` 사용을 고려.

#### 딕셔너리

- 딕셔너리는 키와 값으로 어떤 타입이든 가능. 단, 키는 변경 불가능한 타입이어야 함(list는 불가).
- 미리 계산한 결과를 딕셔너리에 저장해두면 접근이 O(1)이므로 시간 절약 가능(단, MLE 위험성).
- 순회 시 `sorted(dict.keys())`, `dict.values()`, `dict.items()` 등 사용 가능.
- `dict.get(key, default=None)` 키가 없으면 기본값 반환.
- `dict.pop(key, default=None)` 키-값 쌍 삭제.
- 이미 존재하는 키에 값을 할당하면 기존 값을 덮어씀.

#### `enumerate`

- `for i, x in enumerate(list)` → 인덱스-값 쌍 순회

------

## 2·알고리즘

### 소수

오일러(에울러) 시프트(선형 시간)

```python
def oula(a):
    zhishu=[]
    zhishu1=[True]*(a+1)
    for i in range(2,a+1):
        if zhishu1[i]:
            zhishu.append(i)
        for h in zhishu:
            if h*i<=a:
                zhishu1[h*i]=False
    zhishu=set(zhishu)
    return zhishu
```

------

### 동적 프로그래밍 (Dynamic Programming)

#### 최장 공통 부분 수열(LCS)

```python
for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

#### 최장 단조 부분 수열(LIS)

```python
dp = [1]*n
for i in range(1,n):
    for j in range(i):
        if A[j]<A[i]:
            dp[i] = max(dp[i],dp[j]+1)
ans = sum(dp)
```

#### 배낭 문제

##### 0-1 배낭

`dp[t]`가 시간 t에서 얻을 수 있는 최대값이라고 할 때, i번째 물건을 넣을지 말지 결정하는 전이를 수행.
 롤링 배열을 써서 2차원을 1차원으로 줄이되, 내부 반복을 뒤에서부터 돌려야 함.

```python
dp = [0]*T
for i in range(n):
    for t in range(T,time[i]-1,-1):
        dp[t] = max(dp[t],dp[t-time[i]]+value[i])
ans = dp[T]
```

##### 완전 배낭

0-1 배낭에서 내부 반복을 정방향으로 돌리면 됨(중복 가능).

##### 다중 배낭

- 동일한 물건이 여러 개 있을 때, 2의 거듭제곱 형태로 나눠 0-1 배낭으로 처리(이진분할 최적화).

```python
dp = [0]*T
for i in range(n):
    all_num = nums[i]
    k = 1
    while all_num>0:
        use_num = min(k,all_num)
        for t in range(T,use_num*time[i]-1,-1):
            dp[t] = max(dp[t-use_num*time[i]]+use_num*value[i],dp[t])
        k *= 2
        all_num -= use_num
```

- T가 매우 클 경우에는 다른 방법(DFS 등)을 고려할 수도 있음.

------

### 구간(Interval) 문제

#### 1. 구간 병합



주어진 구간들 중 겹치는(끝점이 닿기만 해도 겹침) 구간을 합쳐 최종 구간을 구함.

![img](https://pic4.zhimg.com/80/v2-6e3bb59ed6c14eacfa1331c645d4afdf_1440w.jpg)

1. 구간을 왼쪽 끝 기준 오름차순 정렬

2. 앞서 결정된 구간의 가장 오른쪽 끝 

   ```
   ed
   ```

   를 갱신해가며, 새 구간 [l_i, r_i]가 겹치는지 확인

   - 겹치면 `ed = max(ed, r_i)`
   - 겹치지 않으면 새 구간으로 추가하고 `ed`를 새로 설정

```python
list.sort(key=lambda x:x[0])
st=list[0][0]
ed=list[0][1]
ans=[]
for i in range(1,n):
    if list[i][0]<=ed:
        ed=max(ed,list[i][1])
    else:
        ans.append((st,ed))
        st=list[i][0]
        ed=list[i][1]
ans.append((st,ed))
```

#### 2. 서로 겹치지 않는 구간 최대 개수 선택

주어진 구간들 중 서로 겹치지 않게 최대한 많이 골라야 함(끝점이 같은 것도 겹침으로 봄).

![img](https://pic1.zhimg.com/80/v2-690f7e53fd34c39802f45f48b59d5c5a_1440w.webp)

1. 구간을 오른쪽 끝 기준으로 오름차순 정렬
2. `ed`를 추적하며, `[l_i, r_i]`가 `ed` 이하이면 스킵, 초과하면 선택

```python
list.sort(key=lambda x:x[1])
ed=list[0][1]
ans=[list[0]]
for i in range(1,n):
    if list[i][0]<=ed:
        continue
    else:
        ans.append(list[i])
        ed=list[i][1]
```

#### 3. 구간에 점 찍기(커버)

모든 구간에 최소한 하나씩 점이 포함되도록, 점을 최소 개수로 찍는 문제.
 서로 겹치는 구간이 많으면 한 점으로 여러 구간을 커버 가능.
 위의 “서로 겹치지 않는 구간 최대 개수” 문제와 동일한 방식으로 접근함.

![img](https://pica.zhimg.com/80/v2-a7ef021e1191ec53f20609ba870b44ba_1440w.webp)

```python
list.sort(key=lambda x:x[1])
ed=list[0][1]
ans=[list[0][1]]
for i in range(1,n):
    if list[i][0]<=ed:
        continue
    else:
        ans.append(list[i][1])
        ed=list[i][1]
```

#### 4. 구간 덮기(주어진 목표 구간)

목표로 하는 구간을 덮기 위해 필요한 최소 구간 개수를 구함.

![img](https://pic3.zhimg.com/80/v2-66041d9941667482fc51adeb4a616f64_1440w.webp)

1. 구간을 왼쪽 끝 기준 오름차순 정렬
2. 현재 목표 구간의 시작점을 덮을 수 있는 구간들 중 오른쪽 끝이 가장 큰 것을 선택
3. 목표 구간이 완전히 덮일 때까지 반복

```python
q.sort(key=lambda x:x[0])
# start,end 주어짐
ans=0
ed=q[0][1]
for i in range(n):
    if q[i][0]<=start<=q[i][1]:
        ed=max(ed,q[i][1])
        if ed>=end:
            ans+=1
            break
    else:
        ans+=1
        start=0
        start+=ed
```

#### 5. 구간 분류(그룹핑)

주어진 구간들을 여러 그룹으로 나누되, 같은 그룹 내의 구간들끼리는 겹치지 않도록 하는 최소 그룹 수를 구함.

1. 구간을 왼쪽 끝 기준으로 오름차순 정렬
2. 우선순위 큐(최소 힙)에 각 그룹의 현재 끝점을 저장하고, 새로운 구간이 들어올 때 기존 그룹에 들어갈 수 있는지 확인
3. 불가능하면 새 그룹 추가, 가능하면 기존 그룹의 끝점 갱신

```python
import heapq
list.sort(key=lambda x: x[0])
min_heap = [list[0][1]]
for i in range(1, n):
    if list[i][0] >= min_heap[0]:
        heapq.heappop(min_heap)
    heapq.heappush(min_heap, list[i][1])
num=len(min_heap)
```

------

### BFS

- 최단 거리(최단 경로) 문제에 자주 활용
- 큐에 `(x, y)` 혹은 `(x, y, t)`처럼 필요한 상태 정보를 함께 넣음
- 방문했던 노드는 `visited` 등에 기록해 중복 처리를 방지

```python
from collections import deque
directions=[...]
queue=deque([(x0,y0)])
visited=set()
visited.add((x0,y0))

while queue:
    x,y=queue.popleft()
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if -1<nx<n and -1<ny<m and ... and (nx,ny) not in visited:
            visited.add((nx,ny))
            queue.append((nx,ny))
```

변형할 때는 BFS에서 레벨(깊이)을 추적하고, 각 레벨마다 조건을 다르게 적용할 수도 있음.

------

#### Dijkstra (BFS 변형)

- 가중치가 있는 최단 경로 문제에 쓰임
- 최단 거리를 우선순위 큐(최소 힙)에 `(거리, x, y)` 형태로 넣어 항상 현재까지 최단 거리 노드부터 꺼냄

```python
import heapq
directions=[...]
ditu = []
tl=[[float('inf')]*n for _ in range(m)]
tl[sx][sy]=0
queue = []
heapq.heappush(queue,(0,sx,sy))

while queue:
    t, x, y= heapq.heappop(queue)
    if x==ex and y==ey:
        ...
        break
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and ...:
            ...
            if ...:
                ...
                heapq.heappush(queue,(tl[nx][ny],nx,ny))
```

------

### DFS

- 그래프 탐색, 연결 요소, 경로 찾기 등에 사용.
- 왕복 경로(백트래킹)이 필요한 경우에는 방문 배제를 해제했다가 돌아오거나, 문제에 따라 다른 방식을 채택

#### 미로 문제

- 출구 도달 여부, 가능한 경로 수, 연결 요소 수, 연결 블록 크기 등
- 각 정점을 한 번씩만 방문하면 되므로 방문 배열을 쓴 뒤, 되돌아올 필요는 없는 경우가 많음

```python
directions = [...]
visited = [[False]*n for _ in range(m)]

def dfs(x,y):
    if visited[x][y]:
        return
    visited[x][y] = True
    ...
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<m and 0<=ny<n and ...:
            dfs(nx,ny)
```

#### 백트래킹 예시

- 체스판에서 나이트의 이동, 8퀸 문제 등
- dfs 안에서 시도 후 복귀 시 상태를 되돌리는 로직(회귀, backtrack)

```python
# 나이트 투어
directions=[[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]

def dfs(n,m,x,y,ma,step,p):
    if step==n*m:
        p[0]+=1
        return
    for dx,dy in directions:
        if -1<x+dx<n and -1<y+dy<m and ma[x+dx][y+dy]:
            ma[x+dx][y+dy]=0
            dfs(n,m,x+dx,y+dy,ma,step+1,p)
            ma[x+dx][y+dy]=1  # 복귀(backtrack)

case=int(input())
for _ in range(case):
    n,m,x,y=map(int,input().split())
    ma=[[1 for _ in range(m)] for _ in range(n)]
    ma[x][y]=0
    p=[0]
    dfs(n,m,x,y,ma,1,p)
    print(p[0])
```

------

### 이분 탐색 (Binary Search)

#### `bisect` 라이브러리

- 정렬된(오름차순) 리스트에서 삽입 위치를 구하거나 검색에 사용
- `bisect_left(a, x)`, `bisect_right(a, x)`: x가 삽입될 위치(왼쪽/오른쪽)을 반환
- `insort`로 삽입 가능하지만, 이는 O(n)이므로 대량 삽입 시 비효율적일 수 있음

```python
import bisect
bisect.bisect_right(a,6)  # 중복 요소가 있으면 그 오른쪽 위치 반환
bisect.insort(a,6)        # 리스트 a에 6 삽입
```

#### 적용

- 방정식 근사 해 찾기 (오차 범위 내에서 l, r 반복)
- 특정 최적화 문제(“최대의 최대값”과 같은 단조성 활용)에서도 “가능/불가능”을 판정해 탐색 범위를 줄이는 기법으로 활용

------

### 카데인(Kadane) 알고리즘 (최대 부분 배열)

```python
def max_subarray_sum(arr):
    if not arr:
        return 0
    max_current = max_global = arr[0]
    for num in arr[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global
```

2차원으로 확장해 최대 부분 행렬을 구할 수도 있음:

- 행 단위로 누적합을 구해 1차원 배열 형태를 만든 뒤 Kadane 적용

```python
def max_submatrix(matrix):
    def kadane(arr):
        max_end_here = max_so_far = arr[0]
        for x in arr[1:]:
            max_end_here = max(x, max_end_here + x)
            max_so_far = max(max_so_far, max_end_here)
        return max_so_far

    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float('-inf')

    for left in range(cols):
        temp = [0] * rows
        for right in range(left, cols):
            for row in range(rows):
                temp[row] += matrix[row][right]
            max_sum = max(max_sum, kadane(temp))
    return max_sum

n = int(input())
nums = []

while len(nums) < n * n:
    nums.extend(input().split())
matrix = [list(map(int, nums[i * n:(i + 1) * n])) for i in range(n)]

max_sum = max_submatrix(matrix)
print(max_sum)
```

------

### 기타 팁(성능 향상 등)

#### 재귀 가속

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def ...
```

#### 전처리 누적합

- O(n^2) 작업을 O(n)에 가깝게 줄일 수 있음

#### 늦은 삭제(lazy removal)

- 리스트에서 특정 원소를 찾아 바로 삭제하면 O(n)
- 우선순위 큐에서도 원하는 원소를 직접 제거하기 어렵기 때문에, “삭제 표시”만 하고, 실제 그 원소가 큐에서 맨 위에 도달했을 때 제거

```python
# out[x]에 삭제할 횟수를 기록
from heapq import heappop, heappush

while ls:
    x = heappop(ls)
    if not out[x]:
        new_min = x
        heappush(ls, x)  # 다시 큐에 넣고 종료
        break
    out[x] -= 1
```

#### `heapq` (파이썬 기본 제공 최소 힙)

- `heappush(heap, item)`
- `heappop(heap)`
- `heapify(data)` 등

#### 단조 스택

- 스택에 원소를 쌓되, 새로운 원소가 스택 top보다 클 경우 pop
- 예) 오큰수, 다음에 오는 더 큰 수를 찾는 문제

```python
p=list(map(int,input().split()))
index=[0]*len(p)
stack=[]
for i in range(len(p)-1,-1,-1):
    t=p[i]
    while stack and t>p[stack[-1]]:
        stack.pop()
    if stack:
        index[i]=stack[-1]-i
    stack.append(i)
print(index)
```

#### 날짜와 시간

```python
import calendar, datetime
print(calendar.isleap(2020))                    # 윤년 여부
print(datetime.datetime(2023, 10, 5).weekday()) # 목요일(3) 반환
```

------

