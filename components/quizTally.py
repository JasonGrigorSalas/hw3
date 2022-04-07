from components import vars
def total(value):
    if value <= 4:
        vars.character = vars.character [0]
        print("It's " + vars.character)

    if value <= 3:
        vars.character = vars.character [1]
        print("It's " + vars.character)

    if value <= 1:
        vars.character = vars.character [2]
        print("It's " + vars.character)

    if value <= 0:
        vars.character = vars.character [3]
        print("It's " + vars.character)

    if value <= 2:
        vars.character = vars.character [4]
        print("It's " + vars.character)
