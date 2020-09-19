def clip(lo, x, hi):
    if x>hi:
        z=hi
    elif x<lo:
        z=lo
    else:
        z=x
    return z
print(clip(2,9,4))
