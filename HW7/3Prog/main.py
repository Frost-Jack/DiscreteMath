from math import sqrt


def customSQRT(n, p):
    precision = 10 ** (-p)
    k = n - 1
    seq0 = 2
    seq1 = 2
    seq2 = 2 * seq1 + k * seq0

    while abs(seq2 / seq1 - seq1 / seq0) > precision:
        seq0 = seq1
        seq1 = seq2
        seq2 = 2 * seq1 + k * seq0

    return round(seq2 / seq1 - 1, p)


number = 123342
precision = 3

print("{val:0.{p}f}".format(p=precision, val=customSQRT(number, precision)))
print("{val:0.{p}f}".format(p=precision, val=sqrt(number)))
