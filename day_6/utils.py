from enum import Enum

class Direction(Enum):
    UP = '^'
    DOWN = 'v'
    LEFT = '<'
    RIGHT = '>'

    @staticmethod
    def all_values():
        directions = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]
        return [direction.value for direction in directions]

    def next_direction(self):
        if self == Direction.UP:
            return Direction.RIGHT
        elif self == Direction.RIGHT:
            return Direction.DOWN
        elif self == Direction.DOWN:
            return Direction.LEFT
        elif self == Direction.LEFT:
            return Direction.UP

def open_file_as_2d_array(file_name):
    with open(file_name, 'r') as file:
        return [list(line.strip()) for line in file]

def find_guard_position_and_rotation(map):
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell in ('>', '<', '^', 'v'):
                return (x, y), Direction(cell)

    raise ValueError("Guard not found in map")

class GameOver(Exception):
    pass

class LoopDetected(Exception):
    def __init__(self, next_x, next_y):
        self.next_x = next_x
        self.next_y = next_y
        super().__init__(f"Loop detected at position ({next_x}, {next_y})")
