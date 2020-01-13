#This program performs a run length encoding on a list of characters.
#If input is AAABBC output should be 3A2B1C


def amaz(txt):

    le=len(txt)
    count=0
    stck=[]
    final=[]
    i=0



    while i<le:

        temp=txt[i]
        count=1
        j=i+1


        if j<le:

            while j<le and temp==txt[j]:
                count=count+1
                j=j+1

        cnt=str(count)
        final.append(cnt)
        final.append(temp)
        i=j

    new = ""

    # traverse in the string
    for x in final:
        new += x

        # return string
    return new




txt="AAABBBCCC"
print(amaz(txt))




