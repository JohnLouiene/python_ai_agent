import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        working_dir_abs = os.path.abspath(working_directory)

        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        valid_target_dir = os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory' 
        
        if os.path.isdir(target_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        parent_directory = os.path.dirname(target_file_path)
        os.makedirs(parent_directory, exist_ok=True)

        with open(target_file_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"

#Schema to let the model access the write_file function and add it to its context.
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrites the contents of the specified file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path used to open and overwrite the contents of a file, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="A string that will overwrite the contents of the specified file"
            ),
        },
        required=["file_path", "content"],
    ),
)
