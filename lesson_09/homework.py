# Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
# сторона_а (довжина сторони a).
# кут_а (кут між сторонами a і b).
# кут_б (суміжний з кутом кут_а).
# Необхідно реалізувати наступні вимоги:
#
# Значення сторони сторона_а повинно бути більше 0.
# Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
# Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а,
# значення кут_б обчислюється автоматично.
# Для встановлення значень атрибутів використовуйте метод __setattr__.

class Diamond():

    def __init__(self, diamond_side, angle_a, angle_b):

        self.diamond_side = diamond_side
        self.angle_a = angle_a
        #виклик setattr для angle_b не потрібен, будем рахувати автоматично

    def __str__(self):
        return f"Створено ромб зі стороною: {self.diamond_side},\nкутом А: {self.angle_a},\nкутом В: {self.angle_b}"

    def __setattr__(self, key, value):
        if key == "diamond_side":
            if value <= 0:
                print(f"Спроба створити ромб з невалідною стороною = {value}")
            else:
                super().__setattr__(key, value)
        elif key == "angle_a":
            if 180 > value > 0:
                super().__setattr__('angle_a', value)
                super().__setattr__('angle_b', 180 - value)
            else:
                print(f"Спроба створити ромб з невалідним значенням кута А = {value}")
        elif key == "angle_b":
            super().__setattr__(key, value)
        else:
            super().__setattr__(key, value)

r = Diamond(1, 2, 3)
print(r)