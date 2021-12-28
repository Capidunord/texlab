from sympy import Matrix, S, pprint
from linear_algebra.gauss_inversion import GaussInversion

A = Matrix([[1, 1], [1, -2]])
g = GaussInversion(A)

print(g.to_latex())
g.transvection(2, 1, -1)
g.multiply(2, -S(1)/3)
g.transvection(1, 2, -1)
print(g.to_latex())

pprint(A)