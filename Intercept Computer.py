def snap(l):

    #This code checks for intercepts in any list, with a starting value and an end value
    

    le=len(l)
    inter=0

    for i in range(0,le-1):

        a=l[i][0]
        b=l[i][1]

        for k in range(i+1,le):

            c=l[k][0]
            d=l[k][1]

            if a>c or b>c:
                inter=inter+1

    return inter

l=[(30,40),(0,80),(60,150),(70,190)]
print(snap(l))




