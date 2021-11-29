memory = 0
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):\n"
msg_5 = "Do you want to continue calculations? (y / n):\n"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)\n"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)\n"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)\n"
msg_list = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]


def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


def check_memory(current):
    return str(memory) if current == 'M' else current


def is_one_digit(v):
    if (v > -10 and v < 10) and v.is_integer():
        return True
    return False


def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg = msg + msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)


answer_continue = 'y'
while answer_continue == 'y':
    print(msg_0)
    x, oper, y = input().split()
    x = check_memory(x)
    y = check_memory(y)
    if (is_digit(x) and is_digit(y.replace(',', '.', 1))) is not True:
        print(msg_1)
        continue
    x = float(x)
    y = float(y)
    check(x, y, oper)
    result = 0
    if oper == '+':
        result = x + y
    elif oper == '-':
        result = x - y
    elif oper == '*':
        result = x * y
    elif oper == '/':
        if y == 0:
            print(msg_3)
            continue
        result = x / y
    else:
        print(msg_2)
        continue
    print(result)
    answer_store = input(msg_4)
    if answer_store == 'y':
        if is_one_digit(result):
            msg_index = 10
            while msg_index < 13:
                read_answer = input(msg_list[msg_index])
                if read_answer == 'y':
                    msg_index += 1
                elif read_answer == 'n':
                    break
            else:
                memory = result
        else:
            memory = result

    answer_continue = input(msg_5)
    if answer_continue == 'y':
        continue
    elif answer_continue == 'n':
        break
