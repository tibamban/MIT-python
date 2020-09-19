import math
def perpDist(px, py, a, b, c):
    d1=abs(a*px + b*py + c )
    d2=math.sqrt(a**2+b**2)
    return d1/d2
print(perpDist(0,0,3,4,-6))
