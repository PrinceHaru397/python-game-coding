# Sets in Python are a collection of unique elements. They are unordered and do not allow duplicate values. Sets are defined using curly braces {} or the set() function.

# Convert the list into a set
l1 = [1, 1, 2, 2, 3, 3]
s1 = set(l1)
print(s1)
# The output will be {1, 2, 3} because sets do not allow duplicate elements. When we convert the list l1 into a set, it automatically removes the duplicate values and only keeps the unique elements, which are 1, 2, and 3.

# You cannot access index in sets.
# print(s1[2])
# The above line will raise a TypeError because sets do not support indexing. Since sets are unordered collections, you cannot access elements using an index like you would with lists or tuples. To access elements in a set, you can use methods like iteration or membership testing instead.

# Checking if an element exists in the set
if 4 in s1:
    print(True)
else:
    print(False)
# The output will be False because the element 4 is not present in the set s1. The set s1 contains the elements {1, 2, 3}, and since 4 is not among these elements, the condition "4 in s1" evaluates to False, resulting in the else block being executed and printing False.

# Adding an element into the set
s1.add(4)
s1.add(5)
s1.add(6)
s1.add(7)
print(s1)
# The output will be {1, 2, 3, 4, 5, 6, 7} because we have added the elements 4, 5, 6, and 7 to the set s1. Since sets do not allow duplicate values, if any of these elements were already present in the set, they would not be added again. However, in this case, all the added elements are unique and will be included in the set, resulting in the final output of {1, 2, 3, 4, 5, 6, 7}.

# Removing an element from the set
s1.remove(2)
print(s1)
# The output will be {1, 3, 4, 5, 6, 7} because we have removed the element 2 from the set s1. The remove() method removes the specified element from the set. After removing 2, the remaining elements in the set are 1, 3, 4, 5, 6, and 7, which is reflected in the final output of {1, 3, 4, 5, 6, 7}.

# Union of two sets
a1 = {1, 2, 3, 4}
a2 = {12, 34, 56, 78}
print(a1.union(a2))
# Union means all the unique elements from both sets. In this case, the unique elements from a1 and a2 are 1, 2, 3, 4, 12, 34, 56, and 78, so the output will be {1, 2, 3, 4, 12, 34, 56, 78}.

# Intersection of two sets
a3 = {1, 2, 3, 4}
a4 = {3, 4, 5, 6}
print(a3.intersection(a4))
# Intersection means the common elements between two sets. In this case, the common elements between a3 and a4 are 3 and 4, so the output will be {3, 4}.

# Difference of two sets
a5 = {1, 2, 3, 4}
a6 = {3, 4, 5, 6}
print(a5.difference(a6))
# Difference means the elements that are present in one set but not in the other. In this case, the elements that are present in a5 but not in a6 are 1 and 2, so the output will be {1, 2}.

# Symmetric difference of two sets
a7 = {1, 2, 3, 4}
a8 = {3, 4, 5, 6}
print(a7.symmetric_difference(a8))
# Symmetric difference means the elements that are present in either of the sets but not in both. In this case, the elements that are present in either a7 or a8 but not in both are 1, 2, 5, and 6, so the output will be {1, 2, 5, 6}.