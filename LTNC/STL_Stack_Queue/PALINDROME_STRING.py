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

import sys,string

class Stack:
    def __init__(self):
        self.a=[]
    def push(self,x): self.a.append(x)
    def pop(self): return self.a.pop()
    def empty(self): return not self.a

s=sys.stdin.read()
if not s:
    sys.exit()
t=[c.lower() for c in s if c.isalnum()]
st=Stack()
for c in t:
    st.push(c)
rev=[]
while not st.empty():
    rev.append(st.pop())
print("YES" if t==rev else "NO")