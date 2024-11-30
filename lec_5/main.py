def sum_of_elements(numbers, exclude_negative):
    if exclude_negative:
        numbers = [nums for nums in numbers if nums >= 0]

    return sum(numbers)


numbers_input = input("Enter a list of numbers : ")
numbers = list(map(int, numbers_input.split()))

exclude_negative_input = input("Do you want to exclude negative numbers? yes/no: ")

if exclude_negative_input == "yes":
    exclude_negative = True
elif exclude_negative_input == "no":
    exclude_negative = False


result = sum_of_elements(numbers, exclude_negative)

print(f"The sum of the elements is: {result}")