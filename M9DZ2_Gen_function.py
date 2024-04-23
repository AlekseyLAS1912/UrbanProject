def function1(n):
    def function1_1(x):
        return x * n

    return function1_1

func1 = function1(n=5)
print(func1(x=6))

func2 = lambda x: x**2
print(func2(x = 5))

def function2(x):
    return x**2
print(function2(x = 5))

class Rect:
    def __init__(self, a, b):
        self.lenth = a
        self.width = b
    def __call__(self):
        return self.lenth * self.width

rect = Rect(a = 9, b = 6)
print(rect.__call__())