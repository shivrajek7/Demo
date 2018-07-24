from abc import ABC,abstractmethod


class Bank(ABC):

    def __init__(self,bankName,bankAddress,ifsccode):
        self.bankname = bankName
        self.bankaddress = bankAddress
        self.bankifsc = ifsccode

    @abstractmethod
    def calculateintereset(self,account_balance):
          pass


    def displayAccountInfo(self,object):
        print('Bank Details')


    def __str__(self):
        return 'BankName : {} \n' \
               'Bank Address : {} \n' \
                'Bank IFSCCode : {} \n'.format(self.bankname,self.bankaddress,self.bankifsc)


class HDFC(Bank):


    def __init__(self,bankName,bankaddr,ifsccode):
        super().__init__(bankName,bankaddr,ifsccode)


    def calculateintereset(self,account_balance):
        return account_balance*0.07;


class SBI(Bank):

    def calculateintereset(self, account_balance):
        return account_balance * 0.08;

    def __init__(self,bankName,bankaddr,ifsccode):
        super().__init__(bankName,bankaddr,ifsccode)



class ICICI(Bank):

    def calculateintereset(self, account_balance):
        return account_balance * 0.09;


    def __init__(self,bankName,bankaddr,ifsccode):
        super().__init__(bankName,bankaddr,ifsccode)

#bank = Bank()
#print(bank)


'''
icici = ICICI('ICICI','PUNE,BaljiNagar',102011)
iciciInterest = icici.calculateintereset(10000)

sbi = SBI('SBI','PUNE,Hinjewadi',102011)
sbiInterest =sbi.calculateintereset(10000)

hdfc = HDFC('HDFC','PUNE,Wakad',102011)
hdfcInterest =hdfc.calculateintereset(10000)

print(iciciInterest,'--',sbiInterest,'--',hdfcInterest)

print(icici.__dict__)
print(sbi.__dict__)
print(hdfc.__dict__)

'''