[TOC]



# Patterns for Coding Questions

Coding interviews are getting harder every day. A few years back, brushing up on key data structures and going through 50-75 coding interview questions was more than enough prep for an interview. Today, everyone has access to massive sets of coding problems, and they've gotten more difficult to account for that. The process has gotten more competitive.  

When our team sat together to brainstorm on ideas to make the interview process easier for candidates, we realized quickly that one skill helped us the most when we were preparing for coding interviews: "the ability to map a new problem to an already known problem."  

To help candidates with that, we've come up with a list of 16 patterns for coding questions, based on similarities in the techniques needed to solve them. As a result, once you're familiar with a pattern, you'll be able to solve dozens of problems with it.

## Introduction

This course categorizes coding interview problems into a set of **16 patterns**. Each pattern will be a complete tool - consisting of data structures, algorithms, and analysis techniques - to solve a specific category of problems. The goal is to develop an understanding of the underlying pattern, so that, we can apply that pattern to solve other problems.

We have chosen each problem carefully such that it not only maps to the same pattern but also presents different constraints. Overall, the course has around **150 problems** mapped to 16 patterns.

The problems solved under these patterns use a varied set of algorithmic techniques. We will make use of **Breadth-First Search** and **Depth-First Search** to solve problems related to **Trees** and **Graphs**. Similarly, we will also cover **Dynamic Programming**, **Backtracking**, **Recursion**, **Greedy algorithms**, and **Divide & Conquer**.

We will start with a brief introduction of each pattern before jumping onto the problems. Under each pattern, the first problem will explain the underlying pattern in detail to build the concepts that can be applied to later problems. The later problems will focus on the different constraints each problem presents and how our algorithm needs to change to handle them.

Let’s start with the **Sliding Window** pattern.

## Pattern: Sliding Window

In problems dealing with an array (or Linked lists), we are asked to find or calculate something among all the contiguous subarrays (or sublists) of a given size. For example, we are asked the following question: 

>   Given an array, find the average of all contiguous subarrays of size *K* in it

For example we are given an input: 

```python
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
```

So, the means would be: 

*   arr[0:5] / 5 = 2.2
*   Arr[1:6] / 5 = 2.8
*   ...

The final answer would be: 

```python
[2.2, 2.8, 2.4, 3.6, 2.8]
```

The brute force method would be: 

```python
def compute_average(arr, k):
    result = []
    for i in range(len(arr)):
        start = i
        end = i + k
        if end <= len(arr):
            avg = sum(arr[start:end])/5
            result.append(avg)
    return result
```

The brute force method is inefficient because, first of all, it makes of $O(N)$. The second reason is that two consecutive subarrays have a large overlap. For k=5, the overlap between subsequent arrays is of 4 numbers. The sum of these numbers have already been counted during the first pass . But we continue to compute them again in the second pass. 

![image-20201214141558918](Patterns%20for%20Coding%20Questions.assets/image-20201214141558918.png)

Can we somehow reuse the sum from the first pass over when we do the second pass?  The efficient way would be to consider a window of size $K$ which slides one element at a time. To reuse the **sum** of the previous subarray, we subtract the element going out of the window and add the element coming into the window. 

![image-20201214143150897](Patterns%20for%20Coding%20Questions.assets/image-20201214143150897.png)

```python 
def compute_avg(arr, k):
    sums = 0
    start = 0
    result = []
    for end in range(len(arr)):
        sums = sum + arr[end]
        if end >= k - 1:
            result.append(sum / k)
            sums = (sums - arr[start])
            start += 1
     return result
```

Let's understand this code. We start by setting the sum to zero. We set the start of the window to be `0` as well. Then we define a list. 

Now what we want to do is keeping add numbers one by one until we read the window size. This is done using the `for end in range(len(arr))`. This also has a dual purpose. Once the window size is reached, we keep adding the numbers but we begin removing the numbers from the front. This is where the `start` comes into the picture. The `if end >= k - 1` is to check whether the window size is reached. Once the window size is reached, we simply remove the first element from the window and add the next element. 

In the following chapters we will use the sliding window approach to solve few problems. 

In some problems, the size of the sliding window is not fixed. We have to expand or shrink the window based on the problem constraints. We will see a few examples of such problems in the next chapter. 

### Maximum Sum Subarray of Size K

Here's the problem statement: 

Given an array of positive numbers and a positive number, $k$, find the maximum sum of any contiguous subarray of size $k$. 

Here are two examples: 

![image-20201214145200604](Patterns%20for%20Coding%20Questions.assets/image-20201214145200604.png)

![image-20201214145240419](Patterns%20for%20Coding%20Questions.assets/image-20201214145240419.png)

The answer is again the use of sliding window. Here's the code: 

```python
def max_sub(k, arr):
    sum_val = 0
    start = 0
    max_val = 0
    for end in range(len(arr)):
        sum_val += arr[end]
        if end >= k - 1:
            max_val = max(max_val, sum_val)
            sum_val = sum_val - arr[start]
            start += 1
    return max_val

if __name__ == "__main__":
    arr = [2, 1, 5, 1, 3, 2]
    arr2 = [2, 3, 4, 1, 5]
    k = 2
    print(max_sub(k, arr2))
```

Now this is similar to the average we computed. However, there is one difference here: 

```python
max_val = max(max_val, sum_val)
```

We compare the `max_val` with the `sum_val` and take the maximum of the two. Graphically, this is how it looks: 

![image-20201214155628794](Patterns%20for%20Coding%20Questions.assets/image-20201214155628794.png)

