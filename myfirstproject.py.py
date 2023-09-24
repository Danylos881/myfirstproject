board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board():
    print('------------')
    for row in board:
        print(f'| {" | ".join(row)} |')
        print('------------')

def check_win(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def make_move(player):
    while True:
        move = input("Ваш ход (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            index = int(move) - 1
            row, col = divmod(index, 3)
            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("Клетка уже занята!")
        else:
            print("Некорректный ввод!")

def main():
    print("Игра крестики-нолики!")
    print_board()

    players = ['X', 'O']
    current_player = 0

    while True:
        make_move(players[current_player])
        print_board()

        if check_win(players[current_player]):
            print(f"Игрок {players[current_player]} победил!")
            break

        if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            print("Ничья!")
            break

        current_player = (current_player + 1) % 2

if __name__ == '__main__':
    main()