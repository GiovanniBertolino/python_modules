def secure_archive(
        file: str,
        action: str = "r",
        to_write: str | None = None) -> tuple:
    try:
        with open(file, action) as f:
            if action == 'w':
                f.write(to_write)
                data = "Content successfully written to file"
            if action == 'r':
                data = f.read()
            return (True, data)
    except OSError as e:
        return (False, str(e))


def ft_vault_security() -> None:
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    file1 = "/not/existing/file"
    file2 = "/etc/master.passwd"
    file3 = "test.txt"
    print(f"{secure_archive(file1)}\n")
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(f"{secure_archive(file2)}\n")
    print("Using 'secure_archive' to read from a regular file:")
    print(f"{secure_archive(file3)}\n")
    res = secure_archive(file3)
    content = res[1]
    print("Using 'secure_archive' to write previous content to a new file:")
    print(f"{secure_archive(file3, 'w', content)}")


if __name__ == "__main__":
    ft_vault_security()
