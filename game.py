
i = 0
while i < 3:
    question = input("who's the first president of Ghana?\nYour answer: ")
    response = question.lower()

    if len(response.split()) == 2:
        name = response.split()
        if "kwame" and "nkrumah" in name:
            print("congratulation, you won")
            break
    i += 1
else:
    print("You lost, try again")
    