import random
word = "Apple"
numbers_of_errors_allowed = 9
guesses = []
done = False

while not done:
     for letter in word:
          if letter.lower() in guesses:
               print(letter, end=" ")
          else:
               print("_", end=" ")
     print("")
     done = True

     guess = input("Allowed errors left {numbers_of_errors_allowed}, next guess: ")
     guesses.append(guess.lower())
     if guess.lower() not in word.lower():
          numbers_of_errors_allowed -= 1
          if numbers_of_errors_allowed == 0:
               break
     done = True
     for letter in word:
          if letter.lower() not in guesses:
               done = False
if done:
     print("Done!")
else:
     print("Game Over!")
     