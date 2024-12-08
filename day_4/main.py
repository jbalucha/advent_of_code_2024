from logic import WordSearchPart1, WordSearchPart2


def open_file_as_2d_array(file_name):
    with open(file_name, 'r') as file:
        return [list(line.strip()) for line in file]

if __name__ == '__main__':
    map = open_file_as_2d_array('inputs/input.txt')
    print("Part 1: ", WordSearchPart1(map).search("XMAS"))
    print("Part 2: ", WordSearchPart2(map).search())