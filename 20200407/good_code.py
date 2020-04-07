"""DOCSTRING"""
import sys
import math

S = []
if __name__ == "__main__":
    for arg in sys.argv:
        S.append(arg)
A, B, C = int(S[1]), int(S[2]), int(S[3])
D = B ** 2 - 4 * A * C
if D < 0:
    print("No roots")
else:
    D = math.sqrt(D)
    X1 = (-B + D)/(2 * A)
    X2 = (-B - D)/(2 * A)
    if X1 < 0 and X2 < 0:
        print("No roots")
    elif X2 < 0:
        X = math.sqrt(X1)
        print(-X, X)
    elif X1 < 0:
        X = math.sqrt(X2)
        print(-X, X)
    else:
        X1, X2 = math.sqrt(X1), math.sqrt(X2)
        print(-X1, -X2, X1, X2)
