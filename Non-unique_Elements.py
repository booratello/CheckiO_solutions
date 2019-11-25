"""
You are given a non-empty list of integers (X). For this task, you should return a list consisting of only
the non-unique elements in this list. To do so you will need to remove all unique elements (elements which are contained
in a given list only once). When solving this task, do not change the order of the list. Example: [1, 2, 3, 1, 3] 1 and
3 non-unique elements and result will be [1, 3, 1, 3].

Input: A list of integers.

Output: An iterable of integers.
"""


def checkio(data: list) -> list:
    not_unique_data = []
    for el in data:
        if data.count(el) > 1:
            not_unique_data.append(el)
    return not_unique_data


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
