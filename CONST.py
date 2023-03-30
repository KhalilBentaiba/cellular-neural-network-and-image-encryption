import Chens
import Lorenz

''' initial values '''

x1, x2, x3 = Chens.Key(0.1, 0.2, 0.3, 0.01, 490)
x4, x5, x6 = Lorenz.Key(0.1, 0.2, 0.3, 0.01, 490)

x1 /= 10
x2 /= 10
x3 /= 10
x4 /= 10
x5 /= 10
x6 /= 10

print(x1, x2, x3, x4, x5, x6)

h = 0.01