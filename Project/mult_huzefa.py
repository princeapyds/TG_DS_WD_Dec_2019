def mult_two(a,b):
   print(a*b)

def mult(*args):
    i = 1
    for x in args:
        i *= x
    print(i)

mult_two(4,5)
mult(4,5,1)