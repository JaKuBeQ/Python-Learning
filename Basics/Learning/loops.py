#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

a = 5
b = 11

#if
if b > a:
    print("b is greater than a")

if b == 9:
    print("b is a 9")
elif b == 10:
    print("b is a 10")
else:
    print("b is not a 9 or 10")

#while
print("while example:")
i = 1
while i < 6:
  print(i)
  i += 1

print("continue example:")

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

print("break example:")
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1