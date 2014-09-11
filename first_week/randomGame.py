import random
min_value = 1
max_value = 100
compnum = random.randint(min_value, max_value)
usernum = 0
attempts = 0
print("Try to guess a number from 1 to 100")
while usernum !="":
       usernum = input()
       attempts += 1
       if not usernum.isdigit():
              print("Please, write number!")
              continue
       usernum = int(usernum)
       if usernum > compnum:
           print("Too big, try again")
           continue
       elif usernum < compnum:
           print("Too small, try again")
           continue
       else:
           attempts = str(attempts)
           print("Congratulations, you guessed right with " + attempts + " attempts")
input()
