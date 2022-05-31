import math as m
def Create_good_matrix(number):
    N = number
    A = [
        [N+2, 1, 1, N+4],
        [1, N+4, 1, N+6],
        [1, 1, N+6, N+8]
    ]
    return A


def norm(X):
    norm = 0
    for i in range(len(X)):
        norm += X[i]*X[i]
    return m.sqrt(norm)


def Create_bad_matrix(number):
    N = number
    eps = 0.0001
    dim = 7
    A = []
    for i in range(dim):
        A.append([])
        for j in range(dim + 1):
            A[i].append(0)
    for i in range(dim):
        for j in range(dim + 1):
            if i == j:
                A[i][j] = 1 + eps * N
            elif i < j and j != dim:
                A[i][j] = -1 - eps * N
            elif i > j:
                A[i][j] = eps * N
            else:
                A[i][j] = -1
    A[dim - 1][dim] = 1
    return A


def gauss(A):
    dim = len(A)
    count = 0
    swap = count + 1
    while count < dim:
        current = A[count][count]
        if A[count][count] != 0:
            swap = count + 1
            for i in range(dim + 1):
                A[count][i] /= current
            for i in range(count + 1, dim):
                b = A[i][count]
                for j in range(dim + 1):
                    A[i][j] = A[i][j] - b * A[count][j]
            count += 1
            swap += 1
        elif swap <= dim:
            swap_massive=A[count]
            A[count] = A[swap]
            A[swap] = swap_massive
            swap += 1
        else:
            print("Determinant of matrix = 0")
    return A


N = 8
A = Create_good_matrix(N)
print(A)
solution = gauss(A)
print(solution)

A = Create_bad_matrix(N)
def zeidel(A):

    dim = len(A)
    for i in range(dim):
        for j in range(dim + 1):
            if j == dim:
                A[i][j] /= A[i][i]
            elif i != j:
                A[i][j] = (-A[i][j])/A[i][i]
        A[i][i] = 0

    X = []
    for i in range(dim):
        X.append(0.5)
    norm_X = norm(X)
    iterations = 0
    norm_X0 =10123
    while abs(norm_X - norm_X0) > 0.0001:
        for i in range(dim):
            norm_X0 = norm_X
            X[i] = 0
            for j in range(dim):
                X[i] += A[i][j] * X[j]
            X[i] += A[i][dim]
            norm_X = norm(X)
            iterations += 1

    print(iterations)
    return X
solution = zeidel(A)
print(solution)