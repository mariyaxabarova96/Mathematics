from scipy.optimize import fsolve, broyden2


def equations(p):
    x,y = p
    f0 = x**2 - y**2 + 3*x*y*y*y - 2*x*x*y*y + 2*x - 3*y - 5
    f1 = 3*y*y*y - 2*x*x + 2*x*x*x*y - 5*x*x*y*y + 5
    return (f0, f1)

x, y = fsolve(equations, (0,0))
print(x, y)


