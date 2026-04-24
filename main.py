import sys

from parse import parse


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: python3 main.py *.txt")
        sys.exit(1)

    with open(sys.argv[1], "r") as inp:
        tokens = parse(inp)
        pass


if __name__ == "__main__":
    main()
