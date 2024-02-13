def print_params(a = 1, b ='строка', c = True):
     print(a, b, c)
print_params()

values_list=[12, 'Car', True]
values_dict = {
    'a' : 2,
    'b' : 'число',
    'c' : False
}
print_params(*values_list)
print_params(**values_dict)

valuse_list_2 = [23, False]
print_params(*valuse_list_2, '42')

