import re

"""
You have a set of "words", all in lower case, and each word contains symbols in "alphabetical order" (it's not your
typical alphabetical order, but a new and different order). We need to determine the order of the symbols from each
"word" and create a single "word" with all of these symbols, placing them in the new alphabetial order. In some cases,
if we cannot determine the order for several symbols, you should use the traditional latin alphabetical order.
For example: Given words "acb", "bd", "zwa". As we can see "z" and "w" must be before "a" and "d" after "b".
So the result is "zwacbd".

Input: Words as a list of strings.

Output: The order as a string.
"""


def checkio(data):
    data = list(set(data))  # removed possible duplicates words

    for i in range(len(data)):  # removed possible consecutive duplicates of letters
        buffer = [None]
        for letter in data[i]:
            if letter != buffer[-1]:
                buffer.append(letter)
        data.pop(i)
        data.insert(i, "".join(buffer[1:]))

    buffer = list({word[0] for word in data})  # search for the first letter or first letters in alphabetical order
    abc_letters = []
    for letter in buffer:
        if all(word.count(letter) == 0 or word.count(letter) == 1 and word.find(letter) == 0 for word in data):
            abc_letters.append(letter)
    abc_letters = sorted(abc_letters)

    def defining_new_abc(new_abc_letters: str) -> str:
        """
        For the last letter of the new alphabet, all its combinations with the next letter in all available words are
        searched. For all the resulting "next letters" are searched for combinations with their preceding letters. If
        there are combinations with "preceding letters" that are not in the new alphabet, then this "next letter" is not
        suitable. Otherwise ,the "next letter" is added to the new alphabet. If there are several such "next letters",
        they are added to the new alphabet in the standard alphabetical order.
        """
        new_abc_letters = list(new_abc_letters)
        for pos, el in enumerate(new_abc_letters):
            if pos != len(new_abc_letters) - 1:
                continue
            buffer.clear()
            possible_comb = list(set(sum([re.findall(r"{}.".format(el), word) for word in data], [])))
            for counter, comb in enumerate(possible_comb):
                possible_letters = list(set(sum([re.findall(r"[^{}]{}".format("".join(new_abc_letters), comb[1]), word)
                                                 for word in data], [])))
                if len(possible_letters) == 0:
                    buffer.append(comb[1])
                    if counter != len(possible_comb) - 1:
                        continue
                new_abc_letters.extend(sorted(buffer))
        return "".join(new_abc_letters)

    result_word = ""
    for letter in abc_letters:  # this is necessary if the result of abc_letters is more than one letter
        result_word = defining_new_abc(result_word + letter)

    return result_word


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
        "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
        "Paste in"
    assert checkio(["a", "b", "c"]) == "abc", \
        "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs", \
        "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
        "Concatenate and paste in"
