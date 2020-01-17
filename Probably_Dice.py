"""
You're on your way to a board game convention. Chances are there’ll be some stiff competition, so you decide to learn
more about dice probabilities since you suspect you'll be rolling a lot of them soon.

Typically, when using multiple dice, you simply roll them and sum up all the result. To get started with your
investigation of dice probability, write a function that takes the number of dice, the number of sides per die and a
target number and returns the probability of getting a total roll of exactly the target value. The result should be
given with four digits precision as ±0.0001. For example, if you roll 2 six-sided dice, the probability of getting
exactly a 3 is 2/36 or 5.56%, which you should return as ≈0.0556.
For each test, assume all the dice are the same and are numbered from 1 to the number of sides, inclusive. So a 4-sided
die (D4) would have an equal chance of rolling a 1, 2, 3 or 4. A 20-sided die (D20) would have an equal chance of
rolling any number from 1 to 20.

Tips: Be careful if you want to use a brute-force solution -- you could have a very, very long wait for edge cases.
(my solve based on http://ulf.tordenson.ru/articles/dice_and_chance/)

Input: Three arguments. The number of dice, the number of sides per die and the target number as integers.

Output: The probability of getting exactly target number on a single roll of the given dice as a float.
"""


def probability(dice_number, sides, target):

    if not dice_number <= target <= dice_number * sides:
        return 0

    one_dice_prob = 1 / sides
    if dice_number == 1:
        return round(one_dice_prob, 4)

    matrix_num = [[i + j + 2 for j in range(sides)] for i in range(sides)]
    matrix_prob = [[1 / sides ** 2 for _ in range(sides)] for _ in range(sides)]
    dict_prob = {}
    for k in range(2, sides * 2 + 1):
        counter = 0
        for i in range(sides):
            for j in range(sides):
                if matrix_num[i][j] == k:
                    counter += matrix_prob[i][j]
        dict_prob[k] = counter
    if dice_number == 2:
        return round(dict_prob[target], 4)

    dice_counter = 3
    while dice_counter != dice_number + 1:
        matrix_num = [[i + j for j in range(1, sides + 1)] for i in range(dice_counter - 1, sides * (dice_counter - 1) + 1)]
        matrix_prob = [[dict_prob[i] * one_dice_prob for _ in range(sides)] for i in range(dice_counter - 1, sides * (dice_counter - 1) + 1)]
        dict_prob.clear()
        for k in range(dice_counter, sides * dice_counter + 1):
            counter = 0
            for i in range((sides - 1) * (dice_counter - 1) + 1):
                for j in range(sides):
                    if matrix_num[i][j] == k:
                        counter += matrix_prob[i][j]
            dict_prob[k] = counter
        dice_counter += 1
    return round(dict_prob[target], 4)


if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
