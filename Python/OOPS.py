class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    
    def __gt__(self,ordr2):
        return self.price > ordr2.price

ordr1=Order("chips",20)
ordr2=Order("tea",10)

print(ordr1 > ordr2)

    
        