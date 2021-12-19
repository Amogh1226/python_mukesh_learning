c = 40
d = 300

if d > c:
  print("d is greater than c")

#e = 100
#f = 300

#if f > e:
#print("f is greater than e")

g = 90
h = 90
if h > g:
  print("h is greater than g")
elif g == h:
  print("g and h are equal")

i = 900
j = 600
if j > i:
  print("j is greater than i")
elif i == j:
  print("i and j are equal")
else:
  print("i is greater than j")

k = 1000
l = 100
if l > k:
  print("l is greater than k")
else:
  print("l is not greater than k")

m = 900 
n = 400

if m > n: print("m is greater than n")

o = 9
p = 100

print("O") if o > p else print("O")

q = 100
r = 100

print("Q") if q > r else print("=") if q == r else print("R")

s = 100
t = 90
u = 900
if s > t and u > s:
  print("Both conditions are True")

v = 400
w = 200
x = 1000
if v > w or v > x:
  print("At least one of the conditions is True")

y =  80

if y > 10:
  print("Above ten,")
  if y > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

z = 90
a = 900

if a > z:
  pass

# having a empty if statement like this, would raise an error without the pass statement