import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = os.path.abspath(working_directory)

        target_directory = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        valid_target_dir = os.path.commonpath([working_dir_abs, target_directory]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_directory):
            return f'Error: File not found or is not a regular file: "{file_path}"' 

        with open(target_directory, "r") as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        
        return content

    except Exception as e:
        return f"Error: {e}"

#Schema to let the model access the get_file_content function and add it to its context.
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Returns the contents of a specified file relative to the working directory, providing a maximum character size of {MAX_CHARS}",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path used to open and read the contents of a file, relative to the working directory",
            ),
        },
        required=["file_path"],
    ),
)
