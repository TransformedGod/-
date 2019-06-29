# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(self.name, "поехала")
    def stop(self):
        print(self.name, "остановилась")
    def turn(self, direction):
        print(f'{self.name} повернула {direction}')


class SportCar:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(self.name, "поехала")
    def stop(self):
        print(self.name, "остановилась")
    def turn(self, direction):
        print(f'{self.name} повернула {direction}')


class WorkCar:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(self.name, "поехала")
    def stop(self):
        print(self.name, "остановилась")
    def turn(self, direction):
        print(f'{self.name} повернула {direction}')


class PoliceCar:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True

    def go(self):
        print(self.name, "поехала")
    def stop(self):
        print(self.name, "остановилась")
    def turn(self, direction):
        print(f'{self.name} повернула {direction}')


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(self.name, "поехала")
    def stop(self):
        print(self.name, "остановилась")
    def turn(self, direction):
        print(f'{self.name} повернула {direction}')


class PoliceCar(Car):
    pass

class PoliceCar(Car):
    pass

class WorkCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True




