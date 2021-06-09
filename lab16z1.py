

class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Manager(Person):
    contacts = []
    counter = 0

    def __init__(self, name, surname, number=-1):
        if (number == -1) or (number >= len(Manager.contacts)):
            Manager.contacts.append(self)
            Manager.counter += 1
        elif number < len(Manager.contacts):
            Manager.contacts[number] = self
