from Department import *

class FancyShoesDepartment(Department):
    """Class for representing Fancy Shoes department

    Methods: __init__, add_shoe, get_shoes, meet.
    """

    def __init__(self, name, supervisor, employee_count):
      super().__init__(name, supervisor, employee_count)
      self.shoes = {}
      self.popular_model = ""
      self.budget = super().get_budget() + 555555

    def add_shoe(self, shoe_name, shoe_description):
      """Adds a shoe and it's description, to the set of shoes

      Arguments:
        shoe_name (string)
        shoe_description (string)
      """

      self.shoes.update({shoe_name: shoe_description})

    def get_shoes(self):
      """Returns shoe list"""

      return self.shoes

    def meet(self):
      """Prints meeting place for all employees of this Department"""

      print("\t{}: \t\t\t\tEveryone meet in {}'s bathroom.".format(self.name, self.supervisor))