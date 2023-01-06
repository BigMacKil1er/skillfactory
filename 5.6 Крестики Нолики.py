num_field = list(range(1, 10))
check_win = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7),]
a, b, c, d, e, f = [], '', '', '', '', ''

def show_field():
    print('___________________')
    for i in range(3):
        print('|     |     |     |')
        print('| ', num_field[0 + i*3], ' | ', num_field[1 + i*3], ' | ', num_field[2 + i*3],' |')
        print('|_____|_____|_____|')


def check_input(player):
    while True:
        value = input(f'{b}' +player+ ' ? ')
        if not (value in '123456789'):
            print(c)
            continue
        value = int(value)
        if str(num_field[value-1]) in 'XO':
            print(d)
            continue
        num_field[value-1] = player
        break

def definition_of_victory():
    for i in check_win:
        if (num_field[i[0]-1]) == (num_field[i[1]-1]) == (num_field[i[2]-1]):
            return num_field[i[1]-1]
    else:
        return False

def language():
    global a, b, c, d, e, f, g, h
    while True:
        lang = input('Choose language: English or Russian. Enter Eng or Rus: ')
        if lang.lower() == 'rus':
            a = ['Приветствую! Это игра крестики нолики! Правила очень просты!',
                'Игроки по очереди ставят на свободные клетки поля',
                '3×3 знаки (один всегда крестики, другой всегда нолики).',
                'Первый, выстроивший в ряд 3 своих фигуры по вертикали,',
                'горизонтали или диагонали, выигрывает. Первый ход делает игрок, ставящий крестики.'
                'В ответе укажите цифру, на место которой хотите поставить Х или О']
            b = 'Куда поставить: '
            c = 'Неверный ввод!'
            d = 'Клетка занята'
            e = 'Победа!'
            f = 'Ничья'
            g = 'Хотите сиграть еще? ответь "да" или "нет"? '
            h = 'Увидимся снова!'
            break
        elif lang.lower() == 'eng':
            a = ["Greetings! It's a tic-tac-toe game! The rules are very simple!",
                "Players take turns betting on free squares",
                "3×3 characters (one is always crosses, the other is always zeros).",
                "The first one to line up 3 of his pieces vertically,",
                "horizontal or diagonal, wins. The first move is made by the player placing crosses."
                "In your answer, indicate the number where you want to put X or O"]
            b = 'Where to put: '
            c = 'Invalid input!'
            d = 'The cell already matters.'
            e = 'Victory!'
            f = 'Draw'
            g = 'Do you want to play more? answer "yes" or "no"? '
            h = 'See you again!!'
            break
        else:
            print('Invalid input! Try again')
            continue
    return a

def try_():
    while True:
        again = input(g)
        if again.lower() == 'да' or again.lower() == 'yes' or again.lower() == '1':
            main()
        elif again.lower() == 'нет' or again.lower() == 'no' or again.lower() == '2':
            print(h)
            break
        else:
            print(c)
            continue

def main():
    counter = 0
    global num_field
    num_field = list(range(1, 10))
    while True:
        show_field()
        if counter % 2 == 0:
            check_input('X')
        else:
            check_input('O')
        if counter > 3:
            winner = definition_of_victory()
            if winner:
                show_field()
                print(winner, e)
                try_()
                break
        counter += 1
        if counter > 8:
            show_field()
            print(f)
            try_()

print(*language(), sep='\n')
main()
print("Член")


