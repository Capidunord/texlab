from linear_algebra.linear_system import System
from sympy import *

x, y, z = symbols('x, y, z')
A = Matrix([[1, 2, 3], [-4, 5, 6], [7, 8, 9]])
X = Matrix(3, 1, [x, y, z])
Y = zeros(3, 1)
mS = System(A, X, Y)

print(mS.to_latex())