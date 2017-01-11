from FancyShoesDepartment import *
from HumanResourcesDepartment import *
from LasersDepartment import *
from SpinArtDepartment import *
from Employee import *

fancy_shoes_dept = FancyShoesDepartment("Fancy Shoes", "Lauren Taylor", 4)
fancy_shoes_dept.add_shoe("Zebra Heels with Tassles", "A fancy all-nighter with zebra main tassles on the rear.")
fancy_shoes_dept.popular_model = "Zebra Heels with Tassles"

human_resources_dept = HumanResourcesDepartment("Human Resources", "Russel Grab", 2)
human_resources_dept.add_policy("Laser01", "Laser Harassment will NOT be tolerated.")
human_resources_dept.lawsuits = 4

lasers_dept = LasersDepartment("Lasers", "Dirk Funk", 5)
lasers_dept.add_laser("Ricocheting Hi-Beam", "This thing could blind of mongoose from 200yds.")
lasers_dept.last_employee_blinding = "1/4/2017"

spin_art_dept = SpinArtDepartment("Spin Art", "Matthew McCord", 12)
spin_art_dept.add_spin_art("Swirly Twirly Fun and Curly", "A brilliantly woven tapestry of primary colors.")
spin_art_dept.artist_of_the_month = "Orville Sash"

print("Bangazon Company Departments:\n{}".format("*" * 100))
print("\t" + fancy_shoes_dept.name)
print("\t" + human_resources_dept.name)
print("\t" + lasers_dept.name)
print("\t" + spin_art_dept.name)

print("")

print("For Meetings:\n{}".format("*" * 100))
fancy_shoes_dept.meet()
human_resources_dept.meet()
lasers_dept.meet()
spin_art_dept.meet()

print("")

print("Department Budgets:\n{}".format("*" * 100))
print("{} budget: \t\t\t\t${}".format(fancy_shoes_dept.name, fancy_shoes_dept.get_budget()))
print("{} budget: \t\t${}".format(human_resources_dept.name, human_resources_dept.get_budget()))
print("{} budget: \t\t\t\t\t\t\t${}".format(lasers_dept.name, lasers_dept.get_budget()))
print("{} budget: \t\t\t\t\t\t${}".format(spin_art_dept.name, spin_art_dept.get_budget()))

print("")
donny = Employee("Donny", "Vespertino")
donny.eat()
donny.eat(food_eaten="a sandwich")
donny.eat(companions=["Joey", "Big", "Crusher"])
donny.eat("pizza", ["Biggy", "Daniel", "Beno"])
