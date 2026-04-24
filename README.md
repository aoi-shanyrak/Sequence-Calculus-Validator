# Sequence-Calculus-Validator

proves the sequence calculus by making a prove tree till it will goal the axiom

---

write sequent in ASCII
```
A & (B | C) |- (A & B) | (A & C)
```

```
└── (A & (B V C)) ⊢ ((A & B) V (A & C))    [&L] 
    └── A, (B V C) ⊢ ((A & B) V (A & C))    [|R] 
        └── A, (B V C) ⊢ (A & B), (A & C)    [|L] 
            ├── A, B ⊢ (A & B), (A & C)    [&R] 
            |   ├── A, B ⊢ (A & C), A    [axiom] 
            |   └── A, B ⊢ (A & C), B    [axiom] 
            └── A, C ⊢ (A & B), (A & C)    [&R] 
                ├── A, C ⊢ (A & C), A    [axiom] 
                └── A, C ⊢ (A & C), B    [&R] 
                    ├── A, C ⊢ B, A    [axiom] 
                    └── A, C ⊢ B, C    [axiom] 
```

## if it's wrong sequence:

```
A -> (B -> C) |- (A -> B) -> C
```

```
WRONG!!!
```

## Complexity

O(2^N) cause at every step there is a chance that tree will divide into two 
