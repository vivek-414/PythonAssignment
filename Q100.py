class Parent1:
    def function1(self):
        print("Function from Parent1.")

class Parent2:
    def function2(self):
        print("Function from Parent2.")

class Child(Parent1, Parent2):
    pass

child = Child()
child.function1()
child.function2()
