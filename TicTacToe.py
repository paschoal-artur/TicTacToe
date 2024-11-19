import random 
import os 

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
        dict_win = {}
        for i in ["X", "O"]:
            #Horizontais
            dict_win[i] = (self.board[0][0] == self.board[0][1] == self.board[0][2] == i)
            dict_win[i] = (self.board[1][0] == self.board[1][1] == self.board[1][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[2][1] == self.board[2][2] == i) or dict_win[i]
            # Verticals
            dict_win[i] = (self.board[0][0] == self.board[1][0] == self.board[2][0] == i) or dict_win[i]
            dict_win[i] = (self.board[0][1] == self.board[1][1] == self.board[2][1] == i) or dict_win[i]
            dict_win[i] = (self.board[0][2] == self.board[1][2] == self.board[2][2] == i) or dict_win[i]
            #Diagonals
            dict_win[i] = (self.board[0][0] == self.board[1][1] == self.board[2][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[1][1] == self.board[0][2] == i) or dict_win[i]

            if dict_win['X']:
                self.done = 'x'
                print("X wins!")
            elif dict_win['O']:
                self.done = 'o'
                print("O wins!")
            
            c = 0
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] != " ":
                        c += 1
                        break 
            if c == 0:
                self.done = "d"
                print("Draw!")
                return  

    def make_move(self):
        list_moves = []

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    list_moves.append([i, j])
            if len(list_moves) > 0:
                move = random.choice(list_moves)
                self.board[move[0]][move[1]] = "O"

    def check_player_move(self):
        invalid_mode = True

        while invalid_mode:
            try:
                print("Type the line of your next move")
                x = int(input())

                print("Type the column of your next move")
                y = int(input())

                if x > 2 or x < 0 or y > 2 or y < 0:
                    print("Invalid move, try again")

                if self.board[x][y] != " ":
                    print("Position already taken, try again")
                    continue 
            except Exception as e:
                print(e)
                continue 
            invalid_mode = False
        self.board[x][y] = "X"

self = TicTacToe()
self.print_board()
next = 0

while next == 0:
    os.system("clear")
    TicTacToe.print_board()
    while TicTacToe.done == "":
        TicTacToe.check_player_move()
        TicTacToe.make_move()
        os.system("clear")
        TicTacToe.print_board()
        TicTacToe.check_winner_draw()
    print("Type 1 to play again or any key to exit")

    next = int(input())
    if next == 1:
        break 
    else:
        TicTacToe.reset()
        next = 0