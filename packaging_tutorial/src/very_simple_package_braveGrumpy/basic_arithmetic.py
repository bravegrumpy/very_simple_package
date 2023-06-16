class Arithmetic:
    """This class adds and multiplies."""
    def __init__(self, *args):
        """The Arithmetic class can accept any number of arguments."""
        self.params = list(args)
    
    def add(self):
        """Returns the sum of all the arguments passed into the instance."""
        return sum(self.params)
    
    def sum(self):
        """Does the same thing as add."""
        return self.add()
    
    def multiply(self):
        """This function finds the product of all the arguments passed inot hte Arithmetic object."""
        prod = 1
        for x in self.params:
            prod = prod * x
        return prod