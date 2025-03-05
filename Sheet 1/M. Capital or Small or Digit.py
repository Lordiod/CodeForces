x = str(input())

if x.isdigit():
    print("IS DIGIT")
elif x.isalpha():
    print("ALPHA")
    if x.islower():
        print("IS SMALL")
    else:
        print("IS CAPITAL")