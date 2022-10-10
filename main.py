import functions as fc


ans = fc.word()
counter = 0
tries = 1
letters =[]
while tries < 6:
    print("Don't use these: ", letters)
    user = input("Type your answer: ")
    assert fc.contains_number(user) == False, "Numbers are not allowed"
    assert len(user) == 5, "The word must have 5 letters"
    for counter in range(0, 5):
        if user[counter] == ans[counter]:
            print(user[counter]+' ✔')
        else:
            if all([char in ans for char in user[counter]]) is True:
                print(user[counter]+' 🟡')
            else:
                print(user[counter] + ' ❌')
                x = user[counter]
                letters.append(x)
        counter = counter + 1
    if user == ans:
        print('You Win')
        break
    counter = 0
    tries = tries + 1

if tries == 6:
    print('You Lose')
    print("The solution was: ", ans)
