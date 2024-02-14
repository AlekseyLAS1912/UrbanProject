def test(a = 12, b = 'slovo', c = True):
    print(a, b, c)
test()

def test(n):
    if n == 1:
        return 1
    test_n_1 = test (n = n - 1)
    return n * test_n_1
print(test(18))