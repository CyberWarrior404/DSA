class Student:
    def __init__(self, name, age, grade, student_id, address):
        self.name = name
        self.age = age
        self.grade = grade
        self.student_id = student_id
        self.__address = address

    def get_address(self):
        admin_password = input("Enter admin password: ")
        if admin_password == "4213":
            print("authorized")
            print(self.__address)
        else:
            print("You are not authorized")


student1 = Student("Sinmi", 16, "10th", "S001", "123 Main Street")

print(student1.name)
print(student1.age)
print(student1.grade)
print(student1.student_id)

student1.get_address()
