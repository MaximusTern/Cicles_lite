# Lite 1
id = 0
while id <6:
   print(id, '0000')
   id += 1


#Lite 2

k = 0
for i in range(10):
    num = int(input('Введи число: '))
    if num == 5:
        k += 1
print(k)3


#Lite 3
summ = 0
for i in range(1, 101):
    summ += i + 1
print(summ)

#Lite 4
fact=1
for i in range(1, 101):
    fact = fact*i
print(fact)

#Lite 5

number = 123456
number = str(number)
for char in number:
    print(char)
