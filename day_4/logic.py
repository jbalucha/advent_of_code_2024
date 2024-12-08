from typing import Any


class WordSearchPart1:
    def __init__(self, map_data):
        self.map = map_data
        self.rows = len(map_data)
        self.cols = len(map_data[0])
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    def search(self, target_word: str):
        count = 0
        for row in range(self.rows):
            for col in range(self.cols):
                for row_offset, col_offset in self.directions:
                    if self._search_from(row, col, row_offset, col_offset, target_word):
                        count += 1

        return count

    def _search_from(self, row: int, col: int, row_offset: int, col_offset: int, target_word: str) -> bool:
        for i in range(len(target_word)):
            r, c = row + row_offset * i, col + col_offset * i
            if r < 0 or r >= self.rows or c < 0 or c >= self.cols or self.map[r][c] != target_word[i]:
                return False
        return True

class WordSearchPart2(WordSearchPart1):
    def __init__(self, map_data):
        super().__init__(map_data)
        self.left_diagonal_offset = ((-1, 1), (1, -1))
        self.right_diagonal_offset = ((1, 1), (-1, -1))

    def search(self, target_word: str = None):
        count = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if not self.map[row][col] == 'A':
                    continue

                if self._correct_placement(row, col):
                    count += 1

        return count

    def _get_char(self, row: int, col: int) -> str | None:
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return None
        return self.map[row][col]

    def _correct_placement(self, row: int, col: int) -> bool:
        left_diagonal_chars = [self._get_char(row + offset[0], col + offset[1]) for offset in self.left_diagonal_offset]
        right_diagonal_chars = [self._get_char(row + offset[0], col + offset[1]) for offset in self.right_diagonal_offset]

        return True if set(left_diagonal_chars) == {'M', 'S'} and set(right_diagonal_chars) == {'M', 'S'} else False


