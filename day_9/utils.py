class Block:
    def __init__(self, start, size, document_id=None):
        self.start = start
        self.size = size
        self.document_id = document_id

    def decrease_size(self, size):
        self.start += size
        self.size -= size

    def fits(self, block):
        return self.size >= block.size

    def is_empty(self):
        return self.size <= 0

    def __str__(self):
        return f'FreeBlock(id={self.document_id}, start={self.start}, size={self.size})'

class Memory:
    def __init__(self, input_data):
        self.input = input_data
        self.empty_blocks = []
        self.used_blocks = []
        self._load_input()

    def _load_input(self):
        memory_position = 0
        for i, data in enumerate(self.input):
            data = int(data)

            if data < 1:
                continue

            if i % 2:
                self.empty_blocks.append(Block(memory_position, data))
            else:
                self.used_blocks.append(Block(memory_position, data, int(i/2)))

            memory_position += data

    def insert_new_empty_block(self, start, size):
        for i, empty_block in enumerate(self.empty_blocks):
            # check for merging from the right
            if empty_block.start + empty_block.size == start:
                empty_block.size += size
                return
            # check for merging from the left
            elif empty_block.start - size == start:
                empty_block.size += size
                empty_block.start = start
                return
            # insert in between
            elif empty_block.start > start:
                self.empty_blocks.insert(i, Block(start, size))
                return

        # insert at the end
        self.empty_blocks.append(Block(start, size))

    def as_list(self):
        output = []
        blocks = sorted(self.used_blocks + self.empty_blocks, key=lambda x: x.start)
        for block in blocks:
            output.extend([block.document_id] * block.size)
        return output