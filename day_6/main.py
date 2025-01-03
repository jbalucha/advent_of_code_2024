import argparse
import utils

from logic import Part2, Part1

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process a map file.')
    parser.add_argument('--file', type=str, default='inputs/input.txt', help='The map file to process')
    parser.add_argument('--part', type=int, default=1, choices=[1, 2], help='Part of the task to execute (1 or 2)')

    args = parser.parse_args()

    if args.part == 1:
        map = Part1(utils.open_file_as_2d_array(args.file))
    else:
        map = Part2(utils.open_file_as_2d_array(args.file))

    print(map.start_traversing())