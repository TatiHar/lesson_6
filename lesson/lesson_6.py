#задание 1
from time import sleep

class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        a = 0
        while a < 3:
            print(f'{TrafficLight.__color[a]}')
            if a == 0:
                sleep(7)
            elif a == 1:
                sleep(5)
            elif a == 2:
                sleep(5)
            a += 1

TrafficLight = TrafficLight()
TrafficLight.running()

#задание 2
class Road:
    def __init__(self, length, width, mass_asphalt, thickness):
        self._length = length
        self._width = width
        self._mass_asphalt = mass_asphalt
        self._thickness = thickness
    def mass(self):
        return (self._length * self._width * self._mass_asphalt * self._thickness)/ 1000
road = Road(20, 5000, 25, 5)
print(int(road.mass()))


#задание 3
class Work:
    def __init__(self, name, surname, position, wage, bonus):
        self._name = name
        self._surname = surname
        self._position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Work):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    def get_full_name(self):
        return self._name + ' ' + self._surname + ' ' + self._position
    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')
persan = Position("Tatiana", "Haritonova", "epidemiologist", 1000, 2222)

print(persan.get_full_name())
print(persan.get_total_income())

#задание 4
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return self.name
    print('Start')
    def stop(self):
        return self.name
    print('Stop')
    def turn_right(self):
        return self.name
    print('Turn')
    def show_speed(self):
        return self.name is self.speed
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed >= 40:
            print('Превышена скорость')
        else:
            print('Скорость допустимая')
class SportCar(Car):
    pass
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def selspeed(self):
        if self.speed >= 60:
            print('Превышена скорость')
        else:
            print('Скорость допустимая')
class PoliceCar(Car):
    pass

Audi = SportCar(100, 'Red', 'Audi', False)
Nissan = TownCar(150, 'Вlack', 'Nissan', False)
Lada = WorkCar(70, 'Gray', 'Lada', False)
Mercedes = PoliceCar(110, 'White',  'Ford', True)
print(Lada.show_speed())
print(Nissan.show_speed())

#задание 5
class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')
class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print('Ручку')
class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print('Карандаш')
class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print('Маркер')

pen = Pen(' ')
pencil = Pencil(' ')
handle = Handle(' ')
print('Запуск отрисовки')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
