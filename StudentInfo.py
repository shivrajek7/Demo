class StudentInfo:

    def __init__(self,sid,sname,sage,smarks,saddress='Pune'):
        self.studId = sid
        self.studName = sname
        self.studAge = sage
        self.studMarks = smarks
        self.studAdress = saddress

    def showdetails(self):
        print('Student id :',self.studId)
        print('Student Name:',self.studName)
        print('Student Age:', self.studAge)
        print('StudentMarks',self.studMarks)
        print('Student Add:', self.studAdress)
'''
def main():
    student1 = StudentInfo(1,'shiv',30,99,'Peth')
    student2 = StudentInfo(2, 'raj', 31, 100)
    student1.showdetails()
    student2.showdetails()

if __name__ == '__main__':
    main()
'''

