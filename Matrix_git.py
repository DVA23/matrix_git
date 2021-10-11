from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        strOut = ''
        for i in range(len(self.matrix)):
            strOut += "\t".join(map(str, self.matrix[i])) + '\n'
        return strOut[:-1]

    def size(self):
        return len(self.matrix), len(self.matrix[0])

# Task 1 check 1
m = Matrix([[1, 0], [0, 1]])
print(m)
m = Matrix([[2, 0, 0], [0, 1, 10000]])
print(m)
m = Matrix([[-10, 20, 50, 2443], [-5235, 12, 4324, 4234]])
print(m)
# OUTPUT:
# 1	0
# 0	1
# 2	0	0
# 0	1	10000
# -10	20	50	2443
# -5235	12	4324	4234

# Task 1 check 2
m1 = Matrix([[1, 0, 0], [1, 1, 1], [0, 0, 0]])
m2 = Matrix([[1, 0, 0], [1, 1, 1], [0, 0, 0]])
print(str(m1) == str(m2))
# OUTPUT:
# True

# Task 1 check 3
m = Matrix([[1, 1, 1], [0, 100, 10]])
print(str(m) == '1\t1\t1\n0\t100\t10')
# OUTPUT:
# True

# exec(stdin.read())
