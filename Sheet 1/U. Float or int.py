x = float(input().strip())

if x.is_integer():
    print(f"int {int(x)}")
else:
    integer_part = int(x)
    decimal_part = x - integer_part
    print(f"float {integer_part} {decimal_part}")