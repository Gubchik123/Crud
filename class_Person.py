from uuid import uuid4


class Person:
    def __init__(self):
        self.__name = self.__surname = self.__nik = self.__id = ""
        self.__age = self.__numberOfComp = 0

    def __str__(self):
        return f"{self.__surname} {self.__name}"

    @property  # Getter for person's name
    def name(self): return self.__name

    @name.setter  # Setter for person's name
    def name(self, item): self.__name = item

    @property  # Getter for person's surname
    def surname(self): return self.__surname

    @surname.setter  # Setter for person's surname
    def surname(self, item): self.__surname = item

    @property  # Getter for person's nik
    def nik(self): return self.__nik

    @nik.setter  # Setter for person's nik
    def nik(self, item): self.nik = item

    @property  # Getter for person's age
    def age(self): return self.__age

    @age.setter  # Setter for person's age
    def age(self, item): self.__age = item

    @property  # Getter for person's number of computer
    def num_of_comp(self): return self.__numberOfComp

    @num_of_comp.setter  # Setter for person's number of computer
    def num_of_comp(self, item): self.__numberOfComp = item

    @property  # Getter for person's id
    def id(self): return self.__id

    def id_generation(self): self.__id = uuid4()
