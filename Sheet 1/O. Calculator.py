expression = input().strip()

if '+' in expression:
    A, B = map(int, expression.split('+'))
    print(A + B)
elif '-' in expression:
    A, B = map(int, expression.split('-'))
    print(A - B)
elif '*' in expression:
    A, B = map(int, expression.split('*'))
    print(A * B)
elif '/' in expression:
    A, B = map(int, expression.split('/'))
    print(A // B)