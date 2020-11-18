# Магические методы

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_email_data(self):
        return {
            'name': self.name,
            'email': self.email
        }


jane = User('Jane Doe', 'janedoe@example.com')

print(jane.get_email_data())
# {'name': 'Jane Doe', 'email': 'janedoe@example.com'}

class Singleton:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance


a = Singleton()
b = Singleton()

a is b
# True

# __str__

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return '{} <{}>'.format(self.name, self.email)


jane = User('Jane Doe', 'janedoe@example.com')

print(jane)
# Jane Doe < janedoe @ example.com >



