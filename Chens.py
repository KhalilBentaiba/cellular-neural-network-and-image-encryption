import numpy as np
import matplotlib.pyplot as plt

def dx1(x, y, z, a=35., b=3., c=28.):
    return a * (y - x)

def dx2(x, y, z, a=35., b=3., c=28.):
    return (c - a) * x - x * z + c * y

def dx3(x, y, z, a=35., b=3., c=28.):
    return x * y - b * z


def RungeKutta(x1, x2, x3, h):

        ''' step one '''

        k0 = h * dx1(x1, x2, x3)
        l0 = h * dx2(x1, x2, x3)
        q0 = h * dx3(x1, x2, x3)

        ''' step two '''

        k1 = h * dx1(x1 + k0 / 2, x2 + l0 / 2, x3 + q0 / 2)
        l1 = h * dx2(x1 + k0 / 2, x2 + l0 / 2, x3 + q0 / 2)
        q1 = h * dx3(x1 + k0 / 2, x2 + l0 / 2, x3 + q0 / 2)

        ''' step three '''

        k2 = h * dx1(x1 + k1 / 2, x2 + l1 / 2, x3 + q1 / 2)
        l2 = h * dx2(x1 + k1 / 2, x2 + l1 / 2, x3 + q1 / 2)
        q2 = h * dx3(x1 + k1 / 2, x2 + l1 / 2, x3 + q1 / 2)

        ''' step four '''

        k3 = h * dx1(x1 + k2, x2 + l2, x3 + q2)
        l3 = h * dx2(x1 + k2, x2 + l2, x3 + q2)
        q3 = h * dx3(x1 + k2, x2 + l2, x3 + q2)

        ''' step five '''

        x1 += (k0 + 2 * k1 + 2 * k2 + k3) / 6
        x2 += (l0 + 2 * l1 + 2 * l2 + l3) / 6
        x3 += (q0 + 2 * q1 + 2 * q2 + q3) / 6

        return x1, x2, x3


def Key(x, y, z, h, iterations):
    #s1 = np.zeros(iterations, dtype=np.float64)
    #s2 = np.zeros(iterations, dtype=np.float64)
    #s3 = np.zeros(iterations, dtype=np.float64)

    for _ in range(300):
        x, y, z = RungeKutta(x, y, z, h)

    for i in range(iterations):
        x, y, z = RungeKutta(x, y, z, h)
        #s1[i] = x
        #s2[i] = y
        #s3[i] = z

    return x, y, z


#x = 0.1
#y = 0.2
#z = 0.3
#h = 0.01
#iterations = 1
#
#s1, s2, s3 = Sequances(x, y, z, h, iterations)
#print(s1, s2, s3)
##plt.plot(s2, s3, linewidth=0.1)
#
#fig = plt.figure()
#ax = plt.axes(projection ='3d')
#ax.plot3D(s1, s2, s3, linewidth=0.1)
#ax.set_title("Chen's 3D")
#plt.show()