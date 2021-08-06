a = int(input("Введіть кількість a: "))
b = int(input("Введіть кількість b: "))
c = int(input("Введіть кількість c: "))
d = int(input("Введіть кількість d: "))
with open("Input.txt", "w") as file:
    file.write(str(a)+" ")
    file.write(str(b)+" ")
    file.write(str(c)+" ")
    file.write(str(d))

k = 0
x = -100
for x in range(-100, 100):
    if a * x * x * x + b * x * x + c * x + d == 0:
        k += 1
        print("x", k, "=", x)
        with open("Output.txt", "a") as file:
            file.write(str(x) + " ")
if k == 0:
    print("Цілих коренів немає")
file.close()
