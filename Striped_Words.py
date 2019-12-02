"""
You are given a block of text with different words. These words are separated by white-spaces and punctuation marks.
Numbers are not considered words in this mission (a mix of letters and digits is not a word either). You should count
the number of words (striped words) where the vowels with consonants are alternating, that is; words that you count
cannot have two consecutive vowels or consonants. The words consisting of a single letter are not striped - do not count
those. Casing is not significant for this mission.

Input: A text as a string (unicode)

Output: A quantity of striped words as an integer.
"""
# OMG, what have I done? It should be a lot easier...


def checkio(text):
    edited_text = ""
    for symbol in text:
        edited_text += symbol.lower() if symbol.isalnum() else " "
    edited_text = edited_text.strip().split(" ")
    counter = 0
    for word in edited_text:
        consonant_vowel = all("aeiouy".find(el) != -1 for id_, el in enumerate(word) if id_ % 2 == 0) and \
                          all("aeiouy".find(el) == -1 for id_, el in enumerate(word) if id_ % 2 != 0)
        vowel_consonant = all("aeiouy".find(el) == -1 for id_, el in enumerate(word) if id_ % 2 == 0) and \
                          all("aeiouy".find(el) != -1 for id_, el in enumerate(word) if id_ % 2 != 0)
        if word.isalpha() and len(word) > 1 and (consonant_vowel or vowel_consonant):
            counter += 1
    return counter


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
