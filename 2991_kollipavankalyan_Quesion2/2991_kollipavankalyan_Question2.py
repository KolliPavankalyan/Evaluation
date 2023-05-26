given_input = input("enter a sentance :").split()
dict_a = {}
for i in given_input:
    i = i.lower()
    if i != 'a':
        if i == i[::-1]:
            if i in dict_a:
                dict_a[i]+=1
            else:
                dict_a[i]=1
count = 0
for i,v in dict_a.items():
    count += (v)
print(count)
