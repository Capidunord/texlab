from sympy import latex, Matrix, zeros
from general import expr
from .render_row import render_row


class System:
    def __init__(self, A, X, Y):
        self.A = A.copy()
        self.X = X.copy()
        self.Y = Y.copy()

    def to_latex(self):
        result = '\\left\\{\\begin{array}{' + \
                       'rc' * (self.A.cols - 1) + 'r' + 'cr' + '}\n'
        for i in range(0, self.A.rows):
            row = [self.A[i, j] for j in range(0, self.A.cols)]
            line = render_row(row, self.X)
            line += " & = & " + expr.platex(self.Y[i, 0])
            if i != self.A.rows - 1:
                line += ' \\\\'
            line += "\n"
            result += line
        result += "\\end{array}\\right."
        return result

    def transvection(self, row1, row2, factor=1):
        self.A[row1 - 1, :] += factor * self.A[row2 - 1, :]
        self.Y[row1 - 1, :] += factor * self.Y[row2 - 1, :]

    def multiply(self, row, l):
        self.A[row - 1, :] = self.A[row - 1, :] * l
        self.Y[row - 1, :] = self.Y[row - 1, :] * l

    def switch(self, row1, row2):
        temp = self.A[row1 - 1, :]
        self.A[row1 - 1, :] = self.A[row2 - 1, :]
        self.A[row2 - 1, :] = temp
        temp = self.Y[row1 - 1, :]
        self.Y[row1 - 1, :] = self.Y[row2 - 1, :]
        self.Y[row2 - 1, :] = temp

    @staticmethod
    def _remove_line_from_matrix(M: Matrix, line: int) -> Matrix:
        newM = zeros(M.rows - 1, M.cols)
        for i in range(1, M.rows):
            for j in range(1, M.cols + 1):
                if i < line:
                    newM[i-1,j-1] = M[i-1,j-1]
                else:
                    newM[i-1,j-1] = M[i, j-1]
        return newM

    def remove_line(self, line):
        self.A = System._remove_line_from_matrix(self.A, line)
        self.Y = System._remove_line_from_matrix(self.Y, line)

    @staticmethod
    def _remove_col_from_matrix(M: Matrix, col: int) -> Matrix:
        newM = zeros(M.rows, M.cols - 1)
        for i in range(1, M.rows + 1):
            for j in range(1, M.cols):
                if j < col:
                    newM[i-1,j-1] = M[i-1,j-1]
                else:
                    newM[i-1,j-1] = M[i-1, j]
        return newM

    def remove_col(self, col):
        self.A = System._remove_col_from_matrix(self.A, col)
        self.X = System._remove_line_from_matrix(self.X, col)

