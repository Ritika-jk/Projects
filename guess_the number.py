import random
Target = random.randint(0,100)
while True:
    user_choice = int (input("guess number: "))
    if(user_choice == Target ):
        print("Success : Correct Guess")
        break
    elif(user_choice < Target):
        print (" your number is lesser than target. Take a bigger guess")  
    else:
        print("your number is greater than target. Take a smaller guess")

print("-------Game Over-----")       