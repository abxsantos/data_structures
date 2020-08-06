n = 10
queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]

initial_array = [0] * (n + 1)
for query in queries:
    a, b, k = query[0] - 1, query[1], query[2]
    initial_array[a] += k
    initial_array[b] -= k

max_value = 0
running_count = 0
for i in initial_array:
    running_count += i
    if running_count > max_value:
        max_value = running_count
print(max_value)


initial_array = [0] * n
k_arrays = [initial_array]
max_values = []
for querie in queries:
    a, b, k = querie[0] - 1, querie[1], querie[2]
    desired_array = initial_array[:]
    desired_array[a:b] = [k] * (b - a)
    k_arrays.append(desired_array)

summed_lists = [list(x + y for x, y in zip(k_arrays[0], k_arrays[1]))]

for index in list(range(len(k_arrays) - 2)):
    summed_lists.append(
        list(x + y for x, y in zip(summed_lists[index], k_arrays[index + 2]))
    )

max_values_list = []
for max_value in max(summed_lists):
    max_values_list.append(max_value)

print(max(max_values_list))
