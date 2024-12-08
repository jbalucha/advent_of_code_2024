from logic import Part1, Part2

def get_input_lists(file_path):
    list_a = []
    list_b = []

    with open(file_path, 'r') as file:
        for line in file:
            a, b = tuple(map(int, line.strip().split('   ')))
            list_a.append(a)
            list_b.append(b)
    return list_a, list_b

if __name__ == '__main__':
    l_a, l_b = get_input_lists('inputs/input.txt')
    print("Part 1: ", Part1(l_a, l_b).solve())
    print("Part 2: ", Part2(l_a, l_b).solve())