def clipclop(lo, x, hi):
    x=max(x,lo)
    x=min(hi,x)
    return x
print(clipclop(34,9,94))
