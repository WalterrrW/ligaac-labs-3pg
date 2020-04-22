class Animal(object):
    def __init__(self, name, kind):
        self.name = name

    def kind(self):
        return "I am an animal!"


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, "Dog")
        self.name = name

    def pet(self):
        return "I am a dog"


class Cat(Animal):

    def __init__(self, name):
        super(Cat, self).__init__(name, "Cat")
        self.name = name

    def pet(self):
        return "I am a cat"


class Person(object):

    def __init__(self, name):
        self.name = name

    def add_pet(self, animal):
        print(f"I am {animal.name}, {animal.pet()}, {self.name}'s animal! --> {animal.kind()}")


class Employee(Person):
    def __init__(self, person, salary):
        super(Employee, self).__init__(person.name)
        self.Person = person
        self.salary = salary

    def present(self):
        print(f"My name is {person.name} and my salary is {self.salary}")

    def get_salary(self):
        return self.salary

    def lunch(self, fish):
        fish.value()
        fish.element()


class Fish(object):
    def element(self):
        print("I have gill,eye, mouth")

    def value(self):
        print("Normal price")


class Salmon(Fish):
    def value(self):
        print("I worth as much as a diamond!")

    def element(self):
        print("I have gill,eye, mouth and I am a salmon")


class Halibut(Fish):
    def value(self):
        print("Maybe I am cheap but I have character!")

    def element(self):
        print("I have gill,eye, mouth and I am a Halibut")


if __name__ == "__main__":

    person = Person("John")
    dog = Dog("Kira")
    cat = Cat("Zara")
    animal = Animal("Coko", "bird")
    person.add_pet(dog)
    person.add_pet(cat)
    print(animal.kind())
    print()

    employee = Employee(person, 57000) #change the salary to see the change of Fhishes in Employee.lunch
    employee.present()
    print()

    fish = Fish()
    salmon = Salmon()
    halibut = Halibut()

    if employee.get_salary() > 100000:
        employee.lunch(salmon)
    elif employee.get_salary() > 50000:
        employee.lunch(halibut)
    else:
        employee.lunch(fish)
