import math
def pointDist(x1,y1,x2,y2):
    d1=(x2-x1)**2
    d2=(y2-y1)**2
    D=math.sqrt(d1+d2)
    return D
print((pointDist(-7,-4,17,6.5)))
