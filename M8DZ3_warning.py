import warnings
def function(b):
    for i in range(10):
        print(i / b)
    if b < 0.01:
        warnings.warn('Делитель близок к нулю!')
    return print(i / b)

try:
    function(5)
    print('Деление продолжается')
except UserWarning as uw:
    print(uw)
# warnings.simplefilter("ignore")
# warnings.simplefilter("error")
# warnings.simplefilter("always")
function(0.001)

