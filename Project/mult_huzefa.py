def sum(a,b):
   print(a+b)

def sum_n(*args):
    i = 0
    for x in args:
        i += x
    print(i)

sum(4,5)
sum_n(4,5,5)