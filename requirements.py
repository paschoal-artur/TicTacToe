import random

class TicTacToe:
    def __init__(self):
        self.reset()

    def print_board(self):
        print("")
        print(" " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2])
        print("-----------")
        print(" " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2])
        print("-----------")
        print(" " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2])

    def reset(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.done = ""

    def check_winner_draw(self):
        for symbol in ["X", "O"]:
            # Verificar condições de vitória
            if any(
                all(self.board[i][j] == symbol for j in range(3)) or
                all(self.board[j][i] == symbol for j in range(3)) or
                all(self.board[j][j] == symbol for j in range(3)) or
                all(self.board[j][2 - j] == symbol for j in range(3))
                for i in range(3)
            ):
                self.done = symbol
                print(f"{symbol} wins!")
                return

        # Verificar empate
        if all(self.board[i][j] != " " for i in range(3) for j in range(3)):
            self.done = "d"
            print("Draw!")

    def make_move(self, symbol="O"):
        list_moves = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == " "]
        if list_moves:
            move = random.choice(list_moves)
            self.board[move[0]][move[1]] = symbol

    def check_player_move(self, player_symbol):
        while True:
            try:
                print("Type the line of your next move (0-2):")
                x = int(input())
                print("Type the column of your next move (0-2):")
                y = int(input())

                if 0 <= x <= 2 and 0 <= y <= 2 and self.board[x][y] == " ":
                    self.board[x][y] = player_symbol
                    break
                print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter numbers between 0 and 2.")
