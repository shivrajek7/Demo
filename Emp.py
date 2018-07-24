import datetime

print(datetime.datetime.now().year)


class Emp :

    company = 'Infy'

    def __init__(self,id,nm,age,address='Mumbai'):
        self.eid = id
        self.ename = nm
        self.eage = age
        self.eaddress = address

    def showempdetails(self):
        print('Emp Id -- ',self.eid)
        print('FirstName -- ', self.ename)
        print('Emp Age -- ', self.eage)
        print('Emp Address -- ', self.eaddress)
        print('Emp Companay name', self.company)


emp1 =  Emp(10,'Amit',29)
emp2 =  Emp(10,'Amit',29,'Pune')
#emp1 == emp2

emp1.showempdetails()
print('-----------------------------')
emp2.showempdetails()


print(emp1.__dict__,'Emp1 info \n\n') # Cogni
print(emp2.__dict__,'Emp2 info \n\n') # Infy
print(Emp.__dict__,'Emp info \n\n')   #Infy


print('\n\n\n\n\n')

print(id(emp1),'Hashcode of Emp1')
print(id(emp2),'Hashcode of Emp2')
print(id(emp1) == id(emp2),"Emp1 id == Emp2 id")

emp3 = emp2

print(id(emp1))
print(id(emp2))+print(id(emp3))

print(emp1==emp2)
print(emp2==emp3)
print(emp1 is emp2)
print(emp2 is emp3)





'''
id
is
==
constructor default value
globle variable
module == python file 
package == folder in which we have modules  //logical structure of your proj
import followed by module name
from followed by package name



'''