def maxlist(a):
    if len(a) == 1:
        return a[0]
    else:
        maxr = maxlist(a[1:])
        if a[0] > maxr:
            return a[0]
        else:
            return maxr

a = [5, 10, 15, 20, 25]
print(maxlist(a))
