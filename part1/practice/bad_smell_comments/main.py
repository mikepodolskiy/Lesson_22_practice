# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


fly_coeff = 1.2
crawl_coeff = 0.5


class Unit:

    def move_object(self, field, x_coord, y_coord, direction, is_fly: bool, is_crawl: bool, base_speed=1):

        if is_fly and is_crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed = base_speed * 1.2
            if direction == 'UP':
                new_y = y_coord + speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - speed
            elif direction == 'RIGHT':
                new_y = y_coord
                new_x = x_coord + speed
            else:
                raise ValueError('Неизвестное направление')
        elif is_crawl:
            speed = base_speed * crawl_coeff
            if direction == 'UP':
                new_y = y_coord + speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - speed
            elif direction == 'RIGHT':
                new_y = y_coord
                new_x = x_coord + speed
            else:
                raise ValueError('Неизвестное направление')

        else:
            raise ValueError('Неизвестное состояние')

        field.set_unit(x=new_x, y=new_y, unit=self)
