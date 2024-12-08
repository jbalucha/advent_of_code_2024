from logic import Part1, Part2

def open_file_as_one_line(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()

if __name__ == '__main__':
    input = open_file_as_one_line('inputs/input.txt')
    print("Part 1: ", Part1(input).solve())
    print("Part 2: ", Part2(input).solve())