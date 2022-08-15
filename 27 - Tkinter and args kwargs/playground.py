def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)


# add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


# calculate(3, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.colour = kwargs.get('colour')
        self.seats = kwargs.get('seats')


car = Car(make='Jaguar', model='E-Pace')
car1 = Car(model='Spyder')
car2 = Car()
print(car.make)
print(car.model)
print(car1.make)
print(car1.model)

