from typing import Union
# TODO Написать 3 класса с документацией и аннотацией типов
    # TODO работоспособность экземпляров класса проверить с помощью doctest

class Glass:
    def __init__(
        self,
        capacity_volume: Union[int, float],
        occupied_volume: Union[int, float],
    ) -> None:
        self.capacity_volume = None
        self.occupied_volume = None

        self.init_capacity_volume(capacity_volume)
        self.init_occupied_volume(occupied_volume)

    def init_capacity_volume(self, capacity_volume: Union[int, float]) -> None:
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if capacity_volume <= 0:
            raise ValueError
        self.capacity_volume = capacity_volume

    def init_occupied_volume(self, occupied_volume: Union[int, float]) -> None:
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        if occupied_volume > self.capacity_volume:
            raise ValueError
        self.occupied_volume = occupied_volume

if __name__ == "__main__":
    glass1 = Glass(200, 100)
    glass2 = Glass(300, 50)
    glass2.occupied_volume += 100
    print(glass1.capacity_volume, glass1.occupied_volume)
    print(glass2.capacity_volume, glass2.occupied_volume)
    print(glass1 is glass2)