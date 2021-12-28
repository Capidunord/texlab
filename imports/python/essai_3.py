from linear_algebra.render_row import render_row
from sympy import *

x, y, z = symbols('x, y, z')
result = render_row([S(2), S(0), S(2)], Matrix(3, 1, [x, y, z]))
print(result)