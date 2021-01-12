from sympy.core.add import Add
from sympy import latex


def needs_parenthesis(expr):
    try:
        if expr.func == Add:
            return True
    except Exception as e:
        return False


def leading_minus(expr):
    if isinstance(expr.func, Add):
        if any([not leading_minus(sub_expr) for sub_expr in expr.args]):
            return False
        return True
    if str(expr)[0:1] == "-":
        return True
    return False


def platex(expr):
    result = latex(expr)
    if needs_parenthesis(expr):
        result = '\\left(' + result + '\\right)'
    return result
