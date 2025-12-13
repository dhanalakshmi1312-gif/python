
class Personal:
    def information(self, name, mail, mobile, address):
        self.name = name
        self.mail = mail
        self.mobile = mobile
        self.address = address

        print(" PERSONAL DETAILS ")
        print("Name:", self.name)
        print("Email:", self.mail)
        print("Mobile:", self.mobile)
        print("Address:", self.address)


class Educational(Personal):
    def information(self, name, mail, mobile, address, m1, m2, m3):
        super().information(name, mail, mobile, address)

        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

        self.total = m1 + m2 + m3
        self.percentage = self.total / 3

        print(" EDUCATIONAL DETAILS ")
        print("Mark 1:", self.m1)
        print("Mark 2:", self.m2)
        print("Mark 3:", self.m3)
        print("Total:", self.total)
        print("Percentage:", self.percentage)

obj = Educational()
obj.information("Divya", "divya@gmail.com", "9876543210", "Madurai", 85, 90, 80)
