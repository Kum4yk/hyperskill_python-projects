import numbers


class Matrix:
    matrices_number = 0
    num_map = {0: "", 1: "first ", 2: "second "}

    def __init__(self, matrix):
        self.__rows = len(matrix)
        self.__columns = len(matrix[0])
        self.matrix = matrix
        self.dimension = (self.__rows, self.__columns)
        Matrix.matrices_number += 1

    def __str__(self):
        return '\n'.join(' '.join(str(elem) for elem in line) for line in self.matrix)

    def __check_dimension(self, other, mode=True):
        if mode:
            return self.dimension == other.dimension
        return self.__columns == other.__rows

    def mul_by_num(self, num):
        result = [[elem * num for elem in line] for line in self.matrix]
        return Matrix(result)

    def mul_by_matrix(self, other):
        result = [
            [sum(self.matrix[r_1][i] * other.matrix[i][c_2] for i in range(self.__columns))
             for c_2 in range(other.__columns)]
            for r_1 in range(self.__rows)
        ]
        return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return self.mul_by_num(other)
        elif isinstance(other, Matrix) and self.__check_dimension(other, False):
            return self.mul_by_matrix(other)
        return 'The operation cannot be performed.'

    def __add_num(self, other):
        result = [[self.matrix[i][j] + other for j in range(self.__columns)]
                  for i in range(self.__rows)]
        return Matrix(result)

    def __add_matrix(self, other):
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.__columns)]
                  for i in range(self.__rows)]
        return Matrix(result)

    def __add__(self, other):
        if isinstance(other, Matrix) and self.__check_dimension(other):
            return self.__add_matrix(other)
        elif isinstance(other, numbers.Number):
            return self.__add_num(other)
        return 'The operation cannot be performed.'

    def transpose(self):
        res = [[self.matrix[i][j] for i in range(self.__rows)] for j in range(self.__columns)]
        return Matrix(res)

    def transpose_by_side(self):
        res = [
            [self.matrix[self.__rows - 1 - j][self.__columns - 1 - i] for j in range(self.__rows)]
            for i in range(self.__columns)
        ]
        return Matrix(res)

    def transpose_by_vertical(self):
        res = [
            [self.matrix[i][self.__columns - 1 - j] for j in range(self.__columns)]
            for i in range(self.__rows)
        ]
        return Matrix(res)

    def transpose_by_horizontal(self):
        res = [
            [self.matrix[self.__rows - 1 - i][j] for j in range(self.__columns)]
            for i in range(self.__rows)
        ]
        return Matrix(res)

    def det(self):
        return Matrix.calc_det(self.matrix)

    @staticmethod
    def calc_det(matrix: list):
        rows, cols = len(matrix), len(matrix[0])
        if rows == 1:
            return matrix[0][0]
        if rows != cols:
            return 'The operation cannot be performed.'

        answer = 0
        for i in range(cols):
            minor = [line[0: i] + line[i+1:] for line in matrix[1:]]
            const = -1 if i % 2 == 1 else 1
            answer += Matrix.calc_det(minor) * const * matrix[0][i]
        return answer

    def inverse(self):
        if self.dimension[0] != self.dimension[1]:
            return 'The operation cannot be performed.'
        det = self.det()
        if det == 0:
            return "This matrix doesn't have an inverse."
        result = [[0 for _ in range(self.__columns)] for _ in range(self.__rows)]
        for row in range(self.__rows):
            for col in range(self.__columns):
                minor = [
                    [self.matrix[i][j] for j in range(self.__columns) if j != col]
                    for i in range(self.__rows) if i != row
                ]
                sign = 1 if (row + col) % 2 == 0 else -1
                result[row][col] = sign * Matrix.calc_det(minor)
        return Matrix(result).transpose() * (1 / det)


class Processor:
    commands = {"0", "1", "2", "3", "4", "5", "6"}

    @staticmethod
    def print_result(value):
        print("The result is:")
        print(value)

    @staticmethod
    def create_1_matrix():
        Matrix.matrices_number = 0
        matrix = Matrix(Processor.input_matrix())
        return matrix

    @staticmethod
    def create_2_matrix():
        Matrix.matrices_number = 1
        matrix_1 = Matrix(Processor.input_matrix())
        matrix_2 = Matrix(Processor.input_matrix())
        return matrix_1, matrix_2

    @staticmethod
    def input_matrix():
        row, _ = map(
            int,
            input(f"Enter size of {Matrix.num_map[Matrix.matrices_number]}matrix: ").split()
        )
        print(f"Enter {Matrix.num_map[Matrix.matrices_number]}matrix:")
        matrix = [input().split() for _ in range(row)]
        return Processor.convert_by_type(matrix)

    @staticmethod
    def convert_by_type(obj, is_matrix=True):
        if is_matrix:
            func = float if \
                any((elem.__contains__(".") for line in obj for elem in line)) \
                else int
            return [[func(elem) for elem in line] for line in obj]
        return float(obj) if obj.__contains__(".") else int(obj)

    @staticmethod
    def add_matrices():
        matrix_1, matrix_2 = Processor.create_2_matrix()
        Processor.print_result(matrix_1 + matrix_2)

    @staticmethod
    def mul_by_constant():
        matrix = Processor.create_1_matrix()
        const = Processor.convert_by_type(input("Enter constant: "), False)
        Processor.print_result(matrix * const)

    @staticmethod
    def mul_matrices():
        matrix_1, matrix_2 = Processor.create_2_matrix()
        Processor.print_result(matrix_1 * matrix_2)

    @staticmethod
    def calculate_determinant():
        matrix = Processor.create_1_matrix()
        Processor.print_result(matrix.det())

    @staticmethod
    def inverse_matrix():
        matrix = Processor.create_1_matrix()
        Processor.print_result(matrix.inverse())

    @staticmethod
    def transpose():
        transpose_modes = {"1", "2", "3", "4"}

        mode = ""
        while mode not in transpose_modes:
            mode = input("Your choice: ")

        matrix = Processor.create_1_matrix()
        if mode == "1":
            print(matrix.transpose())
        elif mode == "2":
            print(matrix.transpose_by_side())
        elif mode == "3":
            print(matrix.transpose_by_vertical())
        elif mode == "4":
            print(matrix.transpose_by_horizontal())
        else:
            print("Impossible state")

    @staticmethod
    def gain_command():
        command = ""
        while command not in Processor.commands:
            command = input("Your choice: ")
        return command

    @staticmethod
    def main():
        while True:
            message = [
                "1. Add matrices", "2. Multiply matrix by a constant",
                "3. Multiply matrices", "4. Transpose matrix",
                "5. Calculate a determinant", "6. Inverse matrix", "0. Exit"
            ]
            print(*message, sep="\n")

            command = Processor.gain_command()
            if command == "0":
                break
            elif command == "1":
                Processor.add_matrices()
            elif command == "2":
                Processor.mul_by_constant()
            elif command == "3":
                Processor.mul_matrices()
            elif command == "4":
                Processor.transpose()
            elif command == "5":
                Processor.calculate_determinant()
            elif command == "6":
                Processor.inverse_matrix()
            else:
                print("Impossible state")
            print()


if __name__ == '__main__':
    Processor.main()
