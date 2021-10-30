import random

print("H A N G M A N")


def play():
    dic = ['python', 'java', 'kotlin', 'javascript']
    result = random.choice(dic)
    word = '-' * len(result)
    lives = 8
    won = False
    answers = set()
    while lives > 0 and not won:
        print(f"\n{word}")
        answer = input("Input a letter: ")
        if len(answer) != 1:
            print("You should input a single letter")
            continue
        if not (96 < ord(answer) < 123):
            print("Please enter a lowercase English letter")
            continue
        if answer in answers:
            print("You've already guessed this letter")
            continue
        else:
            answers.add(answer)

        if answer in result:
            for x in range(len(result)):
                if answer == result[x]:
                    word = word[:x] + result[x] + word[x + 1:]
        else:
            print(f"That letter doesn't appear in the word")
            lives -= 1
        if word == result:
            won = True
            print(f"""You guessed the {word}!
    You survived!""")
    if not won:
        print("You lost!")


while True:
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == "exit":
        break
    elif menu == "play":
        play()
