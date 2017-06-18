def swap(string):
    words = []
    j = 0
    for i in range(len(string)):
        if string[i] == ' ':
            words.append(string[j:i])
            j = i+1
    words.append(string[j:len(string)])

    length = len(words)
    for i in range(int(length/2)):
        words[i], words[length-i-1] = words[length-i-1], words[i]

    return " ".join(words)

T = int(input().strip())

for _ in range(T):
    string = input().strip()
    print(swap(string))