import math as m
import numpy as np
# По графическому методу локализации можно заметить, что корень между 0.5 и 1 => мы возьмем приближение х = 0.5
x = 0.5
for i in range(15):
    x0=x
    x = x - (x + m.log(x, 10) - 0.5) / (1 + 1 / (x * m.log(10, 10)))
    print(x)
    if abs(x0-x)<0.0001:
        break


# По графическому методу можно заметить, что корень в 3-ей четверти => мы возьмем приближение х = -0.5; y = -1
x = -0.5
y = -1

F1 = m.cos(y + 0.5) + x - 0.8
F2 = m.sin(x) - 2*y - 1.6

F1X = 1 # 1x1
F1Y = m.sin(y + 0.5) # 1x2
F2X = -m.cos(x) # 2x1
F2Y = -2 # 2x2
A = [
    [F1X, F1Y],
    [F2X, F2Y]
]
print(A)
print(np.linalg.inv(A))
A_inv = np.linalg.inv(A)
for i in range(100):
    x0 = x
    y0 = y
    x = x - A_inv[0][0] * F1 - A_inv[0][1] * F2
    y = y - A_inv[1][0] * F1 - A_inv[1][1] * F2

    F1 = m.cos(y + 0.5) + x - 0.8
    F2 = m.sin(x) - 2 * y - 1.6

    F1X = 1  # 1x1
    F1Y = m.sin(y + 0.5)  # 1x2
    F2X = -m.cos(x)  # 2x1
    F2Y = -2  # 2x2

    A = [
        [F1X, F1Y],
        [F2X, F2Y]
    ]
    A_inv = np.linalg.inv(A)
    print(x)
    print(y)
    if m.sqrt((x-x0)**2 + (y-y0)**2) < 0.0001:
        break

