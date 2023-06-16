class Arithmetic:
    """
    This class adds and multiplies.

    :param args: any number of numerical inputs
    :type args: tuple(float)

    """
    def __init__(self, *args):
        self.params = list(args)
    
    def add(self):
        """
        Returns sum of Arithmetic instance attributes.
        
        :param args: None.
        :type args: None
        :return: The sum of all attributres of Arithmetic instance
        """
        return sum(self.params)
    
    def sum(self):
        """
        Returns the sum of Arithmetic instance attributes.
        The duplication is to make the interface easier to use.

        :param args: None.
        :type args: None
        :return: The sum of all attributres of Arithmetic instance

        """
        return self.add()
    
    def multiply(self):
        """
        Returns the product of Arithmetic instance attributes.

        :return: product of all attributes of Arithmetic instance
        """
        prod = 1
        for x in self.params:
            prod = prod * x
        return prod