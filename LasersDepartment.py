from Department import *

class LasersDepartment(Department):
    """Class for representing Lasers department

    Methods: __init__, add_laser, get_lasers, etc.
    """

    def __init__(self, name, supervisor, employee_count):
      super().__init__(name, supervisor, employee_count)
      self.lasers = {}
      self.last_employee_blinding = ""

    def add_laser(self, laser_name, laser_description):
      """Adds a laser and it's description, to the set of lasers

      Arguments:
        laser_name (string)
        laser_description (string)
      """

      self.lasers.update({laser_name: laser_description})

    def get_lasers(self):
      """Returns laser list"""

      return self.lasers