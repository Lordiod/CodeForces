a, b, c = map(int, input().split())

original_list = [a,b,c]
sorted_list = sorted(original_list)

for i in sorted_list:
    print(i)
    
print()

for i in original_list:
    print(i)