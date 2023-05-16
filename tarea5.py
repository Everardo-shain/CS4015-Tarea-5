import numpy as np
import math
from random import random
from random import gauss
from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def f(x1,x2,x3):
    f = x1+2*x2+x2*x3-x1**2-x2**2-x3**2
    return f

def comprobacion():
    a = np.array([[-2, 0, 0], [0, -2, 1], [0, 1, -2]])
    b = np.array([-1, -2, 0])
    sol = np.linalg.solve(a, b)
    print("Punto máximo real: \n",sol)
    print("Valor máximo real: \n",f(sol[0],sol[1],sol[2]))
    
def evol(u,v,w):
    plt.figure(1)
    plt.plot(u)
    plt.plot(v)
    plt.plot(w)
    plt.legend(('x1', 'x2', 'x3'))
    plt.ylim([-2,2])
    plt.show()
    
def mutation(x,s):
    xn = x + s*gauss(0,1)
    while xn < -2 or xn > 2:
        xn = x + s*gauss(0,1)
    return xn
def sigma(s, g, m):
    ps = m/g
    c = 0.817
    if g%20 == 0:
        if ps > 0.2:
            s = s/c
        elif ps < 0.2:
            s = s*c
    return s
def main():
    comprobacion()    
    #parámetros de simulación
    x1min, x1max, x2min, x2max, x3min, x3max  = [-2, 2, -2, 2, -2, 2]
    gmax = 500
    m = 0
    #individuo inicial
    x1 = 4*random()+x1min
    x2 = 4*random()+x2min
    x3 = 4*random()+x3min
    x1ix2ix3i = [round(x1,6),round(x2,6),round(x3,6)]
    print("Punto inicial:",x1ix2ix3i)
    #primer padre
    padre = f(x1,x2,x3)
    s = 1
    #registro de individuos
    u = [x1]
    v = [x2]
    w = [x3]
    #ciclo principal
    for g in range(1, gmax):
        x1n = mutation(x1,s)
        x2n = mutation(x2,s)
        x3n = mutation(x3,s)
        hijo = f(x1n,x2n,x3n)
        if hijo > padre:
            x1 = x1n
            x2 = x2n
            x3 = x3n
            m += 1
            padre = f(x1,x2,x3)
        s = sigma(s, g, m)
        u.append(x1)
        v.append(x2)
        w.append(x3)
    x1fx2fx3f = [round(x1,6),round(x2,6),round(x3,6)]
    print("Punto máximo calculado:",x1fx2fx3f)
    print("Valor máximo calculado:",padre)
    evol(u,v,w)


main()