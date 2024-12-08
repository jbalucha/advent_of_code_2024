import copy
from itertools import combinations, permutations
from typing import List

from utils import PointPair


class AntiNodePredictor:
    def __init__(self, map_data: list[list[str]]):
        self.map = map_data
        self.frequencies = self.get_unique_frequencies()

    def get_unique_frequencies(self) -> set[str]:
        unique_chars = set(char for row in self.map for char in row)
        unique_chars.discard('.')
        return unique_chars

    def get_frequency_positions(self, frequency: str) -> list[tuple[int, int]]:
        return [(row, col) for row, line in enumerate(self.map) for col, char in enumerate(line) if char == frequency]

    def is_valid_anti_node_position(self, position: tuple[int, int]) -> bool:
        row, col = position
        return 0 <= col < len(self.map) and 0 <= row < len(self.map[0])

    def get_frequency_anti_node_positions(self, positions: list[tuple[int, int]]) -> list[tuple[int, int]]:
        point_pairs = [PointPair(point1, point2) for point1, point2 in list(permutations(positions, 2))]
        anti_node_positions = [pair.anti_node_position() for pair in point_pairs]
        return [position for position in anti_node_positions if self.is_valid_anti_node_position(position)]

    def get_frequency_anti_node_positions_part2(self, positions: list[tuple[int, int]]) -> list[tuple[int, int]]:
        point_pairs = [PointPair(point1, point2) for point1, point2 in list(permutations(positions, 2))]
        anti_node_positions = [antinode_position for pair in point_pairs for antinode_position in
                               pair.anti_node_positions_part2(len(self.map[0]), len(self.map))]
        return anti_node_positions

    def draw_map_with_antinodes(self, positions: List[tuple[int, int]]):
        map = copy.deepcopy(self.map)
        for anti_node in positions:
            if map[anti_node[0]][anti_node[1]] == '.':
                map[anti_node[0]][anti_node[1]] = '#'

        for row in map:
            print(''.join(row))

    def predict(self):
        global_anti_node_positions_part_1 = []
        global_anti_node_positions_part_2 = []

        for frequency in self.frequencies:
            positions = self.get_frequency_positions(frequency)
            anti_node_positions_part_1 = self.get_frequency_anti_node_positions(positions)
            anti_node_positions_part_2 = self.get_frequency_anti_node_positions_part2(positions)
            global_anti_node_positions_part_1.extend(anti_node_positions_part_1)
            global_anti_node_positions_part_2.extend(anti_node_positions_part_2)
            global_anti_node_positions_part_2.extend(positions)

            print(f"F:{frequency} with size {len(positions)} has "
                  f"(P1:{len(anti_node_positions_part_2)},"
                  f" P2:{len(anti_node_positions_part_2)}) "
                  f"antinodes")

        self.draw_map_with_antinodes(global_anti_node_positions_part_2)
        return len(set(global_anti_node_positions_part_1)), len(set(global_anti_node_positions_part_2))

