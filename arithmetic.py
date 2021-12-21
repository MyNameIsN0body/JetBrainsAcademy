import random

true_answer = 0
count = 0
amount_question = 5
yes = ["yes", "YES", 'y', "Yes"]


def question():
    while True:
        result = int(input("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29\n"""))
        if result == 1 or result == 2:
            return result
        else:
            print("Incorrect format.")


def level_condition(lev, condit):
    if lev == 1:
        return int(eval(condit))
    elif lev == 2:
        return int(condit) ** 2


level = question()

for _ in range(amount_question):

    if level == 1:
        list_level = [x for x in range(2, 10, 1)]
        oper = random.choice(['+', '-', '*'])
        x, y = random.choices(list_level, k=2)
        condition = f"{x} {oper} {y}\n"
    else:
        list_level = [x for x in range(11, 30, 1)]
        x = random.choice(list_level)
        condition = f"{x}\n"

    answer = 0

    while True:
        try:
            answer = int(input(condition))
        except ValueError:
            print("Wrong format! Try again.")
            continue
        else:
            break

    if int(answer) == level_condition(level, condition):
        count += 1
        true_answer += 1
        print("Right!")
    else:
        print("Wrong!")
        count += 1

answer_2 = input(f"Your mark is {true_answer}/{amount_question}. Would you like to save the result? Enter yes or no.\n")
if answer_2 in yes:
    name = input("What is your name?\n")
    level_description = "(simple operations with numbers 2-9)" if level == 1 else "(integral squares of 11-29)"
    file_result = open("results.txt", 'a')
    file_result.write(f"{name}: {true_answer}/{amount_question} in level {level} {level_description}.")
    file_result.close()
    print('The results are saved in "results.txt".')
