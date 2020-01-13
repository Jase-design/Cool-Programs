def bin(num):

    q=num
    b=[]
    an=0

    while q!=1:

        if q%2==0:
            b.append(0)

        else:
            b.append(1)

        q=q//2


    b.append(1)
    #print(b)

    le = len(b)

    for i in range(0, le):

        z=10**i
        x=b[i]*z
        an=an+x


    return an





print("enter a decimal to be converted")
n=int(input())

print(bin(n))