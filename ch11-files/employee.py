class Employee:
  """Represents an employee and handles salary raises."""

  def __init__(self, first_name, last_name, annual_salary):
    """Store employee information."""
    self.first_name = first_name
    self.last_name = last_name
    self.annual_salary = annual_salary

  def give_raise(self, raise_amount=5000):
    """Calculate the employee salary after raise."""
    self.annual_salary += raise_amount
    original_salary = self.annual_salary - raise_amount
    after_raise = (
      f"After a raise {self.first_name.title()} {self.last_name.title()}'s "
      f"salary increased from {original_salary} to {self.annual_salary}."
    )
    return after_raise
  
employee = Employee('john', 'smith', 45000)
employee_raise = employee.give_raise()

print(employee_raise)
