list_1 = []
list_2 = []

input_file = open("./input")
for line in input_file.readlines():
    new_line = line.split("   ")
    list_1.append(int(new_line[0]))
    list_2.append(int(new_line[1]))

# list_1.sort()
# list_2.sort()

total = 0

for location in list_1:
    total += location * list_2.count(location)

print(total)