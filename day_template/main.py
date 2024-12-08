from logic import Part1, Part2

def open_file_as_2d_list(file_name):
    with open(file_name, 'r') as file:
        return [list(map(int, line.strip().split())) for line in file]

if __name__ == '__main__':
    input = open_file_as_2d_list('inputs/test.txt')
    print("Part 1: ", Part1(input).solve())
    print("Part 2: ", Part2(input).solve())