from functions.run_python_file import run_python_file


def main() -> None:
    print("--- Test 1: main.py (Usage Instructions) ---")
    print(run_python_file("calculator", "main.py"))
    print()

    print("--- Test 2: main.py with expression '3 + 5' ---")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print()

    print("--- Test 3: tests.py ---")
    print(run_python_file("calculator", "tests.py"))
    print()

    print("--- Test 4: Path traversal '../main.py' ---")
    print(run_python_file("calculator", "../main.py"))
    print()

    print("--- Test 5: Nonexistent file ---")
    print(run_python_file("calculator", "nonexistent.py"))
    print()

    print("--- Test 6: Non-Python file 'lorem.txt' ---")
    print(run_python_file("calculator", "lorem.txt"))


if __name__ == "__main__":
    main()