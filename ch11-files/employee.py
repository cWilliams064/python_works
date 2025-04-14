class Employee:
  """Creating a employee and their yearly salary for a raise."""

  def __init__(self, first_name, last_name, annual_salary):
    """Store employee information."""
    self.first_name = first_name
    self.last_name = last_name
    self.annual_salary = annual_salary

  def give_raise(self, raise_ammount=5000):
    """Calcualate the employee salary after raise."""
    self.annual_salary += raise_ammount
    original_salary = self.annual_salary - raise_ammount
    after_raise = (
      f"After a raise {self.first_name.title()} {self.last_name.title()}'s "
      f"salary increased from {original_salary} to {self.annual_salary}."
    )
    return after_raise
  
employee = Employee('john', 'smith', 45000)
employee_raise = employee.give_raise()

print(employee_raise)
