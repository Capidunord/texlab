from general import expr

def render_row(row, X):
    line_started = False
    line = ""
    for j in range(0, len(row)):
        if j == 0:
            if row[j] == 0:
                pass
            else:
                if row[j] == -1:
                    line += ' - ' + expr.platex(X[j, 0])
                elif row[j] == 1:
                    line += expr.platex(X[j, 0])
                else:
                    line += expr.platex(row[j]) + \
                        " " + expr.platex(X[j, 0])
                line_started = True
        else:
            line += " & "
            if row[j] == 0:
                if not line_started and j == len(row) - 1:
                    line += " 0 "
                line += " & "
            else:
                if not expr.leading_minus(row[j]) > 0:
                    if line_started:
                        line += " + & "
                    else:
                        line += " & "
                    if row[j] == 1:
                        line += expr.platex(X[j, 0])
                    else:
                        line += expr.platex(row[j]) + \
                            " " + expr.platex(X[j, 0])
                    line_started = True
                else:
                    if line_started:
                        line += " - & "
                        if row[j] == -1:
                            line += expr.platex(X[j, 0])
                        else:
                            line += expr.platex(-row[j]) + \
                                " " + expr.platex(X[j, 0])
                    else:
                        line += " & "
                        if row[j] == -1:
                            line += " - " + \
                                expr.platex(X[j, 0])
                        else:
                            line += expr.platex(row[j]) + \
                                " " + expr.platex(X[j, 0])
                    line_started = True
    return line