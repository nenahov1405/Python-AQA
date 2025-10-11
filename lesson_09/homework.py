# Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
#
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
        self.diamond_side = None
        self.angle_a = None
        self.angle_b = None

        self.diamond_side = diamond_side
        self.angle_a = angle_a
        #виклик setattr для angle_b не потрібен, будем рахувати автоматично

    def __setattr__(self, key, value):
        if key == 'diamond_side':
            if value <= 0:
                raise ValueError(f'Помилка: Сторона ромба має бути > 0. Спроба встановити: {value}')
            self.diamond_side = value
        elif key == 'angle_a':
            if not 0 < value < 180:
                raise ValueError(f'Помилка: Кут А має бути в діапазоні (0, 180) градусів. Спроба встановити: {value}')
            self.angle_a = value
            self.angle_b = 180 - value
        elif key == 'angle_b':
            if not 0 < value < 180:
                raise ValueError(f'Помилка: Кут B має бути в діапазоні (0, 180) градусів. Спроба встановити: {value}')
            self.angle_b = value
            self.angle_a = 180 - value
        else:
            super().__setattr__(key, value)

    def __str__(self):
        return (f'Ромб зі стороною {self.diamond_side}, першим кутом {self.angle_a} та другим {self.angle_b}')