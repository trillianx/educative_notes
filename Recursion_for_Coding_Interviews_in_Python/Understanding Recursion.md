# Understanding Recursion

There are various ways to work out in recursion. Let's start with something simple and increase the complexity as we go through. In each example, let's understand the behavior of recursion and see if we can put them into buckets.

It is easier to understand recursion when we think in terms of stacks. So, the calls to the function get stored in a stack. When the base case is hit, the unstacking happens. With this in mind, let's see how the recursion behavior works. 



## Example 1: Counting Numbers

There are two ways of counting numbers: straight or in reverse. Recursion of counting numbers happens naturally in reverse because of stacking. If we were to count the numbers from 0 through 10, we would write the recursive function as follows: 

```python
def count_reverse(n):
    # Base Case: 
    if n <= 0:
        print(n)
    else:
        count_reverse(n-1)
        print(n)


if __name__ == "__main__":
    count(10)
```

Let's suppose `n=10`. When we go through recursion, the number 10 will be at the bottom, followed by 9 and then 8 and so on. Our base case stops the recursive process when `n=0`.  At this point, the first print statement print out a value of `0`. Then we go through the stack by printing `1` and `2` and so forth. 

Ok, now here are few nuances to understand: 

1.  If we use a `return n` instead of `print(n)` for the base case, we would not get the `0` unless we use the `print(count(10))`. 
2.  If we use a `return count_reverse(n-1)`, we get `0` because nothing after the function gets printed in Python. 

In this case, we saw that the numbers in the stack went in reverse. But note that as they go into the stack, if we were to print them out, we would get the numbers in reverse. So, the positioning of the `print()` statement helps us

```python
def count(n):
    if n <= 0:
        print(n)
    else:
        print(n-1)
        count(n-1)

if __name__ == "__main__":
    count(10)
```

Here it does not matter if we include `return count(n-1)` or not. We get the answer because the `print()` statement is before the `return` statement. 

## Example 2: Counting Instances 

As we saw, the base case is very important and thinking about what the base case can do helps us get the answer. 

We are given a string and a character. We wish to count the number of times the character repeats in the string. Clearly, we need to include a way to count these instances. Let's see how to do this: 

```python
def count_instances(string, char, n):
    # Base Case: 
    if len(string) == 0:
        return n
    else:
        if string[0] == char:
            return count_instances(string[1:], char, n+1)
        else:
            return count_instances(string[1:], char, n)
            
if __name__ == "__main__":
    string = 'abacdada'
    print(count_instances(string, 'a', 0))
```

In this case, we wish to go through each of the characters once in the given string. Once we have traversed the string, we need to return the count. So, our base case should be exactly this. When the length of string is zero, we return the count value. We really don't care about destacking in this case. 

Because the numbers are being passed in each recursive call, that is, our `n` increases when the condition is met and does not when it is not met. We need to have the return statement. If there is no return statement that the recursive call does not return anything and our `n` does not increment. In fact, if we don't return anything we will simply get `None`. 

There is also another way to write this function 

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

