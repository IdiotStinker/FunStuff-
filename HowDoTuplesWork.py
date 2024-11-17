def tupleStuff(t):
    tuple = (3, 2 ,1)

    otherTuple = (0, -1, -2)
    #tuple.extend(otherTuple)
    print(tuple)
    tuple = (2, 1)
    print(tuple)
    tuple = otherTuple
    print(tuple)
    print(otherTuple)
    tuple = t
    print(tuple)
    print(t)
    t = (7, 7, 7)
    print(t)
    tuple = t + tuple
    print(tuple)
    tuple += tuple
    print(tuple)
    t = otherTuple
    t *= 2
    print(t)
    #t -= (7, 7)
    #print(t)

def listStuff(l):
    list = [2, 5, 6]
    list.extend([3, 1 ,5])
    print(list)
    print(l)
    l.append("hey")
    print(l)

t = (1, 0)
tupleStuff(t)

#listForTest = [2, 0, "no", 4.2]
#for i in range(3, 16):
    #print(i)
#listStuff(listForTest)
#print(listForTest)

#THREE ARGS FOR i IN RANGE
#Start (inclusive)
#End (Exclusive)
#Incrimint
#so 3, -15, -3 i will go 3, 0, -3, -6, -9, -12

#APPEND AFFECTS THE ARGUMENT OUTSIDE THE FUNCTION

#TUPLE HAS NO FUNCTION APPEND OR EXTEND THEY RUN ERRORS
#YOU CAN SET A TUPLE TO ANOTHER TUPLE, NO PROBLEM AND IT WORKS
#YOU CAN ADD TUPLES !!!! IMPORTANT
#Multiplication of tuples.