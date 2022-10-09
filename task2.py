import math


class Rational:
    def __init__(self, numerator=1, denominator=1):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError('numerator and denominator must be an integer type')
        if denominator == 0:
            raise ZeroDivisionError("Can not divide by zero")
        self.__numerator = numerator
        self.__denominator = denominator

    def __str__(self):
        gcd = math.gcd(self.__numerator, self.__denominator)
        return f"{self.__numerator // gcd} / {self.__denominator // gcd}"

    def float_rational(self):
        return self.__numerator / self.__denominator


a = Rational(2, 4)
print(a)
print(a.float_rational())

