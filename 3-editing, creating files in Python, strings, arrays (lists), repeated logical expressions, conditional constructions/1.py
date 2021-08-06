A = int(input("Введіть число A, яке закінчується на 5:"))
# Запис введенного числа в файл Input.txt
with open("Input.txt", "w") as file:
    file.write(str(A))
result = (A // 10) * (A // 10 + 1) * 100 + 25
# Запис результату в файл Output.txt
with open("Output.txt", "w") as file:
    file.write(str(result))
print("Квадрат числа = ", result)
