class Animal(object):
    def run(self):
        print('Animal is running ...')


class Dog(Animal):
    def run(self):
        print('Dog is running ...')


class Cat(Animal):
    def run(self):
        print('Cat is running ...')


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly ...')


class Timer(object):
    def run(self):
        print('Start ...')


def run_twice(animal):
    animal.run()
    animal.run()


def main():
    animal = Animal()
    animal.run()

    dog = Dog()
    dog.run()

    cat = Cat()
    cat.run()

    run_twice(Animal())
    run_twice(Dog())
    run_twice(Tortoise())
    run_twice(Timer())


if __name__ == '__main__':
    main()
