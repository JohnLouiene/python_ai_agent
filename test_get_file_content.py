from functions.get_file_content import get_file_content
from config import MAX_CHARS

def test_not_verbose(working_directory, file_path):
    content = get_file_content(working_directory, file_path)
    truncate_text = f'[...File "{file_path}" truncated at {MAX_CHARS} characters]' 
    if truncate_text in content:
        print(truncate_text)
    print(len(content))

def test_verbose(working_directory, file_path):
    print(get_file_content(working_directory, file_path))

test_not_verbose("calculator", "lorem.txt")
test_verbose("calculator", "main.py")
test_verbose("calculator", "pkg/calculator.py")
test_verbose("calculator", "/bin/cat")
test_verbose("calculator", "pkg/does_not_exist.py")

