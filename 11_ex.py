def ind_maxlist(a, ind=0, mx_ind=0 ):
    if ind < len(a):
        if a[ind] > a[mx_ind]:
            mx_ind = ind
        return ind_maxlist(a, ind+1, mx_ind)
    else:
        return mx_ind

list = [3, 7, 2, 9, 5]
print(ind_maxlist(list)) 
