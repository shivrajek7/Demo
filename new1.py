from new import Bank
from new import HDFC
from new import SBI
from new import ICICI
from new import InvalidCustomerException
from new import InvalidBankException


class Customer:

    def __init__(self, amnt, btype, atmpin):
        self.balance = amnt
        self.bankType = btype
        self.pin = atmpin

    def __str__(self):
        return 'Customer Balance :{}\n' \
               'Customer Bank :{}\n' \
               'Customer PIN : {}\n'.format(self.balance, self.bankType, self.pin)


cust = Customer(11000, 'PNB', '1275')
print('Before1 -- ', cust)
hdfcBank = HDFC(cust)
print('Before2 -- ', cust)
hdfcBank.withdrawAmount(cust, 2000)
print(HDFC.hdfcBalance)
print('Before3 -- ', cust)


cust1 = Customer(12000, 'SBI', '1234')
print('Before1 -- ', cust1)
sbiBank = SBI(cust1)
print('Before2 -- ', cust1)
sbiBank.withdrawAmount(cust1, 1000)
print(SBI.sbiBalance)
print('Before3 -- ', cust1)

cust2 = Customer(14000, 'ICICI', '1257')
print('Before1 -- ', cust2)
iciciBank = ICICI(cust2)
print('Before2 -- ', cust2)
iciciBank.withdrawAmount(cust2, 3000)
print(ICICI.iciciBalance)
print('Before3 -- ', cust2)