
# class RentShop:
#     def __init__(self,stock):
#         self.stock=stock
#     def stockdisplay(self):
#         print("Total available Stock",self.stock)
#     def Rentfor(self,q):
#         print("total value",q*100)
#         if q <= 0 :
#
#             print("enter only positive number")
#         else:
#             print("Stock available is ", self.stock -q )
# while True:
#     obj=obj.RentShop(100)
#     obj.RentShop=RentShop(100)
#     UC = int(input( '''
#         1 For available stock
#         2 Enter Your required Qty
#         3 Exit
#     '''
#     ))
#     if UC == 1:
#         obj.stockdisplay()
#     elif UC == 2:
#          n = int(input ("enter Qty", obj.Rentfor))
#     else :
#
#          break


class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    def print_name(self):
        return f"{self.first_name}, {self.last_name}, {self.pay}"


emp1 = Employee("ALi", "Ahmad", 50000)
# print(emp1.pay)

class Programmer(Employee):
    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)
        self.prog_lang = prog_lang

pro1 = Programmer("ALi", "Ahmad", 90000, "PYTHON")
pro2 = Programmer("ءسمان", "Khan", 70000, "JAVA")
# print(pro1.pay)


class Manger(Employee):
    def __init__(self, first_name, last_name, pay, employee=None):
        super().__init__(first_name, last_name, pay)
        if employee == None:
            employee = []
        else:
            self.employee = employee

    def add_emp(self, emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def remove_emp(self, emp):
        if emp in self.employee:
            self.employee.remove(emp)

    def print_emp(self):
        for i in self.employee:
            print("---->", i.print_name())

mgr = Manger("Haris", "Ali", 90000, [pro1])
# mgr.print_emp()
mgr.remove_emp(pro2)
mgr.print_emp()





