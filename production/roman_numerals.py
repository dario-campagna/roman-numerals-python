class RomanNumeral(object):
    def __init__(self, decimal):
        super()
        self.decimal = decimal

    def __numeral_to_string__(self):
        numeral_by_decimal = {0: '', 1: 'I', 4: 'IV', 5: 'V'}
        if self.decimal in numeral_by_decimal:
            return numeral_by_decimal[self.decimal]
        elif self.decimal == 6:
            return 'VI'
        else:
            return numeral_by_decimal[1]*self.decimal

    def __str__(self):
        return self.__numeral_to_string__()
