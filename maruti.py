from Vehicle import Vehicle

class disel(Vehicle):

    def __init__(self,model,wheel,airbag,engin,sunroof,seats):
        super(disel,self).__init__(model,wheel,airbag,engin,seats)
        self.dsunroof = sunroof


    def Showinfo(self):
        print('###########################')
        super(disel,self).Showinfo()
        print('Sunroof present',self.dsunroof)

class petrol(Vehicle):

    def __init__(self,model,wheel,airbag,engin,sunroof,seats):
        super(petrol,self).__init__(model,wheel,airbag,engin,seats)
        self.psunroof = sunroof


    def Showinfo(self):
        print('###########################')
        super(petrol,self).Showinfo()
        print('Sunroof present',self.psunroof)