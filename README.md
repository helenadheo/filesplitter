# FileSplitter

FileSplitter is a Python program designed to split large files into smaller, more manageable parts for easier sharing and storage on Windows systems. This can be particularly useful for transferring files that exceed size limits on email or other sharing platforms.

## Features

- Splits files into smaller parts based on user-defined size in megabytes (MB).
- Provides console output indicating the completion of each file part.
- Handles errors such as file not found.

## Requirements

- Python 3.x

## Installation

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/yourusername/FileSplitter.git
   ```
2. Navigate to the project directory.
   ```bash
   cd FileSplitter
   ```

## Usage

1. Run the program using Python.
   ```bash
   python file_splitter.py
   ```
2. Enter the path of the file you wish to split when prompted.
3. Enter the desired size for each part in megabytes (MB).

The program will create new files with .part1, .part2, etc. appended to the original filename, indicating the sequence of the parts.

## Example

```bash
Enter the path of the file to split: example.zip
Enter the part size in MB: 50
```

This will split `example.zip` into parts of 50 MB each.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.