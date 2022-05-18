from random import randint

class Game:
    def __init__(self, difficulty_level):
        self.difficulty_level = difficulty_level
        self.number = randint(1,100)
        self.attempts_remaining = 10 if difficulty_level == "easy" else 5
    
    def make_guess(self):
        while self.attempts_remaining > 0:
            print(f"You have {self.attempts_remaining} attempts remaining to guess the number.")
            user_input = int(input("Make a guess: "))
            if user_input != self.number:
                if user_input > self.number:
                    print("Too high.")
                else:
                    print("Too low.")
                self.attempts_remaining -= 1
                if self.attempts_remaining != 0: print("Guess again.")
            else:
                print("You guessed correctly!")
                return 
        return print("Out of guesses.")
    
    def play(self):
        self.make_guess()
