def check(move):
    if len(move) != 5:
        return 'ERROR'

    ch = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
    src, dst = move.split('-')

    if all([int(src[1]) % 9, int(dst[1]) % 9]):
        try:
            result = '{0}{1}'.format(
                abs(ch[src[0]] - ch[dst[0]]),
                abs(int(src[1]) - int(dst[1]))
            )
            if result in ('12', '21'):
                return 'YES'

            return 'NO'

        except KeyError:
            return 'ERROR'

    return 'ERROR'


print("Введіть комбінацію: ")
N = str(input())
print(check(N))
with open("Input.txt", "w") as file:
    file.write(N)
with open("Output.txt", "w") as file:
    file.write(check(N))
