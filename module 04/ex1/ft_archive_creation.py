import sys
import typing


def ft_archive_creation() -> None:
    if len(sys.argv) <= 1:
        print("Usage: ft_ancient_text.py <file>\n")
        return
    try:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{sys.argv[1]}'")
        f: typing.IO = open(sys.argv[1])
        print("---\n")
        content = f.read()
        print(content)
        print("\n---")
        f.close()
        print(f"File '{sys.argv[1]}' closed.\n")
        print("Transform data:")
        print("---\n")
        lines_list = []
        lines = content.splitlines()
        for line in lines:
            lines_list.append(f"{line}#")
            print(f"{line}#")
        print("\n---")
        file_name = input("Enter new file name (or empty): ")
        if file_name == "":
            print("Not saving data.")
            return
        else:
            print(f"Saving data to '{file_name}'")
            try:
                x = "\n".join(lines_list)
                f = open(file_name, "w")
                content = f.write(x)
                f.close()
                print(f"Data saved in file '{file_name}'.\n")
            except OSError as e:
                print(f"Error opening file '{file_name}': {e}")
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    ft_archive_creation()
