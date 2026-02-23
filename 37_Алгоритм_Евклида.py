import time
def get_node(a,b):
    '''Вычисляется НОД для двух натуральных чисел по алгоритму Евклида
    param а:первое натуральное число
    param b второе натуральное число
    return НОД
    '''
    while a !=b:
        if a>b:
            a -=b
        else:
            b -=a
    return a
def get_node_new(a,b):
    '''Вычисляется НОД для двух натуральных чисел по ,быстромуалгоритму Евклида
    param а:первое натуральное число
    param b второе натуральное число
    return НОД
    '''
    if a>b:
        a,b=b,a
    while b !=0:
           a,b=b,a%b
    return a


res=get_node(18,24)
print(res)
help(get_node)

def test_note(func):
    # -- тест 1
    a=28
    b=35
    res=func(a,b)
    if res == 7:
        print('test 1 passed')
    else:
        print('test 1 failed')
    # -- тест 2
    a=100
    b=1
    res=func(a,b)
    if res == 1:
        print('test 2 passed')
    else:
        print('test 2 failed')
    # -- тест 3
    a=2
    b=100000000
    
    st=time.time()
    res=func(a,b)
    et=time.time()
    dt=et-st
    if res == 2 and dt<1:
        print('test 3 passed')
    else:
        print('test 3 failed')
    print('time=',et-st)
test_note(get_node)
test_note(get_node_new)