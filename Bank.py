from abc import ABC,abstractmethod
from customer import customer

class Bank(ABC):


    @abstractmethod
    def calculate_interest(self):
          pass

class Hdfc(Bank):

    def calculate_interest(self,interest):
        self.cinterest = interest
        return interest * 0.07


class Sbi(Bank):

    def calculate_interest(self,interest):
        self.cinterest = interest
        return interest * 0.07

class Icici(Bank):

    def calculate_interest(self,interest):
        self.cinterest = interest
        return interest * 0.07

class UBI(Bank):

    def calculate_interest(self,interest):
        self.cinterest = interest
        return interest * 0.07        

class Bcici(Bank):

    def calculate_interest(self,interest):
        self.cinterest = interest
        return interest * 0.09
    
def main():
   c1 = hdfc()
   d = c1.calculate_interest()
   list.append(d)
   print(list)




if __name__ == '__main__':
    main()














