class Part1:
    def __init__(self, input_data):
        self.map_data = input_data
        self.moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    @property
    def starting_points(self):
        return [(i, j) for i, row in enumerate(self.map_data) for j, value in enumerate(row) if value == 0]

    def is_position_within_map(self, i, j):
        return 0 <= i < len(self.map_data) and 0 <= j < len(self.map_data[0])

    def allowed_moves(self, i, j):
        current_mark = self.map_data[i][j]
        new_positions = [(i + move[0], j + move[1]) for move in self.moves]

        for new_position in new_positions:
            if not self.is_position_within_map(*new_position):
                continue

            if self.map_data[new_position[0]][new_position[1]] != current_mark + 1:
                continue

            yield new_position

    def find_paths(self, i, j):
        visited_paths = set()

        if self._is_path_completed(i, j):
            visited_paths.add((i, j))
            return visited_paths

        for allowed_move in self.allowed_moves(i, j):
            visited_paths = visited_paths.union(self.find_paths(*allowed_move))

        return visited_paths

    def solve(self):
        total_paths = 0
        for start_point in self.starting_points:
            total_paths += len(self.find_paths(*start_point))

        return total_paths

    def _is_path_completed(self, i, j):
        return self.map_data[i][j] == 9

class Part2(Part1):
    def find_paths(self, i, j):
        complete_paths = 0

        if self._is_path_completed(i, j):
            return 1

        for allowed_move in self.allowed_moves(i, j):
            complete_paths += self.find_paths(*allowed_move)

        return complete_paths

    def solve(self):
        total_paths = 0
        for start_point in self.starting_points:
            total_paths += self.find_paths(*start_point)

        return total_paths