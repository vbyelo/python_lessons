def unique_names(names1, names2):
    s1 = set(names1)
    s2 = set(names2)
    # print(names1, type(names1), s1, type(s1))
    # print(names2, type(names2), s2, type(s2))

    return list(s1 | s2)

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia
