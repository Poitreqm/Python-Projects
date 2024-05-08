#
# Записная книжка: Создайте программу для хранения и управления списком контактов.
#

from datetime import date


class Contact:

    id = 0

    def __init__(self, name, phone):  # конструктор
        today = date.today()
        self.id = Contact.get_id()
        self.create_date = today
        self.name = name
        self.phone = phone
        print(
            f"Contact was created. ID: {self.id} Name: {self.name} Phone: {self.phone}  Create date: {self.create_date}"
        )

    @classmethod
    def get_id(cls):  # автоматически добваляет индекс +1 к каждомгу экземпляру класса.
        cls.id += 1
        return cls.id

    def display_info(self):
        print(f"Name: {self.name}  Phone: {self.phone} Create date: {self.create_date}")


list = []

print("Hello! Welcome to Your contact list")

while True:
    print("")
    print("If you want to add contact, write 1")
    print("If you want to see all contacts, write 2")

    user_input = input("Choice: ")

    if user_input == "1":
        add_name = input("Add name of Contact: ")
        add_phone = input("Add phone of Contact: ")
        list.append(Contact(f"{add_name}", f"{add_phone}"))
    elif user_input == "2":
        if len(list) == 0:
            print("List is empty")
            continue
        print("List of Contacts: ")
        for i in list:
            print(
                f"ID: {i.id} Name: {i.name} Phone: {i.phone}  Create date: {i.create_date}",
                sep=" ",
            )
    else:
        print("Sorry. I dont undestand...")
