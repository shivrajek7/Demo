from abc import ABC,abstractmethod
from customer import customer

class Bank(ABC):


    @abstractmethod
    def calculate_interest(self):
          pass

class hdfc(Bank):

    def calculate_interest(self,interest):
        self.cinterest = interest
        return interest * 0.07


class sbi(Bank):

    def calculate_interest(self,interest):
        self.cinterest = interest
        return interest * 0.07

def main():
   c1 = hdfc()
   d = c1.calculate_interest()
   list.append(d)
   print(list)




if __name__ == '__main__':
    main()














