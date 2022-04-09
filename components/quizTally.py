from .vars import quizTotal, character, characters, images
from PIL import Image

def total(value):
    if value == 4:
        character = characters [0]
        print("It's " + character)
        zeusImage = Image.open("components/images/zeus.jpg")
        zeusImage.show()

    if value == 3:
        character = characters [1]
        print("It's " + character)
        athenaImage = Image.open("components/images/athena.jpg")
        athenaImage.show()

    if value == 1:
        character = characters [2]
        print("It's " + character)
        poseidonImage = Image.open("components/images/poseidon.jpg")
        poseidonImage.show()

    if value == 0:
        character = characters [3]
        print("It's " + character)
        hadesImage = Image.open("components/images/hades.jpg")
        hadesImage.show()

    if value == 2:
        character = characters [4]
        print("It's " + character)
        gaiaImage = Image.open("components/images/gaia.jpg")
        gaiaImage.show()
