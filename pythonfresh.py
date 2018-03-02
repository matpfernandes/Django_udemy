age = 26

name = 'Matheus'

print("Hello my name is {} and i have {}".format(name,age))

if age > 18:
    print("You are older than 18")
else:
    print("You are younger than 18")

def hello():
    print('Hello world!')

def hello_name(name):
    print('Hello '+ name)

def hello_param(name='John'):
    print('Hello '+ name)

hello()
hello()
hello_name('Cheesecake Labs')
hello_param()
hello_param('Dog')

#List
dog_names = ['Dara','Mila']
print(dog_names)
dog_names.insert(0, 'Nero')
dog_names[1] = 'Laika'
print(dog_names)
del(dog_names[-1])
print(dog_names[-1])
print(len(dog_names))


#For
for dog in dog_names:
    print(dog)

for num in range(10):
    print(num)

#While
age = 0
while age < 10:
    print(age)
    age += 1

#Dict
dogs = {"Fido":8,
        "Sally":7}
print(dogs)
print(dogs['Fido'])
dogs['Sara'] = 6
print(dogs)


class Dog:

    dogInfo = 'Hey dogs are cool'

    def bark(self):
        print("BARK!")


mydog = Dog()
print(mydog)
print(mydog.dogInfo)
mydog.dogInfo = 'Hey'
print(mydog.dogInfo)
mydog.bark()


class Dog2:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("BARK!")

myNewDog = Dog2('Dara',20)
print(myNewDog.name)
