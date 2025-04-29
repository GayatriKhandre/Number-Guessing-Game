import random
num = random.randint(1,10)
print("Welcome to Numner Guessing Game")
print("You will have 3 chances")
user_chance = 1
user_num = int(input("Enter a number between 1 to 10: "))
while user_num != num and user_chance < 3:
    user_chance += 1
    user_num = int(input("Enter a number between 1 to 10: "))
    
if  user_num == num:
    print("Well Done!")
    print("You took",user_chance,"chances to guess.") 
   
else:
    print("Sorry, Better luck next time.")
print("Thank you!")