input_file = "input.txt"

with open(input_file, 'r') as f:
    file = f.readlines()

a = int(file[0].strip())
increased_1 = 0

for line in file:
    b =  int(line.strip())
    if b > a:
        increased_1 += 1
    a = b

print(f"puzzle1: {increased_1}")

increased_2 = 0

input_list = []
for line in file:
    input_list.append(int(line.strip()))

for elem in range(len(input_list) - 2):
    sum1 = sum(input_list[elem:elem+3])
    sum2 = sum(input_list[elem+1:elem+4])
    if sum2 > sum1:
        increased_2 += 1

print(f"puzzle2: {increased_2}")
