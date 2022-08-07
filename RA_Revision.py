# Revision for Numeric, String and Sequence Data Types

# Reverse the order of words in a given sentence.
str_val = "Hello World"
L = str_val.split()
L.reverse()
print(' '.join(L))


'''
Write a program  that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
'''
list1 = [10, 23, 23, 5, 67, 10]
res = list(set(list1))
print(res)

list2 = [list1[i] for i in range(len(list1)) if ((list1[i] in list1[:i]) == False)]
print(list2)


'''
Write a password strength verifier in Python that checks if user password is strong.
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
'''
PW = '1EggPerD@y'
PW = 'risto1#'

import string
L = string.ascii_lowercase
U = string.ascii_uppercase
D = string.digits
P = string.punctuation
C = [L,U,D,P]
sum1 = 0
for i in C:
    sum1 +=(set(PW) & set(i)) != set()
print('Yes' if sum1==4 else 'No')


'''
Write a program to reverse row sort in list of lists
'''
list_id = [[4,1,6], [7,9], [8,9,2,4]]
res = []
for i in list_id:
    i.reverse()
    res.append(i)
print(res)


'''
Write a program to pair elements with rear element in matrix row
'''
list1 = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
for i in range(len(list1)):
    j = list1[i]
    list1[i] = [[j[0],j[-1]],[j[1],j[-1]]]
print(list1)
    

'''
Replace each special symbol with # in the following string
Hint: import string, and use string.punctuation
'''
str1 = "%There &are three( students$ and& 1 trainer!"
res =''
for i in str1:
    if i in string.punctuation:
        res +='#'
    else:
        res += i
print(res)


'''
Remove all characters for string except integers
hint: list comprehension and isdigit()
'''
str1 = "My mum has a 10 year old dog and 2 fishes"
res = ''
for i in str1:
    if i in '0123456789':
        res +=i
print(res)


'''
Remove all empty strings from a list of strings
hint: use filter() => https://docs.python.org/3/library/functions.html#filter
'''
name_list = ['orange', None, 'pineapple', "", 'apples', 'mangoes','Hello Dear','', 'Hello Sir']
for i in name_list:
    if i !=None and len(i) == 0:
        name_list.remove(i)
print(name_list)