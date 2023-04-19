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

    def get_all_users(self, db):
        with open(db, "r") as fo:
            rows = csv.reader(fo)
            rows = list(rows)
        for row in rows:
            user = User(row[0], row[1], row[4], row[5])
            self.__users.append(user)

    def log_in(self):
        login = input("Please, enter login: ")
        ness_user = None
        for user in self.__users:
            if user.login == login:
                ness_user = user
        if ness_user is None:
            print("there is no user with such a login")
        else:
            password = input("Plese, enter the password: ")
            user_password = user.get_password()
            if password == user_password:
                print("success")
            else:
                print("wrong password try again")


class User:
    def __init__(self, user_id, login, password, money):
        self.user_id = user_id
        self.login = login
        self.__password = password
        self.money = money

    def get_password(self):
        return self.__password


app = App(None, None)

# user_info = input("id login name surname password: ").split()
# password = input("Please, input password: ")
# app.register(user_info[0], user_info[1], user_info[2], user_info[3], password, 400000)
app.get_all_users("Users_2.csv")
app.log_in()