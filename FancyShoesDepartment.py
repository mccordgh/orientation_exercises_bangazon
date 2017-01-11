from Department import *

class FancyShoesDepartment(Department):
    """Class for representing Fancy Shoes department

    Methods: __init__, add_shoe, get_shoes, etc.
    """

    def __init__(self, name, supervisor, employee_count):
      super().__init__(name, supervisor, employee_count)
      self.shoes = {}
      self.popular_model = ""

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