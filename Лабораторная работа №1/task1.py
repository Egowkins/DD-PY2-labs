# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union


class Paper:
    def __init__(self, height: Union[int, float], width:Union[int, float],
                 density: Union[int, float]):
        """
        Создание объекта бумага
        :param height: длина бумаги
        :param width: ширина бумаги
        :param density: плотность бумаги
        :raise: TypeError: Если длина бумаги не принадлежит типу int или float
        :raise: ValueError: Если Длина бумаги меньше нуля
        :raise: TypeError: Если Ширина бумаги не принадлежит типу int или float
        :raise: ValueError: Если ширина бумаги меньше нуля
        :raise: TypeError: Если плотность бумаги не принадлежит типу int или float
        :raise: ValueError: Если плотность бумаги меньше нуля
        """

        if not isinstance(height, (int, float)):
            raise TypeError("Длина бумаги может быть типа int или float")
        if height <= 0:
            raise ValueError("Длина бумаги должна быть положительным числом, больше нуля")
        self.height = height
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина бумаги может быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина бумаги должна быть положительным числом, больше нуля")
        self.width = width
        if not isinstance(density, (int, float)):
            raise TypeError("Плотность бумаги может быть типа int или float")
        if density <= 0:
            raise ValueError("Плотность бумаги должна быть положительным числом, больше 0")
        self.density = density

    def folding_paper_in_half(self, count: int):
        """
        Сложить бумагу попалам count раз
        :param count: количество складываний бумаги попалам
        Пример: paper1 = Paper(200,100,100)
                paper1.folding_paper_in_half(3)

        """
        if not isinstance(count, (int, float)):
            raise TypeError("Количество сгибов может быть типа int или float")
        if count <= 0:
            raise ValueError("Количество сгибов должно быть положительным числом, больше 0")
        ...

    def number_of_chars(self,char_square: Union[int, float]):
        """
        Количество символов, вмещаемых на лист
        :param char_square:
        Пример:paper1 = Paper(200,100,100)
               paper1.number_of_chars(12)
        """
        ...


class Burger:
    def __init__(self, kkal:Union[int, float], fats:Union[int, float],
                 proteins:Union[int, float]):
        """
        Создание объекта бургер
        :param kkal: Энергетическая ценность бургера
        :param fats: Количество жиров
        :param proteins: Количество белков
        :raise: TypeError: Если энерг. ценность не принадлежит типу int или float
        :raise: ValueError: Еслиэнерг. ценность  меньше нуля
        :raise: TypeError: Если количество жиров не принадлежит типу int или float
        :raise: ValueError: Если количество жиров меньше нуля
        :raise: TypeError: Если количество белков не принадлежит типу int или float
        :raise: ValueError: Если количество белков меньше нуля
        """
        if not isinstance(kkal, (int, float)):
            raise TypeError("Энергетическая ценность бургера может быть типа int или float")
        if kkal <= 0:
            raise ValueError("Энергетическая ценность бургера должна быть положительным числом, больше нуля")
        self.kkal = kkal
        if not isinstance(fats, (int, float)):
            raise TypeError("Количество жиров в бургере может быть типа int или float")
        if fats <= 0:
            raise ValueError("Количество жиров в бургере должно быть положительным числом, больше нуля")
        self.height = fats
        if not isinstance(proteins, (int, float)):
            raise TypeError("Количество протеинов в бургере может быть типа int или float")
        if proteins <= 0:
            raise ValueError("Количество протеинов в бургере должно быть положительным числом, больше нуля")
        self.proteins = proteins

    def adding_cutlets(self, num_of_cutlets: int, max_amount = 5):
        """
        Добавление котлет в бургер
        :param num_of_cutlets: количество добавленных котлет
        Пример: burger1 = Burger(500, 70, 20)
                burger1.adding_cutlets(2)
        """
        if not isinstance(num_of_cutlets, int):
            raise TypeError("Количество котлет может быть типа int ")
        if num_of_cutlets <= 0 or num_of_cutlets > max_amount:
            raise ValueError("Количество котлет должно быть положительным числом, больше нуля, и не больше, чем максимально возможное количество")
        ...


class School:
    def __init__(self, number:int, n_students:int, name: str):
        """
        Создание объекта школа
        :param number: номер школы
        :param n_students: количество учеников
        :param name: имя школы
        :raise: TypeError: Если номер школы не принадлежит типу int
        :raise: ValueError: Номер школы меньше нуля или равен нулю
        :raise: TypeError: Если количество учеников не принадлежит типу int
        :raise: ValueError: Если количество учеников меньше нуля или равно нулю.
        :raise: TypeError: Если название школы не принадлежит типу str

        """
        if not isinstance(number, int):
            raise TypeError("Номер школы может быть типа int")
        if number <= 0:
            raise ValueError("Номер школы должен быть положительным числом, больше нуля")
        self.number = number
        if not isinstance(n_students, int):
            raise TypeError("Количество учеников может быть только типа int ")
        if n_students <= 15:
            raise ValueError("Количество учеников должно быть положительным числом, больше 15")
        self.n_students = n_students
        if not isinstance(name, str):
            raise TypeError("Имя школы может быть только типа str")
        self.name = name

    def new_director(self, director_name:str):
        """
        Назначение нового директора школы
        :param director_name: Имя директора
        Пример: school1 = School(1, 1000, 'Имени А.С.Пушкина')
                school1.new_director('А.А. Иванов')
        """
        if not isinstance(director_name, str):
            raise TypeError("Имя директора может быть только типа str")
        ...

    def school_renovation_time(self, mounth: int):
        """
        Время, затраченное на ремонт школы
        :param mounth: Количество месяцев
        Пример: school1 = School(1, 1000, 'Имени А.С.Пушкина')
                school1.school_renovation_time(10)
        """
        if not isinstance(mounth, int):
            raise TypeError("Количество месяцев может быть типа int")
        if mounth <= 0:
            raise ValueError("Количество месяцев должны быть положительным числом, больше нуля")
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
