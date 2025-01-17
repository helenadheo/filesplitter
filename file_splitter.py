import os

class FileSplitter:
    def __init__(self, filepath, part_size_mb):
        self.filepath = filepath
        self.part_size_mb = part_size_mb
        self.part_size_bytes = part_size_mb * 1024 * 1024

    def split_file(self):
        if not os.path.isfile(self.filepath):
            raise FileNotFoundError(f"The file {self.filepath} does not exist.")

        file_size = os.path.getsize(self.filepath)
        parts = file_size // self.part_size_bytes + (file_size % self.part_size_bytes > 0)

        with open(self.filepath, 'rb') as file:
            for part in range(parts):
                part_filename = f"{self.filepath}.part{part + 1}"
                with open(part_filename, 'wb') as part_file:
                    part_file.write(file.read(self.part_size_bytes))
                print(f"Created: {part_filename}")

if __name__ == "__main__":
    filepath = input("Enter the path of the file to split: ")
    part_size_mb = int(input("Enter the part size in MB: "))

    splitter = FileSplitter(filepath, part_size_mb)
    try:
        splitter.split_file()
    except Exception as e:
        print(f"An error occurred: {e}")