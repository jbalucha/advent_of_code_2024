import copy
from utils import Direction, find_guard_position_and_rotation, GameOver, LoopDetected

class Map:
    def __init__(self, map_data):
        self.map_data = map_data
        self.current_position, self.current_rotation = find_guard_position_and_rotation(self.map_data)
        self.start_position = self.current_position
        self.previous_position, self.previous_rotation = (-1, -1), None
        self._max_y = len(self.map_data)
        self._max_x = len(self.map_data[0]) if self._max_y > 0 else 0
        self.visited_positions = set()


    def next_position(self):
        if self.current_rotation == Direction.UP:
            return self.current_position[0], self.current_position[1] - 1
        elif self.current_rotation == Direction.RIGHT:
            return self.current_position[0] + 1, self.current_position[1]
        elif self.current_rotation == Direction.DOWN:
            return self.current_position[0], self.current_position[1] + 1
        elif self.current_rotation == Direction.LEFT:
            return self.current_position[0] - 1, self.current_position[1]

    def is_loop_detected(self, next_x, next_y):
        return (next_x, next_y, self.current_rotation) in self.visited_positions

    def next_step(self, counter = 0):
        next_x, next_y = self.next_position()

        if next_y >= self._max_y or next_x >= self._max_x or next_y < 0 or next_x < 0:
            raise GameOver()
        elif self.is_loop_detected(next_x, next_y):
            raise LoopDetected(next_x, next_y)
        elif self.map_data[next_y][next_x] == '#':
            self.current_rotation = self.current_rotation.next_direction()
            return self.next_step(counter + 1)
        else:
            self.visited_positions.add((next_x, next_y, self.current_rotation))
            return next_x, next_y

    def previous_position_mark(self):
        if self.current_position == self.start_position:
            return self.map_data[self.current_position[1]][self.current_position[0]]
        elif self.previous_rotation != self.current_rotation:
            return '+'
        else:
            return self.current_rotation.value

    def make_step(self):
        self.previous_position = self.current_position
        self.current_position = self.next_step()
        self.map_data[self.previous_position[1]][self.previous_position[0]] = self.previous_position_mark()
        self.previous_rotation = self.current_rotation

    def print_map(self, map_data = None):
        map = map_data if map_data else self.map_data
        for row in map:
            print(''.join(row))
        print()

    def count_unique_positions(self, characters):
        return sum([row.count(char) for row in self.map_data for char in characters])

    def start_traversing(self):
        try:
            while True:
                self.make_step()

        except GameOver:
            # self.print_map()
            return self.count_unique_positions(['X', 'S', '+'] + Direction.all_values()) + 1

        except LoopDetected as e:
            raise e

class LoopDetector(Map):

    def __init__(self, map_data):
        super().__init__(map_data)
        self.default_map_data = copy.deepcopy(map_data)
        self.detected_loop_positions = set()

    def test_map_with_blocked_current_position(self):
        if self.current_position == self.start_position:
            return
        try:
            new_map = copy.deepcopy(self.default_map_data)
            new_map[self.current_position[1]][self.current_position[0]] = '#'
            Map(new_map).start_traversing()
        except LoopDetected:
            self.detected_loop_positions.add(self.current_position)

    def start_traversing(self):
        try:
            while True:
                self.make_step()
                self.test_map_with_blocked_current_position()

        except GameOver:
            return len(self.detected_loop_positions)

        except LoopDetected as e:
            raise e