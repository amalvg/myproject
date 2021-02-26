dic={'apple':200,'orange':300,'banana':400}
print(dic)
print(dic['apple'])
for i in dic:
    print(i)
for i in dic.values():
    print(i)
for i in dic.items():
    print(i)
dic['apple']=380
print(dic)
del dic['apple']
print(dic)
dic.popitem()
print(dic)