from CNN import *

def RungeKutta(x1, x2, x3, x4, x5, x6, h):

        ''' step one '''

        k0 = h * dx1(x1, x2, x3, x4, x5, x6)
        l0 = h * dx2(x1, x2, x3, x4, x5, x6)
        q0 = h * dx3(x1, x2, x3, x4, x5, x6)
        r0 = h * dx4(x1, x2, x3, x4, x5, x6)
        s0 = h * dx5(x1, x2, x3, x4, x5, x6)
        t0 = h * dx6(x1, x2, x3, x4, x5, x6)

        ''' step two '''

        k1 = h * dx1(x1 + k0 / 2, x2 + l0 / 2, x3 + q0 / 2, x4 + r0 / 2, x5 + s0 / 2, x6 + t0 / 2)
        l1 = h * dx2(x1 + k0 / 2, x2 + l0 / 2, x3 + q0 / 2, x4 + r0 / 2, x5 + s0 / 2, x6 + t0 / 2)
        q1 = h * dx3(x1 + k0 / 2, x2 + l0 / 2, x3 + q0 / 2, x4 + r0 / 2, x5 + s0 / 2, x6 + t0 / 2)
        r1 = h * dx4(x1 + k0 / 2, x2 + l0 / 2, x3 + q0 / 2, x4 + r0 / 2, x5 + s0 / 2, x6 + t0 / 2)
        s1 = h * dx5(x1 + k0 / 2, x2 + l0 / 2, x3 + q0 / 2, x4 + r0 / 2, x5 + s0 / 2, x6 + t0 / 2)
        t1 = h * dx6(x1 + k0 / 2, x2 + l0 / 2, x3 + q0 / 2, x4 + r0 / 2, x5 + s0 / 2, x6 + t0 / 2)

        ''' step three '''

        k2 = h * dx1(x1 + k1 / 2, x2 + l1 / 2, x3 + q1 / 2, x4 + r1 / 2, x5 + s1 / 2, x6 + t1 / 2)
        l2 = h * dx2(x1 + k1 / 2, x2 + l1 / 2, x3 + q1 / 2, x4 + r1 / 2, x5 + s1 / 2, x6 + t1 / 2)
        q2 = h * dx3(x1 + k1 / 2, x2 + l1 / 2, x3 + q1 / 2, x4 + r1 / 2, x5 + s1 / 2, x6 + t1 / 2)
        r2 = h * dx4(x1 + k1 / 2, x2 + l1 / 2, x3 + q1 / 2, x4 + r1 / 2, x5 + s1 / 2, x6 + t1 / 2)
        s2 = h * dx5(x1 + k1 / 2, x2 + l1 / 2, x3 + q1 / 2, x4 + r1 / 2, x5 + s1 / 2, x6 + t1 / 2)
        t2 = h * dx6(x1 + k1 / 2, x2 + l1 / 2, x3 + q1 / 2, x4 + r1 / 2, x5 + s1 / 2, x6 + t1 / 2)

        ''' step four '''

        k3 = h * dx1(x1 + k2, x2 + l2, x3 + q2, x4 + r2, x5 + s2, x6 + t2)
        l3 = h * dx2(x1 + k2, x2 + l2, x3 + q2, x4 + r2, x5 + s2, x6 + t2)
        q3 = h * dx3(x1 + k2, x2 + l2, x3 + q2, x4 + r2, x5 + s2, x6 + t2)
        r3 = h * dx4(x1 + k2, x2 + l2, x3 + q2, x4 + r2, x5 + s2, x6 + t2)
        s3 = h * dx5(x1 + k2, x2 + l2, x3 + q2, x4 + r2, x5 + s2, x6 + t2)
        t3 = h * dx6(x1 + k2, x2 + l2, x3 + q2, x4 + r2, x5 + s2, x6 + t2)

        ''' step five '''

        x1 += (k0 + 2 * k1 + 2 * k2 + k3) / 6
        x2 += (l0 + 2 * l1 + 2 * l2 + l3) / 6
        x3 += (q0 + 2 * q1 + 2 * q2 + q3) / 6
        x4 += (r0 + 2 * r1 + 2 * r2 + r3) / 6
        x5 += (s0 + 2 * s1 + 2 * s2 + s3) / 6
        x6 += (t0 + 2 * t1 + 2 * t2 + t3) / 6

        return x1, x2, x3, x4, x5, x6


