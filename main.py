import functions as fc

ans = fc.word()
counter = 0
tries = 1
while tries < 6:
    user = input("Type your answear: ")
    assert len(user) == 5, "The word must have 5 letters"
    for  counter in range(0,5):
        if user[counter]==ans[counter]:
            print(user[counter]+' ✔')
        else:
            if all([char in ans for char in user[counter] ]) == True:
                print(user[counter]+' 🟡')
            else:
                print(user[counter] + ' ❌')
        counter = counter + 1
    if user == ans:
        print('You Win')
        break
    counter = 0
    tries = tries + 1

if tries == 6:
    print('You Lose')
