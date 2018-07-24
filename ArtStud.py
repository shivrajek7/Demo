from StudentInfo import StudentInfo

class ArtStud(StudentInfo):

    def __init__(self,sid,sname,sage,smarks,degree,saddress):
        super(ArtStud,self).__init__(sid,sname,sage,smarks,saddress)
        self.artDegree = degree


    def showdetails(self):
        super(ArtStud,self).showdetails()
        print('Student degree',self.artDegree)


