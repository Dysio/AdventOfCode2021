#dict that shows how many segments are needed to create a number number:no_of_seg
numb_dict = {1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
data = "input.txt"

def part1(data):
    with open(data) as f:
        file = f.readlines()

    counter = 0
    for line in file:
        len_list = list(map(len, line.split(" | ")[1].strip().split(" ")))
        tot_leng = (1 for ch in len_list if ch in (2,3,4,7))
        counter += sum(tot_leng)

    return counter

def part2(data):
    with open(data) as f:
        file = f.readlines()

    numbers_list = []
    for line in file:
        code_list = line.split(" | ")[1].strip().split(" ")
        # print(code_list)
        # number = ''.join(list(map(decode, code_list)))
        # numbers_list.append(int(number))
        number = "".join(map(str, (decode(num) for num in code_list)))
        numbers_list.append(number)
    return sum(numbers_list)

def decode(code:str):
    code_dict = {}
    if len(code) == 2:
        code_dict[1] = code
    if len(code) == 3:
        code_dict[7] = code
    if len(code) == 4:
        code_dict[4] = code
    if len(code) == 7:
        code_dict[8] = code

    a = code_dict[7] - code_dict[1]
    bd = code_dict[4] - code_dict[1]
    eg = code_dict[8] - code_dict[7] - bd

    if len(code) == 5 and eg in code:
        code_dict[2] = code
    if len(code) == 5 and code[1] in code:
        code_dict[3] = code
    if len(code) == 5 and bd in code:
        code_dict[5] = code
    if len(code) == 6 and code_dict[3] in code:
        code_dict[9] = code
    if len(code) == 6 and code_dict[1] in code:
        code_dict[0] = code
    if len(code) == 6:
        code_dict[6] = code

    return code_dict

if __name__ == '__main__':
    # print(part1(data))
    print(part2("test.txt"))
    code = "acedgfb"
