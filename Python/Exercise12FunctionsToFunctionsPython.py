def greet(who="Colin"):
    print("Hello,", who)

greet()
greet(who="Kaggle")
greet("world")

def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    return fn(arg)

def squared_call(fn, arg):
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep='\n',
)