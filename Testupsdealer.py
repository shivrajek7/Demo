from UPSCustomer import dealer
from UPS import UPS
from UPS import powersafe
from UPS import rudra
from UPS import eaton



def checkdealerinfo():

    list1=[]
    dealercommision =0
    while 1:
        dealername = input('Enter Dealer Name:')
        dealeradd = input('Enter Dealer Address:')
        dealertype = input('Enter UPS Type:')
        upscompany = input('Enter UPS company:')
        upsrate =input('Enter UPS Price:')

        deal = dealer(dealername,dealeradd,dealertype,upscompany,upsrate)
        list1.append(deal)

        #upskdealer = dealer(dealername,dealeradd,dealertype,upscompany,upsrate)


        flag = int(input('Do you want to contiue ....0 - No, 1- Yes'))
        if flag == 0:
            break


    for item in list1:
       print(item)


    for it in list1:
        if it.upscompany.lower() == 'powersafe':
            psu = powersafe('powerresources','Highfrequency','15','3ph')
            dealercommision = UPS.calculate_commision(dealer.upsrate)
            dealercommision += dealercommision
            print(dealercommision)

    ''' 
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
'''
if __name__ == '__main__':
    checkdealerinfo()
