from components import vars
from PIL import Image

def total(value):
    if value <= 4:
        vars.character = vars.character [0]
        print("It's " + vars.character)
        zeusImage = Image.open("zeus.jpg")
        zeusImage.show()

    if value <= 3:
        vars.character = vars.character [1]
        print("It's " + vars.character)
        athenaImage = Image.open("athena.jpg")
        athenaImage.show()

    if value <= 1:
        vars.character = vars.character [2]
        print("It's " + vars.character)
        poseidonImage = Image.open("poseidon.jpg")
        poseidonImage.show()

    if value <= 0:
        vars.character = vars.character [3]
        print("It's " + vars.character)
        hadesImage = Image.open("poseidon.jpg")
        hadesImage.show()

    if value <= 2:
        vars.character = vars.character [4]
        print("It's " + vars.character)
        gaiaImage = Image.open("gaia.jpg")
        gaiaImage.show()
