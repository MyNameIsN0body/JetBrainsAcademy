# RAW need to finish
import random
import re

from random import randint

state = random.getstate()
random.seed(0)
random.setstate(state)
total_dominoes = [[y, x] for x in range(7) for y in range(x + 1)]
stock = []
computer = []
player = []
domino_snake = []
active_player = computer
game_over = False



def isdigit(string):
    return bool(re.match(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)', string))


def take_from_stock(who):
    if len(stock) != 0:
        who.append(stock.pop(randint(0, len(stock) - 1)))


def find_active_player():  # this method works
    global active_player
    if len(player) == len(computer):
        active_player = computer if active_player == player else computer
    elif len(player) > len(computer):
        active_player = player
    else:
        active_player = computer


def say_status(active_p):
    if active_p == player:
        print(f"\nStatus: It's your turn to make a move. Enter your command.")
    else:
        print(f"\nStatus: Computer is about to make a move. Press Enter to continue...")


def start():
    while len(domino_snake) == 0:
        global stock
        global computer
        global player
        stock = total_dominoes[:]
        for _ in range(7):
            take_from_stock(computer)
            take_from_stock(player)

        doublet_computer = [item for item in computer if item[0] == item[1]]
        doublet_player = [item for item in player if item[0] == item[1]]

        if len(doublet_computer) != 0 and len(doublet_player) != 0:
            max_computer = max(sorted(doublet_computer))
            max_player = max(sorted(doublet_player))
            max_computer_index = computer.index(max_computer)
            max_player_index = player.index(max_player)
            max_doublet = player.pop(max_player_index) if max_player > max_computer else computer.pop(
                max_computer_index)
            domino_snake.append(max_doublet)
        elif len(doublet_computer) != 0 and len(doublet_player) == 0:
            max_computer = max(sorted(doublet_computer))
            max_computer_index = computer.index(max_computer)
            max_doublet = computer.pop(max_computer_index)
            domino_snake.append(max_doublet)
        elif len(doublet_player) != 0 and len(doublet_computer) == 0:
            max_player = max(sorted(doublet_player))
            max_player_index = player.index(max_player)
            max_doublet = player.pop(max_player_index)
            domino_snake.append(max_doublet)
        else:
            continue


start()


def show_domino_snake():  # this method works
    if len(domino_snake) > 6:
        result = f"{''.join(str(e) for e in domino_snake[:3])}...{''.join(str(e) for e in domino_snake[-3:])}"
    else:
        result = ''.join(str(e) for e in domino_snake)
    print(f"{result}\n")


def add_in_snake(from_whom, number):  # this method works
    number = int(number)
    element = from_whom[abs(number) - 1]
    if number == 0:
        take_from_stock(from_whom)
    elif number > 0:
        last_element = domino_snake[len(domino_snake) - 1][1]
        if last_element != element[0]:
            swap_bone(element)
        domino_snake.append(from_whom.pop(number - 1))
    elif number < 0:
        first_element = domino_snake[0][0]
        if first_element != element[1]:
            swap_bone(element)
        domino_snake.insert(0, from_whom.pop(abs(number) - 1))


def swap_bone(bone):  # this method works
    temp = bone[0]
    bone[0] = bone[1]
    bone[1] = temp
    return bone


def show_your_pieces():  # this method works
    print("Your pieces:")
    count = 1
    for i in player:
        print(f"{count}:{i}")
        count += 1


def check(num, player_active):
    gamer = player_active
    bone = num

    while abs(int(bone)) > len(gamer):
        bone = input("Invalid input. Please try again.\n")
    return bone


def sorted_dict(dict):
    sorted_values = sorted(dict.values(), reverse=True)
    sorted_dict = {}
    for i in sorted_values:
        for k in dict.keys():
            if dict[k] == i:
                sorted_dict[k] = dict[k]
                break
    return sorted_dict

def move_computer():
    first_element = domino_snake[0][0]
    last_element = domino_snake[len(domino_snake) - 1][1]
    all = [x for item in (computer + domino_snake) for x in item]
    cost_element = {i: all.count(i) for i in all}
    result = {}
    index = 0
    for x in computer:
        result[index] = cost_element.get(x[0]) + cost_element.get(x[1])
        index += 1
    sorted_dic = sorted_dict(result)
    sorted_computer = []
    for key in sorted_dic:
        sorted_computer.append(computer[key])

    for item in sorted_computer:
        if last_element in item:
            add_in_snake(computer, computer.index(item) + 1)
            break
        elif first_element in item:
            add_in_snake(computer, -(computer.index(item) + 1))
            break
    else:
        take_from_stock(computer)


def check_draw(snake):
    if snake[0][0] == snake[len(snake) - 1][1] and [element for item in snake for element in item].count(5) == 8 or len(domino_snake) == 0:
        print("Status: The game is over. It's a draw!")
        game_over =True


def print_state():
    print('=' * 70)
    print(f"Stock size: {len(stock)}")
    print(f"Computer pieces: {len(computer)}\n")



def massage_title():  # this method works
    print_state()
    show_domino_snake()
    show_your_pieces()
    check_draw(domino_snake)
    if not game_over:
        say_status(active_player)



def is_winner():  # this method works
    if len(active_player) == 0:
        print_state()
        show_domino_snake()
        show_your_pieces()
        win = "\nStatus: The game is over. The computer won!" if active_player == computer else "\nStatus: The game is over. You won!"
        print(win)
        game_over = True
        return True
    return False


def massage_invalid(gamer):  # this method works
    if gamer == player:
        print("Invalid input. Please try again.\n")
    elif gamer == computer:
        print("Invalid input. Please try again.\n")


def check_bone(number_bone, gamer):  # this method works
    element = gamer[abs(int(number_bone)) - 1]
    first_element = domino_snake[0][0]
    last_element = domino_snake[len(domino_snake) - 1][1]
    return first_element in element or last_element in element


def check_input(player):
    while True:
        bone_number = input()
        if bone_number == '0':
            return 0
        elif bone_number == "" or not isdigit(bone_number) or abs(int(bone_number)) > len(player):
            massage_invalid(active_player)
            continue

        number_bone = int(bone_number)
        if number_bone > 0:
            if domino_snake[len(domino_snake) - 1][1] == player[abs(int(number_bone)) - 1][1]:
                swap_bone(player[abs(int(number_bone)) - 1])
                return number_bone
            elif domino_snake[len(domino_snake) - 1][1] == player[abs(int(number_bone)) - 1][0]:
                return number_bone
            else:
                print(f"\nIllegal move. Please try again.")
        elif number_bone < 0:
            if domino_snake[0][0] == player[abs(int(number_bone)) - 1][0]:
                swap_bone(player[abs(int(number_bone)) - 1])
                return number_bone
            elif domino_snake[0][0] == player[abs(int(number_bone)) - 1][1]:
                return number_bone
            else:
                print(f"\nIllegal move. Please try again.")



find_active_player()
while not is_winner():
    check_draw(domino_snake)
    while active_player == computer and not is_winner():
        massage_title()
        bone_number = input()

        if bone_number != "":
            bone_number = massage_invalid(active_player)
        move_computer()
        if is_winner():
            break
        active_player = player

    while active_player == player and not is_winner():
        massage_title()
        bone_number = check_input(active_player)
        if bone_number is not None:
            add_in_snake(active_player, bone_number)
        if is_winner():
            break
        active_player = computer

