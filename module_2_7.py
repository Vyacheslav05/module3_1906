# 1. Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()
print_params(10, 20, [1, 2])
print_params(10, 'строка2')
print_params(b=25) # работает
print_params(c = [1,2,3]) # работает

# 2. Распаковка параметров:
values_list = [1, 'Привет', [1, 2, 3]]
values_dict = {'a': 10, 'b': 'Hello', 'c': True}

print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
values_list_2 = [100, True]
print_params(*values_list_2, 42) # работает


