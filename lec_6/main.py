import random

def generate_random_matrix(n, m):
    array = [[random.randint(0, 100) for _ in range(m)] for _ in range(n)]
    return array


def get_column_sum(array, n, column_index):
    column_sum = 0
    for i in range(n):
        column_sum += array[i][column_index]
    return column_sum

def row_average(array, row_index):
    row_sum = 0
    for value in array[row_index]:
        row_sum += value
    return row_sum / len(array[row_index])


n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

array = generate_random_matrix(n, m)
print("Generated Matrix:")
for row in array:
    print(row)

column_index = int(input("Enter the column index (0 to  to sum: "))

column_sum = get_column_sum(array, n, column_index)
print(f"Sum of column {column_index}: {column_sum}")

row_index = int(input(f"Enter the row index to average: "))

average = row_average(array, row_index)
print(f"Average of row {row_index}: {average:.2f}")