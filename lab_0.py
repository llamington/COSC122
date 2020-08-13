class Rectangle(object):
    """ Rectangle class """

    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height

    def area(self):
        """computes area"""
        return self.width * self.height

    def perimeter(self):
        """computes perimeter"""
        return 2*self.width + 2*self.height

    def __str__(self):
        """returns rectangle"""
        hash_rec = ''
        for row in range(self.height):
            hash_rec += '#'*self.width + '\n'
        return hash_rec


rec = Rectangle(20, 5)
print(rec)