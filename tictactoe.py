from requirements import TicTacToe
import os 

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

game = TicTacToe()

player_symbol = ""
while player_symbol not in ["X", "O"]:
    print("Choose your symbol (X or O):")
    player_symbol = input().upper()

computer_symbol = "O" if player_symbol == "X" else "X"
print(f"You chose {player_symbol}. The computer will be {computer_symbol}.\n")

next_move = 1

while next_move == 1:
    clear_screen()
    game.reset()
    game.print_board()

    while game.done == "":
        if player_symbol == "X":  # Jogador começa
            game.check_player_move(player_symbol)
        else:  # Computador começa
            game.make_move(computer_symbol)

        clear_screen()
        game.print_board()
        game.check_winner_draw()

        if game.done == "":
            if player_symbol == "O":
                game.check_player_move(player_symbol)
            else:
                game.make_move(computer_symbol)

        clear_screen()
        game.print_board()
        game.check_winner_draw()

    print("Type 1 to play again or any other key to exit:")
    try:
        next_move = int(input())
    except ValueError:
        next_move = 0