from typing import Tuple, List
from dataclasses import dataclass

from symbols import AND, OR, IMPLICATION, NOT


class Formula:
    pass


@dataclass(frozen=True)
class Atom(Formula):
    name: str

    def __str__(self):
        return self.name


@dataclass(frozen=True)
class Not(Formula):
    arg: Formula

    def __str__(self):
        return NOT + str(self.arg)


@dataclass(frozen=True)
class And(Formula):
    left: Formula
    right: Formula

    def __str__(self):
        return "(" + str(self.left) + AND + str(self.right) + ")"


@dataclass(frozen=True)
class Or(Formula):
    left: Formula
    right: Formula

    def __str__(self):
        return "(" + str(self.left) + OR + str(self.right) + ")"


@dataclass(frozen=True)
class Implies(Formula):
    left: Formula
    right: Formula

    def __str__(self):
        return "(" + str(self.left) + IMPLICATION + str(self.right) + ")"


@dataclass(frozen=True)
class Sequent:
    left: Tuple[Formula, ...]
    right: Tuple[Formula, ...]


@dataclass
class ProofNode:
    sequent: Sequent
    rule: str
    premises: List["ProofNode"]
