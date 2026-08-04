# Easy Problems in leetcode.cn

*Updated 2026-08-04 09:28 GMT+8*
 *Compiled by Hongfei Yan (2024 Fall)*



> Logs:
>
> 2026/8/04, md文件有1.5+MB，打开太慢了。我<mark>把“简单”开始题目，分到`2024fall_LeetCode_easy_problems.md`</mark>
>
> 2025/9/27, 此md文件有1.5+MB，打开太慢了。我<mark>把“挑战”开始题目，分到`2024fall_LeetCode_tough_problems.md`</mark>
>
> 2025/2/10，除了力扣的题目，“挑战”题目之后，放了几个其他网站的题目，如：洛谷
>
> 2025/1/27, 力扣题目难度分数，https://zerotrac.github.io/leetcode_problem_rating/#/
>
> 2024/11/14, 尽量先刷 LeetCode热题100， https://leetcode.cn/studyplan/top-100-liked/



# 简单Easy

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
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
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



## 13.罗马数字转整数

哈希表，https://leetcode.cn/problems/roman-to-integer/

罗马数字包含以下七种字符: `I`， `V`， `X`， `L`，`C`，`D` 和 `M`。

```
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

例如， 罗马数字 `2` 写做 `II` ，即为两个并列的 1 。`12` 写做 `XII` ，即为 `X` + `II` 。 `27` 写做 `XXVII`, 即为 `XX` + `V` + `II` 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 `IIII`，而是 `IV`。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 `IX`。这个特殊的规则只适用于以下六种情况：

- `I` 可以放在 `V` (5) 和 `X` (10) 的左边，来表示 4 和 9。
- `X` 可以放在 `L` (50) 和 `C` (100) 的左边，来表示 40 和 90。 
- `C` 可以放在 `D` (500) 和 `M` (1000) 的左边，来表示 400 和 900。

给定一个罗马数字，将其转换成整数。

 

**示例 1:**

```
输入: s = "III"
输出: 3
```

**示例 2:**

```
输入: s = "IV"
输出: 4
```

**示例 3:**

```
输入: s = "IX"
输出: 9
```

**示例 4:**

```
输入: s = "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
```

**示例 5:**

```
输入: s = "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
```

 

**提示：**

- `1 <= s.length <= 15`
- `s` 仅含字符 `('I', 'V', 'X', 'L', 'C', 'D', 'M')`
- 题目数据保证 `s` 是一个有效的罗马数字，且表示整数在范围 `[1, 3999]` 内
- 题目所给测试用例皆符合罗马数字书写规则，不会出现跨位等情况。
- IL 和 IM 这样的例子并不符合题目要求，49 应该写作 XLIX，999 应该写作 CMXCIX 。
- 关于罗马数字的详尽书写规则，可以参考 [罗马数字 - 百度百科](https://baike.baidu.com/item/罗马数字/772296)。



```python
class Solution:
    def romanToInt(self, s: str) -> int:
        # 罗马数字字符映射表
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000, 
            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 
            'CD': 400, 'CM': 900
        }
        
        num = 0
        i = 0
        while i < len(s):
            # 尝试读取两个字符的组合
            if i + 1 < len(s) and s[i:i+2] in roman_map:
                num += roman_map[s[i:i+2]]
                i += 2
            else:
                # 如果没有两个字符的组合，则读取一个字符
                num += roman_map[s[i]]
                i += 1
        return num
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

- `1 <= s.length <= 10^4`
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

linked list, recursion, https://leetcode.cn/problems/merge-two-sorted-lists/

将两个升序链表合并为一个新的 **升序** 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

**示例 1：**

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/merge_ex1.jpg" alt="img" style="zoom:67%;" />

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



用`dummy`节点，遍历两个链表，每次选择较小的加入链表。

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



递归，判断两个链表的节点哪个较小，较小的节点指向剩余链表合并后的结果，当两个链表都为空，终止递归。

```python
# Definition for singly-linked list.
# class ListNode:
# def __init__(self, val=0, next=None):
# self.val = val
# self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2
```



Q. leetcode上链表题的代码该怎么在本地运行？

> 你可以补全 `ListNode` 类，并添加一个辅助函数来构造和打印链表，这样代码可以在本地运行和测试。例如：  
>
> ```python
> from typing import Optional, List
> 
> # 定义链表节点
> class ListNode:
>     def __init__(self, val=0, next=None):
>         self.val = val
>         self.next = next
> 
> # 解决方案类
> class Solution:
>     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
>         # 创建一个哨兵节点（dummy node），简化边界条件处理
>         prehead = ListNode(-200)
>         prev = prehead
> 
>         # 遍历两个链表直到其中一个为空
>         while list1 and list2:
>             if list1.val <= list2.val:
>                 prev.next = list1
>                 list1 = list1.next
>             else:
>                 prev.next = list2
>                 list2 = list2.next            
>             prev = prev.next
> 
>         # 连接还未遍历完的那个链表
>         prev.next = list1 if list1 is not None else list2
> 
>         # 返回合并后的链表，跳过哨兵节点
>         return prehead.next
> 
> # 辅助函数：将列表转换为链表
> def list_to_linked_list(lst: List[int]) -> Optional[ListNode]:
>     if not lst:
>         return None
>     head = ListNode(lst[0])
>     current = head
>     for val in lst[1:]:
>         current.next = ListNode(val)
>         current = current.next
>     return head
> 
> # 辅助函数：打印链表
> def print_linked_list(head: Optional[ListNode]) -> None:
>     values = []
>     while head:
>         values.append(str(head.val))
>         head = head.next
>     print(" -> ".join(values) if values else "Empty List")
> 
> # 测试代码
> l1 = list_to_linked_list([1, 2, 4])
> l2 = list_to_linked_list([1, 3, 4])
> solution = Solution()
> merged_list = solution.mergeTwoLists(l1, l2)
> print_linked_list(merged_list)
> ```
>
> 运行步骤：
>
> 1. `list_to_linked_list([1, 2, 4])` 和 `list_to_linked_list([1, 3, 4])` 创建两个链表。
> 2. `mergeTwoLists(l1, l2)` 合并两个链表。
> 3. `print_linked_list(merged_list)` 以可读格式输出结果。
>
> 示例输出：
>
> ```
> 1 -> 1 -> 2 -> 3 -> 4 -> 4
> ```
> 这样，你可以在本地直接运行并调试代码！ 🚀



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

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` 为 **无重复元素** 的 **升序** 排列数组
- `-10^4 <= target <= 10^4`



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



## E66.加一

https://leetcode.cn/problems/plus-one/

给定一个表示 **大整数** 的整数数组 `digits`，其中 `digits[i]` 是整数的第 `i` 位数字。这些数字按从左到右，从最高位到最低位排列。这个大整数不包含任何前导 `0`。

将大整数加 1，并返回结果的数字数组。

 

**示例 1：**

```
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
加 1 后得到 123 + 1 = 124。
因此，结果应该是 [1,2,4]。
```

**示例 2：**

```
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
加 1 后得到 4321 + 1 = 4322。
因此，结果应该是 [4,3,2,2]。
```

**示例 3：**

```
输入：digits = [9]
输出：[1,0]
解释：输入数组表示数字 9。
加 1 得到了 9 + 1 = 10。
因此，结果应该是 [1,0]。
```

 

**提示：**

- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`
- `digits` 不包含任何前导 `0`。



```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = ''.join(map(str,digits))
        num = int(num_str) + 1
        return list(map(int, str(num)))
```



## E67.二进制求和

bit manipulation, string, simulation, https://leetcode.cn/problems/add-binary/



给你两个二进制字符串 `a` 和 `b` ，以二进制字符串的形式返回它们的和。

 

**示例 1：**

```
输入:a = "11", b = "1"
输出："100"
```

**示例 2：**

```
输入：a = "1010", b = "1011"
输出："10101"
```

 

**提示：**

- `1 <= a.length, b.length <= 10^4`
- `a` 和 `b` 仅由字符 `'0'` 或 `'1'` 组成
- 字符串如果不是 `"0"` ，就不含前导零



这是一个经典的**二进制加法模拟题**，可以像做十进制加法一样，从右往左逐位相加，并处理进位。

------

**解题思路：**

1. **初始化**：
   - 用一个变量 `carry` 表示进位（初始为 0）。
   - 用两个指针 `i`, `j` 分别从字符串 `a` 和 `b` 的末尾开始向前遍历。
   - 用一个列表 `res` 存储结果的每一位（因为字符串拼接效率低，先用 list 再 join）。
2. **循环条件**：
   - 当 `i >= 0` 或 `j >= 0` 或 `carry != 0` 时继续（防止最后还有进位）。
3. **每一步计算**：
   - 取当前位的数字（如果指针有效，否则为 0）。
   - 计算总和：`total = bit_a + bit_b + carry`
   - 当前位结果是 `total % 2`，进位是 `total // 2`
   - 将当前位插入结果（注意顺序，我们是从低位到高位算的，所以最后要反转）
4. **返回结果**：
   - 把 `res` 反转后拼成字符串。

------

**Python 代码实现：**

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []
        
        while i >= 0 or j >= 0 or carry:
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            
            total = bit_a + bit_b + carry
            res.append(str(total % 2))
            carry = total // 2
            
            i -= 1
            j -= 1
        
        return ''.join(reversed(res))
```

**复杂度分析：**

- **时间复杂度**：O(max(m, n))，其中 m、n 是 a 和 b 的长度。
- **空间复杂度**：O(max(m, n))，用于存储结果。

------

这个解法清晰、高效，且符合题目“不含前导零”的要求（因为我们是从实际计算得出的结果，不会多出前导零，除非结果就是 "0"，但题目保证输入非 "0" 时无前导零，而我们的算法在 a="0", b="0" 时也会正确返回 "0"）。

如有需要，也可以用位运算实现（将字符串转为整数再用 `bin()`），但当字符串很长（如 10^4 位）时会溢出或效率低，**模拟加法是最稳妥的方法**。





## E69.x 的平方根

binary search, https://leetcode.cn/problems/sqrtx/

给你一个非负整数 `x` ，计算并返回 `x` 的 **算术平方根** 。

由于返回类型是整数，结果只保留 **整数部分** ，小数部分将被 **舍去 。**

**注意：**不允许使用任何内置指数函数和算符，例如 `pow(x, 0.5)` 或者 `x ** 0.5` 。

**示例 1：**

```
输入：x = 4
输出：2
```

**示例 2：**

```
输入：x = 8
输出：2
解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
```

**提示：**

- `0 <= x <= 2^31 - 1`



```python
class Solution:
    def mySqrt(self, x: int) -> int:
        s = 1
        while s*s <= x:
            s += 1
        
        return s - 1
        
```



```python
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x + 1, 0
        while l < r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1 
            else:
                r = mid
        
        return ans
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



二叉树的中序遍历顺序是：**左子树 -> 根节点 -> 右子树**。

这里提供两种主流写法：**递归**（最直观）和 **迭代**（进阶要求，使用栈）。

**方法一：递归 (Recursion)**

递归是最简单的方法。我们定义一个辅助函数，先访问左子树，再记录当前节点值，最后访问右子树。

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def dfs(node):
            if not node:
                return
            # 1. 遍历左子树
            dfs(node.left)
            # 2. 访问根节点
            res.append(node.val)
            # 3. 遍历右子树
            dfs(node.right)
            
        dfs(root)
        return res
```

*   **时间复杂度**：$O(n)$，其中 $n$ 是节点数，每个节点访问一次。
*   **空间复杂度**：$O(n)$，最坏情况下（树呈链状）递归调用的栈深度为 $n$。

---

**方法二：迭代 (Iteration - 使用栈)**

进阶要求使用迭代。我们可以利用**显式栈**来模拟递归的过程：

1. 一直向左走，将路径上的节点全部入栈，直到尽头。
2. 从栈中弹出一个节点（这通常是当前最左的节点）。
3. 记录该节点的值。
4. 转向该节点的右子树，重复步骤 1。

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root
        
        while curr or stack:
            # 1. 尽可能向左走，并将沿途节点入栈
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 2. 当前节点为空，说明左边走到底了，弹出栈顶元素（最近的根节点）
            curr = stack.pop()
            res.append(curr.val)
            
            # 3. 转向右子树
            curr = curr.right
            
        return res
```

*   **时间复杂度**：$O(n)$。
*   **空间复杂度**：$O(n)$，栈的大小在最坏情况下等于树的高度。

---

**方法三：Morris 遍历 (进阶 - $O(1)$ 空间)**

如果面试官要求 **$O(1)$ 空间复杂度**（不考虑结果数组），可以使用 Morris 遍历。它通过修改树的空闲指针，利用叶子节点的右指针指向其中序遍历的后继节点，从而避免了使用栈。

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        curr = root
        
        while curr:
            if not curr.left:
                # 如果没有左孩子，直接访问当前节点，并进入右孩子
                res.append(curr.val)
                curr = curr.right
            else:
                # 找到左子树中序遍历的最后一个节点（最右侧节点）
                pre = curr.left
                while pre.right and pre.right != curr:
                    pre = pre.right
                
                if not pre.right:
                    # 建立临时链接，指向后继节点（当前节点）
                    pre.right = curr
                    curr = curr.left
                else:
                    # 链接已存在，说明左子树已访问完，断开链接，访问当前节点
                    pre.right = None
                    res.append(curr.val)
                    curr = curr.right
        return res
```

*   **时间复杂度**：$O(n)$，虽然有嵌套循环，但每条边最多被访问两次。
*   **空间复杂度**：$O(1)$（不计入结果列表）。



添加一个辅助函数来根据列表创建二叉树，然后调用这个函数来生成 `root` 节点。

```python
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        curr = root

        while curr:
            if not curr.left:
                # 如果没有左孩子，直接访问当前节点，并进入右孩子
                res.append(curr.val)
                curr = curr.right
            else:
                # 找到左子树中序遍历的最后一个节点（最右侧节点）
                pre = curr.left
                while pre.right and pre.right != curr:
                    pre = pre.right

                if not pre.right:
                    # 建立临时链接，指向后继节点（当前节点）
                    pre.right = curr
                    curr = curr.left
                else:
                    # 链接已存在，说明左子树已访问完，断开链接，访问当前节点
                    pre.right = None
                    res.append(curr.val)
                    curr = curr.right
        return res


def build_tree_from_list(values):
    """
    根据列表构建二叉树。
    列表按层序遍历顺序表示二叉树，None 表示空节点。
    """
    if not values:
        return None

    # 创建根节点
    root = TreeNode(values[0])
    # 使用队列进行层序构建
    queue = [root]
    i = 1

    while i < len(values):
        current_node = queue.pop(0)

        # 处理左子节点
        if i < len(values) and values[i] is not None:
            current_node.left = TreeNode(values[i])
            queue.append(current_node.left)
        i += 1

        # 处理右子节点
        if i < len(values) and values[i] is not None:
            current_node.right = TreeNode(values[i])
            queue.append(current_node.right)
        i += 1

    return root


if __name__ == "__main__":
    sol = Solution()
    # 1. 使用辅助函数将列表转换为 TreeNode 对象
    #root = build_tree_from_list([1, None, 2, 3])
    root = build_tree_from_list([1, 2, 3, 4, 5])
    """
          1
         / \
        2   3
       / \
      4   5
    """
    # 2. 将 TreeNode 对象传入方法
    print(sol.inorderTraversal(root))

# [4, 2, 5, 1, 3]
```



> Morris 遍历（Morris Traversal）的精髓在于：**利用二叉树中大量的空闲指针（叶子节点的右孩子指针），来保存临时信息，从而省去栈的空间。**
>
> 它的核心目标是：**在左子树遍历完后，能通过某种方式“走回来”找到根节点。**
>
> ---
>
> **1. 核心逻辑（直白版）**
>
> 假设当前节点为 `curr`：
>
> 1.  **如果 `curr` 没有左孩子**：
>     *   说明左边没东西了，直接**打印 `curr`**。
>     *   然后去右边：`curr = curr.right`。
> 2.  **如果 `curr` 有左孩子**：
>     *   我们要找 `curr` 的**前驱节点**（即：左子树中最后被访问的那个点，也就是左子树里“最右边”的节点）。
>     *   **情况 A（还没建立连接）**：如果前驱节点的右孩子是空的，我们就把它连到 `curr` 上：`pre.right = curr`。然后继续去左子树：`curr = curr.left`。
>     *   **情况 B（已经建立过连接）**：如果前驱节点的右孩子指向 `curr`，说明这是第二次回来，左子树已经走完了。此时我们要**断开连接**（恢复树结构），**打印 `curr`**，然后去右边：`curr = curr.right`。
>
> ---
>
> **2. 详细图解示例**
>
> 假设我们有这样一颗二叉树：
>
> ```
>       1
>      / \
>     2   3
>    / \
>   4   5
> ```
>
> **目标中序遍历结果：`[4, 2, 5, 1, 3]`**
>
> **第一阶段：从根节点 1 开始**
>
> *   `curr` 在 **1**。它有左孩子（2）。
> *   找到 1 的前驱（左子树最右节点）：是 **5**。
> *   5 的右孩子为空，建立连接：`5.right = 1`。
> *   `curr` 移向左孩子 **2**。
>     *   *此时树的样子（逻辑上）：4 -> 2 -> 5 -> 1 -> 3*
>
>     **第二阶段：处理节点 2**
>
> *   `curr` 在 **2**。它有左孩子（4）。
> *   找到 2 的前驱（左子树最右节点）：是 **4**。
> *   4 的右孩子为空，建立连接：`4.right = 2`。
> *   `curr` 移向左孩子 **4**。
>
> **第三阶段：处理节点 4**
>
> *   `curr` 在 **4**。它**没有**左孩子。
> *   **打印 4**。
> *   `curr` 移向 `curr.right`。由于刚才连了线，它回到了 **2**。
>
> **第四阶段：回到节点 2**
>
> *   `curr` 在 **2**。它有左孩子（4）。
> *   找到 2 的前驱：还是 **4**。
> *   发现 `4.right` 已经指向了 `curr`(2)。
> *   **说明左边全走完了！**
> *   **断开连接**：`4.right = None`。
> *   **打印 2**。
> *   `curr` 移向右孩子 **5**。
>
> **第五阶段：处理节点 5**
>
> *   `curr` 在 **5**。它**没有**左孩子。
> *   **打印 5**。
> *   `curr` 移向 `curr.right`。由于第一阶段连了线，它回到了 **1**。
>
> **第六阶段：回到节点 1**
>
> *   `curr` 在 **1**。它有左孩子（2）。
> *   找到 1 的前驱：是 **5**（沿着 2 -> 5 找到）。
> *   发现 `5.right` 已经指向了 `curr`(1)。
> *   **说明左边全走完了！**
> *   **断开连接**：`5.right = None`。
> *   **打印 1**。
> *   `curr` 移向右孩子 **3**。
>
> **第七阶段：处理节点 3**
>
> *   `curr` 在 **3**。没有左孩子。
> *   **打印 3**。
> *   `curr` 移向 `curr.right`（None）。
> *   **结束。**
>
> ---
>
> **3. 总结**
>
> | 步骤     | 打印结果 | 说明                              |
> | :------- | :------- | :-------------------------------- |
> | 1. 遇到1 |          | 建立 5 -> 1 的线，去2             |
> | 2. 遇到2 |          | 建立 4 -> 2 的线，去4             |
> | 3. 遇到4 | **4**    | 无左孩子，打印并沿线回2           |
> | 4. 回到2 | **2**    | 发现 4 -> 2 已存，拆线，打印，去5 |
> | 5. 遇到5 | **5**    | 无左孩子，打印并沿线回1           |
> | 6. 回到1 | **1**    | 发现 5 -> 1 已存，拆线，打印，去3 |
> | 7. 遇到3 | **3**    | 无左孩子，打印，结束              |
>
> **核心精髓：**
>
> 1.  **线索化**：把原本是 `None` 的右指针利用起来，指向中序遍历的后继。
> 2.  **原地修改，原地恢复**：访问完后把线拆掉，不破坏原树结构。
> 3.  **空间 $O(1)$**：除了保存结果的数组，只用了两个辅助指针（`curr` 和 `pre`），没有用栈，也没有递归。





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



用stack模拟的“颜色填充法”，和递归的思路其实很相似。

核心思想如下：

- 使用颜色标记节点的状态，新节点为白色，已访问的节点为灰色。
- 如果遇到的节点为白色，则将其标记为灰色，然后将其右子节点、自身、左子节点依次入栈。
- 如果遇到的节点为灰色，则将节点的值输出。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        white, gray = 0, 1
        res = []
        stack = [(white, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == white:
                stack.append((white, node.right))
                stack.append((gray, node))
                stack.append((white, node.left))
            else:
                res.append(node.val)
        return res
```





非递归写法

```python
# 戴嘉震 24信科学院
from typing import Optional, List

#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        result = []
        while stack:
            top = stack.pop()
            if top == None:
                continue
            if isinstance(top, TreeNode):
                stack.append(top.right)
                stack.append(top.val)
                stack.append(top.left)
            else:
                result.append(top)
        return result
```



【傅坚军】思路：该方法通过迭代方式模拟递归过程：将当前节点的所有左子节点压入栈中，直到最左侧叶子节点。然后弹出栈顶元素（当前最左侧节点），将其值加入结果列表。将当前指针转向该节点的右子节点，重复上述过程。
用时约20分钟

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
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

tree, dfs, https://leetcode.cn/problems/maximum-depth-of-binary-tree/

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

- 树中节点的数量在 `[0, 10^4]` 区间内。
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

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` 按 **严格递增** 顺序排列



由有序数组想到中序遍历，选择中间位置的数作为二叉树的根节点。

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



## E110.平衡二叉树

binary tree, https://leetcode.cn/problems/balanced-binary-tree/

给定一个二叉树，判断它是否是 平衡二叉树 

 

**示例 1：**

<img src="https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg" alt="img" style="zoom: 67%;" />

```
输入：root = [3,9,20,null,null,15,7]
输出：true
```

**示例 2：**

<img src="https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg" alt="img" style="zoom:67%;" />

```
输入：root = [1,2,2,3,3,null,null,4,4]
输出：false
```

**示例 3：**

```
输入：root = []
输出：true
```

 

**提示：**

- 树中的节点数在范围 `[0, 5000]` 内
- `-104 <= Node.val <= 10^4`



这个问题可以通过递归来解决。

**1. 核心概念**

一个二叉树是**平衡**的，当且仅当：

1. 它的左子树是平衡的。
2. 它的右子树是平衡的。
3. 左子树和右子树的高度差（绝对值）不超过 1。

**2. 解题思路：自底向上（最优解）**

如果我们采用自顶向下的方法，会对同一个节点多次调用高度函数，导致时间复杂度较高 $O(n^2)$。

**自底向上**的方法类似于后序遍历（左-右-中）：

- 对于当前遍历到的节点，先递归地判断其左右子树是否平衡。
- 如果左子树或右子树中有一个不平衡，则整个树不平衡，直接返回 `-1`（标记位）。
- 如果都是平衡的，检查当前节点的左右子树高度差：
  - 差值大于 1：返回 `-1`。
  - 差值小于等于 1：返回当前节点的高度（即 `max(左子树高度, 右子树高度) + 1`）。

  **3. 代码实现**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 辅助函数：计算高度的同时判断是否平衡
        def getHeight(node) -> int:
            if not node:
                return 0
            
            # 1. 递归获取左子树高度
            left_height = getHeight(node.left)
            # 如果左子树已经不平衡了，直接向上层层返回 -1
            if left_height == -1:
                return -1
            
            # 2. 递归获取右子树高度
            right_height = getHeight(node.right)
            # 如果右子树已经不平衡了，直接返回 -1
            if right_height == -1:
                return -1
            
            # 3. 检查当前节点是否平衡
            # 如果左右高度差 > 1，说明以当前节点为根的子树不平衡
            if abs(left_height - right_height) > 1:
                return -1
            
            # 4. 如果平衡，返回当前节点的高度
            return max(left_height, right_height) + 1

        # 如果返回值不是 -1，说明整棵树平衡
        return getHeight(root) != -1
```

**4. 复杂度分析**

*   **时间复杂度：$O(n)$**
    其中 $n$ 是二叉树中的节点个数。每个节点只会被访问一次，计算高度的时间复杂度是 $O(1)$。
*   **空间复杂度：$O(n)$**
    在最坏情况下（树呈现链状），递归栈的深度为 $n$。如果树是完全平衡的，空间复杂度为 $O(\log n)$。

    **5. 为什么这是最优解？**

    因为我们只需一次遍历（Post-order traversal）。在求高度的过程中顺便把平衡性给检查了，一旦发现任何一个子树不平衡，就立即通过 `-1` 信号“剪枝”停止后续多余的计算。





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



思路：关键在于对齐数字

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1,i):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
        return ans
```



思路：使用二维列表储存杨辉三角，先将两端赋值为1，然后逐层计算。

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

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`



```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0

        min_v = prices[0]  # 记录最低买入价
        max_profit = 0  # 记录最大利润

        for price in prices[1:]:  # 从第二天开始遍历
            min_v = min(min_v, price)  # 更新最低买入价
            max_profit = max(max_profit, price - min_v)  # 计算最大利润

        return max_profit

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([2, 4, 1]))  # 2
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
    print(solution.maxProfit([7, 6, 4, 3, 1]))  # 0
```



## 125.验证回文串

https://leetcode.cn/problems/valid-palindrome/

如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 **回文串** 。

字母和数字都属于字母数字字符。

给你一个字符串 `s`，如果它是 **回文串** ，返回 `true` ；否则，返回 `false` 。

 

**示例 1：**

```
输入: s = "A man, a plan, a canal: Panama"
输出：true
解释："amanaplanacanalpanama" 是回文串。
```

**示例 2：**

```
输入：s = "race a car"
输出：false
解释："raceacar" 不是回文串。
```

**示例 3：**

```
输入：s = " "
输出：true
解释：在移除非字母数字字符之后，s 是一个空字符串 "" 。
由于空字符串正着反着读都一样，所以是回文串。
```

 

**提示：**

- `1 <= s.length <= 2 * 10^5`
- `s` 仅由可打印的 ASCII 字符组成



```python
class Solution:
    def isPalindrome(self, s: str) -> bool:       
        s_filtered = ''.join(c.lower() for c in s if c.isalnum())

        left, right = 0, len(s_filtered) - 1
        while left < right:
            if s_filtered[left] == s_filtered[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True
```





## 136.只出现一次的数字

bit manipulation, https://leetcode.cn/problems/single-number/

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

- `1 <= nums.length <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`
- 除了某个元素只出现一次以外，其余每个元素均出现两次。



```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        for i in range(1,n):
            ans ^= nums[i]
        
        return ans
```



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

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png" alt="img" style="zoom: 50%;" />

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



快慢指针

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True
```



## E160.相交链表

two pointers, https://leetcode.cn/problems/intersection-of-two-linked-lists/

给你两个单链表的头节点 `headA` 和 `headB` ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 `null` 。

图示两个链表在节点 `c1` 开始相交**：**

[<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_statement.png" alt="img" style="zoom: 50%;" />](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_statement.png)

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

[<img src="https://assets.leetcode.com/uploads/2021/03/05/160_example_1_1.png" alt="img" style="zoom: 50%;" />](https://assets.leetcode.com/uploads/2018/12/13/160_example_1.png)

```
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,6,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
— 请注意相交节点的值不为 1，因为在链表 A 和链表 B 之中值为 1 的节点 (A 中第二个节点和 B 中第三个节点) 是不同的节点。换句话说，它们在内存中指向两个不同的位置，而链表 A 和链表 B 中值为 8 的节点 (A 中第三个节点，B 中第四个节点) 在内存中指向相同的位置。
```

 

**示例 2：**

[<img src="https://assets.leetcode.com/uploads/2021/03/05/160_example_2.png" alt="img" style="zoom: 50%;" />](https://assets.leetcode.com/uploads/2018/12/13/160_example_2.png)

```
输入：intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Intersected at '2'
解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [1,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
```

**示例 3：**

[<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_example_3.png" alt="img" style="zoom: 50%;" />](https://assets.leetcode.com/uploads/2018/12/13/160_example_3.png)

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
- `1 <= m, n <= 3 * 10^4`
- `1 <= Node.val <= 10^5`
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

> 【刘家亦，24物理学院】
>
> 思路乍看很神奇，其实不难想到，只要遵循一个原则：在单边列表中，只有步数是可以控制的，只能利用步数进行计时，所以我们必须要找到两个链表从头出发如何经过相同的步数到达同点。



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



思路：既然两个链表的值均为正数，那么先遍历一次链表A，将其所有值变为相反数。再遍历一次链表B，如果遇到了负数，说明这就是其与A相交的点。注意要把链表A的值改回来。也可以用标准的双指针方法，时间复杂度是一致的。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cur = headA
        while cur:
            cur.val = -cur.val
            cur = cur.next
        cur = headB
        inter = None
        while cur:
            if cur.val < 0:
                inter = cur
                break
            cur = cur.next
        cur = headA
        while cur:
            cur.val = -cur.val
            cur = cur.next
        return inter
```



## 169.多数元素

Boyer-Moore, https://leetcode.cn/problems/majority-element/

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
- `1 <= n <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

 

**进阶：**尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。



可以用 **Boyer-Moore 投票算法** 在 **O(n) 时间复杂度** 和 **O(1) 空间复杂度** 内解决。

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = None, 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
```

性质保证正确性：由于多数元素 **出现次数超过 ⌊n/2⌋**，所以即使有抵消，其仍然会成为最终 `candidate`。

> **Boyer-Moore 投票算法**（Boyer-Moore Majority Vote Algorithm）是一种高效的算法，专门用于在一个序列中寻找**多数元素**（Majority Element）。
>
> 所谓的“多数元素”，是指在一个长度为 $n$ 的数组中，出现次数**大于** $\lfloor n/2 \rfloor$ 的元素。
>
> **1. 核心思想：两两抵消**
>
> 该算法的核心直觉非常简单：**在数组中，如果每次都删去两个不同的元素，最后剩下的如果还有元素，那么这个元素就可能是多数元素。**
>
> 因为多数元素的出现次数超过了一半，即便它和其他所有非多数元素一对一“同归于尽”，最后剩下的也一定会是它。
>
> ---
>
> **2. 算法步骤**
>
> 算法通常分为两个阶段：
>
> **第一阶段：寻找候选人 (Candidate)**
>
> 初始化两个变量：`candidate`（候选人）和 `count`（票数计数器，初始为 0）。
> 遍历数组中的每个元素 `x`：
> 1. 如果 `count == 0`，则将当前元素 `x` 设为 `candidate`，并将 `count` 设为 1。
> 2. 如果 `x == candidate`，则 `count++`。
> 3. 如果 `x != candidate`，则 `count--`。
>
> **第二阶段：验证候选人 (Verification)**
>
> 第一阶段结束后得到的 `candidate` **不一定**就是多数元素（例如数组为 `[1, 2, 3]` 时，最后候选人可能是 3，但它不是多数元素）。
> *   **如果题目保证一定存在多数元素**，则无需第二阶段，`candidate` 即为答案。
> *   **如果不保证存在**，则需要再次遍历数组，统计 `candidate` 出现的实际次数。如果次数 $> n/2$，则它是多数元素；否则，该数组不存在多数元素。
>
> ---
>
> **3. 复杂度分析**
>
> *   **时间复杂度：$O(n)$**。只需要遍历一次数组即可找到候选人（如果需要验证，则遍历两次），依然是线性的。
> *   **空间复杂度：$O(1)$**。只使用了两个变量（`candidate` 和 `count`），不需要额外的哈希表或排序空间。
>
> ---
>
> **4. 代码示例 (Python)**
>
> ```python
> def majority_element(nums):
>     candidate = None
>     count = 0
>     
>     # 第一阶段：投票
>     for num in nums:
>         if count == 0:
>             candidate = num
>             count = 1
>         elif num == candidate:
>             count += 1
>         else:
>             count -= 1
>             
>     # 第二阶段：验证（可选）
>     if nums.count(candidate) > len(nums) // 2:
>         return candidate
>     else:
>         return None
> ```
>
> ---
>
> **5. 直观类比：帮派混战**
>
> 想象一个战场上有好几个帮派。每个士兵遇到**同帮派**的人就会聚在一起（`count++`），遇到**不同帮派**的人就会同归于尽（`count--`）。
> *   如果一个帮派的人数超过了所有人的一半，那么无论其他帮派如何联合，最后战场上剩下的那个人一定属于这个人数最多的帮派。
>
> **6. 算法扩展**
>
> *   **寻找出现次数超过 $n/3$ 的元素**：可以维护两个候选人和两个计数器。如果有两个候选人出现次数都超过 $n/3$，它们加起来不超过 $2n/3$，剩余元素也不足 $n/3$。同理可推广到寻找出现次数超过 $n/k$ 的元素。
> *   **LeetCode 相关题目**：
>     *   [169. 多数元素](https://leetcode.cn/problems/majority-element/)（$n/2$ 情况）
>     *   [229. 多数元素 II](https://leetcode.cn/problems/majority-element-ii/)（$n/3$ 情况）



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



## E190.颠倒二进制位

bit manipulation, divide and conquer, https://leetcode.cn/problems/reverse-bits/

颠倒给定的 32 位有符号整数的二进制位。

 

**示例 1：**

**输入：**n = 43261596

**输出：**964176192

**解释：**

| 整数      | 二进制                           |
| --------- | -------------------------------- |
| 43261596  | 00000010100101000001111010011100 |
| 964176192 | 00111001011110000010100101000000 |

**示例 2：**

**输入：**n = 2147483644

**输出：**1073741822

**解释：**

| 整数       | 二进制                           |
| ---------- | -------------------------------- |
| 2147483644 | 01111111111111111111111111111100 |
| 1073741822 | 00111111111111111111111111111110 |

 

**提示：**

- `0 <= n <= 2^31 - 2`
- `n` 为偶数

 

**进阶**: 如果多次调用这个函数，你将如何优化你的算法？



逻辑：将整数转为二进制字符串，补足 32 位，反转后再转回整数。

**方法一：使用格式化字符串（推荐，简洁高效）**

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        # 格式化为32位二进制字符串，高位补0，然后反转
        return int(f"{n:032b}"[::-1], 2)
```

**优点**：

- 一行完成补零、反转、转整数。
- `f"{n:032b}"` 是 Python 内置的高效格式化方式。
- 可读性强。

------

**方法二：位运算（更贴近底层，适合面试展示）**

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res
```

**优点**：

- 不依赖字符串操作，纯位运算，效率更高（尤其在 C/C++/Java 中优势明显）。
- 展示对位操作的理解。

**说明**：

- 每次取 `n` 的最低位（`n & 1`），放到 `res` 的末尾。
- `res` 左移腾出位置，`n` 右移取出下一位。
- 循环 32 次确保处理全部位。

**总结：**

- **日常开发/LeetCode**：用 **方法一**（格式化 + 切片），简洁清晰。
- **算法面试/追求极致性能**：用 **方法二**（位运算），体现基本功。



```python
class Solution:
    def reverseBits(self, n: int) -> int:
        M1 = 0x55555555  # 01010101010101010101010101010101
        M2 = 0x33333333  # 00110011001100110011001100110011
        M4 = 0x0f0f0f0f  # 00001111000011110000111100001111
        M8 = 0x00ff00ff  # 00000000111111110000000011111111
        
        n = n & 0xFFFFFFFF
        n = (n >> 1 & M1) | ((n & M1) << 1)
        n = (n >> 2 & M2) | ((n & M2) << 2)
        n = (n >> 4 & M4) | ((n & M4) << 4)
        n = (n >> 8 & M8) | ((n & M8) << 8)
        return ((n >> 16) | (n << 16)) & 0xFFFFFFFF

```

> 这段代码实现的是**32位二进制逆序**，它采用的是一种非常高效的**分治法（Divide and Conquer）**，也常被称为“位级归并排序”思想。
>
> 相比于普通的循环 32 次逐位移动，这种方法的时间复杂度是 $O(\log W)$，其中 $W$ 是位数（这里 $W=32$，所以只需 5 步操作）。
>
> **1. 核心思想：分而治之**
>
> 如果我们想翻转一个长度为 32 的序列，可以：
>
> 1. 交换相邻的 **1位** 组。
> 2. 交换相邻的 **2位** 组。
> 3. 交换相邻的 **4位** 组。
> 4. 交换相邻的 **8位** 组。
> 5. 交换相邻的 **16位** 组。
>
> 完成这 5 步后，整个 32 位就彻底颠倒过来了。
>
> ---
>
> **2. 掩码（Mask）的作用**
>
> 代码中定义的 `M1, M2, M4, M8` 是用来定位我们要操作的“块”的：
>
> *   **`M1 = 0x55555555`**: 二进制是 `01010101...`（奇数位为1）。用于处理 **1位** 组。
> *   **`M2 = 0x33333333`**: 二进制是 `00110011...`（每2位一组，后2位为1）。用于处理 **2位** 组。
> *   **`M4 = 0x0f0f0f0f`**: 二进制是 `00001111...`（每4位一组，后4位为1）。用于处理 **4位** 组。
> *   **`M8 = 0x00ff00ff`**: 二进制是 `0000000011111111...`（每8位一组，后8位为1）。用于处理 **8位** 组。
>
> ---
>
> **3. 逐行图解**
>
> 以 `n = (n >> 1 & M1) | ((n & M1) << 1)` 为例：
>
> *   `(n & M1) << 1`: 把所有位于“偶数位”的数字提取出来，向左移动一位，移到奇数位。
> *   `n >> 1 & M1`: 把所有位于“奇数位”的数字向右移动一位，移到偶数位。
> *   `|`: 合并两者。效果是：**相邻的两位互换了位置**。
>
> **演示（简化为8位）：**
>
> 假设 `n = 10 11 01 00`
>
> 1.  **交换相邻 1 位：**
>     `10 11 01 00` -> `01 11 10 00`
> 2.  **交换相邻 2 位：**
>     `0111 1000` -> `1101 0010`
> 3.  **交换相邻 4 位：**
>     `11010010` -> `00101101` (完成逆序)
>
> ---
>
> **4. 代码步骤拆解**
>
> ```python
> # 1. 确保是32位无符号数
> n = n & 0xFFFFFFFF 
> 
> # 2. 交换相邻的 1 位
> # 原理：ab cd ef gh -> ba dc fe hg
> n = (n >> 1 & M1) | ((n & M1) << 1)
> 
> # 3. 交换相邻的 2 位
> # 原理：[ba][dc] [fe][hg] -> [dc][ba] [hg][fe]
> n = (n >> 2 & M2) | ((n & M2) << 2)
> 
> # 4. 交换相邻的 4 位
> # 原理：[dcba][hgfe] -> [hgfe][dcba]
> n = (n >> 4 & M4) | ((n & M4) << 4)
> 
> # 5. 交换相邻的 8 位
> n = (n >> 8 & M8) | ((n & M8) << 8)
> 
> # 6. 交换相邻的 16 位 (高16位和低16位互换)
> # 最后一步不需要掩码，因为 16+16 正好是 32 位
> return ((n >> 16) | (n << 16)) & 0xFFFFFFFF
> ```
>
> **5. 为什么这么做？**
>
> *   **性能极高**：不需要写 `for i in range(32)`。对于 CPU 来说，位运算（与、或、移位）是非常基础且极快的指令。
> *   **并行思想**：这种方法实际上是在同一时间“批量”处理了 16 对、8 对、4 对、2 对、1 对位的交换。
> *   **适用场景**：在嵌入式开发、图形学、加密算法或对性能要求极高的底层驱动中，这种位操作技巧非常经典。
>
> **总结**
>
> 这段代码是用**位运算实现的分治算法**，通过不断成倍扩大交换单位（1->2->4->8->16），最终在 5 步内完成了 32 位二进制的左右翻转。



## E191.位1的个数

bit manipulation, divide and conquer, https://leetcode.cn/problems/number-of-1-bits/

给定一个正整数 `n`，编写一个函数，获取一个正整数的二进制形式并返回其二进制表达式中 设置位 的个数（也被称为[汉明重量](https://baike.baidu.com/item/汉明重量)）。

汉明重量是符号序列中非零符号的数量，在二进制数据中特指1的个数

**示例 1：**

```
输入：n = 11
输出：3
解释：输入的二进制串 1011 中，共有 3 个设置位。
```

**示例 2：**

```
输入：n = 128
输出：1
解释：输入的二进制串 10000000 中，共有 1 个设置位。
```

**示例 3：**

```
输入：n = 2147483645
输出：30
解释：输入的二进制串 1111111111111111111111111111101 中，共有 30 个设置位。
```

**提示：**

- `1 <= n <= 2^31 - 1`

 **进阶**：

- 如果多次调用这个函数，你将如何优化你的算法？



这个问题是关于计算一个正整数二进制表示中 `1` 的个数（汉明重量）。

下面为您提供几种不同的解决方法，以及针对“多次调用”进阶问题的优化思路。

---

### 方法一：Brian Kernighan 算法（最经典的位运算方法）

**思路：**
利用 `n & (n - 1)`。这个操作可以**消除**二进制表示中最低位的 `1`。
例如：对于 `n = 12 (1100)`：

1. `n - 1 = 11 (1011)`，`1100 & 1011 = 1000`（清除了最低位的 `1`）。
2. 重复上述操作，直到 `n` 变为 `0`。循环执行的次数就是二进制中 `1` 的个数。

这种方法的时间复杂度取决于 `1` 的个数，而不是二进制的位数，因此非常高效。

**代码实现：**

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count
```

- **时间复杂度**：$O(k)$，其中 $k$ 是 `n` 的二进制表示中 `1` 的个数，最坏情况下为 $O(32)$。
- **空间复杂度**：$O(1)$。

---

### 方法二：利用内置函数（最简短的 Pythonic 方法）

**思路：**
在 Python 3.10 及以上版本中，可以直接使用 `int.bit_count()` 方法。在旧版本中，也可以使用 `bin(n).count('1')`。

**代码实现：**

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()  # Python 3.10+
        # 或者使用：return bin(n).count('1')
```

- **时间复杂度**：$O(\log n)$。
- **空间复杂度**：$O(1)$（若使用 `bin`，则为 $O(\log n)$ 字符串开销）。

---

### 进阶：如何应对多次调用（优化方案）

如果这个函数被频繁、海量地调用，可以通过**查表法（Lookup Table）**进行空间换时间的优化。

**思路：**
一个 32 位的整数可以被拆分为 4 个 8 位的字节（Byte），或者 2 个 16 位的半字。
我们可以预先计算好所有 8 位整数（0 到 255）中 `1` 的个数，并存入一个长度为 256 的数组。
对于输入的任意 32 位整数，我们只需要将其拆分为 4 个字节，分别查表，然后将结果相加。

这样，每次查询只需要进行 4 次移位/按位与操作以及 4 次数组查询。

**代码实现：**

```python
class Solution:
    # 类变量：只在类加载时初始化一次 256 大小的查找表
    # 也可以使用 @cache / @lru_cache 装饰器实现缓存
    _lookup = [0] * 256
    for i in range(256):
        _lookup[i] = (i & 1) + _lookup[i >> 1]

    def hammingWeight(self, n: int) -> int:
        # 将 32 位整数拆分为 4 个 8 位组分别查表
        return (
            self._lookup[n & 0xFF] +
            self._lookup[(n >> 8) & 0xFF] +
            self._lookup[(n >> 16) & 0xFF] +
            self._lookup[(n >> 24) & 0xFF]
        )
```

- **初始化时间复杂度**：$O(256) = O(1)$
- **单次查询时间复杂度**：$O(1)$
- **空间复杂度**：$O(256)$ 存储查找表。

如果多次调用的参数重复率极高，还可以直接利用 Python 的 `@functools.lru_cache` 装饰器对函数进行缓存，以便直接返回已计算过的值。





## E206.反转链表

three pinters, recursion, https://leetcode.cn/problems/reverse-linked-list/

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



使用三个指针（prev, current, next_node）迭代整个链表，将当前节点的 next 指针指向前一个节点，从而实现链表反转，最后返回 prev 作为新的头节点。

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



递归的反转写法

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head  # 基本情况：空链表或只有一个节点的链表直接返回头节点
        p = self.reverseList(head.next)  # 递归反转剩余链表
        head.next.next = head  # 反转当前节点的指针
        head.next = None  # 设置当前节点的next为None
        return p  # 返回新的头节点
```

> 【# 汤伟杰，信息管理系】
>
> 思路：这是在寒假期间做的，当时被递归的写法迷惑了一下午。递归的思路妙就妙在这个函数的返回值上：
>
> ​	在链表不为空或者长度不为1的时候，这个函数体的第一行就进行了函数调用，并将返回值赋给了reversed_head；然后整个函数返回的也是这个reversed_head。经过一阵思考才发现，哦，原来这一行函数调用，实际上是调用了n次（n是链表长度-1），也就是说，一旦调用了这个函数，就会一直调用到这个链表的最后一个节点，才会达到退出条件，并返回这个最终节点。而实际上，它就是想要的最终返回结果，因此把这个节点直接赋值给reversed_head，同时通过将整个函数的返回值也设置为这个变量以保证在回溯时该变量能够不断**原地赋值**（自己给自己赋值）。因此，在调用递归函数这一行的下面两行，实际上是在对当前递归到的节点的**下一个节点的next指针**调整到**自己身上**，并且把**自己的当前next指针**调整为**None**，这样也保证了链表的单向性。总之，这个递归很烧脑，但是想清楚了很通透！



> 这段递归反转链表的写法，做一个逐层剖析。它“烧脑”的地方确实在于：**函数返回值的传递** + **回溯时指针的调整**。
>
> ------
>
> **代码**
>
> ```python
> class Solution:
>     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
>         if head is None or head.next is None:
>             return head  # 递归出口：空链表或最后一个节点
>         
>         p = self.reverseList(head.next)  # 递归反转子链表
>         head.next.next = head  # 将子链表的尾部指向自己
>         head.next = None       # 断开自己和子链表的旧连接
>         return p               # 返回新的头节点
> ```
>
> ------
>
> **分解理解**
>
> 1. 递归出口
>
> ```python
> if head is None or head.next is None:
>     return head
> ```
>
> - 当到达最后一个节点（或空链表）时，直接返回它。
> - **关键点**：这个返回值会在整个递归回溯过程中，一直“往上传递”，最终成为新链表的头。
>
> ------
>
> 2. 递归调用
>
> ```python
> p = self.reverseList(head.next)
> ```
>
> - 假设链表是 `1 -> 2 -> 3 -> 4 -> 5`。
> - 当 `head = 1` 时，这行代码会不断调用自己，直到 `head = 5` 时触发退出条件。
> - 从最深层开始返回，`p` 永远是“反转后的新链表的头节点”。
>   - 所以不论当前递归在哪一层，`p` 始终指向 `5`。
>
> ------
>
> 3. 回溯阶段的指针翻转
>
> ```python
> head.next.next = head
> head.next = None
> ```
>
> - 当递归回到 `head = 4` 时：
>   - `head.next` 是 `5`，
>   - 所以 `head.next.next = head` 把 `5.next` 指向 `4`，形成 `5 -> 4`。
>   - 然后 `head.next = None` 把 `4` 的旧指向断开，避免链表成环。
> - 回溯到 `head = 3`：
>   - `head.next` 是 `4`（但现在 `4 -> None`，`5 -> 4`），
>   - 所以 `head.next.next = head`，把 `4.next` 指向 `3`，形成 `5 -> 4 -> 3`。
>   - 再断开 `3 -> 4` 的旧链。
> - 一直回溯到 `head = 1`，最终形成 `5 -> 4 -> 3 -> 2 -> 1`。
>
> ------
>
> 4. 返回新头节点
>
> ```python
> return p
> ```
>
> - 不管在哪一层递归，`p` 都指向 **反转后的新链表的头**（也就是最初的尾节点）。
> - 所以最终 `reverseList(head)` 返回的就是整个新链表的头节点。
>
> ------
>
> **递归反转的精髓**
>
> 1. **递归到底** → 找到最后一个节点，作为新头。
> 2. **回溯时翻转** → 把“下一个节点”的 `next` 指向自己。
> 3. **断开旧链路** → 避免形成环。
> 4. **始终返回新头** → 保证调用链一路把新头传上来。
>
> ------
>
> 小技巧
>
> 想象一下栈：
>
> - **递归入栈**：一路走到链表的最后。
> - **递归出栈**：在出栈时逐一“掉头”，像一行人走到尽头，逐个转身，最终整个队伍方向掉转。



反转链表是链表操作中的经典题目。我们可以通过**迭代**和**递归**两种方式来实现。

**方法一：迭代（双指针）**

这是最直观且空间效率最高的方法。我们使用两个指针 `prev`（前驱节点）和 `curr`（当前节点）。在遍历过程中，不断改变 `curr.next` 的指向。

**逻辑步骤：**

1. 初始化 `prev` 为 `None`，`curr` 为 `head`。
2. 循环遍历：
   - 先存下 `curr` 的下一个节点 `next_node = curr.next`（防止链表断开）。
   - 将 `curr.next` 指向 `prev`（实现反转）。
   - 移动 `prev` 和 `curr`：`prev` 变成当前的 `curr`，`curr` 变成刚才存下的 `next_node`。
3. 当 `curr` 变成 `None` 时，`prev` 就是新的头节点。

**代码实现：**

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  # 1. 临时保存后续节点
            curr.next = prev       # 2. 反转指针
            prev = curr            # 3. prev 前进
            curr = next_node       # 4. curr 前进
            
        return prev
```

- **时间复杂度**：$O(n)$，其中 $n$ 是链表的长度。
- **空间复杂度**：$O(1)$。

---

**方法二：递归**

递归法的思路是：先反转后面的链表，然后再把当前节点接在后面。

**逻辑步骤：**

1. **终止条件**：如果链表为空或者只有一个节点，直接返回它（它就是反转后的头）。
2. **递归去后面**：假设后面的链表已经反转好了，递归函数会返回反转后的新头节点 `new_head`。
3. **处理当前节点**：
   - 此时 `head.next` 是原链表中的第二个节点，也就是反转后链表的尾巴。
   - 我们让 `head.next.next = head`，即将当前节点接在反转后的链表尾部。
   - 为了防止环路，让 `head.next = None`。
4. 返回 `new_head`。

**代码实现：**

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 基准情况：空链表或只有一个节点
        if not head or not head.next:
            return head
        
        # 2. 递归反转后续部分
        new_head = self.reverseList(head.next)
        
        # 3. 将当前节点接到已反转部分的后面
        # head.next 此时指向的是反转后的尾节点
        head.next.next = head
        head.next = None  # 切断原来的正向连接
        
        return new_head
```

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$，主要是递归调用栈的开销。

---

**总结与对比**

| 特性           | 迭代法           | 递归法             |
| :------------- | :--------------- | :----------------- |
| **空间复杂度** | $O(1)$ (最优)    | $O(n)$ (系统栈)    |
| **理解难度**   | 容易理解指针移动 | 需要理解递归回溯   |
| **实际应用**   | 工业级代码首选   | 理论学习，面试加分 |





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



## 222.完全二叉树的节点个数

bfs, dfs, binary + greedy,  https://leetcode.cn/problems/count-complete-tree-nodes/

> 如果用bfs, dfs写是简单级别，binary search是中级难度。

给你一棵 **完全二叉树** 的根节点 `root` ，求出该树的节点个数。

[完全二叉树](https://baike.baidu.com/item/完全二叉树/7773232?fr=aladdin) 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 `h` 层（从第 0 层开始），则该层包含 `1~ 2h` 个节点。

 

**示例 1：**

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/complete.jpg" alt="img" style="zoom:67%;" />

```
输入：root = [1,2,3,4,5,6]
输出：6
```

**示例 2：**

```
输入：root = []
输出：0
```

**示例 3：**

```
输入：root = [1]
输出：1
```

 

**提示：**

- 树中节点的数目范围是`[0, 5 * 10^4]`
- `0 <= Node.val <= 5 * 10^4`
- 题目数据保证输入的树是 **完全二叉树**

 

**进阶：**遍历树来统计节点是一种时间复杂度为 `O(n)` 的简单解决方案。你可以设计一个更快的算法吗？



思路：直接递归很简单

优化的话利用完全二叉树的性质，左右子树至少有一个是满二叉树，可以直接得出节点数目。学习了一下二进制运算符（满二叉树的节点数为 `2^h - 1`，其中 `h` 是树的高度。使用左移运算符可以高效地计算 `2^h`）

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftnum = self.countNodes(root.left)
        rightnum = self.countNodes(root.right)
        return 1+leftnum +rightnum
#以下是利用完全二叉树性质的解法
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        
        if left_height == right_height:
            # 左子树是满二叉树
            return (1 << left_height) + self.countNodes(root.right)
        else:
            # 右子树是满二叉树
            return (1 << right_height) + self.countNodes(root.left)
    
    def get_height(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height
```

> 核心逻辑
>
> 在完全二叉树中：
>
> 如果 left_height == right_height，则说明左子树是满二叉树。
> 如果 left_height != right_height，则说明右子树是满二叉树。
> 这是因为：
>
> 完全二叉树的节点从左到右依次填满，所以如果左右子树的高度相等，左子树必然是满二叉树。
> 如果左右子树的高度不相等，则右子树必然是满二叉树（因为右子树的高度比左子树少一层）。





bfs

```python
from collections import deque

# 定义树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # 如果根节点为空，直接返回 0
        if not root:
            return 0
        
        # 初始化队列和计数器
        queue = deque([root])
        count = 0
        
        # 使用 BFS 遍历树
        while queue:
            node = queue.popleft()
            count += 1  # 每访问一个节点，计数器加 1
            
            # 将左右子节点加入队列（如果存在）
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return count
```



思路：起初用简单的dfs思路AC了，但时间复杂度不够好看，于是尝试新方法，看了题解中的二进制思路后大受震撼，故用二进制思路走了一遍。

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def check(node_index: int, current_node: Optional[TreeNode]) -> bool:
            """
            检查编号为 node_index 的节点是否存在。
            :param node_index: 节点编号（从 1 开始）
            :param current_node: 当前遍历到的节点
            :return: 如果节点存在返回 True，否则返回 False
            """
            # 将节点编号转换为二进制路径（去掉 '0b' 前缀）
            path = bin(node_index)[3:]
            for direction in path:
                if direction == '0':
                    current_node = current_node.left
                else:
                    current_node = current_node.right
                # 如果当前节点为空，说明该路径不存在
                if not current_node:
                    return False
            return True

        # 计算树的高度（从根节点到最深左子节点的路径长度）
        height = 0
        current = root
        while current.left:
            height += 1
            current = current.left

        # 二分查找最后一层的节点范围
        left, right = 2 ** height, 2 ** (height + 1) - 1
        while left < right:
            mid = (left + right) // 2
            if check(mid, root):
                left = mid + 1  # 编号 mid 存在，尝试更大的编号
            else:
                right = mid  # 编号 mid 不存在，尝试更小的编号

        # 检查最终结果是否包含最后一个节点
        return left if check(left, root) else left - 1
```





这题是关于“**完全二叉树的节点个数**”，如果使用普通遍历，时间复杂度是 **O(n)**。但由于题目保证这是一棵“完全二叉树”，可以利用它的结构性质设计一个更快的算法 —— $O(log² n)$。

---

✅ 思路：利用完全二叉树的高度特性（二分 + 递归）

💡 完全二叉树的特性：

- 除了最后一层，其他每一层的节点数都达到最大；
- 最后一层节点从左到右连续排列；
- 所以我们可以利用“**左子树和右子树高度是否相等**”来判断哪边是满的。

---

✅ 算法步骤

```text
1. 对于当前节点：
   - 计算左子树的深度 left_depth（从左一路到底）
   - 计算右子树的深度 right_depth（从右一路到底）

2. 如果 left_depth == right_depth：
   → 说明是满二叉树，节点个数是 2^depth - 1；
3. 否则：
   → 左右子树继续递归统计。
```

---

✅ 代码（Python）

```python
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def get_depth(node, go_left=True):
            depth = 0
            while node:
                depth += 1
                node = node.left if go_left else node.right
            return depth

        left_depth = get_depth(root, True)
        right_depth = get_depth(root, False)

        if left_depth == right_depth:
            # 是满二叉树
            return (1 << left_depth) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
```

---

✅ 时间复杂度分析

- `get_depth()` 的时间是 `O(log n)`
- 每层递归最多进行一次 `get_depth()`，最多递归 `log n` 层
- 所以总复杂度为 $O((log n)²)$，比 O(n) 快很多





利用完全二叉树的特性，结合 **二分查找（Binary Search）+ 贪心（Greedy）** 来将时间复杂度从 O(n) 降低到 **O(log² n)**。

---

✅ 思路总结：

1. **完全二叉树的性质**：
   - 如果左子树和右子树的高度一样，说明左子树是满的，可以跳过左子树直接查右子树；
   - 如果右子树高度比左子树小，则右子树是满的，可以跳过右子树查左子树；
   - 利用这个可以实现递归或二分。

2. **使用二分查找判断最后一层节点是否存在**：
   - 先计算整棵树的高度 `h`（即从根节点走到最左下角的深度）；
   - 在 `[0, 2^h - 1]` 范围内用二分查找判断某个索引是否存在；
   - 最后总节点数 = `2^h - 1`（前 h 层的满节点）+ `left`（最后一层的节点个数）。

---

🔍 Python 实现（Binary Search + Greedy）：

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def getDepth(node):
            # 计算从当前节点到最左边叶子的深度
            d = 0
            while node.left:
                node = node.left
                d += 1
            return d

        def exists(idx, depth, node):
            # 判断idx编号的节点是否存在于最后一层
            left, right = 0, 2 ** depth - 1
            for _ in range(depth):
                mid = (left + right) // 2
                if idx <= mid:
                    node = node.left
                    right = mid
                else:
                    node = node.right
                    left = mid + 1
                if not node:
                    return False
            return True

        depth = getDepth(root)
        if depth == 0:
            return 1  # 只有一个节点

        # 二分查找最后一层的节点数
        left, right = 0, 2 ** depth - 1
        while left <= right:
            mid = (left + right) // 2
            if exists(mid, depth, root):
                left = mid + 1
            else:
                right = mid - 1

        # 总节点数 = 前面满的节点 + 最后一层的实际节点数
        return (2 ** depth - 1) + left
```

---

**✅ 时间复杂度分析：**

- `getDepth`：O(log n)
- 每次 `exists` 判断走 `depth` 层，O(log n)
- 二分查找次数为 log(n)
- 所以总复杂度是 **O((log n)²)**。

> 这个问题的解法里，确实用了 **两层二分**，我们来分开讲清楚它们的目的和操作方式。
>
> ---
>
> **🔍 二分查找一：在最后一层找有多少节点**
>
> **🧠 背景：**
>
> 完全二叉树中，前 `h` 层一定是满的（即节点数是 `2^h - 1`），最后一层最多有 `2^h` 个节点，编号为 `[0, 2^h - 1]`。
>
> 我们要找的是：**最后一层到底有多少个节点存在？**
>
> ---
>
> **🧪 怎么找？**
>
> 我们对最后一层的编号区间 `[0, 2^h - 1]` 做 **二分查找**，判断编号为 `mid` 的节点是否存在。
>
> 如果 `mid` 存在，说明左边都是满的，可能还有更多 → 查右边；
>
> 如果 `mid` 不存在，说明超出了当前树 → 查左边。
>
> 这就是外层二分：
>
> ```python
> left, right = 0, 2 ** depth - 1
> while left <= right:
>     mid = (left + right) // 2
>     if exists(mid, depth, root):  # 二分查找是否存在这个编号
>         left = mid + 1
>     else:
>         right = mid - 1
> ```
>
> 最终，`left` 就是最后一层真实存在的节点数。
>
> ---
>
> **🔍 二分查找二：exists() 函数内部，用编号查路径**
>
> 🧠 背景：
>
> 现在我们要判断某个编号 `idx`（从 0 开始）对应的节点是否存在于完全二叉树的最后一层。
>
> 但我们没有树的数组表示，要**从根节点走路径**到目标位置。问题是我们只知道编号 `idx`，不知道怎么走。
>
> ---
>
> 🧪 怎么用二分走路径？
>
> 我们假设最后一层的编号范围是 `[0, 2^depth - 1]`，每次根据 `idx` 和中间值 `mid` 来判断：
>
> - 如果 `idx <= mid`，目标在左子树，往左走；
> - 否则在右子树，往右走；
>
> 这样从根开始走 `depth` 步，模拟走到 `idx` 这个位置，看看这个路径上有没有空节点。
>
> ```python
> def exists(idx, depth, node):
>     left, right = 0, 2 ** depth - 1
>     for _ in range(depth):
>         mid = (left + right) // 2
>         if idx <= mid:
>             node = node.left
>             right = mid
>         else:
>             node = node.right
>             left = mid + 1
>         if not node:
>             return False
>     return True
> ```
>
> ---
>
> ✅ 小结：
>
> | 目的     | 二分查找的位置          | 查找什么               | 操作                |
> | -------- | ----------------------- | ---------------------- | ------------------- |
> | 外层二分 | `[0, 2^depth - 1]`      | 最后一层有多少节点     | `countNodes` 主体中 |
> | 内层二分 | 路径 `[0, 2^depth - 1]` | 某个编号的节点是否存在 | `exists()` 中       |
>
> 







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



递归算法：currentNode 指针是先到尾节点，由于递归的特性再从后往前进行比较。frontPointer 是递归函数外的指针。若 currentNode.val != frontPointer.val 则返回 false。反之，frontPointer 向前移动并返回 true。

算法的正确性在于递归处理节点的顺序是相反的，而我们在函数外又记录了一个变量，因此从本质上，我们同时在正向和逆向迭代匹配。

作者：力扣官方题解

```python
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()


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

stack, two pinters, https://leetcode.cn/problems/move-zeroes/

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

- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

 

**进阶：**你能尽量减少完成的操作次数吗？



思路：**快慢指针**。维护一个最左边的空位（慢指针 `i0`），用一个快指针 `i` 遍历数组。

```python
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        i0 = 0  # 慢指针，指向最左边的空位
        for i in range(n):  # 快指针，扫描整个数组
            if nums[i] != 0:
                if i != i0:  # 只有当 i > i0 时才需要交换
                    nums[i0], nums[i] = nums[i], nums[i0]
                i0 += 1
```


直接维护 `i0`，只要发现非零元素就交换到前面。`i != i0` 时才交换，避免了无意义的自交换。

逻辑只分为两步——遇到非零 → 放到最左空位 → 更新 `i0`，
非零元素只动一次（要么本身不动，要么交换到正确位置），时间复杂度 `O(n)`，空间 `O(1)`。





```python
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = 0   # 慢指针，指向最左边的空位
        right = 0  # 快指针，扫描整个数组

        while right < n:
            if nums[right] != 0:   # 找到非零元素
                if left != right:  # 只有当 left < right 才需要交换
                    nums[left], nums[right] = nums[right], nums[left]
                left += 1          # 更新最左空位
            right += 1             # 快指针继续扫描

```



## E303.区域和检索 - 数组不可变

prefix sum, https://leetcode.cn/problems/range-sum-query-immutable/

给定一个整数数组  `nums`，处理以下类型的多个查询:

1. 计算索引 `left` 和 `right` （包含 `left` 和 `right`）之间的 `nums` 元素的 **和** ，其中 `left <= right`

实现 `NumArray` 类：

- `NumArray(int[] nums)` 使用数组 `nums` 初始化对象
- `int sumRange(int left, int right)` 返回数组 `nums` 中索引 `left` 和 `right` 之间的元素的 **总和**，包含 `left` 和 `right` 两点（也就是 `nums[left] + nums[left + 1] + ... + nums[right]` )

 

**示例 1：**

```
输入：
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
输出：
[null, 1, -1, -3]

解释：
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1)) 
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
```

 

**提示：**

- `1 <= nums.length <= 10^4`
- `-10^5 <= nums[i] <= 10^5`
- `0 <= left <= right < nums.length`
- 最多调用 `10^4` 次 `sumRange` 方法



如果只是 **查询一次** 或 **很少查询**，可以直接：

```python
sum(nums[left:right+1])
```

但如果：查询次数 ≥ n，就必须 **前缀和**。这也是这题为什么叫 **Range Query**。



这题是经典 **前缀和（Prefix Sum）** 模板题。思路很直接：

**一、核心思想**

预处理一个 **前缀和数组** `pre`：
pre[i] = nums[0] + nums[1] + ... + nums[i-1]

也就是：

```
pre[0] = 0
pre[1] = nums[0]
pre[2] = nums[0] + nums[1]
...
```

这样区间 `[left, right]` 的和就是：
sum(left,right) = pre[right+1] - pre[left]

原因：

```
pre[right+1] = nums[0] + ... + nums[right]
pre[left]    = nums[0] + ... + nums[left-1]
```

相减就得到：

```
nums[left] + ... + nums[right]
```

时间复杂度：

- 初始化：`O(n)`
- 每次查询：`O(1)`

非常适合 **多次查询区间和**。

------

**二、Python实现**

```python
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.pre = [0] * (n + 1)

        for i in range(n):
            self.pre[i + 1] = self.pre[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right + 1] - self.pre[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
```

------

**四、为什么 `pre` 长度是 `n+1`**

关键是 **避免特判 left=0**。

如果不用 `n+1`，写法会变成：

```python
if left == 0:
    return pre[right]
else:
    return pre[right] - pre[left-1]
```

而使用 `n+1`：pre[0] = 0

就可以统一写成：pre[right+1] - pre[left]

代码更干净。

------

**五、这题的本质**

这是 **最基础的前缀和模型**：

| 问题类型       | 技巧                   |
| -------------- | ---------------------- |
| 多次区间求和   | 前缀和                 |
| 区间修改       | 差分                   |
| 动态更新区间和 | Fenwick / Segment Tree |

这题本质就是：预处理 O(n)，查询 O(1)



常用的前缀和写法**，比标准写法更 **短、清晰、Pythonic。

------

**三行构造前缀和（推荐写法）**

核心技巧：
利用 **`itertools.accumulate`**

```python
from typing import List
import itertools

class NumArray:

    def __init__(self, nums: List[int]):
        self.pre = [0] + list(itertools.accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right+1] - self.pre[left]
```

初始化只需要 **一行核心代码**：



**四、最常见的前缀和模板**

以后你在做算法题基本都会看到这个模板：

```python
from itertools import accumulate

nums = [1,2,3,4,5]

pre = [0] + list(accumulate(nums))

# 区间和
def query(l,r):
    return pre[r+1] - pre[l]
```

------

**五、很多人不知道的一个技巧**

`accumulate` 还能做 **前缀最大值 / 最小值 / 乘积**：

**前缀最大值**

```python
from itertools import accumulate
import operator

nums = [3,1,5,2,4]

pre_max = list(accumulate(nums, max))
```

得到：

```
[3,3,5,5,5]
```

------

**前缀乘积**

```python
list(accumulate(nums, operator.mul))
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



## 392.判断子序列

tow pointers, https://leetcode.cn/problems/is-subsequence/

给定字符串 **s** 和 **t** ，判断 **s** 是否为 **t** 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，`"ace"`是`"abcde"`的一个子序列，而`"aec"`不是）。

**进阶：**

如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

**致谢：**

特别感谢 [@pbrother ](https://leetcode.com/pbrother/)添加此问题并且创建所有测试用例。

 

**示例 1：**

```
输入：s = "abc", t = "ahbgdc"
输出：true
```

**示例 2：**

```
输入：s = "axc", t = "ahbgdc"
输出：false
```

 

**提示：**

- `0 <= s.length <= 100`
- `0 <= t.length <= 10^4`
- 两个字符串都只由小写字符组成。





```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
```





如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

如果有大量的字符串 `S1, S2, ..., Sk` 需要检查是否是 `T` 的子序列，特别是当 `k` 很大时（比如 10 亿），不能再按每个字符串逐一线性扫描 `T`，因为这样会导致非常高的时间复杂度，效率非常低。此时，需要进行优化，尤其是对 `T` 进行预处理，以便对每个 `Si` 进行更高效的查询。

**主要思路**：

1. **预处理 `T`**：我们可以先遍历字符串 `T`，记录每个字符在 `T` 中的所有出现位置。这样对于每个 `Si`，我们可以快速判断字符是否存在，并且通过二分查找来确定字符的位置。
2. **二分查找**：对于每个 `Si`，可以利用 `bisect` 模块（二分查找）快速定位字符的位置，以便高效判断 `Si` 是否是 `T` 的子序列。

**代码实现**：

```python
import bisect
from collections import defaultdict

def preprocess(t: str):
    # 创建一个字典，存储每个字符在 T 中的位置
    char_positions = defaultdict(list)
    for index, char in enumerate(t):
        char_positions[char].append(index)
    return char_positions

def is_subsequence(s: str, t: str, char_positions: defaultdict) -> bool:
    # 定义当前字符的指针，初始为 -1
    current_position = -1
    for char in s:
        if char not in char_positions:
            return False
        # 找到字符在 T 中的位置，且位置大于 current_position
        positions = char_positions[char]
        idx = bisect.bisect_right(positions, current_position)
        if idx == len(positions):
            return False
        current_position = positions[idx]
    return True

# 示例
t = "ahbgdc"
char_positions = preprocess(t)

# 测试多个 S1, S2, ...
S = ["abc", "axc", "ahbgd", "bdc"]
for s in S:
    print(f"'{s}' is a subsequence of '{t}':", is_subsequence(s, t, char_positions))
```

> **解释**：
>
> 1. 预处理 `T`：
>    - 使用 `defaultdict(list)` 来存储 `T` 中每个字符的所有出现位置。这样对于每个字符，`char_positions[char]` 就是一个列表，包含了字符 `char` 在 `T` 中所有出现的索引位置。
> 2. 检查每个 `Si` 是否为 `T` 的子序列：
>    - 对于每个字符串 `Si`，我们遍历 `Si` 中的每个字符，检查该字符是否存在于 `T` 中（可以通过预处理得到的 `char_positions` 字典快速查询）。
>    - 对于每个字符 `char`，我们使用 `bisect_right` 找到 `char` 在 `T` 中的最小的索引，该索引必须大于当前字符在 `T` 中的位置（即 `current_position`）。这样保证了 `Si` 中的字符按顺序出现在 `T` 中。
>    - 如果有任何字符不能满足要求，则返回 `False`，否则返回 `True`。
>
>    **为什么优化**：
>
> 1. **预处理 `T`**：通过预处理 `T`，我们把查询字符位置的时间复杂度从 O(n) 降低到 O(log m)，其中 `m` 是 `T` 的长度。
> 2. **二分查找**：利用 `bisect_right` 快速找到字符在 `T` 中的位置，使得每次查询的时间复杂度是 O(log n)，其中 `n` 是该字符在 `T` 中出现的位置数量。
>
> **时间复杂度**：
>
> - **预处理 `T`**：O(n)，其中 `n` 是 `T` 的长度。
> - **每个 `Si` 的检查**：对于每个 `Si`，如果它的长度是 `m`，检查它是否为 `T` 的子序列的时间复杂度是 O(m log n)，其中 `n` 是 `T` 的长度。
> - **总体复杂度**：对于 `k` 个字符串，总体时间复杂度是 O(k * m log n)。
>
> **总结**：
>
> - 这种方法通过预处理 `T` 并使用二分查找，大大减少了每次检查字符串 `Si` 是否是 `T` 的子序列的时间复杂度，使得即使有大量输入字符串也能高效处理。



## E401.二进制手表

brute force, https://leetcode.cn/problems/binary-watch/

二进制手表顶部有 4 个 LED 代表 **小时（0-11）**，底部的 6 个 LED 代表 **分钟（0-59）**。每个 LED 代表一个 0 或 1，最低位在右侧。

- 例如，下面的二进制手表读取 `"4:51"` 。

<img src="https://assets.leetcode.com/uploads/2021/04/08/binarywatch.jpg" alt="img" style="zoom:50%;" />

给你一个整数 `turnedOn` ，表示当前亮着的 LED 的数量，返回二进制手表可以表示的所有可能时间。你可以 **按任意顺序** 返回答案。

小时不会以零开头：

- 例如，`"01:00"` 是无效的时间，正确的写法应该是 `"1:00"` 。

分钟必须由两位数组成，可能会以零开头：

- 例如，`"10:2"` 是无效的时间，正确的写法应该是 `"10:02"` 。

 

**示例 1：**

```
输入：turnedOn = 1
输出：["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
```

**示例 2：**

```
输入：turnedOn = 9
输出：[]
```

 

**提示：**

- `0 <= turnedOn <= 10`



这个问题可以通过**枚举法**轻松解决。

**解题思路**

与其去计算哪些 LED 灯亮着，不如直接遍历所有可能的时间（小时从 0 到 11，分钟从 0 到 59），然后计算这个时间的二进制表示中共有多少个 $1$。

1.  **遍历范围**：
    *   小时 $h$：$0 \le h < 12$
    *   分钟 $m$：$0 \le m < 60$
2.  **计算二进制中 1 的个数**：
    *   在 Python 中，可以使用 `bin(n).count('1')` 或者更高效的 `int.bit_count()`（Python 3.10+）。
    *   我们需要计算 `h` 的二进制 1 的个数加上 `m` 的二进制 1 的个数。
3.  **匹配与格式化**：
    *   如果总个数等于 `turnedOn`，则按照题目要求的格式 `"H:MM"` 格式化时间。
    *   分钟 `m` 如果小于 10，需要在前面补零（可以使用 `f"{h}:{m:02d}"`）。

    **代码实现**

```python
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        # 遍历所有小时 0-11
        for h in range(12):
            # 遍历所有分钟 0-59
            for m in range(60):
                # 计算小时和分钟二进制中 '1' 的总个数
                # Python 3.10+ 可以直接用 h.bit_count() + m.bit_count()
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    # 格式化时间，m:02d 表示分钟不足两位时前面补 0
                    res.append(f"{h}:{m:02d}")
        return res
```

**复杂度分析**

*   **时间复杂度**：$O(1)$。
    虽然代码中有嵌套循环，但循环次数是固定的（$12 \times 60 = 720$ 次）。这是一个常数级的操作。
*   **空间复杂度**：$O(1)$。
    除了存储答案的列表外，我们只使用了常数级别的额外空间。

    **为什么选择这种方法？**

    虽然也可以使用回溯算法（搜索哪些 LED 被点亮），但回溯的逻辑相对复杂，需要处理“小时不能超过 11”和“分钟不能超过 59”的边界条件。而**直接枚举所有时间**的方法逻辑最清晰，代码最简洁，且由于总状态数极少（仅 720 种），运行速度非常快。





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





## E657.机器人能否返回原点

implementation, https://leetcode.cn/problems/robot-return-to-origin/

在二维平面上，有一个机器人从原点 `(0, 0)` 开始。给出它的移动顺序，判断这个机器人在完成移动后是否在 **`(0, 0)` 处结束**。

移动顺序由字符串 `moves` 表示。字符 `move[i]` 表示其第 `i` 次移动。机器人的有效动作有 `R`（右），`L`（左），`U`（上）和 `D`（下）。

如果机器人在完成所有动作后返回原点，则返回 `true`。否则，返回 `false`。

**注意：**机器人“面朝”的方向无关紧要。 `“R”` 将始终使机器人向右移动一次，`“L”` 将始终向左移动等。此外，假设每次移动机器人的移动幅度相同。

 

**示例 1:**

```
输入: moves = "UD"
输出: true
解释：机器人向上移动一次，然后向下移动一次。所有动作都具有相同的幅度，因此它最终回到它开始的原点。因此，我们返回 true。
```

**示例 2:**

```
输入: moves = "LL"
输出: false
解释：机器人向左移动两次。它最终位于原点的左侧，距原点有两次 “移动” 的距离。我们返回 false，因为它在移动结束时没有返回原点。
```

 

**提示:**

- `1 <= moves.length <= 2 * 10^4`
- `moves` 只包含字符 `'U'`, `'D'`, `'L'` 和 `'R'`



```python
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # 统计左右移动的次数
        # 如果向右的次数等于向左的次数，横向位移抵消
        horizontal = moves.count('R') == moves.count('L')
        
        # 统计上下移动的次数
        # 如果向上的次数等于向下的次数，纵向位移抵消
        vertical = moves.count('U') == moves.count('D')
        
        # 只有当横向和纵向都抵消时，机器人才能回到原点
        return horizontal and vertical
        
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



## E693.交替位二进制数

bit manipulation, https://leetcode.cn/problems/binary-number-with-alternating-bits/

给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。

 

**示例 1：**

```
输入：n = 5
输出：true
解释：5 的二进制表示是：101
```

**示例 2：**

```
输入：n = 7
输出：false
解释：7 的二进制表示是：111.
```

**示例 3：**

```
输入：n = 11
输出：false
解释：11 的二进制表示是：1011.
```

 

**提示：**

- `1 <= n <= 2^31 - 1`



```python
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = bin(n)[2:]
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                return False
        else:
            return True
```



你的代码逻辑是正确的，但可以进一步优化以提升简洁性和性能。以下是几种优化方式：

------

**优化版本 1：使用 `all()` 函数（更 Pythonic）**

```python
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = bin(n)[2:]
        return all(s[i] != s[i - 1] for i in range(1, len(s)))
```

**优点**：

- 更简洁、可读性高。
- 利用短路求值，遇到第一个 `False` 就停止。

------

**优化版本 2：位运算（更高效，不转字符串）**

交替比特的特性是：
如果 `n` 是交替比特（如 `101010`），那么 `n ^ (n >> 1)` 应该得到全 1 的数（如 `111111`）。
而全 1 的数加 1 后会变成 2 的幂（如 `111111 + 1 = 1000000`），此时 `(x & (x + 1)) == 0`。

```python
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n >> 1)
        return x & (x + 1) == 0
```

**优点**：

- 时间复杂度 O(1)，空间 O(1)。
- 不依赖字符串转换，效率更高，尤其对大整数更优。

**原理示例**：

- `n = 0b101010`
- `n >> 1 = 0b010101`
- `x = n ^ (n>>1) = 0b111111`
- `x + 1 = 0b1000000`
- `x & (x+1) = 0b111111 & 0b1000000 = 0` → 符合条件

------

推荐使用 **位运算版本（优化版本 2）**，因为它：

- 更快
- 更省内存
- 更体现算法思维

如果你追求可读性且数据规模不大，版本 1 也是很好的选择。



## E696.计数二进制子串

two pointers, https://leetcode.cn/problems/count-binary-substrings/

给定一个字符串 `s`，统计并返回具有相同数量 `0` 和 `1` 的非空（连续）子字符串的数量，并且这些子字符串中的所有 `0` 和所有 `1` 都是成组连续的。

重复出现（不同位置）的子串也要统计它们出现的次数。

**示例 1：**

```
输入：s = "00110011"
输出：6
解释：6 个子串满足具有相同数量的连续 1 和 0 ："0011"、"01"、"1100"、"10"、"0011" 和 "01" 。
注意，一些重复出现的子串（不同位置）要统计它们出现的次数。
另外，"00110011" 不是有效的子串，因为所有的 0（还有 1 ）没有组合在一起。
```

**示例 2：**

```
输入：s = "10101"
输出：4
解释：有 4 个子串："10"、"01"、"10"、"01" ，具有相同数量的连续 1 和 0 。
```

 

**提示：**

- `1 <= s.length <= 10^5`
- `s[i]` 为 `'0'` 或 `'1'`





利用**分组计数**的思想：

- 遍历字符串，将连续相同字符的长度记录下来，例如 `"00110011"` → `[2, 2, 2, 2]`
- 对于相邻两组（比如 2 个 0 和 2 个 1），它们能组成的合法子串数量是 `min(前一组长度, 后一组长度)`
- 例如 `[2,2]` → min(2,2)=2（即 `"01"` 和 `"0011"`）
- 再比如 `[3,1]` → min(3,1)=1（只能组成 `"01"`）

------

**代码**

```python
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # Step 1: 计算连续字符的长度（分组）
        groups = []
        i = 0
        n = len(s)
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            groups.append(j - i)
            i = j
        
        # Step 2: 遍历相邻组，累加 min(prev, curr)
        cnt = 0
        for i in range(1, len(groups)):
            cnt += min(groups[i - 1], groups[i])
        
        return cnt
```

**时间复杂度**

- **O(n)** 时间，**O(k)** 空间（k 是分组数，最坏 O(n)）
- 远优于原方案的 O(n²)

------

**进一步空间优化（可选）**

可以不用存储整个 `groups` 列表，只需保留前一个 group 的长度：

```python
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, curr = 0, 1
        cnt = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                cnt += min(prev, curr)
                prev, curr = curr, 1
        cnt += min(prev, curr)  # 最后一组也要处理
        return cnt
```

这个版本空间复杂度 **O(1)**，更优！



## E744.寻找比目标字母大的最小字母

binary search, https://leetcode.cn/problems/find-smallest-letter-greater-than-target/

给你一个字符数组 `letters`，该数组按**非递减顺序**排序，以及一个字符 `target`。`letters` 里**至少有两个不同**的字符。

返回 `letters` 中大于 `target` 的最小的字符。如果不存在这样的字符，则返回 `letters` 的第一个字符。

 

**示例 1：**

```
输入: letters = ['c', 'f', 'j']，target = 'a'
输出: 'c'
解释：letters 中字典上比 'a' 大的最小字符是 'c'。
```

**示例 2:**

```
输入: letters = ['c','f','j'], target = 'c'
输出: 'f'
解释：letters 中字典顺序上大于 'c' 的最小字符是 'f'。
```

**示例 3:**

```
输入: letters = ['x','x','y','y'], target = 'z'
输出: 'x'
解释：letters 中没有一个字符在字典上大于 'z'，所以我们返回 letters[0]。
```

 

**提示：**

- `2 <= letters.length <= 10^4`
- `letters[i]` 是一个小写字母
- `letters` 按**非递减顺序**排序
- `letters` 最少包含两个不同的字母
- `target` 是一个小写字母





n小于10^6的情况，线性遍历的实际运行效率更高。



执行用时分布`0ms 击败100.00%`

```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for c in letters:
            if c > target:
                return c
        else:
            return letters[0]
```



执行用时分布`3ms 击败8.94%`

```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters)-1
        ans = letters[0]
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target:
                ans = letters[mid]
                right = mid -1
            else:
                left = mid + 1
        
        return ans
```



使用了 C 实现的 `bisect` 模块，速度会比手写二分快。执行用时分布`0ms 击败100.00%`

```python
import bisect

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        idx = bisect.bisect_right(letters, target)
        return letters[idx % len(letters)]
```



## E762.二进制表示中质数个计算置位

bit manipulation, https://leetcode.cn/problems/prime-number-of-set-bits-in-binary-representation/

给你两个整数 `left` 和 `right` ，在闭区间 `[left, right]` 范围内，统计并返回 **计算置位位数为质数** 的整数个数。

**计算置位位数** 就是二进制表示中 `1` 的个数。

- 例如， `21` 的二进制表示 `10101` 有 `3` 个计算置位。

 

**示例 1：**

```
输入：left = 6, right = 10
输出：4
解释：
6 -> 110 (2 个计算置位，2 是质数)
7 -> 111 (3 个计算置位，3 是质数)
9 -> 1001 (2 个计算置位，2 是质数)
10-> 1010 (2 个计算置位，2 是质数)
共计 4 个计算置位为质数的数字。
```

**示例 2：**

```
输入：left = 10, right = 15
输出：5
解释：
10 -> 1010 (2 个计算置位, 2 是质数)
11 -> 1011 (3 个计算置位, 3 是质数)
12 -> 1100 (2 个计算置位, 2 是质数)
13 -> 1101 (3 个计算置位, 3 是质数)
14 -> 1110 (3 个计算置位, 3 是质数)
15 -> 1111 (4 个计算置位, 4 不是质数)
共计 5 个计算置位为质数的数字。
```

 

**提示：**

- `1 <= left <= right <= 10^6`
- `0 <= right - left <= 10^4`



```python
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = []
        numbers = [True]*(10**2 + 1)
        numbers[0] = numbers[1] = False

        def seive(numbers):
            for i in range(2, int(1e2 + 1)):
                if numbers[i]:
                    primes.append(i)
                for j in range(len(primes)):
                    if i * primes[j] > int(1e2):
                        break
                    numbers[i * primes[j]] = False
                    if i % primes[j] == 0:
                        break

        seive(numbers)
        count = 0
        for i in range(left, right + 1):
            ones = bin(i).count('1')
            if numbers[ones]:
                count += 1

        return count

```



**关键观察**

- `right <= 10^6`
- `10^6 < 2^20`

所以一个数最多只有 **20 个二进制位**

也就是说：

> 置位个数最多是 20

因此我们只需要判断：

```
2, 3, 5, 7, 11, 13, 17, 19
```

这 8 个质数即可。

------

方法一：最清晰写法（推荐）

利用 Python 自带的 `bit_count()`（比 `bin(x).count('1')` 更快）

```python
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        
        ans = 0
        for x in range(left, right + 1):
            if x.bit_count() in primes:
                ans += 1
                
        return ans
```

------

**时间复杂度**

```
区间长度 ≤ 10^4
每个数 bit_count 是 O(1)
```

总体：

```
O(right - left)
```

非常轻松。

------

**进阶操作（位掩码黑科技）**

我们可以用一个整数做“质数表”：

```
665772 = 0b10100010100010101100
```

这个数的第 k 位表示 k 是否是质数。

代码：

```python
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        mask = 665772  # 预计算好的质数位掩码
        
        ans = 0
        for x in range(left, right + 1):
            if (mask >> x.bit_count()) & 1:
                ans += 1
                
        return ans
```

------

**原理**

如果 k 是质数：

```
mask 的第 k 位 = 1
```

判断：

```
(mask >> k) & 1
```

是否为 1。

这是一种 **位运算常见 trick**。



## E796.旋转字符串

https://leetcode.cn/problems/rotate-string/

给定两个字符串, `s` 和 `goal`。如果在若干次旋转操作之后，`s` 能变成 `goal` ，那么返回 `true` 。

`s` 的 **旋转操作** 就是将 `s` 最左边的字符移动到最右边。 

- 例如, 若 `s = 'abcde'`，在旋转一次之后结果就是`'bcdea'` 。

 

**示例 1:**

```
输入: s = "abcde", goal = "cdeab"
输出: true
```

**示例 2:**

```
输入: s = "abcde", goal = "abced"
输出: false
```

 

**提示:**

- `1 <= s.length, goal.length <= 100`
- `s` 和 `goal` 由小写英文字母组成



这个问题可以通过一个经典的技巧来解决：**字符串拼接**。

**解题思路**

1. **长度判断**：如果字符串 `s` 和 `goal` 的长度不相等，那么无论如何旋转 `s` 都不可能变成 `goal`。直接返回 `False`。

2. **拼接规律**：观察 `s` 的所有旋转结果。以 `s = "abcde"` 为例，它的旋转结果有：

   *   `abcde` (旋转0次)
   *   `bcdea` (旋转1次)
   *   `cdeab` (旋转2次)
   *   `deabc` (旋转3次)
   *   `eabcd` (旋转4次)

   如果我们把两个 `s` 拼接在一起，即 `s + s = "abcdeabcde"`，你会发现**所有可能的旋转结果都是这个拼接字符串的子串**。

3. **判断子串**：因此，只要满足 `len(s) == len(goal)` 且 `goal` 是 `s + s` 的子串，就可以判定 `s` 可以旋转成 `goal`。

**代码实现**

```python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # 如果长度不等，一定无法通过旋转得到
        if len(s) != len(goal):
            return False
        
        # 如果 goal 是 s + s 的子串，说明 goal 是 s 的一个旋转结果
        return goal in (s + s)
```

**复杂度分析**

*   **时间复杂度**：$O(n)$。其中 $n$ 是字符串的长度。在 Python 中，字符串的 `in` 操作（子串查找）在平均情况下是 $O(n)$ 的（底层通常使用类似 Boyer-Moore 或 Horspool 的优化算法）。
*   **空间复杂度**：$O(n)$。我们需要创建一个长度为 $2n$ 的新字符串 `s + s`。

**模拟法（另一种思路）**

如果你不想使用拼接的技巧，也可以直接模拟旋转过程：

```python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        # 模拟旋转，最多旋转 n 次
        for _ in range(len(s)):
            if s == goal:
                return True
            s = s[1:] + s[0] # 将左边第一个字符移到末尾
            
        return False
```

这种模拟法的时间复杂度是 $O(n^2)$（循环 $n$ 次，每次字符串切片和比较需要 $O(n)$），对于本题 $n \le 100$ 的数据范围也是可以通过的，但**拼接法**更为简洁且高效。





## E868.二进制间距

bit manipulation, https://leetcode.cn/problems/binary-gap/

给定一个正整数 `n`，找到并返回 `n` 的二进制表示中两个 **相邻** 1 之间的 **最长距离** 。如果不存在两个相邻的 1，返回 `0` 。

如果只有 `0` 将两个 `1` 分隔开（可能不存在 `0` ），则认为这两个 1 彼此 **相邻** 。两个 `1` 之间的距离是它们的二进制表示中位置的绝对差。例如，`"1001"` 中的两个 `1` 的距离为 3 。

 

**示例 1：**

```
输入：n = 22
输出：2
解释：22 的二进制是 "10110" 。
在 22 的二进制表示中，有三个 1，组成两对相邻的 1 。
第一对相邻的 1 中，两个 1 之间的距离为 2 。
第二对相邻的 1 中，两个 1 之间的距离为 1 。
答案取两个距离之中最大的，也就是 2 。
```

**示例 2：**

```
输入：n = 8
输出：0
解释：8 的二进制是 "1000" 。
在 8 的二进制表示中没有相邻的两个 1，所以返回 0 。
```

**示例 3：**

```
输入：n = 5
输出：2
解释：5 的二进制是 "101" 。
```

 

**提示：**

- `1 <= n <= 10^9`



思路：遍历二进制字符串，记录上一个 `'1'` 的位置，并在遇到新的 `'1'` 时更新最大距离。

```python
class Solution:
    def binaryGap(self, n: int) -> int:
        s = bin(n)[2:]
        max_dis = 0
        left, right = 0, 0
        for i in range(1, len(s)):
            if s[i] == '1':
                max_dis = max(max_dis, i - left)
                left = i
        
        return max_dis
```



为了代码的清晰性和鲁棒性，可以稍作优化，使其逻辑更明确，并避免依赖“`s[0]` 一定是 `'1'`”这一隐含前提（尽管在本题中成立）。

此外，还可以不转成字符串，直接用位运算处理，更高效、更符合“二进制间距”的题意。

------

**优化版本 1：保持字符串思路，但逻辑更清晰**

```python
class Solution:
    def binaryGap(self, n: int) -> int:
        s = bin(n)[2:]
        max_dis = 0
        prev = -1  # 上一个 '1' 的位置
        for i, ch in enumerate(s):
            if ch == '1':
                if prev != -1:
                    max_dis = max(max_dis, i - prev)
                prev = i
        return max_dis
```

**优点**：

- 明确只在两个 `'1'` 之间计算距离。
- 初始 `prev = -1` 表示尚未遇到第一个 `'1'`，逻辑清晰。
- 避免了对 `s[0] == '1'` 的隐式依赖（虽然实际成立）。

------

**优化版本 2：使用位运算（推荐，更高效）**

```python
class Solution:
    def binaryGap(self, n: int) -> int:
        max_dis = 0
        prev = -1
        i = 0
        while n:
            if n & 1:
                if prev != -1:
                    max_dis = max(max_dis, i - prev)
                prev = i
            n >>= 1
            i += 1
        return max_dis
```

**优点**：

- 不需要生成字符串，节省空间。
- 时间复杂度相同 O(log n)，但常数更小。
- 更贴近底层二进制操作，适合面试展示位运算能力。

------

**总结**

你原来的代码在 LeetCode 上可能能通过（因为 `bin(n)[2:]` 确实以 `'1'` 开头），但存在逻辑隐患（比如若输入允许前导零就会出错）。推荐使用 **优化版本 1 或 2**，尤其是**版本 2 的位运算解法**更为优雅高效。



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



## E961.在长度 2N 的数组中找出重复 N次的元素

Boyer-Moore, https://leetcode.cn/problems/n-repeated-element-in-size-2n-array/

给你一个整数数组 `nums` ，该数组具有以下属性：

- `nums.length == 2 * n`.
- `nums` 包含 `n + 1` 个 **不同的** 元素
- `nums` 中恰有一个元素重复 `n` 次

找出并返回重复了 `n` 次的那个元素。

 

**示例 1：**

```
输入：nums = [1,2,3,3]
输出：3
```

**示例 2：**

```
输入：nums = [2,1,2,5,3,2]
输出：2
```

**示例 3：**

```
输入：nums = [5,1,5,2,5,3,5,4]
输出：5
```

 

**提示：**

- `2 <= n <= 5000`
- `nums.length == 2 * n`
- `0 <= nums[i] <= 10^4`
- `nums` 由 `n + 1` 个 **不同的** 元素组成，且其中一个元素恰好重复 `n` 次



```python
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums.sort()
        ans = nums[0]
        for n in nums[1:]:
            if ans == n:
                return ans
            else:
                ans = n
```



【灵茶山艾府】https://leetcode.cn/problems/n-repeated-element-in-size-2n-array/solutions/3870905/si-chong-fang-fa-ha-xi-ji-he-mo-er-tou-p-f95m/

摩尔投票，先完成169题目，再来这个题目。

为了让出现 n 次的那个数变成绝对众数，我们可以分类讨论：

如果 nums[0] 在下标 [1,n−1] 中出现过，那么返回 nums[0]。
否则，去掉 nums[0]，剩下 2n−1 个数，出现次数为 n 的那个数变成绝对众数，可以用 169 题的算法解决。
这两件事情可以在同一个循环中完成。

```python
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        ans = hp = 0
        for x in nums[1:]:  # 也可以写 for i in range(1, len(nums)) 避免切片
            if x == nums[0]:
                return x
            if hp == 0:  # x 是初始擂主，生命值为 1
                ans, hp = x, 1
            else:  # 比武，同门加血，否则扣血
                hp += 1 if x == ans else -1
        return ans
```





## 997.找到小镇的法官

graph, hash table, https://leetcode.cn/problems/find-the-town-judge/

小镇里有 `n` 个人，按从 `1` 到 `n` 的顺序编号。传言称，这些人中有一个暗地里是小镇法官。

如果小镇法官真的存在，那么：

1. 小镇法官不会信任任何人。
2. 每个人（除了小镇法官）都信任这位小镇法官。
3. 只有一个人同时满足属性 **1** 和属性 **2** 。

给你一个数组 `trust` ，其中 `trust[i] = [ai, bi]` 表示编号为 `ai` 的人信任编号为 `bi` 的人。

如果小镇法官存在并且可以确定他的身份，请返回该法官的编号；否则，返回 `-1` 。

 

**示例 1：**

```
输入：n = 2, trust = [[1,2]]
输出：2
```

**示例 2：**

```
输入：n = 3, trust = [[1,3],[2,3]]
输出：3
```

**示例 3：**

```
输入：n = 3, trust = [[1,3],[2,3],[3,1]]
输出：-1
```

 

**提示：**

- `1 <= n <= 1000`
- `0 <= trust.length <= 10^4`
- `trust[i].length == 2`
- `trust` 中的所有`trust[i] = [ai, bi]` **互不相同**
- `ai != bi`
- `1 <= ai, bi <= n`



```python
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out_degrees = [0] * (n + 1)
        in_degrees = [0] * (n + 1) 

        for u, v in trust:
            out_degrees[u] += 1 
            in_degrees[v] += 1 

        for v in range(1, n + 1):
            if out_degrees[v] == 0 and in_degrees[v] == n - 1:
                return v

        return -1
```



```python
        if n == 1 and not trust:
            return 1
        
        trust_others = set()
        trusted_by = [0] * (n + 1)
        
        for x, y in trust:
            trust_others.add(x)
            trusted_by[y] += 1
        
        for i in range(1, n + 1):
            if i not in trust_others and trusted_by[i] == n - 1:
                return i
        
        return -1
```



## E1009.十进制整数的反码

bit manipulation, https://leetcode.cn/problems/complement-of-base-10-integer/

每个非负整数 `N` 都有其二进制表示。例如， `5` 可以被表示为二进制 `"101"`，`11` 可以用二进制 `"1011"` 表示，依此类推。注意，除 `N = 0` 外，任何二进制表示中都不含前导零。

二进制的反码表示是将每个 `1` 改为 `0` 且每个 `0` 变为 `1`。例如，二进制数 `"101"` 的二进制反码为 `"010"`。

给你一个十进制数 `N`，请你返回其二进制表示的反码所对应的十进制整数。

 

**示例 1：**

```
输入：5
输出：2
解释：5 的二进制表示为 "101"，其二进制反码为 "010"，也就是十进制中的 2 。
```

**示例 2：**

```
输入：7
输出：0
解释：7 的二进制表示为 "111"，其二进制反码为 "000"，也就是十进制中的 0 。
```

**示例 3：**

```
输入：10
输出：5
解释：10 的二进制表示为 "1010"，其二进制反码为 "0101"，也就是十进制中的 5 。
```

 

**提示：**

1. `0 <= N < 10^9`
2. 本题与 476：https://leetcode.cn/problems/number-complement/ 相同



```python
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        # n.bit_length() 返回 n 的二进制有效位数
        mask = (1 << n.bit_length()) - 1
        return mask ^ n  # 或者 return mask - n
```





## E1022.从根到叶的二进制数之和

binary, tree, https://leetcode.cn/problems/sum-of-root-to-leaf-binary-numbers/

给出一棵二叉树，其上每个结点的值都是 `0` 或 `1` 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。

- 例如，如果路径为 `0 -> 1 -> 1 -> 0 -> 1`，那么它表示二进制数 `01101`，也就是 `13` 。

对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。

返回这些数字之和。题目数据保证答案是一个 **32 位** 整数。

 

**示例 1：**

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/sum-of-root-to-leaf-binary-numbers.png" alt="img" style="zoom:50%;" />

```
输入：root = [1,0,1,0,1,0,1]
输出：22
解释：(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
```

**示例 2：**

```
输入：root = [0]
输出：0
```

 

**提示：**

- 树中的节点数在 `[1, 1000]` 范围内
- `Node.val` 仅为 `0` 或 `1` 



**`path` 是可变列表，在递归中被多个分支共享**。需要回溯。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        paths = []

        def dfs(node, path):
            # 将当前节点的值（0 或 1）作为字符加入路径
            path.append(str(node.val))

            # 如果是叶子节点，保存当前路径的拷贝
            if not node.left and not node.right:
                paths.append(path[:])  # 注意：必须拷贝！
            else:
                # 递归左右子树（如果存在）
                if node.left:
                    dfs(node.left, path)
                if node.right:
                    dfs(node.right, path)

            # 回溯：移除当前节点，返回上一层
            path.pop()

        dfs(root, [])

        ans = 0
        for path in paths:
            ans += int(''.join(path), 2)
        return ans
```





思路：数值累加方式

- 使用 DFS 递归遍历树。
- 每向下一层，当前路径的二进制值可以这样更新：`current_value = current_value * 2 + node.val`
- 到达叶子节点时，将当前值加入总和。
- **不需要存储所有路径**，直接累加即可，节省空间。

------

优化后的代码（推荐）：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_val):
            if not node:
                return 0
            current_val = current_val * 2 + node.val
            # 如果是叶子节点，返回当前路径的值
            if not node.left and not node.right:
                return current_val
            # 否则继续递归左右子树
            return dfs(node.left, current_val) + dfs(node.right, current_val)
        
        return dfs(root, 0)
```

**优点：**

- **时间复杂度**：O(N)，每个节点访问一次。
- **空间复杂度**：O(H)，H 是树的高度（递归栈）。
- **简洁高效**：无需额外存储路径，直接计算数值。
- **正确处理二进制构建**：根到叶子，高位到低位。



## 1078.Bigram分词

strings, https://leetcode.cn/problems/occurrences-after-bigram/

给出第一个词 `first` 和第二个词 `second`，考虑在某些文本 `text` 中可能以 `"first second third"` 形式出现的情况，其中 `second` 紧随 `first` 出现，`third` 紧随 `second` 出现。

对于每种这样的情况，将第三个词 "`third`" 添加到答案中，并返回答案。

 

**示例 1：**

```
输入：text = "alice is a good girl she is a good student", first = "a", second = "good"
输出：["girl","student"]
```

**示例 2：**

```
输入：text = "we will we will rock you", first = "we", second = "will"
输出：["we","rock"]
```

 

**提示：**

- `1 <= text.length <= 1000`
- `text` 由小写英文字母和空格组成
- `text` 中的所有单词之间都由 **单个空格字符** 分隔
- `1 <= first.length, second.length <= 10`
- `first` 和 `second` 由小写英文字母组成
- `text` 不包含任何前缀或尾随空格。



```python
from typing import List
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans = []
        text = text.split()
        for i in range(len(text) - 2):
            if text[i] == first and text[i + 1] == second:
                ans.append(text[i + 2])

        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.findOcurrences("alice is a good girl she is a good student", "a", "good"))
```



为了优化这段代码，我们可以考虑以下几点：

1. **减少不必要的列表切分和索引操作**：通过使用生成器表达式来直接迭代文本中的单词组合。
2. **提高可读性和简洁性**：使代码更加直观易懂。

以下是优化后的代码实现：

```python
from typing import List

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        # 使用zip函数配合切片来简化三元组的查找过程
        return [word for prev, curr, word in zip(words[:-2], words[1:-1], words[2:]) if prev == first and curr == second]

if __name__ == "__main__":
    sol = Solution()
    print(sol.findOcurrences("alice is a good girl she is a good student", "a", "good"))  # 示例输入
```

**优化点解释**：

- **`zip(words[:-2], words[1:-1], words[2:])`**：这个技巧利用了Python的`zip`函数与切片功能，同时遍历三个连续的单词。`words[:-2]`表示除了最后两个元素的所有元素，`words[1:-1]`表示从第二个到倒数第二个的所有元素，而`words[2:]`则是从第三个到最后的所有元素。这样可以一次性获取所有可能的三元组（prev, curr, word）。

- **列表推导式**：在列表推导式中直接检查当前三元组的第一个和第二个元素是否匹配给定的`first`和`second`字符串，如果是，则将第三个元素添加到结果列表中。

这种方法不仅减少了手动管理索引的复杂度，还使得代码更加简洁易读，同时也保持了原有的功能和效率。



【罗锐，工学院，2025 级】思路：

- ~~虽然这题用正则表达式做好像反而挺麻烦的且时间复杂度偏高，但为练习 `re` 库，倒也不妨边看库文档边写这题。~~
- 首先在文本前面插入空格，接下来匹配空格 + `first` 的模式，获得匹配结束的下一个位置。
- 具体地，可以通过 `pattern.finditer(text)` 的语句获得所有**不交**匹配对象的迭代器，`match.end()` 为匹配结束的下一个位置。
- 若匹配结束位置不在文本末尾，接下来截取匹配后面的部分，在这部分的开头匹配空格 + `second` + 空格 + 小写英文字母的非空组合（即 `[a-z]+`），若找到匹配则提取后面的单词作为 `third`。
- 具体地，可以通过在正则表达式 `f" {second} ([a-z]+)"` 中把后半部分用括号括起来，接下来若确能匹配，便可以使用匹配对象的方法 `matchobj.group(1)` 把它提取出来。这里的 $1$ 表示这是第 $1$ 个被括起来以便提取的部分。

代码：

```python
class Solution:
	def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
		pattern1 = re.compile(f" {first}")
		pattern2 = re.compile(f" {second} ([a-z]+)")

		text = f" {text}"
		iter = pattern1.finditer(text)

		result = []
		for match in iter:
			if match.end() == len(text):
				continue
			
			remain = text[match.end():]
			matchobj = re.match(pattern2, remain)
			if matchobj != None:
				result.append(matchobj.group(1))
		
		return result
```



## E1189.“气球” 的最大数量

implementation, https://leetcode.cn/problems/maximum-number-of-balloons/

给你一个字符串 `text`，你需要使用 `text` 中的字母来拼凑尽可能多的单词 **"balloon"（气球）**。

字符串 `text` 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 **"balloon"**。

 

**示例 1：**

**<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/202606220046619.jpeg" alt="img" style="zoom:67%;" />**

```
输入：text = "nlaebolko"
输出：1
```

**示例 2：**

**![img](https://raw.githubusercontent.com/GMyhf/img/main/img/202606220046179.jpeg)**

```
输入：text = "loonbalxballpoon"
输出：2
```

**示例 3：**

```
输入：text = "leetcode"
输出：0
```

 

**提示：**

- `1 <= text.length <= 10^4`
- `text` 全部由小写英文字母组成



这道题可以通过统计字符频次的方法来解决。

**解题思路**

单词 **"balloon"** 由以下字符组成：

- `'b'` 出现 1 次
- `'a'` 出现 1 次
- `'l'` 出现 2 次
- `'o'` 出现 2 次
- `'n'` 出现 1 次

要组成尽可能多的 "balloon"，每个单词所需的字母数量是固定的。因此，拼凑出的最大单词数量取决于这五个字母在输入字符串 `text` 中出现频次的限制（即瓶颈）：

- 对于 `'b'`、`'a'` 和 `'n'`，每个单词需要 1 个，所以它们的限制分别是 `count('b')`、`count('a')` 和 `count('n')`。
- 对于 `'l'` 和 `'o'`，每个单词需要 2 个，所以它们的限制分别是 `count('l') // 2` 和 `count('o') // 2`（整除）。

我们只需统计这些字符在 `text` 中的出现次数，并取上述限制条件中的最小值即可。

**Python 代码实现**

```python
from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # 统计 text 中每个字符出现的频次
        counts = Counter(text)
        
        # 计算拼凑 "balloon" 的最大数量
        return min(
            counts['b'],
            counts['a'],
            counts['l'] // 2,
            counts['o'] // 2,
            counts['n']
        )
```

**复杂度分析**

- **时间复杂度**：$O(N)$，其中 $N$ 是字符串 `text` 的长度。我们需要遍历一次字符串来统计字符频次，之后获取各个特定字符频次并求最小值的时间复杂度为 $O(1)$。
- **空间复杂度**：$O(1)$。虽然使用了哈希表存储频次，但由于输入只包含小写英文字母，哈希表的大小最多为 26，占用常数级别的额外空间。





## E1200.最小绝对差

implementation, https://leetcode.cn/problems/minimum-absolute-difference/

给你个整数数组 `arr`，其中每个元素都 **不相同**。

请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。

每对元素对 `[a,b`] 如下：

- `a , b` 均为数组 `arr` 中的元素
- `a < b`
- `b - a` 等于 `arr` 中任意两个元素的最小绝对差

 

**示例 1：**

```
输入：arr = [4,2,1,3]
输出：[[1,2],[2,3],[3,4]]
```

**示例 2：**

```
输入：arr = [1,3,6,10,15]
输出：[[1,3]]
```

**示例 3：**

```
输入：arr = [3,8,-10,23,19,-4,-14,27]
输出：[[-14,-10],[19,23],[23,27]]
```

 

**提示：**

- `2 <= arr.length <= 10^5`
- `-10^6 <= arr[i] <= 10^6`



```python
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        min_diff = float('inf')
        
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < min_diff:
                min_diff = diff
                ans = [[arr[i - 1], arr[i]]]  # 重置结果
            elif diff == min_diff:
                ans.append([arr[i - 1], arr[i]])
        
        return ans
```



## E1260.二维网格迁移

matrix, https://leetcode.cn/problems/shift-2d-grid/

给你一个 `m` 行 `n` 列的二维网格 `grid` 和一个整数 `k`。你需要将 `grid` 迁移 `k` 次。

每次「迁移」操作将会引发下述活动：

- 位于 `grid[i][j]`（`j < n - 1`）的元素将会移动到 `grid[i][j + 1]`。
- 位于 `grid[i][n - 1]` 的元素将会移动到 `grid[i + 1][0]`。
- 位于 `grid[m - 1][n - 1]` 的元素将会移动到 `grid[0][0]`。

请你返回 `k` 次迁移操作后最终得到的 **二维网格**。

 

**示例 1：**

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/e1-1.png" alt="img" style="zoom: 33%;" />

```
输入：grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
输出：[[9,1,2],[3,4,5],[6,7,8]]
```

**示例 2：**

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/e2-1.png" alt="img" style="zoom:50%;" />

```
输入：grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
输出：[[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
```

**示例 3：**

```
输入：grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
输出：[[1,2,3],[4,5,6],[7,8,9]]
```

 

**提示：**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m <= 50`
- `1 <= n <= 50`
- `-1000 <= grid[i][j] <= 1000`
- `0 <= k <= 100`



这个问题可以通过将二维网格“打平”成一维列表来简化。

**解题思路**

1.  **映射关系**：
    观察题目描述的迁移规则，你会发现这本质上是将二维数组看作一个一维序列，然后将该序列循环右移 $k$ 次。
    *   二维网格大小为 $m \times n$，总元素个数为 $S = m \times n$。
    *   二维坐标 $(i, j)$ 对应一维索引为 $idx = i \times n + j$。
    *   经过 $k$ 次迁移后，原来的元素会移动到新的一维索引：$new\_idx = (idx + k) \pmod S$。

2.  **具体步骤**：
    *   **计算参数**：获取行数 `m` 和列数 `n`。
    *   **简化 $k$**：因为移动 $m \times n$ 次网格会回到原状，所以我们令 $k = k \pmod{(m \times n)}$。
    *   **打平网格**：将二维数组 `grid` 转换为一个一维列表 `flat`。
    *   **循环移动**：利用 Python 的切片特性，将 `flat` 列表向右循环移动 $k$ 位：`flat[-k:] + flat[:-k]`。
    *   **重构网格**：将移动后的一维列表重新填充回 $m \times n$ 的二维数组。

**代码实现**

```python
from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        num_elements = m * n
        
        # 1. 实际上移动 k 次相当于移动 k % (m * n) 次
        k %= num_elements
        if k == 0:
            return grid
        
        # 2. 将二维网格展平成一维列表
        flat = []
        for row in grid:
            flat.extend(row)
            
        # 3. 这里的迁移操作等同于一维列表的循环右移
        # 将最后 k 个元素移到最前面
        shifted_flat = flat[-k:] + flat[:-k]
        
        # 4. 将一维列表重新构造成二维网格
        res = []
        for i in range(0, num_elements, n):
            res.append(shifted_flat[i : i + n])
            
        return res
```

**复杂度分析**

*   **时间复杂度**：$O(m \times n)$。我们需要遍历整个网格来展平它，然后再遍历一次来重构它。
*   **空间复杂度**：$O(m \times n)$。我们需要一个额外的列表来存储展平后的数据以及最终的结果网格。

**进阶：原地修改（可选）**

如果面试要求尽量减少空间开销，可以使用一维坐标转换公式直接填充结果数组，或者通过多次翻转（Reverse）实现原地的循环移位。但在本题 $m, n \le 50$ 的数据范围内，上述 Pythonic 的写法最为简洁高效。





## E1266.访问所有点的最小时间

math, https://leetcode.cn/problems/minimum-time-visiting-all-points/)

平面上有 `n` 个点，点的位置用整数坐标表示 `points[i] = [xi, yi]` 。请你计算访问所有这些点需要的 **最小时间**（以秒为单位）。

你需要按照下面的规则在平面上移动：

- 每一秒内，你可以：
  - 沿水平方向移动一个单位长度，或者
  - 沿竖直方向移动一个单位长度，或者
  - 跨过对角线移动 `sqrt(2)` 个单位长度（可以看作在一秒内向水平和竖直方向各移动一个单位长度）。
- 必须按照数组中出现的顺序来访问这些点。
- 在访问某个点时，可以经过该点后面出现的点，但经过的那些点不算作有效访问。

**示例 1：**

<img src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/11/24/1626_example_1.png" alt="img" style="zoom: 67%;" />

```
输入：points = [[1,1],[3,4],[-1,0]]
输出：7
解释：一条最佳的访问路径是： [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
从 [1,1] 到 [3,4] 需要 3 秒 
从 [3,4] 到 [-1,0] 需要 4 秒
一共需要 7 秒
```

**示例 2：**

```
输入：points = [[3,2],[-2,2]]
输出：5
```

**提示：**

- `points.length == n`
- `1 <= n <= 100`
- `points[i].length == 2`
- `-1000 <= points[i][0], points[i][1] <= 1000`



```python
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        cnt = 0
        cx, cy = points[0]
        for point in points[1:]:
            nx, ny = point
            cnt += max(abs(cx - nx), abs(cy - ny))
            cx, cy = nx, ny 
        return cnt
        
```



## 1295.统计位数为偶数的数字

https://leetcode.cn/problems/find-numbers-with-even-number-of-digits/

给你一个整数数组 `nums`，请你返回其中包含 **偶数** 个数位的数字的个数。

 

**示例 1：**

```
输入：nums = [12,345,2,6,7896]
输出：2
解释：
12 是 2 位数字（位数为偶数） 
345 是 3 位数字（位数为奇数）  
2 是 1 位数字（位数为奇数） 
6 是 1 位数字 位数为奇数） 
7896 是 4 位数字（位数为偶数）  
因此只有 12 和 7896 是位数为偶数的数字
```

**示例 2：**

```
输入：nums = [555,901,482,1771]
输出：1 
解释： 
只有 1771 是位数为偶数的数字。
```

 

**提示：**

- `1 <= nums.length <= 500`
- `1 <= nums[i] <= 10^5`



```python
from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count
```





## 1287.有序数组中出现次数超过25%的元素

https://leetcode.cn/problems/element-appearing-more-than-25-in-sorted-array/

给你一个非递减的 **有序** 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。

请你找到并返回这个整数。

**示例：**

```
输入：arr = [1,2,2,6,6,6,6,7,10]
输出：6
```

**提示：**

- `1 <= arr.length <= 10^4`
- `0 <= arr[i] <= 10^5`



```python
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]
        
        threshold = n / 4
        cur, cnt, eps = arr[0], 1, 1e-7
        for fast in arr[1:]:
            if fast == cur:
                cnt += 1
                if cnt - threshold > eps:
                    return fast
            else:
                cur, cnt = fast, 1
```



```python
from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # 计算阈值（数组长度的1/4）
        threshold = len(arr) / 4
        
        # 遍历数组，检查每个元素与其后第threshold个元素是否相同
        for i in range(len(arr)):
            if arr[i] == arr[i + int(threshold)]:
                return arr[i]
        
        # 如果没有找到（理论上不会到达这里，因为题目保证了存在这样的元素）
        return -1
```



## 1299.将每个元素替换为右侧最大元素

dp, https://leetcode.cn/problems/replace-elements-with-greatest-element-on-right-side/

给你一个数组 `arr` ，请你将每个元素用它右边最大的元素替换，如果是最后一个元素，用 `-1` 替换。

完成所有替换操作后，请你返回这个数组。

 

**示例 1：**

```
输入：arr = [17,18,5,4,6,1]
输出：[18,6,6,6,1,-1]
解释：
- 下标 0 的元素 --> 右侧最大元素是下标 1 的元素 (18)
- 下标 1 的元素 --> 右侧最大元素是下标 4 的元素 (6)
- 下标 2 的元素 --> 右侧最大元素是下标 4 的元素 (6)
- 下标 3 的元素 --> 右侧最大元素是下标 4 的元素 (6)
- 下标 4 的元素 --> 右侧最大元素是下标 5 的元素 (1)
- 下标 5 的元素 --> 右侧没有其他元素，替换为 -1
```

**示例 2：**

```
输入：arr = [400]
输出：[-1]
解释：下标 0 的元素右侧没有其他元素。
```

 

**提示：**

- `1 <= arr.length <= 10^4`
- `1 <= arr[i] <= 10^5`



```python
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        dp = [0]*n
        dp[-1] = -1
        for i in range(n-2, -1, -1):
            dp[i] = max(dp[i+1], arr[i+1])

        return dp   
```



## E1331.数组序号转换

implementation, https://leetcode.cn/problems/rank-transform-of-an-array/

给你一个整数数组 `arr` ，请你将数组中的每个元素替换为它们排序后的序号。

序号代表了一个元素有多大。序号编号的规则如下：

- 序号从 1 开始编号。
- 一个元素越大，那么序号越大。如果两个元素相等，那么它们的序号相同。
- 每个数字的序号都应该尽可能地小。

 

**示例 1：**

```
输入：arr = [40,10,20,30]
输出：[4,1,2,3]
解释：40 是最大的元素。 10 是最小的元素。 20 是第二小的数字。 30 是第三小的数字。
```

**示例 2：**

```
输入：arr = [100,100,100]
输出：[1,1,1]
解释：所有元素有相同的序号。
```

**示例 3：**

```
输入：arr = [37,12,28,9,100,56,80,5,12]
输出：[5,3,4,2,8,6,7,1,3]
```

 

**提示：**

- `0 <= arr.length <= 10^5`
- `-10^9 <= arr[i] <= 10^9`



这个问题可以通过排序和哈希表来解决。具体步骤如下：

**解题思路**

1. **去重并排序**：
   通过 `set(arr)` 去除数组中的重复元素，然后使用 `sorted()` 进行升序排序。排序后的数组中，每个元素的索引（加 1）即为其对应的序号。

2. **建立映射关系**：
   遍历排序后的唯一元素列表，使用哈希表（Python 中的字典）存储每个元素与其序号的映射关系。

3. **生成结果数组**：
   遍历原数组 `arr`，利用哈希表将每个元素替换为其对应的序号。

**Python 3 实现**

```python
from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # 1. 去重并排序
        sorted_unique = sorted(set(arr))
        
        # 2. 建立元素到序号的映射关系
        rank_map = {num: i + 1 for i, num in enumerate(sorted_unique)}
        
        # 3. 根据映射关系转换原数组
        return [rank_map[num] for num in arr]
```

**复杂度分析**

- **时间复杂度**：$O(N \log N)$，其中 $N$ 是数组 `arr` 的长度。去重操作需要 $O(N)$ 时间，排序长度最多为 $N$ 的数组需要 $O(N \log N)$ 时间，建立哈希表和重构数组分别需要 $O(N)$ 时间。
- **空间复杂度**：$O(N)$，用于存储去重后的数组以及哈希表映射关系。





## E1356.根据数字二进制下 1 的数目排序

bit manipulation, https://leetcode.cn/problems/sort-integers-by-the-number-of-1-bits/

给你一个整数数组 `arr` 。请你将数组中的元素按照其二进制表示中数字 **1** 的数目升序排序。

如果存在多个数字二进制中 **1** 的数目相同，则必须将它们按照数值大小升序排列。

请你返回排序后的数组。

 

**示例 1：**

```
输入：arr = [0,1,2,3,4,5,6,7,8]
输出：[0,1,2,4,8,3,5,6,7]
解释：[0] 是唯一一个有 0 个 1 的数。
[1,2,4,8] 都有 1 个 1 。
[3,5,6] 有 2 个 1 。
[7] 有 3 个 1 。
按照 1 的个数排序得到的结果数组为 [0,1,2,4,8,3,5,6,7]
```

**示例 2：**

```
输入：arr = [1024,512,256,128,64,32,16,8,4,2,1]
输出：[1,2,4,8,16,32,64,128,256,512,1024]
解释：数组中所有整数二进制下都只有 1 个 1 ，所以你需要按照数值大小将它们排序。
```

**示例 3：**

```
输入：arr = [10000,10000]
输出：[10000,10000]
```

**示例 4：**

```
输入：arr = [2,3,5,7,11,13,17,19]
输出：[2,3,5,17,7,11,13,19]
```

**示例 5：**

```
输入：arr = [10,100,1000,10000]
输出：[10,100,10000,1000]
```

 

**提示：**

- `1 <= arr.length <= 500`
- `0 <= arr[i] <= 10^4`



```python
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key = lambda x: (x.bit_count(), x))
        return arr
```





## 1399.统计最大组的数目

hash table, https://leetcode.cn/problems/count-largest-group/

给你一个整数 `n` 。请你先求出从 `1` 到 `n` 的每个整数 10 进制表示下的数位和（每一位上的数字相加），然后把数位和相等的数字放到同一个组中。

请你统计每个组中的数字数目，并返回数字数目并列最多的组有多少个。

 

**示例 1：**

```
输入：n = 13
输出：4
解释：总共有 9 个组，将 1 到 13 按数位求和后这些组分别是：
[1,10]，[2,11]，[3,12]，[4,13]，[5]，[6]，[7]，[8]，[9]。总共有 4 个组拥有的数字并列最多。
```

**示例 2：**

```
输入：n = 2
输出：2
解释：总共有 2 个大小为 1 的组 [1]，[2]。
```

**示例 3：**

```
输入：n = 15
输出：6
```

**示例 4：**

```
输入：n = 24
输出：5
```

 

**提示：**

- `1 <= n <= 10^4`



```python
class Solution:
    def countLargestGroup(self, n: int) -> int:
        def digit_sum(num):
            return sum(int(digit) for digit in str(num))

        group_counts = {}
        for i in range(1, n + 1):
            s = digit_sum(i)
            if s not in group_counts:
                group_counts[s] = 0
            group_counts[s] += 1

        max_count = max(group_counts.values())
        return list(group_counts.values()).count(max_count)

if __name__ == "__main__":
    solution = Solution()
    print(solution.countLargestGroup(13))
    print(solution.countLargestGroup(24))
```



## E1550.存在连续三个奇数的数组

https://leetcode.cn/problems/three-consecutive-odds/

给你一个整数数组 `arr`，请你判断数组中是否存在连续三个元素都是奇数的情况：如果存在，请返回 `true` ；否则，返回 `false` 。

 

**示例 1：**

```
输入：arr = [2,6,4,1]
输出：false
解释：不存在连续三个元素都是奇数的情况。
```

**示例 2：**

```
输入：arr = [1,2,34,3,4,5,7,23,12]
输出：true
解释：存在连续三个元素都是奇数的情况，即 [5,7,23] 。
```

 

**提示：**

- `1 <= arr.length <= 1000`
- `1 <= arr[i] <= 1000`



```python
from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # 遍历数组，直到倒数第三个元素
        for i in range(len(arr) - 2):
            if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
                return True
        return False
```



## 1534.统计好三元组

https://leetcode.cn/problems/count-good-triplets/description/

给你一个整数数组 `arr` ，以及 `a`、`b` 、`c` 三个整数。请你统计其中好三元组的数量。

如果三元组 `(arr[i], arr[j], arr[k])` 满足下列全部条件，则认为它是一个 **好三元组** 。

- `0 <= i < j < k < arr.length`
- `|arr[i] - arr[j]| <= a`
- `|arr[j] - arr[k]| <= b`
- `|arr[i] - arr[k]| <= c`

其中 `|x|` 表示 `x` 的绝对值。

返回 **好三元组的数量** 。

 

**示例 1：**

```
输入：arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
输出：4
解释：一共有 4 个好三元组：[(3,0,1), (3,0,1), (3,1,1), (0,1,1)] 。
```

**示例 2：**

```
输入：arr = [1,1,2,2,3], a = 0, b = 0, c = 1
输出：0
解释：不存在满足所有条件的三元组。
```

 

**提示：**

- `3 <= arr.length <= 100`
- `0 <= arr[i] <= 1000`
- `0 <= a, b, c <= 1000`



```python
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        cnt = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c :
                        cnt += 1
        
        return cnt
```



## E1582.二进制矩阵中的特殊位置

matrix, https://leetcode.cn/problems/special-positions-in-a-binary-matrix/

给定一个 `m x n` 的二进制矩阵 `mat`，返回矩阵 `mat` 中特殊位置的数量。

如果位置 `(i, j)` 满足 `mat[i][j] == 1` 并且行 `i` 与列 `j` 中的所有其他元素都是 `0`（行和列的下标从 **0** 开始计数），那么它被称为 **特殊** 位置。

 

**示例 1：**

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/special1.jpg" alt="img" style="zoom:67%;" />

```
输入：mat = [[1,0,0],[0,0,1],[1,0,0]]
输出：1
解释：位置 (1, 2) 是一个特殊位置，因为 mat[1][2] == 1 且第 1 行和第 2 列的其他所有元素都是 0。
```

**示例 2：**

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/special-grid.jpg" alt="img" style="zoom:67%;" />

```
输入：mat = [[1,0,0],[0,1,0],[0,0,1]]
输出：3
解释：位置 (0, 0)，(1, 1) 和 (2, 2) 都是特殊位置。
```

 

**提示：**

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 100`
- `mat[i][j]` 是 `0` 或 `1`。



```python
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        # 预计算每行、每列的和
        row_sum = [sum(row) for row in mat]
        col_sum = [sum(mat[i][j] for i in range(m)) for j in range(n)]
        
        cnt = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                    cnt += 1
        
        return cnt
```





## 1656.设计有序流

https://leetcode.cn/problems/design-an-ordered-stream/

有 `n` 个 `(id, value)` 对，其中 `id` 是 `1` 到 `n` 之间的一个整数，`value` 是一个字符串。不存在 `id` 相同的两个 `(id, value)` 对。

设计一个流，以 **任意** 顺序获取 `n` 个 `(id, value)` 对，并在多次调用时 **按 `id` 递增的顺序** 返回一些值。

实现 `OrderedStream` 类：

- `OrderedStream(int n)` 构造一个能接收 `n` 个值的流，并将当前指针 `ptr` 设为 `1` 。

- ```
  String[] insert(int id, String value)
  ```

   

  向流中存储新的

   

  ```
  (id, value)
  ```

   

  对。存储后：

  - 如果流存储有 `id = ptr` 的 `(id, value)` 对，则找出从 `id = ptr` 开始的 **最长 id 连续递增序列** ，并 **按顺序** 返回与这些 id 关联的值的列表。然后，将 `ptr` 更新为最后那个 `id + 1` 。
  - 否则，返回一个空列表。

 

**示例：**

**<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/15/q1.gif" alt="img" style="zoom:50%;" />**

```
输入
["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
[[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
输出
[null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]

解释
OrderedStream os= new OrderedStream(5);
os.insert(3, "ccccc"); // 插入 (3, "ccccc")，返回 []
os.insert(1, "aaaaa"); // 插入 (1, "aaaaa")，返回 ["aaaaa"]
os.insert(2, "bbbbb"); // 插入 (2, "bbbbb")，返回 ["bbbbb", "ccccc"]
os.insert(5, "eeeee"); // 插入 (5, "eeeee")，返回 []
os.insert(4, "ddddd"); // 插入 (4, "ddddd")，返回 ["ddddd", "eeeee"]
```

 

**提示：**

- `1 <= n <= 1000`
- `1 <= id <= n`
- `value.length == 5`
- `value` 仅由小写字母组成
- 每次调用 `insert` 都会使用一个唯一的 `id`
- 恰好调用 `n` 次 `insert`



```python
class OrderedStream:

    def __init__(self, n: int):
        # 初始化流和指针
        self.stream = [None] * (n + 1)  # 0-index 不用
        self.ptr = 1        

    def insert(self, idKey: int, value: str) -> List[str]:
        # 插入值到流中
        self.stream[idKey] = value
        result = []
        
        # 如果 idKey == ptr，开始寻找连续的 id
        if idKey == self.ptr:
            # 查找连续的 id
            while self.ptr <= len(self.stream) - 1 and self.stream[self.ptr]:
                result.append(self.stream[self.ptr])
                self.ptr += 1
        
        return result        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
```



## E1732.找到最高海拔

implementation, https://leetcode.cn/problems/find-the-highest-altitude/

有一个自行车手打算进行一场公路骑行，这条路线总共由 `n + 1` 个不同海拔的点组成。自行车手从海拔为 `0` 的点 `0` 开始骑行。

给你一个长度为 `n` 的整数数组 `gain` ，其中 `gain[i]` 是点 `i` 和点 `i + 1` 的 **净海拔高度差**（`0 <= i < n`）。请你返回 **最高点的海拔** 。

 

**示例 1：**

```
输入：gain = [-5,1,5,0,-7]
输出：1
解释：海拔高度依次为 [0,-5,-4,1,1,-6] 。最高海拔为 1 。
```

**示例 2：**

```
输入：gain = [-4,-3,-2,-1,4,3,2]
输出：0
解释：海拔高度依次为 [0,-4,-7,-9,-10,-6,-3,-1] 。最高海拔为 0 。
```

 

**提示：**

- `n == gain.length`
- `1 <= n <= 100`
- `-100 <= gain[i] <= 100`



```python
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        cur = 0
        for i in range(n):
            gain[i] += cur
            cur = gain[i]
        
        return max(max(gain), 0)
```





## 1742.盒子中小球的最大数量

https://leetcode.cn/problems/maximum-number-of-balls-in-a-box/

你在一家生产小球的玩具厂工作，有 `n` 个小球，编号从 `lowLimit` 开始，到 `highLimit` 结束（包括 `lowLimit`和 `highLimit` ，即 `n == highLimit - lowLimit + 1`）。另有无限数量的盒子，编号从 `1` 到 `infinity` 。

你的工作是将每个小球放入盒子中，其中盒子的编号应当等于小球编号上每位数字的和。例如，编号 `321` 的小球应当放入编号 `3 + 2 + 1 = 6` 的盒子，而编号 `10` 的小球应当放入编号 `1 + 0 = 1` 的盒子。

给你两个整数 `lowLimit` 和 `highLimit` ，返回放有最多小球的盒子中的小球数量*。*如果有多个盒子都满足放有最多小球，只需返回其中任一盒子的小球数量。

 

**示例 1：**

```
输入：lowLimit = 1, highLimit = 10
输出：2
解释：
盒子编号：1 2 3 4 5 6 7 8 9 10 11 ...
小球数量：2 1 1 1 1 1 1 1 1 0  0  ...
编号 1 的盒子放有最多小球，小球数量为 2 。
```

**示例 2：**

```
输入：lowLimit = 5, highLimit = 15
输出：2
解释：
盒子编号：1 2 3 4 5 6 7 8 9 10 11 ...
小球数量：1 1 1 1 2 2 1 1 1 0  0  ...
编号 5 和 6 的盒子放有最多小球，每个盒子中的小球数量都是 2 。
```

**示例 3：**

```
输入：lowLimit = 19, highLimit = 28
输出：2
解释：
盒子编号：1 2 3 4 5 6 7 8 9 10 11 12 ...
小球数量：0 1 1 1 1 1 1 1 1 2  0  0  ...
编号 10 的盒子放有最多小球，小球数量为 2 。
```

 

**提示：**

- `1 <= lowLimit <= highLimit <= 10^5`



511ms，击败27.72%

```python
from collections import defaultdict

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        # 使用defaultdict来存储每个盒子中球的数量
        box_counts = defaultdict(int)
        
        for ball in range(lowLimit, highLimit + 1):
            # 计算球编号各位数字之和作为盒子的索引
            box_index = sum(int(digit) for digit in str(ball))
            box_counts[box_index] += 1
        
        # 找到包含最多球的盒子中的球数
        max_balls_count = max(box_counts.values())
        
        return max_balls_count
```



## E1752.检查数组是否经排序和轮转得到

https://leetcode.cn/problems/check-if-array-is-sorted-and-rotated/

给你一个数组 `nums` 。`nums` 的源数组中，所有元素与 `nums` 相同，但按非递减顺序排列。

如果 `nums` 能够由源数组轮转若干位置（包括 0 个位置）得到，则返回 `true` ；否则，返回 `false`。

源数组中可能存在 **重复项** 。

**注意：**数组 `A` 在轮转 `x` 个位置后得到长度相同的数组 `B` ，使得对于每一个有效的下标 `i`，满足 `B[i] == A[(i+x) % A.length]`。

 

**示例 1：**

```
输入：nums = [3,4,5,1,2]
输出：true
解释：[1,2,3,4,5] 为有序的源数组。
可以轮转 x = 2 个位置，使新数组从值为 3 的元素开始：[3,4,5,1,2] 。
```

**示例 2：**

```
输入：nums = [2,1,3,4]
输出：false
解释：源数组无法经轮转得到 nums 。
```

**示例 3：**

```
输入：nums = [1,2,3]
输出：true
解释：[1,2,3] 为有序的源数组。
可以轮转 x = 0 个位置（即不轮转）得到 nums 。
```

 

**提示：**

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`



利用**循环数组**的思想来简化这段代码。一个数组如果是“分类排序且旋转过的”，那么在将它看作一个首尾相连的环形数组时，**最多只能存在一个位置满足“前一个元素大于后一个元素”**。

以下是两种优化方案：

**方案一：使用单次循环（推荐，逻辑更清晰）**

这种方法遍历数组，并对比相邻元素（包括最后一个元素与第一个元素的对比）。如果逆序对（即前一个数大于后一个数）的数量大于 1，则返回 `False`。

```python
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        cnt = 0
        
        for i in range(n):
            # 使用取模运算 (i + 1) % n 来连接首尾
            if nums[i] > nums[(i + 1) % n]:
                cnt += 1
                if cnt > 1:
                    return False
                    
        return True
```

**方案二：Python 风格的一行式写法**

如果你更倾向于简洁的代码，可以使用 Python 的生成器表达式和 `sum` 函数：

```python
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        return sum(nums[i] > nums[(i + 1) % n] for i in range(n)) <= 1
```

**复杂度分析**

* **时间复杂度**：$O(n)$，其中 $n$ 是数组的长度。我们只需要遍历一次数组。
* **空间复杂度**：$O(1)$，仅使用了常数级别的额外空间。



## E1784.检查二进制字符串字段

string, https://leetcode.cn/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

给你一个二进制字符串 `s` ，该字符串 **不含前导零** 。

如果 `s` 包含 **零个或一个由连续的 `'1'` 组成的字段** ，返回 `true` 。否则，返回 `false` 。

 

**示例 1：**

```
输入：s = "1001"
输出：false
解释：由连续若干个 '1' 组成的字段数量为 2，返回 false
```

**示例 2：**

```
输入：s = "110"
输出：true
```

 

**提示：**

- `1 <= s.length <= 100`
- `s[i]` 为 `'0'` 或 `'1'`
- `s[0]` 为 `'1'`



**题意解析**

给定一个**不含前导零**的二进制字符串 `s`（即 `s[0] == '1'`），判断其中 **连续的 `'1'` 组成的段（segment）是否最多只有一个**。

**关键观察**

因为字符串**以 `'1'` 开头**，所以第一个字符就是 `'1'`。
如果后面在某个 `'0'` **之后**又出现了 `'1'`，那就说明出现了**第二个 `'1'` 段**，应该返回 `False`。

**解法思路**

遍历字符串，设置一个标志表示是否已经“进入0区”：

- 初始时还没遇到 `'0'`；
- 遇到 `'0'` 后，标记为“已进入0区”；
- 如果在“已进入0区”后又遇到 `'1'`，直接返回 `False`；
- 遍历完都没问题，返回 `True`。

或者更简单一点：**检查是否在字符串中存在 `"01"` 子串**。

**代码实现**

**方法一：使用子串判断（最简洁）**

```python
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s
```

**方法二：手动遍历（更直观）**

```python
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        seen_zero = False
        for c in s:
            if c == '0':
                seen_zero = True
            elif seen_zero and c == '1':
                return False
        return True
```



## E1848.到目标元素的最小距离

implementation, https://leetcode.cn/problems/minimum-distance-to-the-target-element/

给你一个整数数组 `nums` （下标 **从 0 开始** 计数）以及两个整数 `target` 和 `start` ，请你找出一个下标 `i` ，满足 `nums[i] == target` 且 `abs(i - start)` **最小化** 。注意：`abs(x)` 表示 `x` 的绝对值。

返回 `abs(i - start)` 。

题目数据保证 `target` 存在于 `nums` 中。

 

**示例 1：**

```
输入：nums = [1,2,3,4,5], target = 5, start = 3
输出：1
解释：nums[4] = 5 是唯一一个等于 target 的值，所以答案是 abs(4 - 3) = 1 。
```

**示例 2：**

```
输入：nums = [1], target = 1, start = 0
输出：0
解释：nums[0] = 1 是唯一一个等于 target 的值，所以答案是 abs(0 - 0) = 0 。
```

**示例 3：**

```
输入：nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0
输出：0
解释：nums 中的每个值都是 1 ，但 nums[0] 使 abs(i - start) 的结果得以最小化，所以答案是 abs(0 - 0) = 0 。
```

 

**提示：**

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^4`
- `0 <= start < nums.length`
- `target` 存在于 `nums` 中



这是一个经典的数组遍历问题。题目要求在数组中找到所有等于 `target` 的元素，并计算它们的下标 `i` 与给定 `start` 之间的绝对距离，最后返回这些距离中的最小值。

**解题思路**

1. **遍历数组**：我们可以遍历整个数组 `nums`。

2. **匹配目标**：检查当前元素 `nums[i]` 是否等于 `target`。

3. **计算距离**：如果相等，计算当前下标与 `start` 的距离，即 `abs(i - start)`。

4. **更新最小值**：维护一个变量来记录遍历过程中遇到的最小距离。

   由于数组长度最大只有 1000，直接进行 $O(n)$ 的线性扫描效率非常高。

**代码实现**

```python
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        # 初始化最小距离为一个很大的值
        min_dist = float('inf')
        
        # 遍历数组及其下标
        for i, num in enumerate(nums):
            # 如果找到目标元素
            if num == target:
                # 计算当前下标到 start 的距离
                dist = abs(i - start)
                # 更新最小距离
                if dist < min_dist:
                    min_dist = dist
                    
        return min_dist
```

**优化写法（Pythonic）**

利用 Python 的生成器表达式和 `min` 函数，可以将代码简化为一行：

```python
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        return min(abs(i - start) for i, num in enumerate(nums) if num == target)
```

**复杂度分析**

*   **时间复杂度**：$O(n)$，其中 $n$ 是数组 `nums` 的长度。我们需要完整遍历一次数组。
*   **空间复杂度**：$O(1)$，只使用了常数级别的额外空间来存储距离值。





## 1863.找出所有子集的异或总和再求和

backtracking, https://leetcode.cn/problems/sum-of-all-subset-xor-totals/

一个数组的 **异或总和** 定义为数组中所有元素按位 `XOR` 的结果；如果数组为 **空** ，则异或总和为 `0` 。

- 例如，数组 `[2,5,6]` 的 **异或总和** 为 `2 XOR 5 XOR 6 = 1` 。

给你一个数组 `nums` ，请你求出 `nums` 中每个 **子集** 的 **异或总和** ，计算并返回这些值相加之 **和** 。

**注意：**在本题中，元素 **相同** 的不同子集应 **多次** 计数。

数组 `a` 是数组 `b` 的一个 **子集** 的前提条件是：从 `b` 删除几个（也可能不删除）元素能够得到 `a` 。

 

**示例 1：**

```
输入：nums = [1,3]
输出：6
解释：[1,3] 共有 4 个子集：
- 空子集的异或总和是 0 。
- [1] 的异或总和为 1 。
- [3] 的异或总和为 3 。
- [1,3] 的异或总和为 1 XOR 3 = 2 。
0 + 1 + 3 + 2 = 6
```

**示例 2：**

```
输入：nums = [5,1,6]
输出：28
解释：[5,1,6] 共有 8 个子集：
- 空子集的异或总和是 0 。
- [5] 的异或总和为 5 。
- [1] 的异或总和为 1 。
- [6] 的异或总和为 6 。
- [5,1] 的异或总和为 5 XOR 1 = 4 。
- [5,6] 的异或总和为 5 XOR 6 = 3 。
- [1,6] 的异或总和为 1 XOR 6 = 7 。
- [5,1,6] 的异或总和为 5 XOR 1 XOR 6 = 2 。
0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28
```

**示例 3：**

```
输入：nums = [3,4,5,6,7,8]
输出：480
解释：每个子集的全部异或总和值之和为 480 。
```

 

**提示：**

- `1 <= nums.length <= 12`
- `1 <= nums[i] <= 20`



```python
from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        subs = []

        # 深度优先搜索生成所有子集
        def dfs(start: int, sub_nums: List[int]):
            # 将当前子集加入结果
            subs.append(sub_nums[:])

            # 遍历剩余元素，生成新的子集
            for i in range(start, n):
                sub_nums.append(nums[i])  # 选择当前元素
                dfs(i + 1, sub_nums)      # 递归处理下一个元素
                sub_nums.pop()            # 回溯，撤销选择

        # 从索引 0 开始生成子集
        dfs(0, [])

        # 计算所有子集的 XOR 和
        ans = 0
        for sub in subs:
            xor = 0
            for num in sub:
                xor ^= num
            ans += xor

        return ans

if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    result = solution.subsetXORSum(nums)
    print(result)  # Output: 6
```



## E1877.数组中最大数对和的最小值

two pointers, https://leetcode.cn/problems/minimize-maximum-pair-sum-in-array/)

一个数对 `(a,b)` 的 **数对和** 等于 `a + b` 。**最大数对和** 是一个数对数组中最大的 **数对和** 。

- 比方说，如果我们有数对 `(1,5)` ，`(2,3)` 和 `(4,4)`，**最大数对和** 为 `max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8` 。

给你一个长度为 **偶数** `n` 的数组 `nums` ，请你将 `nums` 中的元素分成 `n / 2` 个数对，使得：

- `nums` 中每个元素 **恰好** 在 **一个** 数对中，且
- **最大数对和** 的值 **最小** 。

请你在最优数对划分的方案下，返回最小的 **最大数对和** 。

 

**示例 1：**

```
输入：nums = [3,5,2,3]
输出：7
解释：数组中的元素可以分为数对 (3,3) 和 (5,2) 。
最大数对和为 max(3+3, 5+2) = max(6, 7) = 7 。
```

**示例 2：**

```
输入：nums = [3,5,4,2,4,6]
输出：8
解释：数组中的元素可以分为数对 (3,5)，(4,4) 和 (6,2) 。
最大数对和为 max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8 。
```

 

**提示：**

- `n == nums.length`
- `2 <= n <= 10^5`
- `n` 是 **偶数** 。
- `1 <= nums[i] <= 10^5`



```python
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -float('inf')
        nums.sort()
        for i in range(n //2 ):
            tmp = nums[i] + nums[n - 1 - i]
            if tmp > ans:
                ans = tmp
        
        return ans
```



## E1886.判断矩阵经轮转后是否一致

matrix, https://leetcode.cn/problems/determine-whether-matrix-can-be-obtained-by-rotation/

给你两个大小为 `n x n` 的二进制矩阵 `mat` 和 `target` 。现 **以 90 度顺时针轮转** 矩阵 `mat` 中的元素 **若干次** ，如果能够使 `mat` 与 `target` 一致，返回 `true` ；否则，返回 `false` *。*

 

**示例 1：**

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/grid3.png" alt="img" style="zoom:67%;" />

```
输入：mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
输出：true
解释：顺时针轮转 90 度一次可以使 mat 和 target 一致。
```

**示例 2：**

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/grid4.png" alt="img" style="zoom:67%;" />

```
输入：mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
输出：false
解释：无法通过轮转矩阵中的元素使 equal 与 target 一致。
```

**示例 3：**

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/grid4-20260322122827329.png" alt="img" style="zoom:67%;" />

```
输入：mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
输出：true
解释：顺时针轮转 90 度两次可以使 mat 和 target 一致。
```

 

**提示：**

- `n == mat.length == target.length`
- `n == mat[i].length == target[i].length`
- `1 <= n <= 10`
- `mat[i][j]` 和 `target[i][j]` 不是 `0` 就是 `1`



转置 + 行逆序 = 顺时针旋转 90 度。Python 的列表比较运算符 `==` 是**递归深度比较**。

```python
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # 最多尝试 4 次 (0°, 90°, 180°, 270°)
        for _ in range(4):
            # 1. 判断当前是否相等 (直接利用 Python 列表特性)
            if mat == target:
                return True
            
            # 2. 顺时针旋转 90 度准备下一次循环
            # 技巧：转置 (zip) + 每行逆序 ([::-1])
            mat = [list(row)[::-1] for row in zip(*mat)]
        
        # 4 次都不匹配
        return False
```

> 1. 定义区别
>
> **转置 (Transpose)**
>
> - **定义**：将矩阵的**行变成列，列变成行**。即元素 $A_{ij}$ 变为 $A_{ji}$。
> - **几何意义**：相当于沿着**主对角线**（左上角到右下角）进行**镜像翻转**。
> - **公式**：$B_{ij} = A_{ji}$
> - **Python 实现**：`zip(*mat)`
>
> **顺时针旋转 90 度 (Clockwise Rotation 90°)**
>
> - **定义**：整个矩阵向右倒一下。
> - **几何意义**：原来的第一行变成了最后一列，原来的最后一行变成了第一列。
> - **公式**：$B_{ij} = A_{n-1-j, i}$ （其中 $n$ 是矩阵边长）
> - **实现步骤**：**先转置，再左右翻转每一行**。
>
> ---
>
> 2. 直观对比示例
>
> 假设有一个 $2 \times 2$ 矩阵：
> $$
> A = \begin{bmatrix} 
> 1 & 2 \\ 
> 3 & 4 
> \end{bmatrix}
> $$
>
> **操作 A：转置 (`zip(*mat)`)**
>
> 沿着主对角线（1和4连线）翻转：
>
> - 2 和 3 互换位置。
>
> $$
> A^T = \begin{bmatrix} 
> 1 & 3 \\ 
> 2 & 4 
> \end{bmatrix}
> $$
>
> *(注意：1还在左上，4还在右下)*
>
> **操作 B：顺时针旋转 90 度**
>
> 想象把纸向右旋转 90 度：
>
> - 第一行 `[1, 2]` 变成了最后一列（竖着放）。
> - 第二行 `[3, 4]` 变成了第一列（竖着放）。
>
> $$
> A_{rot} = \begin{bmatrix} 
> 3 & 1 \\ 
> 4 & 2 
> \end{bmatrix}
> $$
>
> 所以，**转置 + 行逆序 = 顺时针旋转 90 度**。





## E1920.基于排列构建数组

math, https://leetcode.cn/problems/build-array-from-permutation/

给你一个 **从 0 开始的排列** `nums`（**下标也从 0 开始**）。请你构建一个 **同样长度** 的数组 `ans`，其中，对于每个 `i`（`0 <= i < nums.length`），都满足 `ans[i] = nums[nums[i]]` 。返回构建好的数组 `ans` 。

**从 0 开始的排列** `nums` 是一个由 `0` 到 `nums.length - 1`（`0` 和 `nums.length - 1` 也包含在内）的不同整数组成的数组。

 

**示例 1：**

```
输入：nums = [0,2,1,5,3,4]
输出：[0,1,2,4,5,3]
解释：数组 ans 构建如下：
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    = [0,1,2,4,5,3]
```

**示例 2：**

```
输入：nums = [5,0,1,2,3,4]
输出：[4,5,0,1,2,3]
解释：数组 ans 构建如下：
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
    = [4,5,0,1,2,3]
```

 

**提示：**

- `1 <= nums.length <= 1000`
- `0 <= nums[i] < nums.length`
- `nums` 中的元素 **互不相同**

 

**进阶：**你能在不使用额外空间的情况下解决此问题吗（即 `O(1)` 内存）？



✅ 解法一：直接构造（简单易懂）

直接遍历数组，对每个位置 `i`，取 `nums[i]` 作为下标再次查找，得到 `nums[nums[i]]`，然后放入结果数组中。

**时间复杂度：O(n)**  
**空间复杂度：O(n)**

```python
from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]
```



✅ 解法二：原地修改（进阶问题：O(1) 额外空间）

如果题目要求 **不使用额外空间**，那么我们需要想办法把结果保存在原数组中。可以利用数学方法将新值和旧值存储在一个数中，最后再还原出来。

**原理：**

因为 `nums[i] < 1000`（根据提示），我们可以使用一个大于 `1001` 的基数（比如 `1001`）来编码两个值到一个整数中：

```text
nums[i] = nums[i] + (nums[nums[i]] % 1001) * 1001
```

之后再解码：

```text
nums[i] = nums[i] // 1001
```

这样我们就实现了 **原地修改**，没有使用额外空间。

**代码如下：**

```python
from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # 第一步：将 nums[i] 编码为 nums[i] + nums[nums[i]] * n
        for i in range(n):
            # 使用 nums[nums[i]] 的原始值，需要取模
            val = nums[nums[i]]  # 先取出要用的值
            nums[i] = nums[i] + (val % n) * n  # 防止重复编码
        
        # 第二步：解码，得到最终结果
        for i in range(n):
            nums[i] = nums[i] // n
        
        return nums
```

> 🔍 注意：这里我们用到了 `n` 作为基数，是因为 `nums[i] < n`，所以 `nums[i] * n + nums[nums[i]]` 能够唯一表示两个值。

📌 关键点解释：

- ```
  val = nums[nums[i]]
  ```

  - 这里我们是想拿到原始数组中 `nums[nums[i]]` 的值。
  - 但由于 `nums[i]` 可能已经被修改过，所以我们需要每次使用 `val % n` 来获取原始值。

- 在最后通过 `/ n` 得到新的值，实现原地替换。



总结：

| 方法     | 时间复杂度 | 空间复杂度 | 是否原地 |
| -------- | ---------- | ---------- | -------- |
| 直接构造 | O(n)       | O(n)       | ❌        |
| 原地修改 | O(n)       | O(1)       | ✅        |



## E1984.学生分数的最小差值

sliding window, https://leetcode.cn/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

给你一个 **下标从 0 开始** 的整数数组 `nums` ，其中 `nums[i]` 表示第 `i` 名学生的分数。另给你一个整数 `k` 。

从数组中选出任意 `k` 名学生的分数，使这 `k` 个分数间 **最高分** 和 **最低分** 的 **差值** 达到 **最小化** 。

返回可能的 **最小差值** 。

 

**示例 1：**

```
输入：nums = [90], k = 1
输出：0
解释：选出 1 名学生的分数，仅有 1 种方法：
- [90] 最高分和最低分之间的差值是 90 - 90 = 0
可能的最小差值是 0
```

**示例 2：**

```
输入：nums = [9,4,1,7], k = 2
输出：2
解释：选出 2 名学生的分数，有 6 种方法：
- [9,4,1,7] 最高分和最低分之间的差值是 9 - 4 = 5
- [9,4,1,7] 最高分和最低分之间的差值是 9 - 1 = 8
- [9,4,1,7] 最高分和最低分之间的差值是 9 - 7 = 2
- [9,4,1,7] 最高分和最低分之间的差值是 4 - 1 = 3
- [9,4,1,7] 最高分和最低分之间的差值是 7 - 4 = 3
- [9,4,1,7] 最高分和最低分之间的差值是 7 - 1 = 6
可能的最小差值是 2
```

 

**提示：**

- `1 <= k <= nums.length <= 1000`
- `0 <= nums[i] <= 10^5`



```python
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(len(nums) - (k - 1)):
            ans = min(ans, nums[i + k - 1] - nums[i])
        return ans
```



## E2078.两栋颜色不同且距离最远的房子

greedy, https://leetcode.cn/problems/two-furthest-houses-with-different-colors/

街上有 `n` 栋房子整齐地排成一列，每栋房子都粉刷上了漂亮的颜色。给你一个下标从 **0** 开始且长度为 `n` 的整数数组 `colors` ，其中 `colors[i]` 表示第 `i` 栋房子的颜色。

返回 **两栋** 颜色 **不同** 房子之间的 **最大** 距离。

第 `i` 栋房子和第 `j` 栋房子之间的距离是 `abs(i - j)` ，其中 `abs(x)` 是 `x` 的绝对值。

 

**示例 1：**

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/eg1.png" alt="img" style="zoom:67%;" />

```
输入：colors = [1,1,1,6,1,1,1]
输出：3
解释：上图中，颜色 1 标识成蓝色，颜色 6 标识成红色。
两栋颜色不同且距离最远的房子是房子 0 和房子 3 。
房子 0 的颜色是颜色 1 ，房子 3 的颜色是颜色 6 。两栋房子之间的距离是 abs(0 - 3) = 3 。
注意，房子 3 和房子 6 也可以产生最佳答案。
```

**示例 2：**

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/eg2.png" alt="img" style="zoom:67%;" />

```
输入：colors = [1,8,3,8,3]
输出：4
解释：上图中，颜色 1 标识成蓝色，颜色 8 标识成黄色，颜色 3 标识成绿色。
两栋颜色不同且距离最远的房子是房子 0 和房子 4 。
房子 0 的颜色是颜色 1 ，房子 4 的颜色是颜色 3 。两栋房子之间的距离是 abs(0 - 4) = 4 。
```

**示例 3：**

```
输入：colors = [0,1]
输出：1
解释：两栋颜色不同且距离最远的房子是房子 0 和房子 1 。
房子 0 的颜色是颜色 0 ，房子 1 的颜色是颜色 1 。两栋房子之间的距离是 abs(0 - 1) = 1 。
```

 

**提示：**

- `n == colors.length`
- `2 <= n <= 100`
- `0 <= colors[i] <= 100`
- 生成的测试数据满足 **至少** 存在 2 栋颜色不同的房子



```python
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        ans = -float('inf')
        for i in range(n-1):
            for j in range(i+1,n):
                if colors[i] != colors[j]:
                    ans = max(ans, abs(i -j))
        
        return ans
```





这个问题可以通过**贪心算法**在 $O(n)$ 的时间复杂度内解决。

**解题思路**

要找到两栋颜色不同且距离最远的房子，直观上我们应该尽可能选择靠近两端的房子。最大距离只可能出现在以下两种情况之一：

1.  **左侧端点固定在第 0 栋房子**：我们从最右侧（第 $n-1$ 栋）开始向左扫描，找到第一栋颜色与第 0 栋不同的房子，此时的距离为 `j - 0`。
2.  **右侧端点固定在最后一栋房子**：我们从最左侧（第 0 栋）开始向右扫描，找到第一栋颜色与最后一栋（第 $n-1$ 栋）不同的房子，此时的距离为 `(n - 1) - i`。

**为什么这样是对的？**
假设最远距离的两个房子下标是 $i$ 和 $j$（$i < j$）。如果 $i > 0$ 且 $j < n-1$：

*   如果 `colors[0] != colors[j]`，那么 $(0, j)$ 的距离一定比 $(i, j)$ 更远。
*   如果 `colors[0] == colors[j]`，因为我们已知 `colors[i] != colors[j]`，那么必然有 `colors[i] != colors[0]`，此时 $(0, i)$ 也是一组解（虽然不一定比 $(i, j)$ 长，但观察逻辑可知，最长距离的边界一定可以推导至数组的其中一个端点）。

**Python 代码实现**

```python
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        max_dist = 0
        
        # 情况 1：固定左端点（下标 0），从右向左找第一个颜色不同的
        for j in range(n - 1, 0, -1):
            if colors[j] != colors[0]:
                max_dist = max(max_dist, j)
                break
        
        # 情况 2：固定右端点（下标 n-1），从左向右找第一个颜色不同的
        for i in range(n - 1):
            if colors[i] != colors[n - 1]:
                max_dist = max(max_dist, n - 1 - i)
                break
                
        return max_dist
```

**复杂度分析**

*   **时间复杂度**：$O(n)$。我们最多只需要遍历两次数组。
*   **空间复杂度**：$O(1)$。只使用了常数级别的额外空间。



> 这是一个非常好的直觉。我们可以通过**反证法**（Proof by Contradiction）来证明：**最大距离的两个房子中，至少有一个必然是数组的起点（0）或终点（n-1）。**
>
> 让我们分情况讨论：
>
> 假设存在一组最优解 $(i, j)$，其中 $0 < i < j < n-1$，且 $colors[i] \neq colors[j]$。
>
> **1. 如果 $colors[0] \neq colors[j]$**
>
> 那么下标对 $(0, j)$ 也是合法的（颜色不同）。
> 由于 $i > 0$，所以距离 $j - 0$ 必然大于 $j - i$。
> 这说明 $(i, j)$ 此时**不是**最大距离，$(0, j)$ 更优。
>
> **2. 如果 $colors[n-1] \neq colors[i]$**
>
> 那么下标对 $(i, n-1)$ 也是合法的（颜色不同）。
> 由于 $j < n-1$，所以距离 $(n-1) - i$ 必然大于 $j - i$。
> 这说明 $(i, j)$ 此时**不是**最大距离，$(i, n-1)$ 更优。
>
> **3. 如果以上两种情况都不满足呢？**
>
> 即：
>
> *   $colors[0] = colors[j]$
> *   $colors[n-1] = colors[i]$
>
> 由于我们已知 $colors[i] \neq colors[j]$，根据上面的等式代换，可以得出：
> $$colors[n-1] \neq colors[0]$$
> 既然 $0$ 号和 $n-1$ 号颜色不同，那么下标对 $(0, n-1)$ 就是合法的。
> 显然，距离 $(n-1) - 0$ 是整个数组中**物理上的最大可能距离**。
> 它必然大于或等于任何中间的距离 $j - i$。
>
> 





## E2094.找出3位偶数

hash table, sorting, https://leetcode.cn/problems/finding-3-digit-even-numbers/

给你一个整数数组 `digits` ，其中每个元素是一个数字（`0 - 9`）。数组中可能存在重复元素。

你需要找出 **所有** 满足下述条件且 **互不相同** 的整数：

- 该整数由 `digits` 中的三个元素按 **任意** 顺序 **依次连接** 组成。
- 该整数不含 **前导零**
- 该整数是一个 **偶数**

例如，给定的 `digits` 是 `[1, 2, 3]` ，整数 `132` 和 `312` 满足上面列出的全部条件。

将找出的所有互不相同的整数按 **递增顺序** 排列，并以数组形式返回*。*

 

**示例 1：**

```
输入：digits = [2,1,3,0]
输出：[102,120,130,132,210,230,302,310,312,320]
解释：
所有满足题目条件的整数都在输出数组中列出。 
注意，答案数组中不含有 奇数 或带 前导零 的整数。
```

**示例 2：**

```
输入：digits = [2,2,8,8,2]
输出：[222,228,282,288,822,828,882]
解释：
同样的数字（0 - 9）在构造整数时可以重复多次，重复次数最多与其在 digits 中出现的次数一样。 
在这个例子中，数字 8 在构造 288、828 和 882 时都重复了两次。 
```

**示例 3：**

```
输入：digits = [3,7,5]
输出：[]
解释：
使用给定的 digits 无法构造偶数。
```

 

**提示：**

- `3 <= digits.length <= 100`
- `0 <= digits[i] <= 9`





**题目要求**：

从一个整数数组 `digits` 中选出 **所有互不相同的三元组** 组成一个三位数（或更多位？但题目示例只考虑了三位数），满足：

1. 使用数组中的三个元素组成；
2. 不能以 **前导零** 开头；
3. 必须是 **偶数**；
4. 返回结果中不能有重复数字（即使组合方式不同，只要最终数值相同就算重复）；
5. 结果按 **递增顺序** 排列。

---

**分析**：

- 因为要选出 **三个元素** 构成一个整数，所以生成的是 **三位数**。
- 所有三位数的范围是 `[100, 999]`。
- 要保证三位数是 **偶数**，最后一位必须是偶数（即 0、2、4、6、8）。
- 我们需要从 `digits` 中选出所有的 **不重复的三位数排列**，注意去重！

---

**解法思路**：

1. 使用 `collections.Counter` 统计每个数字出现的次数。
2. 枚举所有可能的三位数（100 到 999）。
3. 对于每个三位数：
   - 检查它是否是偶数；
   - 检查它的每一位数字是否能由 `digits` 提供（使用频率不能超过原始出现次数）；
4. 如果符合条件，加入结果列表；
5. 最后排序返回。



```python
from typing import List
from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        from collections import Counter
        
        count = Counter(digits)
        result = []

        for num in range(100, 1000):
            if num % 2 != 0:
                continue
            
            d1 = num // 100  # 百位
            d2 = (num // 10) % 10  # 十位
            d3 = num % 10  # 个位
            
            # 构造当前数字的 Counter
            temp = [d1, d2, d3]
            temp_counter = Counter(temp)

            # 检查是否每个数字都不超过原数组中出现的次数
            valid = True
            for k, v in temp_counter.items():
                if count[k] < v:
                    valid = False
                    break
            
            if valid:
                result.append(num)
        
        return sorted(result)
```

时间复杂度分析：

- 枚举最多 900 个三位数；
- 每次检查最多 3 个数字的频次；
- 总体效率很高，适用于 `digits.length <= 100` 的限制。



## E2144.打折购买糖果的最小开销

greedy, https://leetcode.cn/problems/minimum-cost-of-buying-candies-with-discount/

一家商店正在打折销售糖果。每购买 **两个** 糖果，商店会 **免费** 送一个糖果。

免费送的糖果唯一的限制是：它的价格需要小于等于购买的两个糖果价格的 **较小值** 。

- 比方说，总共有 `4` 个糖果，价格分别为 `1` ，`2` ，`3` 和 `4` ，一位顾客买了价格为 `2` 和 `3` 的糖果，那么他可以免费获得价格为 `1` 的糖果，但不能获得价格为 `4` 的糖果。

给你一个下标从 **0** 开始的整数数组 `cost` ，其中 `cost[i]` 表示第 `i` 个糖果的价格，请你返回获得 **所有** 糖果的 **最小** 总开销。

 

**示例 1：**

```
输入：cost = [1,2,3]
输出：5
解释：我们购买价格为 2 和 3 的糖果，然后免费获得价格为 1 的糖果。
总开销为 2 + 3 = 5 。这是开销最小的 唯一 方案。
注意，我们不能购买价格为 1 和 3 的糖果，并免费获得价格为 2 的糖果。
这是因为免费糖果的价格必须小于等于购买的 2 个糖果价格的较小值。
```

**示例 2：**

```
输入：cost = [6,5,7,9,2,2]
输出：23
解释：最小总开销购买糖果方案为：
- 购买价格为 9 和 7 的糖果
- 免费获得价格为 6 的糖果
- 购买价格为 5 和 2 的糖果
- 免费获得价格为 2 的最后一个糖果
因此，最小总开销为 9 + 7 + 5 + 2 = 23 。
```

**示例 3：**

```
输入：cost = [5,5]
输出：10
解释：由于只有 2 个糖果，我们需要将它们都购买，而且没有免费糖果。
所以总最小开销为 5 + 5 = 10 。
```



为了求得购买所有糖果的最小总开销，我们可以采用**贪心算法**。

**思路分析**

为了让总开销最小，我们应当尽可能让价格高的糖果作为“免费赠送”的糖果。
根据规则，每购买两个糖果，可以免费获得一个价格小于等于这两个糖果价格较小值的糖果。

1. **排序**：我们将糖果价格从大到小（降序）进行排序。
2. **分组**：从最贵的糖果开始，每三个糖果分成一组。例如对于排序后的数组：`[c1, c2, c3, c4, c5, c6, ...]`（满足 $c_1 \ge c_2 \ge c_3 \ge \dots$）。
   * 第一组：`c1` 和 `c2` 购买，`c3` 免费送（因为 $c_3 \le c_2 \le c_1$）。
   * 第二组：`c4` 和 `c5` 购买，`c6` 免费送（因为 $c_6 \le c_5 \le c_4$）。
   * 依此类推。
3. **统计开销**：在遍历排序后的数组时，下标（从0开始）满足 `(i + 1) % 3 == 0` 的糖果可以免费获得，其余的糖果需要自费购买。

这种贪心策略能够确保我们每次都将当前最贵的两个糖果搭配，从而免单第三贵的糖果，使得免费糖果的总价值达到最大，进而使总开销达到最小。

**Python 代码实现**

```python
from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # 将糖果价格从大到小排序
        cost.sort(reverse=True)
        
        total_cost = 0
        for i in range(len(cost)):
            # 每 3 个糖果中的第 3 个（下标为 2, 5, 8...）是免费的，不需要累加
            if (i + 1) % 3 != 0:
                total_cost += cost[i]
                
        return total_cost
```

**复杂度分析**

- **时间复杂度**：$O(N \log N)$，其中 $N$ 为糖果的数量。主要的时间开销在于对价格数组进行排序。
- **空间复杂度**：$O(1)$ 或 $O(N)$，具体取决于排序算法的实现（Python 的 `sort` 方法使用的是 Timsort，空间复杂度为 $O(N)$）。





## 2176.统计数组中相等且可以被整除的数对

https://leetcode.cn/problems/count-equal-and-divisible-pairs-in-an-array/

给你一个下标从 **0** 开始长度为 `n` 的整数数组 `nums` 和一个整数 `k` ，请你返回满足 `0 <= i < j < n` ，`nums[i] == nums[j]` 且 `(i * j)` 能被 `k` 整除的数对 `(i, j)` 的 **数目** 。

 

**示例 1：**

```
输入：nums = [3,1,2,2,2,1,3], k = 2
输出：4
解释：
总共有 4 对数符合所有要求：
- nums[0] == nums[6] 且 0 * 6 == 0 ，能被 2 整除。
- nums[2] == nums[3] 且 2 * 3 == 6 ，能被 2 整除。
- nums[2] == nums[4] 且 2 * 4 == 8 ，能被 2 整除。
- nums[3] == nums[4] 且 3 * 4 == 12 ，能被 2 整除。
```

**示例 2：**

```
输入：nums = [1,2,3,4], k = 1
输出：0
解释：由于数组中没有重复数值，所以没有数对 (i,j) 符合所有要求。
```

 

**提示：**

- `1 <= nums.length <= 100`
- `1 <= nums[i], k <= 100`



```python
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    if (i*j) % k == 0:
                        cnt += 1
        
        return cnt
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



## 2255.统计是给定字符串前缀的字符串数目

https://leetcode.cn/problems/count-prefixes-of-a-given-string/

给你一个字符串数组 `words` 和一个字符串 `s` ，其中 `words[i]` 和 `s` 只包含 **小写英文字母** 。

请你返回 `words` 中是字符串 `s` **前缀** 的 **字符串数目** 。

一个字符串的 **前缀** 是出现在字符串开头的子字符串。**子字符串** 是一个字符串中的连续一段字符序列。

 

**示例 1：**

```
输入：words = ["a","b","c","ab","bc","abc"], s = "abc"
输出：3
解释：
words 中是 s = "abc" 前缀的字符串为：
"a" ，"ab" 和 "abc" 。
所以 words 中是字符串 s 前缀的字符串数目为 3 。
```

**示例 2：**

```
输入：words = ["a","a"], s = "aa"
输出：2
解释：
两个字符串都是 s 的前缀。
注意，相同的字符串可能在 words 中出现多次，它们应该被计数多次。
```

 

**提示：**

- `1 <= words.length <= 1000`
- `1 <= words[i].length, s.length <= 10`
- `words[i]` 和 `s` **只** 包含小写英文字母。



```python
from typing import List

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        # 生成所有可能的前缀
        s_set = {s[:i] for i in range(1, len(s) + 1)}
        
        # 统计 words 中有多少个是 s 的前缀
        cnt = sum(1 for word in words if word in s_set)
        
        return cnt
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



## 2269.找到一个数字的K美丽值

https://leetcode.cn/problems/find-the-k-beauty-of-a-number/

一个整数 `num` 的 **k** 美丽值定义为 `num` 中符合以下条件的 **子字符串** 数目：

- 子字符串长度为 `k` 。
- 子字符串能整除 `num` 。

给你整数 `num` 和 `k` ，请你返回 `num` 的 k 美丽值。

注意：

- 允许有 **前缀** **0** 。
- `0` 不能整除任何值。

一个 **子字符串** 是一个字符串里的连续一段字符序列。

 

**示例 1：**

```
输入：num = 240, k = 2
输出：2
解释：以下是 num 里长度为 k 的子字符串：
- "240" 中的 "24" ：24 能整除 240 。
- "240" 中的 "40" ：40 能整除 240 。
所以，k 美丽值为 2 。
```

**示例 2：**

```
输入：num = 430043, k = 2
输出：2
解释：以下是 num 里长度为 k 的子字符串：
- "430043" 中的 "43" ：43 能整除 430043 。
- "430043" 中的 "30" ：30 不能整除 430043 。
- "430043" 中的 "00" ：0 不能整除 430043 。
- "430043" 中的 "04" ：4 不能整除 430043 。
- "430043" 中的 "43" ：43 能整除 430043 。
所以，k 美丽值为 2 。
```

 

**提示：**

- `1 <= num <= 10^9`
- `1 <= k <= num.length` （将 `num` 视为字符串）







```python
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        n = len(s)
        if k > n:  # 如果k大于num的位数，则直接返回0
            return 0
        
        cnt = 0
        for i in range(n - k + 1):  # 确保考虑到所有长度为k的子串
            sub_num = int(s[i:i+k])
            if sub_num != 0 and num % sub_num == 0:  # 检查是否为有效除数
                cnt += 1
                
        return cnt
```



## 2278.字母在字符串中的百分比

https://leetcode.cn/problems/percentage-of-letter-in-string/

给你一个字符串 `s` 和一个字符 `letter` ，返回在 `s` 中等于 `letter` 字符所占的 **百分比** ，向下取整到最接近的百分比。

 

**示例 1：**

```
输入：s = "foobar", letter = "o"
输出：33
解释：
等于字母 'o' 的字符在 s 中占到的百分比是 2 / 6 * 100% = 33% ，向下取整，所以返回 33 。
```

**示例 2：**

```
输入：s = "jjjj", letter = "k"
输出：0
解释：
等于字母 'k' 的字符在 s 中占到的百分比是 0% ，所以返回 0 。
```

 

**提示：**

- `1 <= s.length <= 100`
- `s` 由小写英文字母组成
- `letter` 是一个小写英文字母



```python
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        cnt = 0
        for c in s:
            if c == letter:
                cnt += 1
        
        return cnt * 100 // len(s) 
```





## 2506.统计相似字符串对的数目

https://leetcode.cn/problems/count-pairs-of-similar-strings/

给你一个下标从 **0** 开始的字符串数组 `words` 。

如果两个字符串由相同的字符组成，则认为这两个字符串 **相似** 。

- 例如，`"abca"` 和 `"cba"` 相似，因为它们都由字符 `'a'`、`'b'`、`'c'` 组成。
- 然而，`"abacba"` 和 `"bcfd"` 不相似，因为它们不是相同字符组成的。

请你找出满足字符串 `words[i]` 和 `words[j]` 相似的下标对 `(i, j)` ，并返回下标对的数目，其中 `0 <= i < j <= words.length - 1` 。

 

**示例 1：**

```
输入：words = ["aba","aabb","abcd","bac","aabc"]
输出：2
解释：共有 2 对满足条件：
- i = 0 且 j = 1 ：words[0] 和 words[1] 只由字符 'a' 和 'b' 组成。 
- i = 3 且 j = 4 ：words[3] 和 words[4] 只由字符 'a'、'b' 和 'c' 。 
```

**示例 2：**

```
输入：words = ["aabb","ab","ba"]
输出：3
解释：共有 3 对满足条件：
- i = 0 且 j = 1 ：words[0] 和 words[1] 只由字符 'a' 和 'b' 组成。 
- i = 0 且 j = 2 ：words[0] 和 words[2] 只由字符 'a' 和 'b' 组成。 
- i = 1 且 j = 2 ：words[1] 和 words[2] 只由字符 'a' 和 'b' 组成。 
```

**示例 3：**

```
输入：words = ["nba","cba","dba"]
输出：0
解释：不存在满足条件的下标对，返回 0 。
```

 

**提示：**

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` 仅由小写英文字母组成



```python
from typing import List

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        # 使用字典记录每种字符组合出现的次数
        count_map = {}
        for word in words:
            # 对单词中的字符去重并排序，形成字符组合的标识符
            char_set = tuple(sorted(set(word)))
            if char_set not in count_map:
                count_map[char_set] = 0
            count_map[char_set] += 1
        
        # 计算具有相同字符组合的单词对数
        similar_pairs_cnt = 0
        for cnt in count_map.values():
            if cnt > 1:
                # 如果某个字符组合出现了n次，则有n*(n-1)/2个相似对
                similar_pairs_cnt += cnt * (cnt - 1) // 2
                
        return similar_pairs_cnt

if __name__ == "__main__":
    words = ["aba","aabb","abcd","bac","aabc"]
    print(Solution().similarPairs(words))
```





```python
from typing import List

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        words_new = []
        for i in words:
            words_new.append(''.join(sorted(set(list(i)))))
        #print(words_new)

        cnt = 0
        n = len(words_new)
        for i in range(n):
            for j in range(i+1, n):
                if words_new[i] == words_new[j]:
                    cnt += 1
        return cnt

if __name__ == "__main__":
    words = ["aba","aabb","abcd","bac","aabc"]
    print(Solution().similarPairs(words))
```



## E2515.到目标字符串的最短距离

implementation, https://leetcode.cn/problems/shortest-distance-to-target-string-in-a-circular-array/

给你一个下标从 **0** 开始的 **环形** 字符串数组 `words` 和一个字符串 `target` 。**环形数组** 意味着数组首尾相连。

- 形式上， `words[i]` 的下一个元素是 `words[(i + 1) % n]` ，而 `words[i]` 的前一个元素是 `words[(i - 1 + n) % n]` ，其中 `n` 是 `words` 的长度。

从 `startIndex` 开始，你一次可以用 `1` 步移动到下一个或者前一个单词。

返回到达目标字符串 `target` 所需的最短距离。如果 `words` 中不存在字符串 `target` ，返回 `-1` 。

**示例 1：**

```
输入：words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1
输出：1
解释：从下标 1 开始，可以经由以下步骤到达 "hello" ：
- 向右移动 3 个单位，到达下标 4 。
- 向左移动 2 个单位，到达下标 4 。
- 向右移动 4 个单位，到达下标 0 。
- 向左移动 1 个单位，到达下标 0 。
到达 "hello" 的最短距离是 1 。
```

**示例 2：**

```
输入：words = ["a","b","leetcode"], target = "leetcode", startIndex = 0
输出：1
解释：从下标 0 开始，可以经由以下步骤到达 "leetcode" ：
- 向右移动 2 个单位，到达下标 2 。
- 向左移动 1 个单位，到达下标 2 。
到达 "leetcode" 的最短距离是 1 。
```

**示例 3：**

```
输入：words = ["i","eat","leetcode"], target = "ate", startIndex = 0
输出：-1
解释：因为 words 中不存在字符串 "ate" ，所以返回 -1 。
```

 

**提示：**

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` 和 `target` 仅由小写英文字母组成
- `0 <= startIndex < words.length`



这个问题要求在环形数组中找到从 `startIndex` 到达目标字符串 `target` 的最短距离。由于数组是环形的，我们可以向左（逆时针）或向右（顺时针）移动。

**解题思路**

1.  **遍历数组**：遍历 `words` 数组中的每一个元素。
2.  **匹配目标**：如果当前元素 `words[i]` 等于 `target`。
3.  **计算距离**：
    *   在环形数组中，两个下标 $i$ 和 $j$ 之间的距离有两种走法：
        1.  直接相减的绝对值：$|i - j|$。
        2.  跨越首尾的距离：$n - |i - j|$（其中 $n$ 是数组长度）。
    *   这两者中的较小值即为从 `startIndex` 到当前下标 $i$ 的最短步数。
4.  **更新最小值**：在所有匹配到的下标中，记录这个最短步数的全局最小值。
5.  **边界处理**：如果遍历完整个数组都没有找到 `target`，则返回 -1。

**代码实现**

```python
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        # 初始化为一个不可能的大值，n 即可，因为最大距离不会超过 n-1
        min_dist = n
        
        found = False
        for i in range(n):
            if words[i] == target:
                found = True
                # 直接距离
                d1 = abs(i - startIndex)
                # 环形跨越首尾的距离
                d2 = n - d1
                
                # 取两者的最小值，并更新全局最小距离
                min_dist = min(min_dist, d1, d2)
        
        return min_dist if found else -1
```

**复杂度分析**

*   **时间复杂度**：$O(n \times L)$，其中 $n$ 是数组 `words` 的长度，$L$ 是字符串的平均长度。我们需要遍历一次数组，并且每次比较字符串需要 $O(L)$ 的时间。
*   **空间复杂度**：$O(1)$，除了存储输入的变量外，只使用了常数级别的额外空间。

**示例分析 (示例 1)**

输入：`words = ["hello","i","am","leetcode","hello"]`, `target = "hello"`, `startIndex = 1`

1.  数组长度 $n = 5$。
2.  下标 $0$ 处是 "hello"：
    *   距离 $d1 = |0 - 1| = 1$
    *   距离 $d2 = 5 - 1 = 4$
    *   当前最短距离 = $\min(1, 4) = 1$。
3.  下标 $4$ 处是 "hello"：
    *   距离 $d1 = |4 - 1| = 3$
    *   距离 $d2 = 5 - 3 = 2$
    *   当前最短距离 = $\min(1, 2) = 1$。
4.  最终结果为 1。



## E2553.分割数组中数字的数位

implementation, https://leetcode.cn/problems/separate-the-digits-in-an-array/

给你一个正整数数组 `nums` ，请你返回一个数组 `answer` ，你需要将 `nums` 中每个整数进行数位分割后，按照 `nums` 中出现的 **相同顺序** 放入答案数组中。

对一个整数进行数位分割，指的是将整数各个数位按原本出现的顺序排列成数组。

- 比方说，整数 `10921` ，分割它的各个数位得到 `[1,0,9,2,1]` 。

 

**示例 1：**

```
输入：nums = [13,25,83,77]
输出：[1,3,2,5,8,3,7,7]
解释：
- 分割 13 得到 [1,3] 。
- 分割 25 得到 [2,5] 。
- 分割 83 得到 [8,3] 。
- 分割 77 得到 [7,7] 。
answer = [1,3,2,5,8,3,7,7] 。answer 中的数字分割结果按照原数字在数组中的相同顺序排列。
```

**示例 2：**

```
输入：nums = [7,1,3,9]
输出：[7,1,3,9]
解释：nums 中每个整数的分割是它自己。
answer = [7,1,3,9] 。
```

 

**提示：**

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^5`



这道题的要求是将数组 `nums` 中的每个整数拆分为单个数字，并按照原有的顺序合并成一个新的数组。

**解题思路**

1.  **遍历数组**：遍历 `nums` 中的每一个整数。
2.  **转换数位**：对于每一个整数，我们需要获取它的每一个数字位。在 Python 中，最简单的方法是将整数转换为**字符串**。
3.  **提取并存储**：遍历转换后的字符串，将每个字符转回整数，并依次存入结果列表 `answer` 中。
4.  **返回结果**：遍历结束后，返回 `answer` 即可。

**代码实现**

```python
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        # 遍历输入数组中的每一个数字
        for num in nums:
            # 将数字转为字符串，以便遍历它的每一位
            s = str(num)
            for char in s:
                # 将字符转回整数并加入结果数组
                answer.append(int(char))
        return answer
```

**另一种更简洁的写法（列表推导式）**

你可以使用嵌套的列表推导式来完成这个任务：

```python
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(digit) for num in nums for digit in str(num)]
```

**复杂度分析**

*   **时间复杂度**：$O(n \cdot k)$，其中 $n$ 是数组 `nums` 的长度，$k$ 是数字的最大位数（在本题中，数字最大为 $10^5$，即 $k \le 6$）。我们需要遍历每个数字的所有位。
*   **空间复杂度**：$O(n \cdot k)$，我们需要一个额外的数组来存储所有的数位。



## E2574.左右元素和的差值

prefix sum, https://leetcode.cn/problems/left-and-right-sum-differences/

给你一个下标从 **0** 开始的长度为 `n` 的整数数组 `nums`。

定义两个数组 `leftSum` 和 `rightSum`，其中：

- `leftSum[i]` 是数组 `nums` 中下标 `i` 左侧元素之和。如果不存在对应的元素，`leftSum[i] = 0` 。
- `rightSum[i]` 是数组 `nums` 中下标 `i` 右侧元素之和。如果不存在对应的元素，`rightSum[i] = 0` 。

返回长度为 `n` 数组 `answer`，其中 `answer[i] = |leftSum[i] - rightSum[i]|`。

 

**示例 1：**

```
输入：nums = [10,4,8,3]
输出：[15,1,11,22]
解释：数组 leftSum 为 [0,10,14,22] 且数组 rightSum 为 [15,11,3,0] 。
数组 answer 为 [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22] 。
```

**示例 2：**

```
输入：nums = [1]
输出：[0]
解释：数组 leftSum 为 [0] 且数组 rightSum 为 [0] 。
数组 answer 为 [|0 - 0|] = [0] 。
```

 

**提示：**

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^5`



这道题可以通过维护一个**前缀和**和一个**后缀和**的思想来高效解决。

**解题思路**

如果要计算每一个位置 `i` 的 `leftSum[i]` 和 `rightSum[i]`：

1. **右侧元素之和** `rightSum[i]` 实际上等于 `整个数组的总和 - 左侧元素之和 leftSum[i] - 当前元素 nums[i]`。
2. 因此，不需要创建额外的 `leftSum` 和 `rightSum` 数组。我们可以先计算出数组的总和 `total_sum`。
3. 接着，在一次遍历中：
   - 维护一个变量 `left_sum`，初始化为 `0`。
   - 对于每个元素 `nums[i]`，其对应的右侧元素和为 `right_sum = total_sum - left_sum - nums[i]`。
   - 计算差值 `abs(left_sum - right_sum)` 并存入结果数组。
   - 更新 `left_sum = left_sum + nums[i]`，为计算下一个位置做准备。

这种方法只需要两轮遍历（第一轮求和，第二轮计算结果），时间复杂度为 $O(n)$，空间复杂度为 $O(1)$（不计入返回结果的数组空间）。

Python 代码实现

```python
from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        left_sum = 0
        answer = []
        
        for num in nums:
            right_sum = total_sum - left_sum - num
            answer.append(abs(left_sum - right_sum))
            left_sum += num
            
        return answer
```

**复杂度分析**

- **时间复杂度**：$O(n)$。其中 $n$ 是数组 `nums` 的长度。需要遍历一次数组求和，再遍历一次数组计算每个位置的差值。
- **空间复杂度**：$O(1)$。除去用于存储结果的 `answer` 数组，仅使用了 `total_sum`、`left_sum` 和 `right_sum` 等常数个额外变量。



如果按照题目定义，先显式地计算出每个位置的 `leftSum` 和 `rightSum` 数组，然后再计算它们差值的绝对值，也是一种非常直观且符合直觉的解法。

可以通过前缀和与后缀和的递推关系来分别计算这两个数组：

1. **计算 `leftSum`**：
   - `leftSum[0] = 0`
   - 对于 $i > 0$，`leftSum[i] = leftSum[i-1] + nums[i-1]`

2. **计算 `rightSum`**：
   - `rightSum[n-1] = 0`（其中 $n$ 为数组长度）
   - 对于 $i < n-1$（从右往左递推），`rightSum[i] = rightSum[i+1] + nums[i+1]`

3. **计算结果**：
   - 遍历每个位置，计算 `abs(leftSum[i] - rightSum[i])`。

Python 代码实现

```python
from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n
        
        # 1. 计算 leftSum
        for i in range(1, n):
            leftSum[i] = leftSum[i-1] + nums[i-1]
            
        # 2. 计算 rightSum (从右往左遍历)
        for i in range(n-2, -1, -1):
            rightSum[i] = rightSum[i+1] + nums[i+1]
            
        # 3. 计算绝对值差
        answer = []
        for i in range(n):
            answer.append(abs(leftSum[i] - rightSum[i]))
            
        return answer
```

**复杂度分析**

- **时间复杂度**：$O(n)$。分别进行了三次独立的循环（计算 `leftSum`、计算 `rightSum`、计算最终结果 `answer`），每次循环的长度为 $n$。总时间复杂度与数组长度成正比。
- **空间复杂度**：$O(n)$。除了返回的结果数组外，显式地创建了长度为 $n$ 的 `leftSum` 和 `rightSum` 数组。





## 2595.奇偶位数

https://leetcode.cn/problems/number-of-even-and-odd-bits/

给你一个 **正** 整数 `n` 。

用 `even` 表示在 `n` 的二进制形式（下标从 **0** 开始）中值为 `1` 的偶数下标的个数。

用 `odd` 表示在 `n` 的二进制形式（下标从 **0** 开始）中值为 `1` 的奇数下标的个数。

请注意，在数字的二进制表示中，位下标的顺序 **从右到左**。

返回整数数组 `answer` ，其中 `answer = [even, odd]` 。

 

**示例 1：**

**输入：**n = 50

**输出：**[1,2]

**解释：**

50 的二进制表示是 `110010`。

在下标 1，4，5 对应的值为 1。

**示例 2：**

**输入：**n = 2

**输出：**[0,1]

**解释：**

2 的二进制表示是 `10`。

只有下标 1 对应的值为 1。

 

**提示：**

- `1 <= n <= 1000`



```python
from typing import List
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        s = bin(n)[2:][::-1]
        even, odd = 0, 0
        for i in range(len(s)):
            if i & 1:
                if s[i] == '1':
                    odd += 1
            else:
                if s[i] == '1':
                    even += 1

        return [even, odd]

if __name__ == "__main__":
    sol = Solution()
    print(sol.evenOddBit(2))
```



```python
from typing import List

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even, odd = 0, 0
        index = 0
        while n > 0:
            if n & 1:  # Check if the least significant bit is 1
                if index % 2 == 0:
                    even += 1
                else:
                    odd += 1
            n >>= 1  # Shift right to process the next bit
            index += 1
        
        return [even, odd]

if __name__ == "__main__":
    sol = Solution()
    print(sol.evenOddBit(2))  # Example input
```



## 2614.对角线上的质数

matrix, https://leetcode.cn/problems/prime-in-diagonal/

给你一个下标从 **0** 开始的二维整数数组 `nums` 。

返回位于 `nums` 至少一条 **对角线** 上的最大 **质数** 。如果任一对角线上均不存在质数，返回 *0 。*

注意：

- 如果某个整数大于 `1` ，且不存在除 `1` 和自身之外的正整数因子，则认为该整数是一个质数。
- 如果存在整数 `i` ，使得 `nums[i][i] = val` 或者 `nums[i][nums.length - i - 1]= val` ，则认为整数 `val` 位于 `nums` 的一条对角线上。

![img](https://assets.leetcode.com/uploads/2023/03/06/screenshot-2023-03-06-at-45648-pm.png)

在上图中，一条对角线是 **[1,5,9]** ，而另一条对角线是 **[3,5,7]** 。

 

**示例 1：**

```
输入：nums = [[1,2,3],[5,6,7],[9,10,11]]
输出：11
解释：数字 1、3、6、9 和 11 是所有 "位于至少一条对角线上" 的数字。由于 11 是最大的质数，故返回 11 。
```

**示例 2：**

```
输入：nums = [[1,2,3],[5,17,7],[9,11,10]]
输出：17
解释：数字 1、3、9、10 和 17 是所有满足"位于至少一条对角线上"的数字。由于 17 是最大的质数，故返回 17 。
```

 

**提示：**

- `1 <= nums.length <= 300`
- `nums.length == numsi.length`
- `1 <= nums[i][j] <= 4*10^6`



```python
from typing import List

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def sieve(max_num):
            primes = [True] * (max_num + 1)
            primes[0], primes[1] = False, False
            for i in range(2, int(max_num**0.5) + 1):
                if primes[i]:
                    for j in range(i * i, max_num + 1, i):
                        primes[j] = False
            return primes
        
        # 找到nums中的最大值以确定筛选范围
        max_val = max(max(row) for row in nums)
        primes = sieve(max_val)
        
        res = 0
        n = len(nums)
        for i in range(n):
            # 主对角线元素
            if primes[nums[i][i]]:
                res = max(res, nums[i][i])
            # 副对角线元素
            if primes[nums[i][n - 1 - i]]:
                res = max(res, nums[i][n - 1 - i])
                
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.diagonalPrime([[1,2,3],[5,6,7],[9,10,11]]))  # 应该输出 7，因为 5 和 7 都是质数，但 7 更大
```



## 2643.一最多的行

https://leetcode.cn/problems/row-with-maximum-ones/

给你一个大小为 `m x n` 的二进制矩阵 `mat` ，请你找出包含最多 **1** 的行的下标（从 **0** 开始）以及这一行中 **1** 的数目。

如果有多行包含最多的 1 ，只需要选择 **行下标最小** 的那一行。

返回一个由行下标和该行中 1 的数量组成的数组。

 

**示例 1：**

```
输入：mat = [[0,1],[1,0]]
输出：[0,1]
解释：两行中 1 的数量相同。所以返回下标最小的行，下标为 0 。该行 1 的数量为 1 。所以，答案为 [0,1] 。 
```

**示例 2：**

```
输入：mat = [[0,0,0],[0,1,1]]
输出：[1,2]
解释：下标为 1 的行中 1 的数量最多。该行 1 的数量为 2 。所以，答案为 [1,2] 。
```

**示例 3：**

```
输入：mat = [[0,0],[1,1],[0,0]]
输出：[1,2]
解释：下标为 1 的行中 1 的数量最多。该行 1 的数量为 2 。所以，答案为 [1,2] 。
```

 

**提示：**

- `m == mat.length` 
- `n == mat[i].length` 
- `1 <= m, n <= 100` 
- `mat[i][j]` 为 `0` 或 `1`



```python
from typing import List

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_idx, max_v = -1, -1
        
        for i, row in enumerate(mat):
            # 计算当前行的1的数量
            count_ones = sum(row)
            # 更新最大值和对应的索引
            if count_ones > max_v:
                max_v = count_ones
                max_idx = i
                
        return [max_idx, max_v]
```



## 2716.最小化字符串长度

hash table, https://leetcode.cn/problems/minimize-string-length/

给你一个下标从 **0** 开始的字符串 `s` ，重复执行下述操作 **任意** 次：

- 在字符串中选出一个下标 `i` ，并使 `c` 为字符串下标 `i` 处的字符。并在 `i` **左侧**（如果有）和 **右侧**（如果有）各 **删除** 一个距离 `i` **最近** 的字符 `c` 。

请你通过执行上述操作任意次，使 `s` 的长度 **最小化** 。

返回一个表示 **最小化** 字符串的长度的整数。

 

**示例 1：**

```
输入：s = "aaabc"
输出：3
解释：在这个示例中，s 等于 "aaabc" 。我们可以选择位于下标 1 处的字符 'a' 开始。接着删除下标 1 左侧最近的那个 'a'（位于下标 0）以及下标 1 右侧最近的那个 'a'（位于下标 2）。执行操作后，字符串变为 "abc" 。继续对字符串执行任何操作都不会改变其长度。因此，最小化字符串的长度是 3 。
```

**示例 2：**

```
输入：s = "cbbd"
输出：3
解释：我们可以选择位于下标 1 处的字符 'b' 开始。下标 1 左侧不存在字符 'b' ，但右侧存在一个字符 'b'（位于下标 2），所以会删除位于下标 2 的字符 'b' 。执行操作后，字符串变为 "cbd" 。继续对字符串执行任何操作都不会改变其长度。因此，最小化字符串的长度是 3 。
```

**示例 3：**

```
输入：s = "dddaaa"
输出：2
解释：我们可以选择位于下标 1 处的字符 'd' 开始。接着删除下标 1 左侧最近的那个 'd'（位于下标 0）以及下标 1 右侧最近的那个 'd'（位于下标 2）。执行操作后，字符串变为 "daaa" 。继续对新字符串执行操作，可以选择位于下标 2 的字符 'a' 。接着删除下标 2 左侧最近的那个 'a'（位于下标 1）以及下标 2 右侧最近的那个 'a'（位于下标 3）。执行操作后，字符串变为 "da" 。继续对字符串执行任何操作都不会改变其长度。因此，最小化字符串的长度是 2 。
```

 

**提示：**

- `1 <= s.length <= 100`
- `s` 仅由小写英文字母组成



```python
class Solution:
    def minimizedStringLength(self, s: str) -> int:
        n = len(s)
        s = list(s)
        for i in range(n):
            if s[i] == 'D':
                continue

            for j in range(i - 1, -1, -1):
                if s[j] == s[i]:
                    s[j] = 'D'
                    break

            for j in range(i + 1, n):
                if s[j] == s[i]:
                    s[j] = 'D'
                    break

        ans = 0
        for i in range(n):
            if s[i] == 'D':
                ans += 1

        return n - ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimizedStringLength("aaabc"))  # 3

```



```python
class Solution:
    def minimizedStringLength(self, s: str) -> int:
        # 使用集合记录唯一字符
        unique_chars = set(s)
        return len(unique_chars)

if __name__ == "__main__":
    sol = Solution()
    print(sol.minimizedStringLength("aaabc"))  # 输出：3
```



## E2784.检查数组是否是好的

sorting, hash table, https://leetcode.cn/problems/check-if-array-is-good/

给你一个整数数组 `nums` ，如果它是数组 `base[n]` 的一个排列，我们称它是个 **好** 数组。

`base[n] = [1, 2, ..., n - 1, n, n]` （换句话说，它是一个长度为 `n + 1` 且包含 `1` 到 `n - 1` 恰好各一次，包含 `n` 两次的一个数组）。比方说，`base[1] = [1, 1]` ，`base[3] = [1, 2, 3, 3]` 。

如果数组是一个好数组，请你返回 `true` ，否则返回 `false` 。

**注意：**数组的排列是这些数字按任意顺序排布后重新得到的数组。

 

**示例 1：**

```
输入：nums = [2, 1, 3]
输出：false
解释：因为数组的最大元素是 3 ，唯一可以构成这个数组的 base[n] 对应的 n = 3 。但是 base[3] 有 4 个元素，但数组 nums 只有 3 个元素，所以无法得到 base[3] = [1, 2, 3, 3] 的排列，所以答案为 false 。
```

**示例 2：**

```
输入：nums = [1, 3, 3, 2]
输出：true
解释：因为数组的最大元素是 3 ，唯一可以构成这个数组的 base[n] 对应的 n = 3 ，可以看出数组是 base[3] = [1, 2, 3, 3] 的一个排列（交换 nums 中第二个和第四个元素）。所以答案为 true 。
```

**示例 3：**

```
输入：nums = [1, 1]
输出：true
解释：因为数组的最大元素是 1 ，唯一可以构成这个数组的 base[n] 对应的 n = 1，可以看出数组是 base[1] = [1, 1] 的一个排列。所以答案为 true 。
```

**示例 4：**

```
输入：nums = [3, 4, 4, 1, 2, 1]
输出：false
解释：因为数组的最大元素是 4 ，唯一可以构成这个数组的 base[n] 对应的 n = 4 。但是 base[n] 有 5 个元素而 nums 有 6 个元素。所以答案为 false 。
```

 

**提示：**

- `1 <= nums.length <= 100`
- `1 <= num[i] <= 200`



这个问题要求我们判断一个数组是否是 `base[n]` 的一个排列。
`base[n]` 的定义是：长度为 `n + 1`，包含 `1` 到 `n - 1` 各一次，且包含 `n` 两次。

**解题思路**

1.  **确定 $n$ 的值**：
    由于 `base[n]` 的长度必须是 `n + 1`，那么对于给定的数组 `nums`，如果它是好数组，其对应的 $n$ 必须等于 `len(nums) - 1`。
2.  **特殊情况处理**：
    如果数组长度小于 2（即 `len(nums) < 2`），则无法构成最小的 `base[1] = [1, 1]`，直接返回 `False`。
3.  **验证元素组成**：
    *   我们可以先对 `nums` 进行**排序**。
    *   排序后的数组应该满足：
        *   前 `n - 1` 个元素依次是 `1, 2, 3, ..., n-1`。
        *   最后两个元素都应该是 `n`。
4.  **复杂度分析**：
    *   时间复杂度：$O(L \log L)$，其中 $L$ 是数组的长度，主要消耗在排序上。由于题目给出 $L \le 100$，这个复杂度非常理想。
    *   空间复杂度：$O(1)$ 或 $O(L)$，取决于排序算法的实现和是否创建辅助数组。

**代码实现**

```python
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # 1. 确定 n 的值
        n = len(nums) - 1
        
        # 最小的好数组是 base[1] = [1, 1]，长度为 2
        if n < 1:
            return False
        
        # 2. 对数组进行排序
        nums.sort()
        
        # 3. 检查前 n-1 个元素是否为 1 到 n-1
        for i in range(n - 1):
            if nums[i] != i + 1:
                return False
        
        # 4. 检查最后两个元素是否都等于 n
        return nums[n - 1] == n and nums[n] == n

```



**计数法（Hash Map / Array）**

也可以统计每个数字出现的频率：

1. 计算 $n = len(nums) - 1$。
2. 遍历 `nums`，统计 1 到 $n$ 每个数字出现的次数。
3. 检查：
   *   $1$ 到 $n-1$ 的频率是否都为 1。
   *   $n$ 的频率是否为 2。
   *   是否存在大于 $n$ 的数字。

```python
from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        if n < 1: return False
        
        counts = Counter(nums)
        
        # 检查 1 到 n-1 出现次数
        for i in range(1, n):
            if counts[i] != 1:
                return False
        
        # 检查 n 出现次数
        return counts[n] == 2
```

这种计数法的时间复杂度为 $O(L)$，在数组长度较大时比排序法更快，但在本题约束下两者表现相近。





## M2833.距离原点最远的点

implementation, https://leetcode.cn/problems/furthest-point-from-origin/

给你一个长度为 `n` 的字符串 `moves` ，该字符串仅由字符 `'L'`、`'R'` 和 `'_'` 组成。字符串表示你在一条原点为 `0` 的数轴上的若干次移动。

你的初始位置就在原点（`0`），第 `i` 次移动过程中，你可以根据对应字符选择移动方向：

- 如果 `moves[i] = 'L'` 或 `moves[i] = '_'` ，可以选择向左移动一个单位距离
- 如果 `moves[i] = 'R'` 或 `moves[i] = '_'` ，可以选择向右移动一个单位距离

移动 `n` 次之后，请你找出可以到达的距离原点 **最远** 的点，并返回 **从原点到这一点的距离** 。

 

**示例 1：**

```
输入：moves = "L_RL__R"
输出：3
解释：可以到达的距离原点 0 最远的点是 -3 ，移动的序列为 "LLRLLLR" 。
```

**示例 2：**

```
输入：moves = "_R__LL_"
输出：5
解释：可以到达的距离原点 0 最远的点是 -5 ，移动的序列为 "LRLLLLL" 。
```

**示例 3：**

```
输入：moves = "_______"
输出：7
解释：可以到达的距离原点 0 最远的点是 7 ，移动的序列为 "RRRRRRR" 。
```

 

**提示：**

- `1 <= moves.length == n <= 50`
- `moves` 仅由字符 `'L'`、`'R'` 和 `'_'` 组成



**解题思路**

1.  **统计次数**：
    *   统计字符串中 `'L'` 的数量。
    *   统计字符串中 `'R'` 的数量。
    *   统计字符串中 `'_'` 的数量。
2.  **核心逻辑**：
    *   所有的 `'L'` 都会让你向左走（-1），所有的 `'R'` 都会让你向右走（+1）。
    *   那么 `'L'` 和 `'R'` 抵消后的净位移是 `count('R') - count('L')`。
    *   关键在于 `'_'`：它既可以当成 `'L'` 也可以当成 `'R'`。为了让距离原点最远，我们应该让所有的 `'_'` 都朝着**当前偏移方向**（或者离原点更远的方向）移动。
    *   因此，最大距离就是：**`'L'` 和 `'R'` 的净位移的绝对值** 加上 **所有的 `'_'` 的数量**。

**代码实现**

```python
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # 统计 L, R 和 _ 的数量
        count_L = moves.count('L')
        count_R = moves.count('R')
        count_underscore = moves.count('_')
        
        # 最大距离等于 L 和 R 抵消后的绝对值，加上所有的下划线（下划线全部填向同一个方向）
        return abs(count_R - count_L) + count_underscore
```

**复杂度分析**

*   **时间复杂度**：$O(n)$。其中 $n$ 是字符串 `moves` 的长度。我们需要遍历字符串来统计字符个数（在 Python 中 `count` 方法会各遍历一次，总共三次，依然是线性的）。
*   **空间复杂度**：$O(1)$。除了存储计数器的变量外，没有使用额外的空间。



## E2839.判断通过操作能否让字符串相等 I

string, https://leetcode.cn/problems/check-if-strings-can-be-made-equal-with-operations-i/

给你两个字符串 `s1` 和 `s2` ，两个字符串的长度都为 `4` ，且只包含 **小写** 英文字母。

你可以对两个字符串中的 **任意一个** 执行以下操作 **任意** 次：

- 选择两个下标 `i` 和 `j` 且满足 `j - i = 2` ，然后 **交换** 这个字符串中两个下标对应的字符。

如果你可以让字符串 `s1` 和 `s2` 相等，那么返回 `true` ，否则返回 `false` 。

 

**示例 1：**

```
输入：s1 = "abcd", s2 = "cdab"
输出：true
解释： 我们可以对 s1 执行以下操作：
- 选择下标 i = 0 ，j = 2 ，得到字符串 s1 = "cbad" 。
- 选择下标 i = 1 ，j = 3 ，得到字符串 s1 = "cdab" = s2 。
```

**示例 2：**

```
输入：s1 = "abcd", s2 = "dacb"
输出：false
解释：无法让两个字符串相等。
```

 

**提示：**

- `s1.length == s2.length == 4`
- `s1` 和 `s2` 只包含小写英文字母。



这个问题可以通过观察交换规则来解决。

**解题思路**

1.  **观察交换规则**：
    操作允许交换下标 $i$ 和 $j$，满足 $j - i = 2$。对于长度为 4 的字符串（下标为 0, 1, 2, 3），这意味着：
    *   下标 **0** 的字符只能和下标 **2** 的字符交换。
    *   下标 **1** 的字符只能和下标 **3** 的字符交换。
    *   偶数下标位置的字符永远不会移动到奇数下标位置，反之亦然。

2.  **成立条件**：
    两个字符串 `s1` 和 `s2` 可以相等，当且仅当：
    *   `s1` 中所有**偶数下标**位置的字符集合（即 `s1[0]` 和 `s1[2]`）与 `s2` 中相应位置的字符集合一致。
    *   `s1` 中所有**奇数下标**位置的字符集合（即 `s1[1]` 和 `s1[3]`）与 `s2` 中相应位置的字符集合一致。

3.  **具体实现**：
    *   比较 `{s1[0], s1[2]}` 是否等于 `{s2[0], s2[2]}`。
    *   比较 `{s1[1], s1[3]}` 是否等于 `{s2[1], s2[3]}`。
    *   在 Python 中，由于只有两个字符，我们可以直接手动枚举两种可能，或者对这两个字符进行排序后比较。

    **代码实现**

```python
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # 检查偶数下标位置 (0, 2) 的字符是否匹配
        # 两种情况：直接相等，或者交换后相等
        even_match = (sorted([s1[0], s1[2]]) == sorted([s2[0], s2[2]]))
        
        # 检查奇数下标位置 (1, 3) 的字符是否匹配
        odd_match = (sorted([s1[1], s1[3]]) == sorted([s2[1], s2[3]]))
        
        return even_match and odd_match
```

**复杂度分析**

*   **时间复杂度**：$O(1)$。因为字符串长度固定为 4，排序和比较的操作都是常数级别的。
*   **空间复杂度**：$O(1)$。只使用了少量的辅助空间。

**另一种写法（直接比较）**

如果你不想使用 `sorted`，也可以利用逻辑判断：

```python
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # 检查偶数位
        cond1 = (s1[0] == s2[0] and s1[2] == s2[2]) or (s1[0] == s2[2] and s1[2] == s2[0])
        # 检查奇数位
        cond2 = (s1[1] == s2[1] and s1[3] == s2[3]) or (s1[1] == s2[3] and s1[3] == s2[1])
        
        return cond1 and cond2
```





## 2843.统计对称整数的数目

enumeration, https://leetcode.cn/problems/count-symmetric-integers/

给你两个正整数 `low` 和 `high` 。

对于一个由 `2 * n` 位数字组成的整数 `x` ，如果其前 `n` 位数字之和与后 `n` 位数字之和相等，则认为这个数字是一个对称整数。

返回在 `[low, high]` 范围内的 **对称整数的数目** 。

 

**示例 1：**

```
输入：low = 1, high = 100
输出：9
解释：在 1 到 100 范围内共有 9 个对称整数：11、22、33、44、55、66、77、88 和 99 。
```

**示例 2：**

```
输入：low = 1200, high = 1230
输出：4
解释：在 1200 到 1230 范围内共有 4 个对称整数：1203、1212、1221 和 1230 。
```

 

**提示：**

- `1 <= low <= high <= 10^4`



```python
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt = 0
        for num in range(low, high + 1):
            s = [int(i) for i in str(num)]
            if len(s) & 1:
                continue
            mid = len(s) // 2
            if sum(s[:mid]) == sum(s[mid:]):
                cnt += 1
        return cnt
```





## 2873.有序三元组中的最大值I

https://leetcode.cn/problems/maximum-value-of-an-ordered-triplet-i/

给你一个下标从 **0** 开始的整数数组 `nums` 。

请你从所有满足 `i < j < k` 的下标三元组 `(i, j, k)` 中，找出并返回下标三元组的最大值。如果所有满足条件的三元组的值都是负数，则返回 `0` 。

**下标三元组** `(i, j, k)` 的值等于 `(nums[i] - nums[j]) * nums[k]` 。

 

**示例 1：**

```
输入：nums = [12,6,1,2,7]
输出：77
解释：下标三元组 (0, 2, 4) 的值是 (nums[0] - nums[2]) * nums[4] = 77 。
可以证明不存在值大于 77 的有序下标三元组。
```

**示例 2：**

```
输入：nums = [1,10,3,4,19]
输出：133
解释：下标三元组 (1, 2, 4) 的值是 (nums[1] - nums[2]) * nums[4] = 133 。
可以证明不存在值大于 133 的有序下标三元组。 
```

**示例 3：**

```
输入：nums = [1,2,3]
输出：0
解释：唯一的下标三元组 (0, 1, 2) 的值是一个负数，(nums[0] - nums[1]) * nums[2] = -3 。因此，答案是 0 。
```

 

**提示：**

- `3 <= nums.length <= 100`
- `1 <= nums[i] <= 10^6`



```python
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_v = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    max_v = max(max_v, (nums[i]-nums[j])*nums[k])
        return max_v
```



## E2894. 分类求和并作差	

https://leetcode.cn/problems/divisible-and-non-divisible-sums-difference/

给你两个正整数 `n` 和 `m` 。

现定义两个整数 `num1` 和 `num2` ，如下所示：

- `num1`：范围 `[1, n]` 内所有 **无法被** `m` **整除** 的整数之和。
- `num2`：范围 `[1, n]` 内所有 **能够被** `m` **整除** 的整数之和。

返回整数 `num1 - num2` 。

 

**示例 1：**

```
输入：n = 10, m = 3
输出：19
解释：在这个示例中：
- 范围 [1, 10] 内无法被 3 整除的整数为 [1,2,4,5,7,8,10] ，num1 = 这些整数之和 = 37 。
- 范围 [1, 10] 内能够被 3 整除的整数为 [3,6,9] ，num2 = 这些整数之和 = 18 。
返回 37 - 18 = 19 作为答案。
```

**示例 2：**

```
输入：n = 5, m = 6
输出：15
解释：在这个示例中：
- 范围 [1, 5] 内无法被 6 整除的整数为 [1,2,3,4,5] ，num1 = 这些整数之和 =  15 。
- 范围 [1, 5] 内能够被 6 整除的整数为 [] ，num2 = 这些整数之和 = 0 。
返回 15 - 0 = 15 作为答案。
```

**示例 3：**

```
输入：n = 5, m = 1
输出：-15
解释：在这个示例中：
- 范围 [1, 5] 内无法被 1 整除的整数为 [] ，num1 = 这些整数之和 = 0 。 
- 范围 [1, 5] 内能够被 1 整除的整数为 [1,2,3,4,5] ，num2 = 这些整数之和 = 15 。
返回 0 - 15 = -15 作为答案。
```

 

**提示：**

- `1 <= n, m <= 1000`



```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
        
        for i in range(1, n + 1):
            if i % m == 0:
                num2 += i
            else:
                num1 += i
                
        return num1 - num2

        
```



## E2900.最长相邻不相等子序列 I

greedy, https://leetcode.cn/problems/longest-unequal-adjacent-groups-subsequence-i/

给你一个下标从 **0** 开始的字符串数组 `words` ，和一个下标从 **0** 开始的 **二进制** 数组 `groups` ，两个数组长度都是 `n` 。

你需要从 `words` 中选出 **最长子序列**。如果对于序列中的任何两个连续串，二进制数组 `groups` 中它们的对应元素不同，则 `words` 的子序列是不同的。

正式来说，你需要从下标 `[0, 1, ..., n - 1]` 中选出一个 **最长子序列** ，将这个子序列记作长度为 `k`的 `[i0, i1, ..., ik - 1]` ，对于所有满足 `0 <= j < k - 1` 的 `j` 都有 `groups[ij] != groups[ij + 1]` 。

请你返回一个字符串数组，它是下标子序列 **依次** 对应 `words` 数组中的字符串连接形成的字符串数组。如果有多个答案，返回 **任意** 一个。

**注意：**`words` 中的元素是不同的 。

 

**示例 1：**

```
输入：words = ["e","a","b"], groups = [0,0,1]
输出：["e","b"]
解释：一个可行的子序列是 [0,2] ，因为 groups[0] != groups[2] 。
所以一个可行的答案是 [words[0],words[2]] = ["e","b"] 。
另一个可行的子序列是 [1,2] ，因为 groups[1] != groups[2] 。
得到答案为 [words[1],words[2]] = ["a","b"] 。
这也是一个可行的答案。
符合题意的最长子序列的长度为 2 。
```

**示例 2：**

```
输入：words = ["a","b","c","d"], groups = [1,0,1,1]
输出：["a","b","c"]
解释：一个可行的子序列为 [0,1,2] 因为 groups[0] != groups[1] 且 groups[1] != groups[2] 。
所以一个可行的答案是 [words[0],words[1],words[2]] = ["a","b","c"] 。
另一个可行的子序列为 [0,1,3] 因为 groups[0] != groups[1] 且 groups[1] != groups[3] 。
得到答案为 [words[0],words[1],words[3]] = ["a","b","d"] 。
这也是一个可行的答案。
符合题意的最长子序列的长度为 3 。
```

 

**提示：**

- `1 <= n == words.length == groups.length <= 100`
- `1 <= words[i].length <= 10`
- `groups[i]` 是 `0` 或 `1`。

- `words` 中的字符串 **互不相同** 。
- `words[i]` 只包含小写英文字母。



**解法思路：贪心策略（简单且高效）**

可以用贪心的方式遍历整个数组一次：

1. 初始选择第一个元素；
2. 后续每次选择与当前最后一个元素在 `groups` 中不同的项；
3. 直到遍历完整个数组。

因为只要相邻不同即可，而且我们每次都选能继续满足条件的下一个元素，这样可以确保构造出一个合法的最长子序列。

---

Python 实现如下：

```python
from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = [words[0]]      # 初始加入第一个单词
        prev_group = groups[0]  # 记录上一个选中的 group 值

        for i in range(1, len(groups)):
            if groups[i] != prev_group:
                res.append(words[i])
                prev_group = groups[i]
        
        return res
```

时间复杂度分析：

- 时间复杂度：O(n)
- 空间复杂度：O(n)（用于保存结果）



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



## E2946.循环移位后的矩阵相似检查

matrix, https://leetcode.cn/problems/matrix-similarity-after-cyclic-shifts/

给你一个**下标从 0 开始**且大小为 `m x n` 的整数矩阵 `mat` 和一个整数 `k` 。请你将矩阵中的 **奇数** 行循环 **右** 移 `k` 次，**偶数** 行循环 **左** 移 `k` 次。

如果初始矩阵和最终矩阵完全相同，则返回 `true` ，否则返回 `false` 。

 

**示例 1：**

```
输入：mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2
输出：true
解释：


初始矩阵如图一所示。
图二表示对奇数行右移一次且对偶数行左移一次后的矩阵状态。
图三是经过两次循环移位后的最终矩阵状态，与初始矩阵相同。
因此，返回 true 。
```

**示例 2：**

```
输入：mat = [[2,2],[2,2]], k = 3
输出：true
解释：由于矩阵中的所有值都相等，即使进行循环移位，矩阵仍然保持不变。因此，返回 true 。
```

**示例 3：**

```
输入：mat = [[1,2]], k = 1
输出：false
解释：循环移位一次后，mat = [[2,1]]，与初始矩阵不相等。因此，返回 false 。
```

 

**提示：**

- `1 <= mat.length <= 25`
- `1 <= mat[i].length <= 25`
- `1 <= mat[i][j] <= 25`
- `1 <= k <= 50`



这个问题可以通过观察**循环移位的性质**来简化。

**核心思路**

1.  **循环移位的等价性**：
    对于一个长度为 $n$ 的序列，将其循环左移 $k$ 次或循环右移 $k$ 次后，如果要求与原序列完全相同，其本质条件是相同的：**序列必须具有周期性**。
    *   如果向左移 $k$ 位：原位置 $j$ 的元素会移动到 $(j - k) \pmod n$，或者说新位置 $j$ 的元素来源于原位置 $(j + k) \pmod n$。
    *   如果向右移 $k$ 位：原位置 $j$ 的元素会移动到 $(j + k) \pmod n$。

2.  **判断条件**：
    无论奇数行右移还是偶数行左移，矩阵保持不变的充要条件是：对于矩阵中的每一行 `mat[i]`，其中的每个元素 `mat[i][j]` 都必须等于它移动 $k$ 个位置后指向的元素。
    即：`mat[i][j] == mat[i][(j + k) % n]`。
    *注：这里的 $n$ 是列数。由于 $k$ 可能大于 $n$，我们可以先取模 `k %= n`，如果不取模直接使用 `(j + k) % n` 结果也是正确的。*

    **代码实现**

```python
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        
        # 预处理 k，因为移动 n 次等于没移
        k %= n
        if k == 0:
            return True
        
        for i in range(m):
            for j in range(n):
                # 检查当前元素与循环移动 k 位后的元素是否相等
                # 无论左移还是右移，只要满足 mat[i][j] == mat[i][(j + k) % n]，
                # 该行在循环移动 k 次后就会保持不变。
                if mat[i][j] != mat[i][(j + k) % n]:
                    return False
        
        return True
```

**复杂度分析**

*   **时间复杂度**：$O(m \times n)$。我们需要遍历矩阵中的每一个元素一次。
*   **空间复杂度**：$O(1)$。只使用了常数级别的额外空间。

**为什么不需要区分左右移？**

*   **偶数行（左移）**：要求 `mat[i][j]` 移动后回到原位，即 `mat[i][j]` 应该等于移动前在 `(j + k) % n` 位置的数。
*   **奇数行（右移）**：要求 `mat[i][j]` 移动后回到原位，即 `mat[i][j]` 应该等于移动前在 `(j - k) % n` 位置的数。
*   实际上，如果一个数组满足 `row[j] == row[(j + k) % n]`，那么它同时也必然满足 `row[j] == row[(j - k) % n]`（这只是索引的对称性）。因此，统一使用 `(j + k) % n` 进行检查即可涵盖两种情况。





## M3010.将数组分成最小总代价的子数组 I

sorting, https://leetcode.cn/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

给你一个长度为 `n` 的整数数组 `nums` 。

一个数组的 **代价** 是它的 **第一个** 元素。比方说，`[1,2,3]` 的代价是 `1` ，`[3,4,1]` 的代价是 `3` 。

你需要将 `nums` 分成 `3` 个 **连续且没有交集** 的子数组。

请你返回这些子数组的 **最小** 代价 **总和** 。

 

**示例 1：**

```
输入：nums = [1,2,3,12]
输出：6
解释：最佳分割成 3 个子数组的方案是：[1] ，[2] 和 [3,12] ，总代价为 1 + 2 + 3 = 6 。
其他得到 3 个子数组的方案是：
- [1] ，[2,3] 和 [12] ，总代价是 1 + 2 + 12 = 15 。
- [1,2] ，[3] 和 [12] ，总代价是 1 + 3 + 12 = 16 。
```

**示例 2：**

```
输入：nums = [5,4,3]
输出：12
解释：最佳分割成 3 个子数组的方案是：[5] ，[4] 和 [3] ，总代价为 5 + 4 + 3 = 12 。
12 是所有分割方案里的最小总代价。
```

**示例 3：**

```
输入：nums = [10,3,1,1]
输出：12
解释：最佳分割成 3 个子数组的方案是：[10,3] ，[1] 和 [1] ，总代价为 10 + 1 + 1 = 12 。
12 是所有分割方案里的最小总代价。
```

 

**提示：**

- `3 <= n <= 50`
- `1 <= nums[i] <= 50`



```python
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans = nums[0]
        new = nums[1:]
        new.sort()
        ans += new[0] + new[1]

        return ans
```



## E3014.输入单词需要的最少按键次数 I

greedy, https://leetcode.cn/problems/minimum-number-of-pushes-to-type-word-i/

给你一个字符串 `word`，由 **不同** 小写英文字母组成。

电话键盘上的按键与 **不同** 小写英文字母集合相映射，可以通过按压按键来组成单词。例如，按键 `2` 对应 `["a","b","c"]`，我们需要按一次键来输入 `"a"`，按两次键来输入 `"b"`，按三次键来输入 `"c"`*。*

现在允许你将编号为 `2` 到 `9` 的按键重新映射到 **不同** 字母集合。每个按键可以映射到 **任意数量** 的字母，但每个字母 **必须** **恰好** 映射到 **一个** 按键上。你需要找到输入字符串 `word` 所需的 **最少** 按键次数。

返回重新映射按键后输入 `word` 所需的 **最少** 按键次数。

下面给出了一种电话键盘上字母到按键的映射作为示例。注意 `1`，`*`，`#` 和 `0` **不** 对应任何字母。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/keypaddesc.png" alt="img" style="zoom:67%;" />

 

**示例 1：**

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/keypadv1e1.png" alt="img" style="zoom:67%;" />

```
输入：word = "abcde"
输出：5
解释：图片中给出的重新映射方案的输入成本最小。
"a" -> 在按键 2 上按一次
"b" -> 在按键 3 上按一次
"c" -> 在按键 4 上按一次
"d" -> 在按键 5 上按一次
"e" -> 在按键 6 上按一次
总成本为 1 + 1 + 1 + 1 + 1 = 5 。
可以证明不存在其他成本更低的映射方案。
```

**示例 2：**

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/keypadv1e2.png" alt="img" style="zoom:67%;" />

```
输入：word = "xycdefghij"
输出：12
解释：图片中给出的重新映射方案的输入成本最小。
"x" -> 在按键 2 上按一次
"y" -> 在按键 2 上按两次
"c" -> 在按键 3 上按一次
"d" -> 在按键 3 上按两次
"e" -> 在按键 4 上按一次
"f" -> 在按键 5 上按一次
"g" -> 在按键 6 上按一次
"h" -> 在按键 7 上按一次
"i" -> 在按键 8 上按一次
"j" -> 在按键 9 上按一次
总成本为 1 + 2 + 1 + 2 + 1 + 1 + 1 + 1 + 1 + 1 = 12 。
可以证明不存在其他成本更低的映射方案。
```

 

**提示：**

- `1 <= word.length <= 26`
- `word` 仅由小写英文字母组成。
- `word` 中的所有字母互不相同。



这道题可以通过**贪心策略**来求解。

**解题思路**

1. **分析题目**：
   - 题目保证字符串 `word` 中的所有字母**互不相同**（每个字母出现频率均为 1）。
   - 共有 **8 个** 可用按键（编号 2 到 9）。
   - 每个按键可以分配多个字母：
     - 排在按键第 1 位置的字母，需要按 **1** 次；
     - 排在按键第 2 位置的字母，需要按 **2** 次；
     - 排在按键第 3 位置的字母，需要按 **3** 次；
     - 排在按键第 4 位置的字母，需要按 **4** 次。

2. **贪心选择**：
   - 为了使总按键次数最少，我们应当优先把字母分配到 8 个按键的**第 1 位置**。
   - 如果字母数量超过 8 个，多出来的字母再分配到 8 个按键的**第 2 位置**，以此类推。

3. **规律推导**：
   - 对于第 $i$ 个字母（下标从 $0$ 开始，范围为 $0 \le i < \text{len}(word)$）：
     - 第 $0 \sim 7$ 个字母（前 8 个）：需要按 `1` 次，即 `0 // 8 + 1 = 1`；
     - 第 $8 \sim 15$ 个字母（中 8 个）：需要按 `2` 次，即 `8 // 8 + 1 = 2`；
     - 第 $16 \sim 23$ 个字母：需要按 `3` 次，即 `16 // 8 + 1 = 3`；
     - 第 $24 \sim 25$ 个字母：需要按 `4` 次，即 `24 // 8 + 1 = 4`。
   - 因此，第 $i$ 个字母所需的按键次数为：`(i // 8) + 1`。

---

**Python 代码实现**

```python
class Solution:
    def minimumPushes(self, word: str) -> int:
        # 对于第 i 个字符，其按键次数为 (i // 8) + 1
        return sum((i // 8) + 1 for i in range(len(word)))
```

---

**复杂度分析**

- **时间复杂度**：$\mathcal{O}(n)$，其中 $n$ 为字符串 `word` 的长度。因为 $n \le 26$，所以实际运行时间为常数级别 $\mathcal{O}(1)$。
- **空间复杂度**：$\mathcal{O}(1)$，仅使用了常数空间的变量。





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



## E3024.三角形类型

https://leetcode.cn/problems/type-of-triangle/

给你一个下标从 **0** 开始长度为 `3` 的整数数组 `nums` ，需要用它们来构造三角形。

- 如果一个三角形的所有边长度相等，那么这个三角形称为 **equilateral** 。
- 如果一个三角形恰好有两条边长度相等，那么这个三角形称为 **isosceles** 。
- 如果一个三角形三条边的长度互不相同，那么这个三角形称为 **scalene** 。

如果这个数组无法构成一个三角形，请你返回字符串 `"none"` ，否则返回一个字符串表示这个三角形的类型。

 

**示例 1：**

```
输入：nums = [3,3,3]
输出："equilateral"
解释：由于三条边长度相等，所以可以构成一个等边三角形，返回 "equilateral" 。
```

**示例 2：**

```
输入：nums = [3,4,5]
输出："scalene"
解释：
nums[0] + nums[1] = 3 + 4 = 7 ，大于 nums[2] = 5 。
nums[0] + nums[2] = 3 + 5 = 8 ，大于 nums[1] = 4 。
nums[1] + nums[2] = 4 + 5 = 9 ，大于 nums[0] = 3 。
由于任意两边之和都大于第三边，所以可以构成一个三角形，因为三条边的长度互不相等，所以返回 "scalene"。
```

**提示：**

- `nums.length == 3`
- `1 <= nums[i] <= 100`



```python
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        a,b,c = nums[0],nums[1],nums[2]
        if a + b <= c:
            return "none"

        if a == b == c:
            return "equilateral"
        if a == b or b == c:
            return "isosceles"
        
        if a !=b and b != c:
            return "scalene"
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



## 3110.字符串的分数

https://leetcode.cn/problems/score-of-a-string/

给你一个字符串 `s` 。一个字符串的 **分数** 定义为相邻字符 **ASCII** 码差值绝对值的和。

请你返回 `s` 的 **分数** 。

 

**示例 1：**

**输入：**s = "hello"

**输出：**13

**解释：**

`s` 中字符的 **ASCII** 码分别为：`'h' = 104` ，`'e' = 101` ，`'l' = 108` ，`'o' = 111` 。所以 `s` 的分数为 `|104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13` 。

**示例 2：**

**输入：**s = "zaz"

**输出：**50

**解释：**

`s` 中字符的 **ASCII** 码分别为：`'z' = 122` ，`'a' = 97` 。所以 `s` 的分数为 `|122 - 97| + |97 - 122| = 25 + 25 = 50` 。

 

**提示：**

- `2 <= s.length <= 100`
- `s` 只包含小写英文字母。



```python
class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        s_zip = zip(s[0:n-1], s[1:n])
        return sum(abs(ord(_[0]) - ord(_[1])) for _ in s_zip)
```



## E3120.统计特殊字母的数量 I

hash table, https://leetcode.cn/problems/count-the-number-of-special-characters-i/

给你一个字符串 `word`。如果 `word` 中同时存在某个字母的小写形式和大写形式，则称这个字母为 **特殊字母** 。

返回 `word` 中 **特殊字母** 的数量。

**示例 1:**

**输入：**word = "aaAbcBC"

**输出：**3

**解释：**

`word` 中的特殊字母是 `'a'`、`'b'` 和 `'c'`。

**示例 2:**

**输入：**word = "abc"

**输出：**0

**解释：**

`word` 中不存在大小写形式同时出现的字母。

**示例 3:**

**输入：**word = "abBCab"

**输出：**1

**解释：**

`word` 中唯一的特殊字母是 `'b'`。

 

**提示：**

- `1 <= word.length <= 50`
- `word` 仅由小写和大写英文字母组成。



这个问题可以通过集合（Set）来高效解决。

**解题思路**

我们可以将问题拆解为：找出所有在字符串中出现过的小写字母，以及所有在字符串中出现过的大写字母（并将其转换为小写），然后求两者的交集。交集的大小即为“特殊字母”的数量。

具体步骤如下：

1. 找出 `word` 中所有的小写字母，存入集合 `lowers`。
2. 找出 `word` 中所有的大写字母，转换为小写后存入集合 `uppers`。
3. 计算 `lowers` 和 `uppers` 的交集大小。

**Python 代码实现**

```python
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # 收集所有出现过的小写字母
        lowers = {c for c in word if c.islower()}
        # 收集所有出现过的大写字母，并转换为小写
        uppers = {c.lower() for c in word if c.isupper()}
        
        # 返回交集的长度
        return len(lowers & uppers)
```

**复杂度分析**

- **时间复杂度**：$O(N)$，其中 $N$ 是字符串 `word` 的长度。我们需要遍历一次字符串来构建两个集合，集合求交集的操作时间复杂度取决于字符集的大小（最多为 26 个字母），因此也是常数级别的。
- **空间复杂度**：$O(1)$ 或 $O(\Sigma)$，其中 $\Sigma$ 是字符集的大小（这里最多为 26 个英文字母）。因为存储的字符数量不会超过英文字母的数量，所以占用常数级别的额外空间。



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



## E3300.替换为数位和以后的最小元素

math, https://leetcode.cn/problems/minimum-element-after-replacement-with-digit-sum/

给你一个整数数组 `nums` 。

请你将 `nums` 中每一个元素都替换为它的各个数位之 **和** 。

请你返回替换所有元素以后 `nums` 中的 **最小** 元素。

 

**示例 1：**

**输入：**nums = [10,12,13,14]

**输出：**1

**解释：**

`nums` 替换后变为 `[1, 3, 4, 5]` ，最小元素为 1 。

**示例 2：**

**输入：**nums = [1,2,3,4]

**输出：**1

**解释：**

`nums` 替换后变为 `[1, 2, 3, 4]` ，最小元素为 1 。

**示例 3：**

**输入：**nums = [999,19,199]

**输出：**10

**解释：**

`nums` 替换后变为 `[27, 10, 19]` ，最小元素为 10 。

 

**提示：**

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 10^4`



这道题的要求是计算数组 `nums` 中每个元素的数位之和，并返回这些和之中的最小值。

**解题思路**

我们可以遍历数组中的每一个整数，计算它的数位之和。为了求得数位和，可以将整数转换成字符串，然后将每一位字符转换回整数并求和；或者通过循环对 10 取余和整除来计算。由于数据范围较小（每个数最大为 $10^4$），两种方式的效率都很高。

在遍历过程中，维护一个最小值，最终返回该最小值。

```python
from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        def get_digit_sum(n: int) -> int:
            # 计算一个整数的数位之和
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s
        
        # 计算所有元素的数位之和并求出最小值
        return min(get_digit_sum(num) for num in nums)
```

复杂度分析

- **时间复杂度**：$O(N \log_{10} M)$，其中 $N$ 是数组 `nums` 的长度，$M$ 是数组中的最大数值。因为 $nums[i] \le 10^4$，所以对每个数求数位和最多需要执行 5 次循环，整体时间复杂度非常低，接近 $O(N)$。
- **空间复杂度**：$O(1)$，只需要常数级别的额外空间来存储临时变量和最小值。





## E3314.构造最小位运算数组 I

https://leetcode.cn/problems/construct-the-minimum-bitwise-array-i/

给你一个长度为 `n` 的质数数组 `nums` 。你的任务是返回一个长度为 `n` 的数组 `ans` ，对于每个下标 `i` ，以下 **条件** 均成立：

- `ans[i] OR (ans[i] + 1) == nums[i]`

除此以外，你需要 **最小化** 结果数组里每一个 `ans[i]` 。

如果没法找到符合 **条件** 的 `ans[i]` ，那么 `ans[i] = -1` 。

**质数** 指的是一个大于 1 的自然数，且它只有 1 和自己两个因数。

 

**示例 1：**

**输入：**nums = [2,3,5,7]

**输出：**[-1,1,4,3]

**解释：**

- 对于 `i = 0` ，不存在 `ans[0]` 满足 `ans[0] OR (ans[0] + 1) = 2` ，所以 `ans[0] = -1` 。
- 对于 `i = 1` ，满足 `ans[1] OR (ans[1] + 1) = 3` 的最小 `ans[1]` 为 `1` ，因为 `1 OR (1 + 1) = 3` 。
- 对于 `i = 2` ，满足 `ans[2] OR (ans[2] + 1) = 5` 的最小 `ans[2]` 为 `4` ，因为 `4 OR (4 + 1) = 5` 。
- 对于 `i = 3` ，满足 `ans[3] OR (ans[3] + 1) = 7` 的最小 `ans[3]` 为 `3` ，因为 `3 OR (3 + 1) = 7` 。

**示例 2：**

**输入：**nums = [11,13,31]

**输出：**[9,12,15]

**解释：**

- 对于 `i = 0` ，满足 `ans[0] OR (ans[0] + 1) = 11` 的最小 `ans[0]` 为 `9` ，因为 `9 OR (9 + 1) = 11` 。
- 对于 `i = 1` ，满足 `ans[1] OR (ans[1] + 1) = 13` 的最小 `ans[1]` 为 `12` ，因为 `12 OR (12 + 1) = 13` 。
- 对于 `i = 2` ，满足 `ans[2] OR (ans[2] + 1) = 31` 的最小 `ans[2]` 为 `15` ，因为 `15 OR (15 + 1) = 31` 。

 

**提示：**

- `1 <= nums.length <= 100`
- `2 <= nums[i] <= 1000`
- `nums[i]` 是一个质数。



这个问题要求我们找到最小的整数 $ans[i]$，使得 $ans[i] \lor (ans[i] + 1) = nums[i]$。

**算法分析**

1.  **位运算性质**：
    考察表达式 $x \lor (x + 1)$：
    - 如果 $x$ 的二进制表示以 $k$ 个连续的 $1$ 结尾（即 $x = \dots 0\underbrace{11\dots1}_{k}$），那么 $x+1$ 的二进制表示将会是 $\dots 1\underbrace{00\dots0}_{k}$。
    - 此时 $x \lor (x + 1) = (\dots 011\dots1) \lor (\dots 100\dots0) = \dots 111\dots1$。
    - 结果是将 $x$ 从右往左数第一个 $0$ 变成 $1$。

2.  **推导规律**：
    已知 $nums[i]$ 是质数。
    - 如果 $nums[i] = 2$（二进制 `10`）：它是唯一的偶质数。因为 $x \lor (x+1)$ 的结果必然是奇数（末位一定是 $1$），所以 $2$ 无法由该表达式得出，返回 $-1$。
    - 如果 $nums[i]$ 是奇数：它的二进制表示一定以 $1$ 结尾。为了让 $ans[i]$ 最小，我们需要找到 $nums[i]$ 末尾连续的 $1$。
      - 假设 $nums[i]$ 末尾有 $k$ 个连续的 $1$。
      - 根据上面的性质，如果我们把这 $k$ 个 $1$ 中最高位的那个 $1$ 变成 $0$，得到的数就是满足条件的最小 $ans[i]$。
      - 例如：$nums[i] = 7$ (二进制 `111`)，末尾有 $3$ 个 $1$。将从右数第 $3$ 位（权值为 $2^{3-1}=4$）的 $1$ 变 $0$，得到 $7 - 4 = 3$ (二进制 `011`)。
      - 验证：$3 \lor (3+1) = 3 \lor 4 = 7$。

3.  **具体步骤**：
    - 遍历 `nums` 中的每个数 $n$。
    - 若 $n=2$，结果为 $-1$。
    - 否则，从低位向高位查找 $n$ 的二进制中末尾连续 $1$ 的个数 $k$。
    - 计算 $ans = n - 2^{k-1}$ 或 $ans = n \oplus (1 \ll (k-1))$。

    **代码实现**

```python
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if n == 2:
                ans.append(-1)
            else:
                # 寻找末尾连续 1 的个数
                k = 0
                temp = n
                while temp & 1:
                    k += 1
                    temp >>= 1
                
                # 将第 k-1 位（从0开始）的 1 变为 0
                # 例如 n=7 (111), k=3, 结果应为 7 - 2^(3-1) = 3 (011)
                ans.append(n - (1 << (k - 1)))
        return ans
```

**复杂度分析**

- **时间复杂度**：$O(N \times \log(\max(nums)))$，其中 $N$ 是数组长度。由于 $nums[i] \le 1000$，$\log(nums[i])$ 最大约为 $10$，因此计算非常快。
- **空间复杂度**：$O(1)$，除了存储结果所需的数组外，仅使用了常数空间。



```python
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if n == 2:
                ans.append(-1)
            else:
                # n is odd prime >= 3
                low = (n + 1) & -(n + 1)  # lowest set bit of (n+1)
                x = n - low // 2
                ans.append(x)
        return ans
```



> 这份代码本质上是**利用位运算技巧更高效地寻找末尾连续的 1**。
>
> 它的核心逻辑和我之前提供的“寻找 $k$ 个连续的 1”是完全一致的，只不过它避开了 `while` 循环，直接通过位运算公式一步到位。
>
> 我们可以通过一个具体的例子来拆解这段代码的逻辑。
>
> **核心位运算技巧：`x & -x`**
>
> 在位运算中，`x & -x` 是一个经典的技巧，它能提取出整数 `x` 二进制表示中**最低位的 1（Lowest Set Bit）**及其后面的 0。
>
> 例如：
>
> *   若 $x = 12$（二进制 `1100`），则 `12 & -12 = 4`（二进制 `0100`）。
> *   若 $x = 8$（二进制 `1000`），则 `8 & -8 = 8`（二进制 `1000`）。
>
> **代码逻辑推导**
>
> 假设 $nums[i] = 11$，其二进制为 `1011`。
>
> 1.  **第一步：`n + 1`**
>     *   $11 + 1 = 12$。
>     *   二进制变化：`1011` $\rightarrow$ `1100`。
>     *   **关键点**：当一个末尾全是 $1$ 的数加 $1$ 时，这些 $1$ 会全部进位变成 $0$，而紧邻它们左边的那个 $0$ 会变成 $1$。
>
> 2.  **第二步：`low = (n + 1) & -(n + 1)`**
>     *   计算 $12$ 的最低位 $1$。
>     *   $12$ (`1100`) 的最低位 $1$ 是从右数第三位，权值为 $4$。
>     *   这个 `low` (即 $4$) 对应的位置，正好是 `n` (即 $11$) 从右往左数**第一个 0** 的位置。
>
> 3.  **第三步：`low // 2`**
>     *   `low // 2 = 4 // 2 = 2`。
>     *   在二进制中，`low // 2` 就是把那个 $1$ 向右移动一位。
>     *   这个位置对应的正好是 `n` (即 $11$) 末尾那串连续 $1$ 中的**最高位**。
>
> 4.  **第四步：`x = n - low // 2`**
>     *   $11 - 2 = 9$。
>     *   二进制：`1011 - 0010 = 1001`。
>     *   这步操作成功地把 `n` 末尾连续 $1$ 中的最高位从 $1$ 变成了 $0$。
>
>     **总结对照**
>
> | 概念                      | 你的代码写法         | 我的代码写法    |
> | :------------------------ | :------------------- | :-------------- |
> | **末尾 1 的个数**         | 无需计算具体个数 $k$ | 循环得到 $k$    |
> | **末尾 1 中最高位的权值** | `low // 2`           | `1 << (k - 1)`  |
> | **操作目标**              | 将该位的 1 变 0      | 将该位的 1 变 0 |
>
> **示例走读：`n = 7` (二进制 `111`)**
>
> 1.  `n + 1 = 8` (二进制 `1000`)
> 2.  `low = 8 & -8 = 8` (最低位的 1 是 8)
> 3.  `low // 2 = 4` (对应 `7` 的二进制 `111` 中左起第一个 1)
> 4.  `ans = 7 - 4 = 3` (二进制 `011`)
> 5.  验证：$3 \lor (3+1) = 3 \lor 4 = 7$。正确。
>
> **结论**：这份代码使用了 `(n+1) & -(n+1)` 巧妙地定位了需要修改的那一位，避免了循环，在性能上更优（虽然在 LeetCode 这道题的量级下差别不大），是一种更“硬核”的写法。



## E3370.仅含置位位的最小整数

bit manipulation, https://leetcode.cn/problems/smallest-number-with-all-set-bits/

给你一个正整数 `n`。

返回 **大于等于** `n` 且二进制表示仅包含 **置位** 位的 **最小** 整数 `x` 。

**置位** 位指的是二进制表示中值为 `1` 的位。

 

**示例 1：**

**输入：** n = 5

**输出：** 7

**解释：**

7 的二进制表示是 `"111"`。

**示例 2：**

**输入：** n = 10

**输出：** 15

**解释：**

15 的二进制表示是 `"1111"`。

**示例 3：**

**输入：** n = 3

**输出：** 3

**解释：**

3 的二进制表示是 `"11"`。

 

**提示：**

- `1 <= n <= 1000`



```python
class Solution:
    def smallestNumber(self, n: int) -> int:
        len = n.bit_length()
        s = '1'*len
        return int(s, 2)
```



```python
class Solution:
    def smallestNumber(self, n: int) -> int:
        return (1 << n.bit_length()) - 1
```





## 3375.使数组的值全部为K的最少操作次数

https://leetcode.cn/problems/minimum-operations-to-make-array-values-equal-to-k/

给你一个整数数组 `nums` 和一个整数 `k` 。

如果一个数组中所有 **严格大于** `h` 的整数值都 **相等** ，那么我们称整数 `h` 是 **合法的** 。

比方说，如果 `nums = [10, 8, 10, 8]` ，那么 `h = 9` 是一个 **合法** 整数，因为所有满足 `nums[i] > 9` 的数都等于 10 ，但是 5 不是 **合法** 整数。

你可以对 `nums` 执行以下操作：

- 选择一个整数 `h` ，它对于 **当前** `nums` 中的值是合法的。
- 对于每个下标 `i` ，如果它满足 `nums[i] > h` ，那么将 `nums[i]` 变为 `h` 。

你的目标是将 `nums` 中的所有元素都变为 `k` ，请你返回 **最少** 操作次数。如果无法将所有元素都变 `k` ，那么返回 -1 。



**示例 1：**

**输入：**nums = [5,2,5,4,5], k = 2

**输出：**2

**解释：**

依次选择合法整数 4 和 2 ，将数组全部变为 2 。

**示例 2：**

**输入：**nums = [2,1,2], k = 2

**输出：**-1

**解释：**

没法将所有值变为 2 。

**示例 3：**

**输入：**nums = [9,7,5,3], k = 1

**输出：**4

**解释：**

依次选择合法整数 7 ，5 ，3 和 1 ，将数组全部变为 1 。

 

**提示：**

- `1 <= nums.length <= 100 `
- `1 <= nums[i] <= 100`
- `1 <= k <= 100`



```python
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))
        nums.sort()
        max_v, min_v = nums[-1], nums[0]
        if min_v < k:
            return -1

        if k == min_v:
            return len(nums) - 1
        else:
            return len(nums)


if __name__ == "__main__":
    solution = Solution()
    print(solution.minOperations([5,2,5,4,5], 2))
    print(solution.minOperations([2,1,2], 2))
    print(solution.minOperations([9, 7, 5, 3], 1))
```



## E3379.转换数组

implementation, https://leetcode.cn/problems/transformed-array/

给你一个整数数组 `nums`，它表示一个循环数组。请你遵循以下规则创建一个大小 **相同** 的新数组 `result` ：

对于每个下标 `i`（其中 `0 <= i < nums.length`），独立执行以下操作：

- 如果 `nums[i] > 0`：从下标 `i` 开始，向 **右** 移动 `nums[i]` 步，在循环数组中落脚的下标对应的值赋给 `result[i]`。
- 如果 `nums[i] < 0`：从下标 `i` 开始，向 **左** 移动 `abs(nums[i])` 步，在循环数组中落脚的下标对应的值赋给 `result[i]`。
- 如果 `nums[i] == 0`：将 `nums[i]` 的值赋给 `result[i]`。

返回新数组 `result`。

**注意：**由于 `nums` 是循环数组，向右移动超过最后一个元素时将回到开头，向左移动超过第一个元素时将回到末尾。

 

**示例 1：**

**输入：** nums = [3,-2,1,1]

**输出：** [1,1,1,3]

**解释：**

- 对于 `nums[0]` 等于 3，向右移动 3 步到 `nums[3]`，因此 `result[0]` 为 1。
- 对于 `nums[1]` 等于 -2，向左移动 2 步到 `nums[3]`，因此 `result[1]` 为 1。
- 对于 `nums[2]` 等于 1，向右移动 1 步到 `nums[3]`，因此 `result[2]` 为 1。
- 对于 `nums[3]` 等于 1，向右移动 1 步到 `nums[0]`，因此 `result[3]` 为 3。

**示例 2：**

**输入：** nums = [-1,4,-1]

**输出：** [-1,-1,4]

**解释：**

- 对于 `nums[0]` 等于 -1，向左移动 1 步到 `nums[2]`，因此 `result[0]` 为 -1。
- 对于 `nums[1]` 等于 4，向右移动 4 步到 `nums[2]`，因此 `result[1]` 为 -1。
- 对于 `nums[2]` 等于 -1，向左移动 1 步到 `nums[1]`，因此 `result[2]` 为 4。

 

**提示：**

- `1 <= nums.length <= 100`
- `-100 <= nums[i] <= 100`



```python
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [nums[(i + nums[i]) % n] for i in range(n)]
```





## 3392.统计符合条件长度为3的子数组数目

https://leetcode.cn/problems/count-subarrays-of-length-three-with-a-condition/

给你一个整数数组 `nums` ，请你返回长度为 3 的 子数组，满足第一个数和第三个数的和恰好为第二个数的一半。

**子数组** 指的是一个数组中连续 **非空** 的元素序列。

 

**示例 1：**

**输入：**nums = [1,2,1,4,1]

**输出：**1

**解释：**

只有子数组 `[1,4,1]` 包含 3 个元素且第一个和第三个数字之和是中间数字的一半。number.

**示例 2：**

**输入：**nums = [1,1,1]

**输出：**0

**解释：**

`[1,1,1]` 是唯一长度为 3 的子数组，但第一个数和第三个数的和不是第二个数的一半。

 

**提示：**

- `3 <= nums.length <= 100`
- `-100 <= nums[i] <= 100`



```python
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        left = nums[0]
        for i in range(1, n-1):
            if nums[i] == (nums[i - 1] + nums[i + 1]) * 2:
                ans += 1
                left = nums[i]

        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.countSubarrays([1, 2, 1, 4, 1]))
    print(s.countSubarrays([1, 1, 1]))


```



## 3396.使数组元素互不相同所需的最少操作次数

https://leetcode.cn/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

给你一个整数数组 `nums`，你需要确保数组中的元素 **互不相同** 。为此，你可以执行以下操作任意次：

- 从数组的开头移除 3 个元素。如果数组中元素少于 3 个，则移除所有剩余元素。

**注意：**空数组也视作为数组元素互不相同。返回使数组元素互不相同所需的 **最少操作次数** 。

  

**示例 1：**

**输入：** nums = [1,2,3,4,2,3,3,5,7]

**输出：** 2

**解释：**

- 第一次操作：移除前 3 个元素，数组变为 `[4, 2, 3, 3, 5, 7]`。
- 第二次操作：再次移除前 3 个元素，数组变为 `[3, 5, 7]`，此时数组中的元素互不相同。

因此，答案是 2。

**示例 2：**

**输入：** nums = [4,5,6,4,4]

**输出：** 2

**解释：**

- 第一次操作：移除前 3 个元素，数组变为 `[4, 4]`。
- 第二次操作：移除所有剩余元素，数组变为空。

因此，答案是 2。

**示例 3：**

**输入：** nums = [6,7,8,9]

**输出：** 0

**解释：**

数组中的元素已经互不相同，因此不需要进行任何操作，答案是 0。

 

**提示：**

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`



```python
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
    
        while True:
            # 如果数组中元素已经互不相同，结束操作
            if len(set(nums)) == len(nums):
                break
            
            # 执行一次操作：移除前 3 个元素（或移除所有剩余元素）
            nums = nums[3:]
            operations += 1
            
            # 如果数组为空，直接结束
            if not nums:
                break
        
        return operations

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



## 3461.判断操作后字符串中的数字是否相等I

https://leetcode.cn/problems/check-if-digits-are-equal-in-string-after-operations-i/description/

给你一个由数字组成的字符串 `s` 。重复执行以下操作，直到字符串恰好包含 **两个** 数字：

- 从第一个数字开始，对于 `s` 中的每一对连续数字，计算这两个数字的和 **模** 10。
- 用计算得到的新数字依次替换 `s` 的每一个字符，并保持原本的顺序。

如果 `s` 最后剩下的两个数字 **相同** ，返回 `true` 。否则，返回 `false`。

 

**示例 1：**

**输入：** s = "3902"

**输出：** true

**解释：**

- 一开始，`s = "3902"`
- 第一次操作： 
  - `(s[0] + s[1]) % 10 = (3 + 9) % 10 = 2`
  - `(s[1] + s[2]) % 10 = (9 + 0) % 10 = 9`
  - `(s[2] + s[3]) % 10 = (0 + 2) % 10 = 2`
  - `s` 变为 `"292"`
- 第二次操作： 
  - `(s[0] + s[1]) % 10 = (2 + 9) % 10 = 1`
  - `(s[1] + s[2]) % 10 = (9 + 2) % 10 = 1`
  - `s` 变为 `"11"`
- 由于 `"11"` 中的数字相同，输出为 `true`。

**示例 2：**

**输入：** s = "34789"

**输出：** false

**解释：**

- 一开始，`s = "34789"`。
- 第一次操作后，`s = "7157"`。
- 第二次操作后，`s = "862"`。
- 第三次操作后，`s = "48"`。
- 由于 `'4' != '8'`，输出为 `false`。

 

**提示：**

- `3 <= s.length <= 100`
- `s` 仅由数字组成。





```python
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        q = [int(i) for i in s]
        
        while len(q) > 1:
            if len(set(q)) == 1:  # 如果所有数字相同，直接返回True
                return True
            
            if len(q) == 2:
                return q[0] == q[1]
            
            new_q = []
            for i in range(len(q) - 1):
                tmp = (q[i] + q[i + 1]) % 10
                new_q.append(tmp)
            
            q = new_q
        
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.hasSameDigits("3902"))  # True
    print(sol.hasSameDigits("34789")) # False
```



## 3477.将水果放入篮子II

implementation, https://leetcode.cn/problems/fruits-into-baskets-ii/

给你两个长度为 `n` 的整数数组，`fruits` 和 `baskets`，其中 `fruits[i]` 表示第 `i` 种水果的 **数量**，`baskets[j]` 表示第 `j` 个篮子的 **容量**。

你需要对 `fruits` 数组从左到右按照以下规则放置水果：

- 每种水果必须放入第一个 **容量大于等于** 该水果数量的 **最左侧可用篮子** 中。
- 每个篮子只能装 **一种** 水果。
- 如果一种水果 **无法放入** 任何篮子，它将保持 **未放置**。

返回所有可能分配完成后，剩余未放置的水果种类的数量。

 

**示例 1**

**输入：** fruits = [4,2,5], baskets = [3,5,4]

**输出：** 1

**解释：**

- `fruits[0] = 4` 放入 `baskets[1] = 5`。
- `fruits[1] = 2` 放入 `baskets[0] = 3`。
- `fruits[2] = 5` 无法放入 `baskets[2] = 4`。

由于有一种水果未放置，我们返回 1。

**示例 2**

**输入：** fruits = [3,6,1], baskets = [6,4,7]

**输出：** 0

**解释：**

- `fruits[0] = 3` 放入 `baskets[0] = 6`。
- `fruits[1] = 6` 无法放入 `baskets[1] = 4`（容量不足），但可以放入下一个可用的篮子 `baskets[2] = 7`。
- `fruits[2] = 1` 放入 `baskets[1] = 4`。

由于所有水果都已成功放置，我们返回 0。

 

**提示：**

- `n == fruits.length == baskets.length`
- `1 <= n <= 100`
- `1 <= fruits[i], baskets[i] <= 1000`





```python
from typing import List
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        cnt = 0
        used_baskets = [False] * len(baskets)
        for fruit in fruits:
            for i, basket in enumerate(baskets):
                if not used_baskets[i] and fruit <= basket:
                    used_baskets[i] = True
                    break
            else:
                cnt += 1

        return cnt

if __name__ == "__main__":
    sol = Solution()
    #print(sol.numOfUnplacedFruits([4,2,5], [3,5,4])) # 0
    #print(sol.numOfUnplacedFruits([3,6,1], [6,4,7]))
    #print(sol.numOfUnplacedFruits([8, 5], [1, 8]))# 1
    print(sol.numOfUnplacedFruits([7,4,2,9,7], [5,2,6,7,7])) # 0

```





## 3487.删除后的最大子数组元素和

https://leetcode.cn/problems/maximum-unique-subarray-sum-after-deletion/

给你一个整数数组 `nums` 。

你可以从数组 `nums` 中删除任意数量的元素，但不能将其变为 **空** 数组。执行删除操作后，选出 `nums` 中满足下述条件的一个子数组：

1. 子数组中的所有元素 **互不相同** 。
2. **最大化** 子数组的元素和。

返回子数组的 **最大元素和** 。

**子数组** 是数组的一个连续、**非空** 的元素序列。

 

**示例 1：**

**输入：**nums = [1,2,3,4,5]

**输出：**15

**解释：**

不删除任何元素，选中整个数组得到最大元素和。

**示例 2：**

**输入：**nums = [1,1,0,1,1]

**输出：**1

**解释：**

删除元素 `nums[0] == 1`、`nums[1] == 1`、`nums[2] == 0` 和 `nums[3] == 1` 。选中整个数组 `[1]` 得到最大元素和。

**示例 3：**

**输入：**nums = [1,2,-1,-2,1,0,-1]

**输出：**3

**解释：**

删除元素 `nums[2] == -1` 和 `nums[3] == -2` ，从 `[1, 2, 1, 0, -1]` 中选中子数组 `[2, 1]` 以获得最大元素和。

 

**提示：**

- `1 <= nums.length <= 100`
- `-100 <= nums[i] <= 100`



```python
from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # 筛选正数（删除重复只保留一个即可）
        pos = {x for x in nums if x > 0}
        if pos:
            # 如果有正数，选取所有正数（每个数只保留一次）的和最大
            return sum(pos)
        # 如果没有正数但存在 0，0 的和不会降低，所以答案为 0
        if 0 in nums:
            return 0
        # 如果全部为负数，必须选一个，所以选最大的（即负值中最大的那一个）
        return max(nums)
```



```python
from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = nums[0]
        visited = set()
        visited.add(nums[0])
        for num in nums[1:]:
            if num < 0 and num > ans:
                ans = num
                visited = set()
                visited.add(num)
                continue
            if num not in visited and num>=0:
                visited.add(num)
                ans = max(num, ans + num)

        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSum([1,2,3,4,5])) # 15
    print(sol.maxSum([1,1,0,1,1])) # 11
    print(sol.maxSum([-17,-15]))
```



## 3492.船上可以装载的最大集装箱数量

https://leetcode.cn/problems/maximum-containers-on-a-ship/

给你一个正整数 `n`，表示船上的一个 `n x n` 的货物甲板。甲板上的每个单元格可以装载一个重量 **恰好** 为 `w` 的集装箱。

然而，如果将所有集装箱装载到甲板上，其总重量不能超过船的最大承载重量 `maxWeight`。

请返回可以装载到船上的 **最大** 集装箱数量。

 

**示例 1：**

**输入：** n = 2, w = 3, maxWeight = 15

**输出：** 4

**解释：**

甲板有 4 个单元格，每个集装箱的重量为 3。将所有集装箱装载后，总重量为 12，未超过 `maxWeight`。

**示例 2：**

**输入：** n = 3, w = 5, maxWeight = 20

**输出：** 4

**解释：**

甲板有 9 个单元格，每个集装箱的重量为 5。可以装载的最大集装箱数量为 4，此时总重量不超过 `maxWeight`。

 

**提示：**

- `1 <= n <= 1000`
- `1 <= w <= 1000`
- `1 <= maxWeight <= 10^9`



```python
class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        return min(n*n, maxWeight//w)
```



## 3498.字符串的反转度

implementation, https://leetcode.cn/problems/reverse-degree-of-a-string/

给你一个字符串 `s`，计算其 **反转度**。

**反转度**的计算方法如下：

1. 对于每个字符，将其在 **反转** 字母表中的位置（`'a'` = 26, `'b'` = 25, ..., `'z'` = 1）与其在字符串中的位置（下标从**1** 开始）相乘。
2. 将这些乘积加起来，得到字符串中所有字符的和。

返回 **反转度**。

 

**示例 1：**

**输入：** s = "abc"

**输出：** 148

**解释：**

| 字母  | 反转字母表中的位置 | 字符串中的位置 | 乘积 |
| ----- | ------------------ | -------------- | ---- |
| `'a'` | 26                 | 1              | 26   |
| `'b'` | 25                 | 2              | 50   |
| `'c'` | 24                 | 3              | 72   |

反转度是 `26 + 50 + 72 = 148` 。

**示例 2：**

**输入：** s = "zaza"

**输出：** 160

**解释：**

| 字母  | 反转字母表中的位置 | 字符串中的位置 | 乘积 |
| ----- | ------------------ | -------------- | ---- |
| `'z'` | 1                  | 1              | 1    |
| `'a'` | 26                 | 2              | 52   |
| `'z'` | 1                  | 3              | 3    |
| `'a'` | 26                 | 4              | 104  |

反转度是 `1 + 52 + 3 + 104 = 160` 。

 

**提示：**

- `1 <= s.length <= 1000`
- `s` 仅包含小写字母。





```python
class Solution:
    def reverseDegree(self, s: str) -> int:
        n = len(s)
        total_v = 0
        for i in range(1, n+1):
            total_v += (26 - ord(s[i-1]) + ord('a')) * i

        return total_v

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseDegree("abc"))
    print(sol.reverseDegree("zaza"))
```





## 3502.到达每个位置的最小费用

dp, https://leetcode.cn/problems/minimum-cost-to-reach-every-position/

给你一个长度为 `n` 的整数数组 `cost` 。当前你位于位置 `n`（队伍的末尾），队伍中共有 `n + 1` 人，编号从 0 到 `n`。

你希望在队伍中向前移动，但队伍中每个人都会收取一定的费用才能与你 **交换**位置。与编号 `i` 的人交换位置的费用为 `cost[i]` 。

你可以按照以下规则与他人交换位置：

- 如果对方在你前面，你 **必须** 支付 `cost[i]` 费用与他们交换位置。
- 如果对方在你后面，他们可以免费与你交换位置。

返回一个大小为 `n` 的数组 `answer`，其中 `answer[i]` 表示到达队伍中每个位置 `i` 所需的 **最小** 总费用。

 

**示例 1：**

**输入:** cost = [5,3,4,1,3,2]

**输出:** [5,3,3,1,1,1]

**解释:**

我们可以通过以下方式到达每个位置：

- `i = 0`。可以花费 5 费用与编号 0 的人交换位置。
- `i = 1`。可以花费 3 费用与编号 1 的人交换位置。
- `i = 2`。可以花费 3 费用与编号 1 的人交换位置，然后免费与编号 2 的人交换位置。
- `i = 3`。可以花费 1 费用与编号 3 的人交换位置。
- `i = 4`。可以花费 1 费用与编号 3 的人交换位置，然后免费与编号 4 的人交换位置。
- `i = 5`。可以花费 1 费用与编号 3 的人交换位置，然后免费与编号 5 的人交换位置。

**示例 2：**

**输入:** cost = [1,2,4,6,7]

**输出:** [1,1,1,1,1]

**解释:**

可以花费 1 费用与编号 0 的人交换位置，然后可以免费到达队伍中的任何位置 `i`。

 

**提示**

- `1 <= n == cost.length <= 100`
- `1 <= cost[i] <= 100`



```python
from typing import List

class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        for i in range(1, n):
            if cost[i] >= cost[i-1]:
                dp[i] = dp[i-1]
                continue
            for j in range(i):
                dp[i] = min(cost[i], dp[j])

        return dp

if __name__ == '__main__':
    s = Solution()
    print(s.minCosts([5,3,4,1,3,2]))
    print(s.minCosts([1,2,4,6,7]))
```



## E3507.移除最小数对使数组有序 I

implementation, linked list, https://leetcode.cn/problems/minimum-pair-removal-to-sort-array-i/

给你一个数组 `nums`，你可以执行以下操作任意次数：

- 选择 **相邻** 元素对中 **和最小** 的一对。如果存在多个这样的对，选择最左边的一个。
- 用它们的和替换这对元素。

返回将数组变为 **非递减** 所需的 **最小操作次数** 。

如果一个数组中每个元素都大于或等于它前一个元素（如果存在的话），则称该数组为**非递减**。

 

**示例 1：**

**输入：** nums = [5,2,3,1]

**输出：** 2

**解释：**

- 元素对 `(3,1)` 的和最小，为 4。替换后 `nums = [5,2,4]`。
- 元素对 `(2,4)` 的和为 6。替换后 `nums = [5,6]`。

数组 `nums` 在两次操作后变为非递减。

**示例 2：**

**输入：** nums = [1,2,2]

**输出：** 0

**解释：**

数组 `nums` 已经是非递减的。

 

**提示：**

- `1 <= nums.length <= 50`
- `-1000 <= nums[i] <= 1000`



这个问题是一个**模拟（Simulation）**类型的题目。题目规定了每次操作必须选择数组中“和最小”的“相邻”元素对（若有多个，取最左边），并将它们替换为两数之和。由于操作规则是完全确定的（贪心且带唯一平局处理），且数组长度较小（$N \le 50$），我们可以直接根据规则进行模拟，直到数组满足非递减条件。

**解题思路**

1.  **终止条件**：首先检查数组是否已经是**非递减**的（即对所有 $i$，满足 `nums[i] <= nums[i+1]`）。如果是，则当前操作次数即为结果。
2.  **寻找操作目标**：
    *   遍历当前数组中所有相邻的数对 `(nums[i], nums[i+1])`。
    *   计算它们的和，并记录最小值以及该最小值首次出现的位置（索引 $i$）。
3.  **执行操作**：
    *   将索引 $i$ 处的元素修改为这两个元素的和。
    *   从数组中移除索引 $i+1$ 处的元素（数组长度减 1）。
    *   操作次数加 1。
4.  **循环**：重复上述过程，直到数组达到非递减状态。由于每次操作数组长度都会减少，且长度为 1 的数组天然是非递减的，因此程序一定会终止。

**复杂度分析**

*   **时间复杂度**：$O(N^2)$。数组长度 $N \le 50$，最多进行 $N-1$ 次操作。每次操作中需要扫描数组寻找最小和（$O(N)$）以及判断是否有序（$O(N)$）。总复杂度约为 $50 \times 100$，远小于性能限制。
*   **空间复杂度**：$O(N)$。主要用于存储数组的副本。

Python **代码实现**

```python
from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # 将输入转为列表以便进行原地修改和弹出操作
        arr = list(nums)
        ans = 0
        
        while True:
            # 1. 检查数组是否已经是非递减的
            is_sorted = True
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    is_sorted = False
                    break
            
            # 如果有序，则返回当前累计的操作次数
            if is_sorted:
                return ans
            
            # 2. 寻找和最小的相邻元素对，若有多个则取最左侧的
            # 初始化最小和为无穷大，记录起始索引 k
            min_sum = float('inf')
            k = -1
            
            for i in range(len(arr) - 1):
                current_sum = arr[i] + arr[i + 1]
                # 使用严格小于判断，保证在和相等时保留最左侧的索引
                if current_sum < min_sum:
                    min_sum = current_sum
                    k = i
            
            # 3. 执行替换操作：用和替换这对元素
            # 将第 k 个元素改为和，并删除第 k+1 个元素
            arr[k] = min_sum
            arr.pop(k + 1)
            
            # 增加操作次数
            ans += 1
```





```python
from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        cnt = 0
        arr = nums[:]  # 避免修改原数组（可选）
        
        while len(arr) > 1:
            # 检查是否已经非递减（无逆序对）
            is_non_decreasing = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
            if is_non_decreasing:
                break

            # 找到和最小的相邻对
            min_sum = float('inf')
            idx = 0
            for i in range(len(arr) - 1):
                s = arr[i] + arr[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i

            # 合并 arr[idx] 和 arr[idx+1]
            new_val = arr[idx] + arr[idx + 1]
            arr = arr[:idx] + [new_val] + arr[idx + 2:]
            cnt += 1

        return cnt


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumPairRemoval([-2, 1, 2, -1, -1, -2, -2, -1, -1, 1, 1]))  # 示例
```



## E3512.使数组和能被K整除的最少操作次数

https://leetcode.cn/problems/minimum-operations-to-make-array-sum-divisible-by-k/

给你一个整数数组 `nums` 和一个整数 `k`。你可以执行以下操作任意次：

- 选择一个下标 `i`，并将 `nums[i]` 替换为 `nums[i] - 1`。

返回使数组元素之和能被 `k` 整除所需的**最小**操作次数。

 

**示例 1：**

**输入：** nums = [3,9,7], k = 5

**输出：** 4

**解释：**

- 对 `nums[1] = 9` 执行 4 次操作。现在 `nums = [3, 5, 7]`。
- 数组之和为 15，可以被 5 整除。

**示例 2：**

**输入：** nums = [4,1,3], k = 4

**输出：** 0

**解释：**

- 数组之和为 8，已经可以被 4 整除。因此不需要操作。

**示例 3：**

**输入：** nums = [3,2], k = 6

**输出：** 5

**解释：**

- 对 `nums[0] = 3` 执行 3 次操作，对 `nums[1] = 2` 执行 2 次操作。现在 `nums = [0, 0]`。
- 数组之和为 0，可以被 6 整除。

 

**提示：**

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 1000`
- `1 <= k <= 100`





```python
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total_v = sum(nums)
        res = total_v % k
        if total_v % k == 0:
            return 0
        
        return res
```





## 3516.找到最近的人

https://leetcode.cn/problems/find-closest-person/

给你三个整数 `x`、`y` 和 `z`，表示数轴上三个人的位置：

- `x` 是第 1 个人的位置。
- `y` 是第 2 个人的位置。
- `z` 是第 3 个人的位置，第 3 个人 **不会移动** 。

第 1 个人和第 2 个人以 **相同** 的速度向第 3 个人移动。

判断谁会 **先** 到达第 3 个人的位置：

- 如果第 1 个人先到达，返回 1 。
- 如果第 2 个人先到达，返回 2 。
- 如果两个人同时到达，返回 **0** 。

根据上述规则返回结果。

 

**示例 1：**

**输入：** x = 2, y = 7, z = 4

**输出：** 1

**解释：**

- 第 1 个人在位置 2，到达第 3 个人（位置 4）需要 2 步。
- 第 2 个人在位置 7，到达第 3 个人需要 3 步。

由于第 1 个人先到达，所以输出为 1。

**示例 2：**

**输入：** x = 2, y = 5, z = 6

**输出：** 2

**解释：**

- 第 1 个人在位置 2，到达第 3 个人（位置 6）需要 4 步。
- 第 2 个人在位置 5，到达第 3 个人需要 1 步。

由于第 2 个人先到达，所以输出为 2。

**示例 3：**

**输入：** x = 1, y = 5, z = 3

**输出：** 0

**解释：**

- 第 1 个人在位置 1，到达第 3 个人（位置 3）需要 2 步。
- 第 2 个人在位置 5，到达第 3 个人需要 2 步。

由于两个人同时到达，所以输出为 0。

 

**提示：**

- `1 <= x, y, z <= 100`



```python
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(x - z) < abs(y - z):
            return 1
        elif abs(x - z) > abs(y - z):
            return 2
        else:
            return 0
        
```





## E3536.两个数字的最大乘积

implementation, https://leetcode.cn/problems/maximum-product-of-two-digits/

给定一个正整数 `n`。

返回 **任意两位数字** 相乘所得的 **最大** 乘积。

**注意：**如果某个数字在 `n` 中出现多次，你可以多次使用该数字。

 

**示例 1：**

**输入：** n = 31

**输出：** 3

**解释：**

- `n` 的数字是 `[3, 1]`。
- 任意两位数字相乘的结果为：`3 * 1 = 3`。
- 最大乘积为 3。

**示例 2：**

**输入：** n = 22

**输出：** 4

**解释：**

- `n` 的数字是 `[2, 2]`。
- 任意两位数字相乘的结果为：`2 * 2 = 4`。
- 最大乘积为 4。

**示例 3：**

**输入：** n = 124

**输出：** 8

**解释：**

- `n` 的数字是 `[1, 2, 4]`。
- 任意两位数字相乘的结果为：`1 * 2 = 2`, `1 * 4 = 4`, `2 * 4 = 8`。
- 最大乘积为 8。

 

**提示：**

- `10 <= n <= 10^9`





```python
from typing import List

class Solution:
    def maxProduct(self, n: int) -> int:
        n_lis = list(str(n))
        ans = - float("inf")
        for i in range(len(n_lis) - 1):
            for j in range(len(n_lis)):
                if i == j:
                    continue
                ans = max(ans, int(n_lis[i]) * int(n_lis[j]))

        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct(453))
```



## E3545.不同字符数量最多为 K 时的最少删除数

https://leetcode.cn/problems/minimum-deletions-for-at-most-k-distinct-characters/

给你一个字符串 `s`（由小写英文字母组成）和一个整数 `k`。

你的任务是删除字符串中的一些字符（可以不删除任何字符），使得结果字符串中的 **不同字符数量** 最多为 `k`。

返回为达到上述目标所需删除的 **最小** 字符数量。

 

**示例 1：**

**输入：** s = "abc", k = 2

**输出：** 1

**解释：**

- `s` 有三个不同的字符：`'a'`、`'b'` 和 `'c'`，每个字符的出现频率为 1。
- 由于最多只能有 `k = 2` 个不同字符，需要删除某一个字符的所有出现。
- 例如，删除所有 `'c'` 后，结果字符串中的不同字符数最多为 `k`。因此，答案是 1。

**示例 2：**

**输入：** s = "aabb", k = 2

**输出：** 0

**解释：**

- `s` 有两个不同的字符（`'a'` 和 `'b'`），它们的出现频率分别为 2 和 2。
- 由于最多可以有 `k = 2` 个不同字符，不需要删除任何字符。因此，答案是 0。

**示例 3：**

**输入：** s = "yyyzz", k = 1

**输出：** 2

**解释：**

- `s` 有两个不同的字符（`'y'` 和 `'z'`），它们的出现频率分别为 3 和 2。
- 由于最多只能有 `k = 1` 个不同字符，需要删除某一个字符的所有出现。
- 删除所有 `'z'` 后，结果字符串中的不同字符数最多为 `k`。因此，答案是 2。

 

**提示：**

- `1 <= s.length <= 16`
- `1 <= k <= 16`
- `s` 仅由小写英文字母组成。





```python
from collections import Counter

class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        count = Counter(s)
        n = len(count)
        if n <= k:
            return 0

        count = list(count.items())
        count = sorted(count, key=lambda x: x[1])
        ans = 0
        for key, value in count:
            ans += value
            n -= 1
            if n <= k:
                return ans

        return ans

if __name__ == "__main__":
    sol = Solution()
    #print(sol.minDeletion("abc", 2))  # 1
    #print(sol.minDeletion("yyyzz", 1))  # 2
    #print(sol.minDeletion("adx", 1))  # 2
    print(sol.minDeletion("rxlqseseuq", 1))  # 6
```



## E3550.数位和等于下标的最小下标

https://leetcode.cn/problems/smallest-index-with-digit-sum-equal-to-index/

给你一个整数数组 `nums` 。

返回满足 `nums[i]` 的数位和（每一位数字相加求和）等于 `i` 的 **最小** 下标 `i` 。

如果不存在满足要求的下标，返回 `-1` 。

 

**示例 1：**

**输入：**nums = [1,3,2]

**输出：**2

**解释：**

- `nums[2] = 2`，其数位和等于 2 ，与其下标 `i = 2` 相等。因此，输出为 2 。

**示例 2：**

**输入：**nums = [1,10,11]

**输出：**1

**解释：**

- `nums[1] = 10`，其数位和等于 `1 + 0 = 1`，与其下标 `i = 1` 相等。
- `nums[2] = 11`，其数位和等于是 `1 + 1 = 2`，与其下标 `i = 2` 相等。
- 由于下标 1 是满足要求的最小下标，输出为 1 。

**示例 3：**

**输入：**nums = [1,2,3]

**输出：**-1

**解释：**

- 由于不存在满足要求的下标，输出为 -1 。

 

**提示：**

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 1000`





```python
from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        res = -1
        for i in range(len(nums)):
            tot = 0
            while nums[i] > 0:
                tot += nums[i] % 10
                nums[i] //= 10

            if tot == i:
                res = i
                break

        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.smallestIndex([1, 3, 2])) # Expected output: -1

```



## E3560.木材运输的最小成本

implementation, https://leetcode.cn/problems/find-minimum-log-transportation-cost/description/

给你三个整数 `n`、`m` 和 `k`。

有两根长度分别为 `n` 和 `m` 单位的木材，需要通过三辆卡车运输。每辆卡车最多只能装载一根长度 **不超过** `k` 单位的木材。

你可以将木材切成更小的段，其中将长度为 `x` 的木材切割成长度为 `len1` 和 `len2` 的段的成本为 `cost = len1 * len2`，并且满足 `len1 + len2 = x`。

返回将木材分配到卡车上的 **最小总成本** 。如果木材不需要切割，总成本为 0。

 

**示例 1：**

**输入：** n = 6, m = 5, k = 5

**输出：** 5

**解释：**

将长度为 6 的木材切割成长度为 1 和 5 的两段，成本为 `1 * 5 == 5`。现在三段长度分别为 1、5 和 5 的木材可以分别装载到每辆卡车。

**示例 2：**

**输入：** n = 4, m = 4, k = 6

**输出：** 0

**解释：**

两根木材已经可以直接装载到卡车上，因此不需要切割。

 

**提示：**

- `2 <= k <= 10^5`
- `1 <= n, m <= 2 * k`
- 输入数据保证木材总存在能被运输的方案。





```python
class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if m <=k and n<=k:
            return 0
        if m <= k and n > k:
            return (n-k) * k
        if n <=k and m > k:
            return (m-k) * k

        return (m-k) * k + (n-k) * k

if __name__ == "__main__":
    sol = Solution()
    print(sol.minCuttingCost(6, 5, 5))
    print(sol.minCuttingCost(4, 4, 6))
```



## E3633.最早完成陆地和水上游乐设施的时间 I

greedy, https://leetcode.cn/problems/earliest-finish-time-for-land-and-water-rides-i/

给你两种类别的游乐园项目：**陆地游乐设施** 和 **水上游乐设施**。

- **陆地游乐设施**
  - `landStartTime[i]` – 第 `i` 个陆地游乐设施最早可以开始的时间。
  - `landDuration[i]` – 第 `i` 个陆地游乐设施持续的时间。
- **水上游乐设施**
  - `waterStartTime[j]` – 第 `j` 个水上游乐设施最早可以开始的时间。
  - `waterDuration[j]` – 第 `j` 个水上游乐设施持续的时间。

一位游客必须从 **每个** 类别中体验 **恰好****一个** 游乐设施，顺序 **不限** 。

- 游乐设施可以在其开放时间开始，或 **之后任意时间** 开始。
- 如果一个游乐设施在时间 `t` 开始，它将在时间 `t + duration` 结束。
- 完成一个游乐设施后，游客可以立即乘坐另一个（如果它已经开放），或者等待它开放。

返回游客完成这两个游乐设施的 **最早可能时间** 。

 

**示例 1:**

**输入：**landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]

**输出：**9

**解释：**

- 方案 A（陆地游乐设施 0 → 水上游乐设施 0）：
  - 在时间 `landStartTime[0] = 2` 开始陆地游乐设施 0。在 `2 + landDuration[0] = 6` 结束。
  - 水上游乐设施 0 在时间 `waterStartTime[0] = 6` 开放。立即在时间 `6` 开始，在 `6 + waterDuration[0] = 9` 结束。
- 方案 B（水上游乐设施 0 → 陆地游乐设施 1）：
  - 在时间 `waterStartTime[0] = 6` 开始水上游乐设施 0。在 `6 + waterDuration[0] = 9` 结束。
  - 陆地游乐设施 1 在 `landStartTime[1] = 8` 开放。在时间 `9` 开始，在 `9 + landDuration[1] = 10` 结束。
- 方案 C（陆地游乐设施 1 → 水上游乐设施 0）：
  - 在时间 `landStartTime[1] = 8` 开始陆地游乐设施 1。在 `8 + landDuration[1] = 9` 结束。
  - 水上游乐设施 0 在 `waterStartTime[0] = 6` 开放。在时间 `9` 开始，在 `9 + waterDuration[0] = 12` 结束。
- 方案 D（水上游乐设施 0 → 陆地游乐设施 0）：
  - 在时间 `waterStartTime[0] = 6` 开始水上游乐设施 0。在 `6 + waterDuration[0] = 9` 结束。
  - 陆地游乐设施 0 在 `landStartTime[0] = 2` 开放。在时间 `9` 开始，在 `9 + landDuration[0] = 13` 结束。

方案 A 提供了最早的结束时间 9。

**示例 2:**

**输入：**landStartTime = [5], landDuration = [3], waterStartTime = [1], waterDuration = [10]

**输出：**14

**解释：**

- 方案 A（水上游乐设施 0 → 陆地游乐设施 0）：
  - 在时间 `waterStartTime[0] = 1` 开始水上游乐设施 0。在 `1 + waterDuration[0] = 11` 结束。
  - 陆地游乐设施 0 在 `landStartTime[0] = 5` 开放。立即在时间 `11` 开始，在 `11 + landDuration[0] = 14` 结束。
- 方案 B（陆地游乐设施 0 → 水上游乐设施 0）：
  - 在时间 `landStartTime[0] = 5` 开始陆地游乐设施 0。在 `5 + landDuration[0] = 8` 结束。
  - 水上游乐设施 0 在 `waterStartTime[0] = 1` 开放。立即在时间 `8` 开始，在 `8 + waterDuration[0] = 18` 结束。

方案 A 提供了最早的结束时间 14。****

 

**提示:**

- `1 <= n, m <= 100`
- `landStartTime.length == landDuration.length == n`
- `waterStartTime.length == waterDuration.length == m`
- `1 <= landStartTime[i], landDuration[i], waterStartTime[j], waterDuration[j] <= 1000`



一个可行且高效的方法是遍历所有可能的陆地游乐设施和水上游乐设施的组合，分别计算“先体验陆地项目再体验水上项目”以及“先体验水上项目再体验陆地项目”的结束时间，并求出全局最小值。

**算法步骤**

对于每一个陆地游乐设施 $i$（其开始时间为 `landStartTime[i]`，持续时间为 `landDuration[i]`）和水上游乐设施 $j$（其开始时间为 `waterStartTime[j]`，持续时间为 `waterDuration[j]`）：

1. **先进行陆地游乐设施 $i$，后进行水上游乐设施 $j$**：
   - 陆地项目的结束时间为 $E_{land} = \text{landStartTime}[i] + \text{landDuration}[i]$。
   - 随后，水上项目最早可以在 $\max(E_{land}, \text{waterStartTime}[j])$ 开始，其完成时间为 $\max(E_{land}, \text{waterStartTime}[j]) + \text{waterDuration}[j]$。

2. **先进行水上游乐设施 $j$，后进行陆地游乐设施 $i$**：
   - 水上项目的结束时间为 $E_{water} = \text{waterStartTime}[j] + \text{waterDuration}[j]$。
   - 随后，陆地项目最早可以在 $\max(E_{water}, \text{landStartTime}[i])$ 开始，其完成时间为 $\max(E_{water}, \text{landStartTime}[i]) + \text{landDuration}[i]$。

通过遍历所有 $(i, j)$ 对（其中 $i \in [0, n-1]$，$j \in [0, m-1]$），并维护以上两种方案的最小值，即可求得最早完成两个游乐设施的时间。

**Python 代码实现**

```python
from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
        min_finish_time = float('inf')
        
        for i in range(n):
            lst = landStartTime[i]
            ldu = landDuration[i]
            land_end = lst + ldu
            
            for j in range(m):
                wst = waterStartTime[j]
                wdu = waterDuration[j]
                water_end = wst + wdu
                
                # 方案一：先陆地，后水上
                finish_1 = max(land_end, wst) + wdu
                
                # 方案二：先水上，后陆地
                finish_2 = max(water_end, lst) + ldu
                
                # 更新全局最小值
                if finish_1 < min_finish_time:
                    min_finish_time = finish_1
                if finish_2 < min_finish_time:
                    min_finish_time = finish_2
                    
        return min_finish_time
```

**复杂度分析**

- **时间复杂度**：$O(n \times m)$。其中 $n$ 为陆地游乐设施的数量，$m$ 为水上游乐设施的数量。由于题目中 $n, m \le 100$，最大循环次数约为 $10^4$，能够在极短时间内运行完毕。
- **空间复杂度**：$O(1)$。仅使用了若干变量来记录状态，不需要额外的辅助存储空间。





## E3637.三段式数组 I

implementation, https://leetcode.cn/problems/trionic-array-i/

给你一个长度为 `n` 的整数数组 `nums`。

如果存在索引 `0 < p < q < n − 1`，使得数组满足以下条件，则称其为 **三段式数组（trionic）**：

- `nums[0...p]` **严格** 递增，
- `nums[p...q]` **严格** 递减，
- `nums[q...n − 1]` **严格** 递增。

如果 `nums` 是三段式数组，返回 `true`；否则，返回 `false`。

 

**示例 1:**

**输入:** nums = [1,3,5,4,2,6]

**输出:** true

**解释:**

选择 `p = 2`, `q = 4`：

- `nums[0...2] = [1, 3, 5]` 严格递增 (`1 < 3 < 5`)。
- `nums[2...4] = [5, 4, 2]` 严格递减 (`5 > 4 > 2`)。
- `nums[4...5] = [2, 6]` 严格递增 (`2 < 6`)。

**示例 2:**

**输入:** nums = [2,1,3]

**输出:** false

**解释:**

无法选出能使数组满足三段式要求的 `p` 和 `q` 。

 

**提示:**

- `3 <= n <= 100`
- `-1000 <= nums[i] <= 1000`



```
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
```



0ms 击败100.00%

```python
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        trionic = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] == nums[i]:
                return False

            if trionic == 1 and nums[i-1] < nums[i]:
                continue
            if trionic == 2 and nums[i-1] > nums[i]:
                continue
            if trionic == 3 and nums[i-1] < nums[i]:
                continue

            if trionic == 0 and nums[i-1] > nums[i]:
                return False
            elif trionic == 0 and nums[i-1] < nums[i]:
                trionic = 1
                continue
            
            if trionic == 1 and nums[i-1] < nums[i]:
                return False
            elif trionic == 1 and nums[i-1] > nums[i]:
                trionic = 2
                continue
            
            if trionic == 2 and nums[i-1] >= nums[i]:
                return False
            elif trionic == 2 and nums[i-1] < nums[i]:
                trionic = 3
                continue
            
            if trionic == 3 and nums[i-1] > nums[i]:
                return False
        
        return True if trionic == 3 else False
```



3ms 击败33.33%

```python
from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False  # 至少需要 4 个元素才能有 3 段（如 a<b>c<d）
        
        state = 0  # 0: 初始（期待上升），1: 上升，2: 下降，3: 再次上升
        
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return False
            
            if state == 0:
                if nums[i] > nums[i - 1]:
                    state = 1
                else:
                    return False  # 第一步不能下降
            
            elif state == 1:
                if nums[i] > nums[i - 1]:
                    continue  # 继续上升
                elif nums[i] < nums[i - 1]:
                    state = 2  # 转入下降段
            
            elif state == 2:
                if nums[i] < nums[i - 1]:
                    continue  # 继续下降
                elif nums[i] > nums[i - 1]:
                    state = 3  # 转入第二次上升
            
            elif state == 3:
                if nums[i] > nums[i - 1]:
                    continue  # 继续第二次上升
                else:
                    return False  # 第三段不能下降或持平
        
        return state == 3
```



0ms 击败100.00%

根据题目要求，我们需要判断一个数组是否可以被划分为三个连续的段：**严格递增**、**严格递减**、**严格递增**。

**解题思路**

1.  **定义分界点**：
    我们需要寻找两个索引 $p$ 和 $q$，使得 $0 < p < q < n - 1$。
    *   第一段 `nums[0...p]` 是严格递增的。
    *   第二段 `nums[p...q]` 是严格递减的。
    *   第三段 `nums[q...n-1]` 是严格递增的。

2.  **贪心策略**：
    由于要求是**严格**的，分界点 $p$ 和 $q$ 在满足条件的数组中是唯一的：
    *   $p$ 必须是数组从开头开始的第一个局部极大值点（即递增结束的地方）。
    *   $q$ 必须是 $p$ 之后第一个遇到的局部极小值点（即递减结束的地方）。
    *   如果我们在到达数组末尾之前就走完了这三个阶段，或者某个阶段无法形成（例如没有递减就到了结尾），则该数组不是“三段式”。

3.  **算法步骤**：
    *   初始化指针 `i = 0`。
    *   **阶段 1（严格递增）**：向后移动 `i`，直到不再满足 `nums[i] < nums[i+1]`。此时的 `i` 就是候选的 $p$。如果 $i=0$（没有增加）或 $i \ge n-2$（没有给后续段留出空间），返回 `false`。
    *   **阶段 2（严格递减）**：从 $p$ 开始，向后移动 `i`，直到不再满足 `nums[i] > nums[i+1]`。此时的 `i` 就是候选的 $q$。如果 $i=p$（没有减少）或 $i \ge n-1$（没有给第三段留出空间），返回 `false`。
    *   **阶段 3（严格递增）**：从 $q$ 开始，向后移动 `i`，直到不再满足 `nums[i] < nums[i+1]`。
    *   **最终判断**：如果最后 `i` 成功到达了数组的最后一个元素索引 $n-1$，说明符合条件。

    **Python 代码实现**

```python
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        # 索引 0 < p < q < n - 1 要求 n 至少为 4
        if n < 4:
            return False
        
        i = 0
        
        # 1. 严格递增段 nums[0...p]
        while i + 1 < n and nums[i] < nums[i+1]:
            i += 1
        
        # p = i, p 必须大于 0 且后面至少还要留两个位置给 q 和 n-1
        p = i
        if p == 0 or p >= n - 2:
            return False
        
        # 2. 严格递减段 nums[p...q]
        while i + 1 < n and nums[i] > nums[i+1]:
            i += 1
        
        # q = i, q 必须大于 p 且后面至少要留一个位置给 n-1
        q = i
        if q == p or q >= n - 1:
            return False
        
        # 3. 严格递增段 nums[q...n-1]
        while i + 1 < n and nums[i] < nums[i+1]:
            i += 1
            
        # 必须正好扫描到数组末尾
        return i == n - 1
```

**复杂度分析**

*   **时间复杂度**：$O(n)$。我们只需对数组进行一次线性扫描。
*   **空间复杂度**：$O(1)$。只使用了常数级别的额外空间。



## E3643.垂直翻转子矩阵

two pointers, matrix, https://leetcode.cn/problems/flip-square-submatrix-vertically/

给你一个 `m x n` 的整数矩阵 `grid`，以及三个整数 `x`、`y` 和 `k`。

整数 `x` 和 `y` 表示一个 **正方形子矩阵** 的左上角下标，整数 `k` 表示该正方形子矩阵的边长。

你的任务是垂直翻转子矩阵的行顺序。

返回更新后的矩阵。

 

**示例 1：**

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/gridexmdrawio.png" alt="img" style="zoom:50%;" />

**输入：** grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], x = 1, y = 0, k = 3

**输出：** [[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]

**解释：**

上图展示了矩阵在变换前后的样子。

**示例 2：**

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/gridexm2drawio.png" alt="img" style="zoom:50%;" />

**输入：** grid = [[3,4,2,3],[2,3,4,2]], x = 0, y = 2, k = 2

**输出：** [[3,4,4,2],[2,3,2,3]]

**解释：**

上图展示了矩阵在变换前后的样子。

 

**提示：**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `1 <= grid[i][j] <= 100`
- `0 <= x < m`
- `0 <= y < n`
- `1 <= k <= min(m - x, n - y)`



这个问题要求我们将矩阵中一个指定的 $k \times k$ 正方形子矩阵进行**垂直翻转**。

**算法思路**

1.  **确定范围**：
    *   子矩阵的左上角坐标为 $(x, y)$，边长为 $k$。
    *   行范围是从 $x$ 到 $x + k - 1$。
    *   列范围是从 $y$ 到 $y + k - 1$。
2.  **垂直翻转的含义**：
    *   垂直翻转意味着将子矩阵的第一行与最后一行交换，第二行与倒数第二行交换，依此类推。
    *   注意：**只有**子矩阵内部（即列下标在 $[y, y+k-1]$ 之间）的元素需要交换，该行中位于子矩阵之外的元素保持不变。
3.  **实现步骤**：
    *   使用双指针法，令 `top = x`，`bottom = x + k - 1`。
    *   当 `top < bottom` 时：
        *   遍历列下标 $j$ 从 $y$ 到 $y + k - 1$。
        *   交换 `grid[top][j]` 和 `grid[bottom][j]`。
        *   `top` 向下移动一位（`top += 1`），`bottom` 向上移动一位（`bottom -= 1`）。

        **Python 代码实现**

```python
from typing import List

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        # 初始化双指针，分别指向子矩阵的最顶行和最底行
        top = x
        bottom = x + k - 1
        
        # 进行垂直翻转，直到指针相遇或交错
        while top < bottom:
            # 仅交换子矩阵覆盖的列范围 [y, y + k - 1]
            for j in range(y, y + k):
                grid[top][j], grid[bottom][j] = grid[bottom][j], grid[top][j]
            
            # 移动指针
            top += 1
            bottom -= 1
            
        return grid
```

**复杂度分析**

*   **时间复杂度**：$O(k^2)$。我们需要遍历并交换子矩阵中大约一半的元素。由于 $k \le \min(m, n)$ 且 $m, n \le 50$，最大计算次数约为 $50 \times 25 = 1250$ 次，效率非常高。
*   **空间复杂度**：$O(1)$。我们是在原矩阵上进行原地修改，除了循环变量外没有使用额外的空间。

**示例解析（示例 1）**

输入：`grid` 为 4x4 矩阵，`x=1, y=0, k=3`

*   子矩阵行范围：1 到 3（包含 1, 2, 3 行）。
*   子矩阵列范围：0 到 2（包含 0, 1, 2 列）。
*   第 1 行的 `[5, 6, 7]` 与第 3 行的 `[13, 14, 15]` 交换。
*   第 2 行是中间行，保持不变。
*   结果：第一行不变，二四行部分交换，三行不变。符合预期输出。



```
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        for i in range(k//2):
            for j in range(y, y + k):
                grid[x + i][j], grid[x+k-1 - i][j] = grid[x+k-1 - i][j], grid[x + i][j]
        
        return grid
```



## E3658.奇数和与偶数和的最大公约数

math, https://leetcode.cn/problems/gcd-of-odd-and-even-sums/

给你一个整数 `n`。请你计算以下两个值的 **最大公约数**（GCD）：

- `sumOdd`：最小的 `n` 个正奇数的总和。
- `sumEven`：最小的 `n` 个正偶数的总和。

返回 `sumOdd` 和 `sumEven` 的 GCD。

 

**示例 1：**

**输入：** n = 4

**输出：** 4

**解释：**

- 前 4 个奇数的总和 `sumOdd = 1 + 3 + 5 + 7 = 16`
- 前 4 个偶数的总和 `sumEven = 2 + 4 + 6 + 8 = 20`

因此，`GCD(sumOdd, sumEven) = GCD(16, 20) = 4`。

**示例 2：**

**输入：** n = 5

**输出：** 5

**解释：**

- 前 5 个奇数的总和 `sumOdd = 1 + 3 + 5 + 7 + 9 = 25`
- 前 5 个偶数的总和 `sumEven = 2 + 4 + 6 + 8 + 10 = 30`

因此，`GCD(sumOdd, sumEven) = GCD(25, 30) = 5`。

 

**提示：**

- `1 <= n <= 1000`



**方法分析**

我们可以通过数学公式来推导首 $n$ 个奇数之和与首 $n$ 个偶数之和的关系：

1. **最小的 $n$ 个正奇数的总和 $sumOdd$**：
   前 $n$ 个奇数分别为 $1, 3, 5, \dots, 2n-1$。
   其和为等差数列求和公式：
   $$sumOdd = \frac{(1 + 2n - 1) \times n}{2} = n^2$$

2. **最小的 $n$ 个正偶数的总和 $sumEven$**：
   前 $n$ 个偶数分别为 $2, 4, 6, \dots, 2n$。
   其和同样可以使用求和公式：
   $$sumEven = \frac{(2 + 2n) \times n}{2} = n(n+1)$$

根据最大公约数（GCD）的性质，我们可以提取公共公因数：
$$\text{GCD}(sumOdd, sumEven) = \text{GCD}(n^2, n(n+1))$$

由于 $n > 0$，我们可以将公因数 $n$ 提取到外面：
$$\text{GCD}(n^2, n(n+1)) = n \cdot \text{GCD}(n, n+1)$$

因为 $n$ 和 $n+1$ 是两个连续的整数，它们是互质的（即它们的最大公约数为 $1$）：
$$\text{GCD}(n, n+1) = 1$$

所以：
$$\text{GCD}(sumOdd, sumEven) = n \cdot 1 = n$$

因此，对于任意的正整数 $n$，其结果总是 $n$ 本身。

**Python 代码实现**

```python
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
```

**复杂度分析**

- **时间复杂度**：$O(1)$，只需直接返回 $n$。
- **空间复杂度**：$O(1)$，不需要额外的辅助空间。



## E3731.找出缺失的元素

https://leetcode.cn/problems/find-missing-elements/

给你一个整数数组 `nums` ，数组由若干 **互不相同** 的整数组成。

数组 `nums` 原本包含了某个范围内的 **所有整数** 。但现在，其中可能 **缺失** 部分整数。

该范围内的 **最小** 整数和 **最大** 整数仍然存在于 `nums` 中。

返回一个 **有序** 列表，包含该范围内缺失的所有整数，并 **按从小到大排序**。如果没有缺失的整数，返回一个 **空** 列表。

 

**示例 1：**

**输入：** nums = [1,4,2,5]

**输出：** [3]

**解释：**

最小整数为 1，最大整数为 5，因此完整的范围应为 `[1,2,3,4,5]`。其中只有 3 缺失。

**示例 2：**

**输入：** nums = [7,8,6,9]

**输出：** []

**解释：**

最小整数为 6，最大整数为 9，因此完整的范围为 `[6,7,8,9]`。所有整数均已存在，因此没有缺失的整数。

**示例 3：**

**输入：** nums = [5,1]

**输出：** [2,3,4]

**解释：**

最小整数为 1，最大整数为 5，因此完整的范围应为 `[1,2,3,4,5]`。缺失的整数为 2、3 和 4。

 

**提示：**

- `2 <= nums.length <= 100`
- `1 <= nums[i] <= 100`



这道题要求我们找出在最小值和最大值所构成的连续整数区间 `[min(nums), max(nums)]` 中缺失的所有整数，并按从小到大的顺序返回。

**解题思路**

1. **确定区间范围**：首先求出数组 `nums` 中的最小值 `min_val` 和最大值 `max_val`。
2. **快速查找存在性**：将数组 `nums` 转换为集合 `set`，以便能在 $O(1)$ 时间复杂度内检查某个数是否存在于原数组中。
3. **遍历缺失元素**：从 `min_val` 到 `max_val` 遍历区间内的每一个整数，如果该整数不在集合中，则将其加入结果列表中。

**Python 代码**

```python
from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        min_val = min(nums)
        max_val = max(nums)
        
        # 遍历 [min_val, max_val] 范围内的每个整数，收集缺失的数
        return [x for x in range(min_val, max_val + 1) if x not in num_set]
```

**复杂度分析**

- **时间复杂度**：$O(N + M)$，其中 $N$ 是数组 `nums` 的长度，$M$ 是最大值与最小值的差值（即区间大小 $max\_val - min\_val + 1$）。
  - 求最小值、最大值和转换为集合需要 $O(N)$ 时间。
  - 遍历区间并进行 $O(1)$ 的集合查找需要 $O(M)$ 时间。
  - 本题中 $N, M \le 100$，运行时间极快。
- **空间复杂度**：$O(N)$，用于存储原数组元素的哈希集合 `num_set`。





## E3740.三个相等元素之间的最小距离 I

hash table, https://leetcode.cn/problems/minimum-distance-between-three-equal-elements-i/

给你一个整数数组 `nums`。

如果满足 `nums[i] == nums[j] == nums[k]`，且 `(i, j, k)` 是 3 个 **不同** 下标，那么三元组 `(i, j, k)` 被称为 **有效三元组** 。

**有效三元组** 的 **距离** 被定义为 `abs(i - j) + abs(j - k) + abs(k - i)`，其中 `abs(x)` 表示 `x` 的 **绝对值** 。

返回一个整数，表示 **有效三元组** 的 **最小** 可能距离。如果不存在 **有效三元组** ，返回 `-1`。

 

**示例 1：**

**输入：** nums = [1,2,1,1,3]

**输出：** 6

**解释：**

最小距离对应的有效三元组是 `(0, 2, 3)` 。

`(0, 2, 3)` 是一个有效三元组，因为 `nums[0] == nums[2] == nums[3] == 1`。它的距离为 `abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6`。

**示例 2：**

**输入：** nums = [1,1,2,3,2,1,2]

**输出：** 8

**解释：**

最小距离对应的有效三元组是 `(2, 4, 6)` 。

`(2, 4, 6)` 是一个有效三元组，因为 `nums[2] == nums[4] == nums[6] == 2`。它的距离为 `abs(2 - 4) + abs(4 - 6) + abs(6 - 2) = 2 + 2 + 4 = 8`。

**示例 3：**

**输入：** nums = [1]

**输出：** -1

**解释：**

不存在有效三元组，因此答案为 -1。

 

**提示：**

- `1 <= n == nums.length <= 100`
- `1 <= nums[i] <= n`



这个问题要求我们在数组中找到三个相等的元素，使得它们的下标三元组 $(i, j, k)$ 产生的“距离”最小。

**1. 距离公式分析**

已知有效三元组的距离定义为：
$$D = |i - j| + |j - k| + |k - i|$$

假设我们将三个下标按从小到大排序为 $i < j < k$，则：

- $|i - j| = j - i$
- $|j - k| = k - j$
- $|k - i| = k - i$

将它们代入公式：
$$D = (j - i) + (k - j) + (k - i) = 2 \times (k - i)$$

因此，**最小化距离等价于最小化三元组中最大下标与最小下标的差值**。

**2. 解题思路**

1.  **分组下标**：首先遍历数组，将每个数值对应的所有下标记录下来。例如，如果 `nums = [1, 2, 1, 1, 3]`，则数值 `1` 的下标列表为 `[0, 2, 3]`。
2.  **寻找最小间距**：对于每一个数值，遍历它出现的下标列表。
    *   如果某个数值出现的次数少于 3 次，则无法组成有效三元组。
    *   如果出现次数 $\ge 3$，为了使 $k - i$ 最小，我们只需要检查下标列表中**相邻的三个下标**。假设某个数值的下标列表为 $p_0, p_1, p_2, \dots, p_m$，我们计算所有 $2 \times (p_{t+2} - p_t)$ 的值并取最小值。
3.  **结果处理**：如果遍历完所有可能的数值后都没有找到有效三元组，返回 `-1`；否则返回找到的最小距离。

**3. 代码实现**

```python
from typing import List
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # 使用哈希表记录每个数字出现的下标
        pos_map = defaultdict(list)
        for idx, val in enumerate(nums):
            pos_map[val].append(idx)
        
        min_dist = float('inf')
        found = False
        
        # 遍历每个数字对应的下标列表
        for val in pos_map:
            indices = pos_map[val]
            # 只有出现次数大于等于3次的数字才能构成三元组
            if len(indices) >= 3:
                found = True
                # 检查所有连续的三个下标，计算 2 * (max_idx - min_idx)
                for i in range(len(indices) - 2):
                    # 距离公式简化为 2 * (indices[i+2] - indices[i])
                    current_dist = 2 * (indices[i+2] - indices[i])
                    if current_dist < min_dist:
                        min_dist = current_dist
        
        return int(min_dist) if found else -1

```

**4. 复杂度分析**

*   **时间复杂度**：$O(n)$，其中 $n$ 是数组的长度。我们只需要遍历一次数组来建立下标映射，再遍历一次所有收集到的下标。
*   **空间复杂度**：$O(n)$，用于存储每个数值及其对应的下标列表。



## E3783.整数的镜像距离

implementation, https://leetcode.cn/problems/mirror-distance-of-an-integer/

给你一个整数 `n`。

定义它的 **镜像距离** 为：`abs(n - reverse(n))`，其中 `reverse(n)` 表示将 `n` 的数字反转后形成的整数。

返回表示 `n` 的镜像距离的整数。

其中，`abs(x)` 表示 `x` 的绝对值。

 

**示例 1：**

**输入：** n = 25

**输出：** 27

**解释：**

- `reverse(25) = 52`。
- 因此，答案为 `abs(25 - 52) = 27`。

**示例 2：**

**输入：** n = 10

**输出：** 9

**解释：**

- `reverse(10) = 01`，即 1。
- 因此，答案为 `abs(10 - 1) = 9`。

**示例 3：**

**输入：** n = 7

**输出：** 0

**解释：**

- `reverse(7) = 7`。
- 因此，答案为 `abs(7 - 7) = 0`。

 

**提示：**

- `1 <= n <= 10^9`



这是a + b 的水题。

```python
class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev_n = 0
        tmp = n
        while tmp > 0:
            rev_n = rev_n * 10 + tmp % 10
            tmp = tmp // 10
        
        return abs(n - rev_n)
```





## E3827.统计单比特整数

bit manipulation, https://leetcode.cn/problems/count-monobit-integers/

给你一个整数 `n`。

如果一个整数的二进制表示中所有位都相同，则称其为 **单比特数**（**Monobit**）。

返回范围`[0, n]`（包括两端）内 **单比特数** 的个数。

 

**示例 1：**

**输入：** n = 1

**输出：** 2

**解释：**

- 范围`[0, 1]`内的整数对应的二进制表示为`"0"`和`"1"`。
- 每个表示都由相同的位组成，因此答案是2。

**示例 2：**

**输入：** n = 4

**输出：** 3

**解释：**

- 范围`[0, 4]`内的整数对应的二进制表示为`"0"`、`"1"`、`"10"`、`"11"`和`"100"`。
- 只有`0`、`1`和`3`满足单比特条件。因此答案是3。

 

**提示：**

- `0 <= n <= 1000`



```python
class Solution:
    def countMonobit(self, n: int) -> int:
        count = 0
        for i in range(n+1):
            if (1 << i.bit_length()) - 1 == i:
                count += 1
        
        return count
```



## E3838.带权单词映射

implementation, https://leetcode.cn/problems/weighted-word-mapping/

给你一个字符串数组 `words`，其中每个字符串表示一个由小写英文字母组成的单词。

同时给你一个长度为 26 的整数数组 `weights`，其中 `weights[i]` 表示第 `i` 个小写英文字母的权重。

单词的 **权重** 定义为其所有字符权重的 **总和**。

对于每个单词，将其权重对 26 取模，并将结果按字母倒序映射到一个小写英文字母（`0 -> 'z', 1 -> 'y', ..., 25 -> 'a'`）。

返回一个由所有单词映射后的字符按顺序连接而成的字符串。

 

**示例 1：**

**输入：** words = ["abcd","def","xyz"], weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]

**输出：** "rij"

**解释：**

- `"abcd"` 的权重是 `5 + 3 + 12 + 14 = 34`。对 26 取模的结果是 `34 % 26 = 8`，映射为 `'r'`。
- `"def"` 的权重是 `14 + 1 + 2 = 17`。对 26 取模的结果是 `17 % 26 = 17`，映射为 `'i'`。
- `"xyz"` 的权重是 `7 + 7 + 2 = 16`。对 26 取模的结果是 `16 % 26 = 16`，映射为 `'j'`。

因此，连接映射字符后形成的字符串是 `"rij"`。

**示例 2：**

**输入：** words = ["a","b","c"], weights = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

**输出：** "yyy"

**解释：**

每个单词的权重均为 1。对 26 取模的结果是 `1 % 26 = 1`，映射为 `'y'`。

因此，连接映射字符后形成的字符串是 `"yyy"`。

**示例 3：**

**输入：** words = ["abcd"], weights = [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]

**输出：** "g"

**解释：**

`"abcd"` 的权重是 `7 + 5 + 3 + 4 = 19`。对 26 取模的结果是 `19 % 26 = 19`，映射为 `'g'`。

因此，连接映射字符后形成的字符串是 `"g"`。

 

**提示：**

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 10`
- `weights.length == 26`
- `1 <= weights[i] <= 100`
- `words[i]` 仅由小写英文字母组成。



这是一个在 Python 3 中解决“带权单词映射”问题的实现方法。

**解题思路**

1. **计算单词权重**：对于给定的每一个单词 `word`，遍历其所有字符，根据 `weights` 数组获取每个字符的权重，并计算总和。由于字符是小写英文字母，字符 `c` 对应的 `weights` 索引可以通过 `ord(c) - ord('a')` 得到。

2. **取模运算**：将计算得到的总权重对 26 取模，即 `R = weight % 26`。

3. **字符映射**：根据题目要求的字母倒序映射规则：

   - `0 -> 'z'`
   - `1 -> 'y'`
   - ...
   - `25 -> 'a'`

   我们可以通过公式 `chr(ord('z') - R)` 得到映射后的字符。

4. **拼接结果**：对 `words` 中的每一个单词依次处理，将得到的映射字符拼接成一个完整的字符串并返回。

**Python 3 实现**

```python
from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        ord_a = ord('a')
        ord_z = ord('z')
        
        for word in words:
            # 计算单词的总权重
            total_weight = sum(weights[ord(char) - ord_a] for char in word)
            # 计算对 26 取模的结果
            remainder = total_weight % 26
            # 映射到倒序字母表的对应字符
            mapped_char = chr(ord_z - remainder)
            result.append(mapped_char)
            
        return "".join(result)
```

**复杂度分析**

- **时间复杂度**：$O(N \times L)$，其中 $N$ 是单词数组 `words` 的长度（最多 100），$L$ 是每个单词的最大长度（最多 10）。我们需要遍历每个单词的每个字符来计算权重，因此整体时间复杂度与所有单词字符总数成正比。该算法效率较高，能够快速完成处理。
- **空间复杂度**：$O(N)$，用于存储每个单词映射后的字符以及最后生成的返回字符串。





# End







