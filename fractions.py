def find_gcd(num1, num2):
    """
    Returns the Greatest Common Divisor (GCD) of num1 and num2.
    Assumes num1 and num2 are positive integers.
    """
    smaller = min(num1, num2)
    for i in range(smaller, 1, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return 1


class Fraction(object):
    '''Defines a Fraction type that has an integer
    numerator and a non-zero integer denominator'''

    def __init__(self, num=0, denom=1):
        ''' Creates a new Fraction with numberator
         num and denominator denom'''
        self.numerator = num
        if denom != 0:
            self.denominator = denom
        else:
            raise ZeroDivisionError

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __add__(self, other):
        return Fraction(self.numerator * other.denominator
                        + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator,
                        self.denominator*other.denominator)

    def __eq__(self, other):
        return True if self.numerator*other.denominator \
                       == other.numerator*self.denominator else False

    def __repr__(self):
        return f'Fraction({self.numerator}, {self.denominator})'


class ReducedFraction(Fraction):  # is a sub-class of the Fraction class
    """reduced fraction"""

    def __init__(self, numerator=0, denominator=1):
        super().__init__(numerator, denominator)
        # explicitly use parent/super class __init__()
        self.__reduce__()

    def __reduce__(self):
        gcd = find_gcd(self.numerator, self.denominator)
        self.numerator /= gcd
        self.denominator /= gcd
        self.numerator, self.denominator = int(self.numerator), int(self.denominator)
        return Fraction(self.numerator, self.denominator)

    def __repr__(self):
        return f'ReducedFraction({self.numerator}, {self.denominator})'

    def __add__(self, other):
        added_fraction = super(ReducedFraction, self).__add__(other)
        return ReducedFraction(added_fraction.numerator, added_fraction.denominator)

    def __mul__(self, other):
        multiplied_fraction = super(ReducedFraction, self).__mul__(other)
        return ReducedFraction(multiplied_fraction.numerator, multiplied_fraction.denominator)


class MixedNumber:
    """mixed number"""

    def __init__(self, number: int, fraction):
        self.number = number
        self.fraction = ReducedFraction(fraction.numerator,
                                        fraction.denominator)

    def __repr__(self):
        return f'MixedNumber({self.number},' \
               f' ReducedFraction({self.fraction.numerator},' \
               f' {self.fraction.denominator}))'

    def __str__(self):
        return f'{self.number} and {str(self.fraction)}'

    def __add__(self, other):
        fraction = ReducedFraction(self.fraction.numerator,
                                   self.fraction.denominator) + \
                   ReducedFraction(other.fraction.numerator,
                                   other.fraction.denominator)

        if fraction.numerator / fraction.denominator >= 1:
            fraction.numerator -= fraction.denominator
            return MixedNumber(self.number + other.number + 1, fraction)
        else:
            return MixedNumber(self.number + other.number, fraction)


fraction_1 = Fraction(3, 4)
fraction_2 = Fraction(4, 6)
mixed_num_1 = MixedNumber(2, fraction_1)
mixed_num_2 = MixedNumber(1, fraction_2)
print(mixed_num_1 + mixed_num_2)




