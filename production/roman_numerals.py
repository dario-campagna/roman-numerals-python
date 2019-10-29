class RomanNumeral(object):
    def __init__(self, decimal):
        super()
        self.decimal = decimal

    def __str__(self):
        if self.decimal == 0:
            return ''
        elif self.decimal == 4:
            return 'IV'
        else:
            return 'I'*self.decimal
