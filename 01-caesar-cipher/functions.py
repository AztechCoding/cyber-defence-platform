def greet(name):
    print("hello",name)
greet("Jerry")
greet("Tom")

def add_one(number):
    return number + 1

def add_two(number):
    return number + 2

def add(number, amount):
    return number + amount

result = add_one(8)
result_2 = add_two(15)
result_3 = add(12, 5)
print(result, result_2, result_3)