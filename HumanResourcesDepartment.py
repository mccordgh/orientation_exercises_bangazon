from Department import *

class HumanResourcesDepartment(Department):
    """Class for representing Human Resources department

    Methods: __init__, add_policy, get_policy, meet.
    """

    def __init__(self, name, supervisor, employee_count):
      super().__init__(name, supervisor, employee_count)
      self.policies = {}
      self.lawsuits = 0
      self.budget = super().get_budget() - 95555


    def add_policy(self, policy_name, policy_text):
      """Adds a policy and it's description to the set of policies

      Arguments:
        policy_name (string)
        policy_text (string)
      """

      self.policies.update({policy_name: policy_text})

    def get_policy(self):
      """Returns policy list"""

      return self.policies

    def meet(self):
      """Prints meeting place for all employees of this Department"""
      
      print("\t{}: \t\tEveryone meet in {}'s feelings.".format(self.name, self.supervisor))