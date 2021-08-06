N = int(input("Введіть N-кількість днів:"))
# arr = list(range(1, 31, 31 // N))
a = [int(input()) for i in range(N)]
# Input.txt
# запис кількості днів
with open("Input.txt", "w") as file:
    file.write(str(len(a)) + "\n")
# запис масиву днів через пробіл
for i in range(N):
    with open("Input.txt", "a") as file:
        file.write(str(a[i]) + " ")
# дні коли отримав 3
x = 0
y = 0
for i in range(N):
    if a[i] % 2 != 0:
        x = x + 1
        with open("Output.txt", "w") as file:
            file.write(str(a[i]) + " ")
with open("Output.txt", "a") as file:
    file.write("\n")
# дні коли отримав 4
for i in range(N):
    if a[i] % 2 == 0:
        y = y + 1
        with open("Output.txt", "a") as file:
            file.write(str(a[i]) + " ")
with open("Output.txt", "a") as file:
    file.write("\n")
    file.close()
    # чи оримає він 4 бали
    if x <= y:
        print("Yes")
        with open("Output.txt", "a") as file:
            file.write("Yes")
    else:
        print("NO")
        with open("Output.txt", "a") as file:
            file.write("No")
