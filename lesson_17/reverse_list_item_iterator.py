#Реалізуйте ітератор для зворотного виведення елементів списку.
#Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

class MyList:
    def __init__(self, list_data):
        self._list_data = list_data
        self._index= len(list_data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= 0:
            item = self._list_data[self._index]
            self._index -= 1
            return item
        else:
            raise StopIteration

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
reverse_iter = MyList(lst)
for item in reverse_iter:
    print(item)