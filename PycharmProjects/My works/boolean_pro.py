# username='admin'
# password=1234
# if username=='admin' and password==1234:
#     print('you are logged in')
# else:
#     print('sorry....')
uname=str(input('enter your username '))
pword=str(input('enter your password '))
if uname=='admin' and pword=='1234':
    print('login successful')
else:
    print('invalid credential')