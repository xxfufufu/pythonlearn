import random,sys


def welcome():
    print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.
""")
    
def main():
    print("main")
    
if __name__ == "__main__":
    welcome()
    num_random = num = random.randint(1, 100)
    user_chance = None
    attemps = 0
    while True:
        while True:
            print("""
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
              """)
            text = input("Enter your choice: ").strip()
            try:
                input_number =int(text)
                if input_number not in [1,2,3]:
                    print("Not a correct choice")
                else:
                    if input_number == 1: 
                        user_chance = 10
                    elif input_number ==2:
                        user_chance = 5
                    elif input_number ==3:
                        user_chance =3
                    difficulty = "Easy" if input_number == 1 else "Medium" if input_number == 2 else "Hard"
                    print(f"Great! You have selected the {difficulty} difficulty level.")
                    print("Let's start the game!")
                    break
            except Exception:
                print("Input must be a number")
                
        while True:
            text = input("Enter your guess: ").strip()
            try:
                gues_number = int(text)
                attemps += 1
                if gues_number > num_random:
                    print(f"Incorrect! The number is less than {gues_number}.")
                elif gues_number < num_random:
                    print(f"Incorrect! The number is more than {gues_number}.")
                else:
                    print(f"Congratulations! You guessed the correct number in {attemps} attempts.")
                    while True:
                        action =input("Play again? y/n:").strip()
                        if action == "y":
                            break
                        elif action == "n":
                            print("Goodbye 👋")
                            sys.exit()
                    break
                if attemps >= user_chance:
                    print(f"Opps! Out of attemps")
                    while True:
                        action =input("Play again? y/n:").strip()
                        if action == "y":
                            break
                        elif action == "n":
                            print("Goodbye 👋")
                            sys.exit()
                    break
            except Exception:
                print("Input must be a number")