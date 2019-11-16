class Dog:


    def __init__(self, weight=15, height=67):
        self.weight=weight
        self.height=height

    def voice(self):
        print('Gaaf')
    

class Cat:

    def __init__(self, weight=10, height=37):
        self.weight=weight
        self.height=height

    def voice(self):
        print('Mew')


if __name__ =='__main__':
    dog = Dog()
    cat = Cat()

    dog.voice()
    cat.voice()
