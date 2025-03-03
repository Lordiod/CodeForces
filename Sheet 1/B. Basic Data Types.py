i, l, c, f, d = input().split()
i = int(i)
l = int(l)
c = str(c)
f = float(f) # Float (32-bit)
d = float(d) # Double (64-bit, but float in Python handles both)

print(i)
print(l)
print(c)
print(f"{f:.2f}")  # Print float with 2 decimal places
print(f"{d:.1f}")  # Print double with 1 decimal place