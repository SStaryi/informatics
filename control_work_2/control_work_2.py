from itertools import product


def formula(a, b, c):
    return (int)(not (b or c) and not (a and c))


def truth_table_for_3(f):
    print("A\tB\tC\tF(A, B, C)")

    for a, b, c in product([0, 1], repeat=3):
        print(a, "\t", b, "\t", c, "\t", f(a, b, c))
