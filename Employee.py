import random

class Employee(object):
    """Class for representing an Employee

    Methods: __init__, eat.
    """

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.restaurant_list = ["Shoney's", "Outback", "Dorsia", "The Lovely Nibblet", "Solomon Grundy's"]

    def eat(self, food_eaten="", companions=""):
        if companions == "" and food_eaten != "":
            random_restaurant = "the office"
        else:
            random_restaurant = self.restaurant_list[random.randint(0,4)]

        if companions == "":
            companions_string = ""
        else:
            companions_string = "with {}".format(", ".join(companions))

        if food_eaten != "":
            food_eaten += " "

        print("{0} {1} ate {2}at {3} {4}".format(self.first_name, self.last_name, food_eaten, random_restaurant, companions_string))
