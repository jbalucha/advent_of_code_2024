from utils import parse_line

class Resolver:
    def __init__(self, file_name):
        self.file_name = file_name
        self.sum = 0

    def read_file_by_line(self):
        with open(self.file_name, 'r') as file:
            for line in file:
                yield line.strip()

    @staticmethod
    def solvable(result, numbers):
        def helper(current, index):
            if index == len(numbers):
                return current == result

            # Try adding the next number
            if helper(current + numbers[index], index + 1):
                return True

            # Try multiplying the next number
            if helper(current * numbers[index], index + 1):
                return True

            # Try concatenating the next number
            if helper(int(str(current) + str(numbers[index])), index + 1):
                return True

            return False

        if not numbers:
            return False

        return helper(0, 0)

    def resolve(self):
        for line in self.read_file_by_line():
            result, numbers = parse_line(line)
            if self.solvable(result, numbers):
                self.sum += result

        return self.sum
