# List Exercises

'''
Reverse a given list in python
'''
info = ['karl', '100', 'Red', 'Mangoes']
info.reverse()
print(info)


'''
Write a program to add two lists index-wise.
Create a new list that contains the 0th index item from both the list,
then the 1st index item, and so on till the last element.
any leftover items will get added at the end of the new list.
'''
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [list1[i]+list2[i] for i in range(min(len(list1),len(list2)))]
print(list3)

'''
Hint: use list comprehension with zip function
'''
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i+j for (i,j) in zip(list1, list2)]
print(list3)
print(' '.join(list3))



'''
Write a Python program to find the second largest number in the given list.
'''
list1 = [10, 20, 4]
list1.sort()
print(list1[-2])



'''
Concatenate two list
Hint: use list comprehension
<<new_list>> = [expression for item in list1 for y in list2]
'''

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
result = [x+y for x in list1 for y in list2]
print(result)


'''
Write a program to find value 20 in the list,
and if it is present, replace it with 200.
Only update the first occurrence of an item.
'''

list1 = [5, 10, 15, 20, 25, 50, 20]
res = [200 if i==20 else i for i in list1]
print(res)


'''
count number of occurrences of x in the given list
'''

lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10
print(lst.count(x))

'''
write a program to remove all occurrences of item 20
Hint: list comprehension
'''
list1 = [5, 20, 15, 20, 25, 50, 20]
list1 = [i for i in list1 if i!=20]
print(list1)


'''
Write a program to return the middle value of a list.
If there are 2 middle values, return the second
'''
age = [10, 3, 45, 67, 89.0, 45]
res = age[len(age)//2]
print(res)