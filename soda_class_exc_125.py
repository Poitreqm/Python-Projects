# Create a Soda class (to determine the type of carbonated water) that takes 1 argument during initialization (responsible for adding to the selected lemonade).
# In this class, implement the show_my_drink() method, which prints "Soda and {ADDITIVE}" if there is an additive, otherwise the following phrase will be displayed: "Regular soda".


class Soda:
    def __init__(self, dobavka=None):
        self.dobavka = dobavka

    def show_my_drink(self):
        if self.dobavka:
            print(f"gaz: {self.dobavka}")
        else:
            print("Simple gaz")


r = Soda()
r.show_my_drink()
