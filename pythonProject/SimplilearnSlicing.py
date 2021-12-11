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

welcome = "Welcome to amoghitschool"
print(welcome[0])
print(welcome[11:])
print(welcome[::-1])

mySlice = slice(1,5,2)
print(lst)
print(lst[mySlice])

mySlice = slice(-1,-12,-1)
print(welcome[mySlice])

#program to search for a substring within a string using slice function

s=input("Enter a string ")
sub=input("Enter a substring ")
print(s.find(sub))

lstr = len(s)   #Length of string
lsub = len(sub)   #Length of substring
if lsub > lstr:
    print("Invalid substring")
    exit()
flag = True
for i in range(0,lstr-lsub+1):
    mySlice = slice(i,i+lsub) #extracting every substring of length of "sub" from str
    temps = s[mySlice]
    if temps==sub:
        flag = False
        print("Substring found at position ", i)
        break
if flag:
    print("substring not found")