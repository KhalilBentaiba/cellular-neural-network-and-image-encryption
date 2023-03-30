import matplotlib.pyplot as plt
from Sequances import get_sequances
from CONST import *

iterations = 45_000

s1, s2, s3, s4, s5, s6 = get_sequances(x1, x2, x3, x4, x5, x6, h, iterations)


x1, x2, x3 = Chens.Key(0.1, 0.2, 0.3, 0.01, 490)
x4, x5, x6 = Lorenz.Key(0.1, 0.2 + 10**-14, 0.3, 0.01, 490)

x1 /= 10
x2 /= 10
x3 /= 10
x4 /= 10
x5 /= 10
x6 /= 10

print(x1, x2, x3, x4, x5, x6)

r1, r2, r3, r4, r5, r6 = get_sequances(x1, x2, x3, x4, x5, x6, h, iterations)

plt.plot(s4, 'b', label='y', linewidth=0.5)
plt.legend(loc='upper right')
plt.plot(r4, 'r', label='y+1E-14', linewidth=0.5)
plt.legend(loc='upper right')
plt.show()

