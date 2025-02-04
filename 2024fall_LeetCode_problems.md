# Problems in leetcode.cn

Updated 1036 GMT+8 Feb 4 2025

2024 fall, Complied by Hongfei Yan



> Logs:
>
> 2025/1/27, 力扣题目难度分数，https://zerotrac.github.io/leetcode_problem_rating/#/
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

<img src="https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg" alt="img" style="zoom:67%;" />

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



## 26.删除有序数组中的重复项

two pointers, https://leetcode.cn/problems/remove-duplicates-from-sorted-array/

给你一个 **非严格递增排列** 的数组 `nums` ，请你**[ 原地](http://baike.baidu.com/item/原地算法)** 删除重复出现的元素，使每个元素 **只出现一次**，返回删除后数组的新长度。元素的 **相对顺序** 应该保持 **一致** 。然后返回 `nums` 中唯一元素的个数。

考虑 `nums` 的唯一元素的数量为 `k` ，你需要做以下事情确保你的题解可以被通过：

- 更改数组 `nums` ，使 `nums` 的前 `k` 个元素包含唯一元素，并按照它们最初在 `nums` 中出现的顺序排列。`nums` 的其余元素与 `nums` 的大小不重要。
- 返回 `k` 。

**判题标准:**

系统会用下面的代码来测试你的题解:

```
int[] nums = [...]; // 输入数组
int[] expectedNums = [...]; // 长度正确的期望答案

int k = removeDuplicates(nums); // 调用

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

如果所有断言都通过，那么您的题解将被 **通过**。

 

**示例 1：**

```
输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
```

**示例 2：**

```
输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
```

 

**提示：**

- `1 <= nums.length <= 3 * 10^4`
- `-104 <= nums[i] <= 10^4`
- `nums` 已按 **非严格递增** 排列





```python
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        # left指针指向下一个不同元素应该放置的位置
        left = 0
        
        # right指针用于遍历整个数组
        for right in range(1, len(nums)):
            # 如果找到了一个与当前left指向的元素不同的元素
            if nums[right] != nums[left]:
                # 移动left指针并将新值赋予该位置
                left += 1
                nums[left] = nums[right]
        
        # 返回的是数组中唯一元素的个数，也就是left指针位置+1
        return left + 1
```





## 27.移除元素

two pointers, https://leetcode.cn/problems/remove-element/

给你一个数组 `nums` 和一个值 `val`，你需要 **[原地](https://baike.baidu.com/item/原地算法)** 移除所有数值等于 `val` 的元素。元素的顺序可能发生改变。然后返回 `nums` 中与 `val` 不同的元素的数量。

假设 `nums` 中不等于 `val` 的元素数量为 `k`，要通过此题，您需要执行以下操作：

- 更改 `nums` 数组，使 `nums` 的前 `k` 个元素包含不等于 `val` 的元素。`nums` 的其余元素和 `nums`的大小并不重要。
- 返回 `k`。

**用户评测：**

评测机将使用以下代码测试您的解决方案：

```
int[] nums = [...]; // 输入数组
int val = ...; // 要移除的值
int[] expectedNums = [...]; // 长度正确的预期答案。
                            // 它以不等于 val 的值排序。

int k = removeElement(nums, val); // 调用你的实现

assert k == expectedNums.length;
sort(nums, 0, k); // 排序 nums 的前 k 个元素
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
```

如果所有的断言都通过，你的解决方案将会 **通过**。

 

**示例 1：**

```
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2,_,_]
解释：你的函数函数应该返回 k = 2, 并且 nums 中的前两个元素均为 2。
你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。
```

**示例 2：**

```
输入：nums = [0,1,2,2,3,0,4,2], val = 2
输出：5, nums = [0,1,4,0,3,_,_,_]
解释：你的函数应该返回 k = 5，并且 nums 中的前五个元素为 0,0,1,3,4。
注意这五个元素可以任意顺序返回。
你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。
```

 

**提示：**

- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`



```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        while left <= right:
            if nums[right] == val:
                n -= 1
                right -= 1
                continue
            if nums[left] == val:
                nums[left] = nums[right]
                n -= 1
                right -= 1
            else:
                left += 1

        return n
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



## 88.合并两个有序数组

two pointers, https://leetcode.cn/problems/merge-sorted-array/

给你两个按 **非递减顺序** 排列的整数数组 `nums1` 和 `nums2`，另有两个整数 `m` 和 `n` ，分别表示 `nums1` 和 `nums2` 中的元素数目。

请你 **合并** `nums2` 到 `nums1` 中，使合并后的数组同样按 **非递减顺序** 排列。

**注意：**最终，合并后数组不应由函数返回，而是存储在数组 `nums1` 中。为了应对这种情况，`nums1`的初始长度为 `m + n`，其中前 `m` 个元素表示应合并的元素，后 `n` 个元素为 `0` ，应忽略。`nums2` 的长度为 `n` 。

 

**示例 1：**

```
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
```

**示例 2：**

```
输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并 [1] 和 [] 。
合并结果是 [1] 。
```

**示例 3：**

```
输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。
```

 

**提示：**

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-109 <= nums1[i], nums2[j] <= 109`

 

**进阶：**你可以设计实现一个时间复杂度为 `O(m + n)` 的算法解决此问题吗？



```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
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



## 100.相同的树

https://leetcode.cn/problems/same-tree/

给你两棵二叉树的根节点 `p` 和 `q` ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

 

**示例 1：**

<img src="https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg" alt="img" style="zoom:67%;" />

```
输入：p = [1,2,3], q = [1,2,3]
输出：true
```

**示例 2：**

<img src="https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg" alt="img" style="zoom:67%;" />

```
输入：p = [1,2], q = [1,null,2]
输出：false
```

**示例 3：**

<img src="https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg" alt="img" style="zoom:67%;" />

```
输入：p = [1,2,1], q = [1,1,2]
输出：false
```

 

**提示：**

- 两棵树上的节点数目都在范围 `[0, 100]` 内
- `-10^4 <= Node.val <= 10^4`



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

```





## 101.对称二叉树

https://leetcode.cn/problems/symmetric-tree/

给你一个二叉树的根节点 `root` ， 检查它是否轴对称。

 

**示例 1：**

<img src="https://pic.leetcode.cn/1698026966-JDYPDU-image.png" alt="img" style="zoom:67%;" />

```
输入：root = [1,2,2,3,4,4,3]
输出：true
```

**示例 2：**

<img src="https://pic.leetcode.cn/1698027008-nPFLbM-image.png" alt="img" style="zoom:67%;" />

```
输入：root = [1,2,2,null,3,null,3]
输出：false
```

 

**提示：**

- 树中节点数目在范围 `[1, 1000]` 内
- `-100 <= Node.val <= 100`



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isMirror(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)

        return isMirror(root.left, root.right)
```



## 104.二叉树的最大深度

https://leetcode.cn/problems/maximum-depth-of-binary-tree/

给定一个二叉树 `root` ，返回其最大深度。

二叉树的 **最大深度** 是指从根节点到最远叶子节点的最长路径上的节点数。

 

**示例 1：**

<img src="https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg" alt="img" style="zoom:50%;" />

 

```
输入：root = [3,9,20,null,null,15,7]
输出：3
```

**示例 2：**

```
输入：root = [1,null,2]
输出：2
```

 

**提示：**

- 树中节点的数量在 `[0, 104]` 区间内。
- `-100 <= Node.val <= 100`



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def tree_depth(node):
            if node is None:
                return 0
            left_depth = tree_depth(node.left)
            right_depth = tree_depth(node.right)
            return max(left_depth, right_depth) + 1
        
        return tree_depth(root)
```



## 108.将有序数组转换为二叉搜索树

https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/

给你一个整数数组 `nums` ，其中元素已经按 **升序** 排列，请你将其转换为一棵 平衡二叉搜索树。

平衡二叉树是指该树所有节点的左右子树的高度相差不超过1. 

**示例 1：**

<img src="https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg" alt="img" style="zoom: 67%;" />

```
输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
```

**示例 2：**

<img src="https://assets.leetcode.com/uploads/2021/02/18/btree.jpg" alt="img" style="zoom:67%;" />

```
输入：nums = [1,3]
输出：[3,1]
解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。
```

 

**提示：**

- `1 <= nums.length <= 104`
- `-104 <= nums[i] <= 104`
- `nums` 按 **严格递增** 顺序排列



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid +1:])
        
        return root
```



## 112.路径总和

https://leetcode.cn/problems/path-sum/

给你二叉树的根节点 `root` 和一个表示目标和的整数 `targetSum` 。判断该树中是否存在 **根节点到叶子节点**的路径，这条路径上所有节点值相加等于目标和 `targetSum` 。如果存在，返回 `true` ；否则，返回 `false`。

**叶子节点** 是指没有子节点的节点。

 

**示例 1：**

<img src="https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg" alt="img" style="zoom:67%;" />

```
输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
解释：等于目标和的根节点到叶节点路径如上图所示。
```

**示例 2：**

<img src="https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg" alt="img" style="zoom:67%;" />

```
输入：root = [1,2,3], targetSum = 5
输出：false
解释：树中存在两条根节点到叶子节点的路径：
(1 --> 2): 和为 3
(1 --> 3): 和为 4
不存在 sum = 5 的根节点到叶子节点的路径。
```

**示例 3：**

```
输入：root = [], targetSum = 0
输出：false
解释：由于树是空的，所以不存在根节点到叶子节点的路径。
```

 

**提示：**

- 树中节点的数目在范围 `[0, 5000]` 内
- `-1000 <= Node.val <= 1000`
- `-1000 <= targetSum <= 1000`



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 如果树为空，直接返回False
        if not root:
            return False
        
        # 递归函数定义
        def dfs(node, current_sum):
            # 更新当前路径的和
            current_sum += node.val
            
            # 如果到达叶子节点，检查路径和是否等于目标值
            if not node.left and not node.right:
                return current_sum == targetSum
            
            # 递归遍历左右子树，并且只需要找到一条满足条件的路径即可
            left = dfs(node.left, current_sum) if node.left else False
            right = dfs(node.right, current_sum) if node.right else False
            
            # 返回左子树或右子树中任一路径满足条件的结果
            return left or right
        
        # 调用dfs函数开始搜索
        return dfs(root, 0)
        


        
```



## 118.杨辉三角

dp, https://leetcode.cn/problems/pascals-triangle/

给定一个非负整数 *`numRows`，*生成「杨辉三角」的前 *`numRows`* 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

<img src="https://pic.leetcode-cn.com/1626927345-DZmfxB-PascalTriangleAnimated2.gif" alt="img" style="zoom:67%;" />

 

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



## 119.杨辉三角II

滚动数组，https://leetcode.cn/problems/pascals-triangle-ii/

给定一个非负索引 `rowIndex`，返回「杨辉三角」的第 `rowIndex` 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

<img src="https://pic.leetcode-cn.com/1626927345-DZmfxB-PascalTriangleAnimated2.gif" alt="img" style="zoom:67%;" />

 

**示例 1:**

```
输入: rowIndex = 3
输出: [1,3,3,1]
```

**示例 2:**

```
输入: rowIndex = 0
输出: [1]
```

**示例 3:**

```
输入: rowIndex = 1
输出: [1,1]
```

 

**提示:**

- `0 <= rowIndex <= 33`

 

**进阶：**

你可以优化你的算法到 `*O*(*rowIndex*)` 空间复杂度吗？





滚动数组都是 `简单` 题了？https://leetcode.cn/problems/pascals-triangle-ii/

滚动数组不易理解，可以 https://pythontutor.com/ 看可视化执行过程。

杨辉三角形需要前一行的数据来计算当前行的数据，利用一个一维数组（即滚动数组）来保存这些数据，并随着行数的增加不断更新这个数组。

`dp`数组实际上代表了当前行。从当前行的末尾开始向前遍历并更新`dp`数组中的元素。这样做的好处是不会覆盖掉计算新值所需的旧值，从而确保了算法的正确性，同时节省了额外的存储空间。

```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1] * (rowIndex + 1)
        for row in range(1, rowIndex + 1):
            for i in range(row - 1, 0, -1):
                dp[i] = dp[i - 1] + dp[i]

        return dp
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

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png" alt="img" style="zoom:67%;" />

```
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
```

**示例 2：**

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png" alt="img" style="zoom:67%;" />

```
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
```

**示例 3：**

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png" alt="img" style="zoom:67%;" />

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

[<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_statement.png" alt="img" style="zoom:67%;" />](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_statement.png)

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

[<img src="https://assets.leetcode.com/uploads/2021/03/05/160_example_1_1.png" alt="img" style="zoom:67%;" />](https://assets.leetcode.com/uploads/2018/12/13/160_example_1.png)

```
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,6,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
— 请注意相交节点的值不为 1，因为在链表 A 和链表 B 之中值为 1 的节点 (A 中第二个节点和 B 中第三个节点) 是不同的节点。换句话说，它们在内存中指向两个不同的位置，而链表 A 和链表 B 中值为 8 的节点 (A 中第三个节点，B 中第四个节点) 在内存中指向相同的位置。
```

 

**示例 2：**

[<img src="https://assets.leetcode.com/uploads/2021/03/05/160_example_2.png" alt="img" style="zoom:67%;" />](https://assets.leetcode.com/uploads/2018/12/13/160_example_2.png)

```
输入：intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Intersected at '2'
解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [1,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
```

**示例 3：**

[<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_example_3.png" alt="img" style="zoom:67%;" />](https://assets.leetcode.com/uploads/2018/12/13/160_example_3.png)

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

<img src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg" alt="img" style="zoom:67%;" />

```
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
```

**示例 2：**

<img src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg" alt="img" style="zoom:67%;" />

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



## 219.存在重复元素II

https://leetcode.cn/problems/contains-duplicate-ii/

给你一个整数数组 `nums` 和一个整数 `k` ，判断数组中是否存在两个 **不同的索引** `i` 和 `j` ，满足 `nums[i] == nums[j]` 且 `abs(i - j) <= k` 。如果存在，返回 `true` ；否则，返回 `false` 。

**示例 1：**

```
输入：nums = [1,2,3,1], k = 3
输出：true
```

**示例 2：**

```
输入：nums = [1,0,1,1], k = 1
输出：true
```

**示例 3：**

```
输入：nums = [1,2,3,1,2,3], k = 2
输出：false
```

 

**提示：**

- `1 <= nums.length <= 105`
- `-109 <= nums[i] <= 109`
- `0 <= k <= 105`



```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        d = dict()
        for i in range(n):
            if nums[i] in d and abs(i - d[nums[i]]) <= k:
                    return True
            d[nums[i]] = i
        
        return False
```





## 226.翻转二叉树

https://leetcode.cn/problems/invert-binary-tree/

给你一棵二叉树的根节点 `root` ，翻转这棵二叉树，并返回其根节点。

 

**示例 1：**

<img src="https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg" alt="img" style="zoom:50%;" />

```
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
```

**示例 2：**

<img src="https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg" alt="img" style="zoom:50%;" />

```
输入：root = [2,1,3]
输出：[2,3,1]
```

**示例 3：**

```
输入：root = []
输出：[]
```

 

**提示：**

- 树中节点数目范围在 `[0, 100]` 内
- `-100 <= Node.val <= 100`



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root
```



## 234.回文链表

linked-list, https://leetcode.cn/problems/palindrome-linked-list/

给你一个单链表的头节点 `head` ，请你判断该链表是否为

回文链表（**回文** 序列是向前和向后读都相同的序列。如果是，返回 `true` ；否则，返回 `false` 。



 

**示例 1：**

<img src="https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg" alt="img" style="zoom:67%;" />

```
输入：head = [1,2,2,1]
输出：true
```

**示例 2：**

<img src="https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg" alt="img" style="zoom:67%;" />

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





## 283.移动零

https://leetcode.cn/problems/move-zeroes/

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



## 350.两个数组的交集II

双指针，哈希表，https://leetcode.cn/problems/intersection-of-two-arrays-ii/

给你两个整数数组 `nums1` 和 `nums2` ，请你以数组形式返回两数组的交集。返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。

 

**示例 1：**

```
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
```

**示例 2:**

```
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
```

 

**提示：**

- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`

 

**进阶：**

- 如果给定的数组已经排好序呢？你将如何优化你的算法？
- 如果 `nums1` 的大小比 `nums2` 小，哪种方法更优？
- 如果 `nums2` 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？



If the given arrays are already sorted, you can use a two-pointer technique to find the intersection. This approach is efficient and has a time complexity of O(n + m), where n and m are the lengths of the two arrays.

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1); n2 = len(nums2)
        nums1.sort(); nums2.sort()
        i = j = 0
        res = []
        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1; j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
        
        return res
```



如果 `nums2` 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

```python
from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Count the occurrences of each element in both arrays
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        # Find the intersection by taking the minimum count for each common element
        intersection = []
        for num in count1:
            if num in count2:
                intersection.extend([num] * min(count1[num], count2[num]))
        
        return intersection

# Example usage:
if __name__ == '__main__':
    solution = Solution()
    print(solution.intersect([1, 2, 2, 1], [2, 2]))  # Output: [2, 2]
    print(solution.intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # Output: [4, 9]
```



~~~python
If `nums2` is stored on disk and memory is limited, you can use a strategy that processes `nums2` in chunks. Here is a step-by-step approach:

1. **Count Elements in `nums1`**: Use a `Counter` to count the occurrences of each element in `nums1`.
2. **Process `nums2` in Chunks**: Read `nums2` in chunks, count the occurrences of each element in the current chunk, and update the intersection result accordingly.

Here is the Python code to achieve this:

```python
from collections import Counter
from typing import List, Iterator

class Solution:
    def intersect(self, nums1: List[int], nums2_iterator: Iterator[int], chunk_size: int) -> List[int]:
        # Count the occurrences of each element in nums1
        count1 = Counter(nums1)
        intersection = []

        # Process nums2 in chunks
        while True:
            chunk = list(next(nums2_iterator, None) for _ in range(chunk_size))
            if not chunk or chunk[0] is None:
                break
            count2 = Counter(chunk)
            for num in count1:
                if num in count2:
                    intersection.extend([num] * min(count1[num], count2[num]))

        return intersection

# Example usage:
if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    chunk_size = 2  # Define the chunk size based on available memory
    nums2_iterator = iter(nums2)  # Create an iterator for nums2
    solution = Solution()
    print(solution.intersect(nums1, nums2_iterator, chunk_size))  # Output: [2, 2]
```

### Explanation:
1. **Counter**: Count the occurrences of each element in `nums1`.
2. **Chunk Processing**: Read `nums2` in chunks using an iterator and process each chunk separately.
3. **Intersection**: For each chunk, count the occurrences of elements and update the intersection result by taking the minimum count for each common element.
~~~





## 543.二叉树的直径

https://leetcode.cn/problems/diameter-of-binary-tree/

给你一棵二叉树的根节点，返回该树的 **直径** 。

二叉树的 **直径** 是指树中任意两个节点之间最长路径的 **长度** 。这条路径可能经过也可能不经过根节点 `root` 。

两节点之间路径的 **长度** 由它们之间边数表示。

 

**示例 1：**

<img src="https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg" alt="img" style="zoom:67%;" />

```
输入：root = [1,2,3,4,5]
输出：3
解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。
```

**示例 2：**

```
输入：root = [1,2]
输出：1
```

 

**提示：**

- 树中节点数目在范围 `[1, 104]` 内
- `-100 <= Node.val <= 100`



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def depth(node: TreeNode) -> int:
            if not node:
                return 0
            ldepth = depth(node.left)
            rdepth = depth(node.right)
            self.diameter = max(self.diameter, ldepth + rdepth)
            return 1 + max(ldepth, rdepth)

        depth(root)
        return self.diameter
```



## 598.区间加法II

https://leetcode.cn/problems/range-addition-ii/

给你一个 `m x n` 的矩阵 `M` 和一个操作数组 `op` 。矩阵初始化时所有的单元格都为 `0` 。`ops[i] = [ai, bi]`意味着当所有的 `0 <= x < ai` 和 `0 <= y < bi` 时， `M[x][y]` 应该加 1。

在 *执行完所有操作后* ，计算并返回 *矩阵中最大整数的个数* 。

 

**示例 1:**

<img src="https://assets.leetcode.com/uploads/2020/10/02/ex1.jpg" alt="img" style="zoom: 50%;" />

```
输入: m = 3, n = 3，ops = [[2,2],[3,3]]
输出: 4
解释: M 中最大的整数是 2, 而且 M 中有4个值为2的元素。因此返回 4。
```

**示例 2:**

```
输入: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
输出: 4
```

**示例 3:**

```
输入: m = 3, n = 3, ops = []
输出: 9
```

 

**提示:**



- `1 <= m, n <= 4 * 10^4`
- `0 <= ops.length <= 10^4`
- `ops[i].length == 2`
- `1 <= ai <= m`
- `1 <= bi <= n`





```python
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        
        # 找到所有操作影响的最小行和列
        min_a = min(op[0] for op in ops)
        min_b = min(op[1] for op in ops)
        
        # 最大值一定是操作次数，即受影响的最小行和列的乘积
        return min_a * min_b
```



## 680.验证回文串II

双指针，https://leetcode.cn/problems/valid-palindrome-ii/

给你一个字符串 `s`，**最多** 可以从中删除一个字符。

请你判断 `s` 是否能成为回文字符串：如果能，返回 `true` ；否则，返回 `false` 。

 

**示例 1：**

```
输入：s = "aba"
输出：true
```

**示例 2：**

```
输入：s = "abca"
输出：true
解释：你可以删除字符 'c' 。
```

**示例 3：**

```
输入：s = "abc"
输出：false
```

 

**提示：**

- `1 <= s.length <= 10^5`
- `s` 由小写英文字母组成



```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(subs, left, right):
            """检查子串 subs[left:right+1] 是否为回文"""
            while left < right:
                if subs[left] != subs[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:  
                # 尝试删除左边或右边的字符，看是否是回文
                return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)
            left += 1
            right -= 1
        
        return True  # 如果从头到尾都是回文，直接返回 True

```



## 922.按奇偶排序数组II

two pointers, https://leetcode.cn/problems/sort-array-by-parity-ii/

给定一个非负整数数组 `nums`， `nums` 中一半整数是 **奇数** ，一半整数是 **偶数** 。

对数组进行排序，以便当 `nums[i]` 为奇数时，`i` 也是 **奇数** ；当 `nums[i]` 为偶数时， `i` 也是 **偶数** 。

你可以返回 *任何满足上述条件的数组作为答案* 。

 

**示例 1：**

```
输入：nums = [4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
```

**示例 2：**

```
输入：nums = [2,3]
输出：[2,3]
```

 

**提示：**

- `2 <= nums.length <= 2 * 104`
- `nums.length` 是偶数
- `nums` 中一半是偶数
- `0 <= nums[i] <= 1000`

 

**进阶：**可以不使用额外空间解决问题吗？



```python
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        j = 1  # Pointer for odd index
        for i in range(0, len(nums), 2):  # Traverse even indices
            if nums[i] % 2:  # If an odd number is found at even index
                while nums[j] % 2:  # Find the next even number at odd index
                    j += 2
                # Swap them
                nums[i], nums[j] = nums[j], nums[i]
        
        return nums

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



## 3438.找到字符串中和法的相邻数字

implementation, https://leetcode.cn/problems/find-valid-pair-of-adjacent-digits-in-string/

给你一个只包含数字的字符串 `s` 。如果 `s` 中两个 **相邻** 的数字满足以下条件，我们称它们是 **合法的** ：

- 前面的数字 **不等于** 第二个数字。
- 两个数字在 `s` 中出现的次数 **恰好** 分别等于这个数字本身。

请你从左到右遍历字符串 `s` ，并返回最先找到的 **合法** 相邻数字。如果这样的相邻数字不存在，请你返回一个空字符串。

 

**示例 1：**

**输入：**s = "2523533"

**输出：**"23"

**解释：**

数字 `'2'` 出现 2 次，数字 `'3'` 出现 3 次。`"23"` 中每个数字在 `s` 中出现的次数都恰好分别等于数字本身。所以输出 `"23"` 。

**示例 2：**

**输入：**s = "221"

**输出：**"21"

**解释：**

数字 `'2'` 出现 2 次，数字 `'1'` 出现 1 次。所以输出 `"21"` 。

**示例 3：**

**输入：**s = "22"

**输出：**""

**解释：**

没有合法的相邻数字。

 

**提示：**

- `2 <= s.length <= 100`
- `s` 只包含 `'1'` 到 `'9'` 的数字。



```python
from collections import Counter

class Solution:
    def findValidPair(self, s: str) -> str:
        # 计算每个字符出现的次数
        cnt = Counter(s)
        
        # 遍历字符串，寻找符合条件的第一对字符
        for i in range(len(s) - 1):
            if s[i] != s[i + 1] and cnt[s[i]] == int(s[i]) and cnt[s[i + 1]] == int(s[i + 1]):
                return s[i] + s[i + 1]
                
        return ""

if __name__ == "__main__":
    sol = Solution()
    test_cases = ["2523533", "221"]
    
    for s in test_cases:
        print(f"Input: {s}, Output: {sol.findValidPair(s)}")
```



## 3442.奇偶频次间的最大差值I

https://leetcode.cn/problems/maximum-difference-between-even-and-odd-frequency-i/

给你一个由小写英文字母组成的字符串 `s` 。请你找出字符串中两个字符的出现频次之间的 **最大** 差值，这两个字符需要满足：

- 一个字符在字符串中出现 **偶数次** 。
- 另一个字符在字符串中出现 **奇数次** 。

返回 **最大** 差值，计算方法是出现 **奇数次** 字符的次数 **减去** 出现 **偶数次** 字符的次数。

 

**示例 1：**

**输入：**s = "aaaaabbc"

**输出：**3

**解释：**

- 字符 `'a'` 出现 **奇数次** ，次数为 `5` ；字符 `'b'` 出现 **偶数次** ，次数为 `2` 。
- 最大差值为 `5 - 2 = 3` 。

**示例 2：**

**输入：**s = "abcabcab"

**输出：**1

**解释：**

- 字符 `'a'` 出现 **奇数次** ，次数为 `3` ；字符 `'c'` 出现 **偶数次** ，次数为 2 。
- 最大差值为 `3 - 2 = 1` 。

 

**提示：**

- `3 <= s.length <= 100`
- `s` 仅由小写英文字母组成。
- `s` 至少由一个出现奇数次的字符和一个出现偶数次的字符组成。



```python
from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        odd, even = [], []
        for key,value in count.items():
            if value % 2 == 1:
                odd.append((value, key))
            else:
                even.append((value, key))
        odd.sort(reverse = True)
        even.sort()
        #print(odd, even)
        return odd[0][0] - even[0][0]

if __name__ == '__main__':
    s = Solution()
    print(s.maxDifference("aaaaabbc"))
    print(s.maxDifference("abcabcab"))

```





# 中等



## 2.两数相加

linked list, https://leetcode.cn/problems/add-two-numbers/

给你两个 **非空** 的链表，表示两个非负的整数。它们每位数字都是按照 **逆序** 的方式存储的，并且每个节点只能存储 **一位** 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

 

**示例 1：**

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/02/addtwonumber1.jpg" alt="img" style="zoom:67%;" />

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

<img src="https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/07/25/question_11.jpg" alt="img" style="zoom:67%;" />

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

<img src="https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg" alt="img" style="zoom:67%;" />

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







## 24.两两交换链表中的节点

https://leetcode.cn/problems/swap-nodes-in-pairs/

给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

 

**示例 1：**

<img src="https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg" alt="img" style="zoom:67%;" />

```
输入：head = [1,2,3,4]
输出：[2,1,4,3]
```

**示例 2：**

```
输入：head = []
输出：[]
```

**示例 3：**

```
输入：head = [1]
输出：[1]
```

 

**提示：**

- 链表中节点的数目在范围 `[0, 100]` 内
- `0 <= Node.val <= 100`



```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pre = dummy
        while head and head.next:
            next_node = head.next.next
            pre.next = head.next
            head.next.next = head
            head.next = next_node
            pre = head
            head = next_node
        
        return dummy.next
        
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



## 33.搜索旋转排序数组

二分查找，https://leetcode.cn/problems/search-in-rotated-sorted-array/

整数数组 `nums` 按升序排列，数组中的值 **互不相同** 。

在传递给函数之前，`nums` 在预先未知的某个下标 `k`（`0 <= k < nums.length`）上进行了 **旋转**，使数组变为 `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`（下标 **从 0 开始** 计数）。例如， `[0,1,2,4,5,6,7]` 在下标 `3` 处经旋转后可能变为 `[4,5,6,7,0,1,2]` 。

给你 **旋转后** 的数组 `nums` 和一个整数 `target` ，如果 `nums` 中存在这个目标值 `target` ，则返回它的下标，否则返回 `-1` 。

你必须设计一个时间复杂度为 `O(log n)` 的算法解决此问题。

 

**示例 1：**

```
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
```

**示例 2：**

```
输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
```

**示例 3：**

```
输入：nums = [1], target = 0
输出：-1
```

 

**提示：**

- `1 <= nums.length <= 5000`
- `-104 <= nums[i] <= 104`
- `nums` 中的每个值都 **独一无二**
- 题目数据保证 `nums` 在预先未知的某个下标上进行了旋转
- `-104 <= target <= 104`



```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # 如果左侧是有序的
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 如果右侧是有序的
            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left += 1
        
        return -1
        
```







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



## 40.组合总和II

backtracking , https://leetcode.cn/problems/combination-sum-ii/

给定一个候选人编号的集合 `candidates` 和一个目标数 `target` ，找出 `candidates` 中所有可以使数字和为 `target` 的组合。

`candidates` 中的每个数字在每个组合中只能使用 **一次** 。

**注意：**解集不能包含重复的组合。 

 

**示例 1:**

```
输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
```

**示例 2:**

```
输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]
```

 

**提示:**

- `1 <= candidates.length <= 100`
- `1 <= candidates[i] <= 50`
- `1 <= target <= 30`



```python
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  
        res = []  
        
        def dfs(start, remain, path):
            if remain == 0:
                res.append(path)  # 找到一个组合，加入结果
                return
            if remain < 0:
                return  
            
            for i in range(start, len(candidates)):
                num = candidates[i]
                # 跳过重复的元素，避免重复的组合
                if i > start and num == candidates[i-1]:
                    continue
                
                dfs(i + 1, remain - num, path + [num])
        
        dfs(0, target, [])
        
        return res

```



```python
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtracking(start, remain, path):
            if remain == 0:
                res.append(list(path))  # 找到一个组合，加入结果
                return
            if remain < 0:
                return

            for i in range(start, len(candidates)):
                num = candidates[i]
                # 跳过重复的元素，避免重复的组合
                if i > start and num == candidates[i - 1]:
                    continue
                path.append(num)
                backtracking(i + 1, remain - num, path)
                path.pop()

        backtracking(0, target, [])

        return res
```



## 45.跳跃游戏II

dp, https://leetcode.cn/problems/jump-game-ii/

给定一个长度为 `n` 的 **0 索引**整数数组 `nums`。初始位置为 `nums[0]`。

每个元素 `nums[i]` 表示从索引 `i` 向后跳转的最大长度。换句话说，如果你在 `nums[i]` 处，你可以跳转到任意 `nums[i + j]` 处:

- `0 <= j <= nums[i]` 
- `i + j < n`

返回到达 `nums[n - 1]` 的最小跳跃次数。生成的测试用例可以到达 `nums[n - 1]`。

 

**示例 1:**

```
输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
```

**示例 2:**

```
输入: nums = [2,3,0,1,4]
输出: 2
```

 

**提示:**

- `1 <= nums.length <= 104`
- `0 <= nums[i] <= 1000`
- 题目保证可以到达 `nums[n-1]`



```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(n):
            for j in range(1, nums[i]+1):
                if i + j < n:
                    dp[i+j] = min(dp[i+j], dp[i] + 1)
        
        #print(dp)
        return dp[n-1]
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

<img src="https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg" alt="img" style="zoom:67%;" />

```
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]
```

**示例 2：**

<img src="https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg" alt="img" style="zoom:67%;" />

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

<img src="https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg" alt="img" style="zoom:67%;" />

```
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
```

**示例 2：**

<img src="https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg" alt="img" style="zoom:67%;" />

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



## 55.跳跃游戏

greedy, dp, https://leetcode.cn/problems/jump-game/

给你一个非负整数数组 `nums` ，你最初位于数组的 **第一个下标** 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 `true` ；否则，返回 `false` 。

 

**示例 1：**

```
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
```

**示例 2：**

```
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
```

 

**提示：**

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`



dp

```python
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            if dp[i - 1]:
                for j in range(i, min(i+nums[i - 1], n)):
                    dp[j] = 1

        #print(dp)
        return True if dp[-1] else False

if __name__ == "__main__":
    sol = Solution()
    print(sol.canJump([2,3,1,1,4]))  # True
    print(sol.canJump([3,2,1,0,4]))  # False
```



greedy

```python
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0  # 记录当前能到达的最远位置
        n = len(nums)
        
        for i in range(n):
            if i > max_reach:  
                return False  # 如果当前下标已经超出能到达的最远位置，则无法继续
            
            max_reach = max(max_reach, i + nums[i])  # 更新能到达的最远位置
            
            if max_reach >= n - 1:
                return True  # 如果可以到达或超越终点，直接返回 True
        
        return False

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

<img src="https://pic.leetcode.cn/1697422740-adxmsI-image.png" alt="img" style="zoom:67%;" />

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

<img src="https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg" alt="img" style="zoom:67%;" />

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

<img src="https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg" alt="img" style="zoom:67%;" />

```
输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]
```

**示例 2：**

<img src="https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg" alt="img" style="zoom:67%;" />

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

<img src="https://assets.leetcode.com/uploads/2020/10/05/mat.jpg" alt="img" style="zoom:67%;" />

```
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
```

**示例 2：**

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/25/mat2.jpg" alt="img" style="zoom:67%;" />

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



## 75.颜色分类

https://leetcode.cn/problems/sort-colors/

给定一个包含红色、白色和蓝色、共 `n` 个元素的数组 `nums` ，**[原地](https://baike.baidu.com/item/原地算法)** 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 `0`、 `1` 和 `2` 分别表示红色、白色和蓝色。

必须在不使用库内置的 sort 函数的情况下解决这个问题。

 

**示例 1：**

```
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]
```

**示例 2：**

```
输入：nums = [2,0,1]
输出：[0,1,2]
```

 

**提示：**

- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` 为 `0`、`1` 或 `2`



使用荷兰国旗问题的算法来解决这个问题。该算法基于三个指针：一个指向红色的边界（0），一个指向白色的边界（1），一个指向蓝色的边界（2）。我们可以通过一次遍历，将所有的颜色分组并按顺序排列。

具体步骤如下：

1. 使用三个指针，`low`（红色的边界）、`mid`（白色的当前指针）和 `high`（蓝色的边界）。
2. 遍历数组，遇到以下情况：
   - 如果当前元素是 `0`，将它和 `low` 指向的元素交换，然后 `low` 和 `mid` 都向右移动。
   - 如果当前元素是 `1`，只需将 `mid` 向右移动。
   - 如果当前元素是 `2`，将它和 `high` 指向的元素交换，然后 `high` 向左移动，`mid` 不变。

这个算法的时间复杂度是 O(n)，空间复杂度是 O(1)。

下面是代码实现：

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1
    
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]  # Swap 0 to the low part
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1  # Just move the mid pointer
            else:  # nums[mid] == 2
                nums[high], nums[mid] = nums[mid], nums[high]  # Swap 2 to the high part
                high -= 1
        
        return nums
```

这个算法会一次性完成排序，且不使用任何额外的空间。



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



## 79.单词搜索

回溯，https://leetcode.cn/problems/word-search/



给定一个 `m x n` 二维字符网格 `board` 和一个字符串单词 `word` 。如果 `word` 存在于网格中，返回 `true` ；否则，返回 `false` 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

**示例 1：**

<img src="https://assets.leetcode.com/uploads/2020/11/04/word2.jpg" alt="img" style="zoom:67%;" />

```
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
```

**示例 2：**

<img src="https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg" alt="img" style="zoom:67%;" />

```
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true
```

**示例 3：**

<img src="https://assets.leetcode.com/uploads/2020/10/15/word3.jpg" alt="img" style="zoom:67%;" />

```
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false
```

 

**提示：**

- `m == board.length`
- `n = board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` 和 `word` 仅由大小写英文字母组成

 

**进阶：**你可以使用搜索剪枝的技术来优化解决方案，使其在 `board` 更大的情况下可以更快解决问题？



3535ms，击败58.21%

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            tmp, board[i][j] = board[i][j], '/'
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = tmp
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
        
```





**进阶：**你可以使用搜索剪枝的技术来优化解决方案，使其在 `board` 更大的情况下可以更快解决问题？

To optimize the solution using search pruning, we can add a few checks to avoid unnecessary recursive calls. One effective technique is to use a set to keep track of visited cells, which helps in avoiding revisiting the same cell within the same path.

Here is the optimized Python code:

5133ms，击败18.36%

```python
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k, visited):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k] or (i, j) in visited:
                return False
            if k == len(word) - 1:
                return True
            visited.add((i, j))
            res = (dfs(i + 1, j, k + 1, visited) or
                   dfs(i - 1, j, k + 1, visited) or
                   dfs(i, j + 1, k + 1, visited) or
                   dfs(i, j - 1, k + 1, visited))
            visited.remove((i, j))
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0, set()):
                    return True
        return False
```

### Explanation:

1. **Visited Set**: A set `visited` is used to keep track of the cells that have been visited in the current path.
2. **DFS Function**: The `dfs` function now takes an additional parameter `visited` to manage the visited cells.
3. **Pruning**: Before making recursive calls, the function checks if the current cell is already visited or if it does not match the current character in the word.
4. **Backtracking**: After exploring all possible paths from the current cell, the cell is removed from the `visited` set to allow other paths to use it.



## 81.搜索旋转排序数组II

二分查找，https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/

已知存在一个按非降序排列的整数数组 `nums` ，数组中的值不必互不相同。

在传递给函数之前，`nums` 在预先未知的某个下标 `k`（`0 <= k < nums.length`）上进行了 **旋转** ，使数组变为 `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`（下标 **从 0 开始** 计数）。例如， `[0,1,2,4,4,4,5,6,6,7]` 在下标 `5` 处经旋转后可能变为 `[4,5,6,6,7,0,1,2,4,4]` 。

给你 **旋转后** 的数组 `nums` 和一个整数 `target` ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 `nums` 中存在这个目标值 `target` ，则返回 `true` ，否则返回 `false` 。

你必须尽可能减少整个操作步骤。

 

**示例 1：**

```
输入：nums = [2,5,6,0,0,1,2], target = 0
输出：true
```

**示例 2：**

```
输入：nums = [2,5,6,0,0,1,2], target = 3
输出：false
```

 

**提示：**

- `1 <= nums.length <= 5000`
- `-104 <= nums[i] <= 104`
- 题目数据保证 `nums` 在预先未知的某个下标上进行了旋转
- `-104 <= target <= 104`

 

**进阶：**

- 此题与 [搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/) 相似，但本题中的 `nums` 可能包含 **重复** 元素。这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？



```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return True
            
            # 如果左侧是有序的
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 如果右侧是有序的
            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            # 处理重复元素的情况，直接跳过相同的元素
            else:
                left += 1
        
        return False
```





## 98.验证二叉搜索树

https://leetcode.cn/problems/validate-binary-search-tree/

给你一个二叉树的根节点 `root` ，判断其是否是一个有效的二叉搜索树。

**有效** 二叉搜索树定义如下：

- 节点的左子树只包含**小于**当前节点的数。
- 节点的右子树只包含 **大于** 当前节点的数。
- 所有左子树和右子树自身必须也是二叉搜索树。

子树，`treeName`树中的一个节点及其所有子孙节点所构成的树称为`treeName`的子树。

 

**示例 1：**

<img src="https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg" alt="img" style="zoom:67%;" />

```
输入：root = [2,1,3]
输出：true
```

**示例 2：**

<img src="https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg" alt="img" style="zoom:67%;" />

```
输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。
```

 

**提示：**

- 树中节点数目范围在`[1, 10^4]` 内
- `-231 <= Node.val <= 2^31 - 1`



```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            val = node.val
            if val <= low or val >= high:
                return False
            if not dfs(node.right, val, high):
                return False
            if not dfs(node.left, low, val):
                return False
            return True

        return dfs(root)
```







## 102.二叉树的层序遍历

https://leetcode.cn/problems/binary-tree-level-order-traversal/

给你二叉树的根节点 `root` ，返回其节点值的 **层序遍历** 。 （即逐层地，从左到右访问所有节点）。

**示例 1：**

<img src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg" alt="img" style="zoom:67%;" />

```
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
```

**示例 2：**

```
输入：root = [1]
输出：[[1]]
```

**示例 3：**

```
输入：root = []
输出：[]
```

 

**提示：**

- 树中节点数目在范围 `[0, 2000]` 内
- `-1000 <= Node.val <= 1000`





```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result
        
```



## 105.从前序与中序遍历序列构造二叉树

https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

给定两个整数数组 `preorder` 和 `inorder` ，其中 `preorder` 是二叉树的**先序遍历**， `inorder` 是同一棵树的**中序遍历**，请构造二叉树并返回其根节点。

**示例 1:**

<img src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" alt="img" style="zoom:67%;" />

```
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]
```

**示例 2:**

```
输入: preorder = [-1], inorder = [-1]
输出: [-1]
```

 

**提示:**

- `1 <= preorder.length <= 3000`
- `inorder.length == preorder.length`
- `-3000 <= preorder[i], inorder[i] <= 3000`
- `preorder` 和 `inorder` 均 **无重复** 元素
- `inorder` 均出现在 `preorder`
- `preorder` **保证** 为二叉树的前序遍历序列
- `inorder` **保证** 为二叉树的中序遍历序列



```python
from typing import List, Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # The first element in preorder is the root
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Find the index of the root in inorder
        root_index = inorder.index(root_val)

        # Recursively build the left and right subtrees
        root.left = self.buildTree(preorder[1:1 + root_index], inorder[:root_index])
        root.right = self.buildTree(preorder[1 + root_index:], inorder[root_index + 1:])

        return root

if __name__ == '__main__':
    solution = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = solution.buildTree(preorder, inorder)
    # The output tree is [3, 9, 20, None, None, 15, 7]

```





## LCR 107.01 矩阵

dp, https://leetcode.cn/problems/2bCMpM/

给定一个由 `0` 和 `1` 组成的矩阵 `mat` ，请输出一个大小相同的矩阵，其中每一个格子是 `mat` 中对应位置元素到最近的 `0` 的距离。

两个相邻元素间的距离为 `1` 。

 

**示例 1：**

<img src="https://pic.leetcode-cn.com/1626667201-NCWmuP-image.png" alt="img" style="zoom:67%;" />

```
输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
输出：[[0,0,0],[0,1,0],[0,0,0]]
```

**示例 2：**

<img src="https://pic.leetcode-cn.com/1626667205-xFxIeK-image.png" alt="img" style="zoom:67%;" />

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



## 113.路径总和II

https://leetcode.cn/problems/path-sum-ii/

给你二叉树的根节点 `root` 和一个整数目标和 `targetSum` ，找出所有 **从根节点到叶子节点** 路径总和等于给定目标和的路径。

**叶子节点** 是指没有子节点的节点。

 

**示例 1：**

<img src="https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg" alt="img" style="zoom:67%;" />

```
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]
```

**示例 2：**

<img src="https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg" alt="img" style="zoom:67%;" />

```
输入：root = [1,2,3], targetSum = 5
输出：[]
```

**示例 3：**

```
输入：root = [1,2], targetSum = 0
输出：[]
```

 

**提示：**

- 树中节点总数在范围 `[0, 5000]` 内
- `-1000 <= Node.val <= 1000`
- `-1000 <= targetSum <= 1000`



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        # 如果树为空，直接返回False
        if not root:
            return []
        
        # 递归函数定义
        def dfs(node, path, current_sum):
            # 更新当前路径的和
            current_sum += node.val
            new_path = path + [node.val]
            
            # 如果到达叶子节点，检查路径和是否等于目标值
            if not node.left and not node.right:
                if current_sum == targetSum:
                    res.append(new_path)
                return 
            
            if node.left:
                dfs(node.left, new_path, current_sum)
            if node.right:
                dfs(node.right, new_path, current_sum) 
            
        
        dfs(root, [], 0)
        return res
        
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



## 131.分割回文串

backtracking, https://leetcode.cn/problems/palindrome-partitioning/

给你一个字符串 `s`，请你将 `s` 分割成一些子串，使每个子串都是 

**回文串**。返回 `s` 所有可能的分割方案。回文串是指向前和向后读都相同的字符串。



**示例 1：**

```
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
```

**示例 2：**

```
输入：s = "a"
输出：[["a"]]
```

 

**提示：**

- `1 <= s.length <= 16`
- `s` 仅由小写英文字母组成



```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            return s == s[::-1]

        def backtracking(start, path):
            if start == len(s):
                res.append(path)
                return 
            for i in range(start, len(s)):
                if is_palindrome(s[start:i+1]):
                    backtracking(i+1, path + [s[start:i+1]])
        
        res = []
        backtracking(0, [])
        return res
```







## 138.随机链表的复制

https://leetcode.cn/problems/copy-list-with-random-pointer/

给你一个长度为 `n` 的链表，每个节点包含一个额外增加的随机指针 `random` ，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 **[深拷贝](https://baike.baidu.com/item/深拷贝/22785317?fr=aladdin)**。 深拷贝应该正好由 `n` 个 **全新** 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 `next` 指针和 `random` 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。**复制链表中的指针都不应指向原链表中的节点** 。

例如，如果原链表中有 `X` 和 `Y` 两个节点，其中 `X.random --> Y` 。那么在复制链表中对应的两个节点 `x` 和 `y` ，同样有 `x.random --> y`。

返回复制链表的头节点。

用一个由 `n` 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 `[val, random_index]` 表示：

- `val`：一个表示 `Node.val` 的整数。
- `random_index`：随机指针指向的节点索引（范围从 `0` 到 `n-1`）；如果不指向任何节点，则为 `null` 。

你的代码 **只** 接受原链表的头节点 `head` 作为传入参数。

 

**示例 1：**

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e1.png)

```
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
```

**示例 2：**

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e2.png)

```
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
```

**示例 3：**

**![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e3.png)**

```
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
```

 

**提示：**

- `0 <= n <= 1000`
- `-104 <= Node.val <= 104`
- `Node.random` 为 `null` 或指向链表中的节点。





```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Step 1: Clone each node and link them right after the original node.
        current = head
        while current:
            clonedNode = Node(current.val, current.next, None)
            current.next = clonedNode
            current = clonedNode.next
        
        # Step 2: Assign random pointers for the cloned nodes.
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        # Step 3: Separate the cloned nodes to form a new list.
        dummyHead = Node(0)  # Dummy node to help with the new list construction.
        current = head
        clonedCurrent = dummyHead
        
        while current:
            clonedCurrent.next = current.next
            current.next = current.next.next
            
            clonedCurrent = clonedCurrent.next
            current = current.next
        
        return dummyHead.next
        
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



## 142.环形链表II

https://leetcode.cn/problems/linked-list-cycle-ii/

给定一个链表的头节点  `head` ，返回链表开始入环的第一个节点。 *如果链表无环，则返回 `null`。*

如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（**索引从 0 开始**）。如果 `pos` 是 `-1`，则在该链表中没有环。**注意：`pos` 不作为参数进行传递**，仅仅是为了标识链表的实际情况。

**不允许修改** 链表。

 

**示例 1：**

<img src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png" alt="img" style="zoom:67%;" />

```
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
```

**示例 2：**

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png" alt="img" style="zoom:67%;" />

```
输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。
```

**示例 3：**

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png" alt="img" style="zoom:67%;" />

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





## 148.排序链表

https://leetcode.cn/problems/sort-list/

给你链表的头结点 `head` ，请将其按 **升序** 排列并返回 **排序后的链表** 。

 

**示例 1：**

<img src="https://assets.leetcode.com/uploads/2020/09/14/sort_list_1.jpg" alt="img" style="zoom:67%;" />

```
输入：head = [4,2,1,3]
输出：[1,2,3,4]
```

**示例 2：**

<img src="https://assets.leetcode.com/uploads/2020/09/14/sort_list_2.jpg" alt="img" style="zoom:67%;" />

```
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
```

**示例 3：**

```
输入：head = []
输出：[]
```

 

**提示：**

- 链表中节点的数目在范围 `[0, 5 * 10^4]` 内
- `-105 <= Node.val <= 10^5`

 

**进阶：**你可以在 `O(n log n)` 时间复杂度和常数级空间复杂度下，对链表进行排序吗？



```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        # Helper function to find the middle of the linked list
        def find_middle(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        # Helper function to merge two sorted linked lists
        def merge(l1, l2):
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 if l1 else l2
            return dummy.next
        
        # Split the linked list into two halves
        mid = find_middle(head)
        right = mid.next
        mid.next = None
        left = head
        
        # Recursively sort each half
        left = self.sortList(left)
        right = self.sortList(right)
        
        # Merge the sorted halves
        return merge(left, right)

# Example usage
if __name__ == "__main__":
    def print_list(node):
        while node:
            print(node.val, end=" -> ")
            node = node.next
        print("None")
    
    # Create linked list [4, 2, 1, 3]
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    sorted_head = Solution().sortList(head)
    print_list(sorted_head)  # Output: 1 -> 2 -> 3 -> 4 -> None
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





## 153.寻找旋转排序数组中的最小值

binary search, https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/

已知一个长度为 `n` 的数组，预先按照升序排列，经由 `1` 到 `n` 次 **旋转** 后，得到输入数组。例如，原数组 `nums = [0,1,2,4,5,6,7]` 在变化后可能得到：

- 若旋转 `4` 次，则可以得到 `[4,5,6,7,0,1,2]`
- 若旋转 `7` 次，则可以得到 `[0,1,2,4,5,6,7]`

注意，数组 `[a[0], a[1], a[2], ..., a[n-1]]` **旋转一次** 的结果为数组 `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]` 。

给你一个元素值 **互不相同** 的数组 `nums` ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 **最小元素** 。

你必须设计一个时间复杂度为 `O(log n)` 的算法解决此问题。

 

**示例 1：**

```
输入：nums = [3,4,5,1,2]
输出：1
解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。
```

**示例 2：**

```
输入：nums = [4,5,6,7,0,1,2]
输出：0
解释：原数组为 [0,1,2,4,5,6,7] ，旋转 4 次得到输入数组。
```

**示例 3：**

```
输入：nums = [11,13,15,17]
输出：11
解释：原数组为 [11,13,15,17] ，旋转 4 次得到输入数组。
```

 

**提示：**

- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- `nums` 中的所有整数 **互不相同**
- `nums` 原来是一个升序排序的数组，并进行了 `1` 至 `n` 次旋转





这个问题可以使用 **二分查找** 来解决，时间复杂度是 O(log⁡n)。由于数组已经旋转过，所以它是一个部分排序的数组。我们可以利用二分查找来定位最小值。

思路：

1. 数组的最小元素一定会在旋转点附近。如果数组没有被旋转，那么最小元素就是数组的第一个元素。
2. 在旋转数组中，数组的两个部分（左部分和右部分）各自是升序的。
3. 如果 `nums[mid]` 大于 `nums[right]`，说明最小元素在 `mid` 右边的部分，因为此时右部分的值比中间值小；否则，最小元素在 `mid` 左边或者 `mid` 就是最小元素。

代码实现：

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
    
        while left < right:
            mid = left + (right - left) // 2
            
            # 如果中间元素大于右边元素，说明最小元素在右边
            if nums[mid] > nums[right]:
                left = mid + 1
            # 否则最小元素在左边
            else:
                right = mid
        
        # 最后left和right会指向最小元素
        return nums[left]
```

时间复杂度：

- 每次二分查找都将搜索范围缩小一半，所以时间复杂度是 O(log⁡n)。

空间复杂度：

- 只使用了常数级别的额外空间，空间复杂度是 O(1)。

这种方法通过二分查找能够高效地找到最小元素。



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



## 199.二叉树的右视图

bfs, https://leetcode.cn/problems/binary-tree-right-side-view/

给定一个二叉树的 **根节点** `root`，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

 

**示例 1：**

**输入：**root = [1,2,3,null,5,null,4]

**输出：**[1,3,4]

**解释：**

<img src="https://assets.leetcode.com/uploads/2024/11/24/tmpd5jn43fs-1.png" alt="img" style="zoom: 50%;" />

**示例 2：**

**输入：**root = [1,2,3,4,null,null,null,5]

**输出：**[1,3,4,5]

**解释：**

<img src="https://assets.leetcode.com/uploads/2024/11/24/tmpkpe40xeh-1.png" alt="img" style="zoom: 50%;" />

**示例 3：**

**输入：**root = [1,null,3]

**输出：**[1,3]

**示例 4：**

**输入：**root = []

**输出：**[]

 

**提示:**

- 二叉树的节点个数的范围是 `[0,100]`
- `-100 <= Node.val <= 100` 





```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = deque([root])
        while q:
            level_length = len(q)
            for i in range(level_length):
                node = q.popleft()
                if i == level_length - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return res

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



## 207.课程表

拓扑排序，https://leetcode.cn/problems/course-schedule/

你这个学期必须选修 `numCourses` 门课程，记为 `0` 到 `numCourses - 1` 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 `prerequisites` 给出，其中 `prerequisites[i] = [ai, bi]` ，表示如果要学习课程 `ai` 则 **必须** 先学习课程 `bi` 。

- 例如，先修课程对 `[0, 1]` 表示：想要学习课程 `0` ，你需要先完成课程 `1` 。

请你判断是否可能完成所有课程的学习？如果可以，返回 `true` ；否则，返回 `false` 。

 

**示例 1：**

```
输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
```

**示例 2：**

```
输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
```

 

**提示：**

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= ai, bi < numCourses`
- `prerequisites[i]` 中的所有课程对 **互不相同**



这个问题是一个典型的**拓扑排序**问题，要求判断是否可以完成所有课程的学习，或者判断课程之间是否存在循环依赖。拓扑排序的两种常用方法是：**Kahn 算法**（基于入度）和**深度优先搜索**（DFS）。下面我将分别给出这两种方法的 Python 实现。

**1. Kahn 算法（基于入度的拓扑排序）**

Kahn 算法通过入度来实现拓扑排序。首先我们需要构建一个图，并计算每个节点（课程）的入度。然后从入度为 0 的节点开始，依次移除节点并更新相邻节点的入度。如果最后能访问所有课程，则说明没有环，反之则有环。

```python
from collections import deque, defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 构建图和入度数组
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1
        
        # 初始化入度为0的节点
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        # 拓扑排序
        visited_courses = 0
        
        while queue:
            course = queue.popleft()
            visited_courses += 1
            
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # 如果访问的课程数量等于总课程数，则说明没有环，返回 True
        return visited_courses == numCourses

# Example usage
if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0]]
    print(Solution().canFinish(numCourses, prerequisites))  # Output: true
        
```

解析

- **Kahn 算法**：基于入度，首先统计每个节点的入度。入度为 0 的节点可以先学习，然后逐步删除这些节点并减少相邻节点的入度。如果最终所有课程都能学习完，则返回 `True`，否则返回 `False`。

- **Kahn 算法**：`O(V + E)`，其中 `V` 是课程数量，`E` 是先修课程对的数量。



**2.深度优先搜索（DFS）**

DFS 方法通过递归检查课程之间的依赖关系，如果遇到一个课程被访问过两次，说明存在环。在 DFS 过程中，使用一个标记数组来表示当前节点的状态：

- `0` 表示未访问过；
- `1` 表示正在访问（递归栈中）；
- `2` 表示访问完成。

**Plan:**

1. Create a graph using adjacency list representation.
2. Use Depth-First Search (DFS) to detect cycles in the graph.
3. If a cycle is detected, return `false` (not possible to complete all courses).
4. If no cycle is detected, return `true` (possible to complete all courses).

```python
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create adjacency list for the graph
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # States: 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses
        
        def hasCycle(v):
            if state[v] == 1:  # Found a cycle
                return True
            if state[v] == 2:  # Already visited node
                return False
            
            state[v] = 1  # Mark as visiting
            for neighbor in graph[v]:
                if hasCycle(neighbor):
                    return True
            state[v] = 2  # Mark as visited
            return False
        
        for course in range(numCourses):
            if hasCycle(course):
                return False
        
        return True

# Example usage
if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0]]
    print(Solution().canFinish(numCourses, prerequisites))  # Output: true
```

**DFS 方法**：通过深度优先搜索检测图中是否存在环。如果在递归过程中，发现某个节点正在被访问，说明出现了环。时间复杂度`O(V + E)`，每个节点和边最多会被访问一次。



## 208.实现Trie（前缀树）

字典树，https://leetcode.cn/problems/implement-trie-prefix-tree/

Trie（发音类似 "try"）或者说 **前缀树** 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补全和拼写检查。

请你实现 Trie 类：

- `Trie()` 初始化前缀树对象。
- `void insert(String word)` 向前缀树中插入字符串 `word` 。
- `boolean search(String word)` 如果字符串 `word` 在前缀树中，返回 `true`（即，在检索之前已经插入）；否则，返回 `false` 。
- `boolean startsWith(String prefix)` 如果之前已经插入的字符串 `word` 的前缀之一为 `prefix` ，返回 `true` ；否则，返回 `false` 。

 

**示例：**

```
输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True
```

 

**提示：**

- `1 <= word.length, prefix.length <= 2000`
- `word` 和 `prefix` 仅由小写英文字母组成
- `insert`、`search` 和 `startsWith` 调用次数 **总计** 不超过 `3 * 104` 次





```python
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            node = node.setdefault(char, {})    #returns the value of the item with the specified key.
                                                # If the key does not exist, insert the key, with the specified value
        node[self.end_of_word] = self.end_of_word


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))   # return True
    print(trie.search("app"))     # return False
    print(trie.startsWith("app")) # return True
    trie.insert("app")
    print(trie.search("app"))     # return True

```



## 215.数组中的第K个最大元素

heap, https://leetcode.cn/problems/kth-largest-element-in-an-array/

给定整数数组 `nums` 和整数 `k`，请返回数组中第 `k` 个最大的元素。

请注意，你需要找的是数组排序后的第 `k` 个最大的元素，而不是第 `k` 个不同的元素。

你必须设计并实现时间复杂度为 `O(n)` 的算法解决此问题。

 

**示例 1:**

```
输入: [3,2,1,5,6,4], k = 2
输出: 5
```

**示例 2:**

```
输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4
```

 

**提示：** 

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`



对于你提供的情况，数组长度达到 10 万左右且包含大量相同的元素，使用 **快速选择算法**（Quickselect）有时可能会遇到性能瓶颈，尤其是当数组中大部分元素相同时，快速选择算法的性能会退化到最坏情况，导致时间复杂度为 $O(n^2)$。为了避免这种情况，我们可以考虑使用更稳定的算法，比如 **堆排序**（Heap Sort），这也是一个适用于此类问题的常见方法。

使用堆实现第 k 个最大元素

我们可以通过 **最小堆**（Min-Heap）来解决这个问题。具体思路是：

1. 构建一个大小为 k 的最小堆。
2. 遍历数组，对于每个元素，如果堆的大小小于 kk，就将元素加入堆中。
3. 如果堆的大小已经达到 k，并且当前元素比堆顶元素大，则替换堆顶元素。
4. 最终堆顶的元素就是第 k 个最大元素。

这样做的时间复杂度为 $O(n \log k)$，对于你的情况，使用最小堆是一个较为高效的解决方法。

代码实现：

```python
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 使用最小堆
        # 堆的大小保持为 k
        heap = nums[:k]
        heapq.heapify(heap)  # 将前 k 个元素构建成一个最小堆

        for num in nums[k:]:
            if num > heap[0]:  # 如果当前元素大于堆顶元素
                heapq.heapreplace(heap, num)  # 弹出堆顶并加入新元素

        return heap[0]  # 堆顶就是第 k 个最大元素

if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 输出 5
    print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))


    # 对于大数组的测试
    nums = [1] * 100000
    nums[-5:] = [-5, -4, -3, -2, -1]  # 将最后五个元素设置为 -5 到 -1
    k = 50000
    print(s.findKthLargest(nums, k))  # 输出第 50000 个最大的元素
```

> 代码解释：
>
> 1. 最小堆的构建：
>
>    - 我们先构建一个大小为 k 的最小堆，它会存储数组中的前 k 个元素。
>
> 2. 遍历数组：
>
>    - 然后我们从第 k+1
>
>      个元素开始遍历，检查每个元素与堆顶的元素：
>
>      - 如果当前元素比堆顶元素大，就用当前元素替换堆顶元素。
>
> 3. 最终结果：
>
>    - 经过遍历后，堆顶的元素就是第 k 个最大元素。
>
> 时间复杂度：
>
> - 构建最小堆的时间复杂度是 O(k)。
> - 遍历剩余的 n - k 个元素，每个操作的时间复杂度是 $O(\log k)$，因为我们每次要对堆进行替换操作。
> - 总体时间复杂度是 $O(n \log k)$。
>
> 空间复杂度：
>
> - 堆占用的空间为 O(k)，因此空间复杂度是 O(k)。
>
> 示例：
>
> 对于输入 `nums = [1, 2, 3, 4, 5, 1, ..., 1, 1, 1, 1, 1, -5, -4, -3, -2, -1]` 和 `k = 50000`，该算法可以在较短的时间内处理大规模数据，并且避免了快速选择算法可能的最坏情况。
>
> 总结：
>
> 使用最小堆解决这个问题是一个高效的方式，尤其是当数组中包含大量重复元素时，它的性能会比快速选择算法更稳定。







为了在时间复杂度为 O(n) 的情况下解决这个问题，可以利用 **快速选择算法**（Quickselect）。这是一种基于快速排序的分治算法，它能够在平均时间复杂度为 O(n) 的情况下找到数组中的第 k 个最大元素。

思路：

1. **快速排序的思路**：
   - 快速排序的核心思想是选择一个 "pivot" 元素，并将数组划分为两部分：一部分小于或等于 pivot，另一部分大于 pivot。
   - 快速选择算法基于这个思路，通过划分数组来逐步缩小搜索范围，直到找到第 kk 个最大元素。
2. **选择第 kk 个最大元素**：
   - 如果我们希望找到第 k 个 **最大的** 元素，实际上是在排序后的数组中找到第 n-k 个 **最小** 元素。
   - 通过快速选择，我们可以只在需要的部分递归查找，而不需要对整个数组进行排序，从而提高效率。

快速选择算法的核心步骤：

- 随机选择一个 pivot 元素。
- 划分数组，使得 pivot 左边的所有元素都小于 pivot，右边的所有元素都大于 pivot。
- 根据 pivot 的位置与 n−k 比较，确定下一步应该在哪个部分继续查找。

代码实现。超出时间限制，41 / 42 个通过的测试用例。

```python
import random	
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickselect(left, right):
            # 随机选择一个 pivot
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)

            # 判断 pivot 所在位置与目标位置的关系
            if pivot_index == k:
                return nums[pivot_index]
            elif pivot_index < k:
                return quickselect(pivot_index + 1, right)
            else:
                return quickselect(left, pivot_index - 1)

        def partition(left, right, pivot_index):
            pivot_value = nums[pivot_index]
            # 将 pivot 移动到右边
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            store_index = left
            # 将所有小于 pivot 的元素移到左边
            for i in range(left, right):
                if nums[i] < pivot_value:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            # 将 pivot 移动到它的正确位置
            nums[right], nums[store_index] = nums[store_index], nums[right]
            return store_index

        # 目标位置是第 n-k 最小的元素
        n = len(nums)
        k = n - k  # 转换为最小元素的索引
        return quickselect(0, n - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 输出 5
    print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 输出 4

```

> 代码解释：
>
> 1. **`quickselect` 函数**：
>    - 这是快速选择算法的主函数，用来在数组的子区间 `[left, right]` 中查找第 kk 个最大元素。
>    - `pivot_index` 是通过 `partition` 函数划分数组后 pivot 元素的最终位置。
>    - 如果 pivot 的位置是目标位置（即 `pivot_index == k`），则返回该元素。
>    - 如果 pivot 的位置小于目标位置，继续在右半部分查找；如果大于目标位置，继续在左半部分查找。
> 2. **`partition` 函数**：
>    - 通过选定的 pivot 元素将数组划分成两部分：一部分小于 pivot，另一部分大于 pivot。
>    - 最后返回 pivot 的位置，供 `quickselect` 函数进一步判断。
> 3. **目标位置转换**：
>    - 因为我们要求的是第 kk 个 **最大的** 元素，所以在 `quickselect` 中，实际上是查找数组中第 `n-k` 个 **最小** 元素的位置（其中 `n` 是数组的长度）。
>
> 时间复杂度：
>
> - **平均时间复杂度**是 O(n)，这是由于快速选择算法通过每次划分数组的方式将搜索空间缩小到一半。
> - 最坏情况下，时间复杂度为 $O(n^2)$，但这种情况极为少见（当每次选择的 pivot 总是最小或最大时）。
>
> 空间复杂度：
>
> - 快速选择算法的空间复杂度是 O(1)，因为我们只使用了常数级别的额外空间，除了递归栈的深度。





## 230.二叉搜索树中第K小的元素

https://leetcode.cn/problems/kth-smallest-element-in-a-bst/

给定一个二叉搜索树的根节点 `root` ，和一个整数 `k` ，请你设计一个算法查找其中第 `k` 小的元素（从 1 开始计数）。

 

**示例 1：**

<img src="https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg" alt="img" style="zoom:67%;" />

```
输入：root = [3,1,4,null,2], k = 1
输出：1
```

**示例 2：**

<img src="https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg" alt="img" style="zoom:67%;" />

```
输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3
```

 

 

**提示：**

- 树中的节点数为 `n` 。
- `1 <= k <= n <= 104`
- `0 <= Node.val <= 104`

 

**进阶：**如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 `k` 小的值，你将如何优化算法？



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize the result and the counter
        self.result = None
        self.count = 0

        # Helper function to perform in-order traversal
        def in_order(node):
            if not node or self.result is not None:
                return
            in_order(node.left)
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            in_order(node.right)

        # Start in-order traversal from the root
        in_order(root)
        return self.result
        
```



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Helper function for inorder traversal
        def inorder(node):
            if not node:
                return None
            
            # Traverse the left subtree
            left_result = inorder(node.left)
            if left_result is not None:
                return left_result
            
            # Visit current node: if it's the kth node, return its value
            nonlocal k
            k -= 1
            if k == 0:
                return node.val
            
            # Otherwise, traverse the right subtree
            return inorder(node.right)
        
        return inorder(root)
        
```



进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？

为了优化频繁查找第 `k` 小的值的算法，可以在每个节点中维护一个额外的属性 `size`，表示以该节点为根的子树的节点总数。这样可以在对数时间内找到第 `k` 小的元素。

以下是优化后的代码：

```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.size = 1  # Initialize size of the subtree rooted at this node

class Solution:
    def updateSize(self, node: Optional[TreeNode]) -> None:
        if node:
            node.size = 1 + (node.left.size if node.left else 0) + (node.right.size if node.right else 0)

    def insert(self, root: Optional[TreeNode], val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        self.updateSize(root)
        return root

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        left_size = root.left.size if root.left else 0
        if k <= left_size:
            return self.kthSmallest(root.left, k)
        elif k == left_size + 1:
            return root.val
        else:
            return self.kthSmallest(root.right, k - left_size - 1)

# Example usage:
if __name__ == '__main__':
    root = TreeNode(5)
    solution = Solution()
    solution.insert(root, 3)
    solution.insert(root, 6)
    solution.insert(root, 2)
    solution.insert(root, 4)
    solution.insert(root, 1)
    print(solution.kthSmallest(root, 3))  # Output: 3
```

> 解释：
>
> 1. **TreeNode 类**：增加了 `size` 属性来表示以该节点为根的子树的节点总数。
> 2. **updateSize 方法**：更新节点的 `size` 属性。
> 3. **insert 方法**：插入新节点并更新 `size` 属性。
> 4. **kthSmallest 方法**：利用 `size` 属性在对数时间内找到第 `k` 小的元素。



## 236.二叉树的最近公共祖先

https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

[百度百科](https://baike.baidu.com/item/最近公共祖先/8918834?fr=aladdin)中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（**一个节点也可以是它自己的祖先**）。”

 

**示例 1：**

![img](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

```
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
```

**示例 2：**

![img](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

```
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
```

**示例 3：**

```
输入：root = [1,2], p = 1, q = 2
输出：1
```

 

**提示：**

- 树中节点数目在范围 `[2, 105]` 内。
- `-10^9 <= Node.val <= 10^9`
- 所有 `Node.val` `互不相同` 。
- `p != q`
- `p` 和 `q` 均存在于给定的二叉树中。



这是一个典型的二叉树问题，要求找到两个节点的最近公共祖先。通过深度优先搜索（DFS）的方法来解决。算法的核心思想是：

1. 从根节点开始递归遍历二叉树。
2. 如果当前节点为空，返回 `None`。
3. 如果当前节点是 `p` 或 `q`，则返回当前节点（因为节点本身也可以是自己的祖先）。
4. 对左右子树递归查找。如果左右子树都找到了 `p` 或 `q`，则当前节点就是最近公共祖先。
5. 如果左子树或右子树找到一个节点，返回那个节点。如果两个子树都返回非空节点，说明当前节点是最近公共祖先。

以下是实现代码：

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 递归终止条件
        if not root:
            return None
        if root == p or root == q:
            return root
        
        # 递归查找左右子树
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # 如果左右子树都找到了p或q，当前节点是公共祖先
        if left and right:
            return root
        
        # 如果左子树找到了p或q，返回左子树的结果，否则返回右子树的结果
        return left if left else right
```

时间复杂度：

- 每个节点最多访问一次，因此时间复杂度是 O(N)，其中 N 是树中的节点数。

空间复杂度：

- 由于递归调用的栈空间，空间复杂度是 O(H)，其中 H 是树的高度。在最坏情况下（树为链状结构），H = N；在平衡二叉树中，H = log(N)。





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



## 240.搜索二维矩阵II

https://leetcode.cn/problems/search-a-2d-matrix-ii/

编写一个高效的算法来搜索 `*m* x *n*` 矩阵 `matrix` 中的一个目标值 `target` 。该矩阵具有以下特性：

- 每行的元素从左到右升序排列。
- 每列的元素从上到下升序排列。

 

**示例 1：**

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/25/searchgrid2.jpg" alt="img" style="zoom:67%;" />

```
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
输出：true
```

**示例 2：**

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/25/searchgrid.jpg" alt="img" style="zoom:67%;" />

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



## 287.寻找重复数

二分查找，快慢指针，https://leetcode.cn/problems/find-the-duplicate-number/

给定一个包含 `n + 1` 个整数的数组 `nums` ，其数字都在 `[1, n]` 范围内（包括 `1` 和 `n`），可知至少存在一个重复的整数。

假设 `nums` 只有 **一个重复的整数** ，返回 **这个重复的数** 。

你设计的解决方案必须 **不修改** 数组 `nums` 且只用常量级 `O(1)` 的额外空间。

 

**示例 1：**

```
输入：nums = [1,3,4,2,2]
输出：2
```

**示例 2：**

```
输入：nums = [3,1,3,4,2]
输出：3
```

**示例 3 :**

```
输入：nums = [3,3,3,3,3]
输出：3
```

 

 

**提示：**

- `1 <= n <= 105`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`
- `nums` 中 **只有一个整数** 出现 **两次或多次** ，其余整数均只出现 **一次**

 

**进阶：**

- 如何证明 `nums` 中至少存在一个重复的数字?
- 你可以设计一个线性级时间复杂度 `O(n)` 的解决方案吗？



这是一个经典的“寻找重复数字”的问题，可以使用 **Floyd's Tortoise and Hare** 算法来解决，它的时间复杂度是 **O(n)**，空间复杂度是 **O(1)**。这个算法基于快慢指针的思想。

**解决思路**

1. 数组的性质：
   - 数组 `nums` 中的数字是从 `1` 到 `n` 之间的整数，长度是 `n + 1`，意味着根据鸽巢原理，至少有一个数字会重复。
2. 如何找到重复数字：
   - 我们可以将数组 `nums` 看作一个指向数组中位置的指针链。每个数字 `nums[i]` 指向数组中的位置 `nums[i]`。
   - 根据这个链的结构，可以使用类似于链表中环的检测算法，**Floyd’s Cycle Detection Algorithm (Tortoise and Hare)** 来找到重复的数字。

**Floyd's Cycle Detection Algorithm**

这个算法可以分为两个步骤：

**1. 找到相遇点**

- 使用两个指针，一个快指针（`hare`），每次移动两步；一个慢指针（`tortoise`），每次移动一步。
- 如果存在环（即重复的数字），这两个指针最终会相遇。

**2. 找到入口点**

- 一旦快慢指针相遇，将慢指针重置到数组的起始位置，然后同时移动快指针和慢指针，每次都移动一步。相遇的那个点即是重复的数字。

**代码实现**

```python
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Initialize the slow and fast pointers
        tortoise = nums[0]
        hare = nums[0]

        # Step 2: Move the tortoise and hare until they meet
        while True:
            tortoise = nums[tortoise]  # Slow pointer moves one step
            hare = nums[nums[hare]]  # Fast pointer moves two steps
            if tortoise == hare:  # They meet, meaning a cycle exists
                break

        # Step 3: Find the entrance to the cycle
        tortoise = nums[0]  # Reset tortoise to the start
        while tortoise != hare:
            tortoise = nums[tortoise]  # Move one step
            hare = nums[hare]  # Move one step

        return hare  # The duplicate number

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 3, 4, 2, 2]
    print(solution.findDuplicate(nums))  # Output: 2

    nums = [3, 1, 3, 4, 2]
    print(solution.findDuplicate(nums))  # Output: 3

    nums = [1, 1]
    print(solution.findDuplicate(nums))  # Output: 1

    nums = [1, 1, 2]
    print(solution.findDuplicate(nums))  # Output: 1
```

> **解释：**
>
> 1. **初始化**：`tortoise` 和 `hare` 都从数组的第一个元素开始。
> 2. **找环**：通过快慢指针的方式，`tortoise` 每次移动一步，`hare` 每次移动两步。当它们相遇时，证明数组中有环，即存在重复数字。
> 3. **找重复数字**：将 `tortoise` 重置到起始位置，然后和 `hare` 一起继续移动，直到它们再次相遇，那个位置就是重复的数字。
>
> **时间和空间复杂度**
>
> - **时间复杂度**：`O(n)`，因为快慢指针最多走两倍的距离，最多需要 `n` 步。
> - **空间复杂度**：`O(1)`，因为只用了两个额外的指针，空间开销是常数级别的。
>
> **进阶问题解答**
>
> 1. **如何证明 `nums` 中至少存在一个重复的数字？**
>    - 由于数组长度是 `n + 1`，而数组中的数字是从 `1` 到 `n`，根据鸽巢原理，在 `n + 1` 个位置中，只能容纳 `n` 个不同的数字，必定有至少一个数字出现多次。
> 2. **能否设计一个线性时间复杂度 `O(n)` 的解决方案？**
>    - 是的，使用上述的 Floyd’s Cycle Detection Algorithm 方法，我们能在 `O(n)` 的时间复杂度内找到重复的数字，并且使用常量级别的空间。



要解决这个问题而不修改数组 `nums` 且只使用常量级的额外空间，可以利用二分查找结合鸽巢原理来寻找重复的数字。这种方法能在满足题目要求的情况下实现线性级时间复杂度 O(n) 的解决方案。

**解决思路**

根据题意，我们知道数组 `nums` 中包含 n+1 个整数，范围从 1 到 n，并且至少有一个数字是重复的。基于这个信息，我们可以使用二分查找的方法来缩小可能的重复数字的范围：

1. **确定搜索区间**：初始时，我们的搜索区间是 `[1, n]`。
2. **计算中间值**：对于当前的搜索区间 `[low, high]`，我们计算中间值 `mid`。
3. **遍历数组统计**：遍历数组，统计数组中小于等于 `mid` 的元素个数 `count`。
4. **调整搜索区间**：
   - 如果 `count` 大于 `mid`，说明重复的数字在 `[low, mid]` 范围内。
   - 否则，重复的数字在 `[mid + 1, high]` 范围内。
5. **重复上述步骤**，直到找到重复的数字。

这种方法之所以有效是因为它利用了鸽巢原理（如果 `n` 个物品放入 `m` 个容器中，且 `n > m`，那么至少有一个容器里包含了多于一个物品），以及二分查找可以高效地缩小查找范围。

**代码实现**

```python
def findDuplicate(nums):
    low = 1
    high = len(nums) - 1
    
    while low < high:
        mid = (low + high) // 2
        count = sum(num <= mid for num in nums)
        
        if count > mid:
            high = mid
        else:
            low = mid + 1
            
    return low
```

这段代码首先定义了搜索区间的两端 `low` 和 `high`，然后进入一个循环，在循环中通过计算中间值 `mid` 并统计数组中小于等于 `mid` 的元素个数来决定如何调整搜索区间。最终当 `low` 等于 `high` 时，我们就找到了重复的数字。

这种方法的时间复杂度为 O(n log n)，因为每次都需要遍历整个数组来计算 `count`，而二分查找的过程是对数级别的。虽然这里提到希望设计一个线性级时间复杂度 O(n) 的解决方案，但实际上上述方法已经非常接近线性时间复杂度，并且满足题目对空间的要求。对于严格意义上的 O(n) 时间复杂度解法，可以考虑使用快慢指针模拟链表环检测算法（Floyd's Tortoise and Hare algorithm），但那会涉及到将数组视为一种特殊的链表结构进行处理。



> 
>
> **Floyd判圈算法** 
>
> https://blog.csdn.net/weixin_45626133/article/details/126392057
>
>  Floyd判圈算法(Floyd Cycle Detection Algorithm)，又称龟兔赛跑算法(Tortoise and Hare Algorithm)，是一个可以在有限状态机、迭代函数或者链表上判断是否存在环，求出该环的起点与长度的算法。该算法据高德纳称由美国科学家罗伯特·弗洛伊德发明，但这一算法并没有出现在罗伯特·弗洛伊德公开发表的著作中。
>  如果有限状态机、迭代函数或者链表上存在环，那么在某个环上以**不同速度**前进的2个指针必定会在某个时刻相遇。同时显然地，如果从同一个起点(即使这个起点不在某个环上)同时开始以不同速度前进的2个指针最终相遇，那么可以判定存在一个环，且可以求出二者相遇处所在的环的起点与长度。
>
> **算法描述：**
>
> **判断是否存在环路：**
>
> 如果有限状态机、迭代函数或者链表存在环，那么一定存在一个起点可以到达某个环的某处(这个起点也可以在某个环上)。
> 初始状态下，假设已知某个起点节点为节点S。现设两个指针t和h，将它们均指向S。接着，同时让t和h往前推进，但是二者的速度不同：t每前进1步，h前进2步。只要二者都可以前进而且没有相遇，就如此保持二者的推进。当h无法前进，即到达某个没有后继的节点时，就可以确定从S出发不会遇到环。反之当t与h再次相遇时，就可以确定从S出发一定会进入某个环，设其为环C。如果确定了存在某个环，就可以求此环的起点与长度。
>
> **求解环路的长度：**
> 上述算法刚判断出存在环C时，显然t和h位于同一节点，设其为节点M。显然，仅需令h不动，而t不断推进，最终又会返回节点M，统计这一次t推进的步数，显然这就是环C的长度。
>
> **求解环路的起点：**
> 为了求出环C的起点，只要令h仍均位于节点M，而令t返回起点节点S，此时h与t之间距为环C长度的整数倍。随后，同时让t和h往前推进，且保持二者的速度相同：t每前进1步，h前进1步。持续该过程直至t与h再一次相遇，设此次相遇时位于同一节点P，则节点P即为从节点S出发所到达的环C的第一个节点，即环C的一个起点。
>
> **对于环路起点算法的解释：**
>
> ![img](https://i-blog.csdnimg.cn/blog_migrate/364cbe6d5543e1778484bbc3a39851f9.png)
>
> 假设出发起点到环起点的距离为m，已经确定有环，环的周长为n，（第一次）相遇点距离环的起点的距离是k。那么当两者相遇时，慢指针（t）移动的总距离i = m + a * n + k，快指针（h）的移动距离为2i，2i = m + b * n + k。其中，a和b分别为t和h在第一次相遇时转过的圈数。让两者相减（快减慢），那么有i = (b - a) * n。即i是圈长度的倍数。
> 将一个指针移到出发起点S，另一个指针仍呆在相遇节点M处两者同时移动，每次移动一步。当第一个指针前进了m，即到达环起点时，另一个指针距离链表起点为i + m。考虑到i为圈长度的倍数，可以理解为指针从链表起点出发，走到环起点，然后绕环转了几圈，所以第二个指针也必然在环的起点。即两者相遇点就是环的起点。
>
> 
>
> 
>
> 【287. 寻找重复数（龟兔赛跑算法）】快慢指针判断是否有环
>
> https://blog.csdn.net/qq_45955883/article/details/124151777
>
>
> 【龟兔赛跑算法】快慢指针判断是否有环
>
> ![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/2a2b0890e78036fb6de0e17c72c4fc93.png)
>
> 对于慢指针，走过的路程为 a + b
> 对于快指针，走过的路程为 a + nL + b,其中 L代表环的长度
> 由于快指针的速度是慢指针的2倍
> 因此 2(a + b) = a + nL + b
> 即：
> a = nL + b
> =(n−1)L + (L−b)
> =(n−1)L + c
> 上面的式子代表什么意思呢？
> 意思是，如果从一个点从起点出发，令一个点在相遇点出发，那么二者必相遇，并且相遇点为环的入口处。
> 时间复杂度为 O(n)，空间复杂度为 O(1)
>
> 



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



## 347.前K个高频元素

桶排序，堆，https://leetcode.cn/problems/top-k-frequent-elements/

为了满足题目要求，即时间复杂度优于 O(n log n)，我们可以使用一个基于桶排序的方法来解决这个问题。这种方法的时间复杂度为 O(n)，因为我们遍历了输入数组两次，并且对固定数量的桶进行了处理。

下面是具体的实现步骤：

1. 使用一个哈希表（字典）统计每个数字出现的频率。
2. 创建一系列的“桶”，每个桶对应一种出现频率。将每个数字放入相应频率的桶中。
3. 从最高频率开始，从桶中取出前 k 个高频元素。

以下是 Python 实现代码：3ms，击败93.39%

```python
from collections import defaultdict, Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 统计每个数字出现的次数
        count = Counter(nums)

        # 按照出现的频率分桶
        buckets = defaultdict(list)
        for num, freq in count.items():
            buckets[freq].append(num)

        # 收集结果
        res = []
        for freq in range(len(nums), 0, -1):  # 从最高的频率开始收集
            if freq in buckets:
                res += buckets[freq]
                if len(res) >= k:  # 如果已经收集到足够的元素，则停止
                    break

        return res[:k]


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(s.topKFrequent(nums, k))  # 输出：[1, 2]
```

> 解释：
>
> - **`Counter`**：首先使用 `Counter` 来统计每个数字出现的次数，这一步时间复杂度是 O(n)。
> - **桶排序**：然后创建一系列桶，其中索引代表出现频率，值是一个列表，包含所有具有该频率的数字。通过遍历 `count` 字典并将每个数字放入相应的桶中完成这一过程。
> - **收集结果**：最后，我们从最大可能的频率开始（即数组长度），依次向较低频率检查并添加对应的数字到结果列表中，直到收集到了 k 个元素为止。
>
> 这种方法确保了我们可以在 O(n) 时间复杂度内找到前 k 个高频元素，符合题目要求。



```python
import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 统计每个数字出现的次数
        count = Counter(nums)

        # 使用最小堆来保存频率最高的k个元素
        min_heap = []
        for num, freq in count.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, num))
            else:
                # 如果当前元素的频率大于堆顶元素的频率，则替换堆顶元素
                if freq > min_heap[0][0]:
                    heapq.heapreplace(min_heap, (freq, num))

        # 提取堆中的元素，并只返回数字部分
        return [x[1] for x in min_heap]


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(s.topKFrequent(nums, k))  # 输出：[1, 2]

```

> 使用堆（Heap）来解决这个问题也是一个非常有效的方法。我们可以利用 Python 的 heapq 模块来创建一个最小堆，从而保持前 K 个高频元素。这种方法的时间复杂度为 O(n log k)，其中 n 是数组的长度，k 是需要返回的高频元素的数量。虽然这比桶排序的 O(n) 方法稍微慢一些，但在很多实际情况下依然非常高效。这种方法不仅简洁，而且在处理大数据集时也能保证较好的性能。



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





## 394.字符串解码

stack, https://leetcode.cn/problems/decode-string/

给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: `k[encoded_string]`，表示其中方括号内部的 `encoded_string` 正好重复 `k` 次。注意 `k` 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 `k` ，例如不会出现像 `3a` 或 `2[4]` 的输入。

 

**示例 1：**

```
输入：s = "3[a]2[bc]"
输出："aaabcbc"
```

**示例 2：**

```
输入：s = "3[a2[c]]"
输出："accaccacc"
```

**示例 3：**

```
输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"
```

**示例 4：**

```
输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"
```

 

**提示：**

- `1 <= s.length <= 30`
- `s` 由小写英文字母、数字和方括号 `'[]'` 组成
- `s` 保证是一个 **有效** 的输入。
- `s` 中所有整数的取值范围为 `[1, 300]` 



```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
                continue
            
            sub_s = []
            while stack[-1] != '[':
                sub_s.append(stack.pop())
            stack.pop()
            sub_s = ''.join(sub_s[::-1])

            freq = []
            while stack and stack[-1].isdigit():
                freq.append(stack.pop())
            
            freq = int(''.join(freq[::-1]))
            
            stack.append(sub_s * freq)
        
        return ''.join(stack)
```



您的代码已经很好地实现了字符串解码的功能，但我们可以进行一些优化来提高代码的可读性和效率。下面是经过优化后的版本：

```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_string = ""
        
        for char in s:
            if char.isdigit():
                # 当前字符是数字时，更新当前的数字
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # 遇到'['时，将当前的数字和字符串压入栈，并重置变量
                stack.append((current_string, current_num))
                current_string, current_num = "", 0
            elif char == ']':
                # 遇到']'时，从栈中弹出，并根据保存的数字重复当前字符串
                prev_string, num = stack.pop()
                current_string = prev_string + current_string * num
            else:
                # 普通字符直接添加到当前字符串
                current_string += char
                
        return current_string
```

主要改进点：

1. **减少字符串操作次数**：原版代码在遇到`]`时，通过不断弹出栈顶元素来构建子串，然后反转拼接。新版本直接使用一个变量存储当前构建的字符串，减少了多次字符串操作带来的开销。
2. **简化频率解析逻辑**：新版直接在遍历过程中计算数字（频率），而不是通过额外的循环来解析栈中的数字。
3. **提高可读性**：通过明确区分处理数字、`[`、`]`和其他字符的不同逻辑块，使代码更易读。

这样的改动不仅提升了代码执行效率，也使得代码结构更加清晰，便于理解和维护。





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



## 437.路径总和III

dfs, https://leetcode.cn/problems/path-sum-iii/

给定一个二叉树的根节点 `root` ，和一个整数 `targetSum` ，求该二叉树里节点值之和等于 `targetSum` 的 **路径** 的数目。

**路径** 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

 

**示例 1：**

<img src="https://assets.leetcode.com/uploads/2021/04/09/pathsum3-1-tree.jpg" alt="img" style="zoom:67%;" />

```
输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条，如图所示。
```

**示例 2：**

```
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3
```

 

**提示:**

- 二叉树的节点个数的范围是 `[0,1000]`
- `-109 <= Node.val <= 109` 
- `-1000 <= targetSum <= 1000` 





```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, current_path_sums):
            if not node:
                return 0
            
            # 更新当前路径上的所有可能的和
            new_path_sums = [node.val + sums for sums in current_path_sums]
            new_path_sums.append(node.val)  # 单独考虑以当前节点为起点的路径
            
            # 计算满足条件的路径数量
            count = new_path_sums.count(targetSum)
            
            # 递归遍历左右子树
            count += dfs(node.left, new_path_sums)
            count += dfs(node.right, new_path_sums)
            
            return count
        
        return dfs(root, [])

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



## 541.反转字符串II

https://leetcode.cn/problems/reverse-string-ii/

给定一个字符串 `s` 和一个整数 `k`，从字符串开头算起，每计数至 `2k` 个字符，就反转这 `2k` 字符中的前 `k` 个字符。

- 如果剩余字符少于 `k` 个，则将剩余字符全部反转。
- 如果剩余字符小于 `2k` 但大于或等于 `k` 个，则反转前 `k` 个字符，其余字符保持原样。

 

**示例 1：**

```
输入：s = "abcdefg", k = 2
输出："bacdfeg"
```

**示例 2：**

```
输入：s = "abcd", k = 2
输出："bacd"
```

 

**提示：**

- `1 <= s.length <= 104`
- `s` 仅由小写英文组成
- `1 <= k <= 104`



```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)  # 将字符串转为列表，方便修改字符
        n = len(s)
        
        for i in range(0, n, 2 * k):
            # 判断剩余字符的长度
            if i + k <= n:
                s[i:i+k] = reversed(s[i:i+k])  # 反转前 k 个字符
            else:
                s[i:n] = reversed(s[i:n])  # 剩余字符少于 k 个，直接反转
            
        return ''.join(s)  # 将列表转换回字符串
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



## 739.每日温度

单调栈，https://leetcode.cn/problems/daily-temperatures/

给定一个整数数组 `temperatures` ，表示每天的温度，返回一个数组 `answer` ，其中 `answer[i]` 是指对于第 `i` 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 `0` 来代替。

 

**示例 1:**

```
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
```

**示例 2:**

```
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]
```

**示例 3:**

```
输入: temperatures = [30,60,90]
输出: [1,1,0]
```

 

**提示：**

- `1 <= temperatures.length <= 105`
- `30 <= temperatures[i] <= 100`



```python
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        dp = [0] * n  # 初始化结果列表，默认值为0，表示没有找到更高温度
        stack = []  # 使用栈来保存温度的索引
        
        for i in range(n):
            # 当当前温度大于栈顶索引对应的温度时，说明找到了比栈顶索引那天更高的温度
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                dp[prev_index] = i - prev_index  # 计算天数差
            
            # 将当前温度的索引压入栈
            stack.append(i)
        
        return dp
```



## 763.划分字母区间

greedy, https://leetcode.cn/problems/partition-labels/

给你一个字符串 `s` 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。

注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 `s` 。

返回一个表示每个字符串片段的长度的列表。

 

**示例 1：**

```
输入：s = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。 
```

**示例 2：**

```
输入：s = "eccbbbbdec"
输出：[10]
```

 

**提示：**

- `1 <= s.length <= 500`
- `s` 仅由小写英文字母组成

 



```python
from collections import defaultdict
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        char_indices = defaultdict(list)  # 存储每个字符的所有索引

        for i in range(n):
            char_indices[s[i]].append(i)

        segments = []  # 存储合并后的区间
        for _, indices in char_indices.items():
            if len(indices) >= 2:
                segments.append([min(indices), max(indices)])
            segments.append([indices[0], indices[0]])

        partition_sizes = []  # 存储最终的分割长度
        start = 0
        end = segments[0][1]

        for i in range(1, len(segments)):
            if segments[i][0] > end:
                partition_sizes.append(end - start + 1)
                start = segments[i][0]
                end = segments[i][1]
            else:
                end = max(end, segments[i][1])

        if n - sum(partition_sizes) > 0:
            partition_sizes.append(n - sum(partition_sizes))

        return partition_sizes

```



```python
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}  # 记录每个字符的最远出现位置
        ans = []
        start, right = 0, 0  # `start` 记录每个分割区间的起始点，`right` 记录当前区间最远端

        for i, c in enumerate(s):
            right = max(right, last[c])  # 更新当前区间最远端
            if i == right:  # 当前索引 `i` 到达最远端，形成一个独立分区
                ans.append(i - start + 1)
                start = i + 1  # 更新起点，开始新的区间

        return ans

```

> **优化点**
>
> 1. `last = {c: i for i, c in enumerate(s)}`
>    - 直接记录 **每个字符的最右索引**，避免存储整个索引列表，减少 **空间复杂度**。
> 2. 遍历 `s` 计算区间
>    - 维护 `right` 作为当前区间的最远端。
>    - 遍历字符串 `s` 时，动态更新 `right`。
>    - 当 `i == right` 时，表示当前区间可以分割，存入 `ans`。
> 3. 只遍历 `s` 一次 (`O(n)`)
>    - 不需要额外排序 `segs`，也不需要 `sum(ans)` 计算剩余部分，直接使用 `start` 记录区间起始点。



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

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/16/q3v1.jpg" alt="img" style="zoom:67%;" />

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



## 1561.你可以获得的最大硬币数目

https://leetcode.cn/problems/maximum-number-of-coins-you-can-get/

有 3n 堆数目不一的硬币，你和你的朋友们打算按以下方式分硬币：

- 每一轮中，你将会选出 **任意** 3 堆硬币（不一定连续）。
- Alice 将会取走硬币数量最多的那一堆。
- 你将会取走硬币数量第二多的那一堆。
- Bob 将会取走最后一堆。
- 重复这个过程，直到没有更多硬币。

给你一个整数数组 `piles` ，其中 `piles[i]` 是第 `i` 堆中硬币的数目。

返回你可以获得的最大硬币数目。

 

**示例 1：**

```
输入：piles = [2,4,1,2,7,8]
输出：9
解释：选出 (2, 7, 8) ，Alice 取走 8 枚硬币的那堆，你取走 7 枚硬币的那堆，Bob 取走最后一堆。
选出 (1, 2, 4) , Alice 取走 4 枚硬币的那堆，你取走 2 枚硬币的那堆，Bob 取走最后一堆。
你可以获得的最大硬币数目：7 + 2 = 9.
考虑另外一种情况，如果选出的是 (1, 2, 8) 和 (2, 4, 7) ，你就只能得到 2 + 4 = 6 枚硬币，这不是最优解。
```

**示例 2：**

```
输入：piles = [2,4,5]
输出：4
```

**示例 3：**

```
输入：piles = [9,8,7,6,5,1,2,3,4]
输出：18
```

 

**提示：**

- `3 <= piles.length <= 10^5`
- `piles.length % 3 == 0`
- `1 <= piles[i] <= 10^4`



```python
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        from collections import deque
        piles.sort()
        q = deque(piles)
        cnt = 0
        for i in range(len(piles)//3):
            q.popleft()
            q.pop()
            cnt += q.pop()
        return cnt
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



## 2944.购买水果需要的最少金币数

dp, https://leetcode.cn/problems/minimum-number-of-coins-for-fruits/

给你一个 **下标从 1 开始的** 整数数组 `prices` ，其中 `prices[i]` 表示你购买第 `i` 个水果需要花费的金币数目。

水果超市有如下促销活动：

- 如果你花费 `prices[i]` 购买了下标为 `i` 的水果，那么你可以免费获得下标范围在 `[i + 1, i + i]` 的水果。

**注意** ，即使你 **可以** 免费获得水果 `j` ，你仍然可以花费 `prices[j]` 个金币去购买它以获得它的奖励。

请你返回获得所有水果所需要的 **最少** 金币数。

 

**示例 1：**

**输入：**prices = [3,1,2]

**输出：**4

**解释：**

- 用 `prices[0] = 3` 个金币购买第 1 个水果，你可以免费获得第 2 个水果。
- 用 `prices[1] = 1` 个金币购买第 2 个水果，你可以免费获得第 3 个水果。
- 免费获得第 3 个水果。

请注意，即使您可以免费获得第 2 个水果作为购买第 1 个水果的奖励，但您购买它是为了获得其奖励，这是更优化的。

**示例 2：**

**输入：**prices = [1,10,1,1]

**输出：**2

**解释：**

- 用 `prices[0] = 1` 个金币购买第 1 个水果，你可以免费获得第 2 个水果。
- 免费获得第 2 个水果。
- 用 `prices[2] = 1` 个金币购买第 3 个水果，你可以免费获得第 4 个水果。
- 免费获得第 4 个水果。

**示例 3：**

**输入：**prices = [26,18,6,12,49,7,45,45]

**输出：**39

**解释：**

- 用 `prices[0] = 26` 个金币购买第 1 个水果，你可以免费获得第 2 个水果。
- 免费获得第 2 个水果。
- 用 `prices[2] = 6` 个金币购买第 3 个水果，你可以免费获得第 4，5，6（接下来的三个）水果。
- 免费获得第 4 个水果。
- 免费获得第 5 个水果。
- 用 `prices[5] = 7` 个金币购买第 6 个水果，你可以免费获得第 7 和 第 8 个水果。
- 免费获得第 7 个水果。
- 免费获得第 8 个水果。

请注意，即使您可以免费获得第 6 个水果作为购买第 3 个水果的奖励，但您购买它是为了获得其奖励，这是更优化的。

 

**提示：**

- `1 <= prices.length <= 1000`
- `1 <= prices[i] <= 10^5`



```python
class Solution:
    def minimumCoins(self, prices):
        length = len(prices)
        dp = [float('inf')] * (length + 1)
        dp[0] = 0
        for i in range(1, length + 1):
            r = min(length, i + i)
            for j in range(i, r + 1):
                dp[j] = min(dp[j], dp[i - 1] + prices[i - 1])
        return dp[length]
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

> 输入：s = "baeyh", k = 2
> 输出：2
> 解释：字符串 s 中有 2 个美丽子字符串。
>
> - 子字符串 "b**aeyh**"，vowels = 2（["a","e"]），consonants = 2（["y","h"]）。
> 可以看出字符串 "aeyh" 是美丽字符串，因为 vowels == consonants 且 vowels * consonants % k == 0 。
> - 子字符串 "**baey**h"，vowels = 2（["a","e"]），consonants = 2（["b","y"]）。
> 可以看出字符串 "baey" 是美丽字符串，因为 vowels == consonants 且 vowels * consonants % k == 0 。
> 可以证明字符串 s 中只有 2 个美丽子字符串。



**示例 2：**

> 输入：s = "abba", k = 1
> 输出：3
> 解释：字符串 s 中有 3 个美丽子字符串。
>
> - 子字符串 "**ab**ba"，vowels = 1（["a"]），consonants = 1（["b"]）。
> - 子字符串 "ab**ba**"，vowels = 1（["a"]），consonants = 1（["b"]）。
> - 子字符串 "**abba**"，vowels = 2（["a","a"]），consonants = 2（["b","b"]）。
> 可以证明字符串 s 中只有 3 个美丽子字符串。

**示例 3：**

> 输入：s = "bcdf", k = 1
> 输出：0
> 解释：字符串 s 中没有美丽子字符串。

 

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



## 3433.统计用户被提及情况

implementation, https://leetcode.cn/problems/count-mentions-per-user/d

给你一个整数 `numberOfUsers` 表示用户总数，另有一个大小为 `n x 3` 的数组 `events` 。

每个 `events[i]` 都属于下述两种类型之一：

1. 消息事件（Message Event）：

   ```
   ["MESSAGE", "timestampi", "mentions_stringi"]
   ```

   - 事件表示在 `timestampi` 时，一组用户被消息提及。

   - ```
     mentions_stringi
     ```

      字符串包含下述标识符之一：

     - `id<number>`：其中 `<number>` 是一个区间 `[0,numberOfUsers - 1]` 内的整数。可以用单个空格分隔 **多个** id ，并且 id 可能重复。此外，这种形式可以提及离线用户。
     - `ALL`：提及 **所有** 用户。
     - `HERE`：提及所有 **在线** 用户。

2. 离线事件（Offline Event）：

   ```
   ["OFFLINE", "timestampi", "idi"]
   ```

   - 事件表示用户 `idi` 在 `timestampi` 时变为离线状态 **60 个单位时间**。用户会在 `timestampi + 60` 时自动再次上线。

返回数组 `mentions` ，其中 `mentions[i]` 表示  id 为  `i` 的用户在所有 `MESSAGE` 事件中被提及的次数。

最初所有用户都处于在线状态，并且如果某个用户离线并在此上线，其对应的状态变更将会在所有相同时间发生的消息事件之前进行处理和同步。

**注意** 在单条消息中，同一个用户可能会被提及多次。每次提及都需要被 **分别** 统计。

 

**示例 1：**

**输入：**numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]

**输出：**[2,2]

**解释：**

最初，所有用户都在线。

时间戳 10 ，`id1` 和 `id0` 被提及，`mentions = [1,1]`

时间戳 11 ，`id0` **离线** 。

时间戳 71 ，`id0` 再次 **上线** 并且 `"HERE"` 被提及，`mentions = [2,2]`

**示例 2：**

**输入：**numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]

**输出：**[2,2]

**解释：**

最初，所有用户都在线。

时间戳 10 ，`id1` 和 `id0` 被提及，`mentions = [1,1]`

时间戳 11 ，`id0` **离线** 。

时间戳 12 ，`"ALL"` 被提及。这种方式将会包括所有离线用户，所以 `id0` 和 `id1` 都被提及，`mentions = [2,2]`

**示例 3：**

**输入：**numberOfUsers = 2, events = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]

**输出：**[0,1]

**解释：**

最初，所有用户都在线。

时间戳 10 ，`id0` **离线** **。**

时间戳 12 ，`"HERE"` 被提及。由于 `id0` 仍处于离线状态，其将不会被提及，`mentions = [0,1]`

 

**提示：**

- `1 <= numberOfUsers <= 100`
- `1 <= events.length <= 100`
- `events[i].length == 3`
- `events[i][0]` 的值为 `MESSAGE` 或 `OFFLINE` 。
- `1 <= int(events[i][1]) <= 105`
- 在任意 `"MESSAGE"` 事件中，以 `id<number>` 形式提及的用户数目介于 `1` 和 `100` 之间。
- `0 <= <number> <= numberOfUsers - 1`
- 题目保证 `OFFLINE` 引用的用户 id 在事件发生时处于 **在线** 状态。



时间相同时候，先处理OFFLINE。

```python
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda x: (int(x[1]), -ord(x[0][0])))
        d = [0] * numberOfUsers
        online_status = [1] * numberOfUsers
        offline_events = []
        for event in events:
            event_type, timestamp, data = event
            
            timestamp = int(timestamp)
            while offline_events and offline_events[0][0] <= timestamp:
                _, user_id = heapq.heappop(offline_events)
                online_status[user_id] = 1
                 
            if event_type == "MESSAGE":
                if data == "ALL":
                    for i in range(numberOfUsers):
                        d[i] += 1
                elif data == "HERE":
                    for i in range(numberOfUsers):
                        if online_status[i]:
                            d[i] += 1
                else:
                    ids = data.split()
                    for user_id in ids:
                        d[int(user_id[2:])] += 1

            elif event_type == "OFFLINE":
                user_id = int(data)
                online_status[user_id] = 0
                heapq.heappush(offline_events, (timestamp + 60, user_id))
                
                
        return d
                 
```



## 3434.子数组操作后的最大频率

Kadane, https://leetcode.cn/problems/maximum-frequency-after-subarray-operation/

给你一个长度为 `n` 的数组 `nums` ，同时给你一个整数 `k` 。

你可以对 `nums` 执行以下操作 **一次** ：

- 选择一个子数组 `nums[i..j]` ，其中 `0 <= i <= j <= n - 1` 。
- 选择一个整数 `x` 并将 `nums[i..j]` 中 **所有** 元素都增加 `x` 。

请你返回执行以上操作以后数组中 `k` 出现的 **最大** 频率。

**子数组** 是一个数组中一段连续 **非空** 的元素序列。

 

**示例 1：**

**输入：**nums = [1,2,3,4,5,6], k = 1

**输出：**2

**解释：**

将 `nums[2..5]` 增加 -5 后，1 在数组 `[1, 2, -2, -1, 0, 1]` 中的频率为最大值 2 。

**示例 2：**

**输入：**nums = [10,2,3,4,5,5,4,3,2,2], k = 10

**输出：**4

**解释：**

将 `nums[1..9]` 增加 8 以后，10 在数组 `[10, 10, 11, 12, 13, 13, 12, 11, 10, 10]` 中的频率为最大值 4 。

 

**提示：**

- `1 <= n == nums.length <= 105`
- `1 <= nums[i] <= 50`
- `1 <= k <= 50`



```python
class Solution:
    def maxFrequency(self, nums, k):
        # 计算初始的 k 出现次数
        totalK = nums.count(k)
        
        maxExtra = 0
        # 遍历所有可能的增益 (从 -k 到 50 - k)
        for x in range(-k, 51 - k):
            currentSum = 0
            maxSum = 0
            # 遍历数组，计算增益
            for num in nums:
                if num == k + x:
                    currentSum += 1  # 非k元素贡献 +1
                if num == k:
                    currentSum -= 1  # k元素贡献 -1
                if currentSum < 0:
                    currentSum = 0  # 如果增益为负数，重置
                maxSum = max(currentSum, maxSum)  # 更新当前最大增益
            
            maxExtra = max(maxSum, maxExtra)  # 更新最大增益
        
        # 返回最终结果：原有的 k 的频率 + 最大增益
        return totalK + maxExtra

```



实际上是找连续子串中相同元素最多的。结合 Kadane 算法来做：

【Attention】：遍历数组，统计 k 的初始出现次数 kFreq，并收集所有非 k 元素到一个 set 中。
对于每个非 k 元素 nonKNum，使用 Kadane 算法 计算其对应的最大增益子数组。增益子数组的贡献规则为：nonKNum 出现时贡献 +1，k 出现时贡献 -1，其他元素不影响。
维护当前最大增益值 maxGain，遍历所有非 k 元素后，得到最大增益。
最终结果为 kFreq + maxGain。

```python
class Solution:
    def maxFrequency(self, nums, k):
        # 计算k在nums中的频率
        k_freq = nums.count(k)
        
        # 使用集合来存储不是k的数字
        non_k_nums = set(num for num in nums if num != k)
        
        max_gain = 0
        
        for non_k_num in non_k_nums:
            cur_max = 0
            max_subarray = 0
            for num in nums:
                if num == non_k_num:
                    cur_max += 1
                elif num == k:
                    cur_max -= 1
                
                max_subarray = max(max_subarray, cur_max)
                if cur_max < 0:
                    cur_max = 0
            
            max_gain = max(max_gain, max_subarray)
        
        return k_freq + max_gain
```



```c++
class Solution {
   public:
    int maxFrequency(vector<int>& nums, int k) {
        int kFreq = 0;
        unordered_set<int> nonKNums;
        for (int num : nums) {
            if (num == k) {
                kFreq++;
            } else {
                nonKNums.insert(num);
            }
        }

        int maxGain = 0;

        for (int nonKNum : nonKNums) {
            int curMax = 0;
            int maxSubarray = 0;
            for (int num : nums) {
                if (num == nonKNum) {
                    curMax += 1;
                } else if (num == k) {
                    curMax -= 1;
                }

                maxSubarray = max(maxSubarray, curMax);
                if (curMax < 0) {
                    curMax = 0;
                }
            }
            maxGain = max(maxGain, maxSubarray);
        }

        return kFreq + maxGain;
    }
};
```



## 3439.重新安排会议得到最多的空余时间I

滑动窗口，https://leetcode.cn/problems/reschedule-meetings-for-maximum-free-time-i/

给你一个整数 `eventTime` 表示一个活动的总时长，这个活动开始于 `t = 0` ，结束于 `t = eventTime` 。

同时给你两个长度为 `n` 的整数数组 `startTime` 和 `endTime` 。它们表示这次活动中 `n` 个时间 **没有重叠** 的会议，其中第 `i` 个会议的时间为 `[startTime[i], endTime[i]]` 。

你可以重新安排 **至多** `k` 个会议，安排的规则是将会议时间平移，且保持原来的 **会议时长** ，你的目的是移动会议后 **最大化** 相邻两个会议之间的 **最长** 连续空余时间。

移动前后所有会议之间的 **相对** 顺序需要保持不变，而且会议时间也需要保持互不重叠。

请你返回重新安排会议以后，可以得到的 **最大** 空余时间。

**注意**，会议 **不能** 安排到整个活动的时间以外。

 

**示例 1：**

**输入：**eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5]

**输出：**2

**解释：**

![img](https://assets.leetcode.com/uploads/2024/12/21/example0_rescheduled.png)

将 `[1, 2]` 的会议安排到 `[2, 3]` ，得到空余时间 `[0, 2]` 。

**示例 2：**

**输入：**eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10]

**输出：**6

**解释：**

![img](https://assets.leetcode.com/uploads/2024/12/21/example1_rescheduled.png)

将 `[2, 4]` 的会议安排到 `[1, 3]` ，得到空余时间 `[3, 9]` 。

**示例 3：**

**输入：**eventTime = 5, k = 2, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]

**输出：**0

**解释：**

活动中的所有时间都被会议安排满了。

 

**提示：**

- `1 <= eventTime <= 109`
- `n == startTime.length == endTime.length`
- `2 <= n <= 105`
- `1 <= k <= n`
- `0 <= startTime[i] < endTime[i] <= eventTime`
- `endTime[i] <= startTime[i + 1]` 其中 `i` 在范围 `[0, n - 2]` 之间。



```python
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: list[int], endTime: list[int]) -> int:
        n = len(startTime)
        diffs = [startTime[0]]  # 活动开始到第一个会议的空闲时间
        for i in range(1, n):
            diffs.append(startTime[i] - endTime[i - 1])  # 相邻会议之间的空闲时间
        diffs.append(eventTime - endTime[n - 1])  # 最后一个会议结束到活动结束的空闲时间
        
        cur = 0
        res = 0
        for i in range(k + 1):
            cur += diffs[i]
        res = cur
        for i in range(k + 1, n + 1):
            cur = cur + diffs[i] - diffs[i - k - 1]
            res = max(res, cur)
        
        return res
```



## 3440.重新安排会议得到最多空余时间II

implementation, https://leetcode.cn/problems/reschedule-meetings-for-maximum-free-time-ii/

给你一个整数 `eventTime` 表示一个活动的总时长，这个活动开始于 `t = 0` ，结束于 `t = eventTime` 。

同时给你两个长度为 `n` 的整数数组 `startTime` 和 `endTime` 。它们表示这次活动中 `n` 个时间 **没有重叠** 的会议，其中第 `i` 个会议的时间为 `[startTime[i], endTime[i]]` 。

你可以重新安排 **至多** 一个会议，安排的规则是将会议时间平移，且保持原来的 **会议时长** ，你的目的是移动会议后 **最大化** 相邻两个会议之间的 **最长** 连续空余时间。

请你返回重新安排会议以后，可以得到的 **最大** 空余时间。

**注意**，会议 **不能** 安排到整个活动的时间以外，且会议之间需要保持互不重叠。

**注意：**重新安排会议以后，会议之间的顺序可以发生改变。

 

**示例 1：**

**输入：**eventTime = 5, startTime = [1,3], endTime = [2,5]

**输出：**2

**解释：**

![img](https://assets.leetcode.com/uploads/2024/12/22/example0_rescheduled.png)

将 `[1, 2]` 的会议安排到 `[2, 3]` ，得到空余时间 `[0, 2]` 。

**示例 2：**

**输入：**eventTime = 10, startTime = [0,7,9], endTime = [1,8,10]

**输出：**7

**解释：**

![img](https://assets.leetcode.com/uploads/2024/12/22/rescheduled_example0.png)

将 `[0, 1]` 的会议安排到 `[8, 9]` ，得到空余时间 `[0, 7]` 。

**示例 3：**

**输入：**eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10]

**输出：**6

**解释：**

**![img](https://assets.leetcode.com/uploads/2025/01/28/image3.png)**

将 `[3, 4]` 的会议安排到 `[8, 9]` ，得到空余时间 `[1, 7]` 。

**示例 4：**

**输入：**eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]

**输出：**0

**解释：**

活动中的所有时间都被会议安排满了。

 

**提示：**

- `1 <= eventTime <= 10^9`
- `n == startTime.length == endTime.length`
- `2 <= n <= 10^5`
- `0 <= startTime[i] < endTime[i] <= eventTime`
- `endTime[i] <= startTime[i + 1]` 其中 `i` 在范围 `[0, n - 2]` 之间。





提示 1

If we reschedule a meeting earlier or later, we need to find a gap of length at least `endTime[i] - startTime[i]`. Try maintaining the gaps in some sorted data structure.

```python
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: list[int], endTime: list[int]) -> int:
        n = len(startTime)
        
        # 计算每个会议左侧可利用的最大空闲时间
        lRoom = [0] * n
        lRoom[0] = startTime[0]
        for i in range(1, n):
            lRoom[i] = max(lRoom[i - 1], startTime[i] - endTime[i - 1])
        
        # 计算每个会议右侧可利用的最大空闲时间
        rRoom = [0] * n
        rRoom[n - 1] = eventTime - endTime[n - 1]
        for i in range(n - 2, -1, -1):
            rRoom[i] = max(rRoom[i + 1], startTime[i + 1] - endTime[i])
        
        res = 0
        for i in range(n):
            # 左侧和右侧的时间点
            lTime = 0 if i == 0 else endTime[i - 1]
            rTime = eventTime if i == n - 1 else startTime[i + 1]
            
            # 当前会议的长度
            length = endTime[i] - startTime[i]
            
            # 更新最大空闲时间
            res = max(res, rTime - lTime - length)
            
            # 如果当前会议不是第一个会议，检查是否可以利用左侧的空闲时间
            if i > 0 and lRoom[i - 1] >= length:
                res = max(res, rTime - lTime)
            
            # 如果当前会议不是最后一个会议，检查是否可以利用右侧的空闲时间
            if i < n - 1 and rRoom[i + 1] >= length:
                res = max(res, rTime - lTime)
        
        return res
```



## 3443.K次修改后的最大曼哈顿距离

greedy, https://leetcode.cn/problems/maximum-manhattan-distance-after-k-changes/

给你一个由字符 `'N'`、`'S'`、`'E'` 和 `'W'` 组成的字符串 `s`，其中 `s[i]` 表示在无限网格中的移动操作：

- `'N'`：向北移动 1 个单位。
- `'S'`：向南移动 1 个单位。
- `'E'`：向东移动 1 个单位。
- `'W'`：向西移动 1 个单位。

初始时，你位于原点 `(0, 0)`。你 **最多** 可以修改 `k` 个字符为任意四个方向之一。

请找出在 **按顺序** 执行所有移动操作过程中的 **任意时刻** ，所能达到的离原点的 **最大曼哈顿距离** 。

**曼哈顿距离** 定义为两个坐标点 `(xi, yi)` 和 `(xj, yj)` 的横向距离绝对值与纵向距离绝对值之和，即 `|xi - xj| + |yi - yj|`。

 

**示例 1：**

**输入：**s = "NWSE", k = 1

**输出：**3

**解释：**

将 `s[2]` 从 `'S'` 改为 `'N'` ，字符串 `s` 变为 `"NWNE"` 。

| 移动操作    | 位置 (x, y) | 曼哈顿距离 | 最大值 |
| ----------- | ----------- | ---------- | ------ |
| s[0] == 'N' | (0, 1)      | 0 + 1 = 1  | 1      |
| s[1] == 'W' | (-1, 1)     | 1 + 1 = 2  | 2      |
| s[2] == 'N' | (-1, 2)     | 1 + 2 = 3  | 3      |
| s[3] == 'E' | (0, 2)      | 0 + 2 = 2  | 3      |

执行移动操作过程中，距离原点的最大曼哈顿距离是 3 。

**示例 2：**

**输入：**s = "NSWWEW", k = 3

**输出：**6

**解释：**

将 `s[1]` 从 `'S'` 改为 `'N'` ，将 `s[4]` 从 `'E'` 改为 `'W'` 。字符串 `s` 变为 `"NNWWWW"` 。

执行移动操作过程中，距离原点的最大曼哈顿距离是 6 。

 

**示例 3：**

输入：s ="SN", k =0

输出:  1

解释：

因为SN两个方向会互相抵消，所以最大是1。此外，WE也会互相抵消。



**提示：**

- `1 <= s.length <= 10^5`
- `0 <= k <= s.length`
- `s` 仅由 `'N'`、`'S'`、`'E'` 和 `'W'` 。





思路：贪心法，是尽量修改K次为两个方向不能互相抵消的两个字符。



思路：统计每个方向出现频次，找出最大两个频次。如果这两个不是互相抵消的方向，就尽量修改其他方向K次为这两个方向。如果这两个方向是互相抵消的，就修改次小频次的方向为频次大的方向，即每次距离+2;如果K还没有用完，再考虑修改其他方向。



```python
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        # 初始化计数器和答案
        ce = cw = cn = cs = ans = 0
        
        for i, ch in enumerate(s):
            # 更新对应方向的计数
            if ch == "N": cn += 1
            elif ch == "S": cs += 1
            elif ch == "E": ce += 1
            else: cw += 1
            
            # 计算东西向和南北向的净位移
            bx = abs(ce - cw)
            by = abs(cn - cs)
            
            # 可抵消的最小步数
            px = min(ce, cw)
            py = min(cn, cs)
            
            # 计算基础距离加上最多k次转换后能增加的距离
            base = bx + by
            additional = min(k, px + py) * 2
            cand = base + additional
            
            # 更新最大距离，同时考虑当前索引i+1（因为enumerate从0开始）
            ans = max(ans, min(i + 1, cand))
        
        return ans
```





# 困难



## 4.寻找两个正序数组的中位数

binary search, https://leetcode.cn/problems/median-of-two-sorted-arrays/

给定两个大小分别为 `m` 和 `n` 的正序（从小到大）数组 `nums1` 和 `nums2`。请你找出并返回这两个正序数组的 **中位数** 。

算法的时间复杂度应该为 `O(log (m+n))` 。

 

**示例 1：**

```
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
```

**示例 2：**

```
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
```

 

 

**提示：**

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`



这个问题要求在合并两个有序数组后找到中位数，并且时间复杂度要求是 $O(\log (m+n))$。直接合并数组并排序的方式的时间复杂度为 $O((m+n)\log(m+n))$，这显然不符合要求。为了达到要求的时间复杂度，我们可以通过二分查找来解决。

思路：

1. **中位数的定义**：
   - 如果合并后的数组长度是奇数，中位数就是中间那个元素。
   - 如果合并后的数组长度是偶数，中位数是中间两个元素的平均值。
2. **分治法**：
   - 我们可以将问题转化为在两个有序数组中寻找一个合适的分割点，使得：
     - 左侧部分包含的元素数量等于右侧部分（或比右侧部分多一个元素）。
     - 左侧部分的所有元素都不大于右侧部分的所有元素。
3. **二分查找**：
   - 通过对较小数组进行二分查找来优化时间复杂度。我们设定数组 `nums1` 和 `nums2` 中较小的那个作为主数组。
   - 在 `nums1` 中选择一个分割点，然后根据该分割点在 `nums2` 中选择对应的分割点，确保左右两边的元素满足中位数的定义。

代码实现：

```python
def findMedianSortedArrays(nums1, nums2):
    # 确保 nums1 是较小的数组
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    
    # 二分查找 nums1
    left, right = 0, m
    
    while left <= right:
        # 在 nums1 中选择一个分割点
        partition1 = (left + right) // 2
        partition2 = (m + n + 1) // 2 - partition1
        
        # 获取分割点左右两侧的值
        maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        minRight1 = float('inf') if partition1 == m else nums1[partition1]
        
        maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        minRight2 = float('inf') if partition2 == n else nums2[partition2]
        
        # 判断是否找到了正确的分割点
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            # 找到分割点
            if (m + n) % 2 == 0:
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            else:
                return max(maxLeft1, maxLeft2)
        elif maxLeft1 > minRight2:
            # 如果 maxLeft1 大于 minRight2，说明 partition1 需要向左移
            right = partition1 - 1
        else:
            # 如果 maxLeft2 大于 minRight1，说明 partition1 需要向右移
            left = partition1 + 1
```

### 解释：

1. 确保二分查找在较小的数组上进行：
   - 我们首先确保 `nums1` 是较小的数组，这样可以减少二分查找的次数。
2. 二分查找的核心：
   - 在 `nums1` 中选择一个分割点 `partition1`，然后在 `nums2` 中根据 `partition1` 计算对应的分割点 `partition2`。
   - 我们保证：
     - `nums1` 左侧的元素不大于 `nums2` 右侧的元素。
     - `nums2` 左侧的元素不大于 `nums1` 右侧的元素。
3. 中位数的计算：
   - 如果合并后的数组长度是奇数，返回 `max(maxLeft1, maxLeft2)`，即左侧最大的元素。
   - 如果合并后的数组长度是偶数，返回 `(max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2`，即左侧最大元素和右侧最小元素的平均值。



时间复杂度：

- 二分查找的时间复杂度是 $O(\log \min(m, n))$，因此整体时间复杂度是 $O(\log \min(m, n))$。

空间复杂度：

- 只使用了常数级别的额外空间，空间复杂度是 O(1)。





```python
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            nums1, nums2, n1, n2 = nums2, nums1, n2, n1
        if n2 == 0:
            raise ValueError

        left, right, half_len = 0, n1, (n1 + n2 + 1) // 2
        while left <= right:
            i = (left + right) // 2
            j = half_len - i
            if i < n1 and nums2[j - 1] > nums1[i]:
                left = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                right = i
            else:
                max_of_left = 0
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (n1 + n2) % 2 == 1:
                    return max_of_left

                min_of_right = 0
                if i == n1:
                    min_of_right = nums2[j]
                elif j == n2:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0

        raise ValueError

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays([1, 3], [2]))  # 2.0
    print(sol.findMedianSortedArrays([1, 2], [3, 4]))  # 2.5
```





## 23.合并K个升序链表

https://leetcode.cn/problems/merge-k-sorted-lists/

给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

 

**示例 1：**

```
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
```

**示例 2：**

```
输入：lists = []
输出：[]
```

**示例 3：**

```
输入：lists = [[]]
输出：[]
```

 

**提示：**

- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- `lists[i]` 按 **升序** 排列
- `lists[i].length` 的总和不超过 `10^4`



```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(p, q):
            dummy = ListNode()
            pre = dummy
            while p and q:
                if p.val <= q.val:
                    pre.next = p
                    pre = p
                    p = p.next
                elif p.val > q.val:
                    pre.next = q
                    pre = q
                    q = q.next

            pre.next = p if p else q
            
            return dummy.next


        if not lists:
            return None

        n = len(lists)
        while n > 1:
            new_lists = []
            for i in range(0, n, 2):
                if i < n - 1:
                    new_lists.append(merge(lists[i], lists[i+1]))
                else:
                    new_lists.append(lists[i])
            lists = new_lists
            n = len(lists)
        
        return lists[0] if lists else None

```





## 25.K个一组翻转链表

https://leetcode.cn/problems/reverse-nodes-in-k-group/description/

给你链表的头节点 `head` ，每 `k` 个节点一组进行翻转，请你返回修改后的链表。

`k` 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 `k` 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

 

**示例 1：**

<img src="https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg" alt="img" style="zoom:67%;" />

```
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]
```

**示例 2：**

<img src="https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg" alt="img" style="zoom:67%;" />

```
输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]
```

 

**提示：**

- 链表中的节点数目为 `n`
- `1 <= k <= n <= 5000`
- `0 <= Node.val <= 1000`

 

**进阶：**你可以设计一个只用 `O(1)` 额外内存空间的算法解决此问题吗？



```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 创建一个虚拟头节点，并将其next指针指向head
        dummy = ListNode(next=head)
        groupPrev = dummy
        
        while True:
            # 检查从当前起始节点开始是否有k个节点
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            
            # 反转该组内的节点
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # 将前一个group的最后一个节点与新反转后的第一个节点连接起来
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    def getKth(self, curr: ListNode, k: int) -> Optional[ListNode]:
        # 移动curr直到第k个节点或到达链表末尾
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
```



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

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png" alt="img" style="zoom:67%;" />

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



## 51.N皇后

backtracking, https://leetcode.cn/problems/n-queens/

按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

**n 皇后问题** 研究的是如何将 `n` 个皇后放置在 `n×n` 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 `n` ，返回所有不同的 **n 皇后问题** 的解决方案。

每一种解法包含一个不同的 **n 皇后问题** 的棋子放置方案，该方案中 `'Q'` 和 `'.'` 分别代表了皇后和空位。

 

**示例 1：**

![img](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)

```
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。
```

**示例 2：**

```
输入：n = 1
输出：[["Q"]]
```

 

**提示：**

- `1 <= n <= 9`



斜率是+1或者-1，截距是常数。遍历每一列 `q`，检查当前列 `q` 是否可以放置皇后：

- `q not in queens` 确保没有其他皇后在同一列。
- `p - q not in xy_diff` 确保没有其他皇后在同一左下到右上的对角线。
- `p + q not in xy_sum` 确保没有其他皇后在同一左上到右下的对角线。

```python
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(queens, xy_diff, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return
            for q in range(n):
                if q not in queens and p - q not in xy_diff and p + q not in xy_sum:
                    dfs(queens + [q], xy_diff + [p - q], xy_sum + [p + q])
        result = []
        dfs([], [], [])
        print(result)
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]

if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))
```





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





## 84.柱状图中最大的矩形

monotonic stack, https://leetcode.cn/problems/largest-rectangle-in-histogram/

给定 *n* 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

 

**示例 1:**

<img src="https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg" alt="img" style="zoom:67%;" />

```
输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
```

**示例 2：**

<img src="https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg" alt="img" style="zoom:67%;" />

```
输入： heights = [2,4]
输出： 4
```

 

**提示：**

- `1 <= heights.length <=10^5`
- `0 <= heights[i] <= 10^4`



```python
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.largestRectangleArea([2,1,5,6,2,3]))
```

关键概念：

1. **单调栈**：
   - 用栈来维护柱子的索引，并确保栈中的柱子高度是单调递增的。
   - 当遇到比栈顶柱子矮的柱子时，就意味着栈顶的柱子已经不能再扩展更大的矩形了，应该从栈中弹出这个柱子，计算以它为高度的矩形面积。
2. **为什么需要在 `heights` 前后加 0**：
   - 通过在 `heights` 数组的开始和结束分别加上 `0`，可以保证栈最终能清空，并且在所有柱子处理完后能够强制计算出最后一块矩形面积。
   - 这个“0”是为了处理栈中剩余的柱子（特别是最后一部分）。

栈操作：

- **栈中存储的是什么**：
  - `stack` 中存储的是柱子的 **索引**，而不是柱子的高度。这样可以通过 `heights[i]` 直接访问到柱子的高度。
- **计算矩形面积**：
  - 在栈顶元素出栈时，表示栈顶柱子所能组成的最大矩形已经结束，当前的矩形高度就是栈顶柱子的高度。
  - 宽度 `w` 的计算是当前索引 `i` 减去栈中的下一个元素索引（即 `stack[-1]`），再减去 1，因为栈中的元素代表了一个 **区间**。
  - 例如，如果 `stack[-1]` 是索引 `j`，那么这个矩形的宽度就是 `i - j - 1`。



## 124.二叉树中的最大路径和

dfs, https://leetcode.cn/problems/binary-tree-maximum-path-sum/

二叉树中的 **路径** 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 **至多出现一次** 。该路径 **至少包含一个** 节点，且不一定经过根节点。

**路径和** 是路径中各节点值的总和。

给你一个二叉树的根节点 `root` ，返回其 **最大路径和** 。

 

**示例 1：**

<img src="https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg" alt="img" style="zoom:67%;" />

```
输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
```

**示例 2：**

<img src="https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg" alt="img" style="zoom:67%;" />

```
输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
```

 

**提示：**

- 树中节点数目范围是 `[1, 3 * 104]`
- `-1000 <= Node.val <= 1000`



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def max_gain(node):
            if not node:
                return 0

            # Recursively get the maximum gain from the left and right subtrees
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # Calculate the price of the current path
            current_path_sum = node.val + left_gain + right_gain

            # Update the global maximum path sum
            self.max_sum = max(self.max_sum, current_path_sum)

            # Return the maximum gain the current node can contribute to its parent
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return self.max_sum
        
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



## 146.LRU缓存

https://leetcode.cn/problems/lru-cache/

请你设计并实现一个满足 [LRU (最近最少使用) 缓存](https://baike.baidu.com/item/LRU) 约束的数据结构。

实现 `LRUCache` 类：

- `LRUCache(int capacity)` 以 **正整数** 作为容量 `capacity` 初始化 LRU 缓存
- `int get(int key)` 如果关键字 `key` 存在于缓存中，则返回关键字的值，否则返回 `-1` 。
- `void put(int key, int value)` 如果关键字 `key` 已经存在，则变更其数据值 `value` ；如果不存在，则向缓存中插入该组 `key-value` 。如果插入操作导致关键字数量超过 `capacity` ，则应该 **逐出** 最久未使用的关键字。

函数 `get` 和 `put` 必须以 `O(1)` 的平均时间复杂度运行。

 

**示例：**

```
输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
```

 

**提示：**

- `1 <= capacity <= 3000`
- `0 <= key <= 10000`
- `0 <= value <= 105`
- 最多调用 `2 * 105` 次 `get` 和 `put`





```python
class DLinkedNode:
    """双向链表的节点类"""
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # 存储 key 到 DLinkedNode 的映射
        # 初始化双向链表
        self.head = DLinkedNode()  # 虚拟头节点
        self.tail = DLinkedNode()  # 虚拟尾节点
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: DLinkedNode):
        """从链表中移除节点"""
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    def _insert(self, node: DLinkedNode):
        """将节点插入到链表的头部"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        """获取缓存中的值"""
        if key in self.cache:
            node = self.cache[key]
            # 移动到头部
            self._remove(node)
            self._insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """插入/更新键值对"""
        if key in self.cache:
            # 如果键存在，先删除再插入，更新顺序
            node = self.cache[key]
            self._remove(node)
            node.value = value
            self._insert(node)
        else:
            # 如果键不存在，创建新节点
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self._insert(node)
            # 如果超过容量，移除最久未使用的元素
            if len(self.cache) > self.capacity:
                # 移除链表尾部的元素，即最久未使用的
                tail = self.tail.prev
                self._remove(tail)
                del self.cache[tail.key]


if __name__ == "__main__":
    # 测试代码
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    print(lRUCache.get(1))  # 返回 1
    lRUCache.put(3, 3)  # 该操作会使得关键字 2 作废
    print(lRUCache.get(2))  # 返回 -1 (未找到)
    lRUCache.put(4, 4)  # 该操作会使得关键字 1 作废
    print(lRUCache.get(1))  # 返回 -1 (未找到)
    print(lRUCache.get(3))  # 返回 3
    print(lRUCache.get(4))  # 返回 4


```

思考题

在本题的基础上，为 *key* 增加过期时间（put 调用时额外传入过期时间）。如果 *key* 过期，则需要删除掉。



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



## 295.数据流的中位数

heap, https://leetcode.cn/problems/find-median-from-data-stream/

**中位数**是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

- 例如 `arr = [2,3,4]` 的中位数是 `3` 。
- 例如 `arr = [2,3]` 的中位数是 `(2 + 3) / 2 = 2.5` 。

实现 MedianFinder 类:

- `MedianFinder() `初始化 `MedianFinder` 对象。
- `void addNum(int num)` 将数据流中的整数 `num` 添加到数据结构中。
- `double findMedian()` 返回到目前为止所有元素的中位数。与实际答案相差 `10-5` 以内的答案将被接受。

**示例 1：**

```
输入
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
输出
[null, null, null, 1.5, null, 2.0]

解释
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

**提示:**

- `-10^5 <= num <= 10^5`
- 在调用 `findMedian` 之前，数据结构中至少有一个元素
- 最多 `5 * 10^4` 次调用 `addNum` 和 `findMedian`



**解法：最大堆 + 最小堆**

要高效地维护数据流的 **中位数**，我们可以使用 **两个堆**：

1. **最大堆（left_heap）** 存储较小的一半元素（取最大值）
2. **最小堆（right_heap）** 存储较大的一半元素（取最小值）

这样：

- **如果元素个数为奇数**，中位数是 **最大堆的堆顶**。
- **如果元素个数为偶数**，中位数是 **最大堆的堆顶 和 最小堆的堆顶的均值**。

Python 代码

```python
import heapq

class MedianFinder:
    def __init__(self):
        # 最大堆（存储较小的一半，取反存入以模拟最大堆）
        self.left_heap = []
        # 最小堆（存储较大的一半）
        self.right_heap = []

    def addNum(self, num: int) -> None:
        # 先将 num 放入最大堆（但因为 Python 没有最大堆，我们存入负数来模拟）
        heapq.heappush(self.left_heap, -num)

        # 确保最大堆的最大值 ≤ 最小堆的最小值
        if self.left_heap and self.right_heap and (-self.left_heap[0] > self.right_heap[0]):
            heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))

        # 平衡两个堆的大小，使得最大堆的元素个数 ≥ 最小堆的元素个数
        if len(self.left_heap) > len(self.right_heap) + 1:
            heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))
        elif len(self.right_heap) > len(self.left_heap):
            heapq.heappush(self.left_heap, -heapq.heappop(self.right_heap))

    def findMedian(self) -> float:
        # 如果元素个数是奇数，中位数是最大堆的堆顶
        if len(self.left_heap) > len(self.right_heap):
            return -self.left_heap[0]
        # 如果元素个数是偶数，中位数是两个堆顶的平均值
        return (-self.left_heap[0] + self.right_heap[0]) / 2.0
```

最大堆 + 最小堆维护数据流的中位数  
`O(log n)` 插入，`O(1)` 查询，适用于 大数据流  
Python `heapq` 默认最小堆，用负数模拟最大堆





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



## 2218.从栈中取出K个硬币的最大面值和

dp, https://leetcode.cn/problems/maximum-value-of-k-coins-from-piles/

一张桌子上总共有 `n` 个硬币 **栈** 。每个栈有 **正整数** 个带面值的硬币。

每一次操作中，你可以从任意一个栈的 **顶部** 取出 1 个硬币，从栈中移除它，并放入你的钱包里。

给你一个列表 `piles` ，其中 `piles[i]` 是一个整数数组，分别表示第 `i` 个栈里 **从顶到底** 的硬币面值。同时给你一个正整数 `k` ，请你返回在 **恰好** 进行 `k` 次操作的前提下，你钱包里硬币面值之和 **最大为多少** 。

 

**示例 1：**

<img src="https://assets.leetcode.com/uploads/2019/11/09/e1.png" alt="img" style="zoom:67%;" />

```
输入：piles = [[1,100,3],[7,8,9]], k = 2
输出：101
解释：
上图展示了几种选择 k 个硬币的不同方法。
我们可以得到的最大面值为 101 。
```

**示例 2：**

```
输入：piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
输出：706
解释：
如果我们所有硬币都从最后一个栈中取，可以得到最大面值和。
```

 

**提示：**

- `n == piles.length`
- `1 <= n <= 1000`
- `1 <= piles[i][j] <= 105`
- `1 <= k <= sum(piles[i].length) <= 2000`



```python
from typing import List
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(k + 1):
                current_sum = 0
                for x in range(min(j, len(piles[i-1])) + 1):
                    if x > 0:
                        current_sum += piles[i-1][x-1]
                    dp[i][j] = max(dp[i][j], dp[i-1][j-x] + current_sum)

        return dp[n][k]

if __name__ == '__main__':
    sol = Solution()
    piles = [[1, 100, 3], [7, 8, 9]]
    k = 2
    print(sol.maxValueOfCoins(piles, k))  # Output: 101

    piles = [[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]]
    k = 7
    print(sol.maxValueOfCoins(piles, k))  # Output: 706
```



> 这是一个典型的动态规划问题，涉及从多个堆中取出硬币的最大价值。题目大意是：给定若干个堆，每个堆包含一些硬币。你需要从每个堆中选择若干个硬币，使得总共选出的硬币数不超过 `k`，并且硬币的总价值最大。`piles` 是一个二维数组，每个子数组代表一个堆的硬币；`k` 是最多可以选择的硬币数量。
>
> 1. **初始化：**
>
>    ```python
>    n = len(piles)
>    dp = [[0] * (k + 1) for _ in range(n + 1)]
>    ```
>
>    `n` 是堆的数量。`dp[i][j]` 代表考虑前 `i` 个堆，最多取 `j` 个硬币时的最大价值。初始化时，所有的 `dp[i][j]` 都是 `0`，表示初始状态下没有选择任何硬币。
>
> 2. **填充动态规划表格：**
>
>    ```python
>    for i in range(1, n + 1):
>        for j in range(k + 1):
>            current_sum = 0
>            for x in range(min(j, len(piles[i-1])) + 1):
>                if x > 0:
>                    current_sum += piles[i-1][x-1]
>                dp[i][j] = max(dp[i][j], dp[i-1][j-x] + current_sum)
>    ```
>
>    这三层嵌套循环的作用是逐步计算每个 `dp[i][j]` 的值：
>
>    - 外层循环 `i` 从 `1` 到 `n`，表示正在考虑第 `i` 个堆。
>    - 中层循环 `j` 从 `0` 到 `k`，表示选择的硬币数量。
>    - 内层循环 `x` 从 `0` 到 `min(j, len(piles[i-1]))`，表示从当前堆中选择的硬币数量。`min(j, len(piles[i-1]))` 保证不会选择超过当前堆硬币数的硬币。
>
>    `current_sum` 记录当前堆选择的硬币的总价值。如果 `x > 0`，说明选择了 `x` 个硬币，那么就将 `piles[i-1][x-1]` 加入到 `current_sum` 中。
>
>    `dp[i][j]` 的值通过比较两种情况来更新：
>
>    - 不选择当前堆的硬币，`dp[i-1][j]`；
>    - 选择 `x` 个硬币时的值，`dp[i-1][j-x] + current_sum`。





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



## 2412.完成所有交易的初始最少钱数

greedy, https://leetcode.cn/problems/minimum-money-required-before-transactions/

给你一个下标从 **0** 开始的二维整数数组 `transactions`，其中`transactions[i] = [costi, cashbacki]` 。

数组描述了若干笔交易。其中每笔交易必须以 **某种顺序** 恰好完成一次。在任意一个时刻，你有一定数目的钱 `money` ，为了完成交易 `i` ，`money >= costi` 这个条件必须为真。执行交易后，你的钱数 `money` 变成 `money - costi + cashbacki` 。

请你返回 **任意一种** 交易顺序下，你都能完成所有交易的最少钱数 `money` 是多少。

 

**示例 1：**

```
输入：transactions = [[2,1],[5,0],[4,2]]
输出：10
解释：
刚开始 money = 10 ，交易可以以任意顺序进行。
可以证明如果 money < 10 ，那么某些交易无法进行。
```

**示例 2：**

```
输入：transactions = [[3,0],[0,3]]
输出：3
解释：
- 如果交易执行的顺序是 [[3,0],[0,3]] ，完成所有交易需要的最少钱数是 3 。
- 如果交易执行的顺序是 [[0,3],[3,0]] ，完成所有交易需要的最少钱数是 0 。
所以，刚开始钱数为 3 ，任意顺序下交易都可以全部完成。
```

 

**提示：**

- `1 <= transactions.length <= 105`
- `transactions[i].length == 2`
- `0 <= costi, cashbacki <= 10^9`



题目要求的是在任意一种交易顺序下都能完成所有交易的最少初始金额。为了确保在最费钱的交易顺序下也能完成所有交易，我们需要找到一种最费钱的交易排列方式。  

分类交易：  将交易分为两类：cost > cashback 和 cost <= cashback。
排序：  
对于 cost > cashback 的交易，按 cashback 升序排序。
对于 cost <= cashback 的交易，按 cost 降序排序。

```python
from typing import List

class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        # Separate transactions into two categories
        # 1. Transactions where cost > cashback
        # 2. Transactions where cost <= cashback
        cost_greater_than_cashback = []
        cost_less_or_equal_cashback = []
        
        for cost, cashback in transactions:
            if cost > cashback:
                cost_greater_than_cashback.append((cost, cashback))
            else:
                cost_less_or_equal_cashback.append((cost, cashback))
        
        # Sort the first category by cashback in ascending order
        cost_greater_than_cashback.sort(key=lambda x: x[1])
        
        # Sort the second category by cost in descending order
        cost_less_or_equal_cashback.sort(key=lambda x: -x[0])
        
        # Combine the two sorted lists
        sorted_transactions = cost_greater_than_cashback + cost_less_or_equal_cashback
        
        # Calculate the minimum initial money required
        min_money = 0
        current_money = 0
        
        for cost, cashback in sorted_transactions:
            if current_money < cost:
                min_money += cost - current_money
                current_money = cost
            current_money = current_money - cost + cashback
        
        return min_money

# Example usage
if __name__ == "__main__":
    transactions = [[2, 1], [5, 0], [4, 2]]
    print(Solution().minimumMoney(transactions))  # Output: 10
```





## 2920.收集所有金币可获得的最大积分

tree dp, https://leetcode.cn/problems/maximum-points-after-collecting-coins-from-all-nodes/

有一棵由 `n` 个节点组成的无向树，以 `0` 为根节点，节点编号从 `0` 到 `n - 1` 。给你一个长度为 `n - 1` 的二维 **整数** 数组 `edges` ，其中 `edges[i] = [ai, bi]` 表示在树上的节点 `ai` 和 `bi` 之间存在一条边。另给你一个下标从 **0** 开始、长度为 `n` 的数组 `coins` 和一个整数 `k` ，其中 `coins[i]` 表示节点 `i` 处的金币数量。

从根节点开始，你必须收集所有金币。要想收集节点上的金币，必须先收集该节点的祖先节点上的金币。

节点 `i` 上的金币可以用下述方法之一进行收集：

- 收集所有金币，得到共计 `coins[i] - k` 点积分。如果 `coins[i] - k` 是负数，你将会失去 `abs(coins[i] - k)` 点积分。
- 收集所有金币，得到共计 `floor(coins[i] / 2)` 点积分。如果采用这种方法，节点 `i` 子树中所有节点 `j` 的金币数 `coins[j]` 将会减少至 `floor(coins[j] / 2)` 。

返回收集 **所有** 树节点的金币之后可以获得的最大积分。

 

**示例 1：**

<img src="https://assets.leetcode.com/uploads/2023/09/18/ex1-copy.png" alt="img" style="zoom:67%;" />

```
输入：edges = [[0,1],[1,2],[2,3]], coins = [10,10,3,3], k = 5
输出：11                        
解释：
使用第一种方法收集节点 0 上的所有金币。总积分 = 10 - 5 = 5 。
使用第一种方法收集节点 1 上的所有金币。总积分 = 5 + (10 - 5) = 10 。
使用第二种方法收集节点 2 上的所有金币。所以节点 3 上的金币将会变为 floor(3 / 2) = 1 ，总积分 = 10 + floor(3 / 2) = 11 。
使用第二种方法收集节点 3 上的所有金币。总积分 =  11 + floor(1 / 2) = 11.
可以证明收集所有节点上的金币能获得的最大积分是 11 。 
```

**示例 2：**

**<img src="https://assets.leetcode.com/uploads/2023/09/18/ex2.png" alt="img" style="zoom:67%;" />**

```
输入：edges = [[0,1],[0,2]], coins = [8,4,4], k = 0
输出：16
解释：
使用第一种方法收集所有节点上的金币，因此，总积分 = (8 - 0) + (4 - 0) + (4 - 0) = 16 。
```

 

**提示：**

- `n == coins.length`
- `2 <= n <= 105`
- `0 <= coins[i] <= 104`
- `edges.length == n - 1`
- `0 <= edges[i][0], edges[i][1] < n`
- `0 <= k <= 104`



树形dp，还挺有意思。`defaultdict`特别有用，`defaultdict(list)`就是邻接表。另外，类似lru_cache的装饰器可以自己写，例如：

```python
def memoize(f):
    memo = {}
    def helper(x, y, z):
        if (x, y, z) not in memo:
            memo[x, y, z] = f(x, y, z)
        return memo[x, y, z]
    return helper

@memoize
def dfs(node, parent, halved_times):
```





```python
class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        # 构建邻接表表示的图
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # 记忆化装饰器
        def memoize(f):
            memo = {}

            def helper(x, y, z):
                if (x, y, z) not in memo:
                    memo[x, y, z] = f(x, y, z)
                return memo[x, y, z]

            return helper

        @memoize
        def dfs(node, parent, halved_times):
            # 如果该子树已经经过多次减半，直接返回0以避免过小的数值影响结果
            if halved_times >= 14:  # log2(10^4) < 14, 因为coins[i] <= 10^4
                return 0

            # 减半操作应用于当前节点
            current_coins = coins[node] // (2 ** halved_times)

            # 两种选择：不减半和减半
            option1 = current_coins - k
            option2 = current_coins // 2

            for child in graph[node]:
                if child != parent:  # 避免回溯到父节点
                    option1 += dfs(child, node, halved_times)
                    option2 += dfs(child, node, halved_times + 1)

            return max(option1, option2)

        # 从根节点开始DFS遍历
        return dfs(0, None, 0)

```



```python
class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        # 构建邻接表表示的图
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        n = len(coins)
        # dp数组，dp[node][halved_times]表示从node开始，经过halved_times次减半后的最大积分
        dp = [[-1] * 14 for _ in range(n)]

        def dfs(node, parent, halved_times):
            if halved_times >= 14:  # 防止过多减半导致数值过小
                return 0

            if dp[node][halved_times] != -1:
                return dp[node][halved_times]

            current_coins = floor(coins[node] / (2 ** halved_times))

            # 不减半当前节点金币的选择
            option1 = current_coins - k
            # 减半当前节点金币的选择
            option2 = floor(current_coins / 2)

            for child in graph[node]:
                if child == parent:
                    continue
                option1 += dfs(child, node, halved_times)
                option2 += dfs(child, node, halved_times + 1)

            # 记录两种选择中的最大值
            dp[node][halved_times] = max(option1, option2)
            return dp[node][halved_times]

        # 从根节点0开始DFS遍历
        return dfs(0, None, 0)
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



## 3435.最短公共超序列的字母出现频率

枚举, 图谱排序, https://leetcode.cn/problems/frequencies-of-shortest-supersequences/

给你一个字符串数组 `words` 。请你找到 `words` 所有 **最短公共超序列** ，且确保它们互相之间无法通过排列得到。

**最短公共超序列** 指的是一个字符串，`words` 中所有字符串都是它的子序列，且它的长度 **最短** 。

请你返回一个二维整数数组 `freqs` ，表示所有的最短公共超序列，其中 `freqs[i]` 是一个长度为 26 的数组，它依次表示一个最短公共超序列的所有小写英文字母的出现频率。你可以以任意顺序返回这个频率数组。

**排列** 指的是一个字符串中所有字母重新安排顺序以后得到的字符串。

一个 **子序列** 是从一个字符串中删除一些（也可以不删除）字符后，剩余字符不改变顺序连接得到的 **非空** 字符串。

 

**示例 1：**

**输入：**words = ["ab","ba"]

**输出：**[[1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

**解释：**

两个最短公共超序列分别是 `"aba"` 和 `"bab"` 。输出分别是两者的字母出现频率。

**示例 2：**

**输入：**words = ["aa","ac"]

**输出：**[[2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

**解释：**

两个最短公共超序列分别是 `"aac"` 和 `"aca"` 。由于它们互为排列，所以只保留 `"aac"` 。

**示例 3：**

**输入：**words = ["aa","bb","cc"]

**输出：**[[2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

**解释：**

`"aabbcc"` 和它所有的排列都是最短公共超序列。

 

**提示：**

- `1 <= words.length <= 256`
- `words[i].length == 2`
- `words` 中所有字符串都包含不超过 16 个互不相同的小写英文字母。
- `words` 中的字符串互不相同。



【LeetCode作者：流萤】

假设出现两次的字母为 `abc...i`，出现一次的字母为 `jkl...p`，那么序列应该是 `abc...i [jkl...p 的某种排列] abc...i` 最好。这样，对于 `words` 中任何长度为 2 的字符串 $c_1c_2$，只要 $c_1$和 $c_2$其中一个出现两次，那么一定能在这个序列里找到对应的子序列；如果两者都只出现一次，那么它们都会出现在序列的中间，而且必须满足 $c_1$排在 $c_2$的前面。剩下的问题就是只出现一次的字母需要怎么排列。“$c_1$排在 $c_2$前面”这就是经典的拓扑排序。



```python
from graphlib import TopologicalSorter
from collections import defaultdict
from itertools import combinations
from typing import List

class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        # 创建一个集合，包含所有的单词
        word_set = set(words)
        
        # 创建一个字符集合，包含所有出现在单词中的字母
        all_chars = set(y for word in words for y in word)
        
        # 创建一个长度为26的列表，用于记录每个字母的计数
        char_count = [0] * 26
        
        # 遍历所有字母，更新它们的计数
        for char in all_chars:
            # 通过 ord() 将字符转为对应的数字（从'a'到'z'）
            # 假设字母是小写字母，从0开始到25，映射到char_count的索引
            char_count[ord(char) - 97] += 2  # 每个字符初始计数加2
            
        # 从字符集(all_chars)的大小开始，尝试逐步减少，直到0
        for cnt in range(len(all_chars), -1, -1):
            possible_answers = []  # 用来存储当前长度为cnt的可能结果
            
            # 获取所有长度为cnt的字母组合
            for char_combo in combinations(all_chars, cnt):
                # 创建一个图结构，用字典存储字符的依赖关系
                graph = defaultdict(list)
                
                # 遍历当前组合中的字符对
                for char1 in char_combo:
                    for char2 in char_combo:
                        # 如果字符对组成的字符串是单词中的一部分，则建立依赖关系
                        if char1 + char2 in word_set:
                            graph[char1].append(char2)
                
                try:
                    # 使用 TopologicalSorter 来检测是否存在有效的拓扑排序
                    list(TopologicalSorter(graph).static_order())
                    
                    # 复制字符计数列表
                    updated_count = char_count.copy()
                    
                    # 对于当前组合中的每个字符，减去1
                    for char in char_combo:
                        updated_count[ord(char) - 97] -= 1
                    
                    # 将更新后的计数添加到结果列表中
                    possible_answers.append(updated_count)
                
                except:
                    # 如果出现异常（说明无法进行拓扑排序），继续尝试其他组合
                    continue
            
            # 如果有有效的答案，则返回这些结果
            if possible_answers:
                return possible_answers

```





```python
from graphlib import TopologicalSorter

class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        d = set(words)
        d0 = set(y for x in words for y in x)
        l = [0] * 26
        for x in d0:
            l[ord(x) - 97] += 2
            
        for cnt in range(len(d0), -1, -1):
            ans = []
            for x in combinations(d0, cnt):
                g = defaultdict(list)
                for y in x:
                    for z in x:
                        if y + z in d:
                            g[y].append(z)
                try:
                    list(TopologicalSorter(g).static_order())
                    res = l.copy()
                    for y in x:
                        res[ord(y) - 97] -= 1
                    ans.append(res)
                except:
                    continue
            if ans:
                return ans


```



## 3441.变成好标题的最少代价

dp, https://leetcode.cn/problems/minimum-cost-good-caption/

给你一个长度为 `n` 的字符串 `caption` 。如果字符串中 **每一个** 字符都位于连续出现 **至少 3 次** 的组中，那么我们称这个字符串是 **好** 标题。

比方说：

- `"aaabbb"` 和 `"aaaaccc"` 都是 **好** 标题。
- `"aabbb"` 和 `"ccccd"` 都 **不是** 好标题。

你可以对字符串执行以下操作 **任意** 次：

选择一个下标 `i`（其中 `0 <= i < n` ）然后将该下标处的字符变为：

- 该字符在字母表中 **前** 一个字母（前提是 `caption[i] != 'a'` ）
- 该字符在字母表中 **后** 一个字母（`caption[i] != 'z'` ）

你的任务是用 **最少** 操作次数将 `caption` 变为 **好** 标题。如果存在 **多种** 好标题，请返回它们中 **字典序最小** 的一个。如果 **无法** 得到好标题，请你返回一个空字符串 `""` 。

在字符串 `a` 和 `b` 中，如果两个字符串第一个不同的字符处，字符串 `a` 的字母比 `b` 的字母在字母表里出现的顺序更早，那么我们称字符串 `a` 的 **字典序** 比 `b` **小** 。如果两个字符串前 `min(a.length, b.length)` 个字符都相同，那么较短的一个字符串字典序比另一个字符串小。

 

**示例 1：**

**输入：**caption = "cdcd"

**输出：**"cccc"

**解释：**

无法用少于 2 个操作将字符串变为好标题。2 次操作得到好标题的方案包括：

- `"dddd"` ：将 `caption[0]` 和 `caption[2]` 变为它们后一个字符 `'d'` 。
- `"cccc"` ：将 `caption[1]` 和 `caption[3]` 变为它们前一个字符 `'c'` 。

由于 `"cccc"` 字典序比 `"dddd"` 小，所以返回 `"cccc"` 。

**示例 2：**

**输入：**caption = "aca"

**输出：**"aaa"

**解释：**

无法用少于 2 个操作将字符串变为好标题。2 次操作得到好标题的方案包括：

- 操作 1：将 `caption[1]` 变为 `'b'` ，`caption = "aba"` 。
- 操作 2：将 `caption[1]` 变为 `'a'` ，`caption = "aaa"` 。

所以返回 `"aaa"` 。

**示例 3：**

**输入：**caption = "bc"

**输出：**""

**解释：**

由于字符串的长度小于 3 ，无法将字符串变为好标题。

 

**提示：**

- `1 <= caption.length <= 5 * 104`
- `caption` 只包含小写英文字母。



```python
class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if n < 3:
            return ""

        dp = [[0] * 26 for _ in range(n)]
        maxDp = [0] * n
        maxPos = [0] * n
        step = [[0] * 26 for _ in range(n)]

        # 初始化最后三个字符的dp数组
        for j in range(26):
            step[n - 3][j] = 3
            for k in range(n - 3, n):
                dp[n - 3][j] += abs(ord(caption[k]) - ord('a') - j)

        maxDp[n - 3] = dp[n - 3][0]
        for j in range(1, 26):
            if dp[n - 3][j] < maxDp[n - 3]:
                maxDp[n - 3] = dp[n - 3][j]
                maxPos[n - 3] = j

        # 填充dp数组
        for i in range(n - 4, -1, -1):
            for j in range(26):
                # remain
                step[i][j] = 1
                dp[i][j] = dp[i + 1][j] + abs(ord(caption[i]) - ord('a') - j)

                # change
                if i < n - 5:
                    newDp = maxDp[i + 3]
                    newPos = maxPos[i + 3]
                    for k in range(i, i + 3):
                        newDp += abs(ord(caption[k]) - ord('a') - j)
                    if newDp < dp[i][j] or (newDp == dp[i][j] and newPos < j):
                        step[i][j] = 3
                        dp[i][j] = newDp

            maxDp[i] = dp[i][0]
            for j in range(1, 26):
                if dp[i][j] < maxDp[i]:
                    maxDp[i] = dp[i][j]
                    maxPos[i] = j

        # 构建结果字符串
        res = []
        cur = 0
        curPos = maxPos[0]
        while cur < n:
            if step[cur][curPos] == 1:
                res.append(chr(curPos + ord('a')))
                cur += 1
                continue
            res.append(chr(curPos + ord('a')) * 3)
            cur += 3
            if cur < n:
                curPos = maxPos[cur]

        return ''.join(res)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minCostGoodCaption("cdcd"))
    print(sol.minCostGoodCaption("aca"))
    print(sol.minCostGoodCaption("bc"))
```



## 3444.使数组包含目标值倍数的最少增量

动态规划（DP）+ 最小公倍数（LCM）+ 位掩码（Bitmasking），https://leetcode.cn/problems/minimum-increments-for-target-multiples-in-an-array/

给你两个数组 `nums` 和 `target` 。

在一次操作中，你可以将 `nums` 中的任意一个元素递增 1 。

返回要使 `target` 中的每个元素在 `nums` 中 **至少** 存在一个倍数所需的 **最少操作次数** 。

 

**示例 1：**

**输入：**nums = [1,2,3], target = [4]

**输出：**1

**解释：**

满足题目条件的最少操作次数是 1 。

- 将 3 增加到 4 ，需要 1 次操作，4 是目标值 4 的倍数。

**示例 2：**

**输入：**nums = [8,4], target = [10,5]

**输出：**2

**解释：**

满足题目条件的最少操作次数是 2 。

- 将 8 增加到 10 ，需要 2 次操作，10 是目标值 5 和 10 的倍数。

**示例 3：**

**输入：**nums = [7,9,10], target = [7]

**输出：**0

**解释：**

数组中已经包含目标值 7 的一个倍数，不需要执行任何额外操作。

 

**提示：**

- `1 <= nums.length <= 5 * 10^4`
- `1 <= target.length <= 4`
- `target.length <= nums.length`
- `1 <= nums[i], target[i] <= 10^4`



有两个列表 `nums` 和 `target`，要求通过对 `nums` 中的元素增加一些数值，使得它们符合目标的倍数要求。我们最终的目标是计算最少的增量，使得每个目标的倍数都得到满足。

解题思路：

1. **目标描述**：对于每个目标 `target[i]`，我们需要通过对 `nums` 中的元素进行一些增量操作，使得它们满足某种倍数关系。
2. **位运算与子集组合**：使用位掩码 (`mask`) 来表示各个目标的组合情况。`mask` 表示一个目标子集，这样就可以通过动态规划 (DP) 遍历所有的目标组合。
3. **最小公倍数（LCM）计算**：通过计算每个子集目标的最小公倍数（LCM），来帮助确定每次增量操作所需要的最小值。

详细分析：

1. **子集遍历**：

   - 对于目标 `target` 中的每一个子集，我们计算其对应的最小公倍数（LCM）。
   - `lcm_map` 是一个字典，用来存储每个子集对应的 LCM 值。使用位掩码（从 `1` 到 `full`）来遍历所有子集。

2. **动态规划（DP）**：

   - `dp[s]` 表示从 `nums` 中选取的元素的增量之和，使得已经满足了 `target` 中子集 `s` 的倍数条件。
   - 我们通过逐个更新 `dp` 数组，来得到每个可能的子集满足的最小增量值。

3. **LCM 计算**：

   - 对于每个目标子集，首先计算该子集的 LCM，然后对每个 `nums` 中的元素，计算将其增加到满足 LCM 倍数的最小增量。

代码解读：

```python
from math import gcd
from typing import List

class Solution:
    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:
        m = len(target)
        full = (1 << m) - 1  # 计算全子集的掩码

        # 计算每个子集的最小公倍数 (LCM)
        lcm_map = {}
        for mask in range(1, full + 1):  # 从1开始，表示不为空的子集
            l = 1
            i = 0
            tmp = mask
            while tmp:
                if tmp & 1:
                    t = target[i]
                    l = l * t // gcd(l, t)  # 计算LCM
                tmp //= 2  # 移除最低有效位
                i += 1
            lcm_map[mask] = l

        # 动态规划：dp[s]表示达到子集s的最小增量
        inf = float('inf')
        dp = [inf] * (full + 1)
        dp[0] = 0  # 初始状态，子集为空时，增量为0

        # 遍历nums数组
        for a in nums:
            new_dp = dp[:]
            for s in range(full + 1):
                if dp[s] == inf:
                    continue  # 如果当前子集不可能达到，跳过

                # 对于每个子集和LCM，计算增量
                for sub, L in lcm_map.items():
                    cost = (L - (a % L)) % L  # 计算使a满足L倍数的增量
                    ns = s | sub  # 更新子集
                    if new_dp[ns] > dp[s] + cost:
                        new_dp[ns] = dp[s] + cost  # 更新最小增量
            dp = new_dp

        return dp[full]  # 返回全子集的最小增量

```

> 关键部分解释：
>
> - **`full = (1 << m) - 1`**：这表示 `target` 数组的所有子集掩码，即 `m` 个目标的全组合（即所有目标的集合）。
> - **`lcm_map`**：通过位掩码和目标数组 `target` 的组合计算每个子集的最小公倍数（LCM）。
> - **动态规划数组 `dp`**：`dp[s]` 记录了使得目标子集 `s` 满足倍数条件的最小增量，初始时为 `inf`，表示尚未达到该状态。
>
> 优化建议：
>
> 1. **减小空间复杂度**：
>    - `dp` 和 `new_dp` 每次只依赖于上一轮的结果，可以直接修改 `dp` 数组，避免多次复制。
>
> 2. **提前终止**：
>    - 如果发现某个子集的增量已经达到最小值，可以提前结束进一步的计算，避免不必要的计算。
>
> 总结：
>
> 这个解法利用了位运算表示子集组合和动态规划，时间复杂度较高，尤其是涉及 LCM 和子集的遍历（`2^m` 的子集），适用于中等规模的输入数据。如果要进一步优化，可能需要减少不必要的状态更新和优化 LCM 的计算。



## 3445.奇偶频次间的最大差值II

前缀和 + 哈希表（字典）+ 二分查找 组合的 优化滑动窗口，https://leetcode.cn/problems/maximum-difference-between-even-and-odd-frequency-ii/

给你一个字符串 `s` 和一个整数 `k` 。请你找出 `s` 的子字符串 `subs` 中两个字符的出现频次之间的 **最大** 差值，`freq[a] - freq[b]` ，其中：

- `subs` 的长度 **至少** 为 `k` 。
- 字符 `a` 在 `subs` 中出现奇数次。
- 字符 `b` 在 `subs` 中出现偶数次。

返回 **最大** 差值。

**注意** ，`subs` 可以包含超过 2 个 **互不相同** 的字符。.

**子字符串** 是字符串中的一个连续字符序列。

 

**示例 1：**

**输入：**s = "12233", k = 4

**输出：**-1

**解释：**

对于子字符串 `"12233"` ，`'1'` 的出现次数是 1 ，`'3'` 的出现次数是 2 。差值是 `1 - 2 = -1` 。

**示例 2：**

**输入：**s = "1122211", k = 3

**输出：**1

**解释：**

对于子字符串 `"11222"` ，`'2'` 的出现次数是 3 ，`'1'` 的出现次数是 2 。差值是 `3 - 2 = 1` 。

**示例 3：**

**输入：**s = "110", k = 3

**输出：**-1

 

**提示：**

- `3 <= s.length <= 3 * 10^4`
- `s` 仅由数字 `'0'` 到 `'4'` 组成。
- 输入保证至少存在一个子字符串是由一个出现奇数次的字符和一个出现偶数次的字符组成。
- `1 <= k <= s.length`







这个问题的核心是 **前缀和 + 哈希表（字典）+ 二分查找** 组合的 **优化滑动窗口** 方法。

**解题思路**

1. **前缀和计算频次**
   - 使用 **二维前缀和数组 `P[i][d]`** 统计 **前 `i` 个字符中 `d` 出现的次数**（`d` 代表 `0-4`）。
   - 计算每个 `P[i][a]` 和 `P[i][b]`，并用 `P[i][a] - P[i][b]` 作为关键值进行优化。

2. **分组存储不同的奇偶性**
   - 记录 `P[i][a]` 和 `P[i][b]` **的奇偶性组合**，存入 `groups[(pa, pb)]`，即：
     - `pa = P[i][a] % 2`，表示 `a` 的奇偶性。
     - `pb = P[i][b] % 2`，表示 `b` 的奇偶性。
   - 这可以帮助我们 **快速查找某个 `a` 和 `b` 的奇偶性匹配的子串**。

3. **二分查找优化**
   - **存储前缀最小值**，用于计算 `P[i][a] - P[i][b]` 的最优子串。
   - **二分查找 `bisect_right`** 快速找到满足 `k` 长度的最小索引 `j`，加速 `O(n^2)` 的暴力解法到 `O(n log n)`。

**代码优化**

- **减少 `O(n^2)` 的冗余计算**：
  - **使用 `defaultdict(list)`** 代替普通字典手动初始化 `groups`。
  - **去除不必要的 `if` 判断**，简化代码逻辑。
  - **优化 `bisect_right` 查询**，减少 `O(n log n)` 复杂度的查询次数。



**优化后的代码**

```python
from bisect import bisect_right
from collections import defaultdict

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)

        # 计算前缀和 P[i][d]，其中 d ∈ {0,1,2,3,4}
        P = [[0] * 5 for _ in range(n + 1)]
        for i, ch in enumerate(s):
            d = ord(ch) - ord("0")
            for j in range(5):
                P[i + 1][j] = P[i][j]  # 继承前一个前缀和
            P[i + 1][d] += 1  # 当前字符出现次数+1

        ans = float('-inf')

        # 遍历所有 a, b 的组合（a != b）
        for a in range(5):
            for b in range(5):
                if a == b:
                    continue

                # 存储 (pa, pb) 奇偶性的索引和差值
                groups = defaultdict(list)
                for i in range(n + 1):
                    pa, pb = P[i][a] & 1, P[i][b] & 1
                    d_val = P[i][a] - P[i][b]
                    groups[(pa, pb)].append((i, d_val, P[i][b]))

                # 预处理前缀最小值（前缀和单调队列优化）
                proc = {}
                for key, lst in groups.items():
                    idx_arr, d_arr, pb_arr = zip(*lst)  # 解包三列数据
                    pre_min = list(d_arr)  # 复制 `d_arr` 作为最小值数组

                    # 构造前缀最小值数组
                    min_val = float('inf')
                    for j in range(len(pre_min)):
                        min_val = min(min_val, pre_min[j])
                        pre_min[j] = min_val

                    proc[key] = (idx_arr, pb_arr, pre_min)

                # 遍历所有可能的右端点 pos
                for pos in range(k, n + 1):
                    pa, pb = P[pos][a] & 1, P[pos][b] & 1
                    key = (1 - pa, pb)

                    if key not in proc:
                        continue  # 如果没有对应奇偶性的组合，跳过

                    idx_arr, pb_arr, pre_min = proc[key]

                    # 使用二分查找找到符合 k 限制的最小 j
                    j1 = bisect_right(idx_arr, pos - k) - 1
                    j2 = bisect_right(pb_arr, P[pos][b] - 2) - 1
                    j = min(j1, j2)

                    if j >= 0:
                        cur = (P[pos][a] - P[pos][b]) - pre_min[j]
                        ans = max(ans, cur)

        return ans
```



> **优化点**
>
> **1. 使用 `defaultdict(list)` 简化 `groups` 结构**
>
> 原代码手动创建 `groups`：
>
> ```python
> groups = {}
> for pa in (0, 1):
>     for pb in (0, 1):
>         groups[(pa, pb)] = []
> ```
>
> 优化为：
>
> ```python
> groups = defaultdict(list)
> ```
>
> 这样在 `groups[(pa, pb)].append(...)` 时 **自动初始化**，减少了手动赋值的复杂度。
>
> ---
>
> **2. `zip(*lst)` 直接提取列，减少循环次数**
>
> 原代码：
>
> ```python
> idx_arr = [t[0] for t in lst]
> pb_arr = [t[2] for t in lst]
> d_arr = [t[1] for t in lst]
> ```
>
> 优化为：
>
> ```python
> idx_arr, d_arr, pb_arr = zip(*lst)
> ```
>
> 直接从 `lst` 提取 **所有列数据**，提高可读性，避免 `O(n)` 额外循环。
>
> ---
>
> **3. 预计算 `pre_min` 直接更新**
>
> 原代码：
>
> ```python
> pre_min = []
> cur = 10**9
> for d in d_arr:
>     if d < cur:
>         cur = d
>     pre_min.append(cur)
> ```
>
> 优化为：
>
> ```python
> pre_min = list(d_arr)
> min_val = float('inf')
> for j in range(len(pre_min)):
>     min_val = min(min_val, pre_min[j])
>     pre_min[j] = min_val
> ```
>
> - 直接用 `list(d_arr)` **减少一次数组拷贝**。
> - 使用 `min_val` **单调更新**，简洁高效。
>
> ---
>
> **4. 避免不必要的 `continue` 和 `if`**
>
> 原代码：
>
> ```python
> if key not in proc:
>     continue
> ```
>
> 优化：
>
> ```python
> proc.get(key, None)  # 直接返回 None，避免 continue 逻辑跳跃
> ```
>
> 不过这个优化 **可选**，因为 `continue` 仍然可以有效减少循环嵌套深度。
>
> ---
>
> **时间复杂度分析**
>
> | 操作                  | 复杂度       |
> | --------------------- | ------------ |
> | 计算前缀和 `P`        | `O(n)`       |
> | 遍历 `a, b` 组合      | `O(25)`      |
> | 分组存储前缀          | `O(n)`       |
> | 预处理前缀最小值      | `O(n log n)` |
> | 遍历 `pos` 并二分查找 | `O(n log n)` |
>
> **最终时间复杂度**：
> $
> O(25 \times (n + n \log n)) = O(n \log n)
> $
> 由于 `25` 是常数，这个解法对于 `n ≤ 30,000` **可以接受**。
>
> ---
>
> **最终优化结果**
>
> 1. **`defaultdict(list)` 替代手动字典初始化**
> 2. **`zip(*lst)` 直接提取列数据**
> 3. **预计算 `pre_min` 使用 `min_val` 直接更新**
> 4. **减少 `if` 和 `continue`**
> 5. **`O(n log n)` 复杂度，高效处理大数据**
>
> 这样优化后，代码更清晰、执行速度更快，能够顺利通过 `LeetCode` 的测试用例！





```python
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)

        P = [[0] * 5 for _ in range(n + 1)]
        for i, ch in enumerate(s):
            d = ord(ch) - ord("0")
            for j in range(5):
                P[i + 1][j] = P[i][j]
            P[i + 1][d] += 1

        ans = -(10**9)

        for a in range(5):
            for b in range(5):
                if a == b:
                    continue

                groups = {}
                for pa in (0, 1):
                    for pb in (0, 1):
                        groups[(pa, pb)] = []
                for i in range(n + 1):
                    pa = P[i][a] & 1
                    pb = P[i][b] & 1
                    d_val = P[i][a] - P[i][b]
                    groups[(pa, pb)].append((i, d_val, P[i][b]))

                proc = {}
                for key, lst in groups.items():

                    idx_arr = [t[0] for t in lst]
                    pb_arr = [t[2] for t in lst]
                    d_arr = [t[1] for t in lst]

                    pre_min = []
                    cur = 10**9
                    for d in d_arr:
                        if d < cur:
                            cur = d
                        pre_min.append(cur)
                    proc[key] = (idx_arr, pb_arr, pre_min, d_arr)

                for pos in range(k, n + 1):
                    pa = P[pos][a] & 1
                    pb = P[pos][b] & 1

                    key = (1 - pa, pb)
                    idx_arr, pb_arr, pre_min, _ = proc[key]

                    j1 = bisect_right(idx_arr, pos - k) - 1
                    j2 = bisect_right(pb_arr, P[pos][b] - 2) - 1
                    j = min(j1, j2)
                    if j >= 0:
                        cur = (P[pos][a] - P[pos][b]) - pre_min[j]
                        if cur > ans:
                            ans = cur
        return ans
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



## P1165 日志分析

辅助栈，懒删除，https://www.luogu.com.cn/problem/P1165

M 海运公司最近要对旗下仓库的货物进出情况进行统计。目前他们所拥有的唯一记录就是一个记录集装箱进出情况的日志。该日志记录了两类操作：第一类操作为集装箱入库操作，以及该次入库的集装箱重量；第二类操作为集装箱的出库操作。这些记录都严格按时间顺序排列。集装箱入库和出库的规则为先进后出，即每次出库操作出库的集装箱为当前在仓库里所有集装箱中最晚入库的集装箱。

出于分析目的，分析人员在日志中随机插入了若干第三类操作――查询操作。分析日志时，每遇到一次查询操作，都要报告出当前仓库中最大集装箱的重量。

**输入格式**

包含 $N+1$ 行：

第一行为一个正整数 $N$，对应于日志内所含操作的总数。

接下来的 $N$ 行，分别属于以下三种格式之一：

- 格式 1：`0 X`，表示一次集装箱入库操作，正整数 $X$ 表示该次入库的集装箱的重量。
- 格式 2：`1`，表示一次集装箱出库操作，（就当时而言）最后入库的集装箱出库。
- 格式 3：`2`，表示一次查询操作，要求分析程序输出当前仓库内最大集装箱的重量。

当仓库为空时你应该忽略出库操作，当仓库为空查询时你应该输出 $0$。

**输出格式**

输出行数等于日志中查询操作的次数。每行为一个整数，表示查询结果。

样例 #1

样例输入 #1

```
13
0 1
0 2
2
0 4
0 2
2
1
2
1
1
2
1
2
```

样例输出 #1

```
2
4
4
1
0
```

提示

数据范围及约定

- 对于 $20\%$ 的数据，有 $N \le 10$；
- 对于 $40\%$ 的数据，有 $N \le 1000$；
- 对于 $100\%$ 的数据，有 $1 \le N \le 200000$，$1 \le X \le 10^8$。



这道题本来想着用堆+懒删除做，但是确实不如使用辅助栈维护最大值。（参考快速堆猪，一样的道理）

```python
stack = []
for _ in range(int(input())):
	operation = list(map(int, input().split()))
	if operation[0] == 0:
		if stack:
			stack.append(max(stack[-1], operation[1]))
		else:
			stack.append(operation[1])
	elif operation[0] == 1:
		if stack:
			stack.pop()
	else:
		if stack:
			print(stack[-1])
		else:
			print(0)

```



懒删除

```python
import heapq

def main():
    N = int(input())

    stack = []
    max_heap = []
    max_heap_map = {}

    result = []

    for _ in range(N):
        op = list(map(int, input().split()))
        if op[0] == 0:
            weight = int(op[1])
            stack.append(weight)
            heapq.heappush(max_heap, -weight)
            if weight in max_heap_map:
                max_heap_map[weight] += 1
            else:
                max_heap_map[weight] = 1
        elif op[0] == 1:
            if stack:
                weight = stack.pop()
                max_heap_map[weight] -= 1
                if max_heap_map[weight] == 0:
                    del max_heap_map[weight]
        elif op[0] == 2:
            if max_heap:
                while max_heap and -max_heap[0] not in max_heap_map:
                    heapq.heappop(max_heap)
                if max_heap:
                    result.append(-max_heap[0])
                else:
                    result.append(0)
            else:
                result.append(0)

    for res in result:
        print(res)

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

