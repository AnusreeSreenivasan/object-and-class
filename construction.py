class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def increase_salary(self):
        self.salary = self.salary + 1000
    def decrease_salary(self):
        self.salary = self.salary - 2000
    def display(self):
        print(self.name,self.age,self.salary)
obj=Employee("ANUSREE", 21, 2500)
obj.display()
obj.increase_salary()
obj.display()
obj.decrease_salary()
obj.display()
print("**********************************************************")
obj2=Employee("My self", 30, 5000)
obj2.display()
obj2.increase_salary()
obj2.display()
obj2.decrease_salary()
obj2.display()
print("-----------------------------------------------------------------------")
obj3=Employee("SREE", 32, 100000)
obj3.display()
obj3.increase_salary()
obj3.display()
obj3.decrease_salary()
obj3.display()

