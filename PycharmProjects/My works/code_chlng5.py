def div():
    try:
        a=int(input('enter your 1st num'))
        b=int(input('enter your 2nd num'))
        print('the answer is',a/b)
    except:
        print('sorry cannot be divided by zero')
    finally:
        print('the answer is final')
div()