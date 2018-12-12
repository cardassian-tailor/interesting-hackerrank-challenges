'''

challenge in question
https://www.hackerrank.com/challenges/string-validators/problem

ou are given a string .
Your task is to find out if the string

contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string

.

Constraints

Output Format

In the first line, print True if
has any alphanumeric characters. Otherwise, print False.
In the second line, print True if has any alphabetical characters. Otherwise, print False.
In the third line, print True if has any digits. Otherwise, print False.
In the fourth line, print True if has any lowercase characters. Otherwise, print False.
In the fifth line, print True if has any uppercase characters. Otherwise, print False. 
'''

s = input()

print(any(letter.isalnum() for letter in s))
print(any(letter.isalpha() for letter in s))
print(any(letter.isnumeric() for letter in s))
print(any(letter.islower() for letter in s))
print(any(letter.isupper() for letter in s))
