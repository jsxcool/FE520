class LCG:
    #                   x0      a           c          M    (int)
    def __init__(self, seed, multiplier, increment, modulus):
        self.seed = seed 
        self.multiplier = multiplier 
        self.increment = increment 
        self.modulus = modulus 
    
    def getSeed(self):
        return self.seed
    def setSeed(self, val):
        self.seed = val
    
    x = 0
    def start(self):    # initialize generator
        global x 
        x = self.seed/self.modulus
        return x
    
    def nextRandom(self):
        global x
        x = (self.multiplier*x+self.increment)%self.modulus/self.modulus
        return x
    
    def listRandom(self, length):
        ls = [self.seed/self.modulus]
        for i in range(0, length-1):
            ls.append(self.nextRandom())
        return ls

    
class SCG(LCG):
    def __init__(self, seed, multiplier, increment, modulus):
        if seed%4 != 2:
            raise ValueError("seed % 4 != 2")
        self.seed = seed 
        self.multiplier = multiplier 
        self.increment = increment 
        self.modulus = modulus 

    def __iter__(self):
        yield self.seed/self.modulus
        for i in range(0, self.modulus):   # iterate modulus times
            yield self.nextRandom()
        
    
l = LCG(1,543,6,689)
l.setSeed(3)
print("seed is: ", l.getSeed())
l.start()
print("next is: ", l.nextRandom())
print("random list: ", l.listRandom(5))

s = SCG(2,666,6,748)
a = iter(s)
print("SSG next is: ", next(a))
