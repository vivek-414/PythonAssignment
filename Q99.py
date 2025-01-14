class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value

employee = Employee("Atharv", 50000)
print(f"Salary: {employee.salary}")
employee.salary = 60000
print(f"Updated Salary: {employee.salary}")
