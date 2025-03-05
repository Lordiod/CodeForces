x = int(input())

years = x // 365
remaining_days = x % 365
months = remaining_days // 30
days = remaining_days % 30

print(f"{years} years")
print(f"{months} months")
print(f"{days} days")