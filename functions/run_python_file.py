import os
import subprocess

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
