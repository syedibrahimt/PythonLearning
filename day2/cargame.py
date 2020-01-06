command = ''
while command != 'quit':
    command = input("> ").lower()
    if command == 'help':
        print('''start - to start the car
            stop - to stop the car
            quit - to exit
            help - to get help''')
    elif command == 'start':
        print('Car started! Ready to GO!')
    elif command == 'stop':
        print('Car stopped')
    else:
        print("Invalid Input. Do HELP")
else:
    print('Game over!!')
