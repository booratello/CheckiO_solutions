"""
Your mission is to convert the name of a function (a string) from CamelCase ("MyFunctionName") into
the Python format ("my_function_name") where all chars are in lowercase and all words are concatenated with an
intervening underscore symbol "_".

Input: A function name as a CamelCase string.

Output: The same string, but in under_score.
"""


def from_camel_case(name):
    name = list(name)
    for num, char in enumerate(name):
        if char.isupper():
            name.insert(num, "_")
            name[num + 1] = char.lower()
    name = "".join(name[1:])
    return name


if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("Name"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
