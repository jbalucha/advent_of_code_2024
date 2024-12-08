import re


class Part1:
    def __init__(self, data):
        self.data = data

    def find_correct(self):
        pattern = r'(mul\((\d{1,3}),(\d{1,3})\))'
        matches = re.findall(pattern, self.data)
        return matches

    def solve(self):
        correct_statements = self.find_correct()
        # print([statement for statement, _, _ in correct_statements])
        multiply_results = [int(a) * int(b) for _, a, b in correct_statements]
        return sum(multiply_results)


class Part2(Part1):

    def find_correct(self):
        pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
        matches = [(int(match.group(1)) * int(match.group(2)), match.start()) for match in re.finditer(pattern, self.data)]
        return matches

    def find_disabled_blocks(self):
        do_pattern = r'do\(\)'
        dont_pattern = r'don\'t\(\)'
        do_matches = [match.start() for match in re.finditer(do_pattern, self.data)]
        dont_matches = [match.start() for match in re.finditer(dont_pattern, self.data)]

        disabled_blocks = []
        for dont_position in dont_matches:
            do_position = next((do for do in do_matches if do > dont_position), len(self.data))
            disabled_blocks.append((dont_position, do_position))

        return disabled_blocks

    def solve(self):
        correct_statements_group = self.find_correct()
        disabled_blocks = self.find_disabled_blocks()

        enabled_statements = []
        for value, start in correct_statements_group:
            if not any(dont <= start < do for dont, do in disabled_blocks):
                enabled_statements.append(value)

        return sum(enabled_statements)