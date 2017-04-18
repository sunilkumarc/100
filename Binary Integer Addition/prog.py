# Introduction to Algorithms - 2.1-4 (Page No : 22)

a = [1, 0, 1, 1]
b = [1, 1, 1, 1]

a1 = int(''.join(list(map(str, a))), 2)
b1 = int(''.join(list(map(str, b))), 2)
print("Expected - ", a1+b1)
c = []

carry = 0
for i in reversed(range(len(a))):
    sum = a[i] + b[i] + carry
    if sum == 1 or sum == 0:
        c.append(sum)
    else:
        carry = 1
        c.append(sum-2)

if carry == 1:
    c.append(carry)

c.reverse()
print("Actual - ", int(''.join(map(str, c)), 2))
