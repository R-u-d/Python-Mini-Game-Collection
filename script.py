import random

def number_guessing_game():
    random_number = random.randint(1, 100)
    attempts = 0 
    guessed_correctly = False
    while not guessed_correctly:
            guess = int(input("Guess the number: "))
            attempts += 1
        
            if guess < random_number:
                print("Unlucky! Try again with a higher number.")       
            elif guess > random_number:            
                print("Unlucky! Try again with a lower number.")
            else:
                print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.") 
            guessed_correctly = True 
            try_again = input("would you like to try again(y/n):").strip().lower()
            if try_again !="y":
                 print("thanks for playing, better luck next time :p")
                 break


number_guessing_game()