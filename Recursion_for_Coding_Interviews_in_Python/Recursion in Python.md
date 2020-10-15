[TOC]



# Recursion for Coding Interviews in Python

If you’ve ever struggled with solving coding problems using recursion, or if you need to brush up your recursion skills for an interview, this course is for you! We will start with the basics of recursion before we practice solving actual coding problems. By the time you have completed this course, you’ll be able to use all the concepts of recursion to solve complex, real-world problems. 

## Chapter 1: Recursion Fundamentals

Recursion occurs when a function calls itself repeatedly until it reaches a specific stopping condition. Such a function is called a **recursive function**. 

>   Recursion is the process of describing an action in terms of itself

The reason we wish to use recursion because: 

*   Tasks that are composed of similar subtasks
*   Shorter and easier code
*   Loops converted to recursive by compiler

### Format of Recursive Function

A recursive function consists of two main parts: 

*   **Base Case:** is where all further calls to the same function stop
*   **Recursive Case:** is where the function calls itself repeatedly until it reaches the base case

The syntax of a recursive function is the following: 

```python
def RecursiveFunction():
    # Base Case
    if <baseCaseCondition>:
        return <some base case value>
    # Recursive Case
    else:
        return (recursive call and any other task)
```

The base case leads to returning values while the recursive case always calls the function again along with some values

### Recursion & Memory Visualization

Let’s look at how memory is allocated in recursion. When a function is called, its memory is allocated on a **stack**. A stack is a LIFO (Last-In-First-Out) process. When a function executes, it adds its state data to the top of the stack. When a function exits, this data is removed from the stack. 

Suppose we have a function: 

```python
def function1(<parameters>) :
  <create some variables>
  return(<some data>)
 
def function2(<parameters>) :
  <create some variables>
  return(<some data>)
 
# Driver Code
function1()
function2()
```

The memory stack will now look like this: 

<img src="Recursion%20in%20Python.assets/image-20201005102227436.png" alt="image-20201005102227436" style="zoom:30%;" />

A recursive function calls itself, so the memory for a called function is allocated on top of the memory allocated for **calling the function**. When the function reaches the base case, the value of the base case is returned, its memory is de-allocated and the process continues in reverse until all the functions are returned. 

To illustrate this, let’s look at an example of a factorial function. The factorial function is recursive because a factorial of a number is simply the product of all the numbers before it until we reach 1. 

```python
def factorial(n):
    if n < 0: 
        return 'Invalid number'
    # Base Case
    if n <= 1:
        return 1
    # Recursive Case
    else:
        return n * factorial(n-1)
```

Now let’s call the function: 

```python
factorial(5)

120
```

We can visualize this as follows: 

<img src="Recursion%20in%20Python.assets/image-20201005103116999.png" alt="image-20201005103116999" style="zoom:33%;" />

Running through each we stack the function on top of each other: 

<img src="Recursion%20in%20Python.assets/image-20201005103159624.png" alt="image-20201005103159624" style="zoom:33%;" />

Until we reach the top. The function `factorial(1)` is the base case which returns the value of 1. That value is then multiplied by the return of the function `factorial(2)` and so forth. Until we get to the final call in the stack. 

This can also be visualized it in the following way: 

<img src="Recursion%20in%20Python.assets/image-20201005103403769.png" alt="image-20201005103403769" style="zoom:33%;" />

Once the base case is reached, we then get: `2 * 1 = 2` followed by `3 * 2 = 6`, then `4 * 6 = 24` and ending with `24 * 5= 120`, the answer. 

### Direct Vs Indirect Recursion

In this section we will go over two types of recursions. Let’s look at each one of them: 

#### Direct Recursion

Direct recursion occurs when a function calls itself, in the sense, the function makes a recursive call inside its own function body. This is what we have seen in the factorial example. 

In general, the synax is: 

```python
def function1():
    # Some code
    function1()
```



Let’s consider another example. Without using a loop print natural numbers from 1 to n using direct recursion: 

```python
def natural_numbers(n):
    if n < 0:
        return "Invalid Number"
    # Base Case: 
    if n <= 1: 
        print(1)
    # Recursive Case:
    else:
        natural_numbers(n-1)
        print(n)
```

Note that we did not make use of the `return` statement here. We see here that until the base case is reached, nothing is printed to the screen. But when it begin to unstack, we start printing the numbers. This is easily visualized by looking at the function that prints in reverse: 

```python
def natural_numbers(n):
    if n < 0:
        return "Invalid Number"
    # Base Case: 
    if n <= 1: 
        print(1)
    # Recursive Case:
    else:
        print(n)
        natural_numbers(n-1)
```

In this case, the `print(n)` is executed as we stack the function calls. So, we print the number and we stack the recursive call, `natural_numbers(n-1)`. So, the order matters. 

>   If a statement is after the function call in a recursive function, it will be executed when we begin to de-stack. 
>
>   If the statement is before the recursive call, it will be executed when we begin to stack. 

#### Indirect Recursion

Indirect recursion occurs when a function calls another function until the original function is called again. The general syntax is: 

```python
def function1():
    function2()
    
def function2():
    function1()
```

### When to Use Recursion

Even though recursion may seem like a good idea to use all the time, there are times when recursion is not a good idea. 

Recursion should be used where it just feels natural. This will become obvious as you continue to work on various recursion problems. The most obvious indications of recursion are:

*   when the problem can be broken down into **smaller subproblems**. It is likely that a problem can be solved using recursion when you observe a pattern of that problem breaking down into similar subproblems. 
*   When a problem requires an absurd number of nested loops. When the number of nested loops are known, use iteration but when we do not know the number of loops, stick to recursion. 

### Understanding a Recursive Problem

In this section, we will go over methods to help you visualize a recursive function. Let's consider another problem. We are interested in printing the following sequence: 

```python
10
5
0
5
10
```

Let's write down a function that creates such a pattern:

```python
def printPattern(targetNumber):
    if targetNumber <= 0:
        print(0)
    else:
        print(targetNumber)
        printPattern(targetNumber-5)
        print(targetNumber)
```

So, we see that the first print statement prints the values before the recursion call goes into the stack while the second one is printed after we de-stack. 

## Chapter 2: Iteration Vs. Recursion

Iteration means repeating steps in order to achieve the desired outcome. This is generally done with the use of loops. There are two types of iteration loops: 

1.  Loops that continue to iterate until a condition is satisfied. This is typically done using a `while` loop. 
2.  Loops that iterate through a series of elements. This is typically done using a `for` loop. 

As an example, let's implement the factorial function using a `while` loop: 

```python
def factorial(n):
    if n < 0:
        return 'Invalid Number'
    product = 1
    while n != 0:
        product = product * n
        n = n-1
    return product
```

And here is an example of a for loop: 

```python
import numpy as np
def factorial_loop(n):
    if n < 0:
        return 'Invalid Number'
    product = 1
    for i in np.arange(1,n+1):
        product = product * i
    return product
```

Here are the differences between recursive and iterative methods: 

|               | Recursive                                                    | Iterative                                                    |
| ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Definition    | A function that calls itself until a base condition is satisfied | Statements are executed over and over again until a condition is satisfied |
| Application   | Recursion is always called on a function                     | Iterative code is applied to variables. A set of instructions that are called upon repeatedly |
| Termination   | Terminates when the base case condition is satisfied         | Terminates when a specific condition is satisfied or runs through a particular number of loops |
| Code Size     | Smaller and neat                                             | Extensive and cluttered                                      |
| Overhead Time | Each recursive call has an overhead time                     | No overhead time                                             |
| Speed         | Slower as it involves running the program and also invoke stack memory | Faster as the time is only running the program               |
| Stack         | Makes use of stack in each recursive call                    | Does not make use of stack                                   |

### Converting Iterative Code to Recursive Code

There are times when recursive code is more efficient than iterative code. In order to convert the code, use the following steps: 

1.  Identify the main loop. 
    1.  This loop should modify one or more variables
    2.  It should return a result based on its final values
2.  Use the loop condition as a base case and the body of the loop as the recursive case
3.  The local variables in the iterative version turn into the parameters of the recursive version
4.  Compile and rerun tests

Let's take an example to illustrate these points: Reverse a string

```python
# Iterative way: 
def reverse_string(string):
    n = len(string) - 1
    result = ''
    while n >= 0:
        result += result + string[n]
        n -= 1
    return result
```

The loop here modifies the result by adding a value from the string. The loop condition is that `n>= 0`. This becomes our base condition. So, let's write the recursive method: 

```python
def recursive_reverse(string):
    # Base case:
    if len(string) == 1:
        return string[0]
    else:
        return recursive_reverse(string[1:]) + string[0]
```

We see here that the concatenation is done in the second return statement for the recursive case. 

### Counting Vowels in a String

Let's look at another case of iterative and recursive case. This involves counting vowels in a string. 

```python
def counting_vowels_l(string):
    vowels = 'aeiou'
    if len(string) > 0:
        count = 0
        for i in string:
            if i.lower() in vowels:
                count += 1
        return count
    else:
        return 'Length should be non-zero'
```

Let's convert this into a recursive code: 

```python
def counting_vowels_r(string, n):
    # base case:
    if len(string) == 1:
        if string[0].lower() in 'aeiou':
            return n + 1
        else:
            return n
    else:
        if string[0].lower() in 'aeiou':
            return counting_vowels_r(string[1:], n + 1)
        else:
            return counting_vowels_r(string[1:], n)
```

Let's do some challenges to hone our skills

### Challenge 1: Compute Square of a Number

Using the following mathematical identity to compute the square of a number: 
$$
(n-1)^2 = n^2 - 2n + 1
$$
We can rewrite this as: 
$$
n^2 = (n-1)^2 +2n - 1
$$
So, we have $n$ in terms of $n-1$, which allows us to decrease $n$ until it reaches $0$. Thus our base case would be: 

```python
if n == 0:
    return 0
```

Putting together we can write this as: 

```python
def compute_square(n):
    # base case:
    if n == 0:
        return 0
    else:
        return compute_square(n-1) + (2 * n) - 1
```

Graphically, this looks like the following: 

<img src="Recursion%20in%20Python.assets/image-20201006155048315.png" alt="image-20201006155048315" style="zoom:33%;" />

### Challenge 2: Search First Occurrence of a Number

Implement a function that takes an array `arr`, a `testVariable` (containing the number to search) and `currentIndex` (containing the starting index) as parameters. The function then returns the index of the first occurrence of `testVariable` in the `arr`. If the `testVariable` is not found in `arr`, it should return `-1`. 

For example, 

```python
arr = [9, 8, 1, 8, 1, 7]
testVariable = 1
currentIndex = 0
```

The output would be: `2`

```python
def firstIndex(arr, testVariable, currentIndex):
    # Base Case 1: 
	if arr[0] == testVariable:
        return currentIndex
    # Base Case 2
    elif len(arr) == 1:
        return -1
    # Recursive Case
    else:
        return firstIndex(arr[1:], testVariable, currentIndex + 1)
```

Another way to solve this would be: 

```python
def firstIndex(arr, testVariable, currentIndex) : # returns the first occurrence of testVariable
  # Base Case1
  if len(arr) == currentIndex :
    return -1;

  # Base Case2  
  if arr[currentIndex] == testVariable :
    return currentIndex

  # Recursive Case
  return firstIndex(arr, testVariable, currentIndex + 1)
```

### Challenge 3: Implement the Fibonacci Sequence

The Fibonacci sequence is one of the most famous formulas in mathematics. Each number in the sequence is the sum of the two numbers that precede it.

The sequence looks as follows:

$ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 … $

Use the following relationship to write a recursive code: 
$$
F_n = F_{n-2} + F_{n-1}
$$

```python
def fibonacci(testVariable):
    if testVariable == 0:
        return 0
    elif testVariable == 1:
        return 1
    else:
        return fibonacci(testVariable - 2) + fibonacci(testVariable - 1)
```

Another way to solve this is using the following: 

```python
def fibonacci(testVariable):
    # Base Case
    if testVariable <= 1 :
        return testVariable
    
    # Recursive Case
    return(fibonacci(testVariable - 1) + fibonacci(testVariable - 2))
```



## Chapter 2: Recursion with Numbers

In this chapter we will learn how use recursion that involve the use of numbers. 

As a first example, let's see how we can compute the the power of a number. That is to say, given a number n and a computer x, we wish to compute: 
$$
\text{power} = n^x
$$
Let's implement this as a recursion: 

```python
def compute_power(n, x):
    # Base case: 
    if x <= 0:
        return 1
    else:
        return n * compute_power(n, x-1)
```

Next, let's see another example: given a number, n, we would like to compute the sum of integers from 1 to n. 

```python
def compute_sum(n):
    # Base case: 
    if n <= 1:
        return 1
    else:
        return n + compute_sum(n-1)
```

As a third example, we will compute the modulo of a number. The number that is being divided is called the **dividend**. The number that divides the dividend is called the **divisor**. The modulo operation returns the remainder when a number is divded by another number. 

<img src="Recursion%20in%20Python.assets/image-20201014195727524.png" alt="image-20201014195727524" style="zoom:50%;" />

So, the relationship between these components are: 
$$
\text{divisor} \times \text{quotient} + \text{remainder} = \text{dividend}
$$
So, we have the recursion formula as: 
$$
\text{remainder} = \text{dividend} - (\text{divisor} \times \text{quotient})
$$
Let's work this out: 

```python
def get_modulo(dividend, divisor):
    if divisor == 0:
        return 0
    if dividend < divisor:
        return dividend
    else:
        return get_modulo(dividend - divisor, divisor)
```

### Challenge 1: Find the Greatest Common Divisor

Implement a function that takes two numbers, `testVariable1` and `testVariable2` and returns their **greatest common divisor**. The greatest common divisor of two or more integers is the largest positive integer that divides each of the integers. For example, for 42 and 56, we have: 

*   42 is divided by 1, 2, 3, 6, 7, 14, 21, 42
*   56 is divided by 1, 2, 4, 7, 8, 14, 28, 56

So, the greatest common divisor for 42 and 56 is 14. 

```python
def GCD(num1, num2):
    # Base Case:
    if num1 == num2:
        return num1
    if num1 > num2:
        return GCD(num1-num2, num2)
    else:
        return GCD(num1, num2-num1)
```

