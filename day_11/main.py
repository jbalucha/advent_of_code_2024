from logic import Part1, Part2

def open_file_as_2d_list(file_name):
    with open(file_name, 'r') as file:
        return [line.strip().split() for line in file]

if __name__ == '__main__':
    f_input = open_file_as_2d_list('inputs/test.txt')[0]
    print("Part 1: ", Part1(f_input).solve())
    print("Part 2: ", Part2(f_input).solve())