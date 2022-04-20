class Tomato:
    states = {1: 'маленький', 2: 'средний', 3: 'большой'}
    def __init__(self, index):
        self._index = index
        self._state = 1
    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self._state == 3:
            return True
        return False
    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()
    def _print_state(self):
        print(f'помидор {self._index} уже {Tomato.states[self._state]}')
class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])
    def give_away_all(self):
        self.tomatoes = []
class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant
    def work(self):
        print('В процессе')
        self._plant.grow_all()
        print('Выросло')

    # Собираем урожай
    def harvest(self):
        print('Собирается')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Собрано')
        else:
            print('Еще не все созрели')

    # Статический метод
    # Выводит справку по садоводству
    @staticmethod
    def knowledge_base():
        print('Почаще поливайте. Не допускайте иссыхания плодов!')
if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Васька', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()








