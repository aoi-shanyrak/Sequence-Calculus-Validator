from src.classes import ProofNode

from src.symbols import BRANCH, LAST_BRANCH, EMPTY_SET, PROVE_SYMBOL


def proof_to_str(node: ProofNode | None, indent: str = "", is_last: bool = True) -> str:
    if node is None:
        return "WRONG!!!\n"

    result = ""

    seq = node.sequent
    left = ", ".join(str(f) for f in seq.left) if seq.left else EMPTY_SET
    right = ", ".join(str(f) for f in seq.right) if seq.right else EMPTY_SET

    branch = LAST_BRANCH if is_last else BRANCH
    result += indent + branch + left + PROVE_SYMBOL + right + f"    [{node.rule}] \n"

    new_indent = indent + ("    " if is_last else "|   ")
    for i, prem in enumerate(node.premises):
        is_last_prem = i == len(node.premises) - 1
        result += proof_to_str(prem, new_indent, is_last_prem)

    return result
