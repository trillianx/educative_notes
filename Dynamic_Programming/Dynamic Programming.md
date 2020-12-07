# Dynamic Programming 

This course covers the concepts of dynamic programming starting from basic recursion all the way to tabulation-based, bottom-up techniques. The concepts are explained with the help of visualizations and interactive code. There are many coding challenges including classics like the Traveling Salesman, Weighted Scheduling, and String Sub-Sequence problems. We compare multiple solutions for each of these challenges and explain each in depth.

After taking this course, you should be able to:

-   Analyze and formulate a problem recursively.
-   Use memoization to improve simple recursion.
-   Write a bottom-up version of the recursive algorithms.
-   Argue about the time and space complexity of various algorithms.
-   Recognize recurring patterns in different problems to solve them using dynamic programming.

## What is Recursion? 

 Recursion is used quite a lot in interview programs and therefore recursion is technique is important to learn. **Recursion** is a process of repeating a procedure. In CS, recursion is referred to calling itself. There are two types of recursion: 

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

