import random

def generate_numbers():
    lines = []
    for i in range(100):
        line = []
        for i in range(20):
            if random.random() < 0.1:
                line.append(random.randint(41, 100))
            else:
                line.append(random.randint(1, 40))
        lines.append(line)
    return lines

def save(filename):
    lines = generate_numbers()
    with open(filename, 'w') as file:
        for line in lines:
            file.write(' '.join(map(str, line)) + '\n')

