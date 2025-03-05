expression = input().strip()

if '>' in expression:
    a, b = map(int, expression.split('>'))
    if a > b:
        print("Right")
    else:
        print("Wrong")

elif '<' in expression:
    a, b = map(int, expression.split('<'))
    if a < b:
        print("Right")
    else:
        print("Wrong")

elif '=' in expression:
    a, b = map(int, expression.split('='))
    if a == b:
        print("Right")
    else:
        print("Wrong")