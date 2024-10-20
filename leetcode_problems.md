# Leetcode编程题目

Updated 2340 GMT+8 Oct 20, 2024

2024 fall, Complied by Hongfei Yan



练习网址，https://leetcode.cn 。leetcode只需要完成核心代码就可以，不用写输入输出部分。

核心代码已经指定好类名、方法名、参数名，请勿修改或重命名，直接返回值即可。



# 常见区间问题

一文读懂五类常见区间问题，https://zhuanlan.zhihu.com/p/446371757

## 1 区间合并

### 1.1 题意描述

区间合并问题大概**题意**就是：

给出一堆区间，要求**合并**所有**有交集的区间** （端点处相交也算有交集）。最后问合并之后的**区间**。

如下图所示：

![img](https://pic4.zhimg.com/80/v2-6e3bb59ed6c14eacfa1331c645d4afdf_1440w.jpg)

<center>区间合并问题示例：合并结果包含3个区间</center>



### 1.2 解题步骤

【**步骤一**】：按照区间**左端点**从小到大排序。

【**步骤二**】：维护前面区间中最右边的端点为ed。从前往后枚举每一个区间，判断是否应该将当前区间视为新区间。

假设当前遍历到的区间为第i个区间 $[l_i,r_i]$，有以下两种情况：

- $l_i \le ed$：说明当前区间与前面区间**有交集**。因此**不需要**增加区间个数，但需要设置 $ed = max(ed, r_i)$。
- $l_i > ed$: 说明当前区间与前面**没有交集**。因此**需要**增加区间个数，并设置 $ed = max(ed, r_i)$。



### LeetCode 56.合并区间（实例）

https://leetcode.cn/problems/merge-intervals/

以数组 `intervals` 表示若干个区间的集合，其中单个区间为 `intervals[i] = [starti, endi]` 。请你合并所有重叠的区间，并返回 *一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间* 。

 

**示例 1：**

```
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
```

**示例 2：**

```
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
```

 

**提示：**

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 10^4`





```python
from typing import List
import sys

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 对区间进行排序
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

这里有几个需要注意的地方：
- `-sys.maxsize` 用于表示最小整数值。
- 类型注解（如 `List[List[int]]`）是可选的，但有助于提高代码的可读性和类型检查工具的效率。



## 2 选择不相交区间

### 2.1 题意描述

**选择不相交区间问题**大概题意就是：

给出一堆区间，要求选择**尽量多**的区间，使得这些区间**互不相交**，求可选取的区间的**最大数量**。这里端点相同也算有重复。

如下图所示：

![img](https://pic1.zhimg.com/80/v2-690f7e53fd34c39802f45f48b59d5c5a_1440w.webp)

<center>选择不相交区间问题示例：结果包含3个区间</center>

### 2.2 解题步骤

【**步骤一**】：按照区间**右端点**从小到大排序。

【**步骤二**】：从前往后依次枚举每个区间。

假设当前遍历到的区间为第i个区间 $[l_i,r_i]$，有以下两种情况：

- $l_i \le ed$：说明当前区间与前面区间有交集。因此直接跳过。
- $l_i > ed$: 说明当前区间与前面没有交集。因此选中当前区间，并设置 $ed = r_i$。



### LeetCode 435.无重叠区间（实例）

https://leetcode.cn/problems/non-overlapping-intervals/

给定一个区间的集合 `intervals` ，其中 `intervals[i] = [starti, endi]` 。返回 *需要移除区间的最小数量，使剩余区间互不重叠* 。

**注意** 只在一点上接触的区间是 **不重叠的**。例如 `[1, 2]` 和 `[2, 3]` 是不重叠的。

 

**示例 1:**

```
输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。
```

**示例 2:**

```
输入: intervals = [ [1,2], [1,2], [1,2] ]
输出: 2
解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
```

**示例 3:**

```
输入: intervals = [ [1,2], [2,3] ]
输出: 0
解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
```

 

**提示:**

- `1 <= intervals.length <= 10^5`
- `intervals[i].length == 2`
- `-5 * 10^4 <= starti < endi <= 5 * 10^4`





```python
from typing import List
import sys

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 按照右端点从小到大排序
        intervals.sort(key=lambda x: x[1])

        res = 0
        ed = -sys.maxsize
        
        for v in intervals:
            if ed <= v[0]:
                res += 1
                ed = v[1]

        return len(intervals) - res
```



## 3 区间选点问题

### 3.1 题意描述

**区间选点问题**大概题意就是：

给出一堆区间，取**尽量少**的点，使得每个区间内**至少有一个点**（不同区间内含的点可以是同一个，位于区间端点上的点也算作区间内）。

如下图所示：

![img](https://pica.zhimg.com/80/v2-a7ef021e1191ec53f20609ba870b44ba_1440w.webp)

<center>区间选点问题示例，最终至少选择3个点</center>



这个题可以转化为上一题的**求最大不相交区间**的数量。

对于这些**最大的不相交区间**，肯定是每个区间都需要选出一个点。而其他的区间都是和这些选出的区间有重复的，我们只需要把点的位置选在**重合**的部分即可。

也可以换一种思路：

我们将区间按照**右端点**从小到大排序，这时我们应该尽量选择**当前区间最右边的点**。

因为最右边的点可能和下面的其他区间重复，所以至少不比选择区间靠前位置的点差。

所以，最后的解法与选择不相交区间问题解法完全一样。

### 3.2 解题步骤

【**步骤一**】：按照区间右端点从小到大排序。

【**步骤二**】：从前往后依次枚举每个区间。

假设当前遍历到的区间为第i个区间 $[l_i,r_i]$，有以下两种情况：

- $l_i \le ed$：说明当前区间与前面区间有交集，前面已经选点了。因此直接跳过。
- $l_i > ed$: 说明当前区间与前面没有交集。因此选中当前区间，并设置 $ed = r_i$。



### LeetCode 452. 用最少量的箭引爆气球（实例）

https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/

有一些球形气球贴在一堵用 XY 平面表示的墙面上。墙面上的气球记录在整数数组 `points` ，其中`points[i] = [xstart, xend]` 表示水平直径在 `xstart` 和 `xend`之间的气球。你不知道气球的确切 y 坐标。

一支弓箭可以沿着 x 轴从不同点 **完全垂直** 地射出。在坐标 `x` 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  `xstart ≤ x ≤ xend`，则该气球会被 **引爆** 。可以射出的弓箭的数量 **没有限制** 。 弓箭一旦被射出之后，可以无限地前进。

给你一个数组 `points` ，*返回引爆所有气球所必须射出的 **最小** 弓箭数* 。

 

**示例 1：**

```
输入：points = [[10,16],[2,8],[1,6],[7,12]]
输出：2
解释：气球可以用2支箭来爆破:
-在x = 6处射出箭，击破气球[2,8]和[1,6]。
-在x = 11处发射箭，击破气球[10,16]和[7,12]。
```

**示例 2：**

```
输入：points = [[1,2],[3,4],[5,6],[7,8]]
输出：4
解释：每个气球需要射出一支箭，总共需要4支箭。
```

**示例 3：**

```
输入：points = [[1,2],[2,3],[3,4],[4,5]]
输出：2
解释：气球可以用2支箭来爆破:
- 在x = 2处发射箭，击破气球[1,2]和[2,3]。
- 在x = 4处射出箭，击破气球[3,4]和[4,5]。
```

 



**提示:**

- `1 <= points.length <= 105`
- `points[i].length == 2`
- `-231 <= xstart < xend <= 231 - 1`



```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 按照右端点从小到大排序
        points.sort(key=lambda x: x[1])

        res = 0
        ed = -sys.maxsize
        
        for v in points:
            if ed < v[0]:
                res += 1
                ed = v[1]

        return res
```



## 4 区间覆盖问题

### 4.1 题意描述

**区间覆盖问题**大概题意就是：

给出一堆区间和一个目标区间，问最少选择多少区间可以**覆盖**掉题中给出的这段目标区间。

如下图所示： 

![img](https://pic3.zhimg.com/80/v2-66041d9941667482fc51adeb4a616f64_1440w.webp)

<center>区间覆盖问题示例，最终至少选择2个区间才能覆盖目标区间</center>

### 4.2. 解题步骤

【**步骤一**】：按照区间左端点从小到大排序。

**步骤二**】：**从前往后**依次枚举每个区间，在所有能覆盖当前目标区间起始位置start的区间之中，选择**右端点**最大的区间。

假设右端点最大的区间是第$i$个区间，右端点为 $r_i$。

最后将目标区间的start更新成$r_i$



### LeetCode 1024. 视频拼接（实例）

https://leetcode.cn/problems/video-stitching/

你将会获得一系列视频片段，这些片段来自于一项持续时长为 `time` 秒的体育赛事。这些片段可能有所重叠，也可能长度不一。

使用数组 `clips` 描述所有的视频片段，其中 `clips[i] = [starti, endi]` 表示：某个视频片段开始于 `starti` 并于 `endi` 结束。

甚至可以对这些片段自由地再剪辑：

- 例如，片段 `[0, 7]` 可以剪切成 `[0, 1] + [1, 3] + [3, 7]` 三部分。

我们需要将这些片段进行再剪辑，并将剪辑后的内容拼接成覆盖整个运动过程的片段（`[0, time]`）。返回所需片段的最小数目，如果无法完成该任务，则返回 `-1` 。

 

**示例 1：**

```
输入：clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10
输出：3
解释：
选中 [0,2], [8,10], [1,9] 这三个片段。
然后，按下面的方案重制比赛片段：
将 [1,9] 再剪辑为 [1,2] + [2,8] + [8,9] 。
现在手上的片段为 [0,2] + [2,8] + [8,10]，而这些覆盖了整场比赛 [0, 10]。
```

**示例 2：**

```
输入：clips = [[0,1],[1,2]], time = 5
输出：-1
解释：
无法只用 [0,1] 和 [1,2] 覆盖 [0,5] 的整个过程。
```

**示例 3：**

```
输入：clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], time = 9
输出：3
解释： 
选取片段 [0,4], [4,7] 和 [6,9] 。
```

 

**提示：**

- `1 <= clips.length <= 100`
- `0 <= starti <= endi <= 100`
- `1 <= time <= 100`





```python
from typing import List

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # 对 clips 按起点升序排序
        clips.sort()

        st, ed = 0, time
        res = 0

        i = 0
        while i < len(clips) and st < ed:
            maxR = 0
            # 找到所有起点小于等于 st 的片段，并记录这些片段的最大终点 maxR
            while i < len(clips) and clips[i][0] <= st:
                maxR = max(maxR, clips[i][1])
                i += 1

            if maxR <= st:
                # 无法继续覆盖
                return -1

            # 更新 st 为 maxR，并增加结果计数
            st = maxR
            res += 1

            if maxR >= ed:
                # 已经覆盖到终点
                return res

        # 如果没有成功覆盖到终点
        return -1
```





## 5 区间分组问题

### 5.1 题意描述

**区间分组**问题大概题意就是：给出一堆区间，问最少可以将这些区间分成多少组使得每个组内的区间互不相交。

如下图所示： 

![img](https://pic2.zhimg.com/80/v2-6c6a045d481ddc44c66b046ef3e7d4cd_1440w.webp)

<center>区间分组问题示例，最少分成3个组</center>

### 5.2. 解题步骤

【**步骤一**】：按照区间左端点从小到大排序。

【**步骤二**】：从**前往后**依次枚举每个区间，判断当前区间能否被放到某个现有组里面。

（即判断是否存在某个组的右端点在当前区间之中。如果可以，则不能放到这一组）

假设现在已经分了 m 组了，第 k 组最右边的一个点是 $r_k$，当前区间的范围是 $[L_i,R_i]$ 。则：

如果$L_i \le r_k$ 则表示第 i 个区间无法放到第 k 组里面。反之，如果 $L_i > r_k$， 则表示可以放到第 k 组。

- 如果所有 m 个组里面没有组可以接收当前区间，则当前区间新开一个组，并把自己放进去。
- 如果存在可以接收当前区间的组 k，则将当前区间放进去，并更新当前组的 $r_k = R_i$。

**注意：**

为了能快速的找到能够接收当前区间的组，我们可以使用**优先队列 （小顶堆）**。

优先队列里面记录每个组的右端点值，每次可以在 O(1) 的时间拿到右端点中的的最小值。



### NC147 主持人调度（实例）

https://www.nowcoder.com/questionTerminal/4edf6e6d01554870a12f218c94e8a299

有 n 个活动即将举办，每个活动都有开始时间与活动的结束时间，第 i 个活动的开始时间是 starti ,第 i 个活动的结束时间是 endi ,举办某个活动就需要为该活动准备一个活动主持人。

一位活动主持人在同一时间只能参与一个活动。并且活动主持人需要全程参与活动，换句话说，一个主持人参与了第 i 个活动，那么该主持人在 (starti,endi) 这个时间段不能参与其他任何活动。求为了成功举办这 n 个活动，最少需要多少名主持人。

数据范围: $1≤n≤10^5 ， −2^{32}≤start_i≤end_i≤2^{31}$

复杂度要求：时间复杂度 O(nlog⁡n) ，空间复杂度 O(n)

示例1

**输入**

```
2,[[1,2],[2,3]]
```

**输出**

```
1
```

说明

```
只需要一个主持人就能成功举办这两个活动      
```

示例2

输入

```
2,[[1,3],[2,4]]
```

输出

```
2
```

说明

```
需要两个主持人才能成功举办这两个活动      
```

备注:

```
1≤n≤10^5
starti,endi在int范围内
```



```python
from typing import List
import heapq

class Solution:
    def minmumNumberOfHost(self, n: int, startEnd: List[List[int]]) -> int:
        # 按左端点从小到大排序
        startEnd.sort(key=lambda x: x[0])

        # 创建小顶堆
        q = []

        for i in range(n):
            if not q or q[0] > startEnd[i][0]:
                heapq.heappush(q, startEnd[i][1])
            else:
                heapq.heappop(q)
                heapq.heappush(q, startEnd[i][1])

        return len(q)
```



链接：https://www.nowcoder.com/questionTerminal/4edf6e6d01554870a12f218c94e8a299
来源：牛客网



解法2:

将活动开始时间写入一个列表starts，进行排序。 

将活动结束时间写入一个列表ends，进行排序。 

每次活动开始时，需要增加一个主持人上场，每次活动结束时候可以释放一个主持人。 

所以按照时间先后顺序对starts进行遍历，每次有活动开始count++，每次有活动结束count-- 

在count最大的时候，即是需要主持人最多的时候

```python
class Solution:
    def minmumNumberOfHost(self , n , startEnd ):
        starts=[]
        ends=[]
        for start,end in startEnd:
            starts.append(start);
            ends.append(end);
            
        starts.sort();
        ends.sort()
        
        i,j,count,res=0,0,0,0
        for time in starts:
            while(i<n and starts[i]<=time):
                i+=1
                count+=1
            while(j<n and ends[j]<=time):
                j+=1
                count-=1
            if res<count:
                res=count
        return res
```

