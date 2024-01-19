print("donbale fibonachi")
a = 0
b = 1
while True:
    n = int(input("Enter your number: "))
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        print(a)
    elif n == 1: 
        print(b)
    else: 
        for i in range(2,n+1): 
                c = a + b 
                a = b 
                b = c 
                print(c)