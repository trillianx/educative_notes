def count(n):
    if n <= 0:
        print(n)
    else:
        print(n)
        return count(n-1)

def count_instances(string, char, n):
    # Base Case: 
    if len(string) == 0:
        return n
    else:
        if string[0] == char:
            return count_instances(string[1:], char, n+1)
        else:
            return count_instances(string[1:], char, n)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def permutations(str):
  if str == "": # base case
    return [""]
  permutes = []
  for char in str:
    subpermutes = permutations(str.replace(char, "", 1))    # recursive step
    for each in subpermutes:
      permutes.append(char+each)
  return permutes


if __name__ == "__main__":
    string = 'abc'
    print(permutations(string))

