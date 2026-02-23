def say_name(name):
    def say_goodbye():
        print('Dont say good bye, '+ name+ '!')
    return say_goodbye

f=say_name('Alex')
f2=say_name('Python')
f() 
f2() 

def counter(start=0):
    def step():
        nonlocal start
        start+=1
        return start
    return step

c=counter(2)
print(c())
print(c())
print(c())
c1=counter()

def strip_string(strip_chars=" "):
    def do_strip(string):
        return string.strip(strip_chars)
    return do_strip

strip1=strip_string()

strip2=strip_string('! ')
print(strip1('dfgadfg!'))
print(strip2(' dfgadfg!'))