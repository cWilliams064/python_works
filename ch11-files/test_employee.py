import pytest
from employee import Employee

@pytest.fixture
def employee():
  """A employee that will be available to all test functions."""
  employee = Employee('john', 'doe', 65000)
  return employee

def test_give_default_raise(employee):
  """Test for the default raise value."""
  employee.give_raise()
  assert employee.annual_salary == 70000

def test_give_custom_raise(employee):
  """Test for a custom raise value."""
  employee.give_raise(3000)
  assert employee.annual_salary == 68000
