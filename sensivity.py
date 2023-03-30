import matplotlib.pyplot as plt
from Sequances import get_sequances
from CONST import *

fig, axs = plt.subplots(2, 3, figsize=(20, 10))  

iterations = 45000

s1, s2, s3, s4, s5, s6 = get_sequances(x1, x2, x3, x4, x5, x6, h, iterations)


x1, x2, x3 = Chens.Key(0.1, 0.2 , 0.3, 0.01, 490)
x4, x5, x6 = Lorenz.Key(0.1, 0.2 + 10**-14, 0.3, 0.01, 490)
x1 /= 10
x2 /= 10
x3 /= 10
x4 /= 10
x5 /= 10
x6 /= 10
print(x1, x2, x3, x4, x5, x6)

r1, r2, r3, r4, r5, r6 = get_sequances(x1, x2, x3, x4, x5, x6, h, iterations)

axs[0, 0].plot(s1, 'b', label='y', linewidth=0.3)
axs[0, 0].plot(r1, 'r', label='y + 1E-14', linewidth=0.3)
axs[0, 0].set_title('Sequence 1')
axs[0, 0].legend(loc='upper right')

axs[0, 1].plot(s2, 'b', label='y', linewidth=0.3)
axs[0, 1].plot(r2, 'r', label='y + 1E-14', linewidth=0.3)
axs[0, 1].set_title('Sequence 2')
axs[0, 1].legend(loc='upper right')

axs[0, 2].plot(s3, 'b', label='y', linewidth=0.3)
axs[0, 2].plot(r3, 'r', label='y + 1E-14', linewidth=0.3)
axs[0, 2].set_title('Sequence 3')
axs[0, 2].legend(loc='upper right')

axs[1, 0].plot(s4, 'b', label='y', linewidth=0.3)
axs[1, 0].plot(r4, 'r', label='y + 1E-14', linewidth=0.3)
axs[1, 0].set_title('Sequence 4')
axs[1, 0].legend(loc='upper right')

axs[1, 1].plot(s5, 'b', label='y', linewidth=0.3)
axs[1, 1].plot(r5, 'r', label='y + 1E-14', linewidth=0.3)
axs[1, 1].set_title('Sequence 5')
axs[1, 1].legend(loc='upper right')


axs[1, 2].plot(s6, 'b', label='y', linewidth=0.3)
axs[1, 2].plot(r6, 'r', label='y + 1E-14', linewidth=0.3)
axs[1, 2].set_title('Sequence 6')
axs[1, 2].legend(loc='upper right')


#plt.plot(s1, 'b', label='x2', linewidth=0.5)
#plt.plot(r1, 'r', label='x2 + 1E-10', linewidth=0.5)
#plt.title('Sequence 1')

#plt.savefig('figs/Sequence1_x2.png')
plt.show()