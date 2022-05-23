from class_Person import Person  # Importing class from my module
from time import sleep           # Importing special function for waiting
from os import system as sys     # Importing special function for clearing console


# Function for asking user about his\her wanting to continue
def start():
    print("--- Crud-приложение ---".center(40))
    answer = input("Войти в систему? (Да или нет)\nВаш выбор: ")
    sys("cls")  # Clear console
    if answer.lower() == "да":
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
        answer = int(input("Ваш выбор: "))
        sys("cls")  # Clear console
        if answer == 1:
            show_list_of_students()
        elif answer == 2:
            add_students()
        elif answer == 3:
            del_students()
        elif answer == 0:
            print_bye()
            break
        else:
            there_is_no_such_type_of_answer()


# Function for showing students list
def show_list_of_students():
    while True:
        if len(students) == 0:
            list_is_empty()
            break

        students_list()
        print("\n1 - Посмотреть детальную информацию")
        print("2 - Изменить детальную информацию")
        print("0 - Вернуться назад")
        answer = int(input("Ваш выбор: "))
        sys("cls")  # Clear console

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
    answer = int(input("\nВведите номер студента про которого хотите увидеть информацию: "))
    sys("cls")  # Clear console
    if answer < 1 or answer > len(students):
        there_is_no_such_student_num()
    else:
        while True:
            for stud in students:
                if stud.number == answer:
                    stud.print_info()

            print("\n0 - Вернуться назад")
            answer = int(input("Ваш выбор: "))
            sys("cls")  # Clear console
            if answer == 0:
                break
            else:
                there_is_no_such_type_of_answer()


# Function for changing some information about student
def change_info_about_student():
    students_list()
    answer = int(input("\nВведите номер студента информацию которого хотите поменять: "))
    sys("cls")  # Clear console
    if answer < 1 or answer > len(students):
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
            choise = int(input("Ваш выбор: "))
            sys("cls")  # Clear console
            if choise == 0:
                break
            elif choise < 0 or choise > 5:
                there_is_no_such_type_of_answer()
            else:
                for stud in students:
                    if stud.number == answer:
                        if choise == 1:
                            stud.enter_name()
                        elif choise == 2:
                            stud.enter_surname()
                        elif choise == 3:
                            stud.enter_age()
                        elif choise == 4:
                            stud.enter_nik()
                        else:
                            stud.enter_number_of_comp()
                wait_and_clear()


# Function for adding student(s)
def add_students():
    print("--- Добавление студента(ов) ---".center(40))
    count = int(input("Введите сколько студентов хотите добавить: "))
    if count < 1:
        print("Не коректное количество пользователей!")
        wait_and_clear()
    else:
        for i in range(count):
            print(f"--- Студент №{i + 1} ---".center(40))
            global person
            person = Person()
            person.number = i + 1
            person.enter_name()
            person.enter_surname()
            person.enter_age()
            person.enter_nik()
            person.enter_number_of_comp()
            person.id_generation()

            students.append(person)

        wait_and_clear()


# Function for deleting student(s)
def del_students():
    while True:
        if len(students) == 0:
            list_is_empty()
            break

        print("\n1 - Удалить одного студента"
              "\n2 - Удалить всех студентов")
        answer = int(input("Ваш выбор: "))
        sys("cls")  # Clear console

        if answer == 1:
            students_list()
            answer = int(input("\nВведите номер студента которого хотите удалить: "))
            sys("cls")  # Clear console
            if answer < 1 or answer > len(students):
                there_is_no_such_student_num()
            else:
                choice = input("Вы действительно хотите удалить этого студента? (Да или нет)\nВаш выбор: ")
                sys("cls")
                if choice.lower() == "да":
                    for stud in students:
                        if stud.number == answer:
                            students.remove(stud)
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
                students.clear()
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
    for stud in students:
        stud.number = i
        print(stud)
        i += 1


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


# Function for waiting and clearing
def wait_and_clear():
    sleep(3)    # Wait 3 seconds
    sys("cls")  # Clear console


# Function for showing message that user entered invalid answer
def there_is_no_such_type_of_answer():
    print("\n")
    print("Такого варианта ответа нет!".center(40))
    print("Проверьте и попробуйте ещё раз".center(40))
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
    person = Person()   # Object of my class for future actions with it
    students = list()   # List for saving all students
    start()  # Start
