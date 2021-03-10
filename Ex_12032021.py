#EXERCISE 1
#ask name
name = input("What is your name? ")
print("Hello, ",name)
#ask age
age = int(input("What is your age? "))
print("You are", age, "old.")
#calculate the corresponding to the next tenth:
x = int(age / 10)
nextdecade = (x + 1) *10
div = nextdecade - age
#Telling the user (using its name) how many years remain before the next decade
print(name,"in",div,"you are",nextdecade,"years old.")

#EXERCISE 2
#Initializing a variable (integer) to a random value between 0 and 100
import random
myrandom = random.randint(0, 100)
#print(myrandom) #for test only
#asking the user to guess it --> 4.4
found = 0
while found < 1:
  userguess = int(input("Guess a number between 0 and 100."))
  #Should say to the user if the actual value is higher, lower or if it was found. Exit only if found.
  if myrandom == userguess:
      print("You guessed right!")
      found = 1
  elif userguess > myrandom:
      print("Your guess is too high!")
  else:
      print("Your guess is too low!")