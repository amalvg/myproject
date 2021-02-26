# def square():
#     for i in range(10):
#         print(i*i)
# square()
# li=[i*i for i in range(10)]
# print(li)

# letters=[]
# for i in 'amal':
#     letters.append(i)
# print(letters)
# letters=[i for i in 'amal']
# print(letters)

# even=[]
# for i in range(10):
#     if i%2==0:
#         even.append(i)
# print(even)
# even=[i for i in range(10) if i%2==0]
# print(even)

li=[1,4,5,6,8]
even=[i*i for i in li if i%2!=0]
print(even)