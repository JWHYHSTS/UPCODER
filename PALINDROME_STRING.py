'''
A palindrome is a word, phrase, or number that is spelled the same forward and backward. For
example, "dad" is a palindrome; "A man, a plan, a canal: Panama" is a palindrome if you take out
the spaces and ignore the punctuation; and 1001 is a numeric palindrome.
We can use a stack to determine whether a given string is a palindrome. Implement a program to
determine whether an input is palindrome.  
Note: the character is not a alphanumeric will be ignored.

Input: the string s
Output: print YES if s is a palindrome string; otherwise print NO
'''

def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    stack = []
    for c in cleaned:
        stack.append(c)
    return cleaned == ''.join(reversed(stack))

s = input()
if is_palindrome(s):
    print("YES")
else:
    print("NO")