class Stud:

    scount=0
    def __init__(self,id,name,marks):
        self.sid = id
        self.sname = name
        self.smarks = marks
        Stud.scount += 1


    def showstudentinfo(self):
        print('######################')
        print("Student id is",self.sid)
        print('Student name is',self.sname)
        print('Students mark is',self.smarks)

id = int(input('Enter student id '))
name =input('Enter student name')
marks = int(input('Enter students marks'))

print('u enetred --',id,'--',name,'--',marks)
st1=Stud(id,name,marks)

id = int(input('Enter student id '))
name =input('Enter student name')
marks = int(input('Enter students marks'))

print('u enetred --',id,'--',name,'--',marks)
st2=Stud(id,name,marks)



print('Student 1 info')
st1.showstudentinfo()

print('Student 2 info')
st2.showstudentinfo()