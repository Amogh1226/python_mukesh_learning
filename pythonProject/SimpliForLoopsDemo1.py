#x = "amoghitschool"
#print(x[0],x[1],x[2])
#
#for i in x :
#    print(i, end='')

sum=0
for i in range(0,21,2) :
#    print(i)
    if i%2==0 :
        sum=sum+i
print(sum)

#1
#12
#123
#1234
#12345


#n= int(input("enter a number"))
#for i in range(1,n+1) :
#    for j in range(1,i) :
#        print(j,end='')
#    print()

#r=int(input("enter number of rows"))
#c = int(input("enter number of colomns"))
#X=[]
#val=[]
#for i in range(0,r) :
#    for j in range(0,c):
#        val.insert(j,int(input("enter the %d * %d element" %(i,j))))
#    X.insert(i,val)
#Y=[]
#for i in range(0,r) :
#    for j in range(0,c):
#        val.insert(j,int(input("enter the %d * %d element" %(i,j))))
#    Y.insert(i,val)
#    val=[]
#sum=[]
#
#for i in range(0,r):
#    for j in range(0,c):
#        val.insert(j, X[i][j]+ Y[i][j])
#    sum.insert(i,val)
#    val=[]
#print(sum)

stg= input("enter a string")
count=0
for i in range(0,len(stg)//2) :
    if stg[i]!= stg[len(stg)-1-i] :
        break
    count+=1
if count==len(stg)//2 :
    print("%s is a palindrome" %stg)
else:
    print("%s is not a palindrome" %stg)
