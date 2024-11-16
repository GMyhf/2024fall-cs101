# Problems in leetcode.cn

Updated 0216 GMT+8 Nov 17 2024

2024 fall, Complied by Hongfei Yan



> Logs:
>
> 2024/11/14, 尽量先刷 LeetCode热题100， https://leetcode.cn/studyplan/top-100-liked/



# 简单

## 1.两数之和

Hash Table, https://leetcode.cn/problems/two-sum/

给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值** *`target`* 的那 **两个** 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。

 

**示例 1：**

```
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
```

**示例 2：**

```
输入：nums = [3,2,4], target = 6
输出：[1,2]
```

**示例 3：**

```
输入：nums = [3,3], target = 6
输出：[0,1]
```

 

**提示：**

- `2 <= nums.length <= 10^4`
- `-109 <= nums[i] <= 10^9`
- `-109 <= target <= 10^9`
- **只会存在一个有效答案**

 

**进阶：**你可以想出一个时间复杂度小于 `O(n^2)` 的算法吗？



O(n^2)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return(i, j)
        
```



O(n)

```python
class Solution:    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in d:
                return(d[tmp], i)
            d[nums[i]] = i
```



## 70.爬楼梯

dp, https://leetcode.cn/problems/climbing-stairs/

假设你正在爬楼梯。需要 `n` 阶你才能到达楼顶。

每次你可以爬 `1` 或 `2` 个台阶。你有多少种不同的方法可以爬到楼顶呢？

 

**示例 1：**

```
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
```

**示例 2：**

```
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
```

 

**提示：**

- `1 <= n <= 45`



```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
            
        dp = [0]*(n+1)
        dp[1], dp[2]= 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
    
        return dp[n]
```



## 118.杨辉三角

dp, https://leetcode.cn/problems/pascals-triangle/

给定一个非负整数 *`numRows`，*生成「杨辉三角」的前 *`numRows`* 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

![img](https://pic.leetcode-cn.com/1626927345-DZmfxB-PascalTriangleAnimated2.gif)

 

**示例 1:**

```
输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

**示例 2:**

```
输入: numRows = 1
输出: [[1]]
```

 

**提示:**

- `1 <= numRows <= 30`



```python
 class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []
        for i in range(numRows):
            row = [None for _ in range(i+1)]
            row[0], row[-1] = 1, 1
            for j in range(1, len(row)-1):
                row[j] = tri[i-1][j-1] + tri[i-1][j]
            
            tri.append(row)
        
        return tri
        
```



## 283.零移动

two pointers, https://leetcode.cn/problems/move-zeroes/

给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。

**请注意** ，必须在不复制数组的情况下原地对数组进行操作。

 

**示例 1:**

```
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
```

**示例 2:**

```
输入: nums = [0]
输出: [0]
```

 

**提示**:

- `1 <= nums.length <= 104`
- `-231 <= nums[i] <= 231 - 1`

 

**进阶：**你能尽量减少完成的操作次数吗？



```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0; right = 0
        while left < len(nums) and right < len(nums):
            if not nums[left] and nums[right]:
                if left > right:
                    right += 1
                    continue
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
                continue
            if nums[left]:
                left += 1
            if not nums[right]:
                right += 1
```





## 2928.给小朋友们分糖果I

math, combinatorics, enumeration, https://leetcode.cn/problems/distribute-candies-among-children-i/

给你两个正整数 `n` 和 `limit` 。

请你将 `n` 颗糖果分给 `3` 位小朋友，确保没有任何小朋友得到超过 `limit` 颗糖果，请你返回满足此条件下的 **总方案数** 。

 

**示例 1：**

```
输入：n = 5, limit = 2
输出：3
解释：总共有 3 种方法分配 5 颗糖果，且每位小朋友的糖果数不超过 2 ：(1, 2, 2) ，(2, 1, 2) 和 (2, 2, 1) 。
```

**示例 2：**

```
输入：n = 3, limit = 3
输出：10
解释：总共有 10 种方法分配 3 颗糖果，且每位小朋友的糖果数不超过 3 ：(0, 0, 3) ，(0, 1, 2) ，(0, 2, 1) ，(0, 3, 0) ，(1, 0, 2) ，(1, 1, 1) ，(1, 2, 0) ，(2, 0, 1) ，(2, 1, 0) 和 (3, 0, 0) 。
```

 

**提示：**

- `1 <= n <= 50`
- `1 <= limit <= 50`



```python
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def backtrack(child: int, candies: int) -> int:
            if child == 3:
                # 当三位小朋友都分配完成，检查是否正好分配了 n 颗糖果
                return 1 if candies == n else 0

            ways = 0
            # 尝试分配给当前小朋友 [0, limit] 颗糖果
            for count in range(0, limit + 1):
                if candies + count <= n:
                    ways += backtrack(child + 1, candies + count)
                else:
                    break
            return ways

        # 开始分配糖果，初始为第 0 位小朋友和 0 颗糖果
        return backtrack(0, 0)

# 示例用法
if __name__ == "__main__":
    sol = Solution()
    print(sol.distributeCandies(5, 2))  # 输出: 3
    print(sol.distributeCandies(3, 3))  
```



```python
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        self.memo = {}

        def helper(n, k):
            if k == 0:
                return 1 if n == 0 else 0
            if (n, k) in self.memo:
                return self.memo[(n, k)]

            ways = 0
            for i in range(min(n, limit) + 1):
                ways += helper(n - i, k - 1)

            self.memo[(n, k)] = ways
            return ways

        return helper(n, 3)

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.distributeCandies(5, 2))  # 输出: 3
    print(sol.distributeCandies(3, 3))  
```



```python

```



```python

```



```python

```





# 中等



## 2.两数相加

linked list, https://leetcode.cn/problems/add-two-numbers/

给你两个 **非空** 的链表，表示两个非负的整数。它们每位数字都是按照 **逆序** 的方式存储的，并且每个节点只能存储 **一位** 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

 

**示例 1：**

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/02/addtwonumber1.jpg)

```
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
```

**示例 2：**

```
输入：l1 = [0], l2 = [0]
输出：[0]
```

**示例 3：**

```
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
```

 

**提示：**

- 每个链表中的节点数在范围 `[1, 100]` 内
- `0 <= Node.val <= 9`
- 题目数据保证列表表示的数字不含前导零



```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        n1, n2, carry, current = 0, 0, 0, head
        while l1 != None or l2 != None or carry != 0 :
            if l1 == None :
                n1 = 0
            else:
                n1 = l1.val
                l1 = l1.next
            
            if l2 == None :
                n2 = 0
            else:
                n2 = l2.val
                l2 = l2.next

            current.next = ListNode((n1 + n2 + carry) % 10)
            current = current.next
            carry = (n1 + n2 + carry) // 10
        
        return head.next
```

> 链表中的每个节点包含一个数字，数字按逆序存储，即个位数在链表的头部。
>
> **代码解读**
>
> ```python
> class Solution:
>     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
>         head = ListNode(0)
>         n1, n2, carry, current = 0, 0, 0, head
> ```
> - `Solution` 类包含一个方法 `addTwoNumbers`，该方法接受两个链表 `l1` 和 `l2` 作为参数，返回一个新的链表表示它们的和。
> - `head` 是结果链表的虚拟头节点，初始值为 0。
> - `n1` 和 `n2` 分别存储当前处理的 `l1` 和 `l2` 节点的值。
> - `carry` 存储进位值，初始为 0。
> - `current` 是当前处理的节点指针，初始指向 `head`。
>
> **主要逻辑**
>
> ```python
>         while l1 != None or l2 != None or carry != 0 :
>             if l1 == None :
>                 n1 = 0
>             else:
>                 n1 = l1.val
>                 l1 = l1.next
>             
>             if l2 == None :
>                 n2 = 0
>             else:
>                 n2 = l2.val
>                 l2 = l2.next
> 
>             current.next = ListNode((n1 + n2 + carry) % 10)
>             current = current.next
>             carry = (n1 + n2 + carry) // 10
> ```
> - 使用 `while` 循环，只要 `l1` 或 `l2` 还有剩余节点，或者 `carry` 不为 0，就继续处理。
> - 检查 `l1` 是否为空，如果为空则 `n1` 设为 0，否则 `n1` 设为 `l1` 当前节点的值，并将 `l1` 指针移动到下一个节点。
> - 检查 `l2` 是否为空，如果为空则 `n2` 设为 0，否则 `n2` 设为 `l2` 当前节点的值，并将 `l2` 指针移动到下一个节点。
> - 计算当前位的和 `n1 + n2 + carry`，并取模 10 得到当前位的结果，创建一个新的节点 `ListNode((n1 + n2 + carry) % 10)`，将其连接到结果链表的末尾。
> - 更新 `current` 指针，使其指向新创建的节点。
> - 更新 `carry`，计算新的进位值 `(n1 + n2 + carry) // 10`。
>
> **返回结果**
>
> ```python
>         return head.next
> ```
> - 最后返回 `head.next`，即结果链表的头节点。`head` 是虚拟头节点，实际结果从 `head.next` 开始。
>



## 3.无重复字符的最长子串

sliding window, https://leetcode.cn/problems/longest-substring-without-repeating-characters/

给定一个字符串 `s` ，请你找出其中不含有重复字符的 **最长** 

**子串**

 的长度。

 

**示例 1:**

```
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```

**示例 2:**

```
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```

**示例 3:**

```
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```

 

**提示：**

- `0 <= s.length <= 5 * 10^4`
- `s` 由英文字母、数字、符号和空格组成



**滑动窗口**

是一个队列，比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！如何移动？我们只要把队列的左边的元素移出就行了，直到满足题目要求！

一直维持这样的队列，找出队列出现最长的长度时候！时间复杂度：O(n)



滑动窗口是一种常用的算法技巧，用于解决数组或字符串中的子数组或子字符串问题。在下面的代码中，滑动窗口的概念体现在通过移动两个指针（起始指针和结束指针）来维护一个当前的无重复子串。

**滑动窗口的基本思想**

1. **初始化**：
   - 维护一个窗口 `[start + 1, i]`，表示当前的无重复子串。
   - 使用一个字典 `char_index` 来记录每个字符最近一次出现的位置。

2. **扩展窗口**：
   - 遍历字符串，逐个字符地扩展窗口的右边界 `i`。

3. **收缩窗口**：
   - 如果当前字符 `c` 在字典中且其上次出现的位置在当前窗口内，则需要收缩窗口的左边界 `start`，使其不包含重复字符。



```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 初始化变量
        start = -1  # 当前无重复子串的起始位置的前一个位置
        max_length = 0  # 最长无重复子串的长度
        char_index = {}  # 字典，记录每个字符最近一次出现的位置
        
        # 遍历字符串
        for i, char in enumerate(s):
            # 如果字符在字典中且上次出现的位置大于当前无重复子串的起始位置
            if char in char_index and char_index[char] > start:
                # 更新起始位置为该字符上次出现的位置
                start = char_index[char]
            
            # 更新字典中字符的位置
            char_index[char] = i
            
            # 计算当前无重复子串的长度，并更新最大长度
            current_length = i - start
            max_length = max(max_length, current_length)
        
        return max_length
```

> **代码解读**
>
> - `k`：记录当前无重复子串的起始位置的前一个位置，初始值为 -1。
> - `res`：记录最长无重复子串的长度，初始值为 0。
> - `c_dict`：一个字典，用于记录每个字符最近一次出现的位置。
>
> **处理字符**
>
> ```python
>             if c in c_dict and c_dict[c] > k:  # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
>                 k = c_dict[c]
>                 c_dict[c] = i
>             else:
>                 c_dict[c] = i
>                 res = max(res, i - k)
> ```
>
> - 条件判断：
>   - `if c in c_dict and c_dict[c] > k`：检查当前字符 `c` 是否在字典中，并且该字符上次出现的位置是否大于当前无重复子串的起始位置的前一个位置 `k`。
>   - 如果条件成立，说明当前字符 `c` 在之前的子串中已经出现过，且该位置在当前无重复子串的范围内，因此需要更新 `k` 为该字符上次出现的位置。
>   - `k = c_dict[c]`：更新 `k` 为字符 `c` 上次出现的位置。
>   - `c_dict[c] = i`：更新字典中字符 `c` 的位置为当前索引 `i`。
> - 否则：
>   - `c_dict[c] = i`：更新字典中字符 `c` 的位置为当前索引 `i`。
>   - `res = max(res, i - k)`：计算当前无重复子串的长度 `i - k`，并更新 `res` 为当前最大值。



## 11.盛最多水的容器

two pointers, https://leetcode.cn/problems/container-with-most-water/

给定一个长度为 `n` 的整数数组 `height` 。有 `n` 条垂线，第 `i` 条线的两个端点是 `(i, 0)` 和 `(i, height[i])` 。

找出其中的两条线，使得它们与 `x` 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

**说明：**你不能倾斜容器。

 

**示例 1：**

![img](https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/07/25/question_11.jpg)

```
输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
```

**示例 2：**

```
输入：height = [1,1]
输出：1
```

 

**提示：**

- `n == height.length`
- `2 <= n <= 105`
- `0 <= height[i] <= 104`



```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0;
        right = len(height) - 1
        ma = min(height[left], height[right]) * (right - left)
        while left < right:
            #print(ma,left,right)
            if height[left] < height[right]:
                left += 1
                ma = max(ma, min(height[left], height[right]) * (right - left))
                continue
            if height[right] < height[left]:
                right -= 1
                ma = max(ma, min(height[left], height[right]) * (right - left))
                continue

            ma = max(ma, min(height[left], height[right]) * (right - left))
            left += 1

        return ma
```



## 15.三数之和

two pointers, https://leetcode.cn/problems/3sum/

给你一个整数数组 `nums` ，判断是否存在三元组 `[nums[i], nums[j], nums[k]]` 满足 `i != j`、`i != k` 且 `j != k` ，同时还满足 `nums[i] + nums[j] + nums[k] == 0` 。请你返回所有和为 `0` 且不重复的三元组。

**注意：**答案中不可以包含重复的三元组。

 

 

**示例 1：**

```
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
```

**示例 2：**

```
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
```

**示例 3：**

```
输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
```

 

**提示：**

- `3 <= nums.length <= 3000`
- `-105 <= nums[i] <= 105`



```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort(reverse = True)

        ans = set()
        if nums[0] == 0 and nums[-1] == 0:
            return [[0,0,0]]
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if -nums[i] == nums[left] + nums[right]:
                    ans.add(tuple([nums[i], nums[left], nums[right]]))
                    left += 1
                
                if -nums[i] < nums[left] + nums[right]:
                    left += 1
                    continue
                if -nums[i] > nums[left] + nums[right]:
                    right -= 1
        
        return list(ans)
```



## 31.下一个排列

two pointers, https://leetcode.cn/problems/next-permutation/

整数数组的一个 **排列** 就是将其所有成员以序列或线性顺序排列。

- 例如，`arr = [1,2,3]` ，以下这些都可以视作 `arr` 的排列：`[1,2,3]`、`[1,3,2]`、`[3,1,2]`、`[2,3,1]` 。

整数数组的 **下一个排列** 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 **下一个排列** 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

- 例如，`arr = [1,2,3]` 的下一个排列是 `[1,3,2]` 。
- 类似地，`arr = [2,3,1]` 的下一个排列是 `[3,1,2]` 。
- 而 `arr = [3,2,1]` 的下一个排列是 `[1,2,3]` ，因为 `[3,2,1]` 不存在一个字典序更大的排列。

给你一个整数数组 `nums` ，找出 `nums` 的下一个排列。

必须**[ 原地 ](https://baike.baidu.com/item/原地算法)**修改，只允许使用额外常数空间。

 

**示例 1：**

```
输入：nums = [1,2,3]
输出：[1,3,2]
```

**示例 2：**

```
输入：nums = [3,2,1]
输出：[1,2,3]
```

**示例 3：**

```
输入：nums = [1,1,5]
输出：[1,5,1]
```

 

**提示：**

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`



```python
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: Find the first decreasing element from the end
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: If no such element is found, reverse the entire list
        if i == -1:
            nums.reverse()
            return
        
        # Step 3: Find the element just larger than nums[i] from the end
        j = len(nums) - 1
        while nums[i] >= nums[j]:
            j -= 1
        
        # Step 4: Swap the elements at indices i and j
        nums[i], nums[j] = nums[j], nums[i]
        
        # Step 5: Reverse the sublist after index i to get the next permutation
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
```

**具体步骤说明**：

1. **找到第一个下降的元素**：从后向前遍历，找到第一个满足 `nums[i] < nums[i + 1]` 的元素 `i`。
2. **判断是否需要完全反转**：如果 `i` 为 -1，说明整个数组是非递增的，直接反转即可得到下一个排列。
3. **找到比 `nums[i]` 大的最小元素**：从后向前遍历，找到第一个大于 `nums[i]` 的元素 `j`。
4. **交换 `nums[i]` 和 `nums[j]`**：交换这两个元素的位置。
5. **反转子数组**：反转 `i` 之后的部分，使其变为最小的排列。



## 49.字母异位词分组

hash table, sorting, https://leetcode.cn/problems/group-anagrams/

给你一个字符串数组，请你将 **字母异位词** 组合在一起。可以按任意顺序返回结果列表。

**字母异位词** 是由重新排列源单词的所有字母得到的一个新单词。

 

**示例 1:**

```
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**示例 2:**

```
输入: strs = [""]
输出: [[""]]
```

**示例 3:**

```
输入: strs = ["a"]
输出: [["a"]]
```

 

**提示：**

- `1 <= strs.length <= 104`
- `0 <= strs[i].length <= 100`
- `strs[i]` 仅包含小写字母



```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict 
        d = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(list(word)))
            d[key].append(word)
        
        ans = []
        for _, i in d.items():
            ans.append(i)
        return ans
```



## 54.螺旋矩阵

matrix, simulation, https://leetcode.cn/problems/spiral-matrix/

给你一个 `m` 行 `n` 列的矩阵 `matrix` ，请按照 **顺时针螺旋顺序** ，返回矩阵中的所有元素。

 

**示例 1：**

![img](https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg)

```
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
```

**示例 2：**

![img](https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg)

```
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
```

 

**提示：**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`





```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()
        
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






## 56.合并区间

intervals, https://leetcode.cn/problems/merge-intervals/

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







## 62.不同路径

dp, https://leetcode.cn/problems/unique-paths/

一个机器人位于一个 `m x n` 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

 

**示例 1：**

![img](https://pic.leetcode.cn/1697422740-adxmsI-image.png)

```
输入：m = 3, n = 7
输出：28
```

**示例 2：**

```
输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
```

**示例 3：**

```
输入：m = 7, n = 3
输出：28
```

**示例 4：**

```
输入：m = 3, n = 3
输出：6
```

 

**提示：**

- `1 <= m, n <= 100`
- 题目数据保证答案小于等于 `2 * 10^9`



dfs, dp都可以实现，但是dfs在`m=23,n=12`超时，dp数组初始化需要想明白。

将 cnt 作为类的属性来管理，或者将 cnt 作为参数传递给 dfs 函数。这里我们选择将 cnt 作为类的属性来管理，这样可以保持代码的清晰和简洁。 `self.cnt = 0` 不需要写在 `uniquePaths` 函数的内部，可以在类的初始化方法 `__init__` 中进行初始化。这样做可以确保每次创建新的 `Solution` 实例时，`cnt` 都会被重置为 0。

```python
# dfs 超时
class Solution:
    def __init__(self):
        self.cnt = 0

    def uniquePaths(self, m: int, n: int) -> int:
        dx = [0, 1]
        dy = [1, 0]
        visited = [[False] * n for _ in range(m)]

        def dfs(x, y):
            if x == m - 1 and y == n - 1:
                self.cnt += 1
                return
            visited[x][y] = True
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    dfs(nx, ny)
            visited[x][y] = False

        dfs(0, 0)
        return self.cnt

# 示例用法
if __name__ == "__main__":
    sol = Solution()
    m = 3
    n = 7
    print(sol.uniquePaths(m, n))  
```



使用深度优先搜索（DFS）来解决这个问题效率不高，特别是当网格很大时。这个问题可以通过动态规划（Dynamic Programming, DP）来更高效地解决。动态规划可以避免重复计算，并且时间复杂度为 O(m*n)。

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 创建一个二维数组 dp 来存储到达每个位置的路径数
        dp = [[1] * n for _ in range(m)]
        
        # 动态规划填表
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # 返回右下角的值，即从左上角到右下角的不同路径数
        return dp[-1][-1]

#m, n = map(int, input().split())

# 创建解决方案实例并调用方法
#solution = Solution()
#ans = solution.uniquePaths(m, n)

#print(ans)
```

使用动态规划来计算从左上角到右下角的不同路径数。我们创建了一个 `dp` 数组，其中 `dp[i][j]` 表示到达 `(i, j)` 位置的路径数。初始化时，所有第一行和第一列的值都设为 1，因为从起点到这些位置只有唯一的一条路径。然后，对于其他每个位置 `(i, j)`，其路径数等于从上方和左侧到达该位置的路径数之和。最后返回 `dp[m-1][n-1]` 即为所求的答案。



## 128.最长连续序列

hash table, https://leetcode.cn/problems/longest-consecutive-sequence/

给定一个未排序的整数数组 `nums` ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 `O(n)` 的算法解决此问题。

 

**示例 1：**

```
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
```

**示例 2：**

```
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
```

 

**提示：**

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`



```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
```



198.打家劫舍

dp, https://leetcode.cn/problems/house-robber/

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，**如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警**。

给定一个代表每个房屋存放金额的非负整数数组，计算你 **不触动警报装置的情况下** ，一夜之内能够偷窃到的最高金额。

 

**示例 1：**

```
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
```

**示例 2：**

```
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
```

 

**提示：**

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`



```python
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0, 0] for _ in range (len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            dp[i][0] = max(dp[i-1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i - 1]

        return (max(dp[-1][0], dp[-1][1]))

if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([2, 1, 1, 2])) # 3
```



## 279.完全平方数

dp, https://leetcode.cn/problems/perfect-squares

给你一个整数 `n` ，返回 *和为 `n` 的完全平方数的最少数量* 。

**完全平方数** 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，`1`、`4`、`9` 和 `16` 都是完全平方数，而 `3` 和 `11` 不是。

 

**示例 1：**

```
输入：n = 12
输出：3 
解释：12 = 4 + 4 + 4
```

**示例 2：**

```
输入：n = 13
输出：2
解释：13 = 4 + 9
```

 

**提示：**

- `1 <= n <= 104`



```python
class Solution:
    def numSquares(self, n: int) -> int:
        coins = [i * i for i in range(1, 101)]
        dp = [0] + [float('inf')] * n
        for i in range(1, n + 1):
            dp[i] = min(dp[i - c] for c in coins if c <= i) + 1

        return dp[n]

if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(12))
```



## 139.单词拆分

dp, https://leetcode.cn/problems/word-break/

给你一个字符串 `s` 和一个字符串列表 `wordDict` 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 `s` 则返回 `true`。

**注意：**不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

 

**示例 1：**

```
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
```

**示例 2：**

```
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。
```

**示例 3：**

```
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
```

 

**提示：**

- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 20`
- `s` 和 `wordDict[i]` 仅由小写英文字母组成
- `wordDict` 中的所有字符串 **互不相同**



```python
from typing import List
from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 作者：灵茶山艾府
        # https://leetcode.cn/problems/word-break/solutions/2968135/jiao-ni-yi-bu-bu-si-kao-dpcong-ji-yi-hua-chrs/

        max_len = max(map(len, wordDict))  # 用于限制下面 j 的循环次数
        words = set(wordDict)  # 便于快速判断 s[j:i] in words

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int) -> bool:
            if i == 0:  # 成功拆分！
                return True
            return any(s[j:i] in words and dfs(j)
                       for j in range(i - 1, max(i - max_len - 1, -1), -1))

        return dfs(len(s))

if __name__ == "__main__":
    sol = Solution()
    print(sol.wordBreak("leetcode", ["leet", "code"])) # True
    print(sol.wordBreak("applepenapple", ["apple", "pen"])) # True
    print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])) # False
    print(sol.wordBreak("cars", ["car", "ca", "rs"])) # True


```



## 152.乘积最大字数组

dp, https://leetcode.cn/problems/maximum-product-subarray/

给你一个整数数组 `nums` ，请你找出数组中乘积最大的非空连续 

子数组

（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。



测试用例的答案是一个 **32-位** 整数。

 

**示例 1:**

```
输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
```

**示例 2:**

```
输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
```

 

**提示:**

- `1 <= nums.length <= 2 * 104`
- `-10 <= nums[i] <= 10`
- `nums` 的任何子数组的乘积都 **保证** 是一个 **32-位** 整数



```python
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = min_product = result = nums[0]
        
        for num in nums[1:]:
            if num < 0:
                max_product, min_product = min_product, max_product
            
            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)
            
            result = max(result, max_product)
        
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct([2, 3, -2, 4])) # 6
    print(sol.maxProduct([-2, 0, -1])) # 0
```





## 300.最长递增子序列

dp, https://leetcode.cn/problems/longest-increasing-subsequence/

给你一个整数数组 `nums` ，找到其中最长严格递增子序列的长度。

**子序列** 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，`[3,6,2,7]` 是数组 `[0,3,1,6,2,2,7]` 的子序列。

 

**示例 1：**

```
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
```

**示例 2：**

```
输入：nums = [0,1,0,3,2,3]
输出：4
```

**示例 3：**

```
输入：nums = [7,7,7,7,7,7,7]
输出：1
```

 

**提示：**

- `1 <= nums.length <= 2500`
- `-104 <= nums[i] <= 104`

**进阶：**

- 你能将算法的时间复杂度降低到 `O(n log(n))` 吗?



```python
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])) # 4
```





## 322.零钱兑换

dp, https://leetcode.cn/problems/coin-change/

给你一个整数数组 `coins` ，表示不同面额的硬币；以及一个整数 `amount` ，表示总金额。

计算并返回可以凑成总金额所需的 **最少的硬币个数** 。如果没有任何一种硬币组合能组成总金额，返回 `-1` 。

你可以认为每种硬币的数量是无限的。

 

**示例 1：**

```
输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
```

**示例 2：**

```
输入：coins = [2], amount = 3
输出：-1
```

**示例 3：**

```
输入：coins = [1], amount = 0
输出：0
```

 

**提示：**

- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 231 - 1`
- `0 <= amount <= 104`



```python
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else float("inf") for c in coins]) + 1

        if dp[-1] == float("inf"):
            return -1
        else:
            return dp[-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.coinChange([1, 2, 5], 11)) # 3
```





## 376.摆动序列

greedy, dp, https://leetcode.cn/problems/wiggle-subsequence/

如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为 **摆动序列 。**第一个差（如果存在的话）可能是正数或负数。仅有一个元素或者含两个不等元素的序列也视作摆动序列。

- 例如， `[1, 7, 4, 9, 2, 5]` 是一个 **摆动序列** ，因为差值 `(6, -3, 5, -7, 3)` 是正负交替出现的。
- 相反，`[1, 4, 7, 2, 5]` 和 `[1, 7, 4, 5, 5]` 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。

**子序列** 可以通过从原始序列中删除一些（也可以不删除）元素来获得，剩下的元素保持其原始顺序。

给你一个整数数组 `nums` ，返回 `nums` 中作为 **摆动序列** 的 **最长子序列的长度** 。

 

**示例 1：**

```
输入：nums = [1,7,4,9,2,5]
输出：6
解释：整个序列均为摆动序列，各元素之间的差值为 (6, -3, 5, -7, 3) 。
```

**示例 2：**

```
输入：nums = [1,17,5,10,13,15,10,5,16,8]
输出：7
解释：这个序列包含几个长度为 7 摆动序列。
其中一个是 [1, 17, 10, 13, 10, 16, 8] ，各元素之间的差值为 (16, -7, 3, -3, 6, -8) 。
```

**示例 3：**

```
输入：nums = [1,2,3,4,5,6,7,8,9]
输出：2
```

 

**提示：**

- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 1000`

 

**进阶：**你能否用 `O(n)` 时间复杂度完成此题?



某个序列被称为「上升摆动序列」，当且仅当该序列是摆动序列，且最后一个元素呈上升趋势。如序列 [1,3,2,4] 即为「上升摆动序列」。

某个序列被称为「下降摆动序列」，当且仅当该序列是摆动序列，且最后一个元素呈下降趋势。如序列 [4,2,3,1] 即为「下降摆动序列」。

up[i] 表示以前 i 个元素中的某一个为结尾的最长的「上升摆动序列」的长度。

down[i] 表示以前 i 个元素中的某一个为结尾的最长的「下降摆动序列」的长度。

https://leetcode.cn/problems/wiggle-subsequence/solutions/518296/bai-dong-xu-lie-by-leetcode-solution-yh2m/

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        
        up = [1] + [0] * (n - 1)
        down = [1] + [0] * (n - 1)
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up[i] = max(up[i - 1], down[i - 1] + 1)
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                up[i] = up[i - 1]
                down[i] = max(up[i - 1] + 1, down[i - 1])
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]
        
        return max(up[n - 1], down[n - 1])

```



利用动态规划分别记录到每个位置的最长摆动序列长度（up 和 down），并且在每一步保持这两个数组的更新。由于在摆动序列中，当前状态只能是“上升”或“下降”，因此这种方法可以保证 up 和 down 之间的差值不会超过 1。

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        up = [1] + [0] * (n - 1)
        down = [1] + [0] * (n - 1)
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                up[i] = up[i - 1]
                down[i] = up[i - 1] + 1
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]

        return max(up[n - 1], down[n - 1])
```



**Plan**

1. Initialize two variables `up` and `down` to 1. These will keep track of the length of the longest wiggle subsequence ending with an upward or downward wiggle, respectively.
2. Iterate through the `nums` array starting from the second element.
3. For each element, compare it with the previous element:
   - If the current element is greater than the previous element, update `up` to `down + 1`.
   - If the current element is less than the previous element, update `down` to `up + 1`.
4. The result will be the maximum value between `up` and `down`.

这个算法实际上结合了贪心（Greedy）和动态规划（Dynamic Programming, DP）的思想。让我们详细分析一下：

贪心（Greedy）思想

贪心算法通常在每一步选择局部最优解，希望最终得到全局最优解。在这个问题中，每当我们遇到一个上升或下降的摆动时，我们都会立即更新 up 或 down，这看起来像是贪心的选择。

动态规划（DP）思想

动态规划通过将问题分解成子问题，并保存子问题的解来避免重复计算。在这个问题中，up 和 down 分别表示以当前元素结尾的最长上升摆动序列和最长下降摆动序列的长度，这是典型的动态规划状态定义。

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        up = down = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1

        return max(up, down)
```



## 416.分割等和子集

dp, https://leetcode.cn/problems/partition-equal-subset-sum

给你一个 **只包含正整数** 的 **非空** 数组 `nums` 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

 

**示例 1：**

```
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
```

**示例 2：**

```
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。
```

 

**提示：**

- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 100`



这个0-1背包，有视频讲解。416. 分割等和子集，https://leetcode.cn/problems/partition-equal-subset-sum

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sum_v = sum(nums)
        if sum_v & 1:
            return False
        
        target = sum_v // 2
        dp = [[False]*(target+1) for _ in range(n)]
        if nums[0] <= target:
            dp[0][nums[0]] = True
        for i in range(1, n):
            for j in range(target + 1):
                
                if j > nums[i]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
            if dp[i][target]:
                return True
        
        return dp[-1][target]
```



## 435.无重叠区间

intervals, https://leetcode.cn/problems/non-overlapping-intervals/

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





## 452. 用最少量的箭引爆气球

intervals, https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/

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





## 1024. 视频拼接

intervals, https://leetcode.cn/problems/video-stitching/

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





## 1552.两球之间的磁力

binary search, https://leetcode.cn/problems/magnetic-force-between-two-balls/

在代号为 C-137 的地球上，Rick 发现如果他将两个球放在他新发明的篮子里，它们之间会形成特殊形式的磁力。Rick 有 `n` 个空的篮子，第 `i` 个篮子的位置在 `position[i]` ，Morty 想把 `m` 个球放到这些篮子里，使得任意两球间 **最小磁力** 最大。

已知两个球如果分别位于 `x` 和 `y` ，那么它们之间的磁力为 `|x - y|` 。

给你一个整数数组 `position` 和一个整数 `m` ，请你返回最大化的最小磁力。

 

**示例 1：**

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/16/q3v1.jpg)

```
输入：position = [1,2,3,4,7], m = 3
输出：3
解释：将 3 个球分别放入位于 1，4 和 7 的三个篮子，两球间的磁力分别为 [3, 3, 6]。最小磁力为 3 。我们没办法让最小磁力大于 3 。
```

**示例 2：**

```
输入：position = [5,4,3,2,1,1000000000], m = 2
输出：999999999
解释：我们使用位于 1 和 1000000000 的篮子时最小磁力最大。
```

 

**提示：**

- `n == position.length`
- `2 <= n <= 10^5`
- `1 <= position[i] <= 10^9`
- 所有 `position` 中的整数 **互不相同** 。
- `2 <= m <= position.length`



```python
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def check(x):
            cnt, pre = 1, position[0]
            for i in range(1,len(position)):
                if position[i] - pre >= x:
                    cnt += 1
                    pre = position[i]
            
            return cnt >= m

        # https://github.com/python/cpython/blob/main/Lib/bisect.py
        lo = 1
        hi = position[-1] - position[0] + 1
        ans = 1
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):      #
                ans = mid       # 如果cnt>=m, mid就是答案
                lo = mid + 1    # 所以lo可以置为 mid + 1。
            else:
                hi = mid

        return ans

```



```python

```



```python

```



```python

```



```python

```





# 困难

## 32.最长有效括号

stack, dp, https://leetcode.cn/problems/longest-valid-parentheses/

给你一个只包含 `'('` 和 `')'` 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

**示例 1：**

```
输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"
```

**示例 2：**

```
输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
```

**示例 3：**

```
输入：s = ""
输出：0
```

 

**提示：**

- `0 <= s.length <= 3 * 104`
- `s[i]` 为 `'('` 或 `')'`





stack解法

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # 初始化栈，-1表示上一个未匹配右括号的位置
        max_length = 0  # 记录最长有效括号长度
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # 左括号入栈
            else:
                stack.pop()  # 右括号尝试匹配
                if not stack:
                    stack.append(i)  # 如果栈为空，更新为当前右括号位置
                else:
                    max_length = max(max_length, i - stack[-1])  # 更新最大长度
        
        return max_length

if __name__ == "__main__":
    sol = Solution()
    s = "()()"
    print(sol.longestValidParentheses(s))  # 输出应该是 4
```



## 42.接雨水

monotonic stack, https://leetcode.cn/problems/trapping-rain-water/

给定 `n` 个非负整数表示每个宽度为 `1` 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

 

**示例 1：**

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png)

```
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
```

**示例 2：**

```
输入：height = [4,2,0,3,2,5]
输出：9
```

 

**提示：**

- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`



**单调栈其实就是在栈的基础上，维持一个栈内元素单调。**

> https://github.com/SharingSource/LogicStack-LeetCode
>
> 在这道题，由于需要找某个位置两侧比其高的柱子（只有两侧有比当前位置高的柱子，当前位置才能接下雨水），我们可以维持栈内元素的单调递减。
>
> **PS.找某侧最近一个比其大的值，使用单调栈维持栈内元素递减；找某侧最近一个比其小的值使用单调栈维持栈内元素递增 ….**
>
> 当某个位置的元素弹出栈时，例如位置 a ，我们自然可以得到 a 位置两侧比 a 高的柱子：
>
> - 一个是导致 a位置元素弹出的柱子( a右侧比 a高的柱子)
> - 一个是 a弹栈后的栈顶元素(a 左侧比 a 高的柱子)
>
> 当有了 a 左右两侧比 a 高的柱子后，便可计算 a 位置可接下的雨水量。
>



```python
class Solution:
    def trap(self, height: List[int]) -> int:
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
        return water
```



> 这段代码实现了一个算法，用于计算给定高度数组 `height` 中可以 trapping 的雨水总量。这个算法使用了栈来高效地解决这个问题。
>
> **代码解读**
>
> **处理栈中的元素**
>
> ```python
>         while stack and height[i] > height[stack[-1]]:
> ```
> - 当栈不为空且当前高度 `height[i]` 大于栈顶元素对应的高度 `height[stack[-1]]` 时，进入循环。
>
> **弹出栈顶元素**
>
> ```python
>             top = stack.pop()
> ```
> - 弹出栈顶元素 `top`，`top` 是当前高度较低的柱子的索引。
>
> **检查栈是否为空**
>
> ```python
>             if not stack:
>                 break
> ```
> - 如果栈为空，说明没有更高的柱子可以形成积水区域，跳出循环。
>
> **计算积水区域**
>
> ```python
>             distance = i - stack[-1] - 1
>             bounded_height = min(height[i], height[stack[-1]]) - height[top]
>             water += distance * bounded_height
> ```
> - `distance`：计算当前柱子 `i` 和栈顶柱子 `stack[-1]` 之间的距离，减去 1 是因为不包括两端的柱子。
> - `bounded_height`：计算当前柱子 `i` 和栈顶柱子 `stack[-1]` 之间的最小高度，减去弹出的柱子 `top` 的高度，得到积水的高度。
> - `water += distance * bounded_height`：计算当前积水区域的水量，并累加到 `water` 中。
>









## 65.有效数字

string, https://leetcode.cn/problems/valid-number/

给定一个字符串 `s` ，返回 `s` 是否是一个 **有效数字**。

例如，下面的都是有效数字：`"2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"`，而接下来的不是：`"abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"`。

一般的，一个 **有效数字** 可以用以下的规则之一定义：

1. 一个 **整数** 后面跟着一个 **可选指数**。
2. 一个 **十进制数** 后面跟着一个 **可选指数**。

一个 **整数** 定义为一个 **可选符号** `'-'` 或 `'+'` 后面跟着 **数字**。

一个 **十进制数** 定义为一个 **可选符号** `'-'` 或 `'+'` 后面跟着下述规则：

1. **数字** 后跟着一个 **小数点 `.`**。
2. **数字** 后跟着一个 **小数点 `.`** 再跟着 **数位**。
3. 一个 **小数点 `.`** 后跟着 **数位**。

**指数** 定义为指数符号 `'e'` 或 `'E'`，后面跟着一个 **整数**。

**数字** 定义为一个或多个数位。

 

**示例 1：**

**输入：**s = "0"

**输出：**true

**示例 2：**

**输入：**s = "e"

**输出：**false

**示例 3：**

**输入：**s = "."

**输出：**false

 

**提示：**

- `1 <= s.length <= 20`
- `s` 仅含英文字母（大写和小写），数字（`0-9`），加号 `'+'` ，减号 `'-'` ，或者点 `'.'` 。





```python
class Solution:
    def isNumber(self, s: str) -> bool:
        import re 
        pattern = r'^[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?$'
        
        ans = re.match(pattern, s) 
        if ans is not None:
            return True
        else:
            return False
```

**正则表达式模式解析**

- `^`：表示字符串的开始。
- `[-+]?`：表示可选的正负号，`?` 表示前面的字符可以出现 0 次或 1 次。
- `(\d+(\.\d*)?|\.\d+)`：表示数字部分，可以是以下两种形式之一：
  - `\d+(\.\d*)?`：整数部分后面可以跟一个小数部分，小数部分可以为空。
  - `\.\d+`：纯小数部分，必须以小数点开头，后面跟着至少一个数字。
- `([eE][-+]?\d+)?`：表示可选的指数部分，`?`表示前面的整个部分可以出现 0 次或 1 次。
  - `[eE]`：表示指数符号，可以是小写 `e` 或大写 `E`。
  - `[-+]?\d+`：表示指数部分的数字，可以带正负号，后面必须跟着至少一个数字。
- `$`：表示字符串的结束。



## 76.最小覆盖子串

sliding window, https://leetcode.cn/problems/minimum-window-substring/description/

给你一个字符串 `s` 、一个字符串 `t` 。返回 `s` 中涵盖 `t` 所有字符的最小子串。如果 `s` 中不存在涵盖 `t` 所有字符的子串，则返回空字符串 `""` 。

 

**注意：**

- 对于 `t` 中重复字符，我们寻找的子字符串中该字符数量必须不少于 `t` 中该字符数量。
- 如果 `s` 中存在这样的子串，我们保证它是唯一的答案。

 

**示例 1：**

```
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
```

**示例 2：**

```
输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。
```

**示例 3:**

```
输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
```

 

**提示：**

- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 105`
- `s` 和 `t` 由英文字母组成

 

**进阶：**你能设计一个在 `o(m+n)` 时间内解决此问题的算法吗？



在字符串 `s` 中找到包含 `t` 中所有字符的最小子串。具体地，使用滑动窗口算法，左右指针逐渐扩大窗口，找到满足条件的子串并逐步优化结果，最后返回最小子串。

```python
from collections import defaultdict

class Solution:
    def __init__(self):
        self.ori = defaultdict(int)
        self.cnt = defaultdict(int)

    def check(self):
        for char, count in self.ori.items():
            if self.cnt[char] < count:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        # 初始化 ori 字典
        for c in t:
            self.ori[c] += 1

        l, r = 0, -1
        len_min = float('inf')
        ansL, ansR = -1, -1

        while r < len(s):
            r += 1
            if r < len(s) and s[r] in self.ori:
                self.cnt[s[r]] += 1

            while self.check() and l <= r:
                if r - l + 1 < len_min:
                    len_min = r - l + 1
                    ansL = l
                if s[l] in self.ori:
                    self.cnt[s[l]] -= 1
                l += 1

        return s[ansL:ansL + len_min] if ansL != -1 else ""

# 示例用法
# sol = Solution()
# s = "ADOBECODEBANC"
# t = "ABC"
# print(sol.minWindow(s, t))  # 输出: "BANC"
```



## 135.分发糖果

greedy, https://leetcode.cn/problems/candy/

`n` 个孩子站成一排。给你一个整数数组 `ratings` 表示每个孩子的评分。

你需要按照以下要求，给这些孩子分发糖果：

- 每个孩子至少分配到 `1` 个糖果。
- 相邻两个孩子评分更高的孩子会获得更多的糖果。

请你给每个孩子分发糖果，计算并返回需要准备的 **最少糖果数目** 。

 

**示例 1：**

```
输入：ratings = [1,0,2]
输出：5
解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。
```

**示例 2：**

```
输入：ratings = [1,2,2]
输出：4
解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。
```

 

**提示：**

- `n == ratings.length`
- `1 <= n <= 2 * 10^4`
- `0 <= ratings[i] <= 2 * 10^4`



贪心算法。通过两次遍历 ratings 数组来确保每个孩子获得的糖果数量满足题目要求：  
第一次遍历（从左到右）：确保每个孩子的糖果数量至少比左边评分低的孩子多。
第二次遍历（从右到左）：确保每个孩子的糖果数量至少比右边评分低的孩子多。
通过这两次遍历，算法能够在 O(n) 时间复杂度内计算出满足条件的最少糖果数目。

```python
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # Traverse from left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Traverse from right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
```



## 629.K个逆序对数组

dp, https://leetcode.cn/problems/k-inverse-pairs-array/description/

对于一个整数数组 `nums`，**逆序对**是一对满足 `0 <= i < j < nums.length` 且 `nums[i] > nums[j]`的整数对 `[i, j]` 。

给你两个整数 `n` 和 `k`，找出所有包含从 `1` 到 `n` 的数字，且恰好拥有 `k` 个 **逆序对** 的不同的数组的个数。由于答案可能很大，只需要返回对 `109 + 7` 取余的结果。

 

**示例 1：**

```
输入：n = 3, k = 0
输出：1
解释：
只有数组 [1,2,3] 包含了从1到3的整数并且正好拥有 0 个逆序对。
```

**示例 2：**

```
输入：n = 3, k = 1
输出：2
解释：
数组 [1,3,2] 和 [2,1,3] 都有 1 个逆序对。
```

 

**提示：**

- `1 <= n <= 1000`
- `0 <= k <= 1000`



通过动态规划来解决。需要计算包含从 `1` 到 `n` 的数字且恰好拥有 `k` 个逆序对的不同数组的个数。由于答案可能非常大，需要对 `10^9 + 7` 取模。

**动态规划思路**

1. **状态定义**：
   - `dp[i][j]` 表示使用前 `i` 个数字（即 `1` 到 `i`）组成的数组中，恰好有 `j` 个逆序对的数组个数。

2. **状态转移**：
   - 当我们在前 `i-1` 个数字的基础上添加第 `i` 个数字时，第 `i` 个数字可以放在任意位置。假设第 `i` 个数字放在第 `m` 个位置（从 0 开始计数），那么它会与前面的 `m` 个数字形成逆序对。
   - 因此，`dp[i][j]` 可以通过 `dp[i-1][j-m]` 转移过来，其中 `m` 的范围是从 `0` 到 `min(i-1, j)`。

3. **初始化**：
   - `dp[0][0] = 1`，表示使用 0 个数字时，恰好有 0 个逆序对的数组个数为 1（空数组）。
   - 其他 `dp[0][j]` 均为 0，因为使用 0 个数字时不可能有逆序对。

4. **优化**：
   - 直接计算 `dp[i][j]` 时可能会超时，因此我们可以使用前缀和来优化状态转移。

### 

```python
class Solusion:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 1000000007
        # 初始化 dp 数组
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        # 动态规划转移
        for i in range(1, n + 1):
            prefix_sum = [0] * (k + 2)
            for j in range(k + 1):
                prefix_sum[j + 1] = (prefix_sum[j] + dp[i - 1][j]) % MOD

            for j in range(k + 1):
                dp[i][j] = (prefix_sum[j + 1] - (prefix_sum[j + 1 - i] if j + 1 - i >= 0 else 0)) % MOD

        return dp[n][k]


```

> **代码解释**
>
> 1. **初始化**：
>    - `dp = [[0] * (k + 1) for _ in range(n + 1)]`：创建一个 `(n + 1) x (k + 1)` 的二维数组，初始值为 0。
>    - `dp[0][0] = 1`：使用 0 个数字时，恰好有 0 个逆序对的数组个数为 1。
>
> 2. **前缀和数组**：
>    - `prefix_sum = [0] * (k + 2)`：用于存储前缀和，方便快速计算区间和。
>    - `for j in range(k + 1): prefix_sum[j + 1] = (prefix_sum[j] + dp[i - 1][j]) % MOD`：计算前缀和。
>
> 3. **状态转移**：
>    - `for j in range(k + 1): dp[i][j] = (prefix_sum[j + 1] - (prefix_sum[j + 1 - i] if j + 1 - i >= 0 else 0)) % MOD`：使用前缀和优化状态转移。
>
> 4. **返回结果**：
>    - `return dp[n][k]`：返回最终结果。
>
> **优化说明**
>
> - **前缀和**：通过前缀和数组，可以在 O(1) 时间内计算出 `dp[i-1][j-m]` 的和，从而将时间复杂度从 O(n * k * k) 优化到 O(n * k)。
>



### 

```python
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 1000000007

        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[1][0] = 1
        for i in range(2, n + 1):
            for j in range(min(k, i * (i - 1) // 2) + 1):
                #for x in range(max(0, j - i + 1), j + 1):
                    #dp[i][j] = (dp[i][j] + dp[i - 1][x]) % MOD
                dp[i][j] = ((dp[i][j - 1] if j >= 1 else 0) + dp[i - 1][j] - (dp[i - 1][j - i] if j >= i else 0) + MOD) % MOD

        return dp[n][k]
```



> 该代码实现了一个解决 `k` 个逆序对数组问题的动态规划算法。以下是代码的详细解释：
>
> **代码解释**
>
> 1. **定义常量和初始化 DP 数组**：
>    ```python
>    MOD = 1000000007
>    dp = [[0] * (k + 1) for _ in range(n + 1)]
>    dp[1][0] = 1
>    ```
>    - `MOD` 是用来取模的常量，防止结果溢出。
>    - `dp` 是一个二维数组，`dp[i][j]` 表示使用 `1` 到 `i` 的数字，恰好有 `j` 个逆序对的数组个数。
>    - 初始化 `dp[1][0]` 为 `1`，因为只有一个元素时，没有逆序对。
>
> 2. **填充 DP 数组**：
>    ```python
>    for i in range(2, n + 1):
>        for j in range(min(k, i * (i - 1) // 2) + 1):
>            dp[i][j] = ((dp[i][j - 1] if j >= 1 else 0) + dp[i - 1][j] - (dp[i - 1][j - i] if j >= i else 0) + MOD) % MOD
>    ```
>    - 外层循环 `i` 从 `2` 到 `n`，表示当前考虑的数字范围是 `1` 到 `i`。
>    - 内层循环 `j` 从 `0` 到 `min(k, i * (i - 1) // 2)`，表示当前考虑的逆序对数量。
>    - `dp[i][j]` 的值通过以下公式计算：
>      - `dp[i][j - 1] if j >= 1 else 0`：前一个逆序对数量的值。
>      - `dp[i - 1][j]`：不包含当前数字 `i` 的逆序对数量。
>      - `-(dp[i - 1][j - i] if j >= i else 0)`：减去多余的部分。
>      - `+ MOD`：防止负数出现。
>      - `% MOD`：取模操作，防止结果溢出。
>
> 3. **返回结果**：
>    ```python
>    return dp[n][k]
>    ```
>    - 返回 `dp[n][k]`，即使用 `1` 到 `n` 的数字，恰好有 `k` 个逆序对的数组个数。
>







```python

```









```python

```







```python

```







```python

```

