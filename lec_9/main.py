
import random

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = []

        for i in range(rows):
            a = []
            for j in range(columns):
                a.append(random.randint(0, 100))
            self.data.append(a)

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])
    def __add__(self, other):
        result=Matrix(self.rows,self.columns)
        result.data=[
            [
                self.data[i][j]+other.data[i][j]
                for j in range (self.columns)
            ]
            for i in range (self.rows)
        ]
        return result
    def __sub__(self, other):
        result=Matrix(self.rows,self.columns)
        result.data=[
            [
                self.data[i][j]-other.data[i][j]
                for j in range (self.columns)
            ]
            for i in range (self.rows)
        ]
        return result
    def __mul__(self, other):
        result=Matrix(self.rows,other.columns)
        result.data=[
            [
               sum(self.data[i][k]*other.data[k][i] for k in range(self.columns))
                for i in range(self.rows)
            ]
            for j in range(self.columns)
        ]
        return result
mymatrix = Matrix(3, 3)
mymatrix2=Matrix(3,3)
print("Matrix 1:")
print(mymatrix)
print("Matrix 2:")
print(mymatrix2)
print("Sum of matrixes")
print(mymatrix+mymatrix2)
print("Sub of matrixes")
print(mymatrix-mymatrix2)
print("Mul of matrixes")
print(mymatrix*mymatrix2)

