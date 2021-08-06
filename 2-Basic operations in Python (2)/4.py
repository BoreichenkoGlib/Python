s = input()
sum1 = int(s[0]) + int(s[1]) + int(s[2])
sum2 = int(s[3]) + int(s[4]) + int(s[5])
if sum1 == sum2:
    print('Щасливий квиток')  # сума перших 3 чисел = сумі останніх 3 чисел
else:
    print('Звичайний квиток')  # все інше
