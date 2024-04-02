class MatrixAnalyzer:
    def __init__(self, matrix):
        self.matrix = matrix
        self.transposed_matrix = [list(row) for row in zip(*self.matrix)]

    def find_nonzero_rows(self):
        return sum(1 for row in self.matrix if 0 not in row)

    def find_max_num(self):
        flatten_matrix = [elem for row in self.matrix for elem in row]
        return max(elem for elem in set(flatten_matrix) if flatten_matrix.count(elem) > 1)

    def find_withzero_columns(self):
        return sum(1 for row in self.transposed_matrix if 0 in row)

    def find_longest_series(self):
        counts = [sum(1 for i in range(len(row) - 1) if row[i] == row[i + 1]) for row in self.matrix]
        return counts.index(max(counts))

    def summarize_positive_rows(self):
        return [sum(row) for row in self.transposed_matrix if all(elem >= 0 for elem in row)]

    def even_positive_sorting(self):
        even_sum = [sum(elem for elem in row if elem % 2 == 0) for row in self.matrix]
        equlize_value = {tuple(self.matrix[i]): even_sum[i] for i in range(len(self.matrix))}
        return sorted(equlize_value, key=equlize_value.get)

    def analyze(self):
        print(f"1) the number of rows containing no zero element: {self.find_nonzero_rows()}")
        print(f"2) the maximum number of numbers occurring more than once: {self.find_max_num()}")
        print(f"3) the number of columns containing at least one zero element: {self.find_withzero_columns()}")
        print(f"4) the number of the row containing the longest series of identical elements: {self.find_longest_series()}")
        print(f"5) the sum of elements in columns without negative elements: {self.summarize_positive_rows()}")
        print(f"6) Rows arranged by the sum of their positive even elements: {self.even_positive_sorting()}")


def main():
    mat = [
        [1, 6, 5, 0],
        [4, 7, 2, 4],
        [1, 1, 5, 1],
        [4, 0, 8, 0],
        [3, 1, 0, -5]
    ]
    analyzer = MatrixAnalyzer(mat)
    analyzer.analyze()


main()
