import random

def number_guessing_game():
    random_number = random.randint(1, 100)
    attempts = 0 
    guessed_correctly = False
    while not guessed_correctly:
        guess = input("Guess the number: ")
        if guess.isdigit():
            guess = int(guess)
            attempts += 1
            if guess < random_number:
                print("Unlucky! Try again with a higher number.")       
            elif guess > random_number:            
                print("Unlucky! Try again with a lower number.")
            else:
                print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.") 
                guessed_correctly = True 
            while True:
                print('Do you want to play again? (y/n)')
                try_again = input().lower()
                if try_again == "y":
                    number_guessing_game()
                    return
                elif try_again == "n":
                    print('Thanks for playing, good luck next time!')
                    return
                else:
                    print('Incorrect input, please input y/n')
        else:
            print('Not a number, please input a number')


number_guessing_game()