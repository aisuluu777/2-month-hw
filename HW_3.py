class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__cpu + self.__memory

    def __str__(self):
        return f'Computer`s cpu: {self.__cpu}, memory: {self.__memory}'

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory!= other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory



class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards = value

    def call(self, sim_cards_number, call_to_number):
        return f'Идет звонок с номера {call_to_number}, с сим карты {sim_cards_number}'

    def __str__(self):
        return f'Phone`s sim_cards_list: {self.__sim_cards}'

class SmartPhone(Phone,Computer):
    def __init__(self, sim_cards_list,cpu, memory):
        Phone.__init__(self, sim_cards_list)
        Computer.__init__(self, cpu, memory)

    def use_gps(self,location):
        return f'Ваш маршрут был построен с вашего местоположения к {location}'
    def __str__(self):
        return f'Smartphones`s sim_cards_list: {self.sim_cards_list}, cpu: {self.cpu}, memory: {self.memory}'



computer_1 =Computer(7,256)
phone_1 = Phone(['Beeline','O'])
smart_phone_1 = SmartPhone(['Mega', 'O'],8, 512)
smart_phone_2 = SmartPhone(['Beeline','Mega'],6, 256)

gadjedts = [computer_1,phone_1,smart_phone_1,smart_phone_2]
for char in gadjedts:
    print(char)

print(f'сумма cpu и memory: {computer_1.make_computations()}')
print(phone_1.call(1,999764523))
print(smart_phone_1.use_gps('Ала-Тоо'))
print(f'Память 1 смартфона больше чем у 2-го: {smart_phone_1 > smart_phone_2}')
print(f'Память 1 смартфона меньше чем у 2-го: {smart_phone_1 < smart_phone_2}')
print(f'Память 1 смартфона не равно 2 смартфону: {smart_phone_1 != smart_phone_2}')
print(f'Память 1 смартфона равно 2 смартфону: {smart_phone_1 == smart_phone_2}')
print(f'Память 1 смартфона равно или больше чем у 2-го: {smart_phone_1 >= smart_phone_2}')
print(f'Память 1 смартфона равно или меньше чем у 2-го: {smart_phone_1 <= smart_phone_2}')