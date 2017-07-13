def addition(a, b):
    print "%d plus %d:" % (a, b)
    return a + b

def subtraction(a, b):
    print "%d minus %d" % (a, b)
    return a - b

def multiplication(a, b):
    print "%d times %d" % (a, b)
    return a * b

def division(a, b):
    print "%d devide %d" % (a, b)
    return a / b

my_age = addition(20, 2)
my_salary = subtraction(1000, 1000)
my_bitcoin_wallet = multiplication(10, 10)
my_iq = division(100, 1)

print "my age is: %d, my salary is: %d, my bitcoins: %d, my_iq: %d" % (my_age, my_salary, my_bitcoin_wallet, my_iq)

weird_string = addition(my_age, subtraction(my_salary, multiplication(my_bitcoin_wallet, division(my_iq, 4))))

print "the result of that weird_string is: " + str(weird_string) + ". Insane, isn't it?"
