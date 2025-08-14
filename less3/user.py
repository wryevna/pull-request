
class User:

    def __init__(self, name, lastname):
        print("Всем привет!")
        self.firstname = name
        self.mylastname = lastname

    def my_name(self):
        print("Меня зовут", self.firstname)

    def my_last_name(self):
        print("Моя фамилия", self.mylastname)

    def my_fio(self):
        print("А все вместе", self.firstname, self.mylastname)
