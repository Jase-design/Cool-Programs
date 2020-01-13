#This code basically returns a truth table based on the number of variables you choose to enter




def generatettrows(n):
    li=["f"]*n
    st=''.join(li)
    print(st)


    while st!=("t")*n:
        ind=st.rfind("f")
        li=list(st)
        li[ind]="t"

        while ind != n-1:
            li[ind+1] = "f"
            ind= ind+1


        st=''.join(li)
        print(st)
    input("press enter to exit")

print("enter number of variables")
num1=input()
num=int(num1)


generatettrows(num);

