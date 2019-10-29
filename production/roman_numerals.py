class RomanNumeral(object):
    def __init__(self, decimal):
        super()
        self.decimal = decimal
        self.numeral_by_decimal = {50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    def __numeral_to_string__(self):
        if self.decimal == 0:
            return ''
        else:
            closest_numeral, rest = self.__closest_numeral__()
            return closest_numeral + str(RomanNumeral(rest))

    def __closest_numeral__(self):
        decimals = self.numeral_by_decimal.keys()
        closest = next(d for d in decimals if d <= self.decimal)
        return (self.numeral_by_decimal[closest], self.decimal - closest)

    def __str__(self):
        return self.__numeral_to_string__()
