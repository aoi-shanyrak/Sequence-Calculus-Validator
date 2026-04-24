from typing import List, Tuple
from functools import lru_cache

from classes import Atom, Not, And, Or, Implies, Sequent, ProofNode


def is_axiom(seq: Sequent) -> bool:
    if any(f in set(seq.left) for f in seq.right):
        return True
    left_set = set(seq.left)
    for f in left_set:
        if isinstance(f, Not) and f.arg in left_set:
            return True
    return False


def find_applications(seq: Sequent) -> List[Tuple[str, List[Sequent]]]:
    apps = []
    left = list(seq.left)
    right = list(seq.right)

    for i, f in enumerate(left):
        match f:
            case And(a, b):
                new_left = tuple(left[:i] + left[i + 1 :] + [a, b])
                apps.append(("&L", [Sequent(new_left, seq.right)]))

            case Or(a, b):
                base = tuple(left[:i] + left[i + 1 :])
                p1 = Sequent(base + (a,), seq.right)
                p2 = Sequent(base + (b,), seq.right)
                apps.append(("|L", [p1, p2]))

            case Implies(a, b):
                base = tuple(left[:i] + left[i + 1 :])
                p1 = Sequent(base, seq.right + (a,))
                p2 = Sequent(base + (b,), seq.right)
                apps.append(("->L", [p1, p2]))

            case Not(a):
                new_left = tuple(left[:i] + left[i + 1 :])
                new_right = tuple(seq.right + (a,))
                apps.append(("~L", [Sequent(new_left, new_right)]))

            case Atom(_):
                pass

    for i, f in enumerate(right):
        match f:
            case And(a, b):
                base = tuple(right[:i] + right[i + 1 :])
                p1 = Sequent(seq.left, base + (a,))
                p2 = Sequent(seq.left, base + (b,))
                apps.append(("&R", [p1, p2]))

            case Or(a, b):
                new_right = tuple(right[:i] + right[i + 1 :] + [a, b])
                apps.append(("|R", [Sequent(seq.left, new_right)]))

            case Implies(a, b):
                base = tuple(right[:i] + right[i + 1 :])
                apps.append(("->R", [Sequent(seq.left + (a,), base + (b,))]))

            case Not(a):
                new_right = tuple(right[:i] + right[i + 1 :])
                apps.append(("~R", [Sequent(seq.left + (a,), new_right)]))

            case Atom(_):
                pass

    return apps


@lru_cache(maxsize=None)
def prove(seq: Sequent) -> ProofNode | None:
    if is_axiom(seq):
        return ProofNode(seq, "axiom", [])

    apps = find_applications(seq)
    apps.sort(key=lambda x: len(x[1]))

    for rule, premises in apps:
        children = []
        ok = True
        for prem in premises:
            child = prove(prem)
            if child is None:
                ok = False
                break
            children.append(child)
        if ok:
            return ProofNode(seq, rule, children)
    return None
