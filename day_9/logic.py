import copy

from day_9.utils import Memory


class Part1:
    def __init__(self, input_data):
        self.memory = Memory(input_data).as_list()
        self.next_free_space = -1

    def find_first_free_space(self, last_position):
        for i, value in enumerate(self.memory[last_position + 1:]):
            if value is None:
                return i + last_position + 1
        raise Exception('No free space available')

    def switch_with_free_space(self, position):
        self.memory[self.next_free_space] = self.memory[position]
        self.next_free_space = self.find_first_free_space(self.next_free_space)
        self.memory[position] = None

    def calculate_checksum(self):
        return sum(value * i for i, value in enumerate(self.memory) if value is not None)

    def solve(self):
        self.next_free_space = self.find_first_free_space(-1)

        for i, value in enumerate(reversed(self.memory)):
            if len(self.memory) - 1 - i <= self.next_free_space:
                break

            if value is None:
                continue
            self.switch_with_free_space(len(self.memory) - 1 - i)

        return self.calculate_checksum()

class Part2:
    def __init__(self, input_data):
        self.memory = Memory(input_data)

    def swap(self, allocated_block, empty_block, empty_block_index):
        new_block_params = (allocated_block.start, allocated_block.size)
        allocated_block.start = empty_block.start
        empty_block.decrease_size(allocated_block.size)
        self.memory.insert_new_empty_block(*new_block_params)

        if empty_block.is_empty():
            self.memory.empty_blocks.pop(empty_block_index)

    def calculate_checksum(self):
        return sum(value * i for i, value in enumerate(self.memory.as_list()) if value is not None)

    def solve(self):
        for allocated_block in reversed(self.memory.used_blocks):
            for i in range(len(self.memory.empty_blocks)):
                if self.memory.empty_blocks[i].start > allocated_block.start:
                    break

                elif self.memory.empty_blocks[i].fits(allocated_block):
                    self.swap(allocated_block, self.memory.empty_blocks[i], i)
                    break
            # print(self.memory.as_list())

        return self.calculate_checksum()
