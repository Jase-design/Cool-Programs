# A fairly simple code that finds the "EDIT DISTANCE" between two strings.
#The edit distance is the least number of characters you need to change in order to convert one string to another


def edd(str1, str2):

    le1=len(str1)
    le2=len(str2)
    count=0


    if le1>le2:
        le=le2
        a=str1
        b=str2
        diff=le1-le2

    else:
        le=le1
        a = str2
        b = str1
        diff=le2-le1

    for i in range (0,le):

        if a[i]!=b[i]:
            count=count+1



    count=diff+count
    return count



str1="rig"
str2="fhpl"

#input(str1)
#input(str2)

print(edd(str1,str2))
print("enter to exit")

