empty_set = set()
number_set = {1, 2, 3, 3, 4, 5}
print(number_set)
# {1, 2, 3, 4, 5}
print(2 in number_set)
# True

odd_set = set()
even_set = set()
for number in range(10):
    if number %2:
        odd_set.add(number)
    else:
        even_set.add(number)
print(odd_set)
print(even_set)
# {1, 3, 5, 7, 9}
# {0, 2, 4, 6, 8}

union_set = odd_set | even_set
union_set = odd_set.union(even_set)
print(union_set)
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
intersection_set = odd_set & even_set
intersection_set = odd_set.intersection(even_set)
print(intersection_set)
# set()

difference_set = odd_set - even_set
difference_set = odd_set.difference(even_set)
print(difference_set)
# {1, 3, 5, 7, 9}

simmetric_difference_set = odd_set ^ even_set
simmetric_difference_set = odd_set.symmetric_difference(even_set)
print(simmetric_difference_set)
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

even_set.remove(2)
print(even_set)
# {0, 4, 6, 8}