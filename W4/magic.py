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

# __hash__, __eq__

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __hash__(self):
        return hash(self.email)

    def __eq__(self, obj):
        return self.email == obj.email


jane = User('Jane Doe', 'jdoe@example.com')
joe = User('Joe Doe', 'jdoe@example.com')

print(jane == joe)
# True
print(hash(jane))
print(hash(joe))
# 7885430882792781082
# 7885430882792781082
user_email_map = {user: user.name for user in [jane, joe]}

print(user_email_map)
# { < __main__.User object at 0x107415908 >: 'Joe Doe'}

# __getattr__, __getattribute__, __setattr__, __delattr__

class Researcher:
    def __getattr__(self, name):
        return 'Nothing found :('

    def __getattribute__(self, name):
        return 'nope'


obj = Researcher()

print(obj.attr)
print(obj.method)
print(obj.DFG2H3J00KLL)
# nope
# nope
# nope

class Researcher:
    def __getattr__(self, name):
        return 'Nothing found :()\n'

    def __getattribute__(self, name):
        print('Looking for {}'.format(name))
        return object.__getattribute__(self, name)


obj = Researcher()

print(obj.attr)
print(obj.method)
print(obj.DFG2H3J00KLL)
# Looking for attr
# #     Nothing
# #     found: ()
# #
# # Looking for method
# #     Nothing
# #     found: ()
# #
# # Looking for DFG2H3J00KLL
# #     Nothing
# #     found: ()

class Ignorant:
    def __setattr__(self, name, value):
        print('Not gonna set {}!'.format(name))


obj = Ignorant()
obj.math = True
# Not gonna set math!

class Polite:
    def __delattr__(self, name):
        value = getattr(self, name)
        print(f'Goodbye {name}, you were {value}!')

        object.__delattr__(self, name)


obj = Polite()

obj.attr = 10
del obj.attr
# Goodbye attr, you were 10!
