# k-перша цифра, b-друга, t-третя
k = int(input("Введіть число К:"))
# Input.txt
with open("Input.txt", "w") as file:
    file.write(str(k))
b = 9
if k > 0 & k <= 9:
    t = b - k
    result = t + b * 10 + k * 100
    print("Різниця чисел = ", result)
    # Output.txt
    with open("Output.txt", "w") as file:
        file.write(str(result))
else:
    print("Помилка!")
