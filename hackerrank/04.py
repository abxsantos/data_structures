strings = ["aba", "baba", "aba", "xzxb"]
queries = ["aba", "xzxb", "ab"]
appearance_list = []

for desired_element in queries:
    appearance_list.append(strings.count(desired_element))

print(appearance_list)
