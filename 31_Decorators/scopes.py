# LEGB -> Local, Enclosed, Global, Built-in

x = 'global x'
def f1():
    # global x
    x = 'enclosed x'
    def f2():
        nonlocal x
        x = 'local x'
        print(x)
    f2()
    print(x)
    

f1()
print(x)