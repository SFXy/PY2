if __name__ == "__main__":
    # Write your solution here
    pass

class Work_Space:
    """ Базовый класс рабочего пространства. """

    def __init__(self, name: str, area: float, users: int, height: float):
        """
               :param name: Название рабочего пространства
               :param users: Кол-во пользователей
               :param area: Площадь пространства (в метрах квадратных)
               :param height: Высота этажа (в метрах)
               Примеры:
               >>> Work_Space(name="Точка Кипения",area=123.4,users=123,height=3.0)
        """
        self._name = name
        self._area = area
        self._users = users
        self._height = 3.0  # в большенстве случаев высота этажа равна трем метрам

    @property
    def name(self):
        """
               Возвращает название рабочего пространства
               :return: Название рабочего пространства
        """
        return self._users

    @property
    def users(self):
        """
               Возвращает кол-во пользователей
               :return: Кол-во пользователей
        """
        return self._users

    @property
    def area(self):
        """
               Возвращает площадь пространства
               :return: Площадь пространства
        """
        return self._area

    @property
    def height(self):
        """
               Возвращает высоту этажа
               :return: Высота этажа
        """
        return self._height

    @height.setter
    def height(self, new_height):
        """
               Устанавливает высоту этажа
        """
        if not isinstance(new_height, float):
            raise TypeError("Высота этажа должна быть типа float")
        if new_height <= 0:
            raise ValueError("Высота этажа должна быть положительным числом")
        self._height = new_height

    def __str__(self):
        return f"Рабочее пространство с кол-вом пользователей {self._users}. Площадь {self._area}" \
               f"Высота этажа {self._height}"

    def __repr__(self):
        return f"{self.__class__.__name__}(users={self._users!r}, area={self._area!r}, height={self._height!r})"

class Coworking(Work_Space):
    def __init__(self, name: str, area: float,users: int, style: int):
        """
               :param name: Название рабочего пространства
               :param area: Площадь пространства (в метрах квадратных)
               :param style: Стиль дизайна интерьера
               :param users: Кол-во пользователей

               Примеры:
               >>> Work_Space(name="Точка Кипения",area=123.4,style="modern", users=123)
        """
        super().__init__(name, area, users)
        self.style = style

    def count_users(self, area):
    """
           Метод считает кол-во пользователей в зависимоти от площади по СНиПам
           :return: Кол-во пользователей
    """
    ...

    @property
    def name(self):
        """
               Возвращает название рабочего пространства
               :return: Название рабочего пространства
        """
        return self._users

    @property
    def users(self):
        """
               Возвращает кол-во пользователей
               :return: Кол-во пользователей
        """
        return self._users

    @property
    def area(self):
        """
               Возвращает площадь пространства
               :return: Площадь пространства
        """
        return self._area


    def __str__(self):
        return f"Рабочее пространство  {self._name} с кол-вом пользователей {self._users}." \
               f"Стиль {self._height}"


    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, users={self._users!r}, area={self._area!r}, style={self._style!r})"

if __name__ == "__main__":
    # Write your solution here
    office = Coworking("Точка Кипения", 123.4, "modern", 123)
    print(office)
    pass





