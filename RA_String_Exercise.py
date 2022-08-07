# String Exercise
'''
Write a program to create a new string made of the middle three characters of an input string.
'''
input = '123456789'
res = input[len(input)//2-1:len(input)//2+2]
print(res)

'''
Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
'''
s1 = 'Aunt'
s2 = 'Sister'
s3 = s2[:len(s2)//2]+s1+s2[len(s2)//2:]
print(s3)

'''
Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
'''
s1 = 'America'
s2 = 'Japan'
res = s1[0]+s2[0]+s1[len(s1)//2]+s2[len(s2)//2]+s1[-1]+s2[-1]
print(res)

'''
Write a program to check if two strings are balanced.
For example, strings s1 and s2 are balanced if all the
characters in the s1 are present in s2.
The character’s position doesn’t matter.
'''

s1 = "Yna"
s2 = "PYnative"
print(set(s1)<=set(s2))

'''
Write a program to split a given string on hyphens and display first and last substring.
'''
str1 = 'Emma-is-a-data-scientist'
res =str1.split('-')
print(res[0]+', '+res[-1])


'''
Reverse a given string
Write a program to find the last position of a substring “Emma” in a given string.
'''
str1 = "Emma is a data scientist who knows Python. Emma works at google."
print(str1[::-1])
print('Last occurrence of Emma starts at index ',len(str1)-4-str1[::-1].find('ammE'))
