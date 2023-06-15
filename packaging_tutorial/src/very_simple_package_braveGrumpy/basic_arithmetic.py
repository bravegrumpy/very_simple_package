class Arithmetic:
    def __init__(self, *args):
        self.params = list(args)
    
    def add(self):
        return sum(self.params)
    
    def sum(self):
        return self.add()
    
    def multiply(self):
        prod = 1
        for x in self.params:
            prod = prod * x
        return prod