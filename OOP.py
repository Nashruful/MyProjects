class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self,age):
        self.age = age
        return age

d = Dog("mr aziz", 53)
print(f'your name is {d.name} and ur age is {d.age}')

print(d.set_age(11))