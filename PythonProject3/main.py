class Matrix:
    def __init__(self, rows, cols, fill_value=0):
        self.rows = rows
        self.cols = cols
        self.data = [[fill_value for _ in range(cols)] for _ in range(rows)]

    def __getitem__(self, indices):
        row, col = indices
        if row >= self.rows or col >= self.cols:
            raise IndexError("Index out of range")
        return self.data[row][col]

    def __setitem__(self, indices, value):
        row, col = indices
        if row >= self.rows or col >= self.cols:
            raise IndexError("Index out of range")
        self.data[row][col] = value

    def __iter__(self):
        """Итерируемся по строкам матрицы"""
        return iter(self.data)

    def __str__(self):
        return '\n'.join(str(row) for row in self.data)


# Пример использования
matrix = Matrix(3, 3)
print(matrix)