import pickle         # For working with file
import os             # For checking file size
import tkinter as tk  # For GUI

from class_Person import Person        # Class Person
from tkinter import ttk                # For Combobox
from tkinter import messagebox as msg  # For showing message or warning


def set_characteristics(window: tk.Tk | tk.Toplevel, geometry: str):
    """Function for setting window characteristics"""
    window.title("Crud-app")
    window.geometry(geometry)
    window.resizable(False, False)
    window["bg"] = "grey60"
    set_row_and_column_configure(window)


def set_row_and_column_configure(window: tk.Tk | tk.Toplevel):
    """Function for setting window row and column configure"""
    for i in range(16):
        window.grid_rowconfigure(i, minsize=50)
        window.grid_columnconfigure(i, minsize=50)


def make_button(master: tk.Tk | tk.Toplevel, text: str, function, row: int, column: int):
    """Function for making a button"""
    btn = tk.Button(master, text=text, command=function,
                    activebackground="light blue", font=("Arial", 25, "normal"))
    btn.grid(row=row, column=column, columnspan=5, rowspan=2, sticky="wens")
    return btn


def make_entry(master: tk.Toplevel, row: int, column: int, column_span: int):
    """Function for making an entering field"""
    entry = tk.Entry(master, font=("Arial", 20, "normal"))
    entry.grid(row=row, column=column,
               rowspan=2, columnspan=column_span, sticky="wens")
    return entry


def make_label(master: tk.Toplevel, text: str, font_size: int,
               row: int, column: int, column_span: int):
    """Function for making a label"""
    label = tk.Label(master, text=text, font=("Arial", font_size, "bold"), bg="grey60")
    label.grid(row=row, column=column, columnspan=column_span, sticky="w")
    return label


def create_window():
    """Function for creating new person"""
    ROOT.withdraw()
    win = tk.Toplevel()
    set_characteristics(win, "800x750+700+20")

    make_label(win, "Name:", 15, row=0, column=9, column_span=10)
    name_ent = make_entry(win, row=1, column=9, column_span=6)

    make_label(win, "Surname:", 15, row=0, column=1, column_span=10)
    surname_ent = make_entry(win, row=1, column=1, column_span=6)

    make_label(win, "Nik name:", 15, row=4, column=1, column_span=10)
    nik_ent = make_entry(win, row=5, column=1, column_span=14)

    make_label(win, "Age:", 15, row=8, column=1, column_span=10)
    age_ent = make_entry(win, row=9, column=1, column_span=6)

    make_label(win, "Number of comp:", 15, row=8, column=9, column_span=10)
    num_of_comp_ent = make_entry(win, row=9, column=9, column_span=6)

    make_button(win, "Create",
                lambda: create_action(win, name_ent, surname_ent, nik_ent, age_ent, num_of_comp_ent),
                row=12, column=10)

    win.mainloop()


def create_action(window: tk.Toplevel, name: tk.Entry, surname: tk.Entry, nik: tk.Entry,
                  age: tk.Entry, num_of_comp: tk.Entry):
    """Function for action after creating window"""
    if name.get() and surname.get() and nik.get() and age.get() and num_of_comp.get():
        person = Person()

        check_name = checking_before_adding("Name", name, person)
        check_surname = checking_before_adding("Surname", surname, person)
        check_age = checking_before_adding("Age", age, person)
        check_num_of_comp = checking_before_adding("Num of comp", num_of_comp, person)

        person.nik = nik.get()
        person.id_generation()

        if check_name and check_surname and check_age and check_num_of_comp:
            LST.insert(tk.END, person)
            PEOPLE.append(person)
            destroy_this_window_and_show_root(window)
    else:
        message("error", "Not all fields are filled!")


def read_window():
    """Function for showing information about person"""
    element = LST.curselection()
    if len(element) != 0:
        person = finding_person(element)

        ROOT.withdraw()
        win = tk.Toplevel()
        set_characteristics(win, "800x750+650+30")

        make_label(win, f"Surname and name: {person.surname} {person.name}", 25,
                   row=1, column=1, column_span=10)
        make_label(win, f"Nik name: {person.nik}", 25,
                   row=3, column=1, column_span=10)
        make_label(win, f"Age: {person.age}", 25,
                   row=5, column=1, column_span=10)
        make_label(win, f"Number of computer: {person.num_of_comp}", 25,
                   row=7, column=1, column_span=10)
        make_label(win, f"ID: {person.id}", 25,
                   row=9, column=1, column_span=30)

        make_button(win, "<- Back", lambda: destroy_this_window_and_show_root(win),
                    row=12, column=10)

        win.mainloop()


def update_window():
    """Function for updating some information about person"""
    element = LST.curselection()
    if len(element) != 0:
        answer = tk.StringVar()

        ROOT.withdraw()
        win = tk.Toplevel()
        set_characteristics(win, "800x550+650+50")

        make_label(win, "What do you want to update?", 15, row=1, column=1, column_span=20)
        choice = ttk.Combobox(win, textvariable=answer, font=("Arial", 15, "normal"),
                              values=("Name", "Surname", "Age", "Nik name", "Number of computer"))
        choice.grid(row=2, column=1, columnspan=8, sticky="wens")

        lbl = make_label(win, "", 15, row=4, column=1, column_span=10)
        lbl.configure(textvariable=answer)
        change_ent = make_entry(win, row=5, column=1, column_span=14)

        make_button(win, "Update", lambda: update_action(win, choice, change_ent, element),
                    row=8, column=10)

        win.mainloop()


def update_action(window: tk.Toplevel, choice: ttk.Combobox, change_ent: tk.Entry, element):
    """Function for action after updating window"""
    person = finding_person(element)

    check = checking_before_adding(choice.get(), change_ent, person)

    if check:
        # Updating person in Listbox
        LST.delete(element[0])
        LST.insert(element[0], person)
        # Updating person in people list
        for p in PEOPLE:
            if p.id == person.id:
                p = person

        destroy_this_window_and_show_root(window)


def delete_action():
    """Function for deleting person"""
    person = LST.curselection()
    if len(person) != 0:
        answer = message("ask", "Are you really want to delete this person?")
        if answer:
            LST.delete(person)
            PEOPLE.pop(person[0])


def message(title: str, mess: str):
    """Function for showing some message"""
    if title == "ask":
        answer = msg.askyesno("Last question", mess)
        return answer
    elif title == "error":
        msg.showerror("Error", mess)


def valid_name(what_check: str, entry: tk.Entry):
    """Function for checking if valid name"""
    return what_check == "Name" and entry.get().isalpha()


def valid_surname(what_check: str, entry: tk.Entry):
    """Function for checking if valid surname"""
    return what_check == "Surname" and entry.get().isalpha()


def valid_age(what_check: str, entry: tk.Entry):
    """Function for checking if valid age"""
    return what_check == "Age" and entry.get().isdigit() and 120 > int(entry.get()) > 0


def valid_number_of_computer(what_check: str, entry: tk.Entry):
    """Function for checking if valid number of computer"""
    return what_check == "Num of comp" and entry.get().isdigit()


def checking_before_adding(what_check: str, entry: tk.Entry, person: Person):
    """Function for some checking on valid information before adding"""
    entry.configure(fg="black")

    if valid_name(what_check, entry):
        person.name = entry.get()
    elif valid_surname(what_check, entry):
        person.surname = entry.get()
    elif valid_age(what_check, entry):
        person.age = int(entry.get())
    elif valid_number_of_computer(what_check, entry):
        person.num_of_comp = int(entry.get())
    else:
        message("error", "There is some mistakes!")
        entry.configure(fg="red")
        return False

    return True


def clearing_entry(entry: tk.Entry):
    """Function for clearing some entry"""
    entry.delete(0, tk.END)


def destroy_this_window_and_show_root(window: tk.Toplevel):
    """Function for destroying some window and showing again main window"""
    window.destroy()
    ROOT.deiconify()


def there_is_such_person(person: Person, surname: str, name: str):
    return surname == person.surname and name == person.name


def finding_person(element):
    """Function for returning person object which was found"""
    surname, name = LST.get(element).split()

    for p in PEOPLE:
        if there_is_such_person(p, surname, name):
            return p


def reading_from_file():
    """Function for reading person list from file"""
    global PEOPLE
    # Actions for checking file size
    file_stats = os.stat("people.txt")
    if file_stats.st_size != 0:
        with open("people.txt", "rb") as file:
            PEOPLE = pickle.load(file)

        for person in PEOPLE:
            LST.insert(tk.END, person)


def writing_in_file():
    """Function for writing person list in file"""
    with open("people.txt", "wb") as file:
        pickle.dump(PEOPLE, file)


if __name__ == '__main__':
    PEOPLE = list()

    ROOT = tk.Tk()
    set_characteristics(ROOT, "800x650+650+50")

    scrollbar = tk.Scrollbar(ROOT)
    scrollbar.grid(row=1, column=7, rowspan=11, sticky="wens")

    LST = tk.Listbox(yscrollcommand=scrollbar.set, font=("Arial", 15, "bold"))
    LST.grid(row=1, column=1, rowspan=11, columnspan=6, sticky="wens")

    reading_from_file()

    make_button(ROOT, "Create", create_window, row=1, column=10)
    make_button(ROOT, "Read", read_window, row=4, column=10)
    make_button(ROOT, "Update", update_window, row=7, column=10)
    make_button(ROOT, "Delete", delete_action, row=10, column=10)

    scrollbar.config(command=LST.yview)
    ROOT.mainloop()

    writing_in_file()
