class Animal:

    def __init__(self, weight=15, height=67):
        self.weight=weight
        self.height=height

class Dog(Animal):


    def voice(self):
        print(f'dog says GAAF... its height is {self.height} and weight is {self.weight}', )
    

class Cat(Animal):


    def voice(self):
        print(f'cat says MEW... its height is {self.height} and weight is {self.weight}')


if __name__ =='__main__':
    dog = Dog()
    cat = Cat(weight=12,height=34)

    dog.voice()
    cat.voice()
