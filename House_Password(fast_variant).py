"""
You should develop a password security check module. The password will be
considered strong enough if its length is greater than or equal to 10 symbols,
it has at least one digit, as well as containing one uppercase letter and one
lowercase letter in it. The password contains only ASCII latin letters or
digits.

Input: A password as a string.

Output: Is the password safe or not as a boolean or any data type that can be
converted and processed as a boolean. In the results you will see the converted
results.
"""


def checkio(data) -> bool:
    return not (len(data) < 10 or data.isdigit() or data.isalpha() or
                data.islower() or data.isupper())


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary
    # for auto-testing
    assert checkio('A1213pokl') is False
    assert checkio('bAse730onE4') is True
    assert checkio('asasasasasasasaas') is False
    assert checkio('QWERTYqwerty') is False
    assert checkio('123456123456') is False
    assert checkio('QwErTy911poqqqq') is True
    print("Coding complete? Click 'Check' to review your tests and earn "
          "cool rewards!")
