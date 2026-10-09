import ast
from pathlib import Path


def parse_file(file_path):
    source_code = Path(file_path).read_text(encoding="utf-8")

    tree = ast.parse(source_code)

    functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):

            parameters = []

            for arg in node.args.args:
                parameters.append(arg.arg)

            function_info = {
                "name": node.name,
                "parameters": parameters
            }

            functions.append(function_info)

    return functions


if __name__ == "__main__":
    result = parse_file("examples/calculator.py")

    for function in result:
        print("Function:", function["name"])
        print("Parameters:", function["parameters"])
        print()
        