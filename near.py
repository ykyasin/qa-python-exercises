def near(x, y):
    x = list(x)
    y = list(y)
    test = x.copy()
    for i in range(len(x)):
        test.pop(i)
        if test == y:
            return True
        test = x.copy()
    
    return False





print(near("reset","rest"))