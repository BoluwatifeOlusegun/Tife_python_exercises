class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = []

    def show_privileges(self):
        print("Administrator Privileges:")
        for privilege in self.privileges:
            print(privilege)

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges