secret_number = 7
guess_number = int(input("enter number :"))
attempts = 1
while secret_number != guess_number:
    if guess_number > secret_number:
        print("to high ")
    elif guess_number < secret_number:
        print(" to low ")
    print("guess number is wrong")
    guess_number = int(input("enter number :"))
    attempts +=1
print("congratulation guess number is correct and number of attempts " , attempts )