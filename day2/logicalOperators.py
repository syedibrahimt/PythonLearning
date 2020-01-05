name = input('Enter your name : ')
if len(name) < 3:
    print("Name must be atleast 3 characters")
elif len(name) > 10:
    print("Name must be atmost 10 characters")
else:
    print('You are good to go')
