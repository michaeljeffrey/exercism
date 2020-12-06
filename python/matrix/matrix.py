class Matrix(object):
    def __init__(self, matrix_string):
        string_rows = matrix_string.split("\n")
        self.int_matrix = [[int(r) for r in row.split(" ")] for row in string_rows]

    def row(self, index):
        return self.int_matrix[index-1]

    def column(self, index):
        return [c[index-1] for c in self.int_matrix]