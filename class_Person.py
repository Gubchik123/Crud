from uuid import uuid4


class Person:
    def __init__(self):
        self.__name = self.__surname = self.__nik = self.__id = ""
        self.__age = self.__numberOfComp = self.__number = 0

    def enter_name(self):
        self.__name = input("Введите имя: ")

    def enter_surname(self):
        self.__surname = input("Введите фамилию: ")

    def enter_age(self):
        self.__age = int(input("Введите возраст: "))

    def enter_nik(self):
        self.__nik = input("Введите никнейм: ")

    def enter_number_of_comp(self):
        self.__numberOfComp = input("Введите номер компьютера: ")

    @property  # Getter for student's nik
    def nik(self): return self.__nik

    @property  # Getter for student's number
    def number(self): return self.__number

    @number.setter  # Setter for student's number
    def number(self, num): self.__number = num

    def id_generation(self): self.__id = uuid4()

    def __str__(self):
        return f"{self.__number}. {self.__surname} {self.__name}"

    def print_info(self):
        print("--- Информация о студенте ---".center(40))
        print(f"Номер: {self.__number}")
        print(f"Имя: {self.__name}")
        print(f"Фамилия: {self.__surname}")
        print(f"Возраст: {self.__age}")
        print(f"Никнейм: {self.__nik}")
        print(f"Номер компьютера: {self.__numberOfComp}")
        print(f"ID: {self.__id}")
