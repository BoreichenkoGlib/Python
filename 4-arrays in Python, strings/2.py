a, b, c = map(int, input('A B C: ').split())
with open("Input.txt", "w") as file:
    file.write(str(a))
    file.write(" ")
    file.write(str(b))
    file.write(" ")
    file.write(str(c))
if a * b == c:
    print('YES')
    with open("Output.txt", "w") as file:
        file.write("Yes")
else:
    print('NO')
    with open("Output.txt", "w") as file:
        file.write("No")
