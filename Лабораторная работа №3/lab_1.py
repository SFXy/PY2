class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """
               :param name: Название книги
               :param author: Имя и фамилия автора
               Примеры:
               >>> Book(name="Шерлок Холмс", author='Артур Конан Дойл')
        """
        self._name = name
        self._author = author

    @property
    def name(self):
        """
               Возвращает название книги
               :return: Название книги
        """
        return self._name

    @property
    def author(self):
        """
               Возвращает автора книги
               :return: Автор книги
        """
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"



class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        """
               :param name: Название книги
               :param author: Имя и фамилия автора
               :param pages: Количество страниц
               Примеры:
               >>> Book(name="Шерлок Холмс", author='Артур Конан Дойл', pages=200)
        """
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self.pages

    @pages.setter
    def pages(self, new_pages: int):
        if not isinstance(new_pages, int) or new_pages <= 0:
            raise ValueError('Кол-во страниц должно быть больше 0 и принадлежать int')
        self.pages = new_pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Кол-во страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        """
               :param name: Название книги
               :param author: Имя и фамилия автора
               :param duration: Продолжительность
               Примеры:
               >>> Book(name="Шерлок Холмс", author='Артур Конан Дойл', duration=50)
        """
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> int:
        return self.duration

    @duration.setter
    def duration(self, new_duration: float):
        if not isinstance(new_duration, float) or new_duration <= 0:
            raise ValueError('Продолжительность должна быть больше 0 и принадлежать float')
        self.duration = new_duration

    def __str__(self):
        return f" Аудио книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


print(AudioBook('Букварь', '2kh', 2.1))