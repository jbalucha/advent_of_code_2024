class Part1:
    def __init__(self, input):
        self.input = input

    def solve(self):
        safe_reports = 0
        for report in self.input:
            if self.is_safe(report):
                safe_reports += 1

        return safe_reports

    def is_safe(self, report):
        if not self.is_sorted(report):
            return False

        if not self.safe_diff_between_numbers(report, 1, 3):
            return False

        return True

    @staticmethod
    def safe_diff_between_numbers(report, min, max):
        for i in range(1, len(report)):
            if not min <= abs(report[i] - report[i - 1]) <= max:
                return False
        return True

    @staticmethod
    def is_sorted(report):
        def is_ascending():
            return all(report[i] <= report[i + 1] for i in range(len(report) - 1))

        def is_descending():
            return all(report[i] >= report[i + 1] for i in range(len(report) - 1))

        return is_ascending() or is_descending()


class Part2(Part1):
    def report_has_one_mistake(self, report):
        for i in range(len(report)):
            if self.is_safe(report[:i] + report[i + 1:]):
                return True
        return False

    def solve(self):
        safe_reports = 0
        for report in self.input:
            if self.is_safe(report) or self.report_has_one_mistake(report):
                safe_reports += 1


        return safe_reports