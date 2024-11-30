n = int(input("Enter the amount of numbers: "))


def classify():
    vector = []
    vecnoteven = []
    veceven = []

    for i in range(n):
        num = int(input(f"Enter the {i + 1} element: "))
        vector.append(num)

    for i in range(n):
        if vector[i] % 2 == 0:
            veceven.append(vector[i])
        else:
            vecnoteven.append(vector[i])

    return veceven, vecnoteven


veceven, vecnoteven = classify()

print("Even numbers are: ", veceven)
print("Not even numbers are: ", vecnoteven)