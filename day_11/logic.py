import os

from day_11.utils import ReadStream, WriteStream

class Part1:
    def __init__(self, input_data):
        self.starting_arrangement = input_data

    def mutate(self, number):
        if number == "0":
            return ["1"]
        elif not len(number) % 2:
            return [str(int(number[:len(number)//2])), str(int(number[len(number)//2:]))]
        else:
            return [str(int(number) * 2024)]

    def solve(self, blinks=25):
        arrangement = self.starting_arrangement
        for blink in range(blinks):
            new_arrangement = []
            for position in range(len(arrangement)):
                new_numbers = self.mutate(arrangement[position])
                new_arrangement.extend(new_numbers)
            arrangement = new_arrangement
            # print(blink)
        return len(arrangement)

class Part2(Part1):
    def __init__(self, input_data):
        super().__init__(input_data)
        self.curr_arrangement_path = 'inputs/temp1.txt'
        self.new_arrangement_path = 'inputs/temp2.txt'
        self.curr_arrangement_stream = ReadStream(self.curr_arrangement_path)
        self.new_arrangement_stream = WriteStream(self.new_arrangement_path)

    def rename_files(self):
        try:
            temp_path = self.curr_arrangement_path + ".tmp"
            os.rename(self.curr_arrangement_path, temp_path)
            os.rename(self.new_arrangement_path, self.curr_arrangement_path)
            os.rename(temp_path, self.new_arrangement_path)

        except Exception as e:
            print(f"An error occurred: {e}")

    def reset_streams(self):
        self.curr_arrangement_stream.close()
        self.new_arrangement_stream.close()
        self.rename_files()
        self.curr_arrangement_stream.open()
        self.new_arrangement_stream.open()


    def solve(self, blinks = 75):
        for blink in range(blinks):
            while number := self.curr_arrangement_stream.read_word():
                self.new_arrangement_stream.write_word(' '.join(self.mutate(number)))
            self.reset_streams()
            print(blink)
        word_count = 0
        while self.curr_arrangement_stream.read_word():
            word_count += 1

        return word_count
