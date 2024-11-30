def calculate(expression):
    def operate(a, b, operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                print("Devision by 0")
            return a / b
        else:
            print("That operator is not suported")
    def precedence(op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

    def apply_operations(numbers, operators):
        right = numbers.pop()
        left = numbers.pop()
        op = operators.pop()
        numbers.append(operate(left, right, op))

    numbers = []
    operators = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            numbers.append(num)
            continue
        elif expression[i] == '(':
            operators.append(expression[i])
        elif expression[i] == ')':
            while operators and operators[-1] != '(':
                apply_operations(numbers, operators)
            operators.pop()
        elif expression[i] in "+-*/":
            while (operators and operators[-1] != '(' and
                   precedence(operators[-1]) >= precedence(expression[i])):
                apply_operations(numbers, operators)
            operators.append(expression[i])
        i += 1


    while operators:
        apply_operations(numbers, operators)

    return numbers[0]



user_input = input("Enter an expression:").strip()
result = calculate(user_input)
print(f"Result:{result}")

