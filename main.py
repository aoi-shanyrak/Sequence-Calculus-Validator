import sys

from parse import parse
from validator import prove
from print_proof import proof_to_str


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: python3 main.py *.txt *.txt")
        sys.exit(1)

    with open(sys.argv[1], "r") as inp:
        with open(sys.argv[2], "w") as out:
            content = inp.read()
            sequent = parse(content)
            proof = prove(sequent)
            out.write(proof_to_str(proof))


if __name__ == "__main__":
    main()
