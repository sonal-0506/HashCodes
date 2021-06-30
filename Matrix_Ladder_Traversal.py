# Matrix Ladder Traversal (Diagonal Traversal from lower indexes)

r = int(input("rows < 500: "))
c = int(input("columns < 500: "))

def minu(a,b):
    if a<b:
        return a
    else:
        return b
    
def minimum(a,b,c):
    return minu(minu(a,b),c)

def maximum(a,b):
    if a>b:
        return a
    else:
        return b
    
for i in range(r+c-1):
    a = maximum(0, i-r)
    count = minimum(i, c-a, r)
    for j in range(count):
        print(minu(r,i)-j-1, a+j)
    print(end="\n")
