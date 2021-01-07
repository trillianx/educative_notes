[TOC]



# Dynamic Programming 

This course covers the concepts of dynamic programming starting from basic recursion all the way to tabulation-based, bottom-up techniques. The concepts are explained with the help of visualizations and interactive code. There are many coding challenges including classics like the Traveling Salesman, Weighted Scheduling, and String Sub-Sequence problems. We compare multiple solutions for each of these challenges and explain each in depth.

After taking this course, you should be able to:

-   Analyze and formulate a problem recursively.
-   Use memoization to improve simple recursion.
-   Write a bottom-up version of the recursive algorithms.
-   Argue about the time and space complexity of various algorithms.
-   Recognize recurring patterns in different problems to solve them using dynamic programming.

## Chapter 1: What is Recursion? 

 Recursion is used quite a lot in interview questions and therefore recursion technique is important to learn. **Recursion** is a process of repeating a procedure. In CS, recursion is referred to "calling itself". There are two types of recursion: 

*   Direct
*   Indirect

### Direct Recursion

A direct recursion happens when a function calls itself directly in its body or definition. For example, 

```python
def func(str, n):
    if n > 0:
        print(str, "called func with n = ", n)
        func("func", n - 1)
```

When we run this function, we get: 

```python
func('string', len('string'))

string called func with n =  6
func called func with n =  5
func called func with n =  4
func called func with n =  3
func called func with n =  2
func called func with n =  1
```

In order for the recursion to end, we use the base case. This base case is `n > 0`. The position of the `print` statement matters too. This is because if you have it before the function call, we get a different answer while if we have it after the function call, we get an entirely different answer as we can see here: 

```python
def func(str, n):
    if n > 0:
        func("func", n - 1)
        print(str, "called func with n = ", n)
        
func('string', len('string'))

func called func with n =  1
func called func with n =  2
func called func with n =  3
func called func with n =  4
func called func with n =  5
string called func with n =  6
```

This is because in a way a recursion function is executed. In the first case, the value `n` decreases from 6 to 1, but as it `n` decreases, it first prints out the `print` statement and then the call of the function. In the second case, the call to the function happens first and then when the base case is hit, the `print` statement is executed. 

The case when the `print` statement happens before the recursive call is called a **tail recursion**. This is the first case in our example. When the `print` statement happens after the recursive call, it is called a **head recursion**. 

### Indirect Recursion

When two or more functions call themselves indirectly from each other, we call it **indirect recursion**. Here's an example: 

```python
def func(str, n):
    if n > 0:
        print(str, 'called func with n = ', n)
        func2("func1", n-1)
        
def func2(str, n):
    if n > 0:
        print(str, 'called func2 with n = ', n)
        func("func2", n-2)
```

The output looks something like this: 

```python
func('string', len('string'))

string called func with n =  6
func1 called func2 with n =  5
func2 called func with n =  3
func1 called func2 with n =  2
```

Basically, in this case we have: 

```python
func -> func2 -> func -> func2 -> ...
```

Here's how the two recursion types differ: 

<img src="Dynamic%20Programming.assets/image-20201207143004143.png" alt="image-20201207143004143" style="zoom:100%;" />

### Non-linear Recursion

The above discussed recursion types make single call to themselves. This type of recursion is called **linear recursion**. You might have a case where a function calls itself multiple times instead of once; we call that **non-linear recursion**. A binary recursion is an example of non-linear recursion

![image-20201207143415006](Dynamic%20Programming.assets/image-20201207143415006.png)

### Thinking Recursively

Let's use an example to illustrate how you can think recursively. Create a function that takes a string and a character. The function should count the number of instances of that character in the given string. For example, 

```python
countChar('abacada', 'a')
4
```

So, we see that `'a'` is repeated 4 times. 

```python
def countChar(string, char, n):
    if len(string) == 0:
        return n
    else:
        if string[0] == char:
            return countChar(string[1:], char, n + 1)
        else:
            return countChar(string[1:], char, n)
```

Notice the base case here. Before you write the base case, you need to understand what it should do, especially when the recursive calls hit the base case. 

An alternative way is: 

```python
def countChar(str, char):
    # Base Case:
    if len(str) == 0:
        return 0
    if str[0] == char:
        return 1 + countChar(str[1:], char)
    else:
        return countChar(str[1:], char)
```

Let's look at another example. 

```python
def fib(n):
    if n <= 0:
        return 1
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```

The time complexity of Fibonacci sequence using a recursive method can be illustrated in the following way. Here we look at the `fib(6)`. 

![image-20210106104322721](Dynamic%20Programming.assets/image-20210106104322721.png)

The time complexity is $\Theta(2^n)$. 

### Is Plain Recursion Good Enough?

Recursion works and works beautifully. However, a recursion approach is a brute force approach. We can see this clearly in the Fibonacci sequence. The computation of Fibonacci takes exponential time. Though recursion seems to work really well, it is still very slow. 

<img src="Dynamic%20Programming.assets/image-20210106111316454.png" alt="image-20210106111316454" style="zoom:50%;" />

This figure show how long it takes to compute Fibonacci of a given number. We see how quickly the duration increases as the number increases. The time complexity is exponential for the recursive method

```python
def run_fib():
    df = pd.DataFrame(columns=['Number', 'Result', 'Duration'])
    num_list = []
    result_list = []
    duration_list = []
    for i in range(0, 41):
        start = time.time()
        result = fib(i)
        end = time.time()
        duration = end - start
        num_list.append(i)
        result_list.append(result)
        duration_list.append(duration)
    df.loc[:, 'Number'] = num_list
    df.loc[:, 'Result'] = result_list
    df.loc[:, 'Duration'] = duration_list
    return df
```



The question is, "Why is recursion so inefficient?" This question can be answered by looking at the figure below. 

![image-20210106110458984](Dynamic%20Programming.assets/image-20210106110458984.png)

We see from the color boxes that the Fibonacci of the same value is computed multiple times. This repeated calculations slows down the function. This is where dynamic programming comes into picture. 

### What is Dynamic Programming? 

Dynamic programming is an approach where if something is repeated, its calculated once and its value is stored and then accessed when required. Accessing a particular value takes $O(1)$ so this approach makes our programs faster. 

We can define dynamic programming as follows: 

>   For a problem that depends on subproblems that are being repeatedly re-evaluated, we can store results of these subproblems to avoid re-evaluation. 



### Approaches of Dynamic Programming

As we saw in the previous section, dynamic programming is used when solving a problem depends on solving a bunch of subproblems. Fibonacci is a good candidate for dynamic programming because solving `Fib(6)` involves solving `Fib(5)` and `Fib(4)` which in turn depends on solving `Fib(3)` and so on...

There are two basic approaches to solving a problem using dynamic programming. These approaches differ from each other in the way they start solving a problem: 

*   **Bottom-up Approach** - involves starting with the most basic unit (subproblem) and then building it up to the solution. For example, if we are asked to create a building with 4 floors and 3 rooms, we start by building one room, then three rooms, then a floor and finally ending with 4 floors. 
*   **Top-down Approach** - involves starting with the problem and building and using smaller components (subproblems) as needed. For example, if we are asked to create a building with 4 floors and 3 rooms, we start by creating a scaffolding that will hold 4 floors and 3 rooms. Then we add a room in each floor and continue until we have three rooms in each floor. 

Recursion is like dumb top-down approach as we start with a big problem and move to the smallest unit, our base case. The only difference in the actual top-down approach is that we evaluate what is required before we start. 

### Where to Use Dynamic Programming? 

Here's an example of Fibonacci function that has been rewritten using dynamic programming: 

```python
calculated = {}

def fib(n):
  if n == 0: # base case 1
    return 0
  if n == 1: # base case 2
    return 1
  elif n in calculated:
    return calculated[n]
  else: # recursive step
    calculated[n] = fib(n-1) + fib(n-2)
    return calculated[n]
```

The comparison between recursion and dynamic programming for Fibonacci sequence is shown below: 



Dynamic programming may seem like a procedure that one can apply instead of recursion. However, dynamic programming works best when certain conditions are satisfied. These are: 

*   **Optimal Structure**
*   **Overlapping Subproblems** 

Let's look at these two prerequisites in more detail: 

### Optimal Structure

This means that an optimal solution can be built to the main problem if an optimal solution can be built to a subproblem. If the main problem exists such that it can be broken down to subproblems. These subproblems can then be solved optimally. 

### Overlapping Subproblems

This means that subproblems are repeated in a given calculations. For example, computation of `Fib(6)` requires computation of `Fib(5)` and `Fib(4)` Now `Fib(5)` requires calculation of `Fib(4)` and `Fib(3)` and so does `Fib(4)` requiring `Fib(3)`. So, we see that a subproblem requires recomputing what another subproblem already did. 

## Chapter 2: Top-Down Dynamic Programming with Memoization

The process of storing evaluated results in the top-down approach is called **memoization**. We saw memoization in the Fibonacci approach. 

```python
calculated = {}

def fib_dp(n):
    if n == 0: # base case 1
        return 0
    if n == 1: # base case 2
        return 1
    elif n in calculated:
        return calculated[n]
    else: # recursive step
        calculated[n] = fib(n-1) + fib(n-2)
        return calculated[n]
```

The dictionary `calculated` is memoization. 

>   Th act of storing results of costly function call, and retrieving them from the store when needed again to avoid re-evaluation.

Memoization is done mostly using hash tables or dictionary. This allows us to quickly check a value based on the key-value pair. 

The method of storing information and retrieving when required reduces the time complexity from $O(2^n)$ to $O(n)$. This works because the computation of the values is much less when there is a look-up table. The graphic below shows `Fib(6)` computation: 

![image-20210106133640921](Dynamic%20Programming.assets/image-20210106133640921.png)

The calculation goes to the base case recursively until it hits the base case. Then when it computes `Fib(2)` it stores this information in the hash table. The computation of `Fib(3)` then requires accessing the result of `Fib(2)` from the table and hitting the base case for `Fib(1)`. This information is not stored in the table. 

Let's look at some examples. 

### The Staircase Problem

Sarah is standing next to a staircase that leads to her apartment. The staircase has `n` total steps; Sarah knows she can climb anywhere between `1` and `m` steps in one jump. She thinks about how many ways there are to climb this staircase. Given that there are `n` stairs and `m` stairs can be covered in one jump, find the number of possible ways to climb the stairs. 

Here's the input: 

```python
n = 4
m = 2
```

And the expected output is: 

```python
staircase(n, m)
5
```

Here are the possible ways: 

1.  Sarah takes one step each time
2.  Sarah takes one step, followed by 2 steps, and then one step
3.  Sarah takes 2 steps followed by one step and one step
4.  Sarah takes 1 step followed by 1 step and then two steps
5.  Sarah takes 2 steps followed by 2 steps 

This adds up to 5 ways. The way to think of this is that at every step in the beginning Sarah can either take 1 or `m` steps. 

Let's solve this using simple recursion and using dynamic programming. To understand how this works, start by looking at a simple problem and then add more complexity to it. So, let's start with `n=2`. 

| n = 1|n  = 2 | n = 3   | n = 4       |
| -----|------ | ------- | ----------- |
| 1|1, 1| 1, 1, 1 | 1, 1, 1, 1  |
|  |2   | 2, 1    | 2, 1, 1     |
|  |    | **1, 2** | 1, 2, 1     |
|  |    |         | **1, 1, 2** |
|  |    |         | **2, 2**    |

We see a pattern here. 

*   The total number of ways to reach `n = 3` is 
    *   by adding 1 to the total number of ways to reach `n = 2` and 
    *   adding 2 to the number of ways to reach `n = 1`. 
*   The total number of ways to reach `n = 4` is 

We can simply the above table to something like this: 

| n = 1 | n = 2 | n = 3 | n = 4 |
| ----- | ----- | ----- | ----- |
| 1     | 2     | 3     | 5     |

Now we see this clearly. The current value is simply the sum of the previous two terms, which would be Fibonacci sequence. 
$$
F(n) = F(n-1) + F(n-2)
$$


But if we have `m = 3` then: 

| n = 1 | n = 2 | n = 3   | n = 4      |
| ----- | ----- | ------- | ---------- |
| 1     | 1, 1  | 1, 1, 1 | 1, 1, 1, 1 |
|       | 2     | 2, 1    | 2, 1, 1    |
|       |       | 1, 2    | 1, 2, 1    |
|       |       | 3       | 3, 1       |
|       |       |         | 1, 1, 2    |
|       |       |         | 2, 2       |
|       |       |         | 1, 3       |

We can simplify this as: 

| n = 1 | n = 2 | n = 3 | n = 4 |
| ----- | ----- | ----- | ----- |
| 1     | 2     | 4     | 7     |

So, when `m = 3`, we add the sum of the previous three terms: 
$$
F(n) = F(n-1) + F(n-2) + F(n-3)
$$

#### Simple Recursion

```python
def staircase(n, m):
    if n == 0:
        return 1
    ways = 0
    for i in range(1, m+1):
        if i <= n:
            ways += staircase(n-i, m)
    return ways
```

In the recursion this is what is happening. When `m = 2`, the loop goes from `1, 2`. Thus in line 7, we have `f(n-1)` and then `f(n-2)`. However, when `m = 3`, we would have: `f(n-1) + f(n-2) + f(n-3)` as expected and so forth. 

But again just like in Fibonacci, we compute the same mulitple times. We can make this easier with dynamic programming. However, before we decide to use dynamic programming we need to check if the two conditions are satisfied: 

*   **Optimal substructure**: If we want to evaluate the answer for `staircase(n, m)`, and we have answers for `staircase(n-1, m)`, `staircase(n-2, m)`, … `staircase(n-m, m)`, we can simply sum up all these answers to get the answer for the `staircase(n, m)`.
*   **Overlapping subproblems**: Again, just like in the case of Fibonacci, there are overlapping subproblems

Knowing these two conditions are satisfied, we can solve the problem using dynamic programming. 

#### Dynamic Programming

Here's the solution to the problem

```python
def staircase_helper(n, m, memo):
    # Base case when there are no stairs
    if n == 0:
        return 1
    # before recursive step check if result is memoized
    if n in memo:
        return memo[n]
    # if not, use the usual calculation
    ways = 0
    for i in range(1, m+1):
        # if steps remaining are smaller than the jump step, skip
        if i <= n:
            ways += staircase_helper(n-i, m, memo)
    memo[n] = ways
    return ways

def staircase(n, m):
    memo = {}
    return staircase_helper(n, m, memo)
```

