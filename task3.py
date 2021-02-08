import re


class NotNumericError(ValueError):
    def __init__(self, text):
        self.txt = text


class float(float):
    def __new__(cls, value):
        regrxp = r"^\d+\.*\d*$"
        match = re.match(regrxp, value)
        if not match:
            raise NotNumericError('Не десятичное чило')
        return super().__new__(cls, value)


numeric_list=[]

while True:
    try:
        f=input()
        if f=='stop':
            break
        numeric_list.append(float(f))
    except NotNumericError as e:
        print(e)
print(*numeric_list)