# Len is a function which is used to used to return the length
#Append size
def append_size(lst):
  lst.append(len(lst))
  return lst
print(append_size([23,42,108]))
#Append sum
def append_sum(lst):
  for lst2 in lst:
    lst.append(lst[-1] + lst[-2])
    if len(lst) == 6:
      return lst

#print sum
print(append_sum([1, 1, 2]))

#Larger list 
def larger_list(lst1, lst2): 
  if len(lst1) >= len(lst2):
    return lst1[-1]
  elif len(lst2) > len(lst1): 
    return lst2[-1]
  else:
    return lst1[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

# More than n function
def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False


print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

#Combine sort 
def combine_sort(lst1, lst2):
  unsorted = lst1 + lst2
  sorted_list = sorted(unsorted)
  return sorted_list

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))