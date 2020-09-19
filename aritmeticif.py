def arithmeticIf(v, a, b, c):
    if v>0:
        z=a
    elif v<0:
        z=b
    else:
        z=c
    return z
print(arithmeticIf(0,'positif','negatif','null'))
