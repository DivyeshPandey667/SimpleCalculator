# Creating Tables
n=int(input("Which table do you want to print "))
for i in range(1,11):
    print(n," X ", i," = ",n*i)

    j=0
    while(j<10):
        j=j+1
        print(n," X ", j, " = ",n*j)