from Vehicle import Vehicle

class bmw(Vehicle):


    def __init__(self,model,wheel,airbag,engin,camera,seats):
        super(bmw,self).__init__(model,wheel,airbag,engin,seats)
        self.bcamera =camera

    def Showinfo(self):
        print('##############################')
        super(bmw,self).Showinfo()
        print('Camera is:',self.bcamera)

