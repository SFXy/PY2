import doctest
from typing import Union
class Bed:
    def __init__(self, height: Union[int, float], width: Union[int, float], colour: str):
        """
                Создание и подготовка к работе объекта "Кровать"
                :param height: Высота кровати (в мм)
                :param width: Ширина кровати (в мм)

                Примеры:
                >>> bed = Bed(550, 225, 'Белая')  # инициализация экземпляра класса
                """
        if not isinstance(height and width, (int, float)):
            raise TypeError("Параметр размера должен быть типа int")
        if height and width < 0:
            raise ValueError("Параметр размера должен быть положительным числом")
        self.height = height
        self.width = width
        if not isinstance(colour, str):
            raise TypeError("Параметр цвета должен быть типа str")
        self.colour = colour

    def size_increase(self, add_width: Union[int, float], add_height: Union[int, float]):
        """
                Функция, которая позволяет увеличить параметры размера кровати
                :param add_width: Увеличивает ширину на желаемое число (в мм)
                :param add_height: Увеличивает высоту на желаемое число (в мм)
                :raise ValueError: Если после добавления размера итоговые
                                   значения не сходятся с ГОСТом, то вызваем ошибку

                Примеры:
                >>> bed = Bed(1000, 2000, 'Gray')
                >>> bed.size_increase(120, 240)
        """
        if not isinstance(add_width and add_height, (int, float)):
            raise TypeError("Параметр размера должен быть типа int")
        if add_width and add_height < 0:
            raise ValueError("Параметр размера должен быть положительным числом")
        ...

    def price(self, width, height):
        """
                Функция, которая зависимости от ширины и высоты кровати выводит ее цену
                :param height: Высота кровати (в мм)
                :param width: Ширина кровати (в мм)
                :return: Цена кровати

                Примеры:
                >>> bed = Bed(1000, 2000, 'Gray')
                >>> bed.price(1000, 2000)
        """
        if not isinstance(width and height, (int, float)):
            raise TypeError("Параметр размера должен быть типа int")
        if width and height < 0:
            raise ValueError("Параметр размера должен быть положительным числом")
        ...

class Building:
    def __init__(self, population: Union[int, float], terrain_type: str):
        """
                Создание и подготовка к работе объекта "Здание"
                :param population: Количество человек в здании
                :param terrain_type: Тип местности, в которой находится здание
                Примеры:
                >>> building = Building(750, 'C')  # инициализация экземпляра класса
                """
        if not isinstance(population, (int, float)):
            raise TypeError("Кол-во людей в здании должно быть типа int")
        if population < 0:
            raise ValueError("Параметр должен быть положительным числом")
        self.population = population
        if not isinstance(terrain_type, str):
            raise TypeError("Тип местности должены быть типа str")
        self.terraint = terrain_type
        ...

    def b_type(self, num_floors):
        """
                Функция, которая определяет классификацию здания по кол-ву этажей
                :param num_floors: Количество этажей в здании
                :return: Класс здания по кол-ву этажей

                Примеры:
                >>> building = Building(750, 'C')
                >>> building.b_type(23)
        """
        if not isinstance(num_floors, (int, float)):
            raise TypeError("Кол-во этажей в здании должно быть типа int")
        if num_floors <= 0:
            raise ValueError("Параметр должен быть положительным числом и не равен нулю")

        if num_floors <= 3: return 'Малоэтажное здание'
        elif 3 < num_floors <= 5: return 'Среднеэтажное здание'
        elif 5 < num_floors <= 10: return 'Здание повышенной этажности'
        elif 10 < num_floors: return 'Многоэтажное здание'

    def new_population(self, add_population):
        """
               Метод увеличивает кол-во людей в здании.
               :param add_population: Количество новых людей
               :raise ValueError: Если после добавления итоговое значение людей
                                   не разшается ГОСТом, то вызваем ошибку

                Примеры:
                >>> building = Building(750, 'C')
                >>> building.new_population(35)
               """
        if not isinstance(add_population, (int, float)):
            raise TypeError("Кол-во этажей в здании должно быть типа int")
        if add_population < 0:
            raise ValueError("Параметр должен быть положительным числом")
        self.population += add_population

class Shirt:
    def __init__(self, size: str, colour: str):
        """
                Создание и подготовка к работе объекта "Рубашка"
                :param size: Название размера
                :param colour: Цвет

                Примеры:
                >>> shirt = Shirt('S', 'White')  # инициализация экземпляра класса
                """
        if not isinstance(size and colour, str):
            raise TypeError("Размер рубашки и цвет должен быть типа str")
        self.size = size
        self.colour = colour
        ...

    def from_size_to_chest(self, size):
        """
                Функция, которая выводит предполагаемый обхват груди для введенного размера
                :param size: Название размера
                :return: Обхват груди

                Примеры:
                >>> shirt = Shirt('S', 'Blue')
                >>> shirt.from_size_to_chest('M')
                """
        size_by_chest_dic = {'S': 86, 'M': 90, 'L': 94, 'XL': 98}
        if size not in size_by_chest_dic:
            raise TypeError("Формат размера некорректный")
        return size_by_chest_dic[size]

    def size_format(self, size: str, format: str):
        """
                Функция, котрорая переводит данный размер в необходимый формат (например, в азиатский)
                :param size: Название размера
                :param format: Название формата
                :return: Формат размера

                Примеры:
                >>> shirt = Shirt('S', 'Blue')
                >>> shirt.size_format('S', 'Asian')
                """
        if not isinstance(size and format, str):
            raise TypeError("Размер рубашки и формат должен быть типа str")
        ...

if __name__ == "__main__":
    doctest.testmod()
    pass
