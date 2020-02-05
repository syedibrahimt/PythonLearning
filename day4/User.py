from day4.BaseEntity import BaseEntity


class User(BaseEntity):
    def __init__(self, name, age, sex) -> None:
        print('### CREATING USER ###')
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self) -> str:
        return f'Name: {self.name}, Age: {self.age}, Sex: {self.sex}'


user = User('syed', 23, 'male')
print(user)
