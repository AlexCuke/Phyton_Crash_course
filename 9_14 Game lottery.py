from random import randint
class Die:
    def __init__(self):
        self.values =[1,2,3,4,5,6,7,8,9,10,'f','s','a','h','g']
        self.win=[]
    def  roll_die(self):
        for i in range(4):
            value = randint(1,len(self.values) )
            self.win.append(self.values[value])
        print(self.win)
die1=Die()
die1.roll_die()
