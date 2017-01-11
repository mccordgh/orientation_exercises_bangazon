from Department import *

class SpinArtDepartment(Department):
    """Class for representing Spin Art department

    Methods: __init__, add_spin_art, get_spin_arts, etc.
    """

    def __init__(self, name, supervisor, employee_count):
      super().__init__(name, supervisor, employee_count)
      self.spin_arts = {}
      self.artist_of_the_month = ""

    def add_spin_art(self, spin_art_name, spin_art_description):
      """Adds a spin_art and it's description, to the set of spin_arts

      Arguments:
        spin_art_name (string)
        spin_art_description (string)
      """

      self.spin_arts.update({spin_art_name: spin_art_description})

    def get_spin_arts(self):
      """Returns spin_art list"""

      return self.spin_arts