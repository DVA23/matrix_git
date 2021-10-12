from sys import stdin
from copy import deepcopy


# create class MatrixError
class MatrixError(BaseException):
    def __init__(self, matrix, other):
        self.matrix1 = matrix
        self.matrix2 = other


# create class Matrix
class Matrix:
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    # create function for print matrix
    def __str__(self):
        strOut = ''
        for i in range(len(self.matrix)):
            strOut += "\t".join(map(str, self.matrix[i])) + '\n'
        return strOut[:-1]

    # create function for size matrix
    def size(self):
        return len(self.matrix), len(self.matrix[0])

    # create function for sum two matrix (Matrix + Matrix)
    # add function that shows error message if two matrix have different size
    def __add__(self, other):
        if self.size() == other.size():
            new_matrix = [map(sum, zip(*i))
                          for i in zip(self.matrix, other.matrix)]
        else:
            raise MatrixError(self, other)
        return Matrix(new_matrix)

    # create function for multiply matrix and number (Matrix * num)
    def __mul__(self, other):
        new_matrix = deepcopy(self.matrix)
        for i in range(len(new_matrix)):
            for j in range(len(new_matrix[i])):
                new_matrix[i][j] *= other
        return Matrix(new_matrix)

    # create function for multiply matrix and number (num * Matrix)
    __rmul__ = __mul__

    # create function for transpose matrix
    def transpose(self):
        trans_matrix = []
        for i in range(len(self.matrix[0])):
            trans_matrix.append(list())
            for j in range(len(self.matrix)):
                trans_matrix[i].append(self.matrix[j][i])
        self.matrix = trans_matrix
        return Matrix(self.matrix)

    # create function for transpose matrix with static method
    @staticmethod
    def transposed(matrix):
        trans_matrix = []
        for i in range(len(matrix.matrix[0])):
            trans_matrix.append(list())
            for j in range(len(matrix.matrix)):
                trans_matrix[i].append(matrix.matrix[j][i])
        return Matrix(trans_matrix)


# Task 1 check 1
# m = Matrix([[1, 0], [0, 1]])
# print(m)
# m = Matrix([[2, 0, 0], [0, 1, 10000]])
# print(m)
# m = Matrix([[-10, 20, 50, 2443], [-5235, 12, 4324, 4234]])
# print(m)
# OUTPUT:
# 1	0
# 0	1
# 2	0	0
# 0	1	10000
# -10	20	50	2443
# -5235	12	4324	4234

# Task 1 check 2
# m1 = Matrix([[1, 0, 0], [1, 1, 1], [0, 0, 0]])
# m2 = Matrix([[1, 0, 0], [1, 1, 1], [0, 0, 0]])
# print(str(m1) == str(m2))
# OUTPUT:
# True

# Task 1 check 3
# m = Matrix([[1, 1, 1], [0, 100, 10]])
# print(str(m) == '1\t1\t1\n0\t100\t10')
# OUTPUT:
# True

# # Task 2 check 1
# m = Matrix([[10, 10], [0, 0], [1, 1]])
# print(m.size())
# OUTPUT:
# (3, 2)

# Task 2 check 2
# m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
# m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
# print(m1 + m2)
# OUTPUT:
# 1     1   0
# 20	1	-1
# -1	-2	1

# # Task 2 check 3
# m = Matrix([[1, 1, 0], [0, 2, 10], [10, 15, 30]])
# alpha = 15
# print(m * alpha)
# print(alpha * m)
# OUTPUT:
# 15	15	0
# 0	30	150
# 150	225	450
# 15	15	0
# 0	30	150
# 150	225	450

# # Task 3 check 1
# # Check exception to add method
m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)

m2 = Matrix([[0, 1, 0], [20, 0, -1]])
try:
    m = m1 + m2
    print('WA\n' + str(m))
except MatrixError as e:
    print(e.matrix1)
    print(e.matrix2)
# OUTPUT:
# 1	1	0
# 20	1	-1
# -1	-2	1
# 1	0	0
# 0	1	0
# 0	0	1
# 0	1	0
# 20	0	-1

# # Task 3 check 2
m = Matrix([[10, 10], [0, 0], [1, 1]])
print(m)
m1 = m.transpose()
print(m)
print(m1)
# OUTPUT:
# 10	10
# 0	0
# 1	1
# 10	0	1
# 10	0	1
# 10	0	1
# 10	0	1

# # Task 3 check 3
m = Matrix([[10, 10], [0, 0], [1, 1]])
print(m)
print(Matrix.transposed(m))
print(m)
# OUTPUT:
# 10	10
# 0	0
# 1	1
# 10	0	1
# 10	0	1
# 10	10
# 0	0
# 1	1

# exec(stdin.read())
