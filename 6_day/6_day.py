input = 'input.txt'

def read_data(input):
    with open(input) as f:
        file = f.read()
    input_list = list(map(int, file.split(',')))

    return input_list

def lanternfish_part1(input:str, days: int):
    input_list = read_data(input)
    for day in range(1, days+1):
        length = len(input_list)
        for x in range(len(input_list)):
            if input_list[x] > 0:
                input_list[x] -= 1
            elif input_list[x] == 0:
                input_list.append(8)
                input_list[x] = 6
    return len(input_list)

def lanternfish_part2(input:str, days: int):
    input_list = read_data(input)
    fish_dict = {}
    for fish in input_list:
        fish_dict[fish] = fish_dict.get(fish, 0) + 1


    return fish_dict

# print(lanternfish_part1(input, 80))
print(lanternfish_part2('test.txt', 2))

