def func1(x):
    return x ** 2
def func2(x):
    return x % 2

my_numbers = [1, 2, 5, 8, 78, 93, 100, 45]

result = map(func1, filter(func2, my_numbers))
print(list(result))