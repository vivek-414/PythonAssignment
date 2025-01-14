class Animal:
    def speak(self):
        print("Some generic animal sound.")

class Dog(Animal):
    def speak(self):
        print("Woof!")

animal = Animal()
animal.speak()

dog = Dog()
dog.speak()
