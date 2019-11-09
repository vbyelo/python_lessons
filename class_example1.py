class Dog:


    def __init__(self):
        pass

    def voice(self):
        print('Gaaf')
    

class Cat:

    def voice(self):
        print('Mew')


if __name__ =='__main__':
    dog = Dog()
    cat = Cat()

    dog.voice()
    cat.voice()
