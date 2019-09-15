def my_function1():
    print("hello from a function")


def my_function2(fname):
    print(fname + " Refsnes")


def my_function3(country="Norway"):
    print("I am from " + country)


my_function1()
print('\n')
my_function2("Emil")
my_function2("Tobias")
my_function2("Linus")
print('\n')
my_function3("Sweden")
my_function3("India")
my_function3()
my_function3("Brazil")
