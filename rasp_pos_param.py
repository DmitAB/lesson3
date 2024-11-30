def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print()
print_params('СТРОКА', 99 )
print()
print_params(b = 25)
print_params(c = [1,2,3])
print('-----------------------------')

values_list = ['one', 'Ту', 3]
values_dict = {'a':555, 'b':False, 'c':'three'}
print_params(*values_list)
print_params(**values_dict)
print()
# Я так понял, что можно ещё отдельно брать и из списка и из словаря:
print_params(values_list[0], values_dict['b'], values_dict['c'])
print('----------------------------')
values_list_2 = ['один', '22']
print_params(*values_list_2,42)