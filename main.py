import pickle  # For working with file
import os      # For checking file size

from class_Person import Person  # My class
from time import sleep           # For waiting
from os import system as sys     # For clearing console


# Function for asking user about his\her wanting to continue
def start():
    print("--- Crud-приложение ---".center(40))
    answer = input("Войти в систему? (Да или нет)\nВаш выбор: ")
    sys("cls")  # Clear console
    if answer.lower() == "да":
        file_stats = os.stat("students.txt")
        if file_stats.st_size == 0:
            pass
        else:
            reading_from_file()
        menu()
    elif answer.lower() == "нет":
        print_bye()
    else:
        print("Такого варианта ответа нет!")
        print_bye()


# Function for choosing future actions
def menu():
    while True:
        print("--- Меню ---".center(40))
        print("1 - Показать список студентов")
        print("2 - Добавить студента в группу")
        print("3 - Удалить студента(ов) из группы")
        print("0 - Выйти")
        answer = try_input("Ваш выбор: ")

        if answer == 1:
            show_list_of_students()
        elif answer == 2:
            add_students()
        elif answer == 3:
            del_students()
        elif answer == 0:
            writing_in_file()
            print_bye()
            break
        else:
            there_is_no_such_type_of_answer()


# Function for showing students list
def show_list_of_students():
    while True:
        if len(STUDENTS) == 0:
            list_is_empty()
            break

        students_list()
        print("\n1 - Посмотреть детальную информацию")
        print("2 - Изменить детальную информацию")
        print("0 - Вернуться назад")
        answer = try_input("Ваш выбор: ")

        if answer == 1:
            info_about_student()
        elif answer == 2:
            change_info_about_student()
        elif answer == 0:
            break
        else:
            there_is_no_such_type_of_answer()


# Function for showing information about some student
def info_about_student():
    students_list()
    answer = try_input("\nВведите номер студента, про которого хотите увидеть информацию: ")

    if answer < 1 or answer > len(STUDENTS):
        there_is_no_such_student_num()
    else:
        while True:
            for stud in STUDENTS:
                if stud.number == answer:
                    stud.print_info()

            print("\n0 - Вернуться назад")
            answer = try_input("Ваш выбор: ")

            if answer == 0:
                break
            else:
                there_is_no_such_type_of_answer()


# Function for changing some information about student
def change_info_about_student():
    students_list()
    answer = try_input("\nВведите номер студента, про которого хотите поменять информацию: ")

    if answer < 1 or answer > len(STUDENTS):
        there_is_no_such_student_num()
    else:
        while True:
            print("--- Изменение информации ---".center(40))
            print("Что вы хотите поменять?")
            print("1 - Поменять имя")
            print("2 - Поменять фамилию")
            print("3 - Поменять возраст")
            print("4 - Поменять никнейм")
            print("5 - Поменять номер компьютера")
            print("0 - Вернуться назад")
            choice = try_input("Ваш выбор: ")

            if choice == 0:
                break
            elif choice < 0 or choice > 5:
                there_is_no_such_type_of_answer()
            else:
                print("--- Изменение информации ---".center(40))
                for stud in STUDENTS:
                    if stud.number == answer:
                        if choice == 1:
                            stud.enter_name()
                        elif choice == 2:
                            stud.enter_surname()
                        elif choice == 3:
                            stud.enter_age()
                        elif choice == 4:
                            stud.enter_nik()
                        else:
                            stud.enter_number_of_comp()
                wait_and_clear()


# Function for adding student(s)
def add_students():
    print("--- Добавление студента(ов) ---".center(40))
    count = try_input("Введите сколько студентов хотите добавить: ")
    if count < 1:
        print("\n")
        print("Не коректный ответ для указания количества студентов!".center(55))
        wait_and_clear()
    else:
        for i in range(count):
            print(f"--- Студент №{i + 1} ---".center(40))
            global PERSON
            PERSON = Person()
            PERSON.number = i + 1
            PERSON.enter_name()
            PERSON.enter_surname()
            PERSON.enter_age()
            PERSON.enter_nik()
            PERSON.enter_number_of_comp()
            PERSON.id_generation()

            STUDENTS.append(PERSON)

        wait_and_clear()


# Function for deleting student(s)
def del_students():
    while True:
        if len(STUDENTS) == 0:
            list_is_empty()
            break
        print("--- Удаление студента(ов) ---".center(40))
        print("1 - Удалить одного студента")
        print("2 - Удалить всех студентов")
        answer = try_input("Ваш выбор: ")

        if answer == 1:
            students_list()
            answer = try_input("\nВведите номер студента, которого хотите удалить: ")

            if answer < 1 or answer > len(STUDENTS):
                there_is_no_such_student_num()
            else:
                choice = input("Вы действительно хотите удалить этого студента? (Да или нет)\nВаш выбор: ")
                sys("cls")
                if choice.lower() == "да":
                    for stud in STUDENTS:
                        if stud.number == answer:
                            STUDENTS.remove(stud)
                            print("\n")
                            print("Студент был успешно удалён!".center(40))
                            wait_and_clear()
                            break
                elif choice.lower() == "нет":
                    operation_canceled()
                    break
                else:
                    there_is_no_such_type_of_answer_and_operation_canceled()
                    break

        elif answer == 2:
            choice = input("Вы действительно хотите удалить всех студентов? (Да или нет)\nВаш выбор: ")
            sys("cls")  # Clear console
            if choice.lower() == "да":
                STUDENTS.clear()
                print("\n")
                print("Студенты были успешно удалены!".center(40))
                wait_and_clear()
                break
            elif choice.lower() == "нет":
                operation_canceled()
                break
            else:
                there_is_no_such_type_of_answer_and_operation_canceled()
                break
        else:
            there_is_no_such_type_of_answer()

        break


# Function for printing students list
def students_list():
    print("--- Список студентов ---".center(40))
    i = 1
    for stud in STUDENTS:
        stud.number = i
        print(stud)
        i += 1


# Function for reading student list from file
def reading_from_file():
    global STUDENTS
    with open("students.txt", "rb") as file:
        STUDENTS = pickle.load(file)


# Function for writing student list in file
def writing_in_file():
    with open("students.txt", "wb") as file:
        pickle.dump(STUDENTS, file)


# Function for waiting and clearing
def wait_and_clear():
    sleep(3)    # Wait 3 seconds
    sys("cls")  # Clear console


def try_input(question):
    try:
        answer = int(input(question))
        sys("cls")  # Clear console
        return answer
    except ValueError:
        sys("cls")  # Clear console
        return -1


# Function for showing message that action canceled
def operation_canceled():
    print("\n")
    print("Операция отменена!".center(40))
    wait_and_clear()


# Function for showing message that user entered invalid answer and action canceled
def there_is_no_such_type_of_answer_and_operation_canceled():
    print("\n")
    print("Такого варианта ответа нет".center(40))
    print("Операция отменена!".center(40))
    wait_and_clear()


# Function for showing message that user entered invalid answer
def there_is_no_such_type_of_answer():
    print("\n")
    print("Такого варианта ответа нет!".center(40))
    print("Попробуйте ещё раз".center(40))
    wait_and_clear()


# Function for showing message that the list of student is empty
def list_is_empty():
    print("\n")
    print("Список студентов пуст!".center(40))
    wait_and_clear()


# Function for showing message that user entered invalid student number
def there_is_no_such_student_num():
    print("\n")
    print("Студента с таким номером нет!".center(40))
    print("Проверьте и попробуйте ещё раз".center(40))
    wait_and_clear()


# Function for showing message "Good bye!"
def print_bye():
    print("\nДо свидания!")


# Start of our program
if __name__ == "__main__":
    PERSON = Person()   # Object of my class for future actions with it
    STUDENTS = list()   # List for saving all students
    start()  # Start
