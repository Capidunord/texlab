from linear_algebra.linear_system import System
from sympy import Matrix, S, symbols


def test_can_remove_line():
    A = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    x, y, z = symbols('x y z')
    X = Matrix(3, 1, [x, y, z])
    Y = Matrix(3, 1, [1, 2, 3])
    mS = System(A, X, Y)

    mS.remove_line(3)

    assert mS.A.rows == 2
    assert mS.A == Matrix([[1,2,3], [4,5,6]])
    assert mS.Y == Matrix(2, 1, [1, 2])

def test_can_remove_line_2():
    A = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    x, y, z = symbols('x y z')
    X = Matrix(3, 1, [x, y, z])
    Y = Matrix(3, 1, [1, 2, 3])
    mS = System(A, X, Y)

    mS.remove_line(2)

    assert mS.A.rows == 2
    assert mS.A == Matrix([[1,2,3], [7,8,9]])
    assert mS.Y == Matrix(2, 1, [1, 3])

def test_can_remove_col():
    A = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    x, y, z = symbols('x y z')
    X = Matrix(3, 1, [x, y, z])
    Y = Matrix(3, 1, [1, 2, 3])
    mS = System(A, X, Y)

    mS.remove_col(3)

    assert mS.A.cols == 2
    assert mS.A == Matrix([[1,2], [4,5], [7, 8]])
    assert mS.X == Matrix(2, 1, [x, y])

def test_can_remove_col_2():
    A = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    x, y, z = symbols('x y z')
    X = Matrix(3, 1, [x, y, z])
    Y = Matrix(3, 1, [1, 2, 3])
    mS = System(A, X, Y)

    mS.remove_col(2)

    assert mS.A.cols == 2
    assert mS.A == Matrix([[1,3], [4,6], [7, 9]])
    assert mS.X == Matrix(2, 1, [x, z])