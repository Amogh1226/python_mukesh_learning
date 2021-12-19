a=60
if a>50 :
    print("This is the if body")
print("This is outside the if block")

i=23
if i%2==0:
    print("This is the if block")
    print("i is an even number")
else:
    print("This is the else block")
    print("i is an odd number")

c=50
if c<25:
    if c%2==0:
        print("c is an even number less than 25")
    else:
        print("c is an odd number less than 25")
else:
    print("c is greater than 25")

var="z"
if var=='a':
    print("This is the vowel a")
elif var=='e':
    print("This is the vowel e")
elif var=='i':
    print("This is the vowel i")
elif var=='o':
    print("This is the vowel o")
elif var=='u':
    print("This is the vowel u")
else:
    print("This is a consonant")

a=10
b=15
c=20
if (a>b) and (a>c) :
    print("the greatest number is a")
elif (b>a) and (b>c):
    print("The greatest number is b")
else:
    print("the greatest number is c")

aa=350
bb=250
cc=300
if (aa>bb) :
    print("%d is the greater than %d"%(aa,bb))
    if(aa>cc) :
        print("%d is the greatest number"%aa)
elif (bb>cc) :
    if(bb>aa) :
        print("%d is the greatest number"%bb)
else:
    print("%d is the greatest number"%cc)

d=7
count=0
if d%2==0:
    print("It is divisible by 2")
    count+=1
if d%3==0 :
    print("It is divisible by 3")
    count+=1
if d%5==0:
    print("It is divisible by 5")
    count+=1
if count==0 :
    print("The number is not divisible by 2,3 or 5")
