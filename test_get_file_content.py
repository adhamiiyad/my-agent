from functions.get_file_content import get_file_content


def main() -> None:
    # 1. Lorem ipsum truncation test
    lorem_result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(lorem_result)}")
    print(f"lorem.txt truncated: {'truncated' in lorem_result}\n")

    # 2. Main script content test
    print("--- main.py ---")
    print(get_file_content("calculator", "main.py"))
    print()

    # 3. Package file content test
    print("--- pkg/calculator.py ---")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print()

    # 4. Out-of-bounds safety test
    print("--- /bin/cat ---")
    print(get_file_content("calculator", "/bin/cat"))
    print()

    # 5. Non-existent file test
    print("--- pkg/does_not_exist.py ---")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))


if __name__ == "__main__":
    main()