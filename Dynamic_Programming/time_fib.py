import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def run_fib():
    df = pd.DataFrame(columns=['Number', 'Result', 'Duration'])
    num_list = []
    result_list = []
    duration_list = []
    for i in range(0, 41):
        print(i)
        start = time.time()
        result = fib_dp(i)
        end = time.time()
        duration = end - start
        num_list.append(i)
        result_list.append(result)
        duration_list.append(duration)
    df.loc[:, 'Number'] = num_list
    df.loc[:, 'Result'] = result_list
    df.loc[:, 'Duration'] = duration_list
    return df

calculated = {}

def fib_dp(n):
    if n == 0: # base case 1
        return 0
    if n == 1: # base case 2
        return 1
    elif n in calculated:
        return calculated[n]
    else: # recursive step
        calculated[n] = fib(n-1) + fib(n-2)
        return calculated[n]


if __name__ == "__main__":
    result2 = run_fib()
    result = pd.read_csv('recursion_test.csv')
    plt.plot(result.Number, result.Duration, label='Recursion')
    plt.plot(result2.Number, result2.Duration, label='Dynamic Programming')
    plt.xlabel('Number')
    plt.ylabel('Duration (seconds)')
    plt.show()