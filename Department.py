class Department(object):
    """Parent class for all departments

    Methods: __init__, get_name, get_supervisor
    """

    def __init__(self, name, supervisor, employee_count):
        self.name = name
        self.supervisor = supervisor
        self.size = employee_count
        self.budget = 500000

    def get_name(self):
      """Returns the name of the department"""
      
      return self.name

    def get_supervisor(self):
      """Returns the name of the supervisor"""

      return self.supervisor

    def get_budget(self):
      """Returns base budget for Department"""
      return self.budget

    def meet(self):
      """Prints meeting place for all employees of this Department"""
      
      print("\t{}: \t\tEveryone meet in {}'s offce.".format(self.name, self.supervisor))