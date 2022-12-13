# 2. Напишите программу, которая на вход принимает 5 чисел 
# и находит максимальное из них.
#     Примеры:
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# list = []
# for i in range(5):
#     num = int(input())
#     list.append(num)

# max = -99999999999999
# for i in range(len(list)):
#     if list[i] > max:
#         max = list[i]

# print("max = ", max)


print ('#1 :')
a= int (input())
print ('#2 :')
b= int (input())
print ('#3 :')
c= int (input())
print ('#4 :')
d= int (input())
print ('#5 :')
e= int (input())

max=a
if (a>max):
    max=a

if (b>max):
    max=b
    
if (c>max):
    max=c
 
if (d>max):
    max=d
   
if (e>max):
    max=e

print(f'max={max}')