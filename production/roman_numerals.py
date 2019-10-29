class RomanNumeral(object):
    def __init__(self, decimal):
        super()
        self.decimal = decimal

    def __numeral_to_string__(self):
        if self.decimal == 0:
            return ''
        elif self.decimal == 4:
            return 'IV'
        elif self.decimal == 5:
            return 'V'
        else:
            return 'I'*self.decimal

    def __str__(self):
        return self.__numeral_to_string__()
