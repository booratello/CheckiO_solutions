from random import randint

"""
Дан массив MxM заполненный случайным образом числами от 0 до 9.
Сформировать новый массив MxM по следующему правилу:
1) Если в строке встречаются одинаковые числа, то они заменяются на 
результат произведения этого числа на количество повторений.
2) Если в столбце встречаются одинаковые числа, то они заменяются на 
результат произведения этого числа на количество повторений.
3) Если число встречается и в строке, и в столбце, то оно заменяется 
на сумму произведения этого числа на количество повторений в строке 
и произведения этого числа на количество повторений в столбце.
4) Если число встречает в строке и столбце один раз,
то оно переносится без изменений.

Пример:
|0|2|3|9|7|             |0 |4|3|9|7 |
|6|2|4|5|8|             |12|4|8|5|16|
|8|9|1|2|8|     ->      |16|9|1|4|32|
|6|5|4|3|0|             |12|5|8|3|0 |
|9|7|6|2|1|             |9 |7|6|2|1 |
"""


def is_it_right_int(some_var, ctrl=0):
    """
    Функция для проверки корректности вводимых чисел.
    :param ctrl: 0, 1 или 2 - нужен для переключения между проверками:
                    - 0 (по умолчанию) для вводимых в матрицу чисел
                    - 1 для порядка матрицы
                    - 2 для метода заполнения матрицы
    :param some_var: str
    :return: int
    """

    if ctrl == 1:
        while True:
            try:
                some_var = int(some_var)
                if some_var < 2:
                    raise ValueError
                return some_var
            except ValueError:
                some_var = input("Нужно целое число больше 1. "
                                 "Введите заново.\n")
    elif ctrl == 2:
        while True:
            try:
                some_var = int(some_var)
                if some_var not in [1, 2]:
                    raise ValueError
                return some_var
            except ValueError:
                some_var = input("Нужно вести 1 или 2. Введите заново.\n")
    else:
        while True:
            try:
                some_var = int(some_var)
                if not 0 <= some_var <= 9:
                    raise ValueError
                return some_var
            except ValueError:
                some_var = input("Нужно целое число от 0 до 9 включительно. "
                                 "Введите заново.\n")


m = is_it_right_int(input("Укажите порядок M квадратной матрицы.\n"), ctrl=1)

if is_it_right_int(input("Введите [1] для автоматического или [2] "
                         "для ручного заполенения матрицы.\n"), ctrl=2) == 1:
    """
    Списки (одномерные массивы) можно создавать с помощью конструкции типа
    [f(x) for x in <некая последовательность>] - т.н. "генератор списка"
    (list comprehensions). Т.к. в примере ниже randint(0, 9) не зависит от
    переменной после for, используется т.н. "буферная переменная" _.
    """
    matrix = [[randint(0, 9) for _ in range(m)] for _ in range(m)]
else:
    matrix = [
        [is_it_right_int(input(f"Строка {i + 1}, столбец {j + 1}. "
                               f"Введите число.\n")) for j in range(m)]
        for i in range(m)]

print("Получена следующая матрица:")

for el in matrix:
    print(el)

print("\nМатрица после выполения условий задания:")

# Заполненая нулями матрица тех же размеров, что и исходная, в ней будет
# производиться замена элементов.
new_matrix = [[0 for _ in range(m)] for _ in range(m)]

"""
- matrix[i][j] вернёт число из исходной матрицы
- matrix[i] вернёт в виде списка содержимое строки исходной матрицы, в которой
  находится искомое число
- [matrix[k][j] for k in range(m)] вернёт в виде списка содержимое столбца
  исходной матрицы, в котором находится искомое число
- метод count() вернёт число, равное количеству вхождений искомого
  числа в список, к которому применяется данный метод
"""

for i in range(m):
    for j in range(m):
        
        row_count = matrix[i].count(matrix[i][j])
        column_count = [matrix[k][j] for k in range(m)].count(matrix[i][j])

        if row_count == 1 or column_count == 1:
            if row_count == column_count:
                new_matrix[i][j] = matrix[i][j]
            else:
                new_matrix[i][j] = matrix[i][j] * max(row_count, column_count)
        else:
            new_matrix[i][j] = matrix[i][j] * (row_count + column_count)

for el in new_matrix:
    print(el)
