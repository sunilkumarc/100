# http://www.geeksforgeeks.org/reverse-words-in-a-given-string/
# Example: Let the input string be “i like this program very much”.
# The function should change the string to “much very program this like i”

def reverseWord(string, start, end):
    while start < end:
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1

    return string

def reverse(string):
    string = list(string)
    start = 0
    end = start
    while end < len(string):
        end = start
        while end < len(string) and string[end] != ' ':
            end += 1

        string = reverseWord(string, start, end-1)
        start = end+1

    start = 0
    end = len(string)-1
    while start < end:
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1

    return ''.join(string)

if __name__ == '__main__':
    string = input().strip()
    print(reverse(string))
