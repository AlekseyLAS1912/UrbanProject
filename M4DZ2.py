def test_function():
    print('test_function')
    def inner_function():
        print('я в области видимости test_function')

    inner_function()

test_function()

