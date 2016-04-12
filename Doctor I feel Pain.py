
#Players get 10 guesses.
#They must guess a random number.
#It has to be a whole number from 1 to 10
#Tell them if they are too high or too low if they guess wrong
#Tell them how many guesses they have made

import random


random_number = random.randint(1,10)
tries = 0
tries_remaining = 10


while tries < 10:
  guess = input('Your patient is experiencing some pain. They won\'t tell you\
 unless you guess. Guess a number from 1-10 ')
  tries += 1
  tries_remaining -= 1

  try:
    guess_num = int(guess)
  except:
    print("Patient says: That's not a whole number! You suck!! ")
    break

  if not guess_num > 0 or not guess_num < 11:
    print("That number is not between 1 and 10.")
    break



  elif guess_num == random_number:
    print("You\'re right Doc!")
    print("It took you {} tries. ".format(tries))
    break


  elif guess_num < random_number:
    if tries_remaining > 0:
      print("That number is low. You have {} tries..".format(int(tries_remaining)))
      continue
    else:
      print("It feels more like a {}".format(random_number))
      print("I\'m leaving.")



  elif guess_num > random_number:
    if tries_remaining > 0:
      print("That number is too high Doc. You have {} more tries.".format(int(tries_remaining)))
      continue
    else:
      print("My number was {}".format(random_number))
      print("Bye.")

