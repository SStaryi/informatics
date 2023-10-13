from itertools import product


def formula_1(x1, x2, x3, x4, x5):
    return (int)(
        (x2 and x3 and x4 and x5) or (x1 and (not x3) and x4 and x5) or ((not x2) and x3 and (not x4)
                                                                         and x5) or (
                (not x1) and x2 and (not x4) and x5) or ((not x1) and (not x2) and x3 and x4 and
                                                         (not x5)) or (
                x1 and (not x2) and (not x3) and (not x4) and (not x5)) or (x1 and x2 and x3
                                                                            and (not x4) and (not x5)))


def formula_2(x1, x2, x3, x4, x5):
    return (int)((x1 or x2 or x3) and (x1 or (not x2) or x3 or (not x4)) and (x1 or (not x2) or (not
                                                                                                 x3) or x5) and (
                         (not x1) or x2 or (not x3) or x5) and ((not x1) or (not x2) or x3 or x4) &
                 ((not x1) or (not x2) or (not x3) or x5) and (x1 or x2 or (not x3) or x4 or x5) and (x1 or x2
                                                                                                      or (not x3) or (
                                                                                                          not x4) or (
                                                                                                          not x5)) and (
                         x1 or (not x2) or x3 or x4 or x5) and ((not x1) or x2
                                                                or x3 or x4 or (not x5)) and (
                         (not x1) or x2 or x3 or (not x4) or x5) and ((not x1) or (not x2)
                                                                      or x3) or (not x4) or x5)


def the_truth_table_for_5(f):
    print("x1\tx2\tx3\tx4\tx5\tG(x1, x2, x3, x4, x5)")

    for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
        print(x1, "\t", x2, "\t", x3, "\t", x4, "\t", x5, "\t", f(x1, x2, x3, x4, x5))


# Возвращает значение обратное a
def denial(a):
    return not a


# Возвращает результат конъюнкции между числами a и b
def conjuction(a, b):
    return a and b


# Возвращает результат дизъюнкции между числами a и b
def desjunction(a, b):
    return a or b


# Возвращает результат исключающего или между числами a и b
def exclusive_or(a, b):
    return a ^ b


# Возвращает результат эквивалентности между числами a и b
def equivalence(a, b):
    return a == b


# Возвращает результат импликации между числами a и b
def implication(a, b):
    return (not a) or b


# Возвращает результат штриха Шеффера между числами a и b
def schaeffers_stroke(a, b):
    return not (a and b)


# Возвращает результат стрелки Пирса между числами a и b
def pier_arrow(a, b):
    return not (a or b)
