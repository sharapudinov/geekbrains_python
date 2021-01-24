class Matrix:
    """Класс описывающий линейное пространство матриц"""

    def __init__(self, matrix=None, *args, dim_r=0, dim_c=0):
        if matrix:
            self._body = matrix;
        else:
            self._body = [[0 for i in range(dim_r)] for j in range(dim_c)]

    def transposed(self):
        return Matrix([list(i) for i in zip(*self._body)])

    def zero(self):
        return Matrix(dim_r=self.dim_r(), dim_c=self.dim_c())
        pass

    def __str__(self):
        return '\n'+'\n'.join(list(map(lambda row: str(row).strip('[]'), self._body)))

    def dim_r(self):
        """возвращаем размерность строки(число столбцов)"""
        return max([len(row) for row in self._body])

    def dim_c(self):
        """возвращаем размерность столбца(число строк)"""
        return len(self._body)

    def __getitem__(self, row_number=None):
        if row_number == None:
            return self.transposed()
        elif row_number < self.dim_c():
            return self._body[row_number]
        else:
            raise IndexError

    def __setitem__(self, row_number: int, row: list):
        self._body[row_number] = row

    def __add__(self, other):
        result = self.zero()
        for i in range(self.dim_c()):
            for j in range(self.dim_r()):
                result[i][j] = self[i][j] + other[i][j]
        return result

    def __sub__(self, other):
        result = self.zero()
        for i in range(self.dim_c()):
            for j in range(self.dim_r()):
                result[i][j] = self[i][j] - other[i][j]
        return result

    def __iadd__(self, other):
        for i in range(self.dim_c()):
            for j in range(self.dim_r()):
                self[i][j] += other[i][j]
        return self

    def __isub__(self, other):
        for i in range(self.dim_c()):
            for j in range(self.dim_r()):
                self[i][j] -= other[i][j]
        return self

    def __mul__(self, other):
        if (self.dim_r() != other.dim_c()):
            raise ArithmeticError
        result = self.zero()
        for i in range(self.dim_c()):
            for j in range(self.dim_r()):
                result[i][j] += sum([a * b for a, b in zip(self[i], self[None][j])])
        return result


matrix1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix2 = matrix1 + matrix1
matrix3 = matrix2.transposed()
print('\nсумма матриц:',matrix1 + matrix2)
print('\nпроизведение матриц:',matrix1 * matrix3)
