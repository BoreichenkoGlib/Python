a = 0
arr = []
while a <= 100:  # поки менше 100
    a = int(input())
    if a > 100:  # якщо більше 100 то стоп
        break
    if a < 10:  # якщо менше то пропуск
        continue
    else:
        arr.append(a)
    print(a)
