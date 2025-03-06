A, S, B, Q, C = input().split()

A, B, C = int(A), int(B), int(C)

if S == '+':
    result = A + B
elif S == '-':
    result = A - B
elif S == '*':
    result = A * B

if result == C:
    print("Yes")
else:
    print(result)