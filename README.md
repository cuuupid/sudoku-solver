# Sudoku Solver

## Curiosity

**Curiosity** is the first rendition of the solver and relies on bruteforce :( sorry folks!

Curiosity's backend uses intersected sets ("destructive" solving) from the `helper.py` library.

Curiosity attempts to fill in each box sequentially following a clear set of rules:
- if there is only one possible choice, fill that in
- if there is no possible choice, kill the current branch
- if there is more than one choice, branch off

Curiosity is, of course, very inefficient in this way and so is slow (just under 0.3s per solve).

## Zealous

**Zealous** is a faithful zealot! Zealous has faith that the board will be solved immediately, and so tries to solve it without checking choices. If Zealous can't solve it still, he will allow there to be greater and greater levels of uncertainty (# of choices allowed to pick from).

e.g. if Zealous is allowing 2 guesses and a cell has 3 choices it will be skipped. If the cell has 2 choices, each choice will be evaluated from scratch (pick the choice, then branch off with a 1 choice tolerance).

Zealous is much faster than Curiosity due to this and can solve most scenarios before the complexity reaches 4 cases, in an extremely fast manner (just under 0.05s per solve).

## Ignoramus

**Ignoramus** is Zealous's student who copies the same technique, with a small modification. Ignoramus will tolerate cells with more choices than allowed, but will randomly pick <# of choices> choices to assess, ignoring the rest.

This means Ignoramus has unpredictable behavior. Sometimes Ignoramus will fail and have to try again. Ignoramus could be much faster or much slower than Zealous depending on the situation. As the nature of Sudoku does not favor randomness, it turns out Ignoramus is on average slightly slower (~0.55s per solve).

## Benchmarks

Model     | Solve Time (Average) (seconds)
--------- | ------------------------------
Curiosity | 0.28358543157577515
Zealous   | 0.045852898359298705
Ignoramus | 0.05323422074317932