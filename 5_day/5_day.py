input = 'input.txt'
test = 'test.txt'

def part1(data):
    with open(data) as f:
        file = f.read()

    field_dict = dict()

    for line in file.splitlines():
        l,r = line.split(' -> ')
        x1, y1 = map(int, l.split(','))
        x2, y2 = map(int, r.split(','))
        if x1 == x2:
            for y in range(min(y1,y2), max(y1,y2) + 1):
                field_dict[(x1, y)] = field_dict.get((x1,y), 0) + 1
        elif y1 == y2:
            for x in range(min(x1,x2), max(x1,x2) +1):
                field_dict[(x, y1)] = field_dict.get((x,y1), 0) + 1

    points_overlap = 0
    for value in field_dict.values():
        if value > 1:
            points_overlap += 1

    return points_overlap

def part2(data):
    with open(data) as f:
        file = f.read()

    field_dict = dict()

    for line in file.splitlines():
        l,r = line.split(' -> ')
        x1, y1 = map(int, l.split(','))
        x2, y2 = map(int, r.split(','))
        if x1 == x2:
            for y in range(min(y1,y2), max(y1,y2) + 1):
                field_dict[(x1, y)] = field_dict.get((x1,y), 0) + 1
        elif y1 == y2:
            for x in range(min(x1,x2), max(x1,x2) +1):
                field_dict[(x, y1)] = field_dict.get((x,y1), 0) + 1
        elif abs(x1 - x2) == abs(y1 - y2) and x1 != x2 and y1 != y2:
            count = 1
            if x1 < x2:
                y = y1
                if y1 > y2:
                    count = -1
            else:
                y = y2
                if y2 > y1:
                    count = -1

            for x in range(min(x1, x2), max(x1, x2) + 1):
                field_dict[(x, y)] = field_dict.get((x, y), 0) + 1
                y += count

    points_overlap = 0
    for value in field_dict.values():
        if value > 1:
            points_overlap += 1

    return points_overlap

print(part1(input))
print(part2(input))

