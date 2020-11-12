print("Крестики-нолики")
field = ['.', '.', '.',
         '.', '.', '.',
         '.', '.', '.']

game_continues = True
current_player = "X"
winner = None

def display_field():
    print(field[0] + " " + field[1] + " " + field[2])
    print(field[3] + " " + field[4] + " " + field[5])
    print(field[6] + " " + field[7] + " " + field[8])

def play_game():
    display_field()
    while game_continues:
        handle_turn(current_player)
        check_game_over()
        change_player()
    if winner == "X" or winner == "O":
        print("Победа " + winner)
    elif winner == None:
        print("Ничья")

def handle_turn(player):
    print("Ход " + player)
    position = input("Введите значение от 1 до 9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Пожалуйста, введите значение от 1 до 9: ")
        position = int(position) - 1
        if field[position] == ".":
            valid = True
        else:
            print("Такой ход нельзя совершить! Попробуйте еще раз!")
    field[position] = player
    display_field()

def check_game_over():
    check_win()
    check_tie()

def check_win():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():
    global game_continues
    row_1 = field[0] == field[1] == field[2] != "."
    row_2 = field[3] == field[4] == field[5] != "."
    row_3 = field[6] == field[7] == field[8] != "."
    if row_1 or row_2 or row_3:
        game_continues = False
    if row_1:
        return field[0]
    elif row_2:
        return field[3]
    elif row_3:
        return field[6]
    return

def check_columns():
    global game_continues
    column_1 = field[0] == field[3] == field[6] != "."
    column_2 = field[1] == field[4] == field[7] != "."
    column_3 = field[2] == field[5] == field[8] != "."
    if column_1 or column_2 or column_3:
        game_continues = False
    if column_1:
        return field[0]
    elif column_2:
        return field[1]
    elif column_3:
        return field[2]
    return

def check_diagonals():
    global game_continues
    diagonal_1 = field[0] == field[4] == field[8] != "."
    diagonal_2 = field[6] == field[4] == field[2] != "."
    if diagonal_1 or diagonal_2:
        game_continues = False
    if diagonal_1:
        return field[0]
    elif diagonal_2:
        return field[6]
    return

def check_tie():
    global game_continues
    if "." not in field:
        game_continues = False
    return

def change_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()