class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Employee:
    def __init__(self, designation, salary):
        self.designation = designation
        self.salary = salary

    def emp_info(self):
        return f"Designation: {self.designation}, Salary: {self.salary}"

class Manager(Person, Employee):
    def __init__(self, name, age, designation, salary):
        # Initialize the base classes
        Person.__init__(self, name, age)
        Employee.__init__(self, designation, salary)
        self.experience = "20 years"

    def manager_info(self):
        # Collect info from both Person and Employee classes
        person_info = self.person_info()
        employee_info = self.emp_info()
        return f"{person_info}, {employee_info}"

# Create an instance of Manager
manager = Manager("Krish", 21, "Snr DevSecOps Engineer", 2500000)

# Print the manager's info and experience
print(manager.manager_info())
print(f"Experience: {manager.experience}")
