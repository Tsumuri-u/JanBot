"""JanBot entry point script"""

from hand import Hand
from wall import Wall

def main():
    choice = ""
    while choice != "q":
        print("(1) Hand analysis\n(2) Quit")
        choice = input()

        if choice == "1":
            inithand()
        elif choice == "2":
            choice = "q"

def inithand():
    playerHand = Hand()
    wall = Wall()

if __name__ == "__main__":
    main()