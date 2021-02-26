def weight():
    w=int(input('enter the weight in kg'))
    return w
def height():
    h=float(input('enter the height in mtrs'))
    a=h*h
    return a
def bmi():
    x=weight()/height()
    return x
print('your BMI is',bmi())
# bmi=weight()/height()
# print('your BMI is', bmi)