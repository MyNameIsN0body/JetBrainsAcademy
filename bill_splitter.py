import random

dict_friends = {}
count_friends = int(input("Enter the number of friends joining (including you):\n"))
if count_friends > 0:
    print("\nEnter the name of every friend (including you), each on a new line:")
    for _ in range(count_friends):
        dict_friends.update({input(): 0})
    receipt = int(input("Enter the total bill value:\n"))
    receipt_for_friend = round(receipt / count_friends, 2)
    for x in dict_friends.keys():
        dict_friends[x] = receipt_for_friend
    answer = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if answer == "Yes":
        lucky = random.choice(list(dict_friends.keys()))
        receipt_for_friend = round(receipt / (count_friends - 1), 2)
        for x in dict_friends.keys():
            if x == lucky:
                dict_friends[x] = 0
            else:
                dict_friends[x] = receipt_for_friend
        print(f"\n{lucky} is the lucky one!\n")
    else:
        print("No one is going to be lucky\n")
    print(dict_friends)
else:
    print("No one is joining for the party")
