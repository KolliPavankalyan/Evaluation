l1 = input("Enter names of person :").split()
l2 = input("Enter heigths").split()

l2_heights = [int(i) for i in l2]

results = dict(zip(l1,l2_heights))

sorted_dict = sorted(results.items(), key= lambda y:y[1],reverse=True)
names_as_per_heigth = []
for i in sorted_dict[::-1]:
    names_as_per_heigth.append(i[0])

print(names_as_per_heigth)


