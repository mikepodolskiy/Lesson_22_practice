# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)

base_speed = 1
fly_coeff = 1.2
crawl_coeff = 0.5

class Unit:
    def __init__(self, state: str, start_field: list, direction):
        self.state = state
        self.start_field = start_field
        self.direction = direction

    def _get_speed(self):
        if self.state == 'fly':
            self.speed = base_speed * fly_coeff
        elif self.state == 'crawl':
            self.speed = base_speed * crawl_coeff
        else:
            raise ValueError('unknown state')
        return self.speed

    def move(self):
        speed = self._get_speed()
        if self.direction == 'up':
            new_x = self.start_field[0]
            new_y = self.start_field[1] + speed
        elif self.direction == 'down':
            new_x = self.start_field[0]
            new_y = self.start_field[1] - speed
        elif self.direction == 'right':
            new_x = self.start_field[0] + speed
            new_y = self.start_field[1]
        elif self.direction == 'left':
            new_x = self.start_field[0] - speed
            new_y = self.start_field[1]

        else:
            raise ValueError('wrong direction')

        return [new_x, new_y]
