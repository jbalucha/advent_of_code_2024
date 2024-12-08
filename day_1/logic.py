class Part1:
    def __init__(self, list_a, list_b):
        self.list_a = list_a
        self.list_b = list_b

    def solve(self):
        list_a = self.sort_list(self.list_a)
        list_b = self.sort_list(self.list_b)
        distances = []

        for a, b in zip(list_a, list_b):
            distances.append(abs(a - b))

        return sum(distances)

    @staticmethod
    def sort_list(lst):
        return sorted(lst)

class Part2(Part1):
    def solve(self):
        sum = 0
        histogram_b = self.build_histogram(self.list_b)

        for a in self.list_a:
            if histogram_b.get(a, 0) > 0:
              sum += a * histogram_b[a]

        return sum


    @staticmethod
    def build_histogram(lst):
        histogram = {}
        for value in lst:
            if value in histogram:
                histogram[value] += 1
            else:
                histogram[value] = 1
        return histogram