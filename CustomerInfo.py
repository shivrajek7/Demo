class Customer :

    def __init__(self,name,addr,age,gender,bank,balance):
            self.custname = name
            self.custaddr = addr
            self.custage = age
            self.custgender = gender
            self.custbank = bank
            self.custbalance = balance

    def showCustomerDetails(self):
        return '------------------------- \n' \
               'CustName : {} \n' \
               'CustAddr : {} \n' \
               'CustAge : {} \n' \
               'CustGender : {} \n' \
               'CustBank : {} \n'\
               'CustBalance : {} \n'.format(self.custname,self.custaddr,
                                      self.custage,self.custgender,
                                      self.custbank,self.custbalance)

    def __str__(self):
        return '------------------------- \n' \
               'CustName : {} \n' \
               'CustAddr : {} \n' \
               'CustAge : {} \n' \
               'CustGender : {} \n' \
               'CustBank : {} \n' \
               'CustBalance : {} \n'.format(self.custname, self.custaddr,
                                            self.custage, self.custgender,
                                            self.custbank, self.custbalance)



'''
cust1 = Customer('John','Pune,Katraj',34,'Male','SBI',20000)
print(str(cust1))


cust2 = Customer('John','Pune,Katraj',34,'Male','SBI',30000)
#print(cust1.showCustomerDetails())
#print(cust2.showCustomerDetails())
print(cust2)
print(str(cust1))
'''

