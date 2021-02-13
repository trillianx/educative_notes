import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

x = np.arange(1, 30)
plt.plot(x, x, label='n')
plt.plot(x, x**2, label='$n^2$')
plt.plot(x, x*np.log2(x), label='$n\ log\ n$')
plt.plot(x, np.log2(x), label='$log\ n$')
plt.plot(x, 2**x, label='$2^n$')
plt.plot(x, )
plt.yscale('log')
plt.xscale('log')
plt.xlabel('N')
plt.ylabel('Steps')
plt.legend()
plt.show()