board = list(range(1, 10))
wins = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]

def draw_board():
    for i in range(2):
        print('|', board[i*3], '|', board[1+i*3], '|', board[2+i*3], '|','\n-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')

def take_input(token):
    while True:
        value = input('Куда ставить ' + token + ": ")
        print(value)
        if not (value in '123456789'):
            print('Ошибочный ввод. Попробуйте снова.')
            continue
        value = int(value)
        if str(board[value-1]) in 'XO':
            print('Эта клетка уже занята')
            continue
        board[value-1] = token
        break

def check_win():
    for move in wins:
        if (board[move[0]-1]) == (board[move[1]-1]) == (board[move[2]-1]):
            return board[move[1]-1]
    else:
        return False

def main():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if counter > 3:
            winner = check_win()
            if winner:
                draw_board()
                print("Победа",winner)
                break
        counter += 1
        if counter > 8:
            draw_board()
            print("Ничья!")
            break
main()