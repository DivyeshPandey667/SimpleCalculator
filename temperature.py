#taking input from user
celcius=float(input("Write your temperature in celcius: "))
farhenite=(9/5)*celcius+32
print ("temperature in Farhenite ", farhenite)

if( farhenite >= 104):
    print("it is hot")
elif (farhenite>=50):
    print("it is cold")
else:
    print("soothing temperature")  