import time
def countdown(n):
    if n == 0:
        print ("Blast OFF")
    else:
        print(n)
        print('*'*n)
        time.sleep(1)
        countdown(n-1)

a=int(input("Enter The Limit"))
countdown(a)