class TicTacToe:
    wining_pos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
    
    def __init__(self):
        self.lst = " " * 9
        self.matrix = [list(" " * 3) for i in range(3)]

    def print_matrix(self):
        print('---------')
        for line in self.matrix:
            print('|', *line, '|')
        print('---------')

    def check_state(self):
        if abs(self.lst.count("X") - self.lst.count("O")) > 1:
            print("Impossible")
            return False
        
        x_win = False
        o_win = False
        for i, j, k in TicTacToe.wining_pos:
            if self.lst[i] == self.lst[j] == self.lst[k]:
                x_win = True if self.lst[i] == "X" else x_win
                o_win = True if self.lst[i] == "O" else o_win
        
        if x_win and o_win:
            print("Impossible")
            return False
        
        if not x_win and not o_win:
            if self.lst.count(" "):
                #  "Game not finished"
                return True
            print("Draw")
            return False
        
        print("X wins" if x_win else "O wins")
        return False

    def put_symbol(self, x_time=False):
        symbol = "X" if x_time else "O"
        
        while True:
            in_ = input("Enter the coordinates: ").split()
            if not in_[0].isdigit():
                print("You should enter numbers!")
                continue

            col, row = map(int, in_)
            print(col, row)
            if row not in {1, 2, 3} or col not in {1, 2, 3}:
                print("Coordinates should be from 1 to 3!")
                continue

            row, col = abs(row - 3), col - 1
            if self.matrix[row][col] != " ":
                print("This cell is occupied! Choose another one!")
                continue
            
            self.matrix[row][col] = symbol
            i = row * 3 + col
            self.lst = self.lst[:i] + symbol + self.lst[i+1:]
            
            break
        return not x_time

    @staticmethod
    def run_game():
        game = TicTacToe()
        game.print_matrix()
        x_time = True
        while game.check_state():
            x_time = game.put_symbol(x_time=x_time)
            game.print_matrix()


if __name__ == "__main__":
    TicTacToe.run_game()
