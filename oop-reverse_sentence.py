class Sentense:
    def __init__(self, senten):
        self.senten = senten
        
    def reverse (self):
        return ' '.join(self.senten.split()[::-1])
        
        
sentense =Sentense(input('enter your sentence:'))
print(sentense.reverse())