import time
print('Гулятор by 4elovek')
print('Напишите число которое хотите гульнуть')
x = int(input())
while x >= 0:
    x=x-7
    y=x-7
    time.sleep(0.1)
    print(x,'- 7 =',y)
print('Я гуль')
