input = 'input.txt'

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

print(gamma_epsilon_rate(input))


