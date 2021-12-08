def bin_to_dec(num: str):
    number = 0
    for elem in range(1, len(num) + 1):
        number += int(num[-elem]) * 2 ** (elem - 1)
    return number

def gamma_epsilon_rate(data):
    with open(data) as f:
        file = f.readlines()

    num_rate = [0 for digit in file[0].strip()]
    counter = 0
    for line in file:
        counter += 1
        for i in range(len(line.strip())):
            num_rate[i] += int(line.strip()[i])

    gamma_rate = ''
    epsilon_rate = ''
    for i in range(len(num_rate)):
        if num_rate[i] > counter // 2:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    gamma_rate = bin_to_dec(gamma_rate)
    epsilon_rate = bin_to_dec(epsilon_rate)
    result = gamma_rate * epsilon_rate

    return gamma_rate, epsilon_rate, result


def oxygen_co2_rating(data, value:str):
    with open(data) as f:
        file = f.readlines()

    num_list = file

    if value == 'oxygen':
        for digit in range(len(file[0].strip())):
            list_zero = []
            list_one = []
            for num in num_list:
                if num[digit] == "1":
                    list_one.append(num)
                elif num[digit] == "0":
                    list_zero.append(num)
            if len(list_one) > len(list_zero):
                num_list = list_one
            elif len(list_one) < len(list_zero):
                num_list = list_zero
            else:
                num_list = list_one
            if len(num_list) == 1:
                break
    else:
        for digit in range(len(file[0].strip())):
            list_zero = []
            list_one = []
            for num in num_list:
                if num[digit] == "1":
                    list_one.append(num)
                elif num[digit] == "0":
                    list_zero.append(num)
            if len(list_one) < len(list_zero):
                num_list = list_one
            elif len(list_one) > len(list_zero):
                num_list = list_zero
            else:
                num_list = list_zero
            if len(num_list) == 1:
                break

    return bin_to_dec(num_list[0].strip())


if __name__ == '__main__':
    input = 'input.txt'

    print(gamma_epsilon_rate(input))

    oxygen_generator_rating = oxygen_co2_rating(input, 'oxygen')
    co2_scrubber_rating = oxygen_co2_rating(input, 'co2')
    print(f'oxygen generator rating = {oxygen_generator_rating}')
    print(f'co2 scrubber rating = {co2_scrubber_rating}')
    print(f'life support rating = {oxygen_generator_rating * co2_scrubber_rating}')