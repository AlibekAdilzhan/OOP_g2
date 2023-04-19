import csv

class App:
    def __init__(self, graph_price, graph_time):
        self.graph_price = graph_price
        self.graph_time = graph_time
        self.__users = []

    def register(self, id, login, name, surname, password, money):
        user = User(id, login, password, money)
        with open("Users_2.csv", "a", newline="") as fo:
            writer = csv.writer(fo)
            writer.writerow([id, login, name, surname, password, money]) 
        self.__users.append(user)


class User:
    def __init__(self, user_id, login, password, money):
        self.user_id = user_id
        self.login = login
        self.__password = password
        self.money = money

    def get_password(self):
        return self.__password


app = App(None, None)

user_info = input("id login name surname password: ").split()
password = input("Please, input password: ")
app.register(user_info[0], user_info[1], user_info[2], user_info[3], password, 400000)