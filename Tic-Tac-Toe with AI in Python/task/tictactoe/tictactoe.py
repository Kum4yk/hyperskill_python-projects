class TicTacToe:
    def __init__(self, some_list):
        self.matrix = self.create_matrix(some_list)

    @staticmethod
    def create_matrix(some_list, col=3):
        matrix = [some_list[i:i+col] for i in range(0, len(some_list), col)]
        return matrix

    def print_matrix(self):
        print('---------')
        for line in self.matrix:
            print('|', *line, '|')
        print('---------')
        print()


if __name__ == "__main__":
    some_list = list(input("Enter cells: ")[1:-1])
    game = TicTacToe(some_list)
    game.print_matrix()
