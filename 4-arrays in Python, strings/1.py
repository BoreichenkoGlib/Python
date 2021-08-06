infile = open("Input.txt")
outfile = open("Output.txt", "w")

line = [int(x) for x in infile.readline().split()]

outfile.write(str(max(line)))

infile.close()
outfile.close()

# a = [int(input()) for i in range()]
# print(max(input().split(), key=int))
