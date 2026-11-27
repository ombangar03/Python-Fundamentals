class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def work(self):
        print("Developer is writing code")

class Tester(Employee):
    pass

dev = Developer()
tester = Tester()

dev.work()
tester.work()


# Method overriding → Child provides its own implementation.
# Method inheritance → Child reuses the parent's implementation.