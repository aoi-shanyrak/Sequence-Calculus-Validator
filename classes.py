from typing import Tuple, List
from dataclasses import dataclass


class Formula:
    pass


@dataclass
class Atom(Formula):
    name: str


@dataclass
class Not(Formula):
    arg: Formula


@dataclass
class And(Formula):
    left: Formula
    right: Formula


@dataclass
class Or(Formula):
    left: Formula
    right: Formula


@dataclass
class Implies(Formula):
    left: Formula
    right: Formula


@dataclass
class Sequent:
    left: Tuple[Formula, ...]
    right: Tuple[Formula, ...]


@dataclass
class ProofNode:
    sequent: Sequent
    rule: str
    premises: List["ProofNode"]
