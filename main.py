"""class MyClass:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def make_action(self):
        print(self.first, self.second)
        print("What do Pink Floyd and Princess Diana have in common? Their greatest hit was the wall.")


def main():
    cockroach1 = MyClass('DanDan', 'Dan')
    cockroach1.make_action()


main()"""

####### HOME TASK N1 #######


"""lst = [[5, 2, 6, 1],
       [4, 7, 3, 8],
       [5, 9, 0, 4],
       [3, 1, 0, -3],
       [9, 0, 2, 2]]


# 1 Дана целочисленная прямоугольная матрица. Определить
def first(lst):
    print("Вариант 1 \n Дана целочисленная прямоугольная матрица. Определить")
    # 1) количество строк, не содержащих ни одного нулевого элемента
    j = 0
    for i in lst:
        if 0 not in i:
            j += 1
    print("1) количество строк, не содержащих ни одного нулевого элемента: ", j)

    # 2) максимальное из чисел, встречающихся в заданной матрице более одного раза
    a = 0
    for i in lst:
        for j in i:
            a += i.count(j)
    if a > 1:
        print("2) максимальное из чисел, встречающихся в заданной матрице более одного раза:",
              max([j for i in lst for j in i]))


first(lst)


# 3 Дана целочисленная прямоугольная матрица. Определить
def third(lst):
    print("Вариант 3 \n Дана целочисленная прямоугольная матрица. Определить")
    # 1) количество столбцов, содержащих хотя бы один нулевой элемент;
    lst_t = list(zip(*lst))
    j = 0
    for i in lst_t:
        if 0 in i:
            j += 1
    print("1) количество столбцов, содержащих хотя бы один нулевой элемент:", j)

    # 2) номер строки, в которой находится самая длинная серия одинаковых элементов
    max_count = 0
    max_row = 0
    row_num = 0
    for row in lst:
        count = 1
        for i in range(1, len(row)):
            if row[i] == row[i - 1]:
                count += 1
            else:
                count = 1
            if count > max_count:
                max_count = count
                max_row = row_num
        row_num += 1
    print("2) номер строки, в которой находится самая длинная серия одинаковых элементов: ", max_row)


third(lst)


# 18 Дана целочисленная прямоугольная матрица. Определить
def eighteenth(lst):
    print("Вариант 18 \n Дана целочисленная прямоугольная матрица. Определить")
    # 1) количество строк, содержащих хотя бы один нулевой элемент;
    j = 0
    for i in lst:
        if 0 in i:
            j += 1
    print("1) количество строк, содержащих хотя бы один нулевой элемент:", j)

    # 2) номер столбца, в которой находится самая длинная серия одинаковых элементов
    lst_t = list(zip(*lst))
    max_count = 0
    max_row = 0
    row_num = 0
    for row in lst_t:
        count = 1
        for i in range(1, len(row)):
            if row[i] == row[i - 1]:
                count += 1
            else:
                count = 1
            if count > max_count:
                max_count = count
                max_row = row_num
        row_num += 1
    print("2) номер столбца, в которой находится самая длинная серия одинаковых элементов: ", max_row)


eighteenth(lst)"""
