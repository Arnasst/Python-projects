a = input()
s = str(a)
first = 1
for letter in s:
    if letter == '6' and first == 1:
        letter = '9'
        first = 0
    print(letter, end = '')
print()

""" kazkodel neveikia
for i in range(len(s)):
    if s[i] == '6':
        s[i] = '9'
        break
print(a)
"""
        