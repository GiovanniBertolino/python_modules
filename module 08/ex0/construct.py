import sys
import site
import os


def construct() -> None:
    is_venv = sys.prefix != sys.base_prefix
    if not is_venv:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual environment: None detect\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:\n")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows")
        print("\nThen run this program again.")
        return
    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")
    print("Package installation path:")
    print(f"{site.getsitepackages()[0]}")


if __name__ == "__main__":
    construct()
