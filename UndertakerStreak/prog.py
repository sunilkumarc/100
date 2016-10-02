N = int(input().strip())

for _ in range(N):
    num = int(input().strip())
    if (num%21 == 0):
        print("The streak is broken!")
    else:
        if "21" in str(num):
            print("The streak is broken!")
        else:
            print("The streak lives still in our heart!")
