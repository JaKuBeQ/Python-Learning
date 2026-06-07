#lists in python - table = []

list = [1,2,3,4,5]
list2 = ["apple", "banana", "Lime", "Apricot", "Blackberry"]
list3 = [True, False, True]
list4 = ["abc", 34, True, 40, "male"]
empty_lists = []

print(list, list2, list3, list4)
print(type(list3))

#lists functions

print(list[0], list2[-1]) # first and the last
print(len(list), len(list2)) # lenght
print(list[1:4], list2[0:2]) # range [x:y] x to y [x:] x to end [:y] all to y

if "apple" in list2:
    print("it's working")

list2[1] = "cherry"
print(list2) # changing the banana value to cherry

list2.insert(2, "peach") # adding new value to the 2 index before the lime
list2.append("orange") # adding new value to the end of the list
print("list before deleting fruits:", list2)
list2.pop(3)
list2.remove("Blackberry") # removes the specified item
print(list2)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical) #extending thislist by all of the tropical list value

print(thislist)

# list methods https://www.w3schools.com/python/python_lists_methods.asp