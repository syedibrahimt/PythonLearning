magic_number = 7
count = 0
while count < 3:
    guessed_number = int(input("Enter your guess : "))
    count += 1
    if guessed_number == magic_number:
        print('You guessed it right!')
        break
else:
    print("sorry you failed")
