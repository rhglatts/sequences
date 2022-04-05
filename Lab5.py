#Rebecca Glatts
#Lab 5 


#Task 1: Strings
first = input("Enter first string: ")
second = input("Enter second string: ")
third = input("Enter third string: ")

list1 = [first, second, third]

#Finds the max character in the string using the max function
first_max = max(first)
second_max = max(second)
third_max = max(third)

print(f"Max of each string: {first_max} {second_max} {third_max}")

max_list = max(list1)
print("Max of the strings:", max_list)

#Adds a special character between the strings
concat = first + "#" + second + "#" + third
print(concat)

"""
Enter first string: Hello
Enter second string: You
Enter third string: Bye
Max of each string: o u y
Max of the strings: You
Hello#You#Bye

Enter first string: this
Enter second string: is
Enter third string: test
Max of each string: t s t
Max of the strings: this
this#is#test
"""

#Task 2: Lists
import random

L1 = []

#asks the user to input floats until they enter -, the stop character
while True:
    number = input("Enter a float, - to stop. ")
    if number == "-":
        break
    number = float(number)
    L1.append(number)

#creates a list of n float numbers
L2 = []
count = random.randint(1, 10)
for i in range(count):
    a = random.uniform(0, 100)
    L2.append(a)

#prints lists after generating them
print("Before\nL1: ", L1)
print("L2: ", L2)

#if L1 has more elements than L2, it appends every element in L2 to the end of L1

if len(L1) > len(L2):
    for i in L2:
        L1.append(i)
        
#if L1 has less than or equal to elements than L2, it inserts elements from L1 in between 
#elements of L2, starting at index 1

else:
    position = 1
    for i in L1:
        L2.insert(position, i)
        position += 2

#prints lists after appending/inserting numbers
print("After\nL1: ", L1)
print("L2: ", L2)


"""
Enter a float, - to stop. 10.2
Enter a float, - to stop. 20.1
Enter a float, - to stop. 15.2
Enter a float, - to stop. -
Before
L1:  [10.2, 20.1, 15.2]
L2:  [23.847435981128516, 39.69786988694119, 1.6166808660327492, 60.23109114941671, 
45.69324350147592, 3.5368522899341004, 78.37009465150784]
After
L1:  [10.2, 20.1, 15.2]
L2:  [23.847435981128516, 10.2, 39.69786988694119, 20.1, 1.6166808660327492, 15.2,
 60.23109114941671, 45.69324350147592, 3.5368522899341004, 78.37009465150784]


Enter a float, - to stop. 1
Enter a float, - to stop. 2
Enter a float, - to stop. 3
Enter a float, - to stop. -
Before
L1:  [1.0, 2.0, 3.0]
L2:  [18.981732908850546, 56.117280600228895, 74.43896418517774, 59.36487928296542, 
38.69465895893638, 92.75607451912036, 97.00860164619053, 38.95808079916693, 35.63965342172703]
After
L1:  [1.0, 2.0, 3.0]
L2:  [18.981732908850546, 1.0, 56.117280600228895, 2.0, 74.43896418517774, 3.0, 59.36487928296542,
 38.69465895893638, 92.75607451912036, 97.00860164619053, 38.95808079916693, 35.63965342172703]

"""

#Task 3: Tuples

#Splits the strings into characters in a tuple using the tuple() command
tuple1 = tuple(first)
tuple2 = tuple(second)
tuple3 = tuple(third)

#Iterates over the characters in the tuple and if the character matches a vowel, it adds to the count
count = 0
for i in tuple1:
    if i == 'a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or  'U':
        count += 1
    else:
        continue
print(f"Vowels in first string: {count}")

count = 0
for i in tuple2:
    if i == 'a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or  'U':
        count += 1
  
print(f"Vowels in second string: {count}")

count = 0
for i in tuple3:
    if i == 'a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or  'U':
        count += 1
print(f"Vowels in third string: {count}")

import copy

#changes the lists into tuples
L1 = tuple(L1)
L2 = tuple(L2)

#if the length of L1 is greater than L2, deepcopy L1 and change it to a list 
#so the original values arent affected, then iterate over the smaller list,
#adding the values from L2 to the values from 
if len(L1) > len(L2):
    temp = copy.deepcopy(L1)
    l3 = list(temp)
    index = 0
    for i in L2:
        l3[index] += i
        index += 1
#if length of L2 > L1 or L2 = L1, it copies L2 into l3 and iterates over L1, adding its index's
#values to l3
else: 
    temp = copy.deepcopy(L2)
    l3 = list(temp)
    index = 0
    for i in L1:
        l3[index] += i
        index += 1
#prints L3 which is the sum of L1 and L2
print("L3 (sum of L1 and L2): ", l3)
"""
Vowels in first string: 5
Vowels in second string: 3
Vowels in third string: 3
L3 (sum of L1 and L2):  [34.047435981128515, 30.3, 54.897869886941194, 
20.1, 1.6166808660327492, 15.2, 60.23109114941671, 45.69324350147592, 
3.5368522899341004, 78.37009465150784]

Vowels in first string: 4
Vowels in second string: 2
Vowels in third string: 4
L3 (sum of L1 and L2):  [19.981732908850546, 3.0, 59.117280600228895, 
2.0, 74.43896418517774, 3.0, 59.36487928296542, 38.69465895893638, 
92.75607451912036, 97.00860164619053, 38.95808079916693, 35.63965342172703]

"""