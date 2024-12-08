from collections import defaultdict, deque

class Resolver:
    def __init__(self, rules: dict[int, set], sequences: list[list[int]]):
        self.rules = rules
        self.sequences = sequences

    def resolve(self, part: int) -> int:
        count = 0
        for sequence in self.sequences:
            if self._is_sequence_valid(sequence) and part == 1:
                print(sequence)
                count += self._middle_number_of_sequence(sequence)

            elif not self._is_sequence_valid(sequence) and part==2:
                print(sequence)
                sequence = self.reorder_sequence(sequence)
                count += self._middle_number_of_sequence(sequence)

        return count

    def reorder_sequence(self, sequence: list[int]) -> list[int]:
        graph = defaultdict(list)
        in_degree = {num: 0 for num in sequence}

        for num in sequence:
            for rule_num in self.rules.get(num, []):
                if rule_num in sequence:
                    graph[rule_num].append(num)
                    in_degree[num] += 1

        queue = deque([num for num in sequence if in_degree[num] == 0])
        sorted_sequence = []

        while queue:
            current = queue.popleft()
            sorted_sequence.append(current)
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return sorted_sequence

    def _is_sequence_valid(self, sequence: list[int]) -> bool:
        def is_rule_broken(rule, max_position):
            return not rule.isdisjoint(sequence[max_position:])

        for index, number in enumerate(sequence):
            if is_rule_broken(self.rules[number], index):
                return False

        return True

    @staticmethod
    def _middle_number_of_sequence(sequence: list[int]) -> int:
        middle_index = len(sequence) // 2
        return sequence[middle_index]