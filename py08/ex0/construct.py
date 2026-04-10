import sys
import site


def no_venv():
    print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.prefix}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!\n"
          "The machines can see everything you install\n")
    print("To enter the construct, run:\n"
          "python -m venv matrix_env\n"
          "source matrix_env/bin/activate # On Unix\n"
          "matrix_env\\Scripts\\activate # On Windows\n")
    print("Then run this program again.")


def with_venv():
    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.prefix}")
    print(f"Virtual Environment: {sys.prefix.split("\\")[-1]}\n")
    print(f"Environment Path: {"\\".join(sys.prefix.split("\\")[:-1])}\n")
    print("SUCCESS: You're in an isolated environment!\n"
          "Safe to install packages without affecting\n"
          "the global system.\n")
    print("Package installation path:\n"
          f"{site.getsitepackages()[1]}\n")


if __name__ == "__main__":
    if sys.prefix != sys.base_prefix:
        with_venv()
    else: 
        no_venv()