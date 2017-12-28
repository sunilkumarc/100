# https://www.interviewbit.com/problems/palindrome-integer/

'''
Determine whether an integer is a palindrome. Do this without extra space.

A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
Negative numbers are not palindromic.

Example :

Input : 12121
Output : 1

Input : 123
Output : 0
'''

def isPalindrome(A):
    bak = A
    mul = 1
    res = 0
    
    while A >= 10:
        mul *= 10
        A = int(A/10)
    
    A = bak
    
    while A > 0:
        digit = A % 10
        A = int(A / 10)
        res += digit * mul
        mul /= 10
        
    if res == bak:
        return 1
        
    return 0

if __name__ == '__main__':
    N = int(input().strip())
    res = isPalindrome(N)

    if res == 1:
        print(N, ': A palindrome')
    else:
        print(N, ': Not a palindrome')
