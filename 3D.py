import matplotlib.pyplot as plt
from Sequances import get_sequances
from CONST import *

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
def multi_plot(fig, pos, s, x, y, z, a):
    ax = fig.add_subplot(2, 4, pos, projection='3d')
    ax.set_xlabel('x'+str(x))
    ax.set_ylabel('x'+str(y))
    ax.set_zlabel('x'+str(z))
    ax.set_title(f'({a}) '+'x'+str(x)+'-x'+str(y)+'-x'+str(z))
    ax.plot3D(s[x-1], s[y-1], s[z-1], 'b', linewidth=0.1)


fig = plt.figure(figsize=(30, 23))

s1, s2, s3, s4, s5, s6 = get_sequances(x1, x2, x3, x4, x5, x6, h, 45000)

S = [s1, s2, s3, s4, s5, s6]

multi_plot(fig, 1, S, 3, 6, 4, 'a')
multi_plot(fig, 2, S, 1, 3, 4, 'b')
multi_plot(fig, 3, S, 5, 4, 3, 'c')
multi_plot(fig, 4, S, 2, 4, 6, 'd')
multi_plot(fig, 5, S, 2, 3, 4, 'e')
multi_plot(fig, 6, S, 4, 5, 6, 'f')
multi_plot(fig, 7, S, 1, 3, 5, 'g')
multi_plot(fig, 8, S, 1, 2, 3, 'h')

plt.show()
