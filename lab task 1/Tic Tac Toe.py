

class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def print_board(self):
        print("\n")
        for i in range(3):
            print(" | ".join(self.board[i]))
            if i < 2:
                print("--+---+--")

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            return True
        else:
            print(" Cell already taken! Try again.")
            return False

    def check_winner(self):
        
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def is_draw(self):
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
        return True


game = TicTacToe()

while True:
    game.print_board()
    print(f"Player {game.current_player}'s turn")
    r = int(input("Enter row (0-2): "))
    c = int(input("Enter col (0-2): "))

    if game.make_move(r, c):
        if game.check_winner():
            game.print_board()
            print(f" Player {game.current_player} Wins!")
            break
        elif game.is_draw():
            game.print_board()
            print(" It's a Draw!")
            break
        game.switch_player()
