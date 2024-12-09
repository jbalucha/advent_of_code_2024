from logic import Part1, Part2

def open_file(file_name):
    with open(file_name, 'r') as file:
        return file.readline().strip()

if __name__ == '__main__':
    f_input = open_file('inputs/input.txt')
    print("Part 1: ", Part1(f_input).solve())
    print("Part 2: ", Part2(f_input).solve())