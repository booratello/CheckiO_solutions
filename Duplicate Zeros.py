"""
You are given a list of integers. Your task in this mission is to double all the zeros in the given list

Input: List.
Output: List.
"""


def duplicate_zeros(donuts: list) -> list:
    return list(map(int, ' '.join([str(el) if el != 0 else '0 0' for el in donuts]).split()))


print("Example:")
print(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]))

assert duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]) == [1, 0, 0, 2, 3, 0, 0, 4, 5, 0, 0]
assert duplicate_zeros([0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0]
assert duplicate_zeros([100, 10, 0, 101, 1000]) == [100, 10, 0, 0, 101, 1000]

print("The mission is done! Click 'Check Solution' to earn rewards!")
