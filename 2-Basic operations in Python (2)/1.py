A = float(input())
B = float(input())
C = str(input())
if C == '+':
    print(A + B)
elif C == '-':
    print(A - B)
elif C == '*':
    print(A * B)
elif C == '/' and B == 0:
    print("Діл на 0!")
elif C == '/':
    print(A / B)
elif C == 'mod' and B == 0:
    print('Діл на 0!')
elif C == 'mod' and B != 0:
    print(A % B)
elif C == 'pow':
    print(A ** B)
elif C == 'div' and B == 0:
    print('Діл на 0!')
elif C == 'div' and B != 0:
    print(A // B)
