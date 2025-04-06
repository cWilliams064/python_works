class User:

  def __init__(self, first_name, last_name, email, username, login_attempts):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.username = username
    self.login_attempts = login_attempts

  def describe_user(self):
    return (
      f"Name: {self.first_name} {self.last_name}, Email: {self.email}, "
      f"Username: {self.username}"
    )
    
  def greet_user(self):
    return f"Hello, {self.first_name}! Welcome back."
  
  def increment_login_attempts(self):
    self.login_attempts += 1
    return self.login_attempts

  def reset_login_attempts(self):
    self.login_attempts = 0
    return self.login_attempts

user = User('emily', 'clark', 'emily.clark@example.com', 'emilyclark', 0)
print(user.describe_user())

print(user.increment_login_attempts())
print(user.increment_login_attempts())
print(user.increment_login_attempts())
print(user.increment_login_attempts())
print(user.increment_login_attempts())

print(f"Login attempts before reset: {user.login_attempts}")

user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")