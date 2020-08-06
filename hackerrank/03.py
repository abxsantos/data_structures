"""
Given  n = len(array)
and d, perform d left rotations on the array
"""

n = 5
d = 4
a = [1, 2, 3, 4, 5]
rotated_d_array = a[d:] + a[0:d]
print(str(rotated_d_array).strip("[]").replace(",", ""))
