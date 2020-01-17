"""
Help the robot to speak properly and increase his number processing speed by
writing a new speech module for him. All the words in the string must be
separated by exactly one space character. Be careful with spaces -- it's hard
to see if you place two spaces instead one.

Input: A number as an integer.

Output: The string representation of the number as a string.

Precondition: 0 < number < 1000
"""


def checkio(number):
    std_num_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
                    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
                    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen"}
    # I wanted to limit the dictionary to 12, but then an error appears in
    # the number 40 as "fourty".

    composite_num_dict = {2: "twen", 3: "thir", 4: "for", 5: "fif",
                          6: "six", 7: "seven", 8: "eigh", 9: "nine"}

    hundreds = std_num_dict[number // 100] + " hundred " \
        if number // 100 > 0 else ""

    decades = number % 100 if number % 100 != 0 else ""

    if type(decades) is int:
        if decades <= 14:
            decades = std_num_dict[decades]
        elif 15 <= decades <= 19:
            decades = composite_num_dict[decades % 10] + "teen"
        else:
            first_nine = std_num_dict[decades % 10] \
                if decades % 10 != 0 else ""
            decades = composite_num_dict[decades // 10] + "ty " \
                if decades // 10 != 0 else ""
            decades = decades + first_nine

    return (hundreds + decades).rstrip()


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary
    # for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), \
        "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
