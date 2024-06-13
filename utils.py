import re
from pathlib import Path


def list_files_in_directory(directory):
    dir_path = Path(directory)
    files = [file.name for file in dir_path.iterdir() if file.is_file()]
    return files


def find_first_python_code(input_string):
    """
    This function finds and returns the first code block enclosed in ```python``` in the input string.

    :param input_string: The string containing the python code blocks.
    :return: A string representing the first python code block, or None if no block is found.
    """
    pattern = r"```python(.*?)```"
    match = re.search(pattern, input_string, re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        return None
