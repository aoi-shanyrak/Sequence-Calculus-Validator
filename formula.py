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
