class User:
    def __init__(self, name, login, password, age):
        self.name = name
        self.__age = age
        self.__login = login
        self.__password = password

    @property
    def login(self):
        return f"{self.name}'s login is {self.__login}"

    @property
    def password(self):
        raise AttributeError("you cant see it")

    @password.setter
    def password(self, new_password):
        self.__password = new_password
        print("password has been changed")


u1 = User("Jack", "Jack1324132", "1324243sdfkjsdf", 31)
# print(u1.password)
u1.password = "sdfwrwer"
