from ast import While


A=int(input("ingrese el primer numero de 1-258:\n"))
B=int(input("ingrese el segundo numero de 1-258:\n"))
C=int(input("ingrese el tercer numero de 1-258:\n"))
D=int(input("ingrese el cuarto numero de 1-258:\n"))
E=int(input("ingrese el quinto numero de 1-258:\n"))
T=(A+B+C+D+E)/5
while T != 1:
    if T % 2==0:
        T=T/2
        print(T)
    else:
        T=(T*3)+1
        print(T)