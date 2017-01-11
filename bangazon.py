from FancyShoesDepartment import *
from HumanResourcesDepartment import *
from LasersDepartment import *
from SpinArtDepartment import *

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

print(fancy_shoes_dept.name)
print(human_resources_dept.name)
print(lasers_dept.name)
print(spin_art_dept.name)