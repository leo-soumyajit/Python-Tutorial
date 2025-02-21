def calculateGmean(a,b):
    res = (a*b)/(a+b)
    return res

print(calculateGmean(9,8))



def greaterNumber(a,b):
    if a>b:
        print(a,"is Greater..")
    else:
        print(b, "is Greater..")

print(__name__)
if __name__ == "__main__":
    greaterNumber(10, 11)


def isLesser(a,b):
    pass    # says to python the impl of this function will do later
            # otherwise it gives an exception