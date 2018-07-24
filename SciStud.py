from StudentInfo import StudentInfo

class Scistud(StudentInfo):


    def __init__(self,sid,sname,sage,smarks,degree,saddress):
        super(Scistud,self).__init__(sid,sname,sage,smarks,saddress)
        self.scidegree = degree

    def showdetails(self):
        super(Scistud,self).showdetails()
        print('Students degree: ',self.scidegree)

        