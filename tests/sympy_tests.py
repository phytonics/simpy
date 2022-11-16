import np
from sympy import symbols

x, y, z = symbols("x y z")
x1, y1, x2, y2, x3, y3 = symbols("x1 y1 x2 y2 x3 y3")
vx1, vy1, vx2, vy2, vx3, vy3 = symbols("vx1 vy1 vx2 vy2 vx3 vy3")
m1, m2, m3 = symbols("m1 m2 m3")


z = np.array(((x1, y1), (x2, y2), (x3, y3), (vx1, vy1), (vx2, vy2), (vx3, vy3)))

m = np.array((m1, m2, m3))

G = 1
t = [0, 1]

