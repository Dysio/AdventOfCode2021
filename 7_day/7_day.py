input = 'input.txt'

def whale_part1(input):
    with open(input) as f:
        file = f.read()

    crabs_positions = list(map(int, file.split(',')))

    fuel_list = []
    for position in range(min(crabs_positions), max(crabs_positions) + 1):
        fuel = 0
        for crab in crabs_positions:
            fuel += abs(crab - position)
        fuel_list.append(fuel)

    min_fuel = min(fuel_list)
    return min_fuel

def sum_n(n):
    suma = 0
    for i in range(n+1):
        suma += i
    return suma

def whale_part2(input):
    with open(input) as f:
        file = f.read()

    crabs_positions = list(map(int, file.split(',')))

    fuel_list = []
    for position in range(min(crabs_positions), max(crabs_positions) + 1):
        fuel = 0
        for crab in crabs_positions:
            fuel += sum_n(abs(crab - position))
        fuel_list.append(fuel)

    min_fuel = min(fuel_list)
    return min_fuel

print(whale_part1(input))
print(whale_part2(input))
