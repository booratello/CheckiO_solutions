"""
You are given a dictionary where the keys are strings and the values are strings or dictionaries. The goal is flatten
the dictionary, but save the structures in the keys. The result should be the a dictionary without the nested
dictionaries. The keys should contain paths that contain the parent keys from the original dictionary. The keys in the
path are separated by a "/". If a value is an empty dictionary, then it should be replaced by an empty string ("").

Input: An original dictionary as a dict.

Output: The flattened dictionary as a dict.
"""


def flatten(dictionary):
    buffer_dict = {}
    for key, value in dictionary.items():
        if type(value) == dict:
            if value == {}:
                buffer_dict.update({key: ""})
            else:
                for sub_key, sub_value in value.items():
                    buffer_dict.update({"/".join([key, sub_key]): sub_value})
        else:
            buffer_dict.update({key: value})
    dictionary.clear()
    dictionary.update(buffer_dict)
    if any(type(value) == dict for value in dictionary.values()):
        flatten(dictionary)
    return dictionary


if __name__ == '__main__':
    test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    print(' Input: {}'.format(test_input))
    print('Output: {}'.format(flatten(test_input)))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
        "first": "One",
        "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {
            "place": {
                "zone": "1",
                "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    print('You all set. Click "Check" now!')
