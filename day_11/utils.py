class ReadStream:
    def __init__(self, file_path, chunk_size=1024):
        self.file_path = file_path
        self.chunk_size = chunk_size
        self.file = None
        self.residue = ""
        self.words = []
        self.open()

    def open(self):
        self.file = open(self.file_path, "r", encoding="utf-8")

    def clear(self):
        """Clears the entire content of the file."""
        if self.file:  # Close the file if it is open
            self.file.close()
        with open(self.file_path, "w", encoding="utf-8") as file:  # Open in write mode
            file.truncate(0)  # Truncate the file to zero size
        self.file = None  # Reset file reference

    def close(self):
        if self.file:
            self.clear()
            self.file = None

    def read(self):
        if not self.file:
            self.open()

        chunk = self.file.read(self.chunk_size)
        if not chunk:
            return False

        chunk = self.residue + chunk
        self.words = chunk.split()

        if len(chunk) < self.chunk_size or chunk[-1].isspace():
            self.residue = ""
        else:
            self.residue = self.words.pop() if self.words else ""

        return True

    def read_word(self):
        while not self.words:
            if not self.read():
                return None

        return self.words.pop(0)

class WriteStream:
    def __init__(self, file_path):
        """
        Initialize the WriteStream instance.

        :param file_path: Path to the file to be written to
        """
        self.file_path = file_path
        self.file = None

    def open(self):
        self.file = open(self.file_path, "a", encoding="utf-8")

    def close(self):
        """Close the file."""
        if self.file:
            self.file.seek(max(0, self.file.tell() - 1), 0)  # Move the pointer back by 1 character
            self.file.truncate()  # Remove the last trailing space
            self.file.close()
            self.file = None

    def write_word(self, word):
        """
        Write a word to the file.

        :param word: The word to write to the file
        """
        if not self.file:
            self.open()

        self.file.write(word + " ")  # Write the word followed by a space