"""
There is a list which contains integers or other nested lists which may contain yet more lists and integers which then…
You should put all of the integer values into one flat list. The order should be as it was in the original list with
string representation from left to right.

Input data: A nested list with integers.

Output data: The one-dimensional list with integers.
"""


def flat_list(array):
    while any(type(el) == list for el in array):
        buffer_list = []
        for el in array:
            buffer_list.extend(el) if type(el) == list else buffer_list.append(el)
        array = buffer_list
    return array


if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
