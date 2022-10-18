# деление чисел
def init(a, b, c):
    global divisible, divisor, sign
    divisible=a
    divisor=b
    sign=c

def do():
    if sign=="%":
        return divisible%divisor
    if sign=="/":
        return divisible/divisor
    if sign=="//":
        return divisible//divisor
