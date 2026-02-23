import time
def func_decorator(funk):
    def wrapper(*args, **kwargs):
        print('Делаем до функции')
        res=funk(*args, **kwargs)
        print('Делаем после функции')
        return res
    return wrapper

def some_funk(title,tag):
    print(f'Я функция - {title},tag - {tag}')
    return f'Я функция - {title},tag - {tag}'

some_funk = func_decorator(some_funk)
res=some_funk('Python навсегда','h1')
print(res)
def test_time(funk):
    def wrapper(*args, **kwargs):   
        st=time.time()
        res=funk(*args, **kwargs)
        et=time.time()
        dt=et-st
        print(f'Время работы функции {dt} секунд')
        return res
    return wrapper
@test_time
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
#Скорость работы разных функций


'''get_node = test_time(get_node)
res=get_node(2,100000)
print(res)'''

get_node(2,100000)