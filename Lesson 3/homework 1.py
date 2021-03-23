# Завдання 1-1:
# Эта программа считывает два числа и выводит их сумму:

a = int(input())

b = int(input())

c = int(input())

print(a + b + c)




# Завдання 1-2:
b = int(input())

h = int(input())

print ((b * h)/2)

# Выводите результат через print()




# Завдання 1-3:
# ділимо яблука.
n = int(input())

k = int(input())


print("Яблук кожному школяру: ", (k // n))

print("Яблук залишиться в кошику: ", (k % n))



# Завдання 1-4:
# Електронний годиннник
n = int(input())
print ((n // 60) % 24, ":", (n % 60))


# Завдання 1-5:
# Hello, Harry!

name = (input())
print ("Hello, " + name + "!")


# Завдання 1-6:
# наступне і попереднє
my_digit = int(input())
print ("Наступне число для числа", my_digit, " - це число ", (my_digit + 1))
print ("Попереднє число для числа", my_digit, " - це число ", (my_digit - 1))


# Завдання 1-7:
# парти для класів:
clas1 = int(input())
clas2 = int(input())
clas3 = int(input())
parta1 = (clas1 // 2) + (clas1 % 2)
parta2 = (clas2 // 2) + (clas2 % 2)
parta3 = (clas3 // 2) + (clas3 % 2)
print (parta1 + parta2 + parta3)



# Завдання 1-8:
# Довжина шнурка
a = int(input())
b = int(input())
l = int(input())
N = int(input())
print ((((N - 1) * (a + b) * 2) + a) + l * 2 )