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
            avg = sum(arr[start:end])/k
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
        sums = sums + arr[end]
        if end >= k - 1:
            result.append(sum / k)
            sums = (sums - arr[start])
            start += 1
     return result
```

Let's understand this code. We start by setting the sum to zero. We set the start of the window to be `0` as well. Then we define a list. 

Now what we want to do is keep adding numbers one by one until we get to the window size. This is done using the `for end in range(len(arr))`. 

This also has a dual purpose. Once the window size is reached, we keep adding the numbers but we begin removing the numbers from the front. This is where the `start` comes into the picture. The `if end >= k - 1` is to check whether the window size is reached. We use `k-1` because the numbers go start from `1` but indices start from `0`. 

Once the window size is reached, we compute the average and then we simply remove the first element from the window. The loop goes back and then adds the next element to the window. 

In the following chapters we will use the sliding window approach to solve few problems. 

In some problems, the size of the sliding window is not fixed. We have to expand or shrink the window based on the problem constraints. We will see a few examples of such problems in the next chapter. 

Here's the whole thing shown pictorally. 

<img src="Patterns%20for%20Coding%20Questions.assets/image-20210215102936004.png" alt="image-20210215102936004" style="zoom:80%;" />

>   To summarize: Start with start of the window at 0 and increase the end of the window from 0. This is done in the loop by setting the index as end. Keep adding elements to the sums until the end of the window equals k. Then subtract the start and add the end to the sum. 

### Maximum Sum Subarray of Size K (easy)

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

>   To summarise: We start with the beginning and end of the window to be zero. We increase the window size and keep adding the elements until the end of the window is `k-1`, or the window size is `k-1`. Then we take the maximum valule between the sums and the max_val and subtract the element at the start of the window from the sum. The loop then continues.  

### Smallest Subarray with a Given Sum (easy)

Given an array of positive numbers and a positive number $S$, find the length of the smallest contiguous subarray whose sum is greater than or equal to $S$. Return `0` if no such subarray exists. 

Here are some examples: 

![image-20201214162024312](Patterns%20for%20Coding%20Questions.assets/image-20201214162024312.png)

We start with a window size of `1`. We find that there is no number which is greater or equal to `7`. However, when we increase the window size to `2`, we see that we have one possibility, `[5,2]`, which equals `7`. 

Here's another example: 

![image-20201214162205739](Patterns%20for%20Coding%20Questions.assets/image-20201214162205739.png)

In this case, a window size of 1 helps get the answer. 

While for the following, we see that: 

![image-20201214162248875](Patterns%20for%20Coding%20Questions.assets/image-20201214162248875.png)

A window size of 3 gets us the answer. Note that, in this case there are two possibilities, so we show both of them. 

This problem follows the Sliding Window pattern, and we can use a similar strategy as discussed in the previous question. However, the sliding window size is not fixed. 

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

The time complexity of the above algorithm will be $O(N)$. The outer for loop runs through all elements while the inner loop processes each element only once. So, the time complexity is $O(N + N) \approx O(N)$. 

Here are the steps we take: 

1.  We add elements to `sum_val`, thus increasing the window size, until the `sum_val` is greater than `s`. 
2.  When the above condition is satisfied, we note the size of the current window. This is done using:  `cur_length = end - start + 1`. 
3.  We then pick the minimum window size. For this we set the `min_length = math.inf`. So, the minimum would be the window size we get. 
4.  Next we remove an element from start in the sum_val. This shrinks our window. If the total sum still exceeds, `s`, then we continue to shrink the window. If this is not the case, we get out of the while loop and enter the for loop. 
5.  In the for loop we increase the `end`, this increasing the window size again. 
6.  We repeat steps 2 - 6

Graphically, this is how it looks like: 

![image-20201215145305548](Patterns%20for%20Coding%20Questions.assets/image-20201215145305548.png)

In this way we only traverse the array once rather than multiple times using the double for loop. The time complexity for this is $O(N + N) \approx O(N)$. And the space complexity is $O(1)$ as the algorithm runs in constant space. 

### Longest Substring with K Distinct Characters (medium)

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

This is similar to the smallest sub. The interesting complexity is the fact that we use a hash table to keep track of characters.

This is my version of the code: 

```python
def longest(arr, k):
    n = len(arr)
    max_length = 0
    start = 0
    unique = {}
    for end in range(n):
        end_string = arr[end]
        if end_string not in unique:
            unique[end_string] = 0
        else:
            unique[end_string] += 1
        while len(unique) > k:
            start_string = arr[start]
            if unique[start_string] == 0:
                del unique[start_string]
            else:
                unique[start_string] -= 1
            start += 1
        length = end - start + 1
        max_length = max(max_length, length)
    return max_length
```



>   In general, when we are dealing with problems that involve flexible window size, move the end first and then move the start based on the condition. 

### Fruits into Baskets (medium)

Given an array of characters where each character represents a fruit tree, you are given **two baskets**, and your goal is to put **maximum number of fruits** in each basket. The only restriction is that **each basket can have only one type of fruit**. 

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

### No-repeat Substring (hard)

Given a string, find the l**ength of the longest substring**, which has **no repeating characters**. 

The solution is similar to the sliding window strategy discussed in Longest Substring with K Distinct Characters. We will use the hash map to remember the last index of each character that we have processed. Whenever we get a repeating character, we will shrink our sliding window to ensure that we always have distinct characters in the sliding window. 

```python
def non_repeat_substring(str1):
  window_start = 0
  max_length = 0
  char_index_map = {}

  for window_end in range(len(str1)):
    right_char = str1[window_end]
    
    if right_char in char_index_map:
      window_start = max(window_start, char_index_map[right_char] + 1)
    char_index_map[right_char] = window_end
    
    max_length = max(max_length, window_end - window_start + 1)
  return max_length
```

>   In summary, we increase the end index. If the end index is in the character, we measure the length of the window 

## Pattern: Two Pointers

In problems where we deal with sorted arrays (or LinkedLists) and need to find a set of elements that fulfill certain constraints, the **two pointer** approach becomes quite useful. The set of elements could be a pair, a triplet or even a subarray. 

Consider the following example: 

>    Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target

To solve this problem we make use of two pointers, one on each side of the array. Then we use the following logic: 

*   If the sum of the elements for the two pointers is greater than the target sum, we decrease the second pointer
*   If the sum of the element is less than the target, we increase the first pointer

This approach is graphically shown in the figure below: 

![image-20201217133620662](Patterns%20for%20Coding%20Questions.assets/image-20201217133620662.png)

Such an approach results in time complexity of $O(N)$. 

### Pair with Target Sum

Given an array of sorted numbers and target sum, find a pair in the array whose sum is equal to the given target. Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target. 

![image-20201217133853506](Patterns%20for%20Coding%20Questions.assets/image-20201217133853506.png)

Let's write down a solution: 

```python
def pair_with_targetsum(arr, target):
    start = 0
    end = len(arr) - 1
    sum = arr[end] + arr[start]
    while sum != target:
        if sum > target:
            end -= 1
            if end < 0:
                return None
        else:
            start += 1
            if start >= len(arr):
                return None
        sum = arr[start] + arr[end]
    return [start, end]
```

An other way of writing this would be: 

```python
def target_sum(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        sum_val = arr[start] + arr[end]
        if sum_val == target:
            return (arr[start], arr[end])
        elif sum_val > target:
            end -= 1
        else:
            start += 1
        
    return False 
```

The time complexity is $O(N)$ and the space complexity is $O(1)$. 

#### An Alternative Approach

Rather than using pointers, you can use a hash table. 

```python
def pair_with_targetsum(arr, target):
    nums = {}
    for i, num in enumerate(arr):
        if target - num in nums:
            return [nums[target - num], i]
        else:
            nums[arr[i]] = i
    return [-1, -1]
```

In this case, we add element to the dictionary along with the index. At each time, we also subtract the target value with the element and check whether the result is in the dictionary. The way this works is that elements `1, 2, 3`  are added first to the dictionary. However, when `6-4` is computed, the result value of `2` is found in the dictionary. So, the index in the loop `i` along with the value associated with the key, `2`, in the dictionary is returned. 

The time complexity is $O(N)$ and because we use a data structure, the space complexity is also $O(N)$. 

### Remove Duplicates

 Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space. Return the length of the subarray that has no duplicate in it. 

![image-20201217141656382](Patterns%20for%20Coding%20Questions.assets/image-20201217141656382.png)

Here's how we would traverse:

*   Step 1: We start with two pointers both are at index 1. One is called non duplicate index, while the other is the running index. 
*   Step 2: We compare the elements of `non_duplicate_index - 1` with element at index 1. 
*   Step 3: If the elements are not same, we copy the element of running index at the non duplicate index.
*   Step 4: We increase value of non duplicate index by 1
*   Step 5: Outside this if statement, we increase the running index by 1.





![image-20201217144717685](Patterns%20for%20Coding%20Questions.assets/image-20201217144717685.png)

We implement it in the following way: 

```python
def remove_duplicates(arr):
    non_dup_index = 1
    index = 1
    while index < len(arr):
        if arr[non_dup_index - 1] != arr[index]:
            arr[non_dup_index] = arr[index]
            non_dup_index += 1
        index += 1
    return arr[:non_dup_index] 
```

The reason we start with index of 1 for `non_dup_index` is because if there are duplicates, say two duplicates, we want to keep one while replace the other with a new number. 

This is the way I did:

```python
def remove_duplicates(arr):
    start = 0
    end = 1
    n = len(arr)
    while end < n:
        if arr[end] == arr[start]:
            arr.pop(end)
            n -= 1
        else:
            end += 1
            start += 1
    return arr
```

This method is not as efficient as the one above because `.pop(N)` takes $\mathcal{O}(N)$. Furthermore, because the array needs to be resized, that would take another $\mathcal{O}(N/2)$. 

Here's another method I created: 

```python
def remove_duplicates(arr):
    start = 0
    end = 0
    n = len(arr)
    while end < n:
        if arr[end] != arr[start]:
            start += 1
            arr[start] = arr[end]
        else:
            end += 1
    return arr[:start+1]
```



### Squaring a Sorted Array

Given a sorted array, create a new array containing squares of all the numbers of the input array in sorted order. 

![image-20201218101837535](Patterns%20for%20Coding%20Questions.assets/image-20201218101837535.png)

We start from either side of the array. 

![image-20201218102607625](Patterns%20for%20Coding%20Questions.assets/image-20201218102607625.png)

Here's how it is done: 

*   We begin by creating the start and end indexes of our pointers
*   We create an array equal to the length of the original array. This will be used to store the squared values in it. 
*   Now we will move inward and the pointers will move based on which square is less. 

Here's the solution: 

```python
def make_squares(arr):
    n = len(arr)
    start = 0
    end = len(arr) - 1
    new_arr_index = end
    
    # create a new array
    new_array = [0] * n
    while start <= end:
        start_sq = arr[start] ** 2
        end_sq = arr[end] ** 2
        if start_sq > end_sq:
            new_array[new_arr_index] = start_sq
            start += 1
        elif start_sq <= end_sq:
            new_array[new_arr_index] = end_sq
            end -= 1
        new_arr_index -= 1
    return new_array
```

This takes $O(N)$ time complexity and $O(N)$ space complexity. 

### Triple Sum to Zero

Given an array of unsorted numbers, find all unique triplets in it that add up to zero. 

![image-20201218104118468](Patterns%20for%20Coding%20Questions.assets/image-20201218104118468.png)

