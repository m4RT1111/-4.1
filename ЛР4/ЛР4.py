class Task:  # класс задания
    def __init__(self, name: str, reward: int):
        self.name = name        # имя задания
        self.reward = reward        # награда за задание
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        if not isinstance(new_name, str):
            raise TypeError('Имя должно быть типа str')
        self._name = new_name

    # конвертация награды в золото
    def convert_to_gold(self):
        return self.reward * 100

    def __str__(self):
        return f'Задание "{self._name}". Награда - {self.reward}'

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self._name!r}, reward={self.reward!r})'


class Dungeon(Task):  # класс подземелья
    def __init__(self, name: str, difficult: str, reward: int):
        super().__init__(name, reward)
        super.__str__(name)
        super().convert_to_gold()
        self.difficult = difficult      # сложность подземелья

    @property
    def difficult(self):
        return self._difficult

    @difficult.setter
    def difficult(self, new_diff):
        if not isinstance(new_diff, str):
            raise TypeError('Сложность задания должна типа str')
        if new_diff not in ['Легкая', 'Средняя', 'Сложная']:
            raise ValueError('Сложность не является существующей')
        self._difficult = new_diff

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, difficult={self._difficult!r})'

    # изменить награду в зависимости от сложности

    def add_reward(self):
        if self._difficult == 'Средняя':
            return self.reward * 1.2
        if self._difficult == 'Сложная':
            return self.reward * 1.5


if __name__ == "__main__":
    task = Task('Принести припасы', 100)
    dungeon = Dungeon('Обследовать замок Дракона', 'Сложная', 580)

    print(task)
    print(task.convert_to_gold())
    print(dungeon)
    print(dungeon.convert_to_gold())
    print(dungeon.__repr__())
