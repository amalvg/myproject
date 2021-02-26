dic={'apple':20000,'samsung':15000,'lenovo':16000,'asus':16500,
     'dell':14500,'hp':14000}
p=str(input('enter the product name'))
if p in dic:
    print('the price is',dic[p])
else:
    print('price not found')