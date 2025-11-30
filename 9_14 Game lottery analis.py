from random import randint
class Die:
    def __init__(self):
        self.values =[1,2,3,4,5,6,7,8,9,10,'f','s','a','h','g']
        self.win=[]
        self.my_ticket=[3,5,'f','a']
        self.count=0
    def  roll_die(self):
        win=[]
        for i in range(4):
            value = randint(1,len(self.values) -1)
            win.append(self.values[value])
        self.count += 1
        return win
    
    def roll_my_ticket(self):
        while True:
            win = self.roll_die()
            if win == self.my_ticket:
                print("Совпало после попыток:", self.count)
                print("Выигрышный билет:", win)
                break
die1=Die()
die1.roll_my_ticket()
