class RomanNumeral(object):
    def __init__(self, decimal):
        super()
        self.decimal = decimal

    def __str__(self):
        if self.decimal == 0:
            return ''
        else:
            return 'I'*self.decimal
