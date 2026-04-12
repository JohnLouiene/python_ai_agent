import os

def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)

        target_directory = os.path.normpath(os.path.join(working_dir_abs, directory))
        
        valid_target_dir = os.path.commonpath([working_dir_abs, target_directory]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_directory):
            return f'Error: "{directory}" is not a directory'
        
        file_name_info = []
        for file_name in os.listdir(path=target_directory):
            file_path = f"{target_directory}/{file_name}"
            file_size = os.path.getsize(file_path)
            file_is_dir = os.path.isdir(file_path)
            file_name_info.append(f"- {file_name}: file_size={file_size}, is_dir={file_is_dir}")

        return "\n".join(file_name_info)
    
    except Exception as e:
        return f"Error: {e}"

