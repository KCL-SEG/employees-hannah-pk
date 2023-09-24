"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Commission:
    def __init__(self):
        pass

    def get_pay(self):
        return 0

    def __str__(self):
        return ""

class BonusCommission(Commission):
    def __init__(self,amount):
        self.amount = amount

    def get_pay(self):
        return self.amount

    def __str__(self):
        return " and receives a bonus commission of "+str(self.amount)

class ContractCommission(Commission):
    def __init__(self,amount,contracts):
        self.amount = amount
        self.contracts= contracts
        
    def get_pay(self):
        return self.amount*self.contracts

    def __str__(self):
        return " and receives a commission for "+str(self.contracts)+" contract(s) at "+str(self.amount)+"/contract"

class Employee:
    def __init__(self, name):
        self.name = name
    def get_pay(self):
        pass
    
    def __str__(self):
        return self.name

class SalaryEmployee(Employee):
    def __init__(self, name, pay, commission=Commission()):
        super().__init__(name)
        self.commission = commission
        self.pay = pay

    def get_pay(self):
        base = self.commission.get_pay()
        base += self.pay
        return base

    def __str__(self):
        return super().__str__()+ " works on a monthly salary of "+str(self.pay)+ str(self.commission)+". Their total pay is "+str(self.get_pay())+"."

class HourlyEmployee(Employee):
    def __init__(self,name,pay,hours,commission=Commission()):
        super().__init__(name)
        self.commission = commission
        self.pay = pay
        self.hours = hours

    def get_pay(self):
        base = self.commission.get_pay()
        base += self.pay*self.hours 
        return base

    def __str__(self):
        return super().__str__()+ " works on a contract of "+str(self.hours)+" hours at "+str(self.pay)+"/hour" +str(self.commission)+". Their total pay is "+str(self.get_pay())+"."


    



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
#billie = Employee("Billie")
billie = SalaryEmployee('Billie',4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie',25,100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryEmployee('Renee',3000,ContractCommission(200,4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyEmployee('Jan',25,150,ContractCommission(220,3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryEmployee('Robbie',2000,BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyEmployee('Ariel',30,120,BonusCommission(600))
