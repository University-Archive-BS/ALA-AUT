from fractions import Fraction
import numpy as np


def print_matrix(matrix, text=None):
    print(text)
    print(matrix.astype(str))


def return_vector(text="Enter Vector"):
    return list(map(Fraction, input(text + "\n").split()))


def create_matrix(c_vector, r_vector):
    matrix = np.zeros((len(c_vector), len(c_vector)), dtype=Fraction)
    matrix[:, 0] = c_vector
    matrix[0, 1:] = r_vector[1:]
    for r in range(1, len(c_vector)):
        for c in range(1, len(c_vector)):
            matrix[r, c] = matrix[r - 1, c - 1]
    print_matrix(matrix, "Toeplitz matrix is: ")
    return matrix


def echelon_form(matrix):
    u = np.copy(matrix)
    number_of_change = 0
    pivot = 0
    for r in range(matrix.shape[0]):
        temp = r
        while u[temp, pivot] == 0:
            temp += 1
            if u.shape[0] == temp:
                temp = r
                pivot += 1
                if u.shape[0] == pivot:
                    return False
        if temp != r:
            u[[temp, r]] = u[[r, temp]]
            number_of_change += 1
        for i in range(r + 1, matrix.shape[0]):
            if i != r:
                u[i] -= u[r] * (u[i, r] / u[r, r])
        pivot += 1
    print_matrix(u, "echelon form  is: ")
    return number_of_change, u


def calculate_det(matrix, n):
    det = Fraction(1)
    for i in range(matrix.shape[0]):
        det *= matrix[i, i]
    return det * Fraction(np.math.pow(-1, n))


matrix = create_matrix(return_vector("Enter Vector c:"), return_vector("Enter Vector r:"))
number_of_change, u_matrix = echelon_form(matrix)
print("det is: " + str(calculate_det(u_matrix, number_of_change)))
