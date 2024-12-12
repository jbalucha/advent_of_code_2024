from day_6.utils import open_file_as_2d_array
from logic import Part1, Part2

def open_file_as_2d_array(file_name):
    with open(file_name, 'r') as file:
        return [[int(char) for char in line.strip()] for line in file]

if __name__ == '__main__':
    f_input = open_file_as_2d_array('inputs/input.txt')
    print("Part 1: ", Part1(f_input).solve())
    print("Part 2: ", Part2(f_input).solve())