class User:

    def __init__(self, name, birthday_year):
        self.name = name
        self.birthday_year = birthday_year

    def __str__(self):
        return self.name


class Biography:

    def __init__(self, text, users):
        self.user = users
        self.text = text


class Brend:

    def __init__(self, name, users):
        self.name = name
        self.users = users
