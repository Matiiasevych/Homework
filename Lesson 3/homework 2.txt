# Завдання 2-1:
# Мінімальне число

a = int(input())
b = int(input())
if a < b:
    print (a)
else: 
    print (b)


# Завдання 2-2:
# Sigh(x)
a = int(input())

if a > 0:
    print (1)
elif a < 0:
    print(-1)
else: 
    print (0)


# Завдання 2-3:
# Шахова дошка:

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a % 2 == 1 and b % 2 == 1) or (a % 2 == 0 and b % 2 == 0):
    x = "white"
else:
    x = "black"
if (c % 2 == 1 and d % 2 == 1) or (c % 2 == 0 and d % 2 == 0):
    y = "white"
else:
    y = "black"
if x == y:
    print ("Yes")
else:
    print ("No")


# Завдання 2-4:
# Високосний рік
year = int(input())

if year % 4 == 0 and year % 100 != 0:
    print ("Yes")
elif year % 400 == 0:
    print ("Yes")
else:
    print ("No")


# Завдання 2-5:
# Мінімум з трьох:
a = int(input())
b = int(input())
c = int(input())

if (a <= b and a <= c):
    print ("Найменше число: ", a)
elif (b <= a and b <= c):
    print ("Найменше число: ", b)
else:
    print ("Найменше число: ", c)
   

# Завдання 2-5:
# Співпадаючі:

a = int(input())
b = int(input())
c = int(input())

if a == b:
    if a == c:
        print(3)
    else:
        print(2)
elif a == c:
    print(2)
elif b == c:
    print(2)
else: 
    print(0)
  

# Завдання 2-6:
# Хід тури:
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a == c or b == d):
    print ("Yes")
else:
    print ("No")


# Завдання 2-7:
# Хід короля:
a = int(input())
b = int(input())
c = int(input())
d = int(input())
delta1 = a - c
delta2 = b - d
if delta1 < 0:
    delta1 = - delta1
if delta2 < 0:
    delta2 = - delta2
if delta1 < 2 and delta2 < 2:
    print ("Yes")
else:
    print ("No")

# Завдання 2-8:
# Хід слона:
a = int(input())
b = int(input())
c = int(input())
d = int(input())
delta1 = a - c
delta2 = b - d
if delta1 < 0:
    delta1 = - delta1
if delta2 < 0:
    delta2 = - delta2
if delta1 - delta2 == 0:
    print ("Yes")
else:
    print ("No")

# Завдання 2-9:
# Хід королеви:
a = int(input())
b = int(input())
c = int(input())
d = int(input())
delta1 = a - c
delta2 = b - d
if delta1 < 0:
    delta1 = - delta1
if delta2 < 0:
    delta2 = - delta2
if delta1 - delta2 == 0 or a == c or b == d:
    print ("Yes")
else:
    print ("No")


# Завдання 2-10:
# Хід коня:
a = int(input())
b = int(input())
c = int(input())
d = int(input())
delta1 = a - c
delta2 = b - d
if delta1 < 0:
    delta1 = - delta1
if delta2 < 0:
    delta2 = - delta2
if (delta1 == 2 and delta2 == 1) or (delta1 == 1 and delta2 == 2):
    print ("Yes")
else:
    print ("No")


# Завдання 2-11:
# Шоколад:
n = int(input())
m = int(input())
k = int(input())
a = k / n
a_int = a - int(a)
b = k / m
b_int = b - int(b)
if (a_int == 0 or b_int == 0) and n * m >= k and n + m > 2: 
    print("Yes")
else:
    print("No")


# Завдання 2-12:
# Басейн

n = int(input())
m = int(input())
x = int(input())
y = int(input())

lon = None
sho = None

if n < m:
    lon = m
    sho = n
else:
    lon = n
    sho = m
if x > y:
    x1 = lon - x
    y1 = sho - y
else:
    x1 = sho - x
    y1 = lon - y
if x1 < x:
    x = x1
if y1 < y:
    y = y1
if x < y:
    print(x)
else:
    print(y)