numbers = []
for x in range(1,1000001):
    numbers.append(x)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd = []
for y in range(1,21):
    odd.append(y)
print(odd)

odd = [2*y  - 1 for y in range(1,11)]

print(odd)

for a in numbers[-3:]:
    print(f"The first three numbers are: ", a)