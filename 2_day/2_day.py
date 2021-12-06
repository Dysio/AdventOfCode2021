input_file = "input.txt"

def day2_func_01(input_file):
    with open(input_file) as f:
        file = f.readlines()

    list_of_moves = []
    for line in file:
        list_of_moves.append((line.strip().split(" ")))

    vertical = 0
    horizontal = 0

    for elem in list_of_moves:
        if elem[0] == 'forward':
            horizontal += int(elem[1])
        elif elem[0] == 'down':
            vertical += int(elem[1])
        elif elem[0] == 'up':
            vertical -= int(elem[1])
        else:
            print('No input')

    answer = vertical * horizontal
    return vertical, horizontal, answer


def day2_func_02(input_file):
    with open(input_file) as f:
        file = f.readlines()

    list_of_moves = []
    for line in file:
        list_of_moves.append((line.strip().split(" ")))

    depth = 0
    horizontal = 0
    aim = 0

    for elem in list_of_moves:
        if elem[0] == 'forward':
            horizontal += int(elem[1])
            depth += aim * int(elem[1])
        elif elem[0] == 'down':
            aim += int(elem[1])
        elif elem[0] == 'up':
            aim -= int(elem[1])
        else:
            print('No input')

    answer = depth * horizontal
    return depth, horizontal, answer

vertical_01 = day2_func_01(input_file)[0]
horizontal_01 = day2_func_01(input_file)[1]
answer_01 = day2_func_01(input_file)[2]

result_02 = day2_func_02(input_file)
depth_02 = result_02[0]
horizontal_02 = result_02[1]
answer_02 = result_02[2]

print(f"Final position:\nvertical: {vertical_01}\nhorizontal: {horizontal_01}\nAnswer 1: {answer_01}\n")
print(f"Final position:\nvertical: {depth_02}\nhorizontal: {horizontal_02}\nAnswer 2: {answer_02}\n")
