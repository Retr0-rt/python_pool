import os
import site
import sys


def print_outside_matrix() -> None:

    print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows")
    print("Then run this program again.")


def print_inside_matrix() -> None:

    venv_path: str = sys.prefix
    venv_name: str = os.path.basename(venv_path)

    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")

    site_packages: str = site.getsitepackages()[0]

    print("Package installation path:")
    print(site_packages)


if __name__ == "__main__":
    if sys.prefix != sys.base_prefix:
        print_inside_matrix()
    else:
        print_outside_matrix()
