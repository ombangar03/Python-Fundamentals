# Create a class called Student.

# Requirements:
# 1. Use __init__() to accept name, age, and course.
# 2. Store them using self.
# 3. Create a method called display_details().
# 4. Create two student objects with different values.
# 5. Display both students' details.


class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print(self.name, self.age, self.course)


student1 = Student("Rahul", 24, "Computer Science")
student2 = Student("Ravi", 25, "Mechanical")

student1.display_details()
student2.display_details()