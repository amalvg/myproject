dic1={1:'abc',2:'efgh',3:'qwerty'}
print(dic1)
print(dic1[1])
print(dic1.get(2,'not available'))
print(dic1.get(6,'not available'))
dic1[1]='hello'
print(dic1)
for x in dic1:
    print(x)
for x in dic1.values():
    print(x)
for x in dic1.items():
    print(x)
if 1 in dic1:
    print('availabe')
else:
    print('not available')
print(len(dic1))
dic1[4]='new'
print(dic1)
dic1.pop(1)
print(dic1)
dic1.popitem()
print(dic1)
del dic1[2]
print(dic1)
dic2=dic1.copy()
print(dic2)
mydic=dict(dic1)
print(mydic)
new=dict(a=1,b='car',c='19ab')
print(new)