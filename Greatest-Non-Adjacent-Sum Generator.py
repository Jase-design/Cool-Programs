#This code generates the greatest sum of not adjacent numbers in the list

def air(l):

    le=len(l)
    max=0
    t=0


    for i in range(0,le):

        t=i


        temp=l[i]


        if max<l[i]:

            max=l[i]

        for j in range(0,le):




            if j!=i and j!=i+1 and j!=i-1 and j!=t and j!=t+1 and j!=t-1:

                temp=temp+l[j]

                t = j


                if temp>max:

                    max=temp







    return max





print(air([2,4,8,5]))



