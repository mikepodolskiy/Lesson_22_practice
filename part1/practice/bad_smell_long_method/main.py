# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list(substring, reverse: bool = False):
    data = _read_data(substring)
    return _process_data(data, reverse)


def _read_data(substring):
    return [data.split(";") for data in substring.split('\n')]


def _process_data(data, reverse):
    return sorted([item for item in data if int(item[1]) >= 10], reverse=reverse)


if __name__ == '__main__':
    print(get_users_list(csv))
