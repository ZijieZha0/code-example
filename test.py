from rockpaperscissors2333.cli import play, simulate, tutorial
from rockpaperscissors2333.game import reset_scoreboard
while True:
        print("Welcome to Rock, Paper, Scissors!")
        print("1. View tutorial")
        print("2. Play against the computer")
        print("3. Simulate a game between two players")
        print("4. Reset the scoreboard")
        print("5. Quit")
        choice = input("Enter the number of your choice: ")
        if choice == "1":
            tutorial()
        elif choice == "2":
            play()
        elif choice == "3":
            simulate()
        elif choice == "4":
            reset_scoreboard()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")   