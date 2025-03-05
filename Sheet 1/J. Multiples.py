x,y = input().split()

if int(y) % int(x) == 0 or int(x) % int(y) == 0:
    print("Multiples")
else:
    print("No Multiples")