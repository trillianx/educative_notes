

# Recursion

Here is a recursion coding problems to work out periodically: 

## Challenge 1:  Find the length of a given array using Recursion

Given an array output the length of the array

## Challenge 2: Find the number of occurences of a value in an array

Given an array and a value, find the number of times the value occurs in the array

## Challenge 3: Invert an Array

Given an array output the array in reverse. 

<img src="Recursion.assets/image-20201117153053053.png" alt="image-20201117153053053" style="zoom:50%;" />



## Challenge 4: Replace all Negative Numbers with `0`

Given an array. If the array has a negative number, replace that with `0`. Do not create a new array: 

<img src="Recursion.assets/image-20201117154039713.png" alt="image-20201117154039713" style="zoom:50%;" />



## Challenge 5: Find the Average of Numbers

Given an array find the average of numbers. The function has two inputs, the array and `currentIndex`. 

```python
def average(arr, currentIndex):
    pass
```



# Solutions

Here are the solutions for the challenges

## Challenge 1:  Find the length of a given array using Recursion

```python
def find_length(arr, count):
    if arr == []:
        return count
    else:
        count = find_length(arr[1:], count+1)
   	return count
```

Note that we need to have a return statement that returns the count when the length of the array is 0. If this is not set correctly, we will get incorrect result. The other thing to keep in mind is the count itself. By assigning the call to the same variable `count`, you capture the increment in the count. If you don't do that, the count will be reset to zero. This solution may not seen quite intuitive but it is a way we use to count the height of a binary tree. 

An alternative to solve this problem is in the following way: 

```python
def find_length(arr):
    if arr == []:
        return 0
    else:
        return 1 + find_length(arr)
```

This may be more intuitive. 

## Challenge 2: Find the number of occurences of a value in an array

```python
def find_occurrence(arr, value, count):
    if len(arr) == 0:
        return count
    else:
        if arr[0] == value:
            count = find_occurrences(arr[1:], value, count+1)
        else:
            count = find_occurrences(arr[1:], value, count)
    return count
```

This solution is similar to finding the length of an array. The only difference here is that we make use of a condition to test whether a value in the array is equal to the value. If it is, we increase the counter, else we don't. 

Alternative way is solving is again using the alternative method we used to get the length of the array: 

```python
def find_occurrences(arr, value):
    if arr == []:
        return 0
    else:
        if arr[0] == value:
            return 1 + find_occurrences(arr[1:], value)
        else:
            return 1 + find_occurrences(arr[1:], value)
```

## Challenge 3: Invert an Array

```python
def reverse(arr):
    if len(arr) == 0:
        return []
    else:
        return reverse(arr[1:]) + [arr[0]]
```

The position of the `[arr[0]]` matters. If you place that in front of the recursive function, we get the same array in the same order. But by putting it after we get the array in reverse. This is because when the array is in the stack and we empty the stack, we get something like this: 

```
[]
[] + [4]
[] + [4] + [3] 
...
```

But if we had put that in front, we would get: 

```python
[]
[4] + []
[3] + [4] + [] 
...
```

## Challenge 4: Replace all Negative Numbers with `0`

```python
def replace(arr):
    if len(arr) == 0:
        return []
    else:
        if arr[0] < 0:
            return [0] + replace(arr[1:])
        else:
            return [arr[0]] + replace(arr[1:])
```

This is the same idea as reversing it. But instead of passing the actual number BEFORE the recursive call, simply pass an array with `0`. 

## Challenge 5: Find the Average of Numbers

```python
def average(arr, currentIndex):
    # Base Case: 
    if currentIndex == len(arr) - 1:
        return arr[currentIndex]
    
    # Compute the average:
    if currentIndex == 0:
        return (arr[currentIndex] + average(arr, currentIndex + 1)) / len(arr)
    
    # Compute the sum of the numbers: 
    return arr[currentIndex] + average(arr, currentIndex + 1)
```

