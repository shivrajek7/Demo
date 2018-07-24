from CustomerInfo import Customer
from BankInfo import SBI
from BankInfo import ICICI
from BankInfo import HDFC



def startBankApplication():
    custlist = []

    sbiinterest = 0
    hdfcinterest = 0
    iciciinterest = 0

    while 1:
        custname = input('Enter CustName')
        custAddress = input('Enter CustAddress')
        custage = int(input('Enter CustAge'))
        custGender = input('Enter CustGender')
        custBank = input('Enter CustBank')
        custBalance = int(input('Enter CustBalance'))
        cust = Customer(custname, custAddress, custage, custGender, custBank, custBalance)
        custlist.append(cust)
        flag = int(input('Do you want to contiue ....0 - No, 1- Yes'))
        if flag == 0:
            break;

    print('No of Customers -- ', custlist.__len__())
    print(custlist)
'''
    print('Before interest calculation')
    for item in custlist:
        print(item)

    for customer in custlist:
        if customer.custbank.upper() == 'SBI':
            bank = SBI('SBI', 'Pune,wakad', 410121)
            custinterest = bank.calculateintereset(customer.custbalance)
            sbiinterest += custinterest
        elif customer.custbank.upper() == 'ICICI':
            bank = ICICI('ICICI', 'Pune,Hinjewadi', 145121) 
            custinterest = bank.calculateintereset(customer.custbalance)
            iciciinterest += custinterest
        elif customer.custbank.upper() == 'HDFC':
            bank = HDFC('HDFC', 'Pune,Katraj', 320121)
            custinterest = bank.calculateintereset(customer.custbalance)
            hdfcinterest += custinterest
        else:
            print('Invalid customer bank type', customer)

        customer.custbalance += custinterest

    print('After interest calculation')
    for item in custlist:
        print(item)

    print('ICICI has paid {} much of interest'.format(iciciinterest))
    print('HDFC has paid {} much of interest'.format(hdfcinterest))
    print('SBI has paid {} much of interest'.format(sbiinterest))
'''

if __name__ == '__main__':
    startBankApplication()



'''
    variables -- local/public
    abstractions -- bank -- calculateinterest
     Inheritacnce bank  -- HDFC
                        -- ICICI
                        -- SBI
     Polymorphism -- Method overriding -- __str__, calculateinterest
     list[] -- customer object hold
     loopings -- while, for, if
     main method --  
     method overriridding -- calculate interest is called based on object
     class-- object

'''


