class Vehicle:
    """
    Базовый класс для транспортных средств.
    Атрибуты:
        brand (str): Марка транспортного средства.
        model (str): Модель транспортного средства.
        year (int): Год выпуска.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализирует объект транспортного средства.
        Args:
            brand (str): Марка.
            model (str): Модель.
            year (int): Год выпуска.
        """
        self.brand = brand
        self.model = model
        self.year = year

    def move(self) -> str:
        """
        Описывает общее движение транспортного средства.
        Returns:
            str: Сообщение о движении.
        """
        return f"{self.brand} {self.model} движется по дороге."

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта для пользователя.
        Returns:
            str: Удобочитаемая строка.
        """
        return f"Транспорт: {self.brand} {self.model}, {self.year} года выпуска"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта.
        Returns:
            str: Строка для разработчика.
        """
        return f"Vehicle(brand='{self.brand}', model='{self.model}', year={self.year})"

class Car(Vehicle):
    """
    Дочерний класс легкового автомобиля.
    Дополнительные атрибуты:
        doors (int): Количество дверей.
    """

    def __init__(self, brand: str, model: str, year: int, doors: int) -> None:
        """
        Инициализирует объект автомобиля.
        Args:
            brand (str): Марка.
            model (str): Модель.
            year (int): Год выпуска.
            doors (int): Количество дверей.
        """
        super().__init__(brand, model, year)
        self.doors = doors

    def move(self) -> str:
        """
        Переопределенный метод движения для автомобиля.
        Returns:
            str: Сообщение о движении автомобиля.
        """
        return f"Автомобиль {self.brand} {self.model} едет по трассе."

    def open_trunk(self) -> str:
        """
        Дополнительный метод дочернего класса.
        Returns:
            str: Сообщение об открытии багажника.
        """
        return f"У автомобиля {self.brand} {self.model} открыт багажник."

if __name__ == "__main__":
    vehicle = Vehicle("Mercedes", "Sprinter", 2020)
    car = Car("Toyota", "Camry", 2022, 4)

    print(vehicle)
    print(repr(vehicle))
    print(vehicle.move())

    print()

    print(car)
    print(repr(car))
    print(car.move())
    print(car.open_trunk())
