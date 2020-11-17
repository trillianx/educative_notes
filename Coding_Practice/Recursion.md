

# Recursion

Here is a recursion coding problems to work out periodically: 

## Challenge 1:  Find the length of a given array using Recursion

Given an array output the length of the array

## Challenge 2: Find the number of occurences of a value in an array

Given an array and a value, find the number of times the value occurs in the array







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

Note that we need to have a return statement that returns the count when the length of the array is 0. If this is not set correctly, we will get incorrect result. The other thing to keep in mind is the 

