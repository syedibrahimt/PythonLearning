weight = int(input('Enter your weight : '))
current_unit = input("L(lbs) or K(kgs) : ")
if current_unit.lower() == 'l':
    message = f'{int(weight * .45)} kg is your weight'
elif current_unit.lower() == 'k':
    message = f'{int(2.2 * weight)} lbs is your weight'
else:
    message = 'Invalid input'
print(message)
