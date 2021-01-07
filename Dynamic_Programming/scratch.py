def staircase(n, m):
  # base case of when there is no stair
  if n == 0:    
    return 1
  ways = 0
  # iterate over number of steps, we can take
  for i in range(1,m+1):  
    # if steps remaining is smaller than the jump step, skip   
    if i <= n:  
      # recursive call with n i units lesser where i is the number of steps taken here            
      ways += staircase(n-i, m) 
  return ways

if __name__ == "__main__":
    print(staircase(4, 3))