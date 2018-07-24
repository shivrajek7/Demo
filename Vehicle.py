class Vehicle:

    def __init__(self,model,wheel,airbag,engin,seats):
        self.VModel = model
        self.VWheel = wheel
        self.VAirbag = airbag
        self.VEngin = engin
        self.VSeats = seats

    def Showinfo(self):
        print('Model name:',self.VModel)
        print('No.of Wheels:',self.VWheel)
        print('No.of Air bags:',self.VAirbag)
        print('Type of Engin:',self.VEngin)
        print('No.of Seats:',self.VSeats)


