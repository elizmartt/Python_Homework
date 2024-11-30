import random


class Matrix:
    def __init__(self, rows, columns):
        self.n = rows
        self.m = columns
        self.matrix = []


        for i in range(rows):
            row = []
            for j in range(columns):
                row.append(random.randint(1, 100))
            self.matrix.append(row)


    def printMatrix(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.matrix[i][j], end=" ")
            print()


    def calculateMean(self):
        total = 0
        for i in range(self.n):
            for j in range(self.m):
                total += self.matrix[i][j]
        return total / (self.n * self.m)


    def sumRow(self, k):
        total = 0
        for j in range(self.m):
            total += self.matrix[k][j]
        return total
    def avColumn (self,l):
        sum=0
        for i in range(self.n):
            sum+=self.matrix[i][l]
        return sum/self.m
    def printSubMatrix(self,col1,col2,row1,row2):
        for i in range (row1,row2+1):
            for j in range (col1,col2+1):
                print(self.matrix[i][j],end=" ")
            print ()

n=int(input("Input the number of row"))
m=int(input("Input the number of columns"))
matrix = Matrix(n, m)
matrix.printMatrix()
k=int(input("Input the row to calculate the sum"))
l=int(input("Input the column to calculate the average of that column"))
print("Mean:", matrix.calculateMean())
print(f"Sum of row {k} :", matrix.sumRow(k))
print(f"Average of the column {l} :",matrix.avColumn(l))
col1=int(input("Input the first column of submatrix:"))
col2=int(input("Input the second column of submatrix :"))
row1=int(input("Input the first row of submatrix:"))
row2=int(input("Input the second row of submatrix :"))
print(f"The submatrix with columns {col1},{col2} and rows {row1},{row2}:")
matrix.printSubMatrix(col1,col2,row1,row2)