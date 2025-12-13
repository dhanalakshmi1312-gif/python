
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
    def education_info(self, m1, m2, m3):
        self.total = m1 + m2 + m3
        self.percentage = self.total / 3

        print(" EDUCATIONAL DETAILS ")
        print("Total:", self.total)
        print("Percentage:", self.percentage)


class Bank(Educational):
    def bank_info(self, acc_num, branch_name, bank_name, ifsc, balance):
        self.acc_num = acc_num
        self.branch_name = branch_name
        self.bank_name = bank_name
        self.ifsc = ifsc
        self.balance = balance

        print(" BANK DETAILS ")
        print("Account No:", self.acc_num)
        print("Branch:", self.branch_name)
        print("Bank:", self.bank_name)
        print("IFSC:", self.ifsc)
        print("Available Balance:", self.balance)


obj = Bank()
obj.information("Divya", "divya@gmail.com", "9876543210", "Madurai")
obj.education_info(85, 90, 80)
obj.bank_info("123456789", "Main Branch", "SBI", "SBIN000123", 50000)
