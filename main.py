import numpy as np


# #12 - override this if you must
def f(x):
    return x / (x ** 3 + 8)


true_result = -0.006294843240543572
#

x0 = -1
xk = 1
h = 0.5
h_2 = 0.25


def rectangles_method(f, a, b, dx=0.1):
    n = (b - a) // dx
    result = 0

    for i in range(int(n)):
        result += dx * f(a + i * dx)
    return result


def trapezoid_method(f, a, b, dx=0.1):
    n = (b - a) // dx
    n = int(n)
    xi = np.linspace(a, b, n + 1)
    result = 0
    for i in range(0, n):
        result += (f(xi[i]) + f(xi[i + 1])) / 2 * dx
    return result


def simpson_method(f, a, b, dx=0.1):
    n = (b - a) // dx
    xi = np.linspace(a, b, int(n) + 1)

    result = 0
    for i in range(1, int(n / 2) + 1):
        result += f(xi[i * 2 - 2]) + \
                  4 * f(xi[i * 2 - 1]) + \
                  f(xi[i * 2])

    return dx / 3 * result


print(f'True result is {true_result}')
print()

r1 = rectangles_method(f, x0, xk, h)
r2 = rectangles_method(f, x0, xk, h_2)
print(f'rectangles method for step {h} yields: {r1} ({(r1 - true_result) * 100 / true_result:.2f}% error)')
print(f'rectangles method for step {h_2} yields: {r2} ({(r2 - true_result) * 100 / true_result:.2f}% error)')
p = 1
r12 = r2 + (r2-r1)/(2**p-1)
print(f'rectangles*runge method yields: {r12} ({(r12 - true_result) * 100 / true_result:.2f}% error)')
print()

t1 = trapezoid_method(f, x0, xk, h)
t2 = trapezoid_method(f, x0, xk, h_2)
print(f'trapezoid method for step {h} yields: {t1} ({(t1 - true_result) * 100 / true_result:.2f}% error)')
print(f'trapezoid method for step {h_2} yields: {t2} ({(t2 - true_result) * 100 / true_result:.2f}% error)')
p = 2
t12 = t2 + (t2-t1)/(2**p-1)
print(f'trapezoid* method yields: {t12} ({(t12 - true_result) * 100 / true_result:.2f}% error)')
print()

s1 = simpson_method(f, x0, xk, h)
s2 = simpson_method(f, x0, xk, h_2)
p = 4
s12 = s2 + (s2-s1)/(2**p-1)
print(f'simpson method for step {h} yields: {s1} ({(s1 - true_result) * 100 / true_result:.2f}% error)')
print(f'simpson method for step {h_2} yields: {s2} ({(s2 - true_result) * 100 / true_result:.2f}% error)')

print(f'simpson* method yields: {s12} ({(s12 - true_result) * 100 / true_result:.2f}% error)')
