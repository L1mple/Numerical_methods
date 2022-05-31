import math as m
count = 1
w0 = m.sqrt(1 + m.atan(0.8*0.1 + 0.2))
comp = []
for i in range(10, 21, 1):
    i = i * 0.01
    F =  m.sqrt(1 + m.atan(0.8*i + 0.2)) * m.exp(2*i + 1)
    comp.append(F)
    #print(count, F)
    count += 1
p = 0
count = 1
ryad = []
i = 0.1
for i in range(10,21,1):
    i = i * 0.01
    arc = 1
    x = 0.8 * i + 0.2
    y = 2 * i + 1
    w0 = 10
    k = 0
    while abs((-1)**(k)*(x**(2*k+1))/(2*k + 1)) > 10**(-6)/4/1.74:
        arc += ((-1)**(k))*(x**(2*k+1))/((2*k + 1))
        k += 1
    e = 0
    n = 0
    while abs((y**(n))/m.factorial(n)) > 10**(-6)/4/1.1599:
        e += (y**(n))/m.factorial(n)
        n += 1
    w1 = 0.5 * (w0 + arc / w0)
    while abs(w1 - w0) > 10**(-6)/2/1.332:
        swap = w1 
        w1 = 0.5 * (w1 + arc / w1)
        w0 = swap
    F =  w1 * e
    ryad.append(F)
    #print(count, F, i)
    count += 1
for i in range(10,21):
    print((i)*0.01, comp[i-10], ryad[i-10])