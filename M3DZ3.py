def test(*args):
    print('Параметры:', args)
test(0, 12.5, 'slovo', True)


def test(n):
    if n == 1:
        return 1
    test_n_1 = test(n = n - 1)
    return n * test_n_1
print(test(18))