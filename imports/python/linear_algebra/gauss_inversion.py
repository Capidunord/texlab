from typing import Any, Optional
from sympy.core.function import ArgumentIndexError
from sympy.core.symbol import symbols

from .render_row import render_row
from enum import Enum
from sympy import Matrix, eye


class ActionMode(Enum):
    LINES = "LINES"
    COLUMNS = "COLUMNS"


class GaussInversion:
    def __init__(
        self,
        A: Matrix,
        action_mode: ActionMode = ActionMode.LINES,
        B: Optional[Matrix] = None,
        X: Optional[Matrix] = None,
        Y: Optional[Matrix] = None,
    ) -> None:
        self.A = A.copy()
        self.B = B.copy() if B else eye(self.A.rows)

        def generate_symbols(prefix, size):
            result = []
            for k in range(1, size + 1):
                result.append(symbols(prefix + "_" + str(k)))
            return Matrix(size, 1, result)

        self.X = X.copy() if X else generate_symbols("x", A.rows)
        self.Y = Y.copy() if Y else generate_symbols("y", A.rows)
        self.action_mode = action_mode

    def to_latex(self) -> str:
        table_headers = "rc" * self.A.rows + "c" + "rc" * self.B.rows
        result = ""

        for i in range(0, self.A.rows):
            row_A = [self.A[i, j] for j in range(self.A.cols)]
            line = render_row(row_A, self.X)
            row_B = [self.B[i, j] for j in range(self.B.cols)]
            line += " & = & " + render_row(row_B, self.Y)
            result += line
            if i != self.A.rows - 1:
                result += " \\\\\n"

        return (
            "\\left\\{\\begin{array}{"
            + table_headers
            + "}\n"
            + result
            + "\n\\end{array}\\right."
        )

    def transvection(self, i: int, j: int, l: Any) -> None:
        if self.action_mode == ActionMode.LINES:
            for k in range(0, self.A.cols):
                self.A[i-1, k] = self.A[i - 1, k] + l * self.A[j - 1, k]
                self.B[i-1, k] = self.B[i - 1, k] + l * self.B[j - 1, k]
        elif self.action_mode == ActionMode.COLUMNS:
            for k in range(0, self.A.rows):
                self.A[k, i-1] = self.A[k, i - 1] + l * self.A[k, j-1]
                self.B[k, i-1] = self.B[k, i - 1] + l * self.B[k, j-1]
        else:
            raise ArgumentIndexError()

    def multiply(self, i: int, l: Any) -> None:
        if self.action_mode == ActionMode.LINES:
            for k in range(0, self.A.cols):
                self.A[i-1, k] = l * self.A[i-1, k]
                self.B[i-1, k] = l * self.B[i-1, k]
        elif self.action_mode == ActionMode.COLUMNS:
            for k in range(0, self.A.rows):
                self.A[k, i-1] = l * self.A[k, i-1]
                self.B[k, i-1] = l * self.B[k, i-1]
        else:
            raise ArgumentIndexError()

    def switch(self, i: int, j: int) -> None:
        if self.action_mode == ActionMode.LINES:
            for k in range(0, self.A.cols):
                temp = self.A[i-1, k]
                self.A[i-1, k] = self.A[j - 1, k]
                self.A[j - 1, k] = temp
                temp = self.B[i-1, k]
                self.B[i-1, k] = self.B[j - 1, k]
                self.B[j - 1, k] = temp
        elif self.action_mode == ActionMode.COLUMNS:
            for k in range(0, self.A.row):
                temp = self.A[k, i-1]
                self.A[k, i-1] = self.A[k, j - 1]
                self.A[k, j - 1] = temp
                temp = self.B[k, i-1]
                self.B[k, i-1] = self.B[k, j - 1]
                self.B[k, j - 1] = temp
        else:
            raise ArgumentIndexError()

