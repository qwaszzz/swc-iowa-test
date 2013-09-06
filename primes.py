for i in range(4,101):
    number="prime"
    for j in range (2,i):
        if (i%j==0):
            number="nonprime"
    print i, number
        
