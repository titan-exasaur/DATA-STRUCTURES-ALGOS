class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("woof!")

class Cat(Animal):
    def speak(self):
        print("meow!")

class Mouse(Animal):
    def speak(self):
        print("squeak!")

dog1 = Dog("Dx")
dog1.eat()
dog1.sleep()
dog1.speak()

cat1 = Cat("Dotty")
cat1.eat()
cat1.sleep()
cat1.speak()

mouse1 = Mouse("Mickey")
mouse1.eat()
mouse1.sleep()
mouse1.speak()

