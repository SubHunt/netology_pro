class FlatIterator:
    """Итератор получает на вход список с вложенными списками на выдает поочередно все элементы списков"""

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.outer_cursor = 0
        self.inner_cursor = -1
        return self

    def __next__(self):
        self.inner_cursor += 1
        if self.inner_cursor == len(self.list_of_list[self.outer_cursor]):
            self.inner_cursor = 0
            self.outer_cursor +=1
        if self.outer_cursor == len (self.list_of_list):
            raise StopIteration
        return self.list_of_list[self.outer_cursor][self.inner_cursor]


def test_1():
    """ Функция отправляет в итератор список с вложенными списками, на выходе при использовании list получаем один список
        со всеми эелемнтами
    """
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]): 
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

if __name__ == '__main__':
    test_1()