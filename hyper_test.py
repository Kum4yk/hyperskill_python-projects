class Angel:
    color = "white"
    feature = "wings"
    home = "Heaven"


class Demon:
    color = "red"
    feature = "horns"
    home = "Hell"


class Human:
    species = "Homo Sapiens"
    n_legs = 2
    n_arms = 2


class RockBand:
    genre = "rock"
    n_members = 4
    famous_songs = list()


class House:
    construction = "building"
    elevator = True


class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        self.area = 1/2 * self.a * self.b


class Alien:
    count = 0
    places = []

    def __init__(self, planet, species):
        self.planet = planet
        self.species = species


class User:
    n_active = 0
    users = []

    def __init__(self, name, active):
        self.active = active
        self.name = name
        if active:
            User.users.append(name)
            User.n_active += 1


class Painting:
    museum = "Louvre"

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return '"{}" by {} ({}) hangs in the {}.'.\
            format(self.title, self.author, self.year, Painting.museum)


class City:
    all_cities = []

    def __init__(self, name, year):
        self.name = name
        self.year = year


ny = City("New York", 1624)
ny.all_cities.append("New York")

stockholm = City("Stockholm", 1187)
stockholm.all_cities = ["Stockholm"]
print(City.all_cities)
