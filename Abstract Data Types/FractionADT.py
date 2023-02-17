from math import gcd

class Rational:
    def __init__(self, n, d):
        if d == 0:
            print(f"This fraction {n}/{d} is indefinite")
        else: 
            g = gcd(n,d)
            self.numer = int(n/g)
            self.denom = int(d/g)

    def add(self, otherFraction):
        a = self.numer*otherFraction.denom + self.denom*otherFraction.numer
        b = self.denom*otherFraction.denom
        return Rational(a,b)

    def sub(self, otherFraction):
        a = self.numer*otherFraction.denom - self.denom*otherFraction.numer
        b = self.denom*otherFraction.denom
        return Rational(a,b)
    
    def mul(self, otherFraction):
        a = self.numer*otherFraction.numer
        b = self.denom*otherFraction.denom
        return Rational(a,b)
    
    def div(self, otherFraction):
        a = self.numer*otherFraction.denom 
        b = self.denom*otherFraction.numer
        return Rational(a,b)

    def comparative(self, otherFraction):
        if self.S_to_D() < otherFraction.S_to_D(): return f"{self.__str__()} is less than {otherFraction.__str__()}"
        elif self.S_to_D() > otherFraction.S_to_D(): return f"{self.__str__()} is greater than {otherFraction.__str__()}"
        else: return f"{self.__str__()} is equal to {otherFraction.__str__()}"
    
    def S_to_D(self):
        return self.numer/self.denom
    
    def __str__(self):
        return "%d/%d" % (self.numer,self.denom)


if __name__ == "__main__":
    a = Rational(4,8)
    b = Rational(5,15)
    c = Rational(22,99)
    print(a)

    print(b.add(a))
    print(c.sub(b))
    print(a.mul(c))
    print(b.div(b))

    print(b.comparative(a))
    print(b.comparative(c))
    print(c.comparative(c))
    
    print(b.S_to_D())
    