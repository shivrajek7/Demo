from abc import ABC, abstractmethod

class InvalidBankException(Exception):

    def __init__(self, msg):
        super().__init__(msg)


class InvalidCustomerException(Exception):

    def __init__(self, msg):
        super().__init__(msg)


class Bank(ABC):

    @abstractmethod
    def depositAmount(self, amount, atmpin):
        pass

    @abstractmethod
    def withdrawAmount(self, amount, atmpin):
        pass

    def checkIsValidCustomer(self, customer):
        if customer.bankType == 'SBI' or customer.bankType == 'HDFC' or customer.bankType == 'ICICI':
            return True
        else:
            raise InvalidCustomerException('You are not HDFC Customer but belongs to ' + customer.bankType)


class HDFC(Bank):
    hdfcBalance = 100000
    listofPins = ['1234', '4567', '8910']

    def __init__(self, customer):
        isValidCustomer = self.checkIsValidCustomer(customer)
        if isValidCustomer and HDFC.listofPins.__contains__(customer.pin):
            customer.HDFCValidCustomer = True
        else:
            customer.HDFCValidCustomer = False

    def depositAmount(self, customer, depositAmnt):
        if customer.HDFCValidCustomer:
            HDFC.hdfcBalance += depositAmnt
            customer.balance += depositAmnt
        else:
            raise InvalidBankException('You are not HDFC Customer but belongs to ' + customer.bankType)

    def withdrawAmount(self, customer, withDrawAmnt):
        if customer.HDFCValidCustomer:
            HDFC.hdfcBalance -= withDrawAmnt
            customer.balance -= withDrawAmnt
        else:
            raise InvalidBankException('You are not HDFC Customer but belongs to ' + customer.bankType)

class SBI(Bank):
    sbiBalance = 100000
    listofPins = ['1234', '4567', '8910']

    def __init__(self, customer):
        isValidCustomer = self.checkIsValidCustomer(customer)
        if isValidCustomer and SBI.listofPins.__contains__(customer.pin):
            customer.SBIValidCustomer = True
        else:
            customer.SBIValidCustomer = False

    def depositAmount(self, customer, depositAmnt):
        if customer.SBIValidCustomer:
            SBI.sbiBalance += depositAmnt
            customer.balance += depositAmnt
        else:
            raise InvalidBankException('You are not SBI Customer but belongs to ' + customer.bankType)

    def withdrawAmount(self, customer, withDrawAmnt):
        if customer.SBIValidCustomer:
            SBI.sbiBalance -= withDrawAmnt
            customer.balance -= withDrawAmnt


class ICICI(Bank) :
    iciciBalance = 100000
    listofPins = ['1234', '4567', '8910']

    def __init__(self, customer):
        isValidCustomer = self.checkIsValidCustomer(customer)
        if isValidCustomer and ICICI.listofPins.__contains__(customer.pin):
            customer.ICICIValidCustomer = True
        else:
            customer.ICICIValidCustomer = False

    def depositAmount(self, customer, depositAmnt):
        if customer.ICICIValidCustomer:
            ICICI.iciciBalance += depositAmnt
            customer.balance += depositAmnt
        else:
            raise InvalidBankException('You are not ICICI Customer but belongs to ' + customer.bankType)

    def withdrawAmount(self, customer, withDrawAmnt):
        if customer.ICICIValidCustomer:
            ICICI.iciciBalance -= withDrawAmnt
            customer.balance -= withDrawAmnt

'''
class Customer:

    def __init__(self, amnt, btype, atmpin):
        self.balance = amnt
        self.bankType = btype
        self.pin = atmpin

    def __str__(self):
        return 'Customer Balance :{}\n' \
               'Customer Bank :{}\n' \
               'Customer PIN : {}\n'.format(self.balance, self.bankType, self.pin)


cust = Customer(11000, 'HDFC', '1234')
#print('Before1 -- ', cust)
hdfcBank = HDFC(cust)
#print('Before2 -- ', cust)
hdfcBank.withdrawAmount(cust, 2000)
print(HDFC.hdfcBalance)
print('Before3 -- ', cust)

cust1 = Customer(12000, 'SBI', '1234')
#print('Before1 -- ', cust1)
sbiBank = SBI(cust1)
#print('Before2 -- ', cust1)
sbiBank.withdrawAmount(cust1, 1000)
print(SBI.sbiBalance)
print('Before3 -- ', cust1)

cust2 = Customer(14000, 'ICICI', '1234')
#print('Before1 -- ', cust2)
iciciBank = ICICI(cust2)
#print('Before2 -- ', cust2)
iciciBank.withdrawAmount(cust2, 3000)
print(ICICI.iciciBalance)
print('Before3 -- ', cust2)



		Bank
			depositAmount --a
			Withdrawamount --a
			checkValidCustomer --Implemented





			ICICI
					-- checkIsICICCUstomer
			HDFC
					-- checkIsHDFCUstomer
			SBI
					-- checkIsSBICUstomer

		Customer
			id
			nm
			pin
			balance
			accoutType


		Exception
				-- pin invalid
				--customer invalid
				--Doesnt belonw to bank
				-- Token invalid
				--



'''