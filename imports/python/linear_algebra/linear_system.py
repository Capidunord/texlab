from sympy import latex
from general import expr


class System:
    def __init__(self, A, X, Y):
        self.A = A
        self.X = X
        self.Y = Y

    def to_latex(self):
        result = latex('\left\\{\\begin{array}{' +
                       'rc' * (self.A.cols - 1) + 'r' + 'cr' + '}\n')
        for i in range(0, self.A.rows):
            line_started = False
            line = ""
            for j in range(0, self.A.cols):
                if j == 0:
                    if self.A[i, j] == 0:
                        pass
                    else:
                        if self.A[i, j] == -1:
                            line += latex(' - ') + expr.platex(self.X[j, 0])
                        elif self.A[i, j] == 1:
                            line += expr.platex(self.X[j, 0])
                        else:
                            line += expr.platex(self.A[i, j]) + \
                                " " + expr.platex(self.X[j, 0])
                        line_started = True
                    line += " & "
                else:
                    if self.A[i, j] == 0:
                        line += " & "
                        if not line_started and j == self.A.cols - 1:
                            line += " 0 "
                    else:
                        if not expr.leading_minus(self.A[i, j]) > 0:
                            if line_started:
                                line += latex(" + & ")
                            else:
                                line += latex(" & ")
                            if self.A[i, j] == 1:
                                line += expr.platex(self.X[j, 0])
                            else:
                                line += expr.platex(self.A[i, j]) + \
                                    " " + expr.platex(self.X[j, 0])
                            line_started = True
                        else:
                            if line_started:
                                line += expr.platex(" - & ")
                                if self.A[i, j] == -1:
                                    line += expr.platex(self.X[j, 0])
                                else:
                                    line += expr.platex(-self.A[i, j]) + \
                                        " " + expr.platex(self.X[j, 0])
                            else:
                                line += latex(" & ")
                                if self.A[i, j] == -1:
                                    line += latex(" - ") + \
                                        expr.platex(self.X[j, 0])
                                else:
                                    line += expr.platex(self.A[i, j]) + \
                                        " " + expr.platex(self.X[j, 0])
                            line_started = True
                    line += " & "
            line += latex(" = & ") + expr.platex(self.Y[i, 0])
            if i != self.A.rows - 1:
                line += latex(' \\\\')
            line += "\n"
            result += line
        result += latex("\\end{array}\\right.")
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
