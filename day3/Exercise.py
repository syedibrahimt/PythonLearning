# problem 1
s = 'django'

print(s[0])

print(s[-1])

print(s[:4])

print(s[1:4])

print(s[::-1])

# problem 2
l = [3, 7, [1, 4, 'hello']]

l[2][2] = 'goodbye'

print(l)

# problem 3

d1 = {'simple_key': 'hello'}

d2 = {'k1': {'k2': 'hello'}}

d3 = {'k1': [{'nested_key': ['this is deep', ['hello']]}]}

print(d1['simple_key'])

print(d2['k1']['k2'])

print(d3['k1'][0]['nested_key'][1][0])

# problem 4

my_list = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4]

print(set(my_list))

# problem 5

age = 4
name = 'Sammy'

print(f'Hello my dogs name is {name} and he is {age} years old')
