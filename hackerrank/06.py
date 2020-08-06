
a = [11, 6, 1, 13, 14, 7, 8, 10, 3, 17, 7, 18, 6, 4, 5, 13, 17, 4,16,9, 17, 16, 12, 6, 7]
b = [10, 15, 13, 17, 10, 7, 0, 16, 8, 13, 11, 8, 14, 13]
constraint_sum = 55

def two_stacks(constraint_sum, a, b):
    list_a = a[::-1]
    list_b = b[::-1]
    removed_integers = []
    while sum(removed_integers) < constraint_sum:
        if len(list_a) > 0 and len(list_b) > 0:
            if list_a[-1] > list_b[-1]:
                removed_integers.append(list_b.pop())
            else:
                removed_integers.append(list_a.pop())
        elif len(list_a) == 0 and len(list_b) == 0:
            return len(removed_integers)
        elif len(list_a) == 0 and len(list_b) > 0:
            removed_integers.append(list_b.pop())
        elif len(list_b) == 0 and len(list_a) > 0:
            removed_integers.append(list_a.pop())

    if sum(removed_integers) > constraint_sum:
        removed_integers.pop()
    return len(removed_integers)


print(two_stacks(constraint_sum, a, b))