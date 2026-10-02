import random

def dice_roll():
 dice1 = random.randint(1,6)
 dice2 = random.randint(1,6)

 print("you rolled:", dice1, "and", dice2)
 print("you got:", dice1 + dice2)

def main():
 while True:
     print("\n")
     print("1. Roll the dice")
     print("2. exit")

     userchoice = input("Enter your choice:")

     if userchoice == "1":
       dice_roll()

     elif userchoice == "2":
       print("Thanks for playing.")
       break
     
     else:
       print("invalid choice.")

main()
