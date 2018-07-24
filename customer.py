from Bank import Bank

class customer():


    def __init__(self, name, age, bank, ab):
        name = input("Enter customer name:")
        age = int(input('Enter customers age:'))
        bank = input('Enter bank name:')

        if bank.lower()== 'hdfc':
            bank = 'hdfc'
        elif bank.lower()== 'sbi':
            bank = 'sbi'
        else:
            print('Invalid entry!')


        ab =int(input('Enter account balance:'))

        self.cname = name
        self.cage = age
        self.cbank = bank
        self.cab = ab
'''
    def showinfocust(self):
        print('Customer Name:', self.cname)
        print('Customer Age:', self.cage)
        print('Customer Bank:', self.cbank)
        print('Customer A/c bal:', self.cab)
'''
list=[]
count =1
while count<=1:
    a = customer(1,1,1,1)
    list.append(a.cname)
    list.append(a.cage)
    list.append(a.cbank)
    list.append(a.cab)
    count+=1











