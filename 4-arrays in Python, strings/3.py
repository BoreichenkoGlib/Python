from numpy import product

N = int(input("Введіть кількість чисел: "))
# Запис кількості чисел у перший рядок
with open("Input.txt", "w") as file:
    file.write(str(N))
    file.write("\n")
# Введення масиву чисел
arr = [int(input()) for i in range(N)]
# Запис масиву чисел у документ
for i in range(N):
    with open("Input.txt", "a") as file:
        file.write(str(arr[i]) + " ")
# Знаходження суми додатніх чисел, мінімального,максимального
sum = 0
for i in range(N):
    if arr[i] > 0:
        sum += arr[i]
print("сума = ", sum)
print("max = ", max(arr))
print("min = ", min(arr))
# Знаходження добутку чисел між мін і макс
# Знаходження індексу положення мінімального і максимального елементів у масиві
temp = arr.index(min(arr)), arr.index(max(arr))
# У випадку якщо індекс макс елемента менше чим мінімального або навпаки
left, right = min(temp) + 1, max(temp)
# поверне добуток чисел масиву із вказаного проміжку
multi = product(arr[left:right])
print("добуток = ", multi)
with open("Output.txt", "w") as file:
    file.write(str(sum))
    file.write(" ")
    file.write(str(multi))
file.close()
