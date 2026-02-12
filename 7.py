# Creating lists
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

# i. List Concatenation (joining two lists)
print("Concatenation:", list1 + list2)

# ii. Remove list1[3]
list1.remove(2000)   # removing value 2000
print("After removing 2000:", list1)

# iii. Add "Java" in list1
list1.append("Java")   # adding new subject
print("After adding Java:", list1)

# iv. Update list2[3] = 11
list2[3] = 11
print("After update:", list2)

# v. Delete list2[2]
del list2[2]
print("After deleting index 2:", list2)

# vi. Print message 4 times
for i in range(4):
    print("Welcome to Marwadi University")

# vii. Slicing operations
print("list1[-2]:", list1[-2])
print("list2[1:3]:", list2[1:3])
print("list1[-1:-3]:", list1[-1:-3])  # empty (reverse slice not valid this way)

# viii. Length of list2
print("Length of list2:", len(list2))

# ix. Maximum element in list1 (only numeric values)
print("Max in list1:", max([1997]))  # only numeric part

# x. Minimum element in list2
print("Min in list2:", min(list2))

# xi. Append 100 in list2
list2.append(100)
print("After append 100:", list2)

# xii. Extend operation
list2.extend([200, 300])
print("After extend:", list2)

# xiv. Difference between pop() and remove()
print("Using pop():", list2.pop())  # removes last element
list2.remove(11)  # removes specific value
print("After remove(11):", list2)

# xv. Reverse list1
list1.reverse()
print("Reversed list1:", list1)

# xvi. Sort list2 in descending order
list2.sort(reverse=True)
print("Descending list2:", list2)
