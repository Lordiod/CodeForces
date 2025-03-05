A, B = map(int, input().split())

floor_result = A // B
ceil_result = A // B if A % B == 0 else (A // B) + 1
round_result = int(A / B + 0.5) if A / B > 0 else int(A / B - 0.5)

print(f"floor {A} / {B} = {floor_result}")
print(f"ceil {A} / {B} = {ceil_result}")
print(f"round {A} / {B} = {round_result}")