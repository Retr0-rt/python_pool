import sys


def main() -> None:
    print("=== Command Quest ===")

    print(f"Program name: {sys.argv[0]}")

    total_args = len(sys.argv)
    args_received = total_args - 1

    if args_received == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {args_received}")
        index = 1
        for arg in sys.argv[1:]:
            print(f"Argument {index}: {arg}")
            index += 1

    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    main()
