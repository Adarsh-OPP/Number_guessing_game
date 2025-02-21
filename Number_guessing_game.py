import random
secret = random.randint(1, 10)
print("You got 5 attempt--")

for _ in range(5):
    guess = int(input("GUESS  THE NUMBER: "))

    if (guess == secret):
        print("You Got The Number")
        break

    elif (guess > secret):
        print("guess is high")

    elif (guess < secret):
        print("guess is low")
    
else :
    print("guess is over the number is", secret)