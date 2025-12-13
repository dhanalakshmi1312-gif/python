
class School:
    def information(self, name, mail, mobile, address):
        self.name = name
        self.mail = mail
        self.mobile = mobile
        self.address = address

        print(" SCHOOL DETAILS ")
        print("Name:", self.name)
        print("Email:", self.mail)
        print("Mobile:", self.mobile)
        print("Address:", self.address)


class Staff(School):
    def staffinformation(self, dept):
        self.dept = dept
        print(" STAFF DETAILS ")
        print("Department:", self.dept)


class Student(School):
    def studentinformation(self, dept):
        self.dept = dept
        print(" STUDENT DETAILS ")
        print("Department:", self.dept)


choice = input("Enter Student or Staff: ")

name = input("Enter name: ")
mail = input("Enter email: ")
mobile = input("Enter mobile: ")
address = input("Enter address: ")
dept = input("Enter department: ")

if choice.lower() == "student":
    obj = Student()
    obj.information(name, mail, mobile, address)
    obj.studentinformation(dept)

elif choice.lower() == "staff":
    obj = Staff()
    obj.information(name, mail, mobile, address)
    obj.staffinformation(dept)

else:
    print("Invalid Choice")
