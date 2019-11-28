"""
You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.
A pawn is safe if another pawn can capture a unit on that square. We have several white pawns on the chess board and
only white pawns. You should design your code to find how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.

Output: The number of safe pawns as a integer.
"""

def safe_pawns(pawns: set) -> int:

    def some_guard(offset: -1 or 1) -> str:
        all_columns = "abcdefgh"
        return "".join([all_columns[all_columns.index(el_c) + offset], str(int(el_r) - 1)])

    under_guard = 0

    for el in pawns:
        el_c, el_r = list(el)
        if int(el_r) == 1:  # If pawn in first row it in safety but it don't have guards.
            continue
        elif el_c == "a":  # If pawn in "a" column it have one right guard.
            guards = [some_guard(1)]
        elif el_c == "h":  # If pawn in "h" column it have one left guard.
            guards = [some_guard(-1)]
        else:
            guards = [some_guard(-1), some_guard(1)]
        if any(el in pawns for el in guards):
            under_guard += 1

    return under_guard


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
