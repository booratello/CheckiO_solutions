from typing import List

"""
You are given a result of a Tic-Tac-Toe game and you must determine if the game ends in a win or a draw as well as who
will be the winner.
Make sure to return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".
A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.

Input: A game result as a list of strings (unicode).

Output: "X", "O" or "D" as a string.
"""


def checkio(game_result: List[str]) -> str:
    game_result = list(enumerate(list("".join(game_result))))
    # for example, game_result is [(0, 'X'), (1, '.'), (2, 'O'), ect]
    x_set = set([x[0] for x in game_result if x[1] == "X"])
    o_set = set([o[0] for o in game_result if o[1] == "O"])
    combinations_list = [{0, 4, 8}, {2, 4, 6}, {0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}]
    for el in combinations_list:
        if len(el - x_set) == 0:
            return "X"
        elif len(el - o_set) == 0:
            return "O"
    return "D"


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
