# import random
# winning_number = 43
# guess = 1
# number = int(input("guess a number between 1 and 100 "))
# game_over = False
# while not game_over:
#     if number == winning_number:
#         print(f"you win, and you guessed this number in {guess} times")
#         # WIN!!!
#         game_over = True
#     else:
#         if number < winning_number:
#             print("too low")
            
#         else:
#             print("too high")
           
#         guess += 1
#         number = int(input("guess again :"))
        
            #  guess wrong

# import random


# winning_number = random.randint(1,100)
# guess = 1
# number = int(input("guess a number between 1 and 100 "))
# game_over = False
# while not game_over:
#     if number == winning_number:
#         print(f"you win, and you guessed this number in {guess} times")
#         # WIN!!!
#         game_over = True
#     else:
#         if number < winning_number:
#             print("too low")
            
#         else:
#             print("too high")
           
#         guess += 1
#         number = int(input("guess again :"))
        
import random
c = random.randint(1,100)
userinput = int(input("enter"))
if c == userinput:
    print("WIN11")
else:
    if userinput>c:
        print("high")
    else:
        print("Low")
    userinput = False
    userinput = int(input())