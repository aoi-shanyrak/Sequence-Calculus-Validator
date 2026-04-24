import re
from typing import List

from src.classes import Formula, Atom, Not, And, Or, Implies, Sequent

BRACKETS_NOT_AND_OR_ATOM_ALPHABET = r"\(|\)|~|&|\||->|[A-Za-z0-9]+"
ATOM_ALPHABET = r"[A-Za-z0-9]+"


def tokenize(s: str) -> List[str]:
    return re.findall(BRACKETS_NOT_AND_OR_ATOM_ALPHABET, s)


class Parser:
    def __init__(self, tokens):
        self.tokens: Formula = tokens
        self.pos: int = 0

    def peek(self) -> Formula:
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self) -> None:
        self.pos += 1

    def parse_implies(self) -> Formula:
        left = self.parse_or()
        if self.peek() == "->":
            self.consume()
            right = self.parse_implies()
            return Implies(left, right)
        return left

    def parse_or(self) -> Formula:
        left = self.parse_and()
        while self.peek() == "|":
            self.consume()
            right = self.parse_and()
            left = Or(left, right)
        return left

    def parse_and(self) -> Formula:
        left = self.parse_not()
        while self.peek() == "&":
            self.consume()
            right = self.parse_not()
            left = And(left, right)
        return left

    def parse_not(self) -> Formula:
        if self.peek() == "~":
            self.consume()
            return Not(self.parse_not())
        return self.parse_atom()

    def parse_atom(self) -> Formula:
        tok = self.peek()
        if tok == "(":
            self.consume()
            expr = self.parse_implies()
            self.consume()
            return expr
        if re.match(ATOM_ALPHABET, tok):
            self.consume()
            return Atom(tok)
        raise SyntaxError(f"Unexpected token: {tok}")


def parse_formula(s: str) -> Formula:
    tokens = tokenize(s)
    parser = Parser(tokens)
    return parser.parse_implies()


def parse(s: str) -> Sequent:
    if "|-" in s:
        left_str, right_str = s.split("|-", 1)
    else:
        raise SyntaxError("Missing |- in sequent")

    left_formula = parse_formula(left_str) if left_str else None
    right_formula = parse_formula(right_str) if right_str else None

    left_tuple = (left_formula,) if left_formula else ()
    right_tuple = (right_formula,) if right_formula else ()

    return Sequent(left_tuple, right_tuple)
