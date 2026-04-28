import sys
import typing


def ft_ancien_text() -> None:
    if len(sys.argv) <= 1:
        print("Usage: ft_ancient_text.py <file>\n")
        return
    try:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        f: typing.IO = open(sys.argv[1])
        print("---\n")
        content = f.read()
        print(content)
        print("\n---")
        f.close()
        print(f"File '{sys.argv[1]}' closed.")
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    ft_ancien_text()
