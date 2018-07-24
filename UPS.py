from abc import ABC,abstractmethod

class UPS(ABC):

    def __init__(self,upsname,upstype,upscap):
        self.upsname = upsname
        self.upstype = upstype
        self.upscap = upscap


    @abstractmethod
    def calculate_commision(self,upstotalprice):
        pass

    def __str__(self):
        return 'UPS Name:{} \n' \
               'UPS Type:{} \n' \
               'UPS Cap :{} \n'.format(self.upsname,self.upstype,self.upscap)


class powersafe(UPS):

    def __init__(self,upsname,upstype,upscap,upsphase):
        super().__init__(upsname,upstype,upscap)
        self.upsphase =upsphase


    def calculate_commision(self,upstotalprice):
        return upstotalprice * 0.20

    def __str__(self):
        return 'UPS Name:{} \n' \
               'UPS Type:{} \n' \
               'UPS Cap :{} \n'.format(self.upsname,self.upstype,self.upscap)


class rudra(UPS):

    def __init__(self, upsname, upstype, upscap, upsphase,upsdisp):
        super().__init__(upsname, upstype, upscap)
        self.upsphase = upsphase
        self.upsdisp =upsdisp

    def calculate_commision(self, upstotalprice):
        return upstotalprice * 0.30

    def __str__(self):
        return 'UPS Name:{} \n' \
               'UPS Type:{} \n' \
               'UPS Cap :{} \n'.format(self.upsname,self.upstype,self.upscap)


class eaton(UPS):

    def __init__(self, upsname, upstype, upscap, upsphase):
        super().__init__(upsname, upstype, upscap)
        self.upsphase = upsphase

    def calculate_commision(self, upstotalprice):
        return upstotalprice * 0.10

    def __str__(self):
        print('UPS Name:{} \n' \
               'UPS Type:{} \n' \
               'UPS Cap :{} \n'.format(self.upsname,self.upstype,self.upscap))

'''
us = eaton('powerware','highfreq','550kw','three')
me = us.calculate_commision(100)
u = 100+ me
print(u)
'''