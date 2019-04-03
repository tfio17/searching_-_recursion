#
#
## Tom
#
## playing with matplotlib
#
#

import numpy as np
import matplotlib.pyplot as plt

x = range(1,1001)

# Just plot a line
plt.plot(x, np.log(x))
plt.ylabel('some numbers')
plt.show()
