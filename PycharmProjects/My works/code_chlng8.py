# odd=[i for i in range(100) if i%2!=0]
# print(odd)

# odd=list(range(1,100,2))
# print(odd)

odd=[]
for i in range(1,100):
    if i%2!=0:
        odd.append(i)
print(odd)