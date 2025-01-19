# Problems in leetcode.cn

Updated 0054 GMT+8 Jan 20 2025

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



## 20.有效的括号

stack, https://leetcode.cn/problems/valid-parentheses/

给定一个只包括 `'('`，`')'`，`'{'`，`'}'`，`'['`，`']'` 的字符串 `s` ，判断字符串是否有效。

有效字符串需满足：

1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。
3. 每个右括号都有一个对应的相同类型的左括号。

 

**示例 1：**

**输入：**s = "()"

**输出：**true

**示例 2：**

**输入：**s = "()[]{}"

**输出：**true

**示例 3：**

**输入：**s = "(]"

**输出：**false

**示例 4：**

**输入：**s = "([])"

**输出：**true

 

**提示：**

- `1 <= s.length <= 104`
- `s` 仅由括号 `'()[]{}'` 组成



```python
from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if not stack:
                    return False
                if c == ')' and stack[-1] != '(':
                    return False
                if c == ']' and stack[-1] != '[':
                    return False
                if c == '}' and stack[-1] != '{':
                    return False
                stack.pop()
        return not stack
```



## 21.合并两个有序链表

https://leetcode.cn/problems/merge-two-sorted-lists/

将两个升序链表合并为一个新的 **升序** 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

**示例 1：**

![img](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

```
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
```

**示例 2：**

```
输入：l1 = [], l2 = []
输出：[]
```

**示例 3：**

```
输入：l1 = [], l2 = [0]
输出：[0]
```

 

**提示：**

- 两个链表的节点数目范围是 `[0, 50]`
- `-100 <= Node.val <= 100`
- `l1` 和 `l2` 均按 **非递减顺序** 排列



```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个哨兵节点（dummy node），简化边界条件处理
        prehead = ListNode(-200)
        prev = prehead

        # 遍历两个链表直到其中一个为空
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next            
            prev = prev.next

        # 连接还未遍历完的那个链表
        prev.next = list1 if list1 is not None else list2

        # 返回合并后的链表，跳过哨兵节点
        return prehead.next
```



## 35.搜索插入位置

binary search, https://leetcode.cn/problems/search-insert-position/

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 `O(log n)` 的算法。

 

**示例 1:**

```
输入: nums = [1,3,5,6], target = 5
输出: 2
```

**示例 2:**

```
输入: nums = [1,3,5,6], target = 2
输出: 1
```

**示例 3:**

```
输入: nums = [1,3,5,6], target = 7
输出: 4
```

 

**提示:**

- `1 <= nums.length <= 104`
- `-104 <= nums[i] <= 104`
- `nums` 为 **无重复元素** 的 **升序** 排列数组
- `-104 <= target <= 104`



```python
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0;
        hi = len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid

        return lo

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1,3], 2)) # 1
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



## 94.二叉树的中序遍历

https://leetcode.cn/problems/binary-tree-inorder-traversal/

给定一个二叉树的根节点 `root` ，返回 *它的 **中序** 遍历* 。

 

**示例 1：**

<img src="https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg" alt="img" style="zoom: 50%;" />

```
输入：root = [1,null,2,3]
输出：[1,3,2]
```

**示例 2：**

```
输入：root = []
输出：[]
```

**示例 3：**

```
输入：root = [1]
输出：[1]
```

 

**提示：**

- 树中节点数目在范围 `[0, 100]` 内
- `-100 <= Node.val <= 100`



```python
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return result
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



​	

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



维护最左边的空位的位置（下标）。

从左到右遍历 `nums[i]`。同时维护另一个下标 $i_0$（初始值为 0），并保证下标区间 $[i_0,i−1]$ 都是空位，且 $i_0$指向最左边的空位。

每次遇到 nums[i]≠0 的情况，就把 nums[i] 移动到最左边的空位上，也就是交换 nums[i] 和 $nums[i_0]$。交换后把 $i_0$和 i 都加一，从而使【[$i_0$ ,i−1] 都是空位】这一性质仍然成立。

如果 nums[i]=0，无需交换，只把 i 加一。

https://leetcode.cn/problems/move-zeroes/solutions/2969353/kuai-man-zhi-zhen-wei-shi-yao-ke-yi-ba-s-1h8x/

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i0 = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[i0] = nums[i0], nums[i]
                i0 += 1

```





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



## 121.买卖股票的最佳时机

dp, https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/

给定一个数组 `prices` ，它的第 `i` 个元素 `prices[i]` 表示一支给定股票第 `i` 天的价格。

你只能选择 **某一天** 买入这只股票，并选择在 **未来的某一个不同的日子** 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 `0` 。

 

**示例 1：**

```
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
```

**示例 2：**

```
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
```

 

**提示：**

- `1 <= prices.length <= 105`
- `0 <= prices[i] <= 104`



```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minv = prices[0]
        maxProfit = 0
        for p in prices:
            if p < minv:
                minv = p
            else:
                maxProfit = max(p - minv, maxProfit)
        
        return maxProfit
```



## 136.只出现一次的数字

https://leetcode.cn/problems/single-number/

给你一个 **非空** 整数数组 `nums` ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

 

**示例 1 ：**

```
输入：nums = [2,2,1]
输出：1
```

**示例 2 ：**

```
输入：nums = [4,1,2,1,2]
输出：4
```

**示例 3 ：**

```
输入：nums = [1]
输出：1
```

 

**提示：**

- `1 <= nums.length <= 3 * 104`
- `-3 * 104 <= nums[i] <= 3 * 104`
- 除了某个元素只出现一次以外，其余每个元素均出现两次。





```python
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            if i in s:
                s.remove(i)
            else:
                s.add(i)

        return s.pop()
```



## 141.环形链表

https://leetcode.cn/problems/linked-list-cycle/

给你一个链表的头节点 `head` ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。**注意：`pos` 不作为参数进行传递** 。仅仅是为了标识链表的实际情况。

*如果链表中存在环* ，则返回 `true` 。 否则，返回 `false` 。

 

**示例 1：**

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png)

```
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
```

**示例 2：**

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png)

```
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
```

**示例 3：**

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png)

```
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
```

 

**提示：**

- 链表中节点的数目范围是 `[0, 10^4]`
- `-10^5 <= Node.val <= 10^5`
- `pos` 为 `-1` 或者链表中的一个 **有效索引** 。



```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        while head:
            if head in visited:
                return True

            visited.add(head)
            head = head.next
        return False
        
```



## 160.相交链表

https://leetcode.cn/problems/intersection-of-two-linked-lists/

给你两个单链表的头节点 `headA` 和 `headB` ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 `null` 。

图示两个链表在节点 `c1` 开始相交**：**

[![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_statement.png)](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_statement.png)

题目数据 **保证** 整个链式结构中不存在环。

**注意**，函数返回结果后，链表必须 **保持其原始结构** 。

**自定义评测：**

**评测系统** 的输入如下（你设计的程序 **不适用** 此输入）：

- `intersectVal` - 相交的起始节点的值。如果不存在相交节点，这一值为 `0`
- `listA` - 第一个链表
- `listB` - 第二个链表
- `skipA` - 在 `listA` 中（从头节点开始）跳到交叉节点的节点数
- `skipB` - 在 `listB` 中（从头节点开始）跳到交叉节点的节点数

评测系统将根据这些输入创建链式数据结构，并将两个头节点 `headA` 和 `headB` 传递给你的程序。如果程序能够正确返回相交节点，那么你的解决方案将被 **视作正确答案** 。

 

**示例 1：**

[![img](https://assets.leetcode.com/uploads/2021/03/05/160_example_1_1.png)](https://assets.leetcode.com/uploads/2018/12/13/160_example_1.png)

```
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,6,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
— 请注意相交节点的值不为 1，因为在链表 A 和链表 B 之中值为 1 的节点 (A 中第二个节点和 B 中第三个节点) 是不同的节点。换句话说，它们在内存中指向两个不同的位置，而链表 A 和链表 B 中值为 8 的节点 (A 中第三个节点，B 中第四个节点) 在内存中指向相同的位置。
```

 

**示例 2：**

[![img](https://assets.leetcode.com/uploads/2021/03/05/160_example_2.png)](https://assets.leetcode.com/uploads/2018/12/13/160_example_2.png)

```
输入：intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Intersected at '2'
解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [1,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
```

**示例 3：**

[![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_example_3.png)](https://assets.leetcode.com/uploads/2018/12/13/160_example_3.png)

```
输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：No intersection
解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
这两个链表不相交，因此返回 null 。
```

 

**提示：**

- `listA` 中节点数目为 `m`
- `listB` 中节点数目为 `n`
- `1 <= m, n <= 3 * 104`
- `1 <= Node.val <= 105`
- `0 <= skipA <= m`
- `0 <= skipB <= n`
- 如果 `listA` 和 `listB` 没有交点，`intersectVal` 为 `0`
- 如果 `listA` 和 `listB` 有交点，`intersectVal == listA[skipA] == listB[skipB]`



```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        pointerA, pointerB = headA, headB
        
        while pointerA is not pointerB:
            # 如果到达链表末尾，则转向另一个链表的头部
            pointerA = headB if pointerA is None else pointerA.next
            pointerB = headA if pointerB is None else pointerB.next
        
        # 两种情况下会退出循环：
        # 1. 在交点相遇
        # 2. 两个链表都遍历完没有交点（此时 pointerA 和 pointerB 都为 None）
        return pointerA
```

> 这个算法能够找到两个链表相交的节点，其背后的核心思想是通过调整两个指针遍历链表的方式，使得它们在第二次遍历时同时到达交点或链表末尾。下面是该算法为什么有效的原因：
>
> **关键点**
>
> 1. **两次遍历**：每个指针都会遍历自己的链表一次，并且如果到达链表末尾（即 `None`），则跳转到另一个链表的头部继续遍历。这意味着每个指针最终会遍历两个链表。
>
> 2. **等距原则**：假设链表 A 的长度为 $L_A$，链表 B 的长度为 $L_B$，而从各自头结点到交点的距离分别为 $D_A$ 和 $D_B$，交点之后的长度为 C。那么有：
>    - 如果两个链表相交，则 $D_A + C = L_A$ 和 $D_B + C = L_B$。
>    - 当指针A遍历完链表A后跳转到链表B的头部，它实际上走了 $D_A + C + D_B$ 的距离；同样地，当指针B遍历完链表B后跳转到链表A的头部，它实际上也走了 $D_B + C + D_A$ 的距离。
>
> 3. **相遇条件**：由于两个指针走过的总距离相同 ($D_A + C + D_B = D_B + C + D_A$)，所以当它们第二次遍历时，要么会在交点处相遇（因为此时它们都走了相同的距离并且指向同一个节点），要么同时到达链表的末尾（即 `None`），这表明没有交点。
>
> 退出循环的情况
>
> - **交点相遇**：如果两个链表相交，两个指针会在交点处相遇，此时 `pointerA == pointerB`，因此会退出循环并返回该节点。
> - **无交点情况**：如果两个链表不相交，那么两个指针最终都会遍历完两个链表，并且都变为 `None`，这时也会退出循环，返回 `None` 表示没有交点。
>
> **算法的优势**
>
> - **时间复杂度**：该算法的时间复杂度为 O(n + m)，其中 n 和 m 分别是两个链表的长度。这是因为每个指针最多遍历两个链表各一次。
> - **空间复杂度**：只需要常数级别的额外空间来存储两个指针，因此空间复杂度为 O(1)。
>
> 综上所述，这个算法巧妙地利用了两个指针遍历两个链表的方式，确保了即使两个链表长度不同，也能准确找到它们的交点或者确认不存在交点。这种方法不仅高效而且简洁，是解决此类问题的一种经典方法。





## 169.多数元素

https://leetcode.cn/problems/majority-element/

给定一个大小为 `n` 的数组 `nums` ，返回其中的多数元素。多数元素是指在数组中出现次数 **大于** `⌊ n/2 ⌋` 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

**示例 1：**

```
输入：nums = [3,2,3]
输出：3
```

**示例 2：**

```
输入：nums = [2,2,1,1,1,2,2]
输出：2
```

 

**提示：**

- `n == nums.length`
- `1 <= n <= 5 * 104`
- `-109 <= nums[i] <= 109`

 

**进阶：**尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。



```python
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        nums.sort()
        cur = nums[0]
        count = 1
        ans = []
        for i in range(1, len(nums)):
            if nums[i] == cur:
                count += 1
                if i == n - 1 and count > n // 2:
                    ans.append(cur)
            else:
                if count > n // 2:
                    ans.append(cur)
                cur = nums[i]
                count = 1

        return ans[0]

```



## 206.反转链表

linked-list, https://leetcode.cn/problems/reverse-linked-list/

给你单链表的头节点 `head` ，请你反转链表，并返回反转后的链表。

 

**示例 1：**

![img](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)

```
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
```

**示例 2：**

![img](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)

```
输入：head = [1,2]
输出：[2,1]
```

**示例 3：**

```
输入：head = []
输出：[]
```

 

**提示：**

- 链表中节点的数目范围是 `[0, 5000]`
- `-5000 <= Node.val <= 5000`



```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        current = head
        while current:
            next_node = current.next
            current.next = pre
            pre = current
            current = next_node

        return pre
        
```



## 234.回文链表

linked-list, https://leetcode.cn/problems/palindrome-linked-list/

给你一个单链表的头节点 `head` ，请你判断该链表是否为

回文链表（**回文** 序列是向前和向后读都相同的序列。如果是，返回 `true` ；否则，返回 `false` 。



 

**示例 1：**

![img](https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg)

```
输入：head = [1,2,2,1]
输出：true
```

**示例 2：**

![img](https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg)

```
输入：head = [1,2]
输出：false
```

 

**提示：**

- 链表中节点数目在范围`[1, 105]` 内
- `0 <= Node.val <= 9`

 

**进阶：**你能否用 `O(n)` 时间复杂度和 `O(1)` 空间复杂度解决此题？



快慢指针查找链表的中间节点

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # 1. 使用快慢指针找到链表的中点
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. 反转链表的后半部分
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # 3. 对比前半部分和反转后的后半部分
        left, right = head, prev
        while right:  # right 是反转后的链表的头
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True

```



```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Count the length of the linked list
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        odd_f = n % 2 == 1
        n_half = n // 2
        pre = None
        cur = head
        cnt = 0
        while cnt < n_half:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
            cnt += 1
        
        if odd_f:
            cur = cur.next  # Skip the middle node if the length is odd

        # Compare the reversed first half and the second half.
        while cur and pre:
            if cur.val != pre.val:
                return False
            cur = cur.next
            pre = pre.next
        
        return True

if __name__ == "__main__":
    sol = Solution()
    # Test case for non-palindrome linked list
    head = ListNode(1, ListNode(2))
    print(sol.isPalindrome(head))  # Expected output: False

    # Test case for palindrome linked list
    # Uncomment the following line to test a palindrome linked list
    # head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    # print(sol.isPalindrome(head))  # Expected output: True
```



## 2239.找到最接近0的数字

https://leetcode.cn/problems/find-closest-number-to-zero/

给你一个长度为 `n` 的整数数组 `nums` ，请你返回 `nums` 中最 **接近** `0` 的数字。如果有多个答案，请你返回它们中的 **最大值** 。

 

**示例 1：**

```
输入：nums = [-4,-2,1,4,8]
输出：1
解释：
-4 到 0 的距离为 |-4| = 4 。
-2 到 0 的距离为 |-2| = 2 。
1 到 0 的距离为 |1| = 1 。
4 到 0 的距离为 |4| = 4 。
8 到 0 的距离为 |8| = 8 。
所以，数组中距离 0 最近的数字为 1 。
```

**示例 2：**

```
输入：nums = [2,-1,1]
输出：1
解释：1 和 -1 都是距离 0 最近的数字，所以返回较大值 1 。
```

 

**提示：**

- `1 <= n <= 1000`
- `-105 <= nums[i] <= 105`



```python
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        minv = abs(nums[0] - 0)
        raw = nums[0]
        for i in nums[1:]:
            if abs(i - 0) < minv:
                minv = abs(i-0)
                raw = i
        return raw
```



## 2264.字符串中最大的3位相同数字

https://leetcode.cn/problems/largest-3-same-digit-number-in-string/

给你一个字符串 `num` ，表示一个大整数。如果一个整数满足下述所有条件，则认为该整数是一个 **优质整数** ：

- 该整数是 `num` 的一个长度为 `3` 的 **子字符串** 。
- 该整数由唯一一个数字重复 `3` 次组成。

以字符串形式返回 **最大的优质整数** 。如果不存在满足要求的整数，则返回一个空字符串 `""` 。

**注意：**

- **子字符串** 是字符串中的一个连续字符序列。
- `num` 或优质整数中可能存在 **前导零** 。

 

**示例 1：**

```
输入：num = "6777133339"
输出："777"
解释：num 中存在两个优质整数："777" 和 "333" 。
"777" 是最大的那个，所以返回 "777" 。
```

**示例 2：**

```
输入：num = "2300019"
输出："000"
解释："000" 是唯一一个优质整数。
```

**示例 3：**

```
输入：num = "42352338"
输出：""
解释：不存在长度为 3 且仅由一个唯一数字组成的整数。因此，不存在优质整数。
```

 

**提示：**

- `3 <= num.length <= 1000`
- `num` 仅由数字（`0` - `9`）组成



```python
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good_integer = ""
        for i in range(len(num) - 2):
            substring = num[i:i+3]
            if substring[0] == substring[1] == substring[2]:
                if substring > max_good_integer:
                    max_good_integer = substring
        return max_good_integer
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



## 3019.按键变更的次数

https://leetcode.cn/problems/number-of-changing-keys/

给你一个下标从 **0** 开始的字符串 `s` ，该字符串由用户输入。按键变更的定义是：使用与上次使用的按键不同的键。例如 `s = "ab"` 表示按键变更一次，而 `s = "bBBb"` 不存在按键变更。

返回用户输入过程中按键变更的次数。

**注意：**`shift` 或 `caps lock` 等修饰键不计入按键变更，也就是说，如果用户先输入字母 `'a'` 然后输入字母 `'A'` ，不算作按键变更。

 

**示例 1：**

```
输入：s = "aAbBcC"
输出：2
解释： 
从 s[0] = 'a' 到 s[1] = 'A'，不存在按键变更，因为不计入 caps lock 或 shift 。
从 s[1] = 'A' 到 s[2] = 'b'，按键变更。
从 s[2] = 'b' 到 s[3] = 'B'，不存在按键变更，因为不计入 caps lock 或 shift 。
从 s[3] = 'B' 到 s[4] = 'c'，按键变更。
从 s[4] = 'c' 到 s[5] = 'C'，不存在按键变更，因为不计入 caps lock 或 shift 。
```

**示例 2：**

```
输入：s = "AaAaAaaA"
输出：0
解释： 不存在按键变更，因为这个过程中只按下字母 'a' 和 'A' ，不需要进行按键变更。
```

 

**提示：**

- `1 <= s.length <= 100`
- `s` 仅由英文大写字母和小写字母组成。



```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        pre = s[0].lower()
        cnt = 0
        for c in s[1:]:
            if c.lower() != pre:
                cnt += 1
                pre = c.lower()
        return cnt

```



## 3065.超过阈值的最少操作数I

https://leetcode.cn/problems/minimum-operations-to-exceed-threshold-value-i/

给你一个下标从 **0** 开始的整数数组 `nums` 和一个整数 `k` 。

一次操作中，你可以删除 `nums` 中的最小元素。

你需要使数组中的所有元素都大于或等于 `k` ，请你返回需要的 **最少** 操作次数。

 

**示例 1：**

```
输入：nums = [2,11,10,1,3], k = 10
输出：3
解释：第一次操作后，nums 变为 [2, 11, 10, 3] 。
第二次操作后，nums 变为 [11, 10, 3] 。
第三次操作后，nums 变为 [11, 10] 。
此时，数组中的所有元素都大于等于 10 ，所以我们停止操作。
使数组中所有元素都大于等于 10 需要的最少操作次数为 3 。
```

**示例 2：**

```
输入：nums = [1,1,2,4,9], k = 1
输出：0
解释：数组中的所有元素都大于等于 1 ，所以不需要对 nums 做任何操作。
```

**示例 3：**

```
输入：nums = [1,1,2,4,9], k = 9
输出：4
解释：nums 中只有一个元素大于等于 9 ，所以需要执行 4 次操作。
```

 

**提示：**

- `1 <= nums.length <= 50`
- `1 <= nums[i] <= 109`
- `1 <= k <= 109`
- 输入保证至少有一个满足 `nums[i] >= k` 的下标 `i` 存在。



```python
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in nums:
            if i < k:
                cnt += 1
        return cnt
```





## 3079.求出加密整数的和

https://leetcode.cn/problems/find-the-sum-of-encrypted-integers/

给你一个整数数组 `nums` ，数组中的元素都是 **正** 整数。定义一个加密函数 `encrypt` ，`encrypt(x)` 将一个整数 `x` 中 **每一个** 数位都用 `x` 中的 **最大** 数位替换。比方说 `encrypt(523) = 555` 且 `encrypt(213) = 333` 。

请你返回数组中所有元素加密后的 **和** 。

**示例 1：**

**输入：**nums = [1,2,3]

**输出：**6

**解释：**加密后的元素位 `[1,2,3]` 。加密元素的和为 `1 + 2 + 3 == 6` 。

**示例 2：**

**输入：**nums = [10,21,31]

**输出：**66

**解释：**加密后的元素为 `[11,22,33]` 。加密元素的和为 `11 + 22 + 33 == 66` 。

 

**提示：**

- `1 <= nums.length <= 50`
- `1 <= nums[i] <= 1000`



```python
from typing import List
class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        sumv = 0
        for i in nums:
            a = list(str(i))
            a_len = len(str(i))
            max_i = max([int(i) for i in a])
            max_i = str(max_i)* a_len
            sumv += int(max_i)

        return sumv

if __name__ == "__main__":
    sol = Solution()
    print(sol.sumOfEncryptedInt([123, 456, 789])) 
```



## 3095.或值至少K的最短子数组I

滑动窗口，https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-i/

给你一个 **非负** 整数数组 `nums` 和一个整数 `k` 。

如果一个数组中所有元素的按位或运算 `OR` 的值 **至少** 为 `k` ，那么我们称这个数组是 **特别的** 。

请你返回 `nums` 中 **最短特别非空** 

子数组

的长度，如果特别子数组不存在，那么返回 `-1` 。

**示例 1：**

**输入：**nums = [1,2,3], k = 2

**输出：**1

**解释：**

子数组 `[3]` 的按位 `OR` 值为 `3` ，所以我们返回 `1` 。

注意，`[2]` 也是一个特别子数组。

**示例 2：**

**输入：**nums = [2,1,8], k = 10

**输出：**3

**解释：**

子数组 `[2,1,8]` 的按位 `OR` 值为 `11` ，所以我们返回 `3` 。

**示例 3：**

**输入：**nums = [1,2], k = 0

**输出：**1

**解释：**

子数组 `[1]` 的按位 `OR` 值为 `1` ，所以我们返回 `1` 。

 

**提示：**

- `1 <= nums.length <= 50`
- `0 <= nums[i] <= 50`
- `0 <= k < 64`



```python
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        or_value = 0
        min_length = float('inf')

        for right in range(n):
            or_value |= nums[right]

            # 收缩窗口，确保按位或值 >= k
            while or_value >= k and left <= right:
                min_length = min(min_length, right - left + 1)
                left += 1
                # 重新计算窗口的按位或值
                or_value = 0
                for i in range(left, right + 1):
                    or_value |= nums[i]

        return min_length if min_length != float('inf') else -1
        
```



作者：力扣官方题解
链接：https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-i/solutions/3040100/huo-zhi-zhi-shao-k-de-zui-duan-zi-shu-zu-vl4c/

由于给定数组 nums 中的元素大小不超过 10^9，因此最多需要考虑二进制表示的前 30 位。我们需要维护一个长度为 30 的数组 bits，其中 bits[i] 表示滑动窗口中满足二进制表示的从低到高第 i 位的值为 1 的元素个数。

```python
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        bits = [0] * 30
        res = inf
        def calc(bits):
            return sum(1 << i for i in range(30) if bits[i] > 0)

        left = 0
        for right in range(n):
            for i in range(30):
                bits[i] += (nums[right] >> i) & 1
            while left <= right and calc(bits) >= k:
                res = min(res, right - left + 1)
                for i in range(30):
                    bits[i] -= (nums[left] >> i) & 1
                left += 1

        return -1 if res == inf else res

```

复杂度分析

时间复杂度：O(nlogU)，其中 n 表示给定数组 nums 的长度，U 表示数组中的最大的元素。由于使用滑动窗口遍历需要的时间为 O(n)，每次更新窗口元素时需要实时计算当前子数组按位或的值需要的时间为 O(logU)，此时需要的总时间即为 O(nlogU)。

空间复杂度：O(logU)。计算时需要存储当前子数组中每一个二进制位中的统计情况，最多有 logU 位需要记录，因此需要的空间为 logU。





## 3270.求出数字答案

https://leetcode.cn/problems/find-the-key-of-the-numbers/description/

给你三个 **正** 整数 `num1` ，`num2` 和 `num3` 。

数字 `num1` ，`num2` 和 `num3` 的数字答案 `key` 是一个四位数，定义如下：

- 一开始，如果有数字 **少于** 四位数，给它补 **前导 0** 。
- 答案 `key` 的第 `i` 个数位（`1 <= i <= 4`）为 `num1` ，`num2` 和 `num3` 第 `i` 个数位中的 **最小** 值。

请你返回三个数字 **没有** 前导 0 的数字答案。

 

**示例 1：**

**输入：**num1 = 1, num2 = 10, num3 = 1000

**输出：**0

**解释：**

补前导 0 后，`num1` 变为 `"0001"` ，`num2` 变为 `"0010"` ，`num3` 保持不变，为 `"1000"` 。

- 数字答案 `key` 的第 `1` 个数位为 `min(0, 0, 1)` 。
- 数字答案 `key` 的第 `2` 个数位为 `min(0, 0, 0)` 。
- 数字答案 `key` 的第 `3` 个数位为 `min(0, 1, 0)` 。
- 数字答案 `key` 的第 `4` 个数位为 `min(1, 0, 0)` 。

所以数字答案为 `"0000"` ，也就是 0 。

**示例 2：**

**输入：** num1 = 987, num2 = 879, num3 = 798

**输出：**777

**示例 3：**

**输入：**num1 = 1, num2 = 2, num3 = 3

**输出：**1

 

**提示：**

- `1 <= num1, num2, num3 <= 9999`



```python
class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        n1_list = (4-len(str(num1)))*['0'] + list(str(num1))
        n2_list = (4-len(str(num2)))*['0'] + list(str(num2))
        n3_list = (4-len(str(num3)))*['0'] + list(str(num3))
        res = []
        flag = False
        for i in range(4):
            cur = min(n1_list[i], n2_list[i], n3_list[i])
            if not flag and cur == '0':
                continue
            if not flag and cur:
                flag = True

            res.append(cur)
                
        if res:
            return int(''.join(res))
        else:
            return 0
```



不用显性给三个数添加前导零，从三个数的最低位开始构造，每次取`min(num1%10,num2%10,num3%10)×base`累加在答案上，然后更新num1，num2，num3供后续使用。这样次低位又变成了最低位，直到num1=num2=num3=0成立。

```python
class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        key, p = 0, 1
        while num1 and num2 and num3:
            key += min(num1 % 10, num2 % 10, num3 % 10) * p
            p *= 10
            num1, num2, num3 = num1 // 10, num2 // 10, num3 // 10
        return key

```



## 3280.将日期转换为二进制表示

https://leetcode.cn/problems/convert-date-to-binary/

给你一个字符串 `date`，它的格式为 `yyyy-mm-dd`，表示一个公历日期。

`date` 可以重写为二进制表示，只需要将年、月、日分别转换为对应的二进制表示（不带前导零）并遵循 `year-month-day` 的格式。

返回 `date` 的 **二进制** 表示。

 

**示例 1：**

**输入：** date = "2080-02-29"

**输出：** "100000100000-10-11101"

**解释：**

100000100000, 10 和 11101 分别是 2080, 02 和 29 的二进制表示。

**示例 2：**

**输入：** date = "1900-01-01"

**输出：** "11101101100-1-1"

**解释：**

11101101100, 1 和 1 分别是 1900, 1 和 1 的二进制表示。

 

**提示：**

- `date.length == 10`
- `date[4] == date[7] == '-'`，其余的 `date[i]` 都是数字。
- 输入保证 `date` 代表一个有效的公历日期，日期范围从 1900 年 1 月 1 日到 2100 年 12 月 31 日（包括这两天）。



```python
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        y,m,d = map(int, date.split('-'))
        ans = []
        for i in [y,m,d]:
            ans.append(bin(i)[2:])

        return '-'.join(ans) 
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



## 5.最长回文子串

dp, two pointers, string, https://leetcode.cn/problems/longest-palindromic-substring/

给你一个字符串 `s`，找到 `s` 中最长的 

回文子串。

**示例 1：**

```
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
```

**示例 2：**

```
输入：s = "cbbd"
输出："bb"
```

 

**提示：**

- `1 <= s.length <= 1000`
- `s` 仅由数字和英文字母组成



**Plan**

1. Initialize a 2D list `dp` where `dp[i][j]` will be `True` if the substring `s[i:j+1]` is a palindrome.
2. Iterate through the string in reverse order to fill the `dp` table.
3. For each character, check if the substring is a palindrome by comparing the characters at the ends and using the previously computed values in `dp`.
4. Keep track of the start and end indices of the longest palindromic substring found.
5. Return the substring defined by the start and end indices.

对于一个子串而言，如果它是回文串，并且长度大于 2，那么将它首尾的两个字母去除之后，它仍然是个回文串。

状态：`dp[i][j]`表示子串`s[i:j+1]`是否为回文子串

状态转移方程：`dp[i][j] = dp[i+1][j-1] ∧ (S[i] == s[j])`

动态规划中的边界条件，即子串的长度为 1 或 2。对于长度为 1 的子串，它显然是个回文串；对于长度为 2 的子串，只要它的两个字母相同，它就是一个回文串。

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        # Initialize the dp table
        dp = [[False] * n for _ in range(n)]
        start, max_length = 0, 1

        # Every single character is a palindrome
        for i in range(n):
            dp[i][i] = True

        # Check for palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2

        # Check for palindromes of length greater than 2
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_length = length

        return s[start:start + max_length]

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("babad"))  # Output: "bab" or "aba"
    print(sol.longestPalindrome("cbbd"))   # Output: "bb"
```



**Plan**

1. Initialize variables to store the start and end indices of the longest palindromic substring.
2. Iterate through each character in the string, treating each character and each pair of consecutive characters as potential centers of palindromes.
3. For each center, expand outwards while the characters on both sides are equal.
4. Update the start and end indices if a longer palindrome is found.
5. Return the substring defined by the start and end indices.

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, end = 0, 0
        
        for i in range(len(s)):
            odd_len = self.expandAroundCenter(s, i, i)
            even_len = self.expandAroundCenter(s, i, i + 1)
            max_len = max(odd_len, even_len)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end + 1]
    
    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("babad"))  # Output: "bab" or "aba"
    print(sol.longestPalindrome("cbbd"))   # Output: "bb"
```

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20241125155859557.png" alt="image-20241125155859557" style="zoom:50%;" />

这个双指针是从中间往两边跑。



Manacher算法

https://leetcode.cn/problems/longest-palindromic-substring/solutions/255195/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/

```python
class Solution:
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2

    def longestPalindrome(self, s: str) -> str:
        end, start = -1, 0
        s = '#' + '#'.join(list(s)) + '#'
        arm_len = []
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = self.expand(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i
                right = i + cur_arm_len
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len
        return s[start+1:end+1:2]

```



> 这段代码是用于解决“最长回文子串”问题的一个Python实现。它使用了Manacher算法的变种，通过在每个字符间插入特殊字符（这里是`#`）来处理奇数和偶数长度的回文字符串。让我们逐段解析这个解决方案：
>
> 扩展函数 `expand`
>
> - 此函数尝试从给定的中心点向两边扩展，以找到以该中心点为中心的最大回文半径。
> - 如果左右指针指向的字符相等且都在字符串范围内，则继续向外扩展。
> - 返回值为最大回文半径，即`(right - left - 2) // 2`。
>
> 主函数 `longestPalindrome`
>
> - 首先，将原始字符串`s`转换成一个新字符串，其中每个字符之间都插入了一个`#`，这样可以确保所有可能的回文子串都是奇数长度，便于处理。
> - `end` 和 `start` 变量用于记录最长回文子串的边界。
> - `arm_len` 列表存储每个位置的回文臂长。
> - `right` 和 `j` 分别表示当前已知最右端的回文子串的右边界及其对应的中心点。
> - 在遍历新字符串时，如果当前索引`i`位于`right`内，那么利用对称性，计算出`i`关于`j`的对称点`i_sym`，并确定最小臂长。
> - 使用`expand`函数计算当前位置的实际臂长，并更新`arm_len`列表。
> - 如果当前臂长加上`i`超过了`right`，则更新`right`和`j`。
> - 如果当前找到的回文子串比之前记录的更长，则更新`start`和`end`。
> - 最后，返回原始字符串中对应最长回文子串的部分，注意去掉添加的`#`符号。
>
> 整个算法的核心思想是利用已经计算过的回文信息来减少重复计算，从而提高效率。这种方法的时间复杂度接近O(n)，空间复杂度为O(n)。



min_arm_len = min(arm_len[i_sym], right - i)	 如何理解？

> `min_arm_len = min(arm_len[i_sym], right - i)` 这一行代码是用来确定从当前位置 `i` 开始进行中心扩展时，可以跳过的最小臂长。这里有两个关键点需要理解：
>
> 1. **`arm_len[i_sym]`**:
>    - `i_sym` 是位置 `i` 关于当前已知最右边回文子串中心 `j` 的对称点，计算方式为 `2 * j - i`。
>    - `arm_len[i_sym]` 表示的是对称点 `i_sym` 处的回文臂长。如果 `i_sym` 位置的回文臂长足够大，那么根据对称性，我们可以在 `i` 位置直接获得至少相同的臂长，因为这两个位置关于 `j` 对称。
>
> 2. **`right - i`**:
>    - `right` 是当前已知最右端回文子串的边界。
>    - `right - i` 表示从位置 `i` 到当前已知最右端的距离。由于我们已经知道在 `right` 之前的字符都是回文的一部分，因此在 `i` 位置进行扩展时，我们至少可以达到 `right` 位置，而不需要重新验证这些字符。
>
> 综合以上两点，`min_arm_len` 取两者中的较小值，确保了以下几点：
>
> - 如果 `i_sym` 位置的臂长小于或等于 `right - i`，我们可以直接使用 `i_sym` 位置的臂长，因为它不会超出已知的回文区域。
> - 如果 `i_sym` 位置的臂长大于 `right - i`，则我们只能保证到 `right` 位置是回文，所以取 `right - i` 作为最小臂长。
>
> 这样做的目的是为了减少不必要的重复计算，通过利用之前计算的结果（即 `arm_len` 中的信息）来加速找到当前位置的最长回文臂长的过程。这实际上是Manacher算法中的一种优化手段，它允许我们在某些情况下快速跳过已经确认的部分，从而提高算法的整体效率。





思路：马拉车算法（Manacher）

首先一个比较基础的想法是研究以某一个位置为中心的回文串，但考虑到可能存在`aba`和`aa`这样不同奇偶性的回文串，将其补齐成类似`#a#b#a#`的形式，这样所有的回文串都是奇数。
然后，考虑某一个位置为中心的回文串，朴素的算法就是一步一步地扩大半径，直到不再回文，即这一部分代码

```python
while 0 <= i - k and i + k < n and ns[i - k] == ns[i + k]:
    k += 1
```

而马拉车算法在这一部分朴素的算法之外，进一步考虑到在我找到这个位置最长的回文串的时候，我在后面的寻找过程中可以利用这个信息。

我们维护一个最右边的回文串的边界`l, r`，如果`i`已经超出了这一部分，那么就只能直接调用后面的朴素算法；否则，我们可以利用之前的信息，考察在目前的`l, r`下对称的那个点`l+r-i`的最长回文串，将其设为我们朴素算法的起始半径来进行循环。

特别地，如果对称过来的半径太长，超出了`r`的部分事实上我们目前还没进行研究，所以最大值只能到`r-i-1`。

每次求解之后更新最右的`r`以及对应的`l`。

朴素算法，时间复杂度O(n²); Manacher，时间复杂度O(n)。（while循环每进一次r至少变大1）

```python
# 曹以楷 24物理学院
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ns = f"#{'#'.join(s)}#"
        n = len(ns)
        # Manacher start
        d = [0]*n
        l, r = 0, -1
        for i in range(n):
            k = 1 if i > r else min(d[l + r - i], r - i + 1)
            while 0 <= i - k and i + k < n and ns[i - k] == ns[i + k]:
                k += 1
            d[i] = k
            k -= 1
            if i + k > r:
                l = i - k
                r = i + k
        # Manacher end
        cnt = max(d)
        idx = d.index(cnt)

        return ns[idx-cnt+1:idx+cnt].replace("#", "")

```



思路：

- 最开始我没看到题目要求子串必须连续！我想了很久，想到了可能要把原字符串逆序但不知道逆序之后干什么，然后一个同学告诉我直接求最长公共子序列就好，感觉瞬间明白了
- 然后发现子串要求连续，在原来程序的基础上，取出所有的公共子序列，再找其中既是回文的又是最长的那个，也算是过了

```python
# 颜鼎堃 24工学院
class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "".join(reversed(s))
        n = len(s)
        strings = [["" for i in range(n + 2)] for j in range(n + 2)]
        for i in range(n):
            for j in range(n):
                if s[i] == t[j]:
                    strings[i + 1][j + 1] = strings[i][j] + s[i]
        pos_pal = set()
        max_par = s[0]
        for i in map(set, strings):
            pos_pal |= i
        for i in pos_pal:
            if i and i == i[::-1]:
                max_par = max(max_par, i, key=len)
        return max_par


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome(input()))
```





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



## 17.电话号码的字母组合

backtracking, https://leetcode.cn/problems/letter-combinations-of-a-phone-number/

给定一个仅包含数字 `2-9` 的字符串，返回所有它能表示的字母组合。答案可以按 **任意顺序** 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/11/09/200px-telephone-keypad2svg.png)

 

**示例 1：**

```
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

**示例 2：**

```
输入：digits = ""
输出：[]
```

**示例 3：**

```
输入：digits = "2"
输出：["a","b","c"]
```

 

**提示：**

- `0 <= digits.length <= 4`
- `digits[i]` 是范围 `['2', '9']` 的一个数字。



```python
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_char = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno',
        '7':'pqrs','8':'tuv','9':'wxyz'}
        ans = []
        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                ans.append(combination)
            else:
                for letter in num_to_char[next_digits[0]]:
                    backtrack(combination+letter, next_digits[1:])

        if digits:
            backtrack("", digits) # start with an empty string
        return ans

if __name__ == "__main__":
    digits = "23"
    print(Solution().letterCombinations(digits))
```



上面代码中使用了隐式回溯，因为回溯函数 `backtrack` 的参数中直接传递了新的状态。

显示回溯代码如下：

```python
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_char = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
                       '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ans = []

        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                ans.append(combination)
            else:
                # 显式回溯：使用循环遍历数字对应的字母
                for letter in num_to_char[next_digits[0]]:
                    # 将当前字母加入组合
                    combination += letter
                    # 递归回溯，进入下一个数字
                    backtrack(combination, next_digits[1:])
                    # 显式回溯：移除上一个字母，恢复到原来的状态
                    combination = combination[:-1]

        if digits:
            backtrack("", digits)  # start with an empty string
        return ans

if __name__ == "__main__":
    digits = "23"
    print(Solution().letterCombinations(digits))

```



## 19.删除链表的倒数第N个结点

快慢指针，https://leetcode.cn/problems/remove-nth-node-from-end-of-list/

给你一个链表，删除链表的倒数第 `n` 个结点，并且返回链表的头结点。

 

**示例 1：**

![img](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

```
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
```

**示例 2：**

```
输入：head = [1], n = 1
输出：[]
```

**示例 3：**

```
输入：head = [1,2], n = 1
输出：[1]
```

 

**提示：**

- 链表中结点的数目为 `sz`
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`



```python
from typing import Optional
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 创建哑结点（dummy）以处理头结点可能被删除的情况
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy

        # 快指针先前进 n+1 步
        for _ in range(n + 1):
            fast = fast.next

        # 快慢指针同时移动直到快指针到达链表末尾
        while fast:
            fast = fast.next
            slow = slow.next

        # 此时慢指针的下一个结点是要删除的结点
        slow.next = slow.next.next

        # 返回头结点
        return dummy.next

# 测试用例
def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    sol = Solution()
    print(print_list(sol.removeNthFromEnd(head, 2)))  # 输出：[1, 2, 3, 5]

    head = ListNode(1)
    print(print_list(sol.removeNthFromEnd(head, 1)))  # 输出：[]

    head = ListNode(1, ListNode(2))
    print(print_list(sol.removeNthFromEnd(head, 1)))  # 输出：[1]
```



## 22.括号生成

backtracking, https://leetcode.cn/problems/generate-parentheses/

数字 `n` 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 **有效的** 括号组合。

 

**示例 1：**

```
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
```

**示例 2：**

```
输入：n = 1
输出：["()"]
```

 

**提示：**

- `1 <= n <= 8`



```python
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)
        backtrack()
        return ans


if __name__ == "__main__":
    sol = Solution()
    n = 3
    print(sol.generateParenthesis(n))
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



## 34.在排序数组中查找元素的第一个和最后一个位置

Binary search, https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/

给你一个按照非递减顺序排列的整数数组 `nums`，和一个目标值 `target`。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 `target`，返回 `[-1, -1]`。

你必须设计并实现时间复杂度为 `O(log n)` 的算法解决此问题。

 

**示例 1：**

```
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
```

**示例 2：**

```
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
```

**示例 3：**

```
输入：nums = [], target = 0
输出：[-1,-1]
```

 

**提示：**

- `0 <= nums.length <= 105`
- `-109 <= nums[i] <= 109`
- `nums` 是一个非递减数组
- `-109 <= target <= 109`



```python
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = 0;
        hi = len(nums)
        flag = False
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid
            else:
                flag = True
                break
        if not flag:
            return [-1, -1]
        else:
            lo = hi = mid
            while lo >= 0 and nums[lo] == target:
                lo -= 1
            while hi < len(nums) and nums[hi] == target:
                hi += 1
            return [lo + 1, hi - 1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([5,7,7,8,8,10], 8))
    print(sol.searchRange([2,2], 2))
```





## 39.组合总和

backtracking, https://leetcode.cn/problems/combination-sum/

给你一个 **无重复元素** 的整数数组 `candidates` 和一个目标整数 `target` ，找出 `candidates` 中可以使数字和为目标数 `target` 的 所有 **不同组合** ，并以列表形式返回。你可以按 **任意顺序** 返回这些组合。

`candidates` 中的 **同一个** 数字可以 **无限制重复被选取** 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

对于给定的输入，保证和为 `target` 的不同组合数少于 `150` 个。

 

**示例 1：**

```
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。
```

**示例 2：**

```
输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
```

**示例 3：**

```
输入: candidates = [2], target = 1
输出: []
```

 

**提示：**

- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- `candidates` 的所有元素 **互不相同**
- `1 <= target <= 40`



```python
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(start, target, path):
            if target == 0:
                ans.append(path)
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                backtrack(i, target-candidates[i], path+[candidates[i]])
        backtrack(0, target, []) # start with an empty list
        return ans

if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    print(Solution().combinationSum(candidates, target))
```



## 46.全排列

backtracking, https://leetcode.cn/problems/permutations/

给定一个不含重复数字的数组 `nums` ，返回其 *所有可能的全排列* 。你可以 **按任意顺序** 返回答案。

 

**示例 1：**

```
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**示例 2：**

```
输入：nums = [0,1]
输出：[[0,1],[1,0]]
```

**示例 3：**

```
输入：nums = [1]
输出：[[1]]
```

 

**提示：**

- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- `nums` 中的所有整数 **互不相同**



```python
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        visited = [False] * n  # 用于标记 nums 中的元素是否被访问过

        def dfs(a):
            if len(a) == n:
                ans.append(a[:])  # 收集当前排列
                return
            for i in range(n):
                if visited[i]:  # 跳过已访问的元素
                    continue
                visited[i] = True
                a.append(nums[i])
                dfs(a)
                a.pop()  # 回溯
                visited[i] = False

        dfs([])
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1, 2, 3]))

```



隐式回溯写法

```python
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def dfs(a, remaining):
            if len(a) == n:
                ans.append(a[:])  # 收集当前排列
                return
            for i in range(len(remaining)):
                # 选择 remaining[i] 并递归
                dfs(a + [remaining[i]], remaining[:i] + remaining[i+1:])

        dfs([], nums)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1, 2, 3]))

```





```python
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        
        def dfs(path, remaining):
            if len(path) == n:
                ans.append(path)
                return
            for i in range(len(remaining)):
                # 选择当前元素
                new_path = path + [remaining[i]]
                new_remaining = remaining[:i] + remaining[i+1:]
                # 递归调用
                dfs(new_path, new_remaining)
        
        dfs([], nums)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1, 2, 3]))
```

撤销选择：
由于我们在<mark>每次递归调用时创建了新的路径和剩余元素，所以不需要显式地撤销选择</mark>。递归返回后，自动恢复到之前的状态。



## 48.旋转图像

https://leetcode.cn/problems/rotate-image/

给定一个 *n* × *n* 的二维矩阵 `matrix` 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在**[ 原地](https://baike.baidu.com/item/原地算法)** 旋转图像，这意味着你需要直接修改输入的二维矩阵。**请不要** 使用另一个矩阵来旋转图像。

 

**示例 1：**

![img](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)

```
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]
```

**示例 2：**

![img](https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg)

```
输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

 

**提示：**

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`



```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):  # 先转置矩阵
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):  # 再水平翻转矩阵
            matrix[i].reverse()
```



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



## 53.最大子数组和

greedy, dp, https://leetcode.cn/problems/maximum-subarray/

给你一个整数数组 `nums` ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。



**子数组** 

是数组中的一个连续部分。



 

**示例 1：**

```
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
```

**示例 2：**

```
输入：nums = [1]
输出：1
```

**示例 3：**

```
输入：nums = [5,4,-1,7,8]
输出：23
```

 

**提示：**

- `1 <= nums.length <= 105`
- `-104 <= nums[i] <= 104`

 

**进阶：**如果你已经实现复杂度为 `O(n)` 的解法，尝试使用更为精妙的 **分治法** 求解。



```python
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_v = nums[0]
        pre_sum = nums[0]
        for i in range(1, n):
            if pre_sum <= 0:
                pre_sum = nums[i]
            else:
                pre_sum += nums[i]
            max_v = max(max_v, pre_sum)

        return max_v

if __name__ == "__main__":
    sol = Solution()
    #print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
    #print(sol.maxSubArray([1]))  # 1
    print(sol.maxSubArray([5,4,-1,7,8]))  # 23
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
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        m, n = len(matrix), len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        order = []

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        x, y = 0, 0
        direction_idx = 0  # 初始方向为向右
        for _ in range(m * n):
            order.append(matrix[x][y])
            visited[x][y] = True

            dx, dy = directions[direction_idx]
            nx, ny = x + dx, y + dy

            # 检查边界条件和访问状态，如果合法，更新到下一个位置
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                x, y = nx, ny
            else:
                direction_idx = (direction_idx + 1) % 4
                dx, dy = directions[direction_idx]
                x, y = x + dx, y + dy

        return order

if __name__ == "__main__":
    sol = Solution()
    print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

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

dp, math, https://leetcode.cn/problems/unique-paths/

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



因为纯dfs超时，考虑使用lru_cache。

> 使用 `lru_cache` 时需要注意一些细节，特别是当涉及到类方法和状态共享时。在上面的代码中，`lru_cache` 缓存的是 `dfs` 函数的结果，但是 `dfs` 函数内部修改了类的状态（即 `self.cnt`），这会导致缓存的行为不符合预期。
>
> 具体来说，`lru_cache` 会缓存 `dfs` 函数的返回值，而不是函数执行过程中的副作用（如修改 `self.cnt`）。因此，当 `dfs` 函数被多次调用时，`self.cnt` 的值可能不会按预期增加。
>
> 为了解决这个问题，可以考虑以下方法：使用 `lru_cache` 但不依赖类状态
>
> 通过将 `cnt` 作为返回值传递，避免了类状态的影响，同时利用 `lru_cache` 提高了性能。

```python
from functools import lru_cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dx = [0, 1]
        dy = [1, 0]

        @lru_cache(maxsize=None)
        def dfs(x, y):
            if x == m - 1 and y == n - 1:
                return 1
            cnt = 0
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    cnt += dfs(nx, ny)
            return cnt

        return dfs(0, 0)

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



math思路

从左上角到右下角的过程中，我们需要移动 m+n−2 次，其中有 m−1 次向下移动，n−1 次向右移动。因此路径的总数，就等于从 m+n−2 次移动中选择 m−1 次向下移动的方案数，即组合数：

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        import math   
        result = math.comb(m+n-2,m-1)
        return result 
```



思路：选择用Iru_cache的方法加上递归就可以轻松完成（耗时10min)

```python
# 胡家豪 24元培学院
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def roads(m,n):
            if m==1 or n==1:
                return 1
            else:
                return roads(m-1,n)+roads(m,n-1)
        return roads(m,n)
```





## 64.最小路径和

https://leetcode.cn/problems/minimum-path-sum/

给定一个包含非负整数的 `*m* x *n*` 网格 `grid` ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

**说明：**每次只能向下或者向右移动一步。

 

**示例 1：**

![img](https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg)

```
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
```

**示例 2：**

```
输入：grid = [[1,2,3],[4,5,6]]
输出：12
```

 

**提示：**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 200`
- `0 <= grid[i][j] <= 200`





```python
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # Initialize the dp array with the same dimensions as grid
        dp = [[0] * n for _ in range(m)]
        
        # Set the starting point
        dp[0][0] = grid[0][0]
        
        # Fill the first row (can only come from the left)
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        
        # Fill the first column (can only come from above)
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        
        # Fill the rest of the dp array
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        # The bottom-right corner contains the minimum path sum
        return dp[m - 1][n - 1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))  # Output: 7
    print(sol.minPathSum([[1,2,3],[4,5,6]]))  # Output: 12
```



## 72.编辑距离

dp, https://leetcode.cn/problems/edit-distance/

给你两个单词 `word1` 和 `word2`， *请返回将 `word1` 转换成 `word2` 所使用的最少操作数* 。

你可以对一个单词进行如下三种操作：

- 插入一个字符
- 删除一个字符
- 替换一个字符

 

**示例 1：**

```
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
```

**示例 2：**

```
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
```

 

**提示：**

- `0 <= word1.length, word2.length <= 500`
- `word1` 和 `word2` 由小写英文字母组成



```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # 创建一个 (m+1) x (n+1) 的 dp 数组，并初始化为0
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 初始化边界条件
        for i in range(m + 1):
            dp[i][0] = i  # 将 word1 变为空串需要 i 次删除操作
        for j in range(n + 1):
            dp[0][j] = j  # 将空串变成 word2 需要 j 次插入操作

        # 填充 dp 数组
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # 如果当前字符相同，则不需要操作
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 如果不同，取三种可能操作中的最小值
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,  # 删除
                        dp[i][j - 1] + 1,  # 插入
                        dp[i - 1][j - 1] + 1  # 替换
                    )

        # 返回 dp[m][n]，即整个字符串的最小编辑距离
        return dp[m][n]

if __name__ == "__main__":
    minDistance = Solution().minDistance
    print(minDistance("horse", "ros"))  # 输出：3
    print(minDistance("intention", "execution"))  # 输出：5
```



## 73.矩阵置零

https://leetcode.cn/problems/set-matrix-zeroes/

给定一个 `*m* x *n*` 的矩阵，如果一个元素为 **0** ，则将其所在行和列的所有元素都设为 **0** 。请使用 **[原地](http://baike.baidu.com/item/原地算法)** 算法**。**

 

**示例 1：**

![img](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)

```
输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]
```

**示例 2：**

![img](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)

```
输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

 

**提示：**

- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-231 <= matrix[i][j] <= 231 - 1`

 

**进阶：**

- 一个直观的解决方案是使用  `O(*m**n*)` 的额外空间，但这并不是一个好的解决方案。
- 一个简单的改进方案是使用 `O(*m* + *n*)` 的额外空间，但这仍然不是最好的解决方案。
- 你能想出一个仅使用常量空间的解决方案吗？



```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix); n = len(matrix[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and matrix[i][j] == 0:
                    for r in range(m):
                        if matrix[r][j] == 0:
                            continue
                        matrix[r][j] = 0
                        visited.add((r,j))
                    for c in range(n):
                        if matrix[i][c] == 0:
                            continue
                        matrix[i][c] = 0
                        visited.add((i,c))
                    visited.add((i,j))
        
        return matrix
        
```



## 74.搜索二维矩阵

binary search, https://leetcode.cn/problems/search-a-2d-matrix/

给你一个满足下述两条属性的 `m x n` 整数矩阵：

- 每行中的整数从左到右按非严格递增顺序排列。
- 每行的第一个整数大于前一行的最后一个整数。

给你一个整数 `target` ，如果 `target` 在矩阵中，返回 `true` ；否则，返回 `false` 。

 

**示例 1：**

![img](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)

```
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
```

**示例 2：**

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/25/mat2.jpg)

```
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
```

 

**提示：**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-104 <= matrix[i][j], target <= 104`



```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = []
        for row in matrix:
            a.extend(row)
        
        if target == a[0]:
            return True

        flag = False
        lo = 0; hi = len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < target:
                lo = mid + 1
            elif a[mid] > target:
                hi = mid
            else:
                flag = True
                break
        
        return flag
```



## 78.子集

backtracking, https://leetcode.cn/problems/subsets/

给你一个整数数组 `nums` ，数组中的元素 **互不相同** 。返回该数组所有可能的

子集

（幂集）。



解集 **不能** 包含重复的子集。你可以按 **任意顺序** 返回解集。

 

**示例 1：**

```
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**示例 2：**

```
输入：nums = [0]
输出：[[],[0]]
```

 

**提示：**

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- `nums` 中的所有元素 **互不相同**



```python
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(start, path):
            ans.append(path)
            for i in range(start, len(nums)):
                backtrack(i+1, path+[nums[i]])
        backtrack(0, []) # start with an empty path
        return ans

if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().subsets(nums))
```



## LCR 107.01 矩阵

dp, https://leetcode.cn/problems/2bCMpM/

给定一个由 `0` 和 `1` 组成的矩阵 `mat` ，请输出一个大小相同的矩阵，其中每一个格子是 `mat` 中对应位置元素到最近的 `0` 的距离。

两个相邻元素间的距离为 `1` 。

 

**示例 1：**

![img](https://pic.leetcode-cn.com/1626667201-NCWmuP-image.png)

```
输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
输出：[[0,0,0],[0,1,0],[0,0,0]]
```

**示例 2：**

![img](https://pic.leetcode-cn.com/1626667205-xFxIeK-image.png)

```
输入：mat = [[0,0,0],[0,1,0],[1,1,1]]
输出：[[0,0,0],[0,1,0],[1,2,1]]
```

 

**提示：**

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 104`
- `1 <= m * n <= 104`
- `mat[i][j] is either 0 or 1.`
- `mat` 中至少有一个 `0 `

 

注意：本题与主站 542 题相同：https://leetcode-cn.com/problems/01-matrix/



是 OJ01088:滑雪 的升级版。因为矩阵每个点的高度有更新，不能只用sort一次，需要使用heapq。

```python
import heapq
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dp = [[float('inf')] * n for _ in range(m)]
        heap = []

        # 初始化，所有的0加入到堆中
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                    heapq.heappush(heap, (0, i, j))  # (distance, x, y)

        # 定义四个方向的移动
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # 使用堆进行更新
        while heap:
            dist, x, y = heapq.heappop(heap)

            # 如果当前的距离大于 dp[x][y]，说明这个位置已经被更新过，不需要再次处理
            if dist > dp[x][y]:
                continue

            # 对当前点的四个方向进行处理
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    # 如果新位置的dp值可以更新（即发现更短的路径）
                    if dp[nx][ny] > dp[x][y] + 1:
                        dp[nx][ny] = dp[x][y] + 1
                        heapq.heappush(heap, (dp[nx][ny], nx, ny))

        return dp

# 测试用例
if __name__ == "__main__":
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    print(Solution().updateMatrix(mat))
```



```python
from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dp = [[float('inf')] * n for _ in range(m)]
        queue = deque()

        # 将所有0的元素加入队列并初始化dp数组
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                    queue.append((i, j))

        # 定义四个方向的移动
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # BFS开始
        while queue:
            x, y = queue.popleft()
            # 对当前点的四个方向进行处理
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    # 如果新位置的dp值可以更新（即发现更短的路径）
                    if dp[nx][ny] > dp[x][y] + 1:
                        dp[nx][ny] = dp[x][y] + 1
                        queue.append((nx, ny))

        return dp

# 测试用例
if __name__ == "__main__":
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    print(Solution().updateMatrix(mat))
```





```python
from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j-1]+1)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i < m-1:
                        dp[i][j] = min(dp[i][j], dp[i+1][j]+1)
                    if j < n-1:
                        dp[i][j] = min(dp[i][j], dp[i][j+1]+1)
        return dp

if __name__ == "__main__":
    mat = [[0,0,0],[0,1,0],[0,0,0]]
    print(Solution().updateMatrix(mat))
```



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



## 142.环形链表II

https://leetcode.cn/problems/linked-list-cycle-ii/

给定一个链表的头节点  `head` ，返回链表开始入环的第一个节点。 *如果链表无环，则返回 `null`。*

如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（**索引从 0 开始**）。如果 `pos` 是 `-1`，则在该链表中没有环。**注意：`pos` 不作为参数进行传递**，仅仅是为了标识链表的实际情况。

**不允许修改** 链表。

 

**示例 1：**

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

```
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
```

**示例 2：**

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png)

```
输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。
```

**示例 3：**

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png)

```
输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。
```

 

**提示：**

- 链表中节点的数目范围在范围 `[0, 104]` 内
- `-105 <= Node.val <= 105`
- `pos` 的值为 `-1` 或者链表中的一个有效索引



```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        return None
```



## 155.最小栈

辅助栈, https://leetcode.cn/problems/min-stack/

设计一个支持 `push` ，`pop` ，`top` 操作，并能在常数时间内检索到最小元素的栈。

实现 `MinStack` 类:

- `MinStack()` 初始化堆栈对象。
- `void push(int val)` 将元素val推入堆栈。
- `void pop()` 删除堆栈顶部的元素。
- `int top()` 获取堆栈顶部的元素。
- `int getMin()` 获取堆栈中的最小元素。

 

**示例 1:**

```
输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
```

 

**提示：**

- `-231 <= val <= 231 - 1`
- `pop`、`top` 和 `getMin` 操作总是在 **非空栈** 上调用
- `push`, `pop`, `top`, and `getMin`最多被调用 `3 * 104` 次



```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```





## 200.岛屿数量

dfs, https://leetcode.cn/problems/number-of-islands/ 

给你一个由 `'1'`（陆地）和 `'0'`（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

**示例 1：**

```
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
```

**示例 2：**

```
输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
```

 

**提示：**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` 的值为 `'0'` 或 `'1'`



```python
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count
```



## 240.搜索二维矩阵II

https://leetcode.cn/problems/search-a-2d-matrix-ii/

编写一个高效的算法来搜索 `*m* x *n*` 矩阵 `matrix` 中的一个目标值 `target` 。该矩阵具有以下特性：

- 每行的元素从左到右升序排列。
- 每列的元素从上到下升序排列。

 

**示例 1：**

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/25/searchgrid2.jpg)

```
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
输出：true
```

**示例 2：**

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/25/searchgrid.jpg)

```
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
输出：false
```

 

**提示：**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= n, m <= 300`
- `-109 <= matrix[i][j] <= 109`
- 每行的所有元素从左到右升序排列
- 每列的所有元素从上到下升序排列
- `-109 <= target <= 109`



```python
from typing import List
import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            # 在每行中使用 bisect_left 查找目标值的插入位置
            index = bisect.bisect_left(row, target)
            # 检查插入位置是否有效且等于目标值
            if index < len(row) and row[index] == target:
                return True
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5))  # 输出: True
    print(sol.searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20)) # 输出: False
    print(sol.searchMatrix([[1]], 1))  # 输出: True
```



参照源码实现二分，https://github.com/python/cpython/blob/main/Lib/bisect.py

```python
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            lo, hi = 0, len(row)
            while lo < hi:
                mid = (lo + hi) // 2
                if row[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            # 在找到的位置检查是否是目标值
            if lo < len(row) and row[lo] == target:
                return True
        return False  # 如果未找到目标值

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5))  # 输出: True

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
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # 空字符串可以被表示
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        
        return dp[n]
```



```python
from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def dfs(x):
            if len(x) == 0:
                return True
            for i in range(1, len(x)+1):
                if x[0:i] in wordDict and dfs(x[i:]):
                    return True
            return False

        return dfs(s)
if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(Solution().wordBreak(s, wordDict)) # True

    # s = "applepenapple"
    # wordDict = ["apple", "pen"]
    # print(Solution().wordBreak(s, wordDict)) # True
    #
    # s = "catsandog"
    # wordDict = ["cats", "dog", "sand", "and", "cat"]
    # print(Solution().wordBreak(s, wordDict)) # False
```



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



## 189.轮转数组

two pointers, https://leetcode.cn/problems/rotate-array/

给定一个整数数组 `nums`，将数组中的元素向右轮转 `k` 个位置，其中 `k` 是非负数。

 

**示例 1:**

```
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
```

**示例 2:**

```
输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释: 
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]
```

 

**提示：**

- `1 <= nums.length <= 105`
- `-231 <= nums[i] <= 231 - 1`
- `0 <= k <= 105`

 

**进阶：**

- 尽可能想出更多的解决方案，至少有 **三种** 不同的方法可以解决这个问题。
- 你可以使用空间复杂度为 `O(1)` 的 **原地** 算法解决这个问题吗？



```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        l, r = 0, len(nums) - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
```



## 238.除自身以外数组的乘积

前缀和, https://leetcode.cn/problems/product-of-array-except-self/

给你一个整数数组 `nums`，返回 数组 `answer` ，其中 `answer[i]` 等于 `nums` 中除 `nums[i]` 之外其余各元素的乘积 。

题目数据 **保证** 数组 `nums`之中任意元素的全部前缀元素和后缀的乘积都在 **32 位** 整数范围内。

请 **不要使用除法，**且在 `O(n)` 时间复杂度内完成此题。

 

**示例 1:**

```
输入: nums = [1,2,3,4]
输出: [24,12,8,6]
```

**示例 2:**

```
输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]
```

 

**提示：**

- `2 <= nums.length <= 105`
- `-30 <= nums[i] <= 30`
- **保证** 数组 `nums`之中任意元素的全部前缀元素和后缀的乘积都在 **32 位** 整数范围内

 

**进阶：**你可以在 `O(1)` 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 **不被视为** 额外空间。）



```python
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_mul = []
        ans = [1] * n
        product = 1
        for i in range(n):
            product *= nums[i]
            prefix_mul.append(product)
        suffix_mul = []
        product = 1
        for i in range(n - 1, -1, -1):
            product *= nums[i]
            suffix_mul.append(product)
        suffix_mul.reverse()
        for i in range(n):
            if i == 0:
                ans[i] = suffix_mul[i + 1]
            elif i == n - 1:
                ans[i] = prefix_mul[i - 1]
            else:
                ans[i] = prefix_mul[i - 1] * suffix_mul[i + 1]
        
        return ans
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



这是一个贪心问题，考虑局部最优的情形，我们需要将两个峰值之间的数全部删去，来保证子序列中每个元素都是摆动的。
但考虑到有非严格递增的情形，如1，2，2，2，1，摆动长度为3。我们可以设置一个trend来表示前一个摆动的趋势，如初始/非严格单调为0，递增为1，递减为-1。
那么只需要`nums[i] > nums[i-1]` 且`trend ≤ 0` 就能表示出现了一个递增的摆动，递减的摆动同理。最后统计摆动个数即可。


```python
# 徐梓文 24医学预科办
from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        ans,trend=1,0
        
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1] and trend<=0:
                ans+=1
                trend=1
            if nums[i]<nums[i-1] and trend>=0:
                ans+=1
                trend=-1
                
        return ans
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





## 452.用最少量的箭引爆气球

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



## 560.和为K的子数组

https://leetcode.cn/problems/subarray-sum-equals-k/

给你一个整数数组 `nums` 和一个整数 `k` ，请你统计并返回 *该数组中和为 `k` 的子数组的个数* 。

子数组是数组中元素的连续非空序列。

 

**示例 1：**

```
输入：nums = [1,1,1], k = 2
输出：2
```

**示例 2：**

```
输入：nums = [1,2,3], k = 3
输出：2
```

 

**提示：**

- `1 <= nums.length <= 2 * 104`
- `-1000 <= nums[i] <= 1000`
- `-107 <= k <= 107`



```python
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict

        # 哈希表用于存储每个前缀和出现的次数
        prefix_sum_count = defaultdict(int)
        # 初始化前缀和为0的情况出现一次，为了处理整个子数组和恰好为k的情况
        prefix_sum_count[0] = 1

        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num
            # 查找当前前缀和减去目标值k的前缀和数量，并添加到结果计数器
            if (current_sum - k) in prefix_sum_count:
                count += prefix_sum_count[current_sum - k]
            # 更新当前前缀和的数量
            prefix_sum_count[current_sum] += 1

        return count


# test code
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 1]
    k = 2
    print(sol.subarraySum(nums, k))  # expect 2

```





## 698.划分为k个相等的子集

dfs, https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/

给定一个整数数组 `nums` 和一个正整数 `k`，找出是否有可能把这个数组分成 `k` 个非空子集，其总和都相等。

 

**示例 1：**

```
输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
```

**示例 2:**

```
输入: nums = [1,2,3,4], k = 3
输出: false
```

 

**提示：**

- `1 <= k <= len(nums) <= 16`
- `0 < nums[i] < 10000`
- 每个元素的频率在 `[1,4]` 范围内





```python
from functools import lru_cache
from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
        nums.sort(reverse=True)
        
        # Early exit if the largest number is greater than the target
        if nums[0] > target:
            return False
        
        # The 'su' array keeps track of the sum of each subset
        su = [0] * k
        
        @lru_cache(maxsize=None)
        def recursion(nums_tuple, su_tuple):
            nums = list(nums_tuple)
            su = list(su_tuple)
            
            if not nums:
                return all(s == target for s in su)
            
            current_num = nums[0]
            for i in range(k):
                if su[i] + current_num <= target:
                    su[i] += current_num
                    if recursion(tuple(nums[1:]), tuple(su)):
                        return True
                    su[i] -= current_num
                    
                # If the current subset is empty and adding the number doesn't work, break
                if su[i] == 0:
                    break
            
            return False
        
        return recursion(tuple(nums), tuple(su))
```

Explanation of Changes:

1. **Tuple for `nums` and `su`**: We maintain the inputs to the recursive function as tuples, which are hashable and can be used in `lru_cache`. This ensures that the recursion doesn’t recompute already visited states.
2. **Early exit**: The condition `if nums[0] > target` ensures that if the largest number is greater than the target sum, we immediately return `False` (this avoids unnecessary computation).
3. **Optimized backtracking**: We exit the loop early if `su[i] == 0` to avoid repeating attempts to place the same number in already empty positions in `su`.



## 729.我的日程安排表I

https://leetcode.cn/problems/my-calendar-i/

实现一个 `MyCalendar` 类来存放你的日程安排。如果要添加的日程安排不会造成 **重复预订** ，则可以存储这个新的日程安排。

当两个日程安排有一些时间上的交叉时（例如两个日程安排都在同一时间内），就会产生 **重复预订**。

日程可以用一对整数 `startTime` 和 `endTime` 表示，这里的时间是半开区间，即 `[startTime, endTime)`, 实数 `x` 的范围为，  `startTime <= x < endTime` 。

实现 `MyCalendar` 类：

- `MyCalendar()` 初始化日历对象。
- `boolean book(int startTime, int endTime)` 如果可以将日程安排成功添加到日历中而不会导致重复预订，返回 `true` 。否则，返回 `false` 并且不要将该日程安排添加到日历中。

 

**示例：**

```
输入：
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
输出：
[null, true, false, true]

解释：
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False ，这个日程安排不能添加到日历中，因为时间 15 已经被另一个日程安排预订了。
myCalendar.book(20, 30); // return True ，这个日程安排可以添加到日历中，因为第一个日程安排预订的每个时间都小于 20 ，且不包含时间 20 。
```

 

**提示：**

- `0 <= start < end <= 109`
- 每个测试用例，调用 `book` 方法的次数最多不超过 `1000` 次。



```python
from sortedcontainers import SortedDict

class MyCalendar:
    def __init__(self):
        self.booked = SortedDict()

    def book(self, start: int, end: int) -> bool:
        i = self.booked.bisect_left(end)
        if i == 0 or self.booked.items()[i - 1][1] <= start:
            self.booked[start] = end
            return True
        return False

if __name__ == "__main__":
    obj = MyCalendar()
    print(obj.book(10, 20))
    print(obj.book(15, 25))
    print(obj.book(20, 30))
```



## 731.我的日程安排表II

https://leetcode.cn/problems/my-calendar-ii/

实现一个程序来存放你的日程安排。如果要添加的时间内不会导致三重预订时，则可以存储这个新的日程安排。

当三个日程安排有一些时间上的交叉时（例如三个日程安排都在同一时间内），就会产生 **三重预订**。

事件能够用一对整数 `startTime` 和 `endTime` 表示，在一个半开区间的时间 `[startTime, endTime)` 上预定。实数 `x` 的范围为 `startTime <= x < endTime`。

实现 `MyCalendarTwo` 类：

- `MyCalendarTwo()` 初始化日历对象。
- `boolean book(int startTime, int endTime)` 如果可以将日程安排成功添加到日历中而不会导致三重预订，返回 `true`。否则，返回 `false` 并且不要将该日程安排添加到日历中。

 

**示例 1：**

```
输入：
["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
输出：
[null, true, true, true, false, true, true]

解释：
MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
myCalendarTwo.book(10, 20); // 返回 True，能够预定该日程。
myCalendarTwo.book(50, 60); // 返回 True，能够预定该日程。
myCalendarTwo.book(10, 40); // 返回 True，该日程能够被重复预定。
myCalendarTwo.book(5, 15);  // 返回 False，该日程导致了三重预定，所以不能预定。
myCalendarTwo.book(5, 10); // 返回 True，能够预定该日程，因为它不使用已经双重预订的时间 10。
myCalendarTwo.book(25, 55); // 返回 True，能够预定该日程，因为时间段 [25, 40) 将被第三个日程重复预定，时间段 [40, 50) 将被单独预定，而时间段 [50, 55) 将被第二个日程重复预定。
```

 

**提示：**

- `0 <= start < end <= 109`
- 最多调用 `book` 1000 次。



```python
from sortedcontainers import SortedDict

class MyCalendarTwo:
    def __init__(self):
        self.d = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.d[start] = self.d.setdefault(start, 0) + 1
        self.d[end] = self.d.setdefault(end, 0) - 1

        ans = maxBook = 0
        for freq in self.d.values():
            maxBook += freq
            if maxBook > 2:
                self.d[start] = self.d.setdefault(start, 0) - 1
                self.d[end] = self.d.setdefault(end, 0) + 1
                return False
        return True

if __name__ == "__main__":
    obj = MyCalendarTwo()
    print(obj.book(10, 20))
    print(obj.book(50, 60))
    print(obj.book(10, 40))
    print(obj.book(5, 15))
    print(obj.book(5, 10))
    print(obj.book(25, 55))
    print(obj.book(15, 25))

```



## 994.腐烂的橘子

bfs, https://leetcode.cn/problems/rotting-oranges/

在给定的 `m x n` 网格 `grid` 中，每个单元格可以有以下三个值之一：

- 值 `0` 代表空单元格；
- 值 `1` 代表新鲜橘子；
- 值 `2` 代表腐烂的橘子。

每分钟，腐烂的橘子 **周围 4 个方向上相邻** 的新鲜橘子都会腐烂。

返回 *直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 `-1`* 。

 

**示例 1：**

**![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/16/oranges.png)**

```
输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
输出：4
```

**示例 2：**

```
输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个方向上。
```

**示例 3：**

```
输入：grid = [[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
```

 

**提示：**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10`
- `grid[i][j]` 仅为 `0`、`1` 或 `2`



```python
from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0

        # 初始化队列和统计新鲜橘子
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, minutes)
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # 定义4个方向
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        minutes = 0

        # 开始BFS
        while queue:
            r, c, minutes = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # 腐烂新鲜橘子
                    fresh_oranges -= 1
                    queue.append((nr, nc, minutes + 1))

        # 如果还有新鲜橘子，返回-1；否则返回分钟数
        return -1 if fresh_oranges > 0 else minutes
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



## 1143.最长公共子序列

dp, https://leetcode.cn/problems/longest-common-subsequence/

给定两个字符串 `text1` 和 `text2`，返回这两个字符串的最长 **公共子序列** 的长度。如果不存在 **公共子序列** ，返回 `0` 。

一个字符串的 **子序列** 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

- 例如，`"ace"` 是 `"abcde"` 的子序列，但 `"aec"` 不是 `"abcde"` 的子序列。

两个字符串的 **公共子序列** 是这两个字符串所共同拥有的子序列。

 

**示例 1：**

```
输入：text1 = "abcde", text2 = "ace" 
输出：3  
解释：最长公共子序列是 "ace" ，它的长度为 3 。
```

**示例 2：**

```
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc" ，它的长度为 3 。
```

**示例 3：**

```
输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。
```

 

**提示：**

- `1 <= text1.length, text2.length <= 1000`
- `text1` 和 `text2` 仅由小写英文字符组成。



```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # 创建一个 (m+1) x (n+1) 的 dp 数组，并初始化为0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 填充 dp 数组
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # 如果当前字符相同，则 LCS 长度加1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # 如果不同，则取两者中较大的LCS长度
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[-1][-1]
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



## 2241.设计一个ATM机器

https://leetcode.cn/problems/design-an-atm-machine/

一个 ATM 机器，存有 `5` 种面值的钞票：`20` ，`50` ，`100` ，`200` 和 `500` 美元。初始时，ATM 机是空的。用户可以用它存或者取任意数目的钱。

取款时，机器会优先取 **较大** 数额的钱。

- 比方说，你想取 `$300` ，并且机器里有 `2` 张 `$50` 的钞票，`1` 张 `$100` 的钞票和`1` 张 `$200` 的钞票，那么机器会取出 `$100` 和 `$200` 的钞票。
- 但是，如果你想取 `$600` ，机器里有 `3` 张 `$200` 的钞票和`1` 张 `$500` 的钞票，那么取款请求会被拒绝，因为机器会先取出 `$500` 的钞票，然后无法取出剩余的 `$100` 。注意，因为有 `$500` 钞票的存在，机器 **不能** 取 `$200` 的钞票。

请你实现 ATM 类：

- `ATM()` 初始化 ATM 对象。
- `void deposit(int[] banknotesCount)` 分别存入 `$20` ，`$50`，`$100`，`$200` 和 `$500` 钞票的数目。
- `int[] withdraw(int amount)` 返回一个长度为 `5` 的数组，分别表示 `$20` ，`$50`，`$100` ，`$200` 和 `$500` 钞票的数目，并且更新 ATM 机里取款后钞票的剩余数量。如果无法取出指定数额的钱，请返回 `[-1]` （这种情况下 **不** 取出任何钞票）。

 

**示例 1：**

```
输入：
["ATM", "deposit", "withdraw", "deposit", "withdraw", "withdraw"]
[[], [[0,0,1,2,1]], [600], [[0,1,0,1,1]], [600], [550]]
输出：
[null, null, [0,0,1,0,1], null, [-1], [0,1,0,0,1]]

解释：
ATM atm = new ATM();
atm.deposit([0,0,1,2,1]); // 存入 1 张 $100 ，2 张 $200 和 1 张 $500 的钞票。
atm.withdraw(600);        // 返回 [0,0,1,0,1] 。机器返回 1 张 $100 和 1 张 $500 的钞票。机器里剩余钞票的数量为 [0,0,0,2,0] 。
atm.deposit([0,1,0,1,1]); // 存入 1 张 $50 ，1 张 $200 和 1 张 $500 的钞票。
                          // 机器中剩余钞票数量为 [0,1,0,3,1] 。
atm.withdraw(600);        // 返回 [-1] 。机器会尝试取出 $500 的钞票，然后无法得到剩余的 $100 ，所以取款请求会被拒绝。
                          // 由于请求被拒绝，机器中钞票的数量不会发生改变。
atm.withdraw(550);        // 返回 [0,1,0,0,1] ，机器会返回 1 张 $50 的钞票和 1 张 $500 的钞票。
```

 

**提示：**

- `banknotesCount.length == 5`
- `0 <= banknotesCount[i] <= 109`
- `1 <= amount <= 109`
- **总共** 最多有 `5000` 次 `withdraw` 和 `deposit` 的调用。
- 函数 `withdraw` 和 `deposit` 至少各有 **一次** 调用。



```python
from typing import List
class ATM:

    def __init__(self):
        self.cnt = [0] * 5
        self.value = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.cnt[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        res = [0] * 5
        for i in range(4, -1, -1):
            res[i] = min(self.cnt[i], amount // self.value[i])
            amount -= res[i] * self.value[i]
        if amount == 0:
            for i in range(5):
                self.cnt[i] -= res[i]
            return res
        else:
            return [-1]

# Your ATM object will be instantiated and called as such:
if __name__ == '__main__':
    obj = ATM()
    obj.deposit([0,0,1,2,1])
    param_2 = obj.withdraw(600)
    print(param_2)

```



## 2266.统计打字方案数

Alice 在给 Bob 用手机打字。数字到字母的 **对应** 如下图所示。

<img src="https://pic.leetcode.cn/1722224025-gsUAIv-image.png" alt="img" style="zoom: 15%;" />

为了 **打出** 一个字母，Alice 需要 **按** 对应字母 `i` 次，`i` 是该字母在这个按键上所处的位置。

- 比方说，为了按出字母 `'s'` ，Alice 需要按 `'7'` 四次。类似的， Alice 需要按 `'5'` 两次得到字母 `'k'` 。
- 注意，数字 `'0'` 和 `'1'` 不映射到任何字母，所以 Alice **不** 使用它们。

但是，由于传输的错误，Bob 没有收到 Alice 打字的字母信息，反而收到了 **按键的字符串信息** 。

- 比方说，Alice 发出的信息为 `"bob"` ，Bob 将收到字符串 `"2266622"` 。

给你一个字符串 `pressedKeys` ，表示 Bob 收到的字符串，请你返回 Alice **总共可能发出多少种文字信息** 。

由于答案可能很大，将它对 `10^9 + 7` **取余** 后返回。

 

**示例 1：**

```
输入：pressedKeys = "22233"
输出：8
解释：
Alice 可能发出的文字信息包括：
"aaadd", "abdd", "badd", "cdd", "aaae", "abe", "bae" 和 "ce" 。
由于总共有 8 种可能的信息，所以我们返回 8 。
```

**示例 2：**

```
输入：pressedKeys = "222222222222222222222222222222222222"
输出：82876089
解释：
总共有 2082876103 种 Alice 可能发出的文字信息。
由于我们需要将答案对 10^9 + 7 取余，所以我们返回 2082876103 % (10^9 + 7) = 82876089 。
```

 

**提示：**

- `1 <= pressedKeys.length <= 10^5`
- `pressedKeys` 只包含数字 `'2'` 到 `'9'` 。



```python
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 10**9 + 7
        n = len(pressedKeys)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            dp[i] = dp[i - 1]

            if i > 1 and pressedKeys[i - 1] == pressedKeys[i - 2]:
                dp[i] = (dp[i] + dp[i - 2]) % MOD
            if i > 2 and pressedKeys[i-2] != pressedKeys[i-3]:
                continue
            if i > 2 and pressedKeys[i - 1] == pressedKeys[i - 3]:
                dp[i] = (dp[i] + dp[i - 3]) % MOD
            if i > 3 and pressedKeys[i-3] != pressedKeys[i-4]:
                continue
            if i > 3 and pressedKeys[i - 1] in '79' and pressedKeys[i - 1] == pressedKeys[i - 4]:
                dp[i] = (dp[i] + dp[i - 4]) % MOD

        return dp[n]

if __name__ == "__main__":
    pressedKeys = "344644885"
    print(Solution().countTexts(pressedKeys))  # Expected output: 8
```



## 2270.分割数组的方案数

https://leetcode.cn/problems/number-of-ways-to-split-array/

给你一个下标从 **0** 开始长度为 `n` 的整数数组 `nums` 。
如果以下描述为真，那么 `nums` 在下标 `i` 处有一个 **合法的分割** ：

- 前 `i + 1` 个元素的和 **大于等于** 剩下的 `n - i - 1` 个元素的和。
- 下标 `i` 的右边 **至少有一个** 元素，也就是说下标 `i` 满足 `0 <= i < n - 1` 。

请你返回 `nums` 中的 **合法分割** 方案数。

 

**示例 1：**

```
输入：nums = [10,4,-8,7]
输出：2
解释：
总共有 3 种不同的方案可以将 nums 分割成两个非空的部分：
- 在下标 0 处分割 nums 。那么第一部分为 [10] ，和为 10 。第二部分为 [4,-8,7] ，和为 3 。因为 10 >= 3 ，所以 i = 0 是一个合法的分割。
- 在下标 1 处分割 nums 。那么第一部分为 [10,4] ，和为 14 。第二部分为 [-8,7] ，和为 -1 。因为 14 >= -1 ，所以 i = 1 是一个合法的分割。
- 在下标 2 处分割 nums 。那么第一部分为 [10,4,-8] ，和为 6 。第二部分为 [7] ，和为 7 。因为 6 < 7 ，所以 i = 2 不是一个合法的分割。
所以 nums 中总共合法分割方案受为 2 。
```

**示例 2：**

```
输入：nums = [2,3,1,0]
输出：2
解释：
总共有 2 种 nums 的合法分割：
- 在下标 1 处分割 nums 。那么第一部分为 [2,3] ，和为 5 。第二部分为 [1,0] ，和为 1 。因为 5 >= 1 ，所以 i = 1 是一个合法的分割。
- 在下标 2 处分割 nums 。那么第一部分为 [2,3,1] ，和为 6 。第二部分为 [0] ，和为 0 。因为 6 >= 0 ，所以 i = 2 是一个合法的分割。
```

 

**提示：**

- `2 <= nums.length <= 10^5`
- `-105 <= nums[i] <= 10^5`



```python
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_v = sum(nums)
        prefix_sum = 0
        cnt = 0
        for i in nums[:-1]:
            prefix_sum += i
            if prefix_sum >= total_v - prefix_sum:
                cnt += 1
        
        return cnt
```





## 2274.不含特殊楼层的最大连续楼层数

dfs, https://leetcode.cn/problems/maximum-consecutive-floors-without-special-floors/

Alice 管理着一家公司，并租用大楼的部分楼层作为办公空间。Alice 决定将一些楼层作为 **特殊楼层** ，仅用于放松。

给你两个整数 `bottom` 和 `top` ，表示 Alice 租用了从 `bottom` 到 `top`（含 `bottom` 和 `top` 在内）的所有楼层。另给你一个整数数组 `special` ，其中 `special[i]` 表示 Alice 指定用于放松的特殊楼层。

返回不含特殊楼层的 **最大** 连续楼层数。

 

**示例 1：**

```
输入：bottom = 2, top = 9, special = [4,6]
输出：3
解释：下面列出的是不含特殊楼层的连续楼层范围：
- (2, 3) ，楼层数为 2 。
- (5, 5) ，楼层数为 1 。
- (7, 9) ，楼层数为 3 。
因此，返回最大连续楼层数 3 。
```

**示例 2：**

```
输入：bottom = 6, top = 8, special = [7,6,8]
输出：0
解释：每层楼都被规划为特殊楼层，所以返回 0 。
```

 

**提示**

- `1 <= special.length <= 105`
- `1 <= bottom <= special[i] <= top <= 109`
- `special` 中的所有值 **互不相同**



```python
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        max_consecutive = 0

        # Check the gap before the first special floor
        max_consecutive = max(max_consecutive, special[0] - bottom)

        # Check the gaps between consecutive special floors
        for i in range(1, len(special)):
            max_consecutive = max(max_consecutive, special[i] - special[i - 1] - 1)

        # Check the gap after the last special floor
        max_consecutive = max(max_consecutive, top - special[-1])

        return max_consecutive
        
```



## 2275.按位与结果大于零的最长组合

https://leetcode.cn/problems/largest-combination-with-bitwise-and-greater-than-zero/

对数组 `nums` 执行 **按位与** 相当于对数组 `nums` 中的所有整数执行 **按位与** 。

- 例如，对 `nums = [1, 5, 3]` 来说，按位与等于 `1 & 5 & 3 = 1` 。
- 同样，对 `nums = [7]` 而言，按位与等于 `7` 。

给你一个正整数数组 `candidates` 。计算 `candidates` 中的数字每种组合下 **按位与** 的结果。

返回按位与结果大于 `0` 的 **最长** 组合的长度*。*

 

**示例 1：**

```
输入：candidates = [16,17,71,62,12,24,14]
输出：4
解释：组合 [16,17,62,24] 的按位与结果是 16 & 17 & 62 & 24 = 16 > 0 。
组合长度是 4 。
可以证明不存在按位与结果大于 0 且长度大于 4 的组合。
注意，符合长度最大的组合可能不止一种。
例如，组合 [62,12,24,14] 的按位与结果是 62 & 12 & 24 & 14 = 8 > 0 。
```

**示例 2：**

```
输入：candidates = [8,8]
输出：2
解释：最长组合是 [8,8] ，按位与结果 8 & 8 = 8 > 0 。
组合长度是 2 ，所以返回 2 。
```

 

**提示：**

- `1 <= candidates.length <= 10^5`
- `1 <= candidates[i] <= 10^7`



找出所有整数在二进制表示中，任意位上为1的最大共同出现次数。

逐位计算：遍历所有存在该位为 1 元素的二进制位，并统计对应位数值为 1 的元素个数及最大值。对于二进制位的范围，由于 candidates 中的整数的取值范围均在 [1,10^7] 闭区间内，同时我们有 $2^{23} < 10^7 <2^{24}$，因此只需要遍历最低的 24 个二进制位即可。

```python
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # 初始化一个列表来记录每一位为1的数量
        bit_counts = [0] * 24
        
        # 遍历每个数字并更新每一位的计数
        for num in candidates:
            for i in range(24):
                if num & (1 << i):
                    bit_counts[i] += 1
        
        # 返回最大值
        return max(bit_counts)
```



用内置函数bin()，进一步优化

```python
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bit_counts = [0] * 24

        for num in candidates:
            binary_str = bin(num)[2:][::-1]
            for i, bit in enumerate(binary_str):
                if bit == '1':
                    bit_counts[i] += 1

        return max(bit_counts)
```





## 2947.统计美丽子字符串 I

https://leetcode.cn/problems/count-beautiful-substrings-i/

给你一个字符串 `s` 和一个正整数 `k` 。

用 `vowels` 和 `consonants` 分别表示字符串中元音字母和辅音字母的数量。

如果某个字符串满足以下条件，则称其为 **美丽字符串** ：

- `vowels == consonants`，即元音字母和辅音字母的数量相等。
- `(vowels * consonants) % k == 0`，即元音字母和辅音字母的数量的乘积能被 `k` 整除。

返回字符串 `s` 中 **非空美丽子字符串** 的数量。

子字符串是字符串中的一个连续字符序列。

英语中的 **元音字母** 为 `'a'`、`'e'`、`'i'`、`'o'` 和 `'u'` 。

英语中的 **辅音字母** 为除了元音字母之外的所有字母。

 

**示例 1：**

```
输入：s = "baeyh", k = 2
输出：2
解释：字符串 s 中有 2 个美丽子字符串。
- 子字符串 "baeyh"，vowels = 2（["a","e"]），consonants = 2（["y","h"]）。
可以看出字符串 "aeyh" 是美丽字符串，因为 vowels == consonants 且 vowels * consonants % k == 0 。
- 子字符串 "baeyh"，vowels = 2（["a","e"]），consonants = 2（["b","y"]）。
可以看出字符串 "baey" 是美丽字符串，因为 vowels == consonants 且 vowels * consonants % k == 0 。
可以证明字符串 s 中只有 2 个美丽子字符串。
```

**示例 2：**

```
输入：s = "abba", k = 1
输出：3
解释：字符串 s 中有 3 个美丽子字符串。
- 子字符串 "abba"，vowels = 1（["a"]），consonants = 1（["b"]）。
- 子字符串 "abba"，vowels = 1（["a"]），consonants = 1（["b"]）。
- 子字符串 "abba"，vowels = 2（["a","a"]），consonants = 2（["b","b"]）。
可以证明字符串 s 中只有 3 个美丽子字符串。
```

**示例 3：**

```
输入：s = "bcdf", k = 1
输出：0
解释：字符串 s 中没有美丽子字符串。
```

 

**提示：**

- `1 <= s.length <= 1000`
- `1 <= k <= 1000`
- `s` 仅由小写英文字母组成。



```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)
        beautiful_count = 0

        # 遍历所有子字符串
        for i in range(n):
            vowels = 0
            consonants = 0
            for j in range(i, n):
                if s[j] in vowels_set:
                    vowels += 1
                else:
                    consonants += 1

                # 检查美丽字符串条件
                if vowels == consonants and (vowels * consonants) % k == 0:
                    beautiful_count += 1

        return beautiful_count

if __name__ == '__main__':
    s = Solution()
    print(s.beautifulSubstrings("aeiou", 2))  # 输出: 2
    print(s.beautifulSubstrings("aba", 1))  # 输出: 2
    print(s.beautifulSubstrings("baeyh", 2))  # 输出: 2
    print(s.beautifulSubstrings("abba", 1))  # 输出: 3
    print(s.beautifulSubstrings("bcdf", 1))  # 输出: 0


```



## 3066.超过阈值的最少操作数II

heap, https://leetcode.cn/problems/minimum-operations-to-exceed-threshold-value-ii/

给你一个下标从 **0** 开始的整数数组 `nums` 和一个整数 `k` 。

一次操作中，你将执行：

- 选择 `nums` 中最小的两个整数 `x` 和 `y` 。
- 将 `x` 和 `y` 从 `nums` 中删除。
- 将 `min(x, y) * 2 + max(x, y)` 添加到数组中的任意位置。

**注意，**只有当 `nums` 至少包含两个元素时，你才可以执行以上操作。

你需要使数组中的所有元素都大于或等于 `k` ，请你返回需要的 **最少** 操作次数。

 

**示例 1：**

```
输入：nums = [2,11,10,1,3], k = 10
输出：2
解释：第一次操作中，我们删除元素 1 和 2 ，然后添加 1 * 2 + 2 到 nums 中，nums 变为 [4, 11, 10, 3] 。
第二次操作中，我们删除元素 3 和 4 ，然后添加 3 * 2 + 4 到 nums 中，nums 变为 [10, 11, 10] 。
此时，数组中的所有元素都大于等于 10 ，所以我们停止操作。
使数组中所有元素都大于等于 10 需要的最少操作次数为 2 。
```

**示例 2：**

```
输入：nums = [1,1,2,4,9], k = 20
输出：4
解释：第一次操作后，nums 变为 [2, 4, 9, 3] 。
第二次操作后，nums 变为 [7, 4, 9] 。
第三次操作后，nums 变为 [15, 9] 。
第四次操作后，nums 变为 [33] 。
此时，数组中的所有元素都大于等于 20 ，所以我们停止操作。
使数组中所有元素都大于等于 20 需要的最少操作次数为 4 。
```

 

**提示：**

- `2 <= nums.length <= 2 * 105`
- `1 <= nums[i] <= 109`
- `1 <= k <= 109`
- 输入保证答案一定存在，也就是说一定存在一个操作序列使数组中所有元素都大于等于 `k`。



```python
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        import heapq
        cnt = 0
        heapq.heapify(nums)
        while len(nums)>=2 and nums[0]<k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x,y)*2 + max(x,y))
            cnt += 1
        return cnt
```



## 3097.或值至少为K的最短子数组II

https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-ii/

给你一个 **非负** 整数数组 `nums` 和一个整数 `k` 。

如果一个数组中所有元素的按位或运算 `OR` 的值 **至少** 为 `k` ，那么我们称这个数组是 **特别的** 。

请你返回 `nums` 中 **最短特别非空** 子数组的长度，如果特别子数组不存在，那么返回 `-1` 。

**示例 1：**

**输入：**nums = [1,2,3], k = 2

**输出：**1

**解释：**

子数组 `[3]` 的按位 `OR` 值为 `3` ，所以我们返回 `1` 。

**示例 2：**

**输入：**nums = [2,1,8], k = 10

**输出：**3

**解释：**

子数组 `[2,1,8]` 的按位 `OR` 值为 `11` ，所以我们返回 `3` 。

**示例 3：**

**输入：**nums = [1,2], k = 0

**输出：**1

**解释：**

子数组 `[1]` 的按位 `OR` 值为 `1` ，所以我们返回 `1` 。

 

**提示：**

- `1 <= nums.length <= 2 * 105`
- `0 <= nums[i] <= 109`
- `0 <= k <= 109`



```python
from typing import List
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        bits = [0] * 30
        minv = float('inf')
        def sum_bits():
            return sum([1 << i for i in range(30) if bits[i] > 0])

        left = 0
        for right in range(len(nums)):
            for i in range(30):
                if nums[right] & (1 << i):
                    bits[i] += 1
            while left <= right and sum_bits() >= k:
                minv = min(minv, right - left + 1)
                for i in range(30):
                    if nums[left] & (1 << i):
                        bits[i] -= 1
                left += 1

        return minv if minv != float('inf') else -1
```





## 3297.统计重新排列后包含另一个字符串的子字符串数目I

滑动窗口，https://leetcode.cn/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/

给你两个字符串 `word1` 和 `word2` 。

如果一个字符串 `x` 重新排列后，`word2` 是重排字符串的前缀，那么我们称字符串 `x` 是 **合法的** 。

请你返回 `word1` 中 **合法** 子字符串的数目。



**示例 1：**

**输入：**word1 = "bcca", word2 = "abc"

**输出：**1

**解释：**

唯一合法的子字符串是 `"bcca"` ，可以重新排列得到 `"abcc"` ，`"abc"` 是它的前缀。

**示例 2：**

**输入：**word1 = "abcabc", word2 = "abc"

**输出：**10

**解释：**

除了长度为 1 和 2 的所有子字符串都是合法的。

**示例 3：**

**输入：**word1 = "abcabc", word2 = "aaabc"

**输出：**0

 

**解释：**

- `1 <= word1.length <= 10^5`
- `1 <= word2.length <= 10^4`
- `word1` 和 `word2` 都只包含小写英文字母。





这明明是困难，谁把它归到了中等难度。

```python
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        diff = [0] * 26
        for c in word2:
            diff[ord(c) - ord('a')] -= 1

        res = 0
        cnt = sum(1 for c in diff if c < 0)

        def update(c: int, add: int):
            nonlocal cnt
            diff[c] += add
            if add == 1 and diff[c] == 0:
                # 表明 diff[c] 由 -1 变为 0
                cnt -= 1
            elif add == -1 and diff[c] == -1:
                # 表明 diff[c] 由 0 变为 -1
                cnt += 1

        l, r = 0, 0
        while l < len(word1):
            while r < len(word1) and cnt > 0:
                update(ord(word1[r]) - ord('a'), 1)
                r += 1
            if cnt == 0:
                res += len(word1) - r + 1
            update(ord(word1[l]) - ord('a'), -1)
            l += 1

        return res
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



## 37.解数独

backtracking, https://leetcode.cn/problems/sudoku-solver/

编写一个程序，通过填充空格来解决数独问题。

数独的解法需 **遵循如下规则**：

1. 数字 `1-9` 在每一行只能出现一次。
2. 数字 `1-9` 在每一列只能出现一次。
3. 数字 `1-9` 在每一个以粗实线分隔的 `3x3` 宫内只能出现一次。（请参考示例图）

数独部分空格内已填入了数字，空白格用 `'.'` 表示。

 

**示例 1：**

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/04/12/250px-sudoku-by-l2g-20050714svg.png)

```
输入：board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
输出：[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
解释：输入的数独如上图所示，唯一有效的解决方案如下所示：
```

 

**提示：**

- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` 是一位数字或者 `'.'`
- 题目数据 **保证** 输入数独仅有一个解



这个代码超时了，如何优化

```python
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def is_valid(row, col, val, board):
            for i in range(9):
                if board[row][i] == val or board[i][col] == val:
                    return False
            start_row, start_col = row - row % 3, col - col % 3
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == val:
                        return False
            return True

        def backtrack(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for k in range(1, 10):
                            val = str(k)
                            if is_valid(i, j, val, board):
                                board[i][j] = val
                                if backtrack(board):
                                    return True
                                board[i][j] = '.'
                        return False
            return True

        backtrack(board)
```





你提供的代码是一个典型的数独解法，使用了回溯法。对于超时问题，可以从以下几个方向进行优化：

**1. 提前检查列、行和3x3宫内的合法性**

每次调用 `is_valid` 时，都会遍历整个行、列和3x3宫，检查是否合法。这是导致超时的主要原因之一。我们可以通过缓存这些信息来减少冗余计算。

**2. 使用集合来存储已使用的数字**

我们可以使用三个集合来分别跟踪每行、每列和每个3x3宫内的已用数字，从而避免每次都进行完全的遍历。

**3. 选择最优的空格进行回溯**

在回溯过程中，可以尝试优先填充空格数量最少的地方（即空格周围已填数字最少的地方）。这将减少回溯的次数。

**代码优化：**

```python
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        # 记录行、列、3x3宫中已经使用的数字
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # 初始化已经填入的数字
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = board[i][j]
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + (j // 3)].add(val)
        
        # 回溯函数
        def backtrack(i, j):
            if i == 9:  # 如果行遍历完成，说明已解答完毕
                return True
            if j == 9:  # 如果列遍历完成，跳到下一行
                return backtrack(i + 1, 0)
            if board[i][j] != '.':  # 已经填充过的格子，跳过
                return backtrack(i, j + 1)

            # 尝试填充每个数字 1-9
            for num in range(1, 10):
                num_str = str(num)
                box_idx = (i // 3) * 3 + (j // 3)
                if num_str not in rows[i] and num_str not in cols[j] and num_str not in boxes[box_idx]:
                    # 填充数字
                    board[i][j] = num_str
                    rows[i].add(num_str)
                    cols[j].add(num_str)
                    boxes[box_idx].add(num_str)

                    # 继续回溯
                    if backtrack(i, j + 1):
                        return True

                    # 回溯时撤销选择
                    board[i][j] = '.'
                    rows[i].remove(num_str)
                    cols[j].remove(num_str)
                    boxes[box_idx].remove(num_str)

            return False
        
        # 从(0,0)开始回溯
        backtrack(0, 0)
```

**关键优化点：**

1. **缓存行、列和宫内的数字**： 使用三个 `set` 列表（`rows`, `cols`, `boxes`）来缓存每个行、列和宫中已经填入的数字，避免在每次回溯时重新遍历。
2. **减少 `is_valid` 的调用**： 通过使用 `set` 来检查数字是否已经在当前行、列或宫内，这样比遍历整个行、列和宫要高效得多。
3. **回溯的条件优化**：
   - 每次处理一个格子时，只有在格子为空 (`.`) 时才会进行数字填充和回溯。
   - 用行、列和宫的限制条件来提前剪枝，避免不必要的回溯。

**时间复杂度：**

通过使用 `set` 来进行快速查询，减少了每次合法性检查的时间复杂度。整体的时间复杂度接近 `O(9^(N^2))`，但由于回溯过程中有效的剪枝和预处理，实际表现会更快。





## 41.缺失的第一个正数

标记，置换，https://leetcode.cn/problems/first-missing-positive/

给你一个未排序的整数数组 `nums` ，请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 `O(n)` 并且只使用常数级别额外空间的解决方案。

 

**示例 1：**

```
输入：nums = [1,2,0]
输出：3
解释：范围 [1,2] 中的数字都在数组中。
```

**示例 2：**

```
输入：nums = [3,4,-1,1]
输出：2
解释：1 在数组中，但 2 没有。
```

**示例 3：**

```
输入：nums = [7,8,9,11,12]
输出：1
解释：最小的正数 1 没有出现。
```

 

**提示：**

- `1 <= nums.length <= 105`
- `-231 <= nums[i] <= 231 - 1`



这个解法，使用了集合，不满足题面“使用常数级别额外空间”。

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*(n+1)
        minv = 1
        visited = set()
        for i in nums:
            if i < 1:
                continue
            visited.add(i)
            if minv == i:
                tmp = minv + 1
                while tmp in visited:
                    tmp += 1
                minv = tmp
        return minv
```



LeetCode题解：

https://leetcode.cn/problems/first-missing-positive/solutions/304743/que-shi-de-di-yi-ge-zheng-shu-by-leetcode-solution/

实际上，对于一个长度为 N 的数组，其中没有出现的最小正整数只能在 [1,N+1] 中。这是因为如果 [1,N] 都出现了，那么答案是 N+1，否则答案是 [1,N] 中没有出现的最小正整数。这样一来，我们将所有在 [1,N] 范围内的数放入哈希表，也可以得到最终的答案。而给定的数组恰好长度为 N，这让我们有了一种将数组设计成哈希表的思路：

我们对数组进行遍历，对于遍历到的数 x，如果它在 [1,N] 的范围内，那么就将数组中的第 x−1 个位置（注意：数组下标从 0 开始）打上「标记」。在遍历结束之后，如果所有的位置都被打上了标记，那么答案是 N+1，否则答案是最小的没有打上标记的位置加 1。

那么如何设计这个「标记」呢？由于数组中的数没有任何限制，因此这并不是一件容易的事情。但我们可以继续利用上面的提到的性质：由于我们只在意 [1,N] 中的数，因此我们可以先对数组进行遍历，把不在 [1,N] 范围内的数修改成任意一个大于 N 的数（例如 N+1）。这样一来，数组中的所有数就都是正数了，因此我们就可以将「标记」表示为「负号」。算法的流程如下：

我们将数组中所有小于等于 0 的数修改为 N+1；

我们遍历数组中的每一个数 x，它可能已经被打了标记，因此原本对应的数为 ∣x∣，其中 ∣∣ 为绝对值符号。如果 ∣x∣∈[1,N]，那么我们给数组中的第 ∣x∣−1 个位置的数添加一个负号。注意如果它已经有负号，不需要重复添加；

在遍历完成之后，如果数组中的每一个数都是负数，那么答案是 N+1，否则答案是第一个正数的位置加 1。

![fig1](https://assets.leetcode-cn.com/solution-static/41/41_fig1.png)



```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        return n + 1
```

复杂度分析

时间复杂度：O(N)，其中 N 是数组的长度。

空间复杂度：O(1)。



方法二：置换

除了打标记以外，我们还可以使用置换的方法，将给定的数组「恢复」成下面的形式：

如果数组中包含 $x \in [1,N]$，那么恢复后，数组的第 x−1 个元素为 x。

在恢复后，数组应当有 [1, 2, ..., N] 的形式，但其中有若干个位置上的数是错误的，每一个错误的位置就代表了一个缺失的正数。以题目中的示例二 [3, 4, -1, 1] 为例，恢复后的数组应当为 [1, -1, 3, 4]，我们就可以知道缺失的数为 2。

那么我们如何将数组进行恢复呢？我们可以对数组进行一次遍历，对于遍历到的数 x=nums[i]，如果 x∈[1,N]，我们就知道 x 应当出现在数组中的 x−1 的位置，因此交换 nums[i] 和 nums[x−1]，这样 x 就出现在了正确的位置。在完成交换后，新的 nums[i] 可能还在 [1,N] 的范围内，我们需要继续进行交换操作，直到 $x \notin [1,N]$。

注意到上面的方法可能会陷入死循环。如果 nums[i] 恰好与 nums[x−1] 相等，那么就会无限交换下去。此时我们有 nums[i]=x=nums[x−1]，说明 x 已经出现在了正确的位置。因此我们可以跳出循环，开始遍历下一个数。

由于每次的交换操作都会使得某一个数交换到正确的位置，因此交换的次数最多为 N，整个方法的时间复杂度为 O(N)。

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
```

**复杂度分析**

- 时间复杂度：*O*(*N*)，其中 *N* 是数组的长度。
- 空间复杂度：*O*(1)。





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



双指针

```python
class Solution:
    def trap(self, height: List[int]) -> int:
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
        return ans

```



> 单调栈相当于按行接雨水，双指针相当于按列接雨水？
>
> 确实，单调栈和双指针方法在处理“接雨水”问题时采用了不同的思路，但最终都能正确计算出能够接住的雨水总量。下面简要分析这两种方法的工作原理：
>
> **单调栈（按行接雨水）**
>
> 单调栈方法通过维护一个递减栈来找到每个位置左侧和右侧的第一个更高柱子，进而计算该位置上方能接住的雨水量。这种方法可以看作是逐行计算雨水量，因为每次从栈中弹出一个元素时，实际上是在计算该元素上方的水平层（即一行）的雨水量。具体来说，当遇到一个比栈顶元素高的柱子时，就找到了一个可以蓄水的区域，然后根据左右边界的高度差和距离计算出该行的雨水量。
>
> **双指针（按列接雨水）**
>
> 双指针方法则是通过两个指针从数组的两端向中间移动，同时记录左右两边的最大高度。在每一步中，选择较短的一边进行处理，因为水位总是由较短的一边决定的。如果左边高度小于右边高度，那么左边当前柱子上方能接住的雨水量就是左边最大高度减去当前高度；反之亦然。这种方法可以看作是逐列计算雨水量，因为每次移动指针时，实际上是在计算当前指针所指向柱子上方的雨水量。
>
> **比较**
>
> - **单调栈** 更适合理解为按照行来计算雨水量，因为它关注的是每个局部凹陷处（即两根较高柱子之间的一根或几根较低柱子）的雨水量，这些凹陷处可以想象成一个个水平的水层。
> - **双指针** 则更适合理解为按照列来计算雨水量，因为它直接计算每个柱子上方能接住的雨水量，而不需要显式地找出每个凹陷处。
>
> 两种方法虽然计算方式不同，但是都能有效地解决问题，并且时间复杂度都是 O(n)，其中 n 是高度数组的长度。空间复杂度方面，单调栈方法需要额外的空间来存储栈，而双指针方法只需要常数级别的额外空间。





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



## 239.滑动窗口最大值

队列, 滑动窗口, 单调队列, https://leetcode.cn/problems/sliding-window-maximum/

给你一个整数数组 `nums`，有一个大小为 `k` 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 `k` 个数字。滑动窗口每次只向右移动一位。

返回 *滑动窗口中的最大值* 。

 

**示例 1：**

```
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

**示例 2：**

```
输入：nums = [1], k = 1
输出：[1]
```

 

**提示：**

- `1 <= nums.length <= 105`
- `-104 <= nums[i] <= 104`
- `1 <= k <= nums.length`



```python
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        n = len(nums)
        if k == 1:
            return nums

        deque_index = deque()  # 存储索引，保持双端队列中的值递减
        res = []

        for i in range(n):
            # 移除滑出窗口的元素（队首元素）
            if deque_index and deque_index[0] < i - k + 1:
                deque_index.popleft()

            # 移除所有小于当前元素的队尾元素
            while deque_index and nums[deque_index[-1]] < nums[i]:
                deque_index.pop()

            # 将当前元素的索引加入队列
            deque_index.append(i)

            # 从第 k 个元素开始记录结果，队首始终是窗口的最大值
            if i >= k - 1:
                res.append(nums[deque_index[0]])

        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) # [3,3,5,5,6,7]

```

> **单调队列的维护**：
>
> - 队列中存储的是元素的索引，并且始终保持从队首到队尾对应的元素值是递减的。
> - 每次滑动窗口时，移除不在窗口范围内的元素（队首检查）和小于当前元素的值（队尾检查）。
>
> **高效计算最大值**：
>
> - 队首元素的索引始终对应当前窗口的最大值，直接添加到结果中，避免了调用 `max` 的重复计算。
>
> **时间复杂度优化**：
>
> - 每个元素最多被加入和移出队列一次，因此总时间复杂度为 O(n)。



## 517.超级洗衣机

greedy, https://leetcode.cn/problems/super-washing-machines/

假设有 `n` 台超级洗衣机放在同一排上。开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的。

在每一步操作中，你可以选择任意 `m` (`1 <= m <= n`) 台洗衣机，与此同时将每台洗衣机的一件衣服送到相邻的一台洗衣机。

给定一个整数数组 `machines` 代表从左至右每台洗衣机中的衣物数量，请给出能让所有洗衣机中剩下的衣物的数量相等的 **最少的操作步数** 。如果不能使每台洗衣机中衣物的数量相等，则返回 `-1` 。

 

**示例 1：**

```
输入：machines = [1,0,5]
输出：3
解释：
第一步:    1     0 <-- 5    =>    1     1     4
第二步:    1 <-- 1 <-- 4    =>    2     1     3    
第三步:    2     1 <-- 3    =>    2     2     2   
```

**示例 2：**

```
输入：machines = [0,3,0]
输出：2
解释：
第一步:    0 <-- 3     0    =>    1     2     0    
第二步:    1     2 --> 0    =>    1     1     1     
```

**示例 3：**

```
输入：machines = [0,2,0]
输出：-1
解释：
不可能让所有三个洗衣机同时剩下相同数量的衣物。
```

 

**提示：**

- `n == machines.length`
- `1 <= n <= 104`
- `0 <= machines[i] <= 105`



```python
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        avg, mod = divmod(sum(machines), len(machines))
        if mod != 0:
            return -1
        """
        先将所有数减去平均值，然后取前缀和，然后将左侧的元素作为整体考虑：
        如果前缀和`prefixSum[i]`大于0，则该整体必须向右侧移出`prefixSum[i]`个单位，所需步数为`prefixSum[i]`
        如果前缀和`prefixSum[i]`小于0，则右侧必须向该整体移入`prefixSum[i]`个单位，所需步数为`-prefixSum[i]`

        而又因为一台洗衣机可以同时接受两侧的移入，但不可以同时向两侧移出
        所以最少步数必然不小于单台洗衣机移出需要的最大步数
        """
        ans = x = 0
        for n in machines:
            x += n - avg
            ans = max(ans, n - avg, abs(x))

        return ans
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



## 732.我的日程安排表III

区间重叠, https://leetcode.cn/problems/my-calendar-iii/

当 `k` 个日程存在一些非空交集时（即, `k` 个日程包含了一些相同时间），就会产生 `k` 次预订。

给你一些日程安排 `[startTime, endTime)` ，请你在每个日程安排添加后，返回一个整数 `k` ，表示所有先前日程安排会产生的最大 `k` 次预订。

实现一个 `MyCalendarThree` 类来存放你的日程安排，你可以一直添加新的日程安排。

- `MyCalendarThree()` 初始化对象。
- `int book(int startTime, int endTime)` 返回一个整数 `k` ，表示日历中存在的 `k` 次预订的最大值。

 

**示例：**

```
输入：
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
输出：
[null, 1, 1, 2, 3, 3, 3]

解释：
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // 返回 1 ，第一个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
myCalendarThree.book(50, 60); // 返回 1 ，第二个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
myCalendarThree.book(10, 40); // 返回 2 ，第三个日程安排 [10, 40) 与第一个日程安排相交，所以最大 k 次预订是 2 次预订。
myCalendarThree.book(5, 15); // 返回 3 ，剩下的日程安排的最大 k 次预订是 3 次预订。
myCalendarThree.book(5, 10); // 返回 3
myCalendarThree.book(25, 55); // 返回 3
```

 

**提示：**

- `0 <= startTime < endTime <= 109`
- 每个测试用例，调用 `book` 函数最多不超过 `400`次



```python
from bisect import insort, bisect_left

class MyCalendarThree:

    def __init__(self):
        self.times = []  # 存储时间点及其增量的列表 [(time, delta)...]

    def book(self, start: int, end: int) -> int:
        # 使用二分插入以保持times列表有序
        insort(self.times, (start, 1))  # 开始时间，增量+1
        insort(self.times, (end, -1))   # 结束时间，增量-1
        
        maxBook = ans = 0
        for _, delta in self.times:
            maxBook += delta
            ans = max(ans, maxBook)
        
        return ans

if __name__ == "__main__":
    obj = MyCalendarThree()
    print(obj.book(10, 20))
    print(obj.book(50, 60))
    print(obj.book(10, 40))
    print(obj.book(5, 15))
    print(obj.book(5, 10))
    print(obj.book(25, 55))
    print(obj.book(15, 25))
```



```python

```



## 2403.杀死所有怪物的最短时间

28832:【附加题】《黑神话·悟空》，http://jsgl_liding.openjudge.cn/2024midtermtestv1/9/

https://doocs.github.io/leetcode/lc/2403/

你有一个整数数组 `power`，其中 `power[i]` 是第 `i` 个怪物的力量。

你从 `0` 点法力值开始，每天获取 `gain` 点法力值，最初 `gain` 等于 `1`。

每天，在获得 `gain` 点法力值后，如果你的法力值大于或等于怪物的力量，你就可以打败怪物。当你打败怪物时:

- 你的法力值会被重置为 `0`，并且
- `gain` 的值增加 `1`。

返回*打败所有怪物所需的 **最少** 天数。*

 

**示例 1:**

```
输入: power = [3,1,4]
输出: 4
解释: 打败所有怪物的最佳方法是:
- 第 1 天: 获得 1 点法力值，现在总共拥有 1 点法力值。用尽所有法力值击杀第 2 个怪物。
- 第 2 天: 获得 2 点法力值，现在总共拥有 2 点法力值。
- 第 3 天: 获得 2 点法力值，现在总共拥有 4 点法力值。用尽所有法力值击杀第 3 个怪物。
- 第 4 天: 获得 3 点法力值，现在总共拥有 3 点法力值。 用尽所有法力值击杀第 1 个怪物。
可以证明，4 天是最少需要的天数。
```

**示例 2:**

```
输入: power = [1,1,4]
输出: 4
解释: 打败所有怪物的最佳方法是:
- 第 1 天: 获得 1 点法力值，现在总共拥有 1 点法力值。用尽所有法力值击杀第 1 个怪物。
- 第 2 天: 获得 2 点法力值，现在总共拥有 2 点法力值。用尽所有法力值击杀第 2 个怪物。
- 第 3 天: 获得 3 点法力值，现在总共拥有 3 点法力值。
- 第 4 天: 获得 3 点法力值，现在总共拥有 6 点法力值。用尽所有法力值击杀第 3 个怪物。
可以证明，4 天是最少需要的天数。
```

**示例 3:**

```
输入: power = [1,2,4,9]
输出: 6
解释: 打败所有怪物的最佳方法是:
- 第 1 天: 获得 1 点法力值，现在总共拥有 1 点法力值。用尽所有法力值击杀第 1 个怪物
- 第 2 天: 获得 2 点法力值，现在总共拥有 2 点法力值。用尽所有法力值击杀第 2 个怪物。
- 第 3 天: 获得 3 点法力值，现在总共拥有 3 点法力值。
- 第 4 天: 获得 3 点法力值，现在总共拥有 6 点法力值。
- 第 5 天: 获得 3 点法力值，现在总共拥有 9 点法力值。用尽所有法力值击杀第 4 个怪物。
- 第 6 天: 获得 4 点法力值，现在总共拥有 4 点法力值。用尽所有法力值击杀第 3 个怪物。
可以证明，6 天是最少需要的天数。
```

 

**提示:**

- `1 <= power.length <= 17`
- `1 <= power[i] <= 109`



状态压缩 + 动态规划

定义 `f[mask]` 表示当前怪物的状态为*mask* 时，打败所有怪物所需的最少天数。其中 *mask* 是一个 *n* 位的二进制数，其中第 *i* 位为 1 表示第 *i* 个怪物已被击败，为 0 表示第 *i* 个怪物还活着。初始时 `f[0]=0`，其余 `f[mask]=+∞`。答案即为 $f[2^n−1]$。

我们在 $[1,2^n−1]$ 的范围内枚举 *mask*，对于每个 *mask*，我们枚举每个怪物 *i*，如果第 *i* 个怪物被击败，那么它可以从上一个状态 $mask⊕2^i$ 转移过来，转移的代价为 (power[i]+gain−1)/gain，其中 `gain=mask.bitCount()`。

最后，返回 $f[2^n−1]$。

时间复杂度 $O(2^n×n)$，空间复杂度 $O(2^n)$。其中 n 为怪物的数量。

```python
from typing import List

class Solution:
    def minimumTime(self, power: List[int]) -> int:
        n = len(power)
        max_mask = (1 << n)
        
        # dp[mask] 表示当前选择了哪些武器的最小时间
        dp = [float('inf')] * max_mask
        dp[0] = 0  # 初始状态，没有选择任何武器
        
        for mask in range(max_mask):
            selected_count = bin(mask).count('1')  # 已选择武器的数量
            gain = 1 + selected_count  # 当前增益值
            
            for i in range(n):
                if mask & (1 << i) == 0:  # 如果第 i 个武器未被选择
                    next_mask = mask | (1 << i)
                    dp[next_mask] = min(
                        dp[next_mask],
                        dp[mask] + (power[i] + gain - 1) // gain
                    )
        
        return dp[max_mask - 1]

if __name__ == '__main__':
    sol = Solution()
    pow = list(map(int, input().split()))
    print(sol.minimumTime(pow))
```





下面2个greedy方法，虽然能AC，但是在这个数据上会出错。

24-物院-吕金浩：发现如下数据，时间复杂度`O(2^n*n)的dp做法输出68630`，O(n^2)的greedy输出68631。（手在键盘上瞎划拉出的数据）。

要n<=19的话取后面19个数也行。对老师给的dp代码和我自己写的dp，邹同学、郑同学和我自己写的greedy都是这个结果

```
6641 41497 26416 66149 261498 716 616 5148 16416 1435 65 498 321 8682 234 54 82453 824653 465 456 8465
```



```
26416 66149 261498 716 616 5148 16416 1435 65 498 321 8682

dp 72482
greedy 72483
```



贪心做，这题就是要把题目里给的n个boss的力量值和1~n匹配，相除后向上取整并求和。让大的力量值尽可能去匹配大的除数，同时因为涉及到取整，可能有多个除数除出来会是一样的结果，为了避免浪费在商相同的情况下选取最小的那个除数，这样是能AC的，但是我在数学上暂时还给不出一个严格的证明。

```python
#24 物院 郑涵予

a = list(map(int, input().split()))
n = len(a)
a.sort(reverse=True)
b = [False] * n
sum = 0
for i in range(n):
    index = -1
    time = 1e10
    for j in range(n - 1, -1, -1):
        if b[j]:
            continue
        current_time = (a[i] + j) // (j + 1)
        if time == 1e10:
            time = current_time
            index = j
        elif current_time == time:
            index = j
        else:
            break
    b[index] = True
    sum += time
print(sum)
```



```python
#邹一鸣 2400011815
boss_power=sorted(list(map(int,input().split())))
pp=list(boss_power)
def findbest(l,gain):
    if len(l)==1:
        return l[0]//gain+int(bool(l[0]%gain))
    poss=[]
    for i in range(len(l)):
        if l[i]<=3*gain:
            a=l.pop(i)
            poss.append(a//gain+int(bool(a%gain))+findbest(l,gain+1))
            l.insert(i,a)
    if any(poss):
        return min(poss)
    return l[0]//gain+int(bool(l[0]%gain))+findbest(l[1:],gain+1)
a=0
for t in range(len(boss_power)):
    if boss_power[t]<=t+1:
        a+=1
        pp.remove(boss_power[t])
    else:
        a+=findbest(pp,t+1)
        break
print(a)
```





## 2931.购买物品的最大开销

greedy, https://leetcode.cn/problems/maximum-spending-after-buying-items/

给你一个下标从 **0** 开始大小为 `m * n` 的整数矩阵 `values` ，表示 `m` 个不同商店里 `m * n` 件不同的物品。每个商店有 `n` 件物品，第 `i` 个商店的第 `j` 件物品的价值为 `values[i][j]` 。除此以外，第 `i` 个商店的物品已经按照价值非递增排好序了，也就是说对于所有 `0 <= j < n - 1` 都有 `values[i][j] >= values[i][j + 1]` 。

每一天，你可以在一个商店里购买一件物品。具体来说，在第 `d` 天，你可以：

- 选择商店 `i` 。
- 购买数组中最右边的物品 `j` ，开销为 `values[i][j] * d` 。换句话说，选择该商店中还没购买过的物品中最大的下标 `j` ，并且花费 `values[i][j] * d` 去购买。

**注意**，所有物品都视为不同的物品。比方说如果你已经从商店 `1` 购买了物品 `0` ，你还可以在别的商店里购买其他商店的物品 `0` 。

请你返回购买所有 `m * n` 件物品需要的 **最大开销** 。

 

**示例 1：**

```
输入：values = [[8,5,2],[6,4,1],[9,7,3]]
输出：285
解释：第一天，从商店 1 购买物品 2 ，开销为 values[1][2] * 1 = 1 。
第二天，从商店 0 购买物品 2 ，开销为 values[0][2] * 2 = 4 。
第三天，从商店 2 购买物品 2 ，开销为 values[2][2] * 3 = 9 。
第四天，从商店 1 购买物品 1 ，开销为 values[1][1] * 4 = 16 。
第五天，从商店 0 购买物品 1 ，开销为 values[0][1] * 5 = 25 。
第六天，从商店 1 购买物品 0 ，开销为 values[1][0] * 6 = 36 。
第七天，从商店 2 购买物品 1 ，开销为 values[2][1] * 7 = 49 。
第八天，从商店 0 购买物品 0 ，开销为 values[0][0] * 8 = 64 。
第九天，从商店 2 购买物品 0 ，开销为 values[2][0] * 9 = 81 。
所以总开销为 285 。
285 是购买所有 m * n 件物品的最大总开销。
```

**示例 2：**

```
输入：values = [[10,8,6,4,2],[9,7,5,3,2]]
输出：386
解释：第一天，从商店 0 购买物品 4 ，开销为 values[0][4] * 1 = 2 。
第二天，从商店 1 购买物品 4 ，开销为 values[1][4] * 2 = 4 。
第三天，从商店 1 购买物品 3 ，开销为 values[1][3] * 3 = 9 。
第四天，从商店 0 购买物品 3 ，开销为 values[0][3] * 4 = 16 。
第五天，从商店 1 购买物品 2 ，开销为 values[1][2] * 5 = 25 。
第六天，从商店 0 购买物品 2 ，开销为 values[0][2] * 6 = 36 。
第七天，从商店 1 购买物品 1 ，开销为 values[1][1] * 7 = 49 。
第八天，从商店 0 购买物品 1 ，开销为 values[0][1] * 8 = 64 。
第九天，从商店 1 购买物品 0 ，开销为 values[1][0] * 9 = 81 。
第十天，从商店 0 购买物品 0 ，开销为 values[0][0] * 10 = 100 。
所以总开销为 386 。
386 是购买所有 m * n 件物品的最大总开销。
```

 

**提示：**

- `1 <= m == values.length <= 10`
- `1 <= n == values[i].length <= 104`
- `1 <= values[i][j] <= 106`
- `values[i]` 按照非递增顺序排序。



**问题的核心：**

1. 每天只能购买一个物品，每天的开销与天数成比例。
2. 最大化开销的关键是尽可能为最有价值的物品分配更大的天数。因此，应该将**最有价值的物品尽可能安排在靠后的天数**。

**正确的贪心策略：**

- 按照价值从高到低，将物品逐步分配给**靠后的天数**。
- 具体实现：将所有物品按价值排序，然后从最大到最小分配天数，从第 m×nm \times nm×n 天开始。

```python
from typing import List, Tuple
class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        m, n = len(values), len(values[0])
        items = []

        # 收集所有物品
        for i in range(m):
            for j in range(n):
                items.append(values[i][j])

        # 按价值从高到低排序
        items.sort(reverse=True)

        max_cost = 0
        total_days = len(items)

        # 分配天数，从第 total_days 天分配到第 1 天
        for day, value in enumerate(items, start=1):
            max_cost += value * (total_days - day + 1)

        return max_cost

if __name__ == "__main__":
        sol = Solution()
        values1 = [[8, 5, 2], [6, 4, 1], [9, 7, 3]]
        values2 = [[10, 8, 6, 4, 2], [9, 7, 5, 3, 2]]
        print(sol.maxSpending(values1))  # Output: 285
        print(sol.maxSpending(values2))  # Output: 386

```



## 3287.求出数组中最大序列值﻿﻿

枚举 + 01背包，https://leetcode.cn/problems/find-the-maximum-sequence-value-of-array/

给你一个整数数组 `nums` 和一个 **正** 整数 `k` 。

定义长度为 `2 * x` 的序列 `seq` 的 **值** 为：

- `(seq[0] OR seq[1] OR ... OR seq[x - 1]) XOR (seq[x] OR seq[x + 1] OR ... OR seq[2 * x - 1])`.

请你求出 `nums` 中所有长度为 `2 * k` 的 子序列的 **最大值** 。

⚠️子序列 是可以通过从另一个数组删除或不删除某些元素，但不更改其余元素的顺序得到的数组。

**示例 1：**

**输入：**nums = [2,6,7], k = 1

**输出：**5

**解释：**

子序列 `[2, 7]` 的值最大，为 `2 XOR 7 = 5` 。

**示例 2：**

**输入：**nums = [4,2,5,6,7], k = 2

**输出：**2

**解释：**

子序列 `[4, 5, 6, 7]` 的值最大，为 `(4 OR 5) XOR (6 OR 7) = 2` 。

 

**提示：**

- `2 <= nums.length <= 400`
- `1 <= nums[i] < 2^7`
- `1 <= k <= nums.length / 2`





LeetCode排名第4。【mipha, https://leetcode.cn/u/mipha-2022/ 】

更多题目模板总结，请参考 2023年度总结与题目分享﻿﻿，https://leetcode.cn/circle/discuss/1a9w0h/



思路，将题目分解成两部分：左侧|运算  ^  右侧|运算 

枚举左右侧两部分的分解线。看到**左右**侧就很容易联想到 dp ，题目要求的是子序列，那就是 选与不选 的问题，很容易就想到 01背包 

 `left[i][j] = h` 代表原数组 [0,i-1] 中子序列长度为 j 的 or 值集合 `h = set()` 。

$400∗400∗2^7=20,480,000$。1e7 不会超时捏。



```python
        # left[i][j] 到第i位 子序列长度为j的 or 值
        left = [ [set() for _ in range(k+1)]  for _ in range(n+1) ]
        # init
        left[0][0].add(0)

        for i in range(n):
            # 不选
            for lj in range(k+1):
                left[i+1][lj] = left[i][lj].copy()

            num = nums[i]
            # 选
            for lj in range(k):
                for lnum in left[i][lj]:
                    left[i+1][lj+1].add(lnum|num)

```

﻿

同理求右侧  right  时也是同样的方法，当然可以在枚举分界线过程中，滚动数组处理 right 。

```python
        # 右 滚动数组
        right = [set() for _ in range(k+1)]
        right[0].add(0)
        
        res = 0
        # 枚举分界线
        for i in range(n-1,-1,-1):
            # 不选
            tmp = deepcopy(right)
            
            num = nums[i]
            # 选
            for lj in range(k):
                for lnum in right[lj]:
                    tmp[lj+1].add(lnum|num) 

            right = tmp
            # 计算左右侧的异或值
            for a in left[i][k]:
                for b in right[k]:
                    c = a ^ b
                    if c > res:
                        res = c
```

﻿



```python
class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        '''
        res = 前半|运算 ^ 后半|运算

        子序列res最大值
        k 长度

        每个数的二进制只有7位 ※
        128
        '''
        n = len(nums)

        # 枚举分界线 + dp

        # left[i][j] 到第i位 子序列长度为j的 or 值
        left = [ [set() for _ in range(k+1)]  for _ in range(n+1) ]
        # init
        left[0][0].add(0)
        
        from copy import deepcopy 
        for i in range(n):
            # 不选
            left[i+1] = deepcopy(left[i])

            num = nums[i]
            # 选
            for lj in range(k):
                for lnum in left[i][lj]:
                    left[i+1][lj+1].add(lnum|num)
            
        
        # 右 滚动数组
        right = [set() for _ in range(k+1)]
        right[0].add(0)
        
        res = 0
        # 枚举分界线
        for i in range(n-1,-1,-1):
            # 不选
            tmp = deepcopy(right)
            
            num = nums[i]
            # 选
            for lj in range(k):
                for lnum in right[lj]:
                    tmp[lj+1].add(lnum|num) 

            right = tmp
            # 计算左右侧的异或值
            for a in left[i][k]:
                for b in right[k]:
                    c = a ^ b
                    if c > res:
                        res = c
        
        return res

```

﻿

> chatgpt.com解读并优化
>
> 这段代码的目的是求解通过分割数组并进行按位“或”操作后，子序列的最大异或值。它将问题分为左右两个部分，并利用动态规划（DP）存储每个子序列的“或”结果。具体的，代码利用了滚动数组技巧，降低空间复杂度，且通过枚举分界线来找到最优解。
>
> **代码分析与优化建议：**
>
> 1. **内存优化：**
>
> - 代码中使用了 `deepcopy` 来复制数组，然而 `deepcopy` 在内存上消耗较大且效率低下，特别是对于大数据量的情况。你可以考虑改用直接的复制方式（例如直接用切片 `[:]` 或手动复制）。
> - 对于 `left` 和 `right` 数组，`set` 用来存储中间结果是合适的，但是 `set` 会导致很多冗余的计算，特别是当子序列长度较大时，冗余计算会影响性能。
>
> 2. **代码结构与可读性：**
>
> - 注释部分提供了一些背景信息，但可以进一步简化说明，避免过多无关的信息。
> - 代码本身可以进行进一步优化，尤其是在 `deepcopy` 和状态更新部分。
>
> 3. **优化方向：**
>
> - **减少重复计算**： `left` 和 `right` 的状态空间可以进一步压缩。
> - **不需要深拷贝**：通过手动管理每个 DP 状态，可以避免使用 `deepcopy`，从而提高效率。
> - **按需更新`left`和`right`**：考虑仅更新必要的状态，减少不必要的计算。
>
> 优化后的代码：

```python
class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # dp数组存储每个子序列的or值
        left = [[set() for _ in range(k+1)] for _ in range(n+1)]
        right = [set() for _ in range(k+1)]

        # 初始化
        left[0][0].add(0)
        right[0].add(0)

        # 枚举从左到右的dp
        for i in range(n):
            # 不选当前数字
            for j in range(k+1):
                left[i+1][j] = left[i][j].copy()

            num = nums[i]
            # 选当前数字
            for j in range(k):
                for val in left[i][j]:
                    left[i+1][j+1].add(val | num)

        res = 0
        # 枚举从右到左的dp
        for i in range(n-1, -1, -1):
            # 不选当前数字
            tmp = [right[j].copy() for j in range(k+1)]
            num = nums[i]
            # 选当前数字
            for j in range(k):
                for val in right[j]:
                    tmp[j+1].add(val | num)

            right = tmp

            # 计算最大异或值
            for val_left in left[i][k]:
                for val_right in right[k]:
                    res = max(res, val_left ^ val_right)

        return res
```

> 主要优化点：
>
> 1. **去除 `deepcopy`**：直接通过复制 `set`（`copy()`）来避免深拷贝。
> 2. **代码结构简化**：直接使用 `set` 的 `copy()` 方法来更新状态数组，避免不必要的复杂度。
> 3. **`left` 和 `right` 的管理**：仅在需要时更新，减少了不必要的空间使用。
>
> 性能分析：
>
> - 时间复杂度：`O(n * k^2)`，其中 `n` 是数组长度，`k` 是子序列长度。因为我们每次更新状态数组时，会遍历当前所有的 `k` 长度子序列，并且每个状态需要 `k` 次检查。
> - 空间复杂度：`O(n * k)`，由于我们保存了 `n` 个位置和每个位置 `k` 长度的子序列的 `or` 值。
>
> 结论：
>
> 优化后的代码通过减少不必要的内存开销和避免深拷贝，提升了效率，并且保持了代码的可读性。如果需要处理更大规模的数据，可以进一步考虑压缩状态空间，或者使用其他优化技术（如位运算技巧）。



超时代码

```python
from typing import List
from itertools import combinations


class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_val = 0

        # 预先计算所有可能的 OR 结果
        or_results = {}
        for i in range(n):
            or_results[(i, i)] = nums[i]
            for j in range(i + 1, n):
                or_results[(i, j)] = or_results.get((i, j - 1), 0) | nums[j]

        # 枚举所有可能的长度为 2*k 的子序列
        for comb in combinations(range(n), 2 * k):
            left = comb[:k]
            right = comb[k:]

            # 计算前半部分和后半部分的 OR 值
            left_or = 0
            for i in left:
                left_or |= nums[i]

            right_or = 0
            for i in right:
                right_or |= nums[i]

            # 更新最大值
            max_val = max(max_val, left_or ^ right_or)

        return max_val


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxValue([2, 6, 7], 1))  # Expected Output: 5
    print(solution.maxValue([4, 2, 5, 6, 7], 2))  # Expected Output: 2
```





## 3298.统计重新排列后包含另一个字符串的子字符串数目II

给你两个字符串 `word1` 和 `word2` 。

如果一个字符串 `x` 重新排列后，`word2` 是重排字符串的 

前缀

 ，那么我们称字符串 `x` 是 **合法的** 。



请你返回 `word1` 中 **合法** 

子字符串

 的数目。



**注意** ，这个问题中的内存限制比其他题目要 **小** ，所以你 **必须** 实现一个线性复杂度的解法。

 

**示例 1：**

**输入：**word1 = "bcca", word2 = "abc"

**输出：**1

**解释：**

唯一合法的子字符串是 `"bcca"` ，可以重新排列得到 `"abcc"` ，`"abc"` 是它的前缀。

**示例 2：**

**输入：**word1 = "abcabc", word2 = "abc"

**输出：**10

**解释：**

除了长度为 1 和 2 的所有子字符串都是合法的。

**示例 3：**

**输入：**word1 = "abcabc", word2 = "aaabc"

**输出：**0

 

**解释：**

- `1 <= word1.length <= 106`
- `1 <= word2.length <= 104`
- `word1` 和 `word2` 都只包含小写英文字母。



```python
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        diff = [0] * 26
        for c in word2:
            diff[ord(c) - ord('a')] -= 1

        res = 0
        cnt = sum(1 for c in diff if c < 0)

        def update(c: int, add: int):
            nonlocal cnt
            diff[c] += add
            if add == 1 and diff[c] == 0:
                # 表明 diff[c] 由 -1 变为 0
                cnt -= 1
            elif add == -1 and diff[c] == -1:
                # 表明 diff[c] 由 0 变为 -1
                cnt += 1

        l, r = 0, 0
        while l < len(word1):
            while r < len(word1) and cnt > 0:
                update(ord(word1[r]) - ord('a'), 1)
                r += 1
            if cnt == 0:
                res += len(word1) - r + 1
            update(ord(word1[l]) - ord('a'), -1)
            l += 1

        return res
```





# 其他编程网站



## 1115. 取石子游戏

dfs, https://www.acwing.com/problem/content/description/1117/

有两堆石子，两个人轮流去取，每次取的时候，只能从较多的那堆石子里取，并且取的数目必须是较少的那堆石子数目的整数倍（不能不取）。

最后谁能够把一堆石子取空谁就算赢。

比如初始的时候两堆石子的数目是25和7

| 25 7 | →       | 11 7 | →       | 4 7  | →       | 4 3  | →       | 1 3  | →       | 1 0  |
| :--- | :------ | :--- | :------ | :--- | :------ | :--- | :------ | :--- | :------ | :--- |
|      | 选手1取 |      | 选手2取 |      | 选手1取 |      | 选手2取 |      | 选手1取 |      |

最后选手1（先取的）获胜，在取的过程中选手2都只有唯一的一种取法。

给定初始时石子的数目，如果两个人都采取最优策略，请问先手能否获胜。

**输入格式**

输入包含多数数据。每组数据一行，包含两个正整数 a 和 b，表示初始时石子的数目。

输入以两个0表示结束。

**输出格式**

如果先手胜，输出”win”，否则输出”lose”。

数据范围：1≤a,b≤10^9

输入样例：

```
34 12
15 24
0 0
```

输出样例：

```
win
lose
```

提示

假设石子数目为 (a,b) 且 a≥b，如果 [a/b]≥2 则先手必胜,如果 [a/b]<2，那么先手只有唯一的一种取法。

[a/b] 表示 a 除以 b 取整后的值。



按题目提示递归，函数返回值为布尔变量，取一次石子先后手交换，返回相反的结果。注意边界条件，如果有两堆一样的则“当前先手”胜。

```python
# 徐至晟 24光华管院
def f(x,y):
    if x<y:
        return f(y,x)
    if x>=y*2:
        return True
    elif x==y:
        return True
    else:
        return not f(x-y,y)

a,b=map(int,input().split())
while a:
    if f(a,b):
        print("win")
    else:
        print("lose")
    a,b=map(int,input().split())
```





思路：遍历先手取完后所有可能的结果，如果后手有必赢策略则lose，反之win

```python
# 彭凌越 24光华管理学院
dic = {}
def dfs(a,b):
    if (a,b) in dic:
        return dic[(a,b)]
    if a==0 or b==0:
        dic[(a,b)]=True
        return True
    if a<b:
        a,b = b,a
    if a%b==0:
        dic[(a,b)]=True
        return True
    for i in range(1,a//b+1):
            if not dfs(a-i*b,b):
                dic[(a,b)]=True
                return True
    dic[(a,b)]=False
    return False
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if dfs(a,b):
        print('win')
    else:
        print('lose')
```



```python
from functools import lru_cache
import sys
sys.setrecursionlimit(1<<30)

@lru_cache(maxsize=None)
def can_win(a, b):
    if a == 0 or b == 0:
        return False  # 如果有一堆石子为空，则先手输
    if a > b:
        for i in range(1, a // b + 1):
            if not can_win(a - b * i, b):
                return True
    else:
        for i in range(1, b // a + 1):
            if not can_win(a, b - a * i):
                return True
    return False

def main():
    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        if can_win(max(a, b), min(a, b)):
            print("win")
        else:
            print("lose")

if __name__ == "__main__":
    main()
```



## P1429 平面最近点对（加强版）

https://www.luogu.com.cn/problem/P1429

[P7883](/problem/P7883) 平面最近点对（加强加强版）

给定平面上 $n$ 个点，找出其中的一对点的距离，使得在这 $n$ 个点的所有点对中，该距离为所有点对中最小的

输入格式

第一行：$n$ ，保证 $2\le n\le 200000$ 。

接下来 $n$ 行：每行两个实数：$x\ y$ ，表示一个点的行坐标和列坐标，中间用一个空格隔开。

输出格式

仅一行，一个实数，表示最短距离，精确到小数点后面 $4$ 位。

样例 #1

样例输入 #1

```
3
1 1
1 2
2 2
```

样例输出 #1

```
1.0000
```

提示

数据保证 $0\le x,y\le 10^9$



参考 https://oi-wiki.org/ds/kdt/

```c++
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
using namespace std;
constexpr int MAXN = 200010;
int n, d[MAXN], lc[MAXN], rc[MAXN];
double ans = 2e18;

struct node {
  double x, y;
} s[MAXN];

double L[MAXN], R[MAXN], D[MAXN], U[MAXN];

double dist(int a, int b) {
  return (s[a].x - s[b].x) * (s[a].x - s[b].x) +
         (s[a].y - s[b].y) * (s[a].y - s[b].y);
}

bool cmp1(node a, node b) { return a.x < b.x; }

bool cmp2(node a, node b) { return a.y < b.y; }

void maintain(int x) {
  L[x] = R[x] = s[x].x;
  D[x] = U[x] = s[x].y;
  if (lc[x])
    L[x] = min(L[x], L[lc[x]]), R[x] = max(R[x], R[lc[x]]),
    D[x] = min(D[x], D[lc[x]]), U[x] = max(U[x], U[lc[x]]);
  if (rc[x])
    L[x] = min(L[x], L[rc[x]]), R[x] = max(R[x], R[rc[x]]),
    D[x] = min(D[x], D[rc[x]]), U[x] = max(U[x], U[rc[x]]);
}

int build(int l, int r) {
  if (l > r) return 0;
  if (l == r) {
    maintain(l);
    return l;
  }
  int mid = (l + r) >> 1;
  double avx = 0, avy = 0, vax = 0, vay = 0;  // average variance
  for (int i = l; i <= r; i++) avx += s[i].x, avy += s[i].y;
  avx /= (double)(r - l + 1);
  avy /= (double)(r - l + 1);
  for (int i = l; i <= r; i++)
    vax += (s[i].x - avx) * (s[i].x - avx),
        vay += (s[i].y - avy) * (s[i].y - avy);
  if (vax >= vay)
    d[mid] = 1, nth_element(s + l, s + mid, s + r + 1, cmp1);
  else
    d[mid] = 2, nth_element(s + l, s + mid, s + r + 1, cmp2);
  lc[mid] = build(l, mid - 1), rc[mid] = build(mid + 1, r);
  maintain(mid);
  return mid;
}

double f(int a, int b) {
  double ret = 0;
  if (L[b] > s[a].x) ret += (L[b] - s[a].x) * (L[b] - s[a].x);
  if (R[b] < s[a].x) ret += (s[a].x - R[b]) * (s[a].x - R[b]);
  if (D[b] > s[a].y) ret += (D[b] - s[a].y) * (D[b] - s[a].y);
  if (U[b] < s[a].y) ret += (s[a].y - U[b]) * (s[a].y - U[b]);
  return ret;
}

void query(int l, int r, int x) {
  if (l > r) return;
  int mid = (l + r) >> 1;
  if (mid != x) ans = min(ans, dist(x, mid));
  if (l == r) return;
  double distl = f(x, lc[mid]), distr = f(x, rc[mid]);
  if (distl < ans && distr < ans) {
    if (distl < distr) {
      query(l, mid - 1, x);
      if (distr < ans) query(mid + 1, r, x);
    } else {
      query(mid + 1, r, x);
      if (distl < ans) query(l, mid - 1, x);
    }
  } else {
    if (distl < ans) query(l, mid - 1, x);
    if (distr < ans) query(mid + 1, r, x);
  }
}

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);
  cin >> n;
  for (int i = 1; i <= n; i++) cin >> s[i].x >> s[i].y;
  build(1, n);
  for (int i = 1; i <= n; i++) query(1, n, i);
  cout << fixed << setprecision(4) << sqrt(ans) << '\n';
  return 0;
}
```



能AC前三个和最后一个数据。

但是能AC这个题目。 

## P1257 平面上的最接近点对

https://www.luogu.com.cn/problem/P1257

给定平面上 $n$ 个点，找出其中的一对点的距离，使得在这 $n$ 个点的所有点对中，该距离为所有点对中最小的。

**输入格式**

第一行一个整数 $n$，表示点的个数。

接下来 $n$ 行，每行两个整数 $x,y$ ，表示一个点的行坐标和列坐标。

**输出格式**

仅一行，一个实数，表示最短距离，四舍五入保留 $4$ 位小数。

样例 #1

样例输入 #1

```
3
1 1
1 2
2 2
```

样例输出 #1

```
1.0000
```

提示

数据规模与约定

对于 $100\%$ 的数据，保证 $1 \leq n \leq 10^4$，$0 \leq x, y \leq 10^9$。



```python
import math
from functools import cmp_to_key
import sys
sys.setrecursionlimit(1000000)

MAXN = 200010
INF = float("inf")

class Node:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

class KDTree:
    def __init__(self):
        self.n = 0
        self.s = [Node() for _ in range(MAXN)]  # 点集
        self.lc = [0] * MAXN  # 左子树
        self.rc = [0] * MAXN  # 右子树
        self.d = [0] * MAXN   # 划分维度
        self.L = [0.0] * MAXN
        self.R = [0.0] * MAXN
        self.D = [0.0] * MAXN
        self.U = [0.0] * MAXN
        self.ans = INF

    def dist(self, a, b):
        """计算两点之间的欧几里得距离平方"""
        return (self.s[a].x - self.s[b].x) ** 2 + (self.s[a].y - self.s[b].y) ** 2

    def maintain(self, x):
        """维护边界矩形"""
        self.L[x] = self.R[x] = self.s[x].x
        self.D[x] = self.U[x] = self.s[x].y
        if self.lc[x]:
            lc = self.lc[x]
            self.L[x] = min(self.L[x], self.L[lc])
            self.R[x] = max(self.R[x], self.R[lc])
            self.D[x] = min(self.D[x], self.D[lc])
            self.U[x] = max(self.U[x], self.U[lc])
        if self.rc[x]:
            rc = self.rc[x]
            self.L[x] = min(self.L[x], self.L[rc])
            self.R[x] = max(self.R[x], self.R[rc])
            self.D[x] = min(self.D[x], self.D[rc])
            self.U[x] = max(self.U[x], self.U[rc])

    def cmp1(self, a, b):
        return -1 if a.x < b.x else (1 if a.x > b.x else 0)

    def cmp2(self, a, b):
        return -1 if a.y < b.y else (1 if a.y > b.y else 0)

    def build(self, l, r):
        """构建 KD 树"""
        if l > r:
            return 0
        if l == r:
            self.maintain(l)
            return l

        mid = (l + r) >> 1
        avx = avy = vax = vay = 0.0  # 平均值与方差
        for i in range(l, r + 1):
            avx += self.s[i].x
            avy += self.s[i].y
        avx /= (r - l + 1)
        avy /= (r - l + 1)
        for i in range(l, r + 1):
            vax += (self.s[i].x - avx) ** 2
            vay += (self.s[i].y - avy) ** 2

        if vax >= vay:
            self.d[mid] = 1
            self.s[l:r + 1] = sorted(self.s[l:r + 1], key=cmp_to_key(self.cmp1))
        else:
            self.d[mid] = 2
            self.s[l:r + 1] = sorted(self.s[l:r + 1], key=cmp_to_key(self.cmp2))

        self.lc[mid] = self.build(l, mid - 1)
        self.rc[mid] = self.build(mid + 1, r)
        self.maintain(mid)
        return mid

    def f(self, a, b):
        """计算点 a 到矩形 b 的最短距离"""
        ret = 0
        if self.L[b] > self.s[a].x:
            ret += (self.L[b] - self.s[a].x) ** 2
        if self.R[b] < self.s[a].x:
            ret += (self.s[a].x - self.R[b]) ** 2
        if self.D[b] > self.s[a].y:
            ret += (self.D[b] - self.s[a].y) ** 2
        if self.U[b] < self.s[a].y:
            ret += (self.s[a].y - self.U[b]) ** 2
        return ret

    def query(self, l, r, x):
        """查询点 x 的最近邻点"""
        if l > r:
            return
        mid = (l + r) >> 1
        if mid != x:
            self.ans = min(self.ans, self.dist(x, mid))
        if l == r:
            return

        dist_l = self.f(x, self.lc[mid]) if self.lc[mid] else INF
        dist_r = self.f(x, self.rc[mid]) if self.rc[mid] else INF

        if dist_l < dist_r:
            if dist_l < self.ans:
                self.query(l, mid - 1, x)
            if dist_r < self.ans:
                self.query(mid + 1, r, x)
        else:
            if dist_r < self.ans:
                self.query(mid + 1, r, x)
            if dist_l < self.ans:
                self.query(l, mid - 1, x)

    def solve(self):
        """主函数逻辑"""
        root = self.build(1, self.n)
        for i in range(1, self.n + 1):
            self.query(1, self.n, i)
        return math.sqrt(self.ans)

# 示例用法
if __name__ == "__main__":
    kd_tree = KDTree()
    kd_tree.n = int(input())
    for i in range(1, kd_tree.n + 1):
        x, y = map(float, input().split())
        kd_tree.s[i] = Node(x, y)

    result = kd_tree.solve()
    print(f"{result:.4f}")

```





## P4390 [BalkanOI2007] Mokia 摩基亚

https://www.luogu.com.cn/problem/P4390

摩尔瓦多的移动电话公司摩基亚（Mokia）设计出了一种新的用户定位系统。和其他的定位系统一样，它能够迅速回答任何形如 “用户 C 的位置在哪？” 的问题，精确到毫米。但其真正高科技之处在于，它能够回答形如 “给定区域内有多少名用户？” 的问题。

在定位系统中，世界被认为是一个 $w\times w$ 的正方形区域，由 $1\times 1$ 的方格组成。每个方格都有一个坐标 $(x, y)$，$1\leq x,y\leq w$。坐标的编号从 $1$ 开始。对于一个 $4\times 4$ 的正方形，就有 $1\leq x\leq 4$，$1\leq y\leq 4$（如图）：

![](https://cdn.luogu.com.cn/upload/pic/17271.png)

请帮助 Mokia 公司编写一个程序来计算在某个矩形区域内有多少名用户。

**输入格式**

有三种命令，意义如下：

| 命令 |         参数         |                             意义                             |
| :--: | :------------------: | :----------------------------------------------------------: |
| $0$  |         $w$          |         初始化一个全零矩阵。本命令仅开始时出现一次。         |
| $1$  |      $x\ y\ a$       |      向方格 $(x, y)$ 中添加 $a$ 个用户。$a$ 是正整数。       |
| $2$  | $x_1\ y_1\ x_2\ y_2$ | 查询 $x_1\leq x\leq x_2$，$y_1\leq y\leq y_2$ 所规定的矩形中的用户数量。 |
| $3$  |        无参数        |              结束程序。本命令仅结束时出现一次。              |

输入共若干行，每行有若干个整数，表示一个命令。

**输出格式**

对所有命令 $2$，输出一个一行整数，即当前询问矩形内的用户数量。

**样例 #1**

**样例输入 #1**

```
0 4
1 2 3 3
2 1 1 3 3
1 2 2 2
2 2 2 3 4
3
```

**样例输出 #1**

```
3
5
```

**提示**

**数据规模与约定**


对于 $100\%$ 的数据，保证：

- $1\leq w\leq 2\times 10 ^ 6$。
- $1\leq x_1\leq x_2\leq w$，$1\leq y_1\leq y_2\leq w$，$1\leq x,y\leq w$，$0<a\leq 10000$。
- 命令 $1$ 不超过 $160000$ 个。
- 命令 $2$ 不超过 $10000$ 个。





KD树超时，能AC前两个数据。

```python
class KDTree:
    def __init__(self):
        self.nodes = []
        self.root = None

    class Node:
        def __init__(self, x, y, a):
            self.x = x
            self.y = y
            self.a = a
            self.left = None
            self.right = None
            self.dim = 0  # 分割维度：0 表示 x，1 表示 y

    def build(self, points, depth=0):
        if not points:
            return None
        k = depth % 2  # 当前分割维度
        points.sort(key=lambda p: (p[0], p[1]) if k == 0 else (p[1], p[0]))
        mid = len(points) // 2
        node = self.Node(*points[mid])
        node.dim = k
        node.left = self.build(points[:mid], depth + 1)
        node.right = self.build(points[mid + 1:], depth + 1)
        return node

    def insert(self, root, x, y, a, depth=0):
        if not root:
            return self.Node(x, y, a)
        k = depth % 2
        if (x < root.x if k == 0 else y < root.y):
            root.left = self.insert(root.left, x, y, a, depth + 1)
        else:
            root.right = self.insert(root.right, x, y, a, depth + 1)
        return root

    def query(self, root, x1, y1, x2, y2, depth=0):
        if not root:
            return 0
        k = depth % 2
        if x1 <= root.x <= x2 and y1 <= root.y <= y2:
            res = root.a
        else:
            res = 0
        if k == 0:
            if x1 <= root.x:
                res += self.query(root.left, x1, y1, x2, y2, depth + 1)
            if x2 >= root.x:
                res += self.query(root.right, x1, y1, x2, y2, depth + 1)
        else:
            if y1 <= root.y:
                res += self.query(root.left, x1, y1, x2, y2, depth + 1)
            if y2 >= root.y:
                res += self.query(root.right, x1, y1, x2, y2, depth + 1)
        return res

    def add_point(self, x, y, a):
        self.root = self.insert(self.root, x, y, a)

    def range_query(self, x1, y1, x2, y2):
        return self.query(self.root, x1, y1, x2, y2)


# 主程序
import sys
input = sys.stdin.read
data = input().splitlines()

kdtree = KDTree()

for line in data:
    cmd = list(map(int, line.split()))
    if cmd[0] == 0:
        w = cmd[1]  # 初始化宽度，但不需要存储实际矩阵
        continue
    elif cmd[0] == 1:
        x, y, a = cmd[1:]
        kdtree.add_point(x, y, a)
    elif cmd[0] == 2:
        x1, y1, x2, y2 = cmd[1:]
        print(kdtree.range_query(x1, y1, x2, y2))
    elif cmd[0] == 3:
        break

```



二维树状数组（Fenwick Tree / BIT）或者二维线段树。能AC第一个数据，其他数据超内存。

```python
import sys

input = sys.stdin.read
data = input().splitlines()

class FenwickTree2D:
    def __init__(self, size):
        self.size = size
        self.tree = [[0] * (size + 1) for _ in range(size + 1)]

    def update(self, x, y, delta):
        while x <= self.size:
            ny = y
            while ny <= self.size:
                self.tree[x][ny] += delta
                ny += ny & -ny
            x += x & -x

    def query(self, x, y):
        sum = 0
        while x > 0:
            ny = y
            while ny > 0:
                sum += self.tree[x][ny]
                ny -= ny & -ny
            x -= x & -x
        return sum

    def range_query(self, x1, y1, x2, y2):
        return (self.query(x2, y2) - self.query(x2, y1 - 1) -
                self.query(x1 - 1, y2) + self.query(x1 - 1, y1 - 1))

def process_commands(data):
    w = 0
    fenwick_tree = None
    for line in data:
        cmd = list(map(int, line.split()))
        if cmd[0] == 0:
            w = cmd[1]
            fenwick_tree = FenwickTree2D(w)
        elif cmd[0] == 1:
            x, y, a = cmd[1:]
            fenwick_tree.update(x, y, a)
        elif cmd[0] == 2:
            x1, y1, x2, y2 = cmd[1:]
            print(fenwick_tree.range_query(x1, y1, x2, y2))
        elif cmd[0] == 3:
            break

process_commands(data)
```





```python

```







```python

```

