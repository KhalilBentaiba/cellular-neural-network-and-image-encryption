def dx1(x1, x2, x3, x4, x5, x6):
    return - x3 - 1.2 * x4

def dx2(x1, x2, x3, x4, x5, x6):
    return 2 * x2 + x3

def dx3(x1, x2, x3, x4, x5, x6):
    return 11 * x1 - 12 * x2

def dx4(x1, x2, x3, x4, x5, x6):
    return 92 * x1 - 95 * x4 + x5 - x6 + 202 * (abs(x4 + 1) - abs(x4 - 1))

def dx5(x1, x2, x3, x4, x5, x6):
    return 5 * x3 - x5

def dx6(x1, x2, x3, x4, x5, x6):
    return 5 * x4 - 12 * x6


