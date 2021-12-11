lst = [1,2,3,4,5,6,7,8,9,10]
tpl0 = tuple(lst)
tpl = (1,2,3,4,5,6,7,8,9,10)
s = 'Welcome to amoghitschool'

print(lst)
print(tpl)
print(s)

print('0 =', lst[0])
print('9 =', lst[9])
print('5 =', lst[5])
print('-1 =', lst[-1])

print(lst[-3])

print('[0:3] =', lst[0:3])
print('[3:10] =', lst[3:11])
print('[0:-1] =', lst[0:-1])
print('[0:] =', lst[0:])
print('[-3:-1] =', lst[-3:-1])
print('[:] =', lst[:])

print('[::2] =', lst[::2])
print('[::-2] =', lst[::-2])
print('[-2::-2] =', lst[-2::-2])
print('[::-1] =', lst[::-1])
print('tuple', tpl[::-1])
