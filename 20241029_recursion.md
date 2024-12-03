# 2024/10/29 递归

Updated 2253 GMT+8 Nov 7, 2024

2024 fall, Complied by Hongfei Yan



> Log:
>
> 20241102: 在 三 增加了 yield生成器
>
> 20241101: 增加了 3.2 函数参数是可变、不可变对象
>
> 20241024: 晴问 复活了。https://sunnywhy.com 晴问 是零基础同学的福音。算法基础。。。 确实有点难了。
>
> 2024/10/24 部分内容取自, https://github.com/GMyhf/2023fall-cs101/blob/main/recursion_questions.md



# 一、Recap

## 1 博弈题目练习

博弈题目练习greedy挺好，因为双方都要选择局部最优，还有双指针技巧在里面。

> 博弈题目的确是一个非常锻炼思维的类型，尤其在涉及双方都要在局部选择最优时，Greedy（贪心算法）方法特别适用。双方都尽力为自己做出最优选择，但这并不一定保证全局最优，因此这类题目常常涉及策略和博弈论。
>
> 双指针技巧在处理这类问题时也非常有用，特别是在一些序列类问题中，比如：
>
> - **石子游戏**：两名玩家从数组的两端取石子，目标是获取最多的分数。这类问题通常可以通过双指针来模拟双方的选择，配合贪心来决定下一步动作。
> - **扑克牌问题**：双方轮流从一组牌中选择牌，目标是获得最大点数。这里可以结合贪心策略选择最优牌，但也需要考虑对方的选择。
>
> 博弈题目一般会涉及到递归、动态规划等更高级的技巧，因为往往需要记录双方在每一步的最优策略及未来的影响。而贪心往往是处理局部最优解的有效方法，虽然不能保证全局最优，但在特定场景下能简化复杂问题。
>

### 1.1 编程题目

#### 1425A. Arena of Greed

games, greedy, 1400, https://codeforces.com/problemset/problem/1425/A

Lately, Mr. Chanek frequently plays the game **Arena of Greed**. As the name implies, the game's goal is to find the greediest of them all, who will then be crowned king of Compfestnesia.

The game is played by two people taking turns, where Mr. Chanek takes the first turn. Initially, there is a treasure chest containing N gold coins. The game ends if there are no more gold coins in the chest. In each turn, the players can make one of the following moves:

- Take one gold coin from the chest.
- Take half of the gold coins on the chest. This move is only available if the number of coins in the chest is even.

Both players will try to maximize the number of coins they have. Mr. Chanek asks your help to find the maximum number of coins he can get at the end of the game if both he and the opponent plays optimally.



#### 1749C. Number Game

binary search, data structure, games, greedy, implementation, 1400, https://codeforces.com/problemset/problem/1749/C

Alice and Bob are playing a game. They have an array of positive integers 𝑎 of size 𝑛.

Before starting the game, Alice chooses an integer 𝑘≥0. The game lasts for 𝑘 stages, the stages are numbered from 1 to 𝑘. During the 𝑖-th stage, Alice must remove an element from the array that is less than or equal to $𝑘−𝑖+1$. After that, if the array is not empty, Bob must add $𝑘−𝑖+1$ to an arbitrary element of the array. Note that both Alice's move and Bob's move are two parts of the same stage of the game. If Alice can't delete an element during some stage, she loses. If the 𝑘-th stage ends and Alice hasn't lost yet, she wins.

Your task is to determine the maximum value of 𝑘 such that Alice can win if both players play optimally. Bob plays against Alice, so he tries to make her lose the game, if it's possible.





## 2 解决输入数据太多



### 2.1 缓存原理sys.stdin.read

原理很简单，吃饭时候一口一口吃，肯定比一粒一粒吃要快。

合理使用buffer是编程小技巧，但是有的题目不用的话，python提交基本就是超时，如：CF1425A. Arena of Greed.



> 在编程中（例如 Codeforces 上），使用缓冲输入输出（I/O）可以显著提升程序性能，特别是当数据量非常大时。Python 默认情况下使用缓冲 I/O，但通过合理地控制输入输出，可以进一步减少因频繁的 I/O 操作导致的时间开销，避免超时。
>
> **输入优化：**
>
> 1. **`sys.stdin.read()`** 代替 `input()`：
>    - `input()` 每次读取一行，而 `sys.stdin.read()` 会一次性读取所有输入，可以在数据量大时显著提升速度。
>    - 例如：
>      ```python
>      import sys
>      input = sys.stdin.read
>      data = input().split()  # 读入所有数据并分割为列表
>      ```
>
> 2. **批量读取：** 
>    - 对于较大的输入数据，通过一次性读取并处理比逐行读取更高效。
>
> **输出优化：**
>
> 1. **`sys.stdout.write()`** 代替 `print()`：
>    - `print()` 函数默认会在每次调用后刷新输出缓冲区，而 `sys.stdout.write()` 允许在最后一次性输出所有结果。
>    - 例如：
>      ```python
>      import sys
>      sys.stdout.write('\n'.join(map(str, results)) + '\n')
>      ```
>    - 这种方式将所有输出内容一次性写入缓冲区，在最后统一输出，避免了多次刷新。
>
> 2. **批量输出：**
>    - 像处理输入一样，通过将所有输出内容收集后一次性输出可以极大地优化程序性能。
>
> **示例：**
>
> 假设你要处理多个测试用例，下面是一个优化输入输出的 Python 代码示例：
>
> ```python
> import sys
> 
> input = sys.stdin.read
> output = sys.stdout.write
> 
> def solve():
>     data = input().split()
>     n = int(data[0])
>     results = []
>     for i in range(1, n + 1):
>         # 假设是简单的加法运算
>         results.append(str(int(data[2*i - 1]) + int(data[2*i])))
>     output("\n".join(results) + "\n")
> 
> solve()
> ```
>
> 在这段代码中，我们一次性读取所有数据，并通过 `sys.stdout.write` 批量输出，减少了 I/O 操作的次数，能有效避免超时。
>



### 2.2 sys.stdin.read替代try...except

系统的测试文件中数据有很多组，在程序里要写循环读取数据并判断是否读完文件的代码。Python模版这样写：

```python
while(True):
	try:
    ...
	except EOFError:
    break
```



另外一种输入处理方法：使用 sys.stdin.read() 一次性读取所有输入数据，以提高效率。



#### 示例：03248: 最大公约数

math, http://cs101.openjudge.cn/practice/03248

给定两个正整数，求它们的最大公约数。

**输入**

有多组数据，每行为两个正整数，且不超过int可以表示的范围。

**输出**

行对应输出最大公约数。

样例输入

```
4 8
8 6
200 300
```

样例输出

```
4
2
100
```

提示



用math.gcd

```python
from math import gcd

while True:
    try:
        a, b = input().split()
        print(gcd(int(a), int(b)))
    except EOFError:
        break
```



自己实现gcd

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    for line in data:
        a, b = map(int, line.split())
        print(gcd(a, b))

if __name__ == "__main__":
    main()
```





# 二、递归



## 1 What Is Recursion?

https://runestone.academy/ns/books/published/pythonds3/Recursion/WhatIsRecursion.html?mode=browsing

**Recursion** is a method of solving problems that involves breaking a problem down into smaller and smaller subproblems until you get to a small enough problem that it can be solved trivially. Recursion involves a function calling itself. While it may not seem like much on the surface, recursion allows us to write elegant solutions to problems that may otherwise be very difficult to program.

> **递归**是一种解决问题的方法，它涉及将一个问题分解成越来越小的子问题，直到得到一个足够小的问题，可以轻易地解决。递归涉及到一个函数调用自身。虽然表面上看起来可能没什么特别之处，但递归使我们能够编写出优雅的解决方案，来解决那些可能非常难以编程的问题。

### 示例：Calculating the Sum of a Vector of Numbers

We will begin our investigation with a simple problem that you already know how to solve without using recursion. Suppose that you want to calculate the sum of a vector of numbers such as: [1,3,5,7,9]. An iterative function that computes the sum is shown in [ActiveCode 4.3.1](https://runestone.academy/ns/books/published/pythonds3/Recursion/CalculatingtheSumofaListofNumbers.html?mode=browsing#lst-itsum). The function uses an accumulator variable (`the_sum`) to compute a running total of all the numbers in the list by starting with and adding each number in the list.

> 我们将从一个简单的、你已经知道如何在不使用递归的情况下解决的问题开始我们的探讨。假设你想计算一个数字向量（如 [1, 3, 5, 7, 9]）的总和。一个使用迭代方法计算总和的函数如 [ActiveCode 4.3.1](https://runestone.academy/ns/books/published/pythonds3/Recursion/CalculatingtheSumofaListofNumbers.html?mode=browsing#lst-itsum) 所示。该函数使用一个累加器变量 (`the_sum`) 通过从初始值开始并加上列表中的每个数字来计算列表中所有数字的运行总和。

```python
def list_sum(num_list):
    the_sum = 0
    for i in num_list:
        the_sum = the_sum + i
    return the_sum

print(list_sum([1, 3, 5, 7, 9]))
```

Activity: 4.3.1 Iterative Summation



Such an expression looks like this: $((((1 + 3) + 5) + 7) + 9)$

We can also parenthesize the expression the other way around, $(1 + (3 + (5 + (7 + 9))))$

Notice that the innermost set of parentheses, , is a problem that we can solve without a loop or any special constructs. In fact, we can use the following sequence of simplifications to compute a final sum.

   

$total = \  (1 + (3 + (5 + (7 + 9)))) \\
total = \  (1 + (3 + (5 + 16))) \\
total = \  (1 + (3 + 21)) \\
total = \  (1 + 24) \\
total = \  25$



How can we take this idea and turn it into a Python program? First, let’s restate the sum problem in terms of Python lists. We might say the sum of the list `num_list` is the sum of the first element of the list (`num_list[0]`) and the sum of the numbers in the rest of the list (`num_list[1:]`). To state it in a functional form:

> 我们如何将这个想法转化为一个 Python 程序呢？首先，让我们用 Python 列表来重新表述求和问题。我们可以这样描述：列表 `num_list` 的总和等于列表的第一个元素 (`num_list[0]`) 与列表剩余部分 (`num_list[1:]`) 中所有数字的总和。以函数形式表示为：

$list\_sum(num\_list) = first(num\_list) + list\_sum(rest(num\_list))
\label{eqn:list_sum}$

In this equation `first(num_list)`returns the first element of the list and `rest(num_list)`returns a list of everything but the first element. This is easily expressed in Python as shown in [ActiveCode 4.3.2](https://runestone.academy/ns/books/published/pythonds3/Recursion/CalculatingtheSumofaListofNumbers.html?mode=browsing#lst-recsum).

```python
#Example of summing a list using recurison.

def list_sum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + list_sum(numList[1:]) #function makes a recursive call to itself.

print(list_sum([1, 3, 5, 7, 9]))
```

Activity: 4.3.2 Recursive Summation



There are a few key ideas while using vector to look at. First, on line 4 we are checking to see if the vector is one element long. This check is crucial and is our escape clause from the function. The sum of a vector of length 1 is trivial; it is just the number in the vector. Second, on line 7 our function calls itself! This is the reason that we call the `vectsum` algorithm recursive. A recursive function is a function that calls itself.

> 在这段代码中有几个关键点需要注意。首先，在第4行，我们检查列表是否只有一个元素。这个检查是至关重要的，是我们从函数中退出的条件。长度为1的列表的总和是显而易见的；它就是列表中的那个数字。其次，在第7行，我们的函数调用了自身！这就是为什么我们将 `list_sum` 算法称为递归的原因。递归函数是指调用自身的函数。

Figure 1 shows the series of **recursive calls** that are needed to sum the list. You should think of this series of calls as a series of simplifications. Each time we make a recursive call we are solving a smaller problem, until we reach the point where the problem cannot get any smaller.

> 图1展示了求和列表所需的递归调用序列。你可以将这一系列调用视为一系列简化过程。每次进行递归调用时，我们都在解决一个更小的问题，直到问题不能再被简化为止。

![image](https://raw.githubusercontent.com/GMyhf/img/main/img/sumlistIn.png)

Figure 1: Series of Recursive Calls Adding a List of Numbers

When we reach the point where the problem is as simple as it can get, we begin to piece together the solutions of each of the small problems until the initial problem is solved. Figure 2 shows the additions that are performed as `listsum` works its way backward through the series of calls. When `listsum` returns from the topmost problem, we have the solution to the whole problem.

> 当我们到达问题不能再被简化的地步时，我们开始将每个小问题的解逐步组合起来，直到最初的整个问题被解决。图2展示了随着 `listsum` 从最顶层的问题逐步回溯通过一系列调用时所进行的加法运算。当 `listsum` 从最顶层的问题返回时，我们就得到了整个问题的解。

![image](https://raw.githubusercontent.com/GMyhf/img/main/img/sumlistOut.png)

Figure2: Series of Recursive Returns from Adding a List of Numbers



## 2. Three Laws of Recursion递归三法则

https://runestone.academy/ns/books/published/pythonds3/Recursion/TheThreeLawsofRecursion.html?mode=browsing

Like the robots of Asimov, all recursive algorithms must obey three important laws:

> 1. A recursive algorithm must have a **base case**.递归算法必须有一个**基准情形**。
> 2. A recursive algorithm must change its state and move toward the base case.递归算法必须改变其状态并朝着基准情形前进。
> 3. A recursive algorithm must call itself, recursively.递归算法必须调用自身，即进行递归调用。

Let’s look at each one of these laws in more detail and see how it was used in the `vectsum` algorithm. First, a base case is the condition that allows the algorithm to stop recursing. A base case is typically a problem that is small enough to solve directly. In the `vectsum` algorithm the base case is a list of length 1. 

> 基准情形是允许算法停止递归的条件。基准情形通常是一个足够小可以直接解决的问题。在`vectsum`算法中，基准情形是一个长度为1的列表。

To obey the second law, we must arrange for a change of state that moves the algorithm toward the base case. A change of state means that some data that the algorithm is using is modified. Usually the data that represents our problem gets smaller in some way. In the `vectsum` algorithm our primary data structure is a vector, so we must focus our state-changing efforts on the vector. Since the base case is a list of length 1, a natural progression toward the base case is to shorten the vector. 

> 为了遵守第二条法则，我们必须安排状态的变化，使算法朝着基准情形前进。状态变化意味着算法使用的一些数据被修改了。通常代表我们问题的数据会以某种方式变小。在`vectsum`算法中，我们的主要数据结构是一个向量，所以我们必须将状态变化的重点放在向量上。由于基准情形是一个长度为1的列表，因此一个自然的朝向基准情形的进展就是缩短向量。

The final law is that the algorithm must call itself. This is the very definition of recursion. Recursion is a confusing concept to many beginning programmers. As a novice programmer, you have learned that functions are good because you can take a large problem and break it up into smaller problems. The smaller problems can be solved by writing a function to solve each problem. When we talk about recursion it may seem that we are talking ourselves in circles. We have a problem to solve with a function, but that function solves the problem by calling itself! But the logic is not circular at all; the logic of recursion is an elegant expression of solving a problem by breaking it down into smaller and easier problems.

> 最后一条法则是算法必须调用自身。这就是递归的定义。递归对许多初学者来说是一个令人困惑的概念。作为一名新手程序员，你已经了解到函数的好处在于可以将一个大问题分解成更小的问题。这些问题可以通过编写函数来分别解决。当我们谈论递归时，似乎我们在绕圈子说话。我们有一个需要通过函数解决的问题，但该函数通过调用自身来解决问题！但实际上逻辑并不循环；<mark>递归的逻辑是一种优雅的表达方式，它通过将问题分解成更小、更简单的问题来解决问题。</mark>

It is important to note that regardless of whether or not a recursive function implements these three rules, it may still take an unrealistic amount of time to compute (and thus not be particularly useful). 



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231121110930261.png" alt="image-20231121110930261" style="zoom:50%;" />



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231121111000626.png" alt="image-20231121111000626" style="zoom:50%;" />



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231121111024513.png" alt="image-20231121111024513" style="zoom:50%;" />



### 示例：Converting an Integer to a String in Any Base

Suppose you want to convert an integer to a string in some base between binary and hexadecimal. For example, convert the integer 10 to its string representation in decimal as `"10"`, or to its string representation in binary as `"1010"`. While there are many algorithms to solve this problem, including the algorithm discussed in the stack section, the recursive formulation of the problem is very elegant.

> 假设你想将一个整数转换为二进制到十六进制之间的某个进制的字符串表示。例如，将整数10转换为其十进制字符串表示 "10"，或将其转换为二进制字符串表示 "1010"。虽然有很多算法可以解决这个问题，包括在栈部分讨论的算法，但递归方法的表述非常优雅。

Let’s look at a concrete example using base 10 and the number 769. Suppose we have a sequence of characters corresponding to the first 10 digits, like `convString = "0123456789"`. It is easy to convert a number less than 10 to its string equivalent by looking it up in the sequence. For example, if the number is 9, then the string is `convString[9]` or `"9"`. If we can arrange to break up the number 769 into three single-digit numbers, 7, 6, and 9, then converting it to a string is simple. A number less than 10 sounds like a good base case.

> 让我们来看一个具体的例子，使用十进制和数字769。假设我们有一个对应于前10个数字的字符序列，如 `convert_string = "0123456789"`。通过查找这个序列，很容易将小于10的数字转换为其字符串等价形式。例如，如果数字是9，那么字符串就是 `convert_string[9]` 或 "9"。如果我们能够将数字769分解成三个单个数字7、6和9，那么将其转换为字符串就很简单了。小于10的数字听起来像是一个好的基准情形。

Knowing what our base is suggests that the overall algorithm will involve three components:

1. Reduce the original number to a series of single-digit numbers.将原始数字减少为一系列单个数字。
2. Convert the single digit-number to a string using a lookup.使用查找表将单个数字转换为字符串。
3. Concatenate the single-digit strings together to form the final result.将单个数字的字符串连接起来形成最终结果。

The next step is to figure out how to change state and make progress toward the base case. Since we are working with an integer, let’s consider what mathematical operations might reduce a number. The most likely candidates are division and subtraction. While subtraction might work, it is unclear what we should subtract from what. Integer division with remainders gives us a clear direction. Let’s look at what happens if we divide a number by the base we are trying to convert to.

> 下一步是弄清楚如何改变状态并朝着基准情形前进。由于我们在处理一个整数，让我们考虑哪些数学运算可以减少一个数字。最有可能的候选者是除法和减法。虽然减法可能有效，但我们不清楚应该从什么中减去什么。带余数的整数除法则为我们指明了明确的方向。让我们看看当我们试图将一个数字除以目标进制时会发生什么。

Using integer division to divide 769 by 10, we get 76 with a remainder of 9. This gives us two good results. First, the remainder is a number less than our base that can be converted to a string immediately by lookup. Second, we get a number that is smaller than our original and moves us toward the base case of having a single number less than our base. Now our job is to convert 76 to its string representation. Again we will use integer division plus remainder to get results of 7 and 6 respectively. Finally, we have reduced the problem to converting 7, which we can do easily since it satisfies the base case condition of n<base, where base=10. The series of operations we have just performed is illustrated in Figure 3. Notice that the numbers we want to remember are in the remainder boxes along the right side of the diagram.

> 使用整数除法将769除以10，我们得到商76和余数9。这给了我们两个很好的结果。首先，余数是一个小于我们基数的数字，可以通过查找立即转换为字符串。其次，我们得到了一个比原数小的数字，并且它使我们朝着只有一个小于基数的数字的基准情形前进。现在我们的任务是将76转换为其字符串表示。我们再次使用整数除法加上余数，分别得到7和6。最后，我们将问题简化为转换7，这很容易做到，因为它满足基准情形条件。我们刚刚执行的一系列操作如图3所示。注意，我们需要记住的数字在图表右侧的余数框中。



![image](https://runestone.academy/ns/books/published/pythonds3/_images/toStr.png)

**Figure 3:** Converting an Integer to a String in Base 10



Activity: 4.5.1 shows the Python code that implements the algorithm outlined above for any base between 2 and 16.

```python
def to_str(n, base):
    # 定义用于转换的字符序列
    convert_string = "0123456789ABCDEF"

    # 基准情形：如果 n 小于基数，则直接返回对应的字符
    if n < base:
        return convert_string[n]
    else:
        # 递归调用：先处理商，再处理余数
        # 通过延迟连接操作，确保结果的顺序是正确的
        return to_str(n // base, base) + convert_string[n % base]


# 示例
print(to_str(10, 2))  # 输出: "1010"
print(to_str(255, 16))  # 输出: "FF"
```

Activity: 4.5.1 Recursively Converting from Integer to String

Notice that in line 6 we check for the base case where `n` is less than the base we are converting to. When we detect the base case, we stop recursing and simply return the string from the `convertString` sequence. In line 11 we satisfy both the second and third laws–by making the recursive call and by reducing the problem size–using division.

> 请注意，在第6行我们检查了基准情形，即当 `n` 小于我们要转换的基数时。当我们检测到基准情形时，我们停止递归，并直接从 `convert_string` 序列中返回相应的字符串。在第11行，我们通过进行递归调用并使用除法来减小问题规模，从而满足了第二条和第三条法则。

Let’s trace the algorithm again; this time we will convert the number 10 to its base 2 string representation (`"1010"`).

> 让我们再次跟踪 ActiveCode 4.5.1 中显示的算法；这次我们将把数字10转换为其二进制字符串表示（"1010"）。

![image](https://raw.githubusercontent.com/GMyhf/img/main/img/toStrBase2.png)

Figure 4: Converting the Number 10 to its Base 2 String Representation

[Figure 4](https://runestone.academy/ns/books/published/cppds/Recursion/pythondsConvertinganIntegertoaStringinAnyBase.html#fig-tostr2) shows that we get the results we are looking for, but it looks like the digits are in the wrong order. The algorithm works correctly because we make the recursive call first on line 8, then we add the string representation of the remainder. If we reversed returning the `convertString` lookup and returning the `toStr` call, the resulting string would be backward! But ==by delaying the concatenation operation until after the recursive call has returned, we get the result in the proper order.== This should remind you of our discussion of stacks back in the previous chapter.

> 图4.4显示我们得到了预期的结果，但看起来数字的顺序是反的。算法之所以能正确工作，是因为我们在第6行首先进行了递归调用，然后才添加余数的字符串表示。如果我们先返回 `convert_string` 查找的结果，再返回 `to_str` 调用的结果，最终得到的字符串将会是反向的！但是，通过将连接操作延迟到递归调用返回之后进行，我们得到了正确的顺序。这应该让你想起我们在前一章中关于栈的讨论。

<img src="/Users/hfyan/Library/Application Support/typora-user-images/image-20231121113514094.png" alt="image-20231121113514094" style="zoom:50%;" />



## 3. 栈和递归的关系

### 3.1 Stack Frames: Implementing Recursion

https://runestone.academy/ns/books/published/pythonds3/Recursion/StackFramesImplementingRecursion.html?mode=browsing

Suppose that instead of concatenating the result of the recursive call to `to_str` with the string from `convertString`, we modified our algorithm to push the strings onto a stack instead of making the recursive call. The code for this modified algorithm is shown.

> 假设我们不是将递归调用 `to_str` 的结果与 `convertString` 中的字符串进行连接，而是修改算法，将字符串压入栈中，而不是进行递归调用。这个修改后的算法代码如下所示。
>
> - **使用栈替代递归**：通过将字符串压入栈中，我们可以避免递归调用，并在最后从栈中弹出字符串以获得正确的顺序。
> - **栈的后进先出（LIFO）特性**：这确保了我们在处理完所有子问题后，能够以正确的顺序组合结果。

```python
rStack = []

def to_str(n,base):
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.append(convertString[n]) #adds string n to the stack.
        else:
            rStack.append(convertString[n % base]) #adds string n modulo base to the stack.
        n = n // base
    res = ""
    while rStack:
        #combines all the items in the stack to make the full string.
        res = res + str(rStack.pop())
    return res

print(to_str(1453,16))
```

**Activity**: 4.6.1 Converting an Integer to a String Using a Stack



Each time we make a call to `to_str`, we push a character on the stack. Returning to the previous example we can see that after the fourth call to `toStr` the stack would look like Figure 5. Notice that now we can simply pop the characters off the stack and concatenate them into the final result, `"1010"`.

> 每次我们调用 `to_str` 时，都会将一个字符压入栈中。回到前面的例子，我们可以看到，在第四次调用 `to_str` 后，栈的状态如图4.5所示。注意到现在我们可以简单地从栈中弹出字符并将它们连接成最终结果 "1010"。

![../_images/recstack.png](https://raw.githubusercontent.com/GMyhf/img/main/img/recstack.png)

Figure 5: Strings Placed on the Stack During Conversion

The previous example gives us some insight into how Python implements a recursive function call. When a function is called in Python, a **stack frame** is allocated to handle the local variables of the function. When the function returns, the return value is left on top of the stack for the calling function to access. Figure 6 illustrates the call stack after the return statement on line 4.

> 前面的例子让我们对 Python 如何实现递归函数调用有了一些了解。当在 Python 中调用一个函数时，会分配一个栈帧来处理该函数的局部变量。当函数返回时，返回值会被留在栈顶，供调用函数访问。图6展示了第4行的返回语句后的调用栈。





![../_images/callstack.png](https://runestone.academy/ns/books/published/pythonds3/_images/callstack.png)

**Figure 6:** Call Stack Generated from `to_str(10, 2)`



Notice that the call to `to_tr(2//2,2)` leaves a return value of `"1"` on the stack. This return value is then used in place of the function call (`to_str(1,2)`) in the expression `"1" + convertString[2%2]`, which will leave the string `"10"` on the top of the stack. In this way, the Python call stack takes the place of the stack we used explicitly in [Listing 4](https://runestone.academy/ns/books/published/cppds/Recursion/StackFramesImplementingRecursion.html#lst-recstackcpp). In our list summing example, you can think of the return value on the stack taking the place of an accumulator variable.

> 请注意，在清单4.4中定义的 `to_str(2 // 2, 2)` 调用会在栈上留下返回值 "1"。这个返回值随后在表达式 `"1" + convert_string[2 % 2]` 中代替了函数调用 `to_str(1, 2)`，这将在栈顶留下字符串 "10"。通过这种方式，Python 的调用栈替代了我们在 ActiveCode 4.6.1 中显式使用的栈。在我们的列表求和示例中，你可以认为栈上的返回值替代了一个累加器变量的作用。

The stack frames also provide a scope for the variables used by the function. Even though we are calling the same function over and over, each call creates a new scope for the variables that are local to the function.

> 栈帧还为函数使用的变量提供了作用域。即使我们反复调用同一个函数，每次调用都会<mark>为函数的局部变量创建一个新的作用域</mark>。



### 3.2 函数参数是可变、不可变对象

参数是可变，还是不可变对象，是不一样的，前者在被调用者栈帧中，后者在调用者栈帧中。

> 你提到的关于参数是可变对象还是不可变对象的区别是正确的。在 Python 中，参数传递的方式取决于参数的类型：
>
> 1. **不可变对象**（如数字、字符串、元组）：在函数调用时，传递的是值的副本。因此，对不可变对象的修改不会影响调用者。
> 2. **可变对象**（如列表、字典）：在函数调用时，传递的是对象的引用。因此，对可变对象的修改会影响到调用者。
>
> **不可变对象**
>
> 对于不可变对象，每次函数调用时传递的是值的副本，因此在被调用者中对参数的修改不会影响调用者。
>
> **示例**
>
> ```python
> def modify_value(x):
>     x = x + 1
>     print(f"Inside modify_value, x = {x}")
> 
> x = 5
> print(f"Before modify_value, x = {x}")
> modify_value(x)
> print(f"After modify_value, x = {x}")
> ```
>
> **输出**
>
> ```
> Before modify_value, x = 5
> Inside modify_value, x = 6
> After modify_value, x = 5
> ```
>
> **可变对象**
>
> 对于可变对象，每次函数调用时传递的是对象的引用，因此在被调用者中对参数的修改会影响到调用者。
>
> **示例**
>
> ```python
> def modify_list(lst):
>     lst.append(1)
>     print(f"Inside modify_list, lst = {lst}")
> 
> lst = [2, 3]
> print(f"Before modify_list, lst = {lst}")
> modify_list(lst)
> print(f"After modify_list, lst = {lst}")
> ```
>
> **输出**
>
> ```
> Before modify_list, lst = [2, 3]
> Inside modify_list, lst = [2, 3, 1]
> After modify_list, lst = [2, 3, 1]
> ```
>
> 
>
> **递归调用中的回溯**
>
> 在递归调用中，如果传递的参数是一个可变对象（如列表），在被调用者中对这个对象的修改会影响到调用者。为了保持状态的一致性和正确性，通常需要在递归调用返回后恢复这个对象的状态，这就是回溯的过程。
>
> **示例**
>
> 假设我们有一个递归函数 `dfs`，它接受一个列表 `col_selected` 作为参数，并在调用前对 `col_selected` 进行修改。为了确保每次递归调用返回后 `col_selected` 的状态正确恢复，我们需要在递归调用后进行回溯。
>
> ```python
> def dfs(col_selected, j, n):
>     col_selected.append(j)  # 选择列 j
>     print(f"Inside dfs, col_selected = {col_selected}")
>     
>     # 递归调用
>     for next_j in range(j + 1, n):
>         dfs(col_selected, next_j, n)
>     
>     col_selected.pop()  # 回溯，恢复 col_selected 的状态
> 
> # 初始调用
> n = 4
> dfs([], 0, n)
> ```
>
> **输出**
>
> ```
> Inside dfs, col_selected = [0]
> Inside dfs, col_selected = [0, 1]
> Inside dfs, col_selected = [0, 1, 2]
> Inside dfs, col_selected = [0, 1, 2, 3]
> Inside dfs, col_selected = [0, 1, 3]
> Inside dfs, col_selected = [0, 2]
> Inside dfs, col_selected = [0, 2, 3]
> Inside dfs, col_selected = [0, 3]
> ```
>
> 总结
>
> - **不可变对象**：在函数调用时传递的是值的副本，对参数的修改不会影响调用者。
> - **可变对象**：在函数调用时传递的是对象的引用，对参数的修改会影响到调用者。为了保持状态的一致性和正确性，通常需要在递归调用返回后恢复这个对象的状态，这就是回溯的过程。
>
> 通过在递归调用前进行修改，在递归调用后恢复（即回溯），可以确保每次递归调用返回后，对象的状态是正确的，从而保证算法的正确性。



传递的参数如果是可变对象（如列表），它在内存中是共享的。虽然每个函数调用都有自己的栈帧，但栈帧中存储的只是指向可变对象的引用，而不是对象本身。因此，对可变对象的修改会影响到所有引用该对象的地方。

示例图式

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/202411012122382.png" alt="image-20241101212208890" style="zoom:50%;" />



## 4 递归进阶三部曲

递归进阶三部曲：斐波那且数列、汉诺塔，全排列。递归是dfs, dp的基础。



> 《算法笔记》第8章
>
> ## 深度优先搜索(DFS)
>
> 设想我们现在以第一视角身处一个巨大的迷宫当中，没有上帝视角，没有通信设施，更没有热血动漫里的奇迹，有的只是四周长得一样的墙壁。于是，我们只能自己想办法走出去。如果迷失了内心，随便乱走，那么很可能被四周完全相同的景色绕晕在其中，这时只能放弃所谓的侥幸，而去采取下面这种看上去很盲目但实际上会很有效的方法。
>
> 以当前所在位置为起点，沿着一条路向前走，当碰到岔道口时，选择其中一个岔路前进如果选择的这个岔路前方是一条死路，就退回到这个岔道口，选择另一个岔路前进。如果岔路中存在新的岔道口，那么仍然按上面的方法枚举新岔道口的每一条岔路。这样，只要迷宫存在出口，那么这个方法一定能够找到它。可能有读者会问，如果在第一个岔道口处选择了一条没有出路的分支，而这个分支比较深，并且路上多次出现新的岔道口，那么当发现这个分支是个死分支之后，如何退回到最初的这个岔道口?其实方法很简单，只要让右手始终贴着右边的墙壁一路往前走，那么自动会执行上面这个走法，并且最终一定能找到出口。图 8-1 即为使用这个方法走一个简单迷宫的示例。
>
> <img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231126163735204.png" alt="image-20231126163735204" style="zoom:50%;" />
>
> 
>
> 从图 8-1 可知，从起点开始前进，当碰到岔道口时，总是选择其中一条岔路前进(例如图中总是先选择最右手边的岔路)，在岔路上如果又遇到新的岔道口，仍然选择新岔道口的其中一条岔路前进，直到碰到死胡同才回退到最近的岔道口选择另一条岔路。也就是说，当碰到岔道口时，总是以“**深度**”作为前进的关键词，不碰到死胡同就不回头，因此把这种搜索的方式称为**深度优先搜索**(Depth First Search，**DFS**)。
> 从迷宫的例子还应该注意到，深度优先搜索会走遍所有路径，并且每次走到死胡同就代表一条完整路径的形成。这就是说，**深度优先搜索是一种枚举所有完整路径以遍历所有情况的搜索方法**。
>
> 
>
> 深度优先搜索 (DFS)可以使用栈来实现。但是实现起来却并不轻松，有没有既容易理解又容易实现的方法呢?有的——递归。现在从 DFS 的角度来看当初求解 Fibonacci 数列的过程。
> 回顾一下 Fibonacci数列的定义: $F(0)=1,F(1)=1,F(n)=F(n-1)+F(n-2)(n≥2)$。可以从这个定义中挖掘到，每当将 F(n)分为两部分 F(n-1)与 F(n-2)时，就可以把 F(n)看作迷宫的岔道口，由它可以到达两个新的关键结点 F(n-1)与 F(n-2)。而之后计算 F(n-1)时，又可以把 F(n-1)当作在岔道口 F(n)之下的岔道口。
> 既然有岔道口，那么一定有死胡同。很容易想象，当访问到 F(0)和 F(1)时，就无法再向下递归下去，因此 F(0)和 F(1)就是死胡同。这样说来，==递归中的递归式就是岔道口，而递归边界就是死胡同==，这样就可以把如何用递归实现深度优先搜索的过程理解得很清楚。为了使上面的过程更清晰，可以直接来分析递归图 (见图 4-3)：可以在递归图中看到，只要n > 1，F(n)就有两个分支，即把 F(n)当作岔道口；而当n为1或0时，F(1)与F(0)就是迷宫的死胡同，在此处程序就需要返回结果。这样当遍历完所有路径（从顶端的 F(4)到底层的所有 F(1)与 F(0)）后，就可以得到 F(4)的值。
>
> <img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231126164549437.png" alt="image-20231126164549437" style="zoom: 50%;" />
>
> 因此，使用递归可以很好地实现深度优先搜索。这个说法并不是说深度优先搜索就是递归，只能说递归是深度优先搜索的一种实现方式，因为使用非递归也是可以实现 DFS 的思想的，但是一般情况下会比递归麻烦。不过，使用递归时，系统会调用一个叫系统栈的东西来存放递归中每一层的状态，因此使用递归来实现 DFS 的本质其实还是栈。



### 4.1 递归序曲示例：sy115: 斐波拉契数列 简单

https://sunnywhy.com/sfbj/4/3/115

给定正整数n，求斐波那契数列的第n项F(n)。

令表示斐波那契数列的第n项，它的定义是：

当n=1时，F(n)=1；

当n=2时，F(n)=1；

当n>2时，F(n) = F(n-1) + F(n-2)。

大数据版：[斐波拉契数列-大数据版](https://sunnywhy.com/problem/893)

输入描述

一个正整数n（$1 \le n \le 25$）。

输出描述

斐波那契数列的第n项F(n)。

样例1

输入

```
1
```

输出

```
1
```

样例2

输入

```
3
```

输出

```
2
```

样例3

输入

```
5
```

输出

```
5
```



```python
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))
```



### 4.2 递归三部曲：汉诺塔

https://runestone.academy/ns/books/published/pythonds3/Recursion/TowerofHanoi.html?mode=browsing

The Tower of Hanoi puzzle was invented by the French mathematician Edouard Lucas in 1883. He was inspired by a legend that tells of a Hindu temple where the puzzle was presented to young priests. At the beginning of time, the priests were given three poles and a stack of 64 gold disks, each disk a little smaller than the one beneath it. Their assignment was to transfer all 64 disks from one of the three poles to another, with two important constraints. They could only move one disk at a time, and they could never place a larger disk on top of a smaller one. The priests worked very efficiently, day and night, moving one disk every second. When they finished their work, the legend said, the temple would crumble into dust and the world would vanish.

> 汉诺塔谜题是由法国数学家埃杜阿德·卢卡斯于1883年发明的。他受到一个传说的启发，这个传说讲述了一个印度寺庙中的年轻祭司被赋予了这个谜题。在时间的开端，祭司们得到了三根柱子和64个金盘，每个盘子都比它下面的一个稍微小一点。他们的任务是将这64个盘子从一根柱子移动到另一根柱子，但有两个重要的限制：每次只能移动一个盘子，并且不能将较大的盘子放在较小的盘子上面。祭司们非常高效地工作，日以继夜，每秒移动一个盘子。根据传说，当他们完成任务时，寺庙会化为尘土，世界也将消失。

Although the legend is interesting, you need not worry about the world ending any time soon. The number of moves required to correctly move a tower of 64 disks is $2^{64}−1=18,446,744,073,709,551,615$. At a rate of one move per second, that is 584,942,417,355 years! Clearly there is more to this puzzle than meets the eye.

> 虽然这个传说是有趣的，但你不必担心世界会在短时间内终结。正确移动64个盘子所需的步数是 　$2^{64}−1$。如果以每秒移动一次的速度来计算，那需要 $5.85×10^{11}$ 年！显然，这个谜题背后有更多的东西值得探索。

Figure 1 shows an example of a configuration of disks in the middle of a move from the first peg to the third. Notice that, as the rules specify, the disks on each peg are stacked so that smaller disks are always on top of the larger disks. If you have not tried to solve this puzzle before, you should try it now. You do not need fancy disks and poles–a pile of books or pieces of paper will work.

> 图1展示了在从第一根柱子移动到第三根柱子的过程中，盘子配置的一个例子。请注意，正如规则所指定的那样，每根柱子上的盘子都是按照较小的盘子始终在较大盘子之上的方式堆叠的。如果你以前没有尝试过解决这个谜题，你现在应该试试。你不需要精美的盘子和柱子——一堆书或几张纸就可以使用。

![image](https://raw.githubusercontent.com/GMyhf/img/main/img/hanoi-20231121121735301.png)

Figure 1: An Example Arrangement of Disks for the Tower of Hanoi

How do we go about solving this problem recursively? How would you go about solving this problem at all? What is our base case? Let’s think about this problem from the bottom up. Suppose you have a tower of five disks, originally on peg one. If you already knew how to move a tower of four disks to peg two, you could then easily move the bottom disk to peg three, and then move the tower of four from peg two to peg three. But what if you do not know how to move a tower of height four? Suppose that you knew how to move a tower of height three to peg three; then it would be easy to move the fourth disk to peg two and move the three from peg three on top of it. But what if you do not know how to move a tower of three? How about moving a tower of two disks to peg two and then moving the third disk to peg three, and then moving the tower of height two on top of it? But what if you still do not know how to do this? Surely you would agree that moving a single disk to peg three is easy enough, trivial you might even say. This sounds like a base case in the making.

> 我们如何递归地解决这个问题？你将如何着手解决这个问题？我们的基准情形是什么？让我们从底部开始思考这个问题。假设你有一个五层的塔，最初在柱子1上。如果你已经知道如何将四层的塔移动到柱子2上，那么你可以轻松地将最底层的盘子移动到柱子3上，然后再将四层的塔从柱子2移动到柱子3上。但如果你不知道如何移动四层的塔怎么办？假设你知道如何将三层的塔移动到柱子3上；那么很容易将第四层的盘子移动到柱子2上，并将三层的塔移到它上面。但如果你不知道如何移动三层的塔呢？如果将两层的塔移动到柱子2上，然后将第三层的盘子移动到柱子3上，再将两层的塔移到它上面呢？但如果你还是不知道怎么做呢？你肯定会同意，将一个单独的盘子移动到柱子3上是足够简单的，甚至可以说是微不足道的。这听起来像是一个基准情形。

Here is a high-level outline of how to move a tower from the starting pole, to the goal pole, using an intermediate pole:

1. Move a tower of height-1 to an intermediate pole, using the final pole.
2. Move the remaining disk to the final pole.
3. Move the tower of height-1 from the intermediate pole to the final pole using the original pole.

> 下面是一个高层次的概述，说明如何使用中间柱子将高度为 n*n* 的塔从起始柱子移动到目标柱子：
>
> 1. 通过目标柱子将高度为 n−1*n*−1 的塔从起始柱子移动到中间柱子。
> 2. 将剩余的一个盘子从起始柱子移动到最终柱子。
> 3. 通过起始柱子将高度为 n−1*n*−1 的塔从中间柱子移动到目标柱子。

As long as we always obey the rule that the larger disks remain on the bottom of the stack, we can use the three steps above recursively, treating any larger disks as though they were not even there. The only thing missing from the outline above is the identification of a base case. The simplest Tower of Hanoi problem is a tower of one disk. In this case, we need move only a single disk to its final destination. A tower of one disk will be our base case. In addition, the steps outlined above move us toward the base case by reducing the height of the tower in steps 1 and 3. Listing 1 shows the Python code to solve the Tower of Hanoi puzzle.

> 只要我们始终遵守较大的盘子保持在栈底的规则，我们可以使用上述三个步骤进行递归处理，就好像较大的盘子不存在一样。上述概述中唯一缺少的是基准情形的识别。最简单的汉诺塔问题是只有一个盘子的塔。在这种情况下，我们只需要将单个盘子移动到它的最终目的地。一个盘子的塔将作为我们的基准情形。此外，上述步骤通过在第1步和第3步中减少塔的高度，使我们逐步接近基准情形。清单1展示了用Python代码解决汉诺塔谜题的方法。

**Listing 1**

```python
def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole) #Recursive call
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole) #Recursive call
```

Notice that the code in Listing 1 is almost identical to the English description. The key to the simplicity of the algorithm is that we make two different recursive calls, one on line 3 and a second on line 5. On line 3 we move all but the bottom disk on the initial tower to an intermediate pole. The next line simply moves the bottom disk to its final resting place. Then on line 5 we move the tower from the intermediate pole to the top of the largest disk. The base case is detected when the tower height is 0; in this case there is nothing to do, so the `moveTower` function simply returns. The important thing to remember about handling the base case this way is that simply returning from `moveTower` is what finally allows the `moveDisk` function to be called.

> 请注意，清单1中的代码几乎与英文描述完全相同。算法简单性的关键在于我们进行了两次不同的递归调用，一次在第3行，另一次在第5行。在第3行，我们将初始塔上除了最底层盘子以外的所有盘子移动到中间柱子上。下一行则简单地将最底层的盘子移动到它的最终位置。然后在第5行，我们将中间柱子上的塔移动到最大盘子的顶部。当塔的高度为0时，检测到基准情形；在这种情况下，没有什么需要做的，所以 `moveTower` 函数直接返回。以这种方式处理基准情形的重要之处在于，仅仅是返回 `moveTower` 函数就最终允许了 `moveDisk` 函数被调用。

The function `moveDisk`, shown in Listing 2, is very simple. All it does is print out that it is moving a disk from one pole to another. If you type in and run the `moveTower` program you can see that it gives you a very efficient solution to the puzzle.

> 清单2中显示的 `moveDisk` 函数非常简单。它所做的只是打印出从一根柱子移动一个盘子到另一根柱子的信息。如果你输入并运行 `moveTower` 程序，你会看到它为你提供了谜题的一个非常高效的解决方案。

**Listing 2**

```python
def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)
```

The program in ActiveCode 1 provides the entire solution for three disks.

```python
#Simulation of the tower of hanoi.

def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole) #Recursive call
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole) #Recursive call

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)


moveTower(3,"A","B","C")

```

Activity: 5.10.2 Solving Tower of Hanoi Recursively Python (hanoipy)

Now that you have seen the code for both `moveTower` and `moveDisk`, you may be wondering why we do not have a data structure that explicitly keeps track of what disks are on what poles. Here is a hint: if you were going to explicitly keep track of the disks, you would probably use three `Stack` objects, one for each pole. The answer is that Python provides the stacks that we need implicitly through the call stack.

> 现在你已经看到了 `moveTower` 和 `moveDisk` 的代码，你可能会想知道为什么我们没有一个显式的数据结构来跟踪每个柱子上有哪些盘子。这里有一个提示：如果你打算显式地跟踪这些盘子，你可能会使用三个 `Stack` 对象，每个柱子一个。答案是 Python 通过调用栈隐式地提供了我们需要的栈。



#### 示例: 04147汉诺塔问题(Tower of Hanoi)

http://cs101.openjudge.cn/practice/04147

一、汉诺塔问题 

 有三根杆子A，B，C。A杆上有N个(N>1)穿孔圆盘，盘的尺寸由下到上依次变小。要求按下列规则将所有圆盘移至C杆： 每次只能移动一个圆盘； 大盘不能叠在小盘上面。 提示：可将圆盘临时置于B杆，也可将从A杆移出的圆盘重新移回A杆，但都必须遵循上述两条规则。 

 问：如何移？最少要移动多少次？

汉诺塔示意图如下：

![img](https://raw.githubusercontent.com/GMyhf/img/main/img/1429931663.jpg)

三个盘的移动：

![img](https://raw.githubusercontent.com/GMyhf/img/main/img/1429933148.gif)



二、故事由来 

法国数学家爱德华·卢卡斯曾编写过一个印度的古老传说：在世界中心贝拿勒斯（在印度北部）的圣庙里，一块黄铜板上插着三根宝石针。印度教的主神梵天在创造世界的时候，在其中一根针上从下到上地穿好了由大到小的64片金片，这就是所谓的汉诺塔。不论白天黑夜，总有一个僧侣在按照下面的法则移动这些金片：一次只移动一片，不管在哪根针上，小片必须在大片上面。僧侣们预言，当所有的金片都从梵天穿好的那根针上移到另外一根针上时，世界就将在一声霹雳中消灭，而梵塔、庙宇和众生也都将同归于尽。 

不管这个传说的可信度有多大，如果考虑一下把64片金片，由一根针上移到另一根针上，并且始终保持上小下大的顺序。这需要多少次移动呢?这里需要递归的方法。假设有n片，移动次数是f(n).显然f(1)=1,f(2)=3,f(3)=7，且f(k+1)=2*f(k)+1。此后不难证明f(n)=2^n-1。n=64时， 假如每秒钟一次，共需多长时间呢？一个平年365天有31536000 秒，闰年366天有31622400秒，平均每年31556952秒，计算一下： 18446744073709551615秒 这表明移完这些金片需要5845.54亿年以上，而地球存在至今不过45亿年，太阳系的预期寿命据说也就是数百亿年。真的过了5845.54亿年，不说太阳系和银河系，至少地球上的一切生命，连同梵塔、庙宇等，都早已经灰飞烟灭。

三、解法 

解法的基本思想是递归。假设有A、B、C三个塔，A塔有N块盘，目标是把这些盘全部移到C塔。那么先把A塔顶部的N-1块盘移动到B塔，再把A塔剩下的大盘移到C，最后把B塔的N-1块盘移到C。 每次移动多于一块盘时，则再次使用上述算法来移动。

**输入**

输入为一个整数后面跟三个单字符字符串。
整数为盘子的数目，后三个字符表示三个杆子的编号。

**输出**

输出每一步移动盘子的记录。一次移动一行。
每次移动的记录为例如3:a->b 的形式，即把编号为3的盘子从a杆移至b杆。
我们约定圆盘从小到大编号为1, 2, ...n。即最上面那个最小的圆盘编号为1，最下面最大的圆盘编号为n。

样例输入

```
3 a b c
```

样例输出

```
1:a->c
2:a->b
1:c->b
3:a->c
1:b->a
2:b->c
1:a->c
```

提示

可参考如下网址：
https://www.mathsisfun.com/games/towerofhanoi.html
http://blog.csdn.net/geekwangminli/article/details/7981570
http://www.cnblogs.com/yanlingyin/archive/2011/11/14/2247594.html

来源：重庆科技学院 WJQ



```python
# https://blog.csdn.net/geekwangminli/article/details/7981570

# 将编号为numdisk的盘子从init杆移至desti杆 
def moveOne(numDisk : int, init : str, desti : str):
    print("{}:{}->{}".format(numDisk, init, desti))

#将numDisks个盘子从init杆借助temp杆移至desti杆
def move(numDisks : int, init : str, temp : str, desti : str):
    if numDisks == 1:
        moveOne(1, init, desti)
    else: 
        # 首先将上面的（numDisk-1）个盘子从init杆借助desti杆移至temp杆
        move(numDisks-1, init, desti, temp) 
        
        # 然后将编号为numDisks的盘子从init杆移至desti杆
        moveOne(numDisks, init, desti)
        
        # 最后将上面的（numDisks-1）个盘子从temp杆借助init杆移至desti杆 
        move(numDisks-1, temp, init, desti)

n, a, b, c = input().split()
move(int(n), a, b, c)
```





#### 练习: 01958Strange Towers of Hanoi（选做）

http://cs101.openjudge.cn/practice/01958/

Charlie Darkbrown sits in another one of those boring Computer Science lessons: At the moment the teacher just explains the standard Tower of Hanoi problem, which bores Charlie to death!

![img](https://raw.githubusercontent.com/GMyhf/img/main/img/1958_1.jpg)

The teacher points to the blackboard (Fig. 4) and says: "So here is the problem:

- There are three towers: A, B and C.
- There are n disks. The number n is constant while working the puzzle.
- All disks are different in size.
- The disks are initially stacked on tower A increasing in size from the top to the bottom.
- The goal of the puzzle is to transfer all of the disks from tower A to tower C.
- One disk at a time can be moved from the top of a tower either to an empty tower or to a tower with a larger disk on the top.

So your task is to write a program that calculates the smallest number of disk moves necessary to move all the disks from tower A to C."
Charlie: "This is incredibly boring—everybody knows that this can be solved using a simple recursion.I deny to code something as simple as this!"
The teacher sighs: "Well, Charlie, let's think about something for you to do: For you there is a fourth tower D. Calculate the smallest number of disk moves to move all the disks from tower A to tower D using all four towers."
Charlie looks irritated: "Urgh. . . Well, I don't know an optimal algorithm for four towers. . . "
**Problem**
So the real problem is that problem solving does not belong to the things Charlie is good at. Actually, the only thing Charlie is really good at is "sitting next to someone who can do the job". And now guess what — exactly! It is you who is sitting next to Charlie, and he is already glaring at you.
Luckily, you know that the following algorithm works for n <= 12: At first k >= 1 disks on tower A are fixed and the remaining n-k disks are moved from tower A to tower B using the algorithm for four towers.Then the remaining k disks from tower A are moved to tower D using the algorithm for three towers. At last the n - k disks from tower B are moved to tower D again using the algorithm for four towers (and thereby not moving any of the k disks already on tower D). Do this for all k 2 ∈{1, .... , n} and find the k with the minimal number of moves.
So for n = 3 and k = 2 you would first move 1 (3-2) disk from tower A to tower B using the algorithm for four towers (one move). Then you would move the remaining two disks from tower A to tower D using the algorithm for three towers (three moves). And the last step would be to move the disk from tower B to tower D using again the algorithm for four towers (another move). Thus the solution for n = 3 and k = 2 is 5 moves. To be sure that this really is the best solution for n = 3 you need to check the other possible values 1 and 3 for k. (But, by the way, 5 is optimal. . . )

输入

There is no input.

输出

For each n (1 <= n <= 12) print a single line containing the minimum number of moves to solve the problem for four towers and n disks.

样例输入

```
No input.
```

样例输出

```
REFER TO OUTPUT.
```

来源

TUD Programming Contest 2002, Darmstadt, Germany



《短码之美》2007年，184页

汉诺塔，大家知道吗?汉诺塔由 3根柱子、大小不同的空心圆盘组成。所有圆盘最初都放在最左边的柱子上。圆盘的摆放规则是上面的圆盘必须小于下面的圆盘。把这些圆盘一个一个都移动到最右边的柱子上，如果圆盘的个数是 n，大家都知道一般需要移动 (2^n^-1)次。比如，n=3的时候，



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231030193822757.png" alt="image-20231030193822757" style="zoom:50%;" />



的确是用了 2^3^-1=7 次完成了移动。那么，这次的问题不是基本的汉诺塔，而是把柱子的根数增加1根。如果柱子增加到 4根，原来需要移动 7次完成，现在只需要 5次就可以了。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231030194009343.png" alt="image-20231030194009343" style="zoom:50%;" />

如果增加圆盘个数，就应该能省下更多的步数，但是这个规则还不是很清楚。题面要求编写程序计算 4根柱子的时候，1~12 个盘子所需的最小移动次数。



有 4根柱子的时候，可以利用2根空的柱子移动圆盘，圆盘数 n是 1、2、3的时候只需顺序移动，所以各需要 1、3、5次移动。4个圆盘以上:
(1)首先移动其中的几个盘子;
(2)把剩余的圆盘移动到指定的位置;
(3)把(1)的圆盘移动到(2)的上面。
这个时候，(1)和(3)可以有 2 根空柱子可以使用，所以可以互换，但是(2)的时候只有一根空柱子。也就是说移动所需的步数与一般汉诺塔 (3 根柱子)相同。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231030194457296.png" alt="image-20231030194457296" style="zoom:50%;" />





具体地用 4个圆盘来考虑一下，如下图所示。4个圆盘的时候，①可移动2个圆盘 (3步)，②可移动2个圆盘 (3步)，③再移动2个圆盘 (3步)，总共最少需要 9步。如果①移动3个的时候，则需要 5步，②只移动一个需要 1步，③再移动3 个需要 5步，总共需要 11 步，不是最小的移动步数。但是，①只移动1个的话需要 1步，②只移动3个需7步，③再移动 1个需要1步，总共需要 9步，这才是最小步数。==在什么情况下移动步数最小不太容易看出来==，所以要像这样把 n个圆盘分成k个和 (n-k) 个来检查移动步数，找出最小移动步数的移法。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231030195445757.png" alt="image-20231030195445757" style="zoom:50%;" />

圆盘个数增加后需要增加移动步数，如果每次都计算将是很庞大的计算量，所以需要使用DP(Dynamic Programming，动态规划法)求解。

```python
d = [0] * 15
f = [float('inf')] * 15

d[1] = 1
for i in range(2, 13):
    d[i] = d[i - 1] * 2 + 1

f[1] = 1
for i in range(2, 13):
    for j in range(1, i):
        f[i] = min(f[i], f[i - j] * 2 + d[j])

for i in range(1, 13):
    print(f[i])
```



```python
# 23n2300011072，蒋子轩
def hanoi_four_towers(n, source, target, auxiliary1, auxiliary2):
    if n == 0:
        return 0
    if n == 1:
        return 1
    min_moves = float('inf')
    for k in range(1, n):
        three_tower_moves = 2**(n-k)-1
        moves = hanoi_four_towers(k, source, auxiliary1, auxiliary2, target) +\
            three_tower_moves +\
            hanoi_four_towers(k, auxiliary1, target, source, auxiliary2)
        min_moves = min(min_moves, moves)
    return min_moves


for n in range(1, 13):
    print(hanoi_four_towers(n, 'A','D','B','C'))
```



POJ - 1958 Strange Towers of Hanoi 汉诺塔递推问题（4塔），

https://blog.csdn.net/qq_45432665/article/details/104825847

思路：我们先将3塔的情况递推出来，用d[i] 表示有i个盘的时候的最小移动次数，d[1] = 1



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231030200714441.png" alt="image-20231030200714441" style="zoom:50%;" />

当有4塔时，也是一样的思路，f[1] = 1

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231030200853087.png" alt="image-20231030200853087" style="zoom:50%;" />





4 柱汉诺塔游戏是否已经解决了？

https://www.zhihu.com/question/54353032

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231030201742852.png" alt="image-20231030201742852" style="zoom: 50%;" />



### 4.3 递归三部曲：全排列

#### 示例sy132: 全排列I 中等

https://sunnywhy.com/sfbj/4/3/132

给定一个正整数n，假设序列S=[1,2,3,...,n]，求S的全排列。

**输入描述**

一个正整数n（$1 \le n \le 8$）。

**输出描述**

每个全排列一行，输出所有全排列。

输出顺序为：两个全排列A和B，若满足前k-1项对应相同，但有Ak < Bk，那么将全排列Ak优先输出（例如[1,2,3]比[1,3,2]优先输出）。

在输出时，全排列中的每个数之间用一个空格隔开，行末不允许有多余的空格。不允许出现相同的全排列。

样例1

输入

```
1
```

输出

```
1
```

样例2

输入

```
2
```

输出

```
1 2
2 1
```

样例3

输入

```
3
```

输出

```
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
```





```python
maxn = 11
hashTable = [False] * maxn  # 当整数i已经在数组 P中时为 true

#@recviz
def increasing_permutaions(n, prefix=[]):
    if len(prefix) == n:  # 递归边界，已经处理完排列的1~位
        return [prefix]

    result = []
    for i in range(1, n + 1):
        if hashTable[i]:
            continue

        hashTable[i] = True  # 记i已在prefix中
        # 把i加入当前排列，处理排列的后续号位
        result += increasing_permutaions(n, prefix + [i])
        hashTable[i] = False  # 处理完为i的子问题，还原状态

    return result


n = int(input())
result = increasing_permutaions(n)
for r in result:
    print(' '.join(map(str,r)))
```





## 5. 计算机原理（2/3）：虚拟地址空间

三大计算机原理之一，@Book_my_flight_v0.3.md

​	计算机的基础架构自从 20 世纪 40 年代起就已经形成规范，包括处理器、存储指令和数据的内存、输入和输出设备。它通常叫作冯·诺依曼架构，以约翰·冯·诺依曼（德語：John Von Neumann，1903 年12 月 28 日－1957 年 2 月 8 日）的名字来命名，他在 1946 年发表的论文里描述了这一架构。论文的开头句，用现在的专门术语来说就是，CPU提供算法和控制，而 RAM 和磁盘则是记忆存储，键盘、鼠标和显示器与操作人员交互。其中需要重点理解的是与存储相关的进程的虚拟地址空间。

​	在《深入理解计算机系统》[8]第一章中讲到了进程的虚拟地址空间。虚拟存储器是一个抽象概念，它为每个进程提供了一个假象，好像每个进程都在独占地使用主存。每个进程看到的存储器都是一致的，称之为虚拟地址空间。如图1-15所示的是 Linux 进程的虚拟地址空间（其他 Unix 系统的设计与此类似）。在 Linux 中，最上面的四分之一的地址空间是预留给操作系统中的代码和数据的，这对所有进程都一样。底部的四分之三的地址空间用来存放用户进程定义的代码和数据。请注意，图中的地址是从下往上增大的。



![image-20230109195232404](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230109195232404.png)

图1-15 进程的虚拟地址空间（Process virtual address space）（注：图片来源为 Randal Bryant[8]，2015年3月）



​	每个进程看到的虚拟地址空间由准确定义的区（area）构成，每个区都有专门的功能。简单看下每一个区，从最低的地址开始，逐步向上研究。

- 程序代码和数据（code and data）。代码是从同一固定地址开始，紧接着的是和全局变量相对应的数据区。代码和数据区是由可执行目标文件直接初始化的，示例中就是可执行文件hello。

- 堆（heap）。紧随代码和数据区之后的是运行时堆（Run-time heap）。代码和数据区是在进程一旦开始运行时就被指定了大小的，与此不同，作为调用像 malloc 和 free 这样的 C 标准库函数的结果，堆可以在运行时动态地扩展和收缩。

- 共享库（shared libraries）。在地址空间的中间附近是一块用来存放像标准库和数学库这样共享库的代码和数据的区域。共享库的概念非常强大。

- 栈（stack）。位于用户虚拟地址空间顶部的是用户栈，编译器用它来实现函数调用。和堆一样，用户栈（User stack）在程序执行期间可以动态地扩展和收缩。特别地，每次我们调用一个函数时，栈就会增长。每次我们从函数返回时，栈就会收缩。

- 内核虚拟存储器（kernal virtal memory）。内核是操作系统总是驻留在存储器中的部分。地址空间顶部是为内核预留的。应用程序不允许读写这个区域的内容或者直接调用内核代码定义的函数。

​	虚拟存储器的运作需要硬件和操作系统软件间的精密复杂的互相合作，包括对处理器生成的每个地址的硬件翻译。基本思想是把一个进程虚拟存储器的内容存储在磁盘上，然后用主存作为磁盘的高速缓存。





## 6.编程题目

### 练习28717: 递归比较字符串大小

http://wjjc.openjudge.cn/2024jgc4/002/

程序填空，完成按奇异规则比较字符串大小的递归函数strCmp(a,b)，返回值为True或False，表示a是否小于b

不可使用循环，只能使用递归

字符串按奇异规则比较大小，就是逐个字符比较大小直到分出胜负。两个字符比较大小的规则是哪个字符的编码和字母'k'的编码的差的绝对值小，哪个字符就算小。这样两个不同字符可能也算一样大

字符串很短，不用考虑效率问题

 

 

```
def strCmp(a,b) :
	if a == "" and b != "":
		return True
	elif a != "" and b == "":
		return False
	elif a == "" and b == "":
		return False
	else :
		if abs(ord(a[0]) - ord('k')) < abs(ord(b[0]) - ord('k')):#abs是求绝对值的函数
			return True
// 在此处补充你的代码
#填空


n = int(input())
for _ in range(n):
	s1,s2 = input().split()
	if strCmp(s1,s2):
		print("YES")
	else:
		print("NO")
```

输入

第一行是整数n，表示接下来有n对字符串
接下来有n行，每行有用空格分隔的两个字符串，字符串由小写英文字母组成

输出

对没对字符串，如果第一个小于第二个，输出YES，否则输出NO

样例输入

```
4
ebc eab
ac acd
kk ki
abc abc
```

样例输出

```
YES
YES
YES
NO
```

来源

Guo Wei



```python
def strCmp(a, b):
    if a == "" and b != "":
        return True
    elif a != "" and b == "":
        return False
    elif a == "" and b == "":
        return False
    else:
        if abs(ord(a[0]) - ord('k')) < abs(ord(b[0]) - ord('k')):
            return True
        elif abs(ord(a[0]) - ord('k')) > abs(ord(b[0]) - ord('k')):
            return False
        else:
            return strCmp(a[1:], b[1:])

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        s1, s2 = input().split()
        if strCmp(s1, s2):
            print("YES")
        else:
            print("NO")
```





### 练习01661: Help Jimmy（选做）

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



### 练习02386: Lake Counting

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



### 练习05585: 晶矿的个数

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



### 练习02786: Pell数列

dp, http://cs101.openjudge.cn/practice/02786/

Pell数列a1, a2, a3, ...的定义是这样的，a1 = 1, a2 = 2, ... , an = 2 * an − 1 + an - 2 (n > 2)。
给出一个正整数k，要求Pell数列的第k项模上32767是多少。

**输入**

第1行是测试数据的组数n，后面跟着n行输入。每组测试数据占1行，包括一个正整数k (1 ≤ k < 1000000)。

**输出**

n行，每行输出对应一个输入。输出应是一个非负整数。

样例输入

```
2
1
8
```

样例输出

```
1
408
```





```python
#2300011786 裘思远
from functools import lru_cache

@lru_cache(maxsize=None)
def series(n):
    if n>2:
        return (series(n-1)*2+series(n-2))%32767
    elif n==2:
        return 2
    else:
        return 1

n=int(input())
for _ in range(n):
    k=int(input())%150
    ans=series(k)
    print(ans)
```



### 练习02754: 八皇后

dfs and similar, http://cs101.openjudge.cn/practice/02754

描述：会下国际象棋的人都很清楚：皇后可以在横、竖、斜线上不限步数地吃掉其他棋子。如何将8个皇后放在棋盘上（有8 * 8个方格），使它们谁也不能被吃掉！这就是著名的八皇后问题。
		对于某个满足要求的8皇后的摆放方法，定义一个皇后串a与之对应，即$a=b_1b_2...b_8~$,其中$b_i$为相应摆法中第i行皇后所处的列数。已经知道8皇后问题一共有92组解（即92个不同的皇后串）。
		给出一个数b，要求输出第b个串。串的比较是这样的：皇后串x置于皇后串y之前，当且仅当将x视为整数时比y小。

​	八皇后是一个古老的经典问题：**如何在一张国际象棋的棋盘上，摆放8个皇后，使其任意两个皇后互相不受攻击。**该问题由一位德国**国际象棋排局家** **Max Bezzel** 于 1848年提出。严格来说，那个年代，还没有“德国”这个国家，彼时称作“普鲁士”。1850年，**Franz Nauck** 给出了第一个解，并将其扩展成了“ **n皇后** ”问题，即**在一张 n** x **n 的棋盘上，如何摆放 n 个皇后，使其两两互不攻击**。历史上，八皇后问题曾惊动过“数学王子”高斯(Gauss)，而且正是 Franz Nauck 写信找高斯请教的。

**输入**

第1行是测试数据的组数n，后面跟着n行输入。每组测试数据占1行，包括一个正整数b(1 ≤  b ≤  92)

**输出**

输出有n行，每行输出对应一个输入。输出应是一个正整数，是对应于b的皇后串。

样例输入

```
2
1
92
```

样例输出

```
15863724
84136275
```



这里在记录解的时候，不能直接引用数组，否则最终解集中的解都是重复的，要进行拷贝，另外开辟出一个数组空间用解集记录。

```python
ans = []
def queen_dfs(A, cur=0):          #考虑放第cur行的皇后
    if cur == len(A):             #如果已经放了n个皇后，一组新的解产生了
        ans.append(''.join([str(x+1) for x in A])) #注意避免浅拷贝
        return 
    
    for col in range(len(A)):     #将当前皇后逐一放置在不同的列，每列对应一组解
        for row in range(cur):    #逐一判定，与前面的皇后是否冲突
            #因为预先确定所有皇后一定不在同一行，所以只需要检查是否同列，或者在同一斜线上
            if A[row] == col or abs(col - A[row]) == cur - row:
                break
        else:                     #若都不冲突
            A[cur] = col          #放置新皇后，在cur行，col列
            queen_dfs(A, cur+1)	  #对下一个皇后位置进行递归
            
queen_dfs([None]*8)   
for _ in range(int(input())):
    print(ans[int(input()) - 1])
```



![image-20231205002333349](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231205002333349.png)





# 三、递归优化和可视化

## 1 递归程序优化两板斧

递归程序在处理大规模问题时经常会遇到两个主要问题：**递归深度限制** 和 **重复计算子问题**。这两个问题可以通过以下两种方法来解决：

**增加递归深度限制**：使用 `sys.setrecursionlimit` 来增加 Python 的递归深度限制。

**缓存中间结果**：使用 `functools.lru_cache` 或其他形式的 memoization（记忆化）来避免重复计算。



Python 默认的递归深度限制是 1000，对于某些问题来说可能不够。你可以通过 `sys.setrecursionlimit` 来增加这个限制。

```python
import sys
sys.setrecursionlimit(1 << 30)  # 将递归深度限制设置为 2^30
```



使用 `functools.lru_cache` 可以缓存函数的返回值，从而避免重复计算相同的子问题。这对于递归算法尤其有用，可以显著提高性能。

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def recursive_function(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return recursive_function(n - 1) + recursive_function(n - 2)
```

### 示例：斐波那契数列

下面是一个具体的示例，展示了如何使用这两板斧来解决斐波那契数列的问题。

**没有优化的递归实现**

```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 测试
print(fibonacci(35))  # 这将非常慢，甚至可能导致栈溢出
```

**使用 `sys.setrecursionlimit` 和 `lru_cache` 优化后的递归实现**

```python
import sys
from functools import lru_cache

# 设置递归深度限制
sys.setrecursionlimit(1 << 30)

# 使用 lru_cache 缓存中间结果
@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 测试
print(fibonacci(35))  # 现在会非常快
```

> **详细解释**
>
> 1. **增加递归深度限制**：
>
>    ```python
>    import sys
>    sys.setrecursionlimit(1 << 30)
>    ```
>
>    这行代码将递归深度限制设置为 $2^{30}$，足够应对大多数递归问题。
>
> 2. **使用 `lru_cache` 缓存中间结果**：
>
>    ```python
>    from functools import lru_cache
>                            
>    @lru_cache(maxsize=None)
>    def fibonacci(n):
>        if n == 0:
>            return 0
>        elif n == 1:
>            return 1
>        else:
>            return fibonacci(n - 1) + fibonacci(n - 2)
>    ```
>
>    `@lru_cache(maxsize=None)` 装饰器会自动缓存 `fibonacci` 函数的结果，避免重复计算相同的子问题。`maxsize=None` 表示没有缓存大小限制。
>
> **注意事项**
>
> - **内存使用**：虽然 `lru_cache` 可以显著提高性能，但需要注意它会占用额外的内存来存储缓存结果。对于非常大的输入，可能会导致内存不足。
> - **递归深度**：即使增加了递归深度限制，递归调用仍然有可能导致栈溢出。如果递归层数非常深，考虑使用迭代方法或其他非递归算法。



### 示例21760: 递归复习法

http://wjjc.openjudge.cn/2024jgc5/002/

据说，学渣复习期末考试，要用递归复习法，即当他复习知识点A的时候，他发现理解知识点A必须先理解知识点B和知识点C，于是他先去学习知识点B和知识点C，当他复习知识点B的时候，又发现理解知识点B必须先理解知识点D与知识点E，又得先去复习知识点D和知识点E。

现在学渣小明正在通过递归复习法复习知识点n。对任意知识点1 <= k <= n，他复习这个知识点本身需要k小时的时间。但是，小明对这些知识点非常不熟悉，以至于他对任意知识点k， 3 <= k <= n，都必须先复习知识点k - 1和k - 2才能复习知识点k；在复习知识点k - 1的时候，又得先复习知识点k - 2和k - 3才能复习知识点k - 1；以此类推……。注意，即使在复习知识点k - 1的时候他已经复习过了知识点k - 2，在复习知识点k之前他已经忘掉了知识点k - 2，因此他还是会再复习一遍知识点k - 2，并重复上述的递归过程完成新的一轮k - 2的复习后，才会复习知识点k。

现在请问他一共需要多少个小时才能完成知识点n的复习？

输入

第一行是一个整数m，代表数据组数，1 <= m <= 25
之后m行，每行是一组数据，即一个整数n，1 <= n <= 25

输出

对每组数据，输出小明复习知识点n所需要的时间

样例输入

```
9
1
2
3
5
7
9
15
20
25
```

样例输出

```
1
2
6
23
71
200
3786
42164
467833
```

提示

第一个输入n=1，需要复习一个小时。

第二个输入n=3，此时他需要先复习知识点1和知识点2，再复习知识点3，需要复习1+2+3=6个小时。

第三个输入n=5，此时他为了复习知识点5，必须先复习知识点3与知识点4。之前已知复习知识点3需要6个小时。复习知识点4前需要再复习知识点3与知识点2，加上复习知识点4本身的时间，共需要2+6+4=12个小时。因此，复习知识点5共需要6+12+5=23小时。

来源

何昊高洁



```python
def study_time(n, memo):
    if n == 1 or n == 2:
        return n
    if n in memo:
        return memo[n]
    memo[n] = n + study_time(n - 1, memo) + study_time(n - 2, memo)
    return memo[n]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    m = int(data[0])
    results = []
    memo = {}

    for i in range(1, m + 1):
        n = int(data[i])
        results.append(study_time(n, memo))

    for result in results:
        print(result)
```



利用 Python 的 functools.lru_cache 装饰器来自动处理缓存。这样可以简化代码，并且避免手动管理 memo 字典。

```python
from functools import lru_cache
import sys

@lru_cache(maxsize=None)
def study_time(n):
    if n == 1 or n == 2:
        return n
    return n + study_time(n - 1) + study_time(n - 2)

if __name__ == "__main__":
    # 读取所有输入数据
    input_data = sys.stdin.read().strip()
    data = input_data.split()

    m = int(data[0])
    results = []

    for i in range(1, m + 1):
        n = int(data[i])
        results.append(study_time(n))

    for result in results:
        print(result)
```



## 2 递归可视化

方法1：程序在 http://pythontutor.com 中运行，直接可视化。

### 示例：归并排序

递归程序运行过程，不容易理解。https://pythontutor.com，完美展示 归并排序 的递归过程。

![image-20241021221131586](https://raw.githubusercontent.com/GMyhf/img/main/img/202410212211019.png)





方法2：在输出的调试信息前先输出一些和递归深度相关的数量的空格，可以看出递归的层级。

### 示例sy127: 递归调试 

https://sunnywhy.com/sfbj/4/3/127

斐波那契数列的定义：

```text
令F(n)表示斐波那契数列的第n项，则：
当n=1时，F(n)=1；
当n=2时，F(n)=1；
当n>2时，F(n)=F(n-1)+F(n-2)。
```

下面是斐波那契数列问题的递归实现方式的伪代码：

```text
F(n) {
    输出调试信息;
    if (n <= 2) {
        return 1;
    } else {
        return F(n - 1) + F(n - 2);
    }
}
```

递归代码的调试往往会很头疼，一个很重要的原因是在递归代码中输出的信息会因为多层而混在一起。但如果我们能在输出的调试信息前先输出一些和递归深度相关的数量的空格，就可以看出递归的层级，方便我们调试。例如当递归深度为1时先输出0个空格，递归深度为2时先输出4个空格，递归深度为3时先输出8个空格，以此类推，递归深度每多1，空格的个数就多4个）。

**输入描述**

一个正整数n（$2 \le n \le 12$）。

**输出描述**

按题目描述的方式，每行输出调试信息，格式如下：

```text
[与递归深度相关的一堆空格]n=具体值
```

样例1

输入

```
1
```

输出

```
n=1
```

样例2

输入

```
2
```

输出

```
n=2
```

样例3

输入

```
3
```

输出

```
n=3
    n=2
    n=1
```

样例4

输入

```
4
```

输出

```
n=4
    n=3
        n=2
        n=1
    n=2
```

样例5

输入

```
5
```

输出

```
n=5
    n=4
        n=3
            n=2
            n=1
        n=2
    n=3
        n=2
        n=1
```



```python
def F(n, depth=0):
    depth += 1
    blank = ' ' * 4 * (depth-1)
    print(f"{blank}n={n}")
    if n <= 2:
        return 1
    else:
        return F(n-1, depth) + F(n-2, depth)

n = int(input())
if n == 1 or n == 2:
    print(f'n={n}')
else:
    F(n)
```





方法3：用recviz包

`recviz` 是一个用于 Python 的可视化递归调用的库。它可以帮助初学者更好的理解递归，实际开发中不会用这个库。

`recviz` 需要另外安装。



### 示例：dfs生成排列

```python
from recviz import recviz


maxn = 11
hashTable = [False]*maxn  # 当整数i已经在数组 P中时为 true

@recviz
def increasing_permutaions(n, prefix=[]):
    if len(prefix) == n:  # 递归边界，已经处理完排列的1~位
        return [prefix]
    
    result = []
    for i in range(1, n+1):
        if hashTable[i]:
            continue
        
        hashTable[i] = True  #记i已在prefix中
        # 把i加入当前排列，处理排列的后续号位
        result += increasing_permutaions(n, prefix+[i]) 
        hashTable[i] = False #处理完为i的子问题，还原状态
        
    return result


n = int(input())
result = increasing_permutaions(n)
for r in result:
    print(r)
```



![image-20231128135735294](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231128135735294.png)





## 3 yield生成器

### 示例sy132: 全排列

https://sunnywhy.com/sfbj/4/3/132

给定一个正整数n，假设序列S=[1,2,3,...,n]，求S的全排列。





```python
n = int(input())
l = []
for i in range(1,n+1):
    l.append(f'{i}')

def arrange(l):
    if len(l) == 1:
    """
    当列表中只有一个元素时，使用yield关键字返回这个元素。这里使用了生成器，而不是直接返回（return）值，这意味着函数可以暂停执行并在需要时恢复，这对于处理大量数据或递归调用非常有用。
    """
        yield l[0]
    else:
        for i in range(len(l)):
            new_l = l[:i] + l[i+1:]
            for rest in arrange(new_l):
                yield l[i] + ' ' + rest

for ans in arrange(l):
    print(ans)
```

> `yield` 是 Python 中用于定义生成器函数的关键字。生成器是一种特殊的迭代器，它允许你在函数内部逐步生成值，而不是一次性生成所有值并将它们存储在内存中。当你在函数中使用 `yield` 语句时，这个函数就变成了一个生成器。当调用生成器函数时，它不会立即执行函数体内的代码，而是返回一个生成器对象。只有当这个生成器对象被迭代时，才会执行函数体内的代码，直到遇到 `yield` 语句，此时函数会暂停执行，并返回 `yield` 后面的表达式的值。当再次迭代生成器时，函数会从上次暂停的地方继续执行，直到遇到下一个 `yield` 语句，依此类推，直到函数执行完毕。
>
> **`yield` 与 `return` 的区别**
>
> - **执行时机**：当函数中使用 `return` 时，函数会立即终止执行，并返回一个值；而使用 `yield` 时，函数会生成一个生成器对象，该对象可以在需要时逐步产生值。
> - **内存占用**：`return` 需要一次性计算并返回所有的值，如果这些值的数量很大，可能会消耗大量的内存。相比之下，`yield` 可以按需生成值，因此更加节省内存。
> - **可迭代性**：使用 `return` 的函数只能返回一次值，而使用 `yield` 的生成器可以多次产生值，使得生成器可以用于迭代。
> - **状态保持**：`yield` 使函数能够记住其上一次的状态，包括局部变量和执行的位置，因此当生成器再次被调用时，它可以从中断的地方继续执行。而 `return` 则不会保存任何状态信息，每次调用都是全新的开始。
>
> **使用 `yield` 的好处**
>
> - **节省资源**：由于生成器是惰性求值的，只有在需要的时候才计算下一个值，所以它可以有效地处理大数据集，避免一次性加载所有数据到内存中。
> - **简化代码**：生成器提供了一种简单的方式来实现复杂的迭代模式，而不需要显式地管理迭代状态。
> - **提高效率**：对于需要连续处理大量数据的应用场景，生成器可以避免不必要的内存分配和垃圾回收，从而提高程序的运行效率。
> - **易于使用**：生成器可以像普通迭代器一样使用，可以很容易地集成到现有的代码中，如 for 循环等。
>
> 综上所述，`yield` 提供了一种强大的机制，用于处理那些需要逐步生成或处理大量数据的情况，同时保持代码的简洁性和高效性。

