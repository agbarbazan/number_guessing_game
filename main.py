from controllers.Game import Game 

print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")
user_input = input("Choose a difficulty Type 'easy' or 'hard': ")
game = Game(user_input)
game.play()