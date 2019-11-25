from itertools import dropwhile

"""
Here you should find the length of the longest substring that consists of the same letter. For example, line
"aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa".
The last substring is the longest one, which makes it the answer.

Input: String.

Output: Int.
"""


def long_repeat(line: str, max_chain=0) -> int:
    remainder = "".join(list(dropwhile(lambda chain: chain == line[0], line)))
    max_chain = max(len(line) - len(remainder), max_chain)
    return long_repeat(remainder, max_chain) if len(remainder) > 0 else max_chain


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
