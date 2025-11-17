#Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

class PairIterator:
    def __init__(self, n):
        self._n = n
        self._current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current > self._n:
            raise StopIteration
        else:
            result = self._current
            self._current += 2
            return result

N = 100
pairs = PairIterator(N)
for item in pairs:
    print(item)

