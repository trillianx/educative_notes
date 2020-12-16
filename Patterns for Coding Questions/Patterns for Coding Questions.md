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

Let's look at another problem

### Smallest Subarray with a Given Sum

Given an array of positive numbers and a positive number $S$, find the length of the smallest contiguous subarray whose sum is greater than or equal to $S$. Return `0` if no such subarray exists. 

Here are some examples: 

![image-20201214162024312](Patterns%20for%20Coding%20Questions.assets/image-20201214162024312.png)

We start with a window size of `1`. We find that there is no number which is greater or equal to `7`. However, when we increase the window size to `2`, we see that we have one possibility, `[5,2]`, which equals `7`. 

Here's another example: 

![image-20201214162205739](Patterns%20for%20Coding%20Questions.assets/image-20201214162205739.png)

In this case, a window size of 1 helps get the answer. 

While for the following, we see that: 

![image-20201214162248875](Patterns%20for%20Coding%20Questions.assets/image-20201214162248875.png)

a window size of 3 gets us the answer. Note that, in this case there are two possibilities, so we show both of them. 

Let's solve this problem: 

```python
def smallest_sub(s, arr):
    for windowsize in range(len(arr)):
        start = 0
        sum_val = 0
        for end in range(len(arr)):
            sum_val = sum_val + arr[end]
            if sum_val >= s:
                return len(arr[start:end+1])
            if end >= windowsize - 1:
                sum_val = sum_val - arr[start]
                start += 1
    return 0

if __name__ == "__main__":
    arr = [2, 1, 5, 2, 3, 2]
    arr2 = [2, 1, 5, 2, 8]
    arr3 = [3, 4, 1, 1, 6]
    print(smallest_sub(8, arr3))
```

This works well. However, because we used two `for` loops, the time complexity is $O(N^2)$. 

Here's the code: 

```python
import math

def smallest_sub(s, arr):
    sum_val = 0
    min_length = math.inf
    start = 0
    for end in range(len(arr)):
        sum_val += arr[end]
        while sum_val >= s:
            cur_length = end - start + 1
            min_length = min(min_length, cur_length)
            sum_val -= arr[start]
            start += 1
    if min_length == math.inf:
        return 0
    return min_length
```

Here are the steps we take: 

1.  We add elements to `sum_val`, thus increasing the window size, until the `sum_val` is greater than `s`. 
2.  We note the size of the window, `cur_length = end - start + 1`. 
3.  We pick the minimum of the window sizes and store it in `min_length`
4.  We then move the window by 1 element. 
5.  We now add elements until the `sum_val` is greater or equal to `s`
6.  We repeat steps 2 - 6

Graphically, this is how it looks like: 

![image-20201215145305548](Patterns%20for%20Coding%20Questions.assets/image-20201215145305548.png)

In this way we only traverse the array once rather than multiple times using the double for loop. The time complexity for this is $O(N + N) \approx O(N)$. And the space complexity is $O(1)$ as the algorithm runs in constant space. 

Let's look at another problem

### Longest Substring with K Distinct Characters

Given a string, find the length of the longest substring in it with no more than K distinct characters. 

![image-20201215145827174](Patterns%20for%20Coding%20Questions.assets/image-20201215145827174.png)

![image-20201215145915337](Patterns%20for%20Coding%20Questions.assets/image-20201215145915337.png)

Let's solve this problem: 

```python
def longest_substrings_with_k_distinct(string, k):
    start = 0
    max_length = 0
    char_frequency = {}
    
    for end in range(len(string)):
        right_char = string[end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1
        
        while len(char_frequency) > k:
            left_char = string[start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            start += 1
        max_length = max(max_length, end - start + 1)
    return max_length
        
```

The time complexity is $O(2N)$ while the time complexity is $O(K)$. 

### Fruits into Baskets

Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit. 

You can start with any tree, but you can’t skip a tree once you have started. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.

![image-20201215155248154](Patterns%20for%20Coding%20Questions.assets/image-20201215155248154.png)

This problem is quite similar to the previous problem. In this case, we take K = 2. The answer would be the following: 

```python
def fruits_into_baskets(fruits):
  window_start = 0
  max_length = 0
  fruit_frequency = {}

  # try to extend the range [window_start, window_end]
  for window_end in range(len(fruits)):
    right_fruit = fruits[window_end]
    if right_fruit not in fruit_frequency:
      fruit_frequency[right_fruit] = 0
    fruit_frequency[right_fruit] += 1

    # shrink the sliding window, until we are left with '2' fruits in the fruit frequency dictionary
    while len(fruit_frequency) > 2:
      left_fruit = fruits[window_start]
      fruit_frequency[left_fruit] -= 1
      if fruit_frequency[left_fruit] == 0:
        del fruit_frequency[left_fruit]
      window_start += 1  # shrink the window
    max_length = max(max_length, window_end-window_start + 1)
  return max_length
```

