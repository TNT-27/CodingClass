from objects.player import Player
from objects.data import Data
import os, time
from assets import chicken, block, ASSET_MAPPING

data = Data()

def update():
    for item in data.pattern.raw():
        print(ASSET_MAPPING[item])

def loop():
    os.system("cls")
    data.pattern.set("aaaaap")
    update()
    while True:
        move = input("")
        if move == ' ':
            data.pattern.add("a")
        
        os.system("cls")
        update()
        time.sleep(0.1)


def main():
    name = input("What shall your username be?\n> ")
    player = Player(name=name)

    print("Loading Assets...")
    print("Done")

    print("Loading test...\n\n")

    print("☁️")
    print("\n")
    print(block)
    print("\n")
    print(chicken)

    print("Test complete")
    loop()


if __name__ == '__main__':
    main()