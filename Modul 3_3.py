def  print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(12, 'test', False)
print_params(12, 'test')
print_params(12)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [2, 'World', (1, 2, 4)]
values_dict = {'a': 3, 'b': 'Hello', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [5, 'Bye']
print_params(*values_list_2, 42)