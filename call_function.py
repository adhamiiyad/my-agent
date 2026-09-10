import json
from typing import Any

from functions.get_file_content import get_file_content, schema_get_file_content
from functions.get_files_info import get_files_info, schema_get_files_info
from functions.run_python_file import run_python_file, schema_run_python_file
from functions.write_file import schema_write_file, write_file

available_functions = [
    schema_get_files_info,
    schema_get_file_content,
    schema_run_python_file,
    schema_write_file,
]


def call_function(
    tool_call: Any, working_directory: str = "calculator"
) -> str:
    function_name = tool_call.function.name
    args = json.loads(tool_call.function.arguments or "{}")

    if function_name == "get_files_info":
        directory = args.get("directory", ".")
        return get_files_info(working_directory, directory)

    elif function_name == "get_file_content":
        file_path = args.get("file_path", "")
        return get_file_content(working_directory, file_path)

    elif function_name == "run_python_file":
        file_path = args.get("file_path", "")
        python_args = args.get("args")
        return run_python_file(working_directory, file_path, python_args)

    elif function_name == "write_file":
        file_path = args.get("file_path", "")
        content = args.get("content", "")
        return write_file(working_directory, file_path, content)

    else:
        return f"Error: Unknown function '{function_name}'"