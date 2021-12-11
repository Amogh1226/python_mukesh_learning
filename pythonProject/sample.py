# stg='amoghitschool'
# print(stg)
#
# stg1="Tim's birthday"
# print(stg1)
#
# stg2= 'Tim said,"I\'m am busy today".'
# print(stg2)
#
# stg3= '''hey there!
# Welcome to amoghitschool'''
# print(stg3)
#
# stg4= "amoghitschool"
# for i in stg4:
#     print(i, end="")
#
# stg5="amoghitschool"
# print(stg5[0:5])
# print(stg5[:5])
# print(stg5[5:])
# print(stg5[2:5])
#
# stg6="Welcome to amoghitschool"
#
# print(stg6.upper())
# print(stg6.lower())
#
# print(stg6.find('m'))
# print(stg6.index('o'))
#
# x=stg6.split(" ")
# print(x)
#
# print(stg6.replace("amoghitschool","Python tutorial"))
#
# print(stg6.rpartition(" to "))
#
# stg7="good"
# stg8="morning"
# print(stg7+" "+stg8)
#
# stg9="Hey"
# stg10="there"
# stg11="all"
# stg12="{} {}, {}!".format(stg9,stg10,stg11)
# print(stg12)
#
stg13= input("Enter a sentence ")       #Welcome to amoghitschool
stg13=stg13+" "
temp=""
rev=""
for i in stg13:
    if i!=" ":
        temp=i+temp
    else:
        rev=rev+" "+temp
        temp=""
print(rev)
