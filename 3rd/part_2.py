total = 0
input_file = open("./parsed2")
for line in input_file.readlines():
    new_line = line.split(",")
    print(new_line)
    result = int(new_line[0])*int(new_line[1])
    total += result

print(total)
