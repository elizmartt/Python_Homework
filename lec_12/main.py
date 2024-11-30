import time
from number_generator import save

save('main.txt')
numbers40 = []
def execution_time_decorator(func):
    print("Decorator created")
    def wrapper(*args, **kwargs):
       print(f"Executing {func.__name__}")
       start_time = time.time()
       result = func(*args, **kwargs)
       end_time = time.time()
       print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
       return result
    return wrapper
with open('main.txt', 'r') as file:
    all_numbers = []
    for line in file:
        line = line.strip()
        if line:
            try:
                numbers = [int(num) for num in line.split() if num.isdigit()]
                all_numbers.extend(numbers)
            except ValueError as e:
                print(f"Skipping line")
                continue
@execution_time_decorator
def filter_numbers(numbers):
    filtered = [num for num in numbers if num > 40]
    return filtered

with open('main.txt', 'a') as file:
    file.write("\nFiltered Numbers (greater than 40):\n")
    numbers40 = filter_numbers(all_numbers)
    for num in numbers40:
        file.write(str(num) + " ")

def generator(file, limit):
    count = 1
    for line in file:
        if count > limit:
            break
        yield count
        count += 1

with open('main.txt', 'r') as file:
    generator(file,100)


