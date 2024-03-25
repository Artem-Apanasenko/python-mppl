####### HOME TASK N1 #######
mat = [[5, 6, 5, 1],
       [5, 9, 3, 1],
       [1, 8, 0, 1],
       [7, 0, 3, 3],
       [3, 1, 2, 0]]

mat_t = list(zip(*mat))


# 1 Дана целочисленная прямоугольная матрица. Определить
def first(mat):
    def v_one_first():
        print("Вариант 1 \n Дана целочисленная прямоугольная матрица. Определить")
        elem = 0
        for row in mat:
            if 0 not in row:
                elem += 1
        return elem

    def v_one_second():
        seen = []
        repeated = []
        for row in mat:
            for elem in row:
                if elem in seen and elem not in repeated:
                    repeated.append(elem)
                else:
                    seen.append(elem)
        if repeated:
            return max(repeated)
        else:
            return None

    result_v_one_first = v_one_first()
    result_v_one_second = v_one_second()
    return result_v_one_first, result_v_one_second


result_v_one_first, result_v_one_second = first(mat)
print("1) количество строк, не содержащих ни одного нулевого элемента ", result_v_one_first)
print("2) максимальное из чисел, встречающихся в заданной матрице более одного раза ", result_v_one_second)


# 3 Дана целочисленная прямоугольная матрица. Определить
def third(mat):
    print("Вариант 3 \n Дана целочисленная прямоугольная матрица. Определить")

    # 1) количество столбцов, содержащих хотя бы один нулевой элемент;
    def v_three_first():
        elem = 0
        for row in mat_t:
            if 0 in row:
                elem += 1
        return elem

    # 2) номер строки, в которой находится самая длинная серия одинаковых элементов
    def v_three_second():
        max_count = 0
        max_row = 0
        row_num = 0
        for row in mat:
            count = 1
            for elem in range(1, len(row)):
                if row[elem] == row[elem - 1]:
                    count += 1
                else:
                    count = 1
                if count > max_count:
                    max_count = count
                    max_row = row_num
            row_num += 1
        return max_row

    result_v_three_first = v_three_first()
    result_v_three_second = v_three_second()
    return result_v_three_first, result_v_three_second


result_v_three_first, result_v_three_second = third(mat)
print("1) количество столбцов, содержащих хотя бы один нулевой элемент: ", result_v_three_first)
print("2) номер строки, в которой находится самая длинная серия одинаковых элементов ", result_v_three_second)


# 18 Дана целочисленная прямоугольная матрица. Определить
def eighteenth(mat):
    print("Вариант 18 \n Дана целочисленная прямоугольная матрица. Определить")

    # 1) количество строк, содержащих хотя бы один нулевой элемент;
    def v_eighteen_first():
        elem = 0
        for row in mat:
            if 0 in row:
                elem += 1
        return elem

    # 2) номер столбца, в которой находится самая длинная серия одинаковых элементов
    def v_eighteen_second():
        max_count = 0
        max_col = 0
        col_num = 0
        for col in mat_t:
            count = 1
            for elem in range(1, len(col)):
                if col[elem] == col[elem - 1]:
                    count += 1
                else:
                    count = 1
                if count > max_count:
                    max_count = count
                    max_col = col_num
            col_num += 1
        return max_col

    result_v_eighteen_first = v_eighteen_first()
    result_v_eighteen_second = v_eighteen_second()
    return result_v_eighteen_first, result_v_eighteen_second


result_v_eighteen_first, result_v_eighteen_second = eighteenth(mat)
print("1) количество строк, содержащих хотя бы один нулевой элемент: ", result_v_eighteen_first)
print("2) номер столбца, в которой находится самая длинная серия одинаковых элементов ", result_v_eighteen_second)
