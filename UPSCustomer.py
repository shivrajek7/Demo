class dealer:

    def __init__(self,name,address,type,upscompany,upsrate):
        self.dealername = name
        self.dealeradd  = address
        self.dealertype = type
        self.upscompany = upscompany
        self.upsrate = upsrate


    def __str__(self):
        return 'Dealer Name   :{} \n'\
               'Dealer Address:{} \n'\
               'Dealer Type   :{} \n' \
               'UPS company :{} \n' \
               'UPS Rate   :{}\n'.format(self.dealername,self.dealeradd,self.dealertype,self.upscompany,self.upsrate)
