# В классе {{Moped}}напишите статическую функцию, которая на вход будет принимать расстояние и максимальную скорость, а на выходе получать время, за которое проедет мопед это расстояни

class MeansOfTransport:
    def init(self, brand, color):
        self._brand = brand
        self._color = color

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    def show_color(self):
        print(f"цвет машины: {self._color}")

    def show_brand(self):
        print(f"марка машины: {self._brand}")


class Car(MeansOfTransport):
    def init(self, brand, color, wheel_count):
        super().init(brand, color)
        self._wheel_count = wheel_count

    @property
    def wheel_count(self):
        return self._wheel_count

    @wheel_count.setter
    def wheel_count(self, value):
        self._wheel_count = value


class Moped(MeansOfTransport):
    def init(self, brand, color, wheel_count):
        super().init(brand, color)
        self._wheel_count = wheel_count

    @property
    def wheel_count(self):
        return self._wheel_count

    @wheel_count.setter
    def wheel_count(self, value):
        self._wheel_count = value

    @staticmethod
    def calculate_time(distance, max_speed):

        if distance <= 0 or max_speed <= 0:
            raise ValueError("путь и скорость более 0.")

        time = distance / max_speed
        return time


# moped = Moped()
# travel_time = Moped.calculate_time(100, 50)
# print(f"время в пути для мопеда: {travel_time} час")