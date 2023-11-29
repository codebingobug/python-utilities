# Bingo Utilities

This is a Python project hosted on GitHub, containing a collection of utility scripts.

## Installation

You can install this project directly from GitHub using pip:

```bash
pip install git+https://github.com/codebingobug/python-utilities.git
```

## Utilities

This project contains the following utility scripts:

- `file_logger.py`: (Get a logger with both stream and file handler)

```python
from bingo_utils.file_logger import get_logger_with_file

logger = get_logger_with_file('logger_name')
```

## Tests

Tests for each utility can be found in the `tests` directory. To run the tests, use the following command:

```bash
python -m unittest discover tests
```

## Requirements

This project requires Python 3.x and the packages listed in `requirements.txt`. You can install these packages using
pip:

```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Please read the contributing guidelines before making any changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
