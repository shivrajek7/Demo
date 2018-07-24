from Vehicle import Vehicle
from maruti import disel
from maruti import petrol
from bmw import bmw

def main():
    car = Vehicle('Kirloskar',6,'No','4S',1)
    ritz = disel('DI Mahindra',4,'No','1000cc','present',5)
    sls = bmw('SLS Mc learn',4,'YES','Dx','3D camera',2)
    ballano = petrol('New ballano',4,4,'V8','present',4)
    car.Showinfo()
    ritz.Showinfo()
    sls.Showinfo()
    ballano.Showinfo()

if __name__ == '__main__':
        main()