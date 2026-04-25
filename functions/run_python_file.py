import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)

        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        valid_target_dir = os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file_path]

        if args != None:
            command.extend(args)
        
        command_result = subprocess.run(command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30)
        
        output_string = ""

        if command_result.returncode != 0:
            output_string += f"Process exited with code {command_result.returncode}\n"

        if command_result.stdout == "" and command_result.stderr == "":
            output_string += f"No output produced\n"
        else:
            output_string += f"STDOUT: {command_result.stdout}\nSTDERR: {command_result.stderr}\n"

        return output_string

    except Exception as e:
        return f"Error: executing Python file: {e}"

#Schema to declare to an LLM how each function will be called.
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file located at the given path relative to the working directory. Optional CLI arguments can be passed to the script.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path executed to run a Python script, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional list of command-line arguments to pass to the Python script",
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Argument to be passed into a function",
                ),
            ),
        },
        required=["file_path"],
    ),
)
