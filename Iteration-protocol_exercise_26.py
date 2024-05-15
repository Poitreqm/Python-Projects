#
# создайте класс Fibs, реализующий протокол итерации. Следующий код должен работать с вашим классом:
#
# fibs = Fibs()
#   for f in fibs:
#      if f > 1000:
#         print(f)
#         break
#


class Fibs:
    def __init__(self):
        self.data = range(2000)

    def __iter__(self):
        return iter(self.data)

    # или return iter(range(2000)) еслии хотим без __init__


fibs = Fibs()
for f in fibs:
    if f > 1000:
        print(f)
        break
