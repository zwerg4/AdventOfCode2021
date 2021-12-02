with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
horizontal = 0
depth = 0
aim = 0

for line in lines:
  if 'forward' in line:
    horizontal += int(line[-1])
  if 'down' in line:
    depth += int(line[-1])
  if 'up' in line:
    depth += - int(line[-1])
  
print("2.1) horizontal: " + str(horizontal) + " depth: "+ str(depth) + " result: " + str(horizontal*depth))

horizontal = 0
depth = 0
aim = 0
for line in lines:
  if 'forward' in line:
    horizontal += int(line[-1])
    depth += aim * int(line[-1])
  if 'down' in line:
    aim += int(line[-1])
  if 'up' in line:
    aim += - int(line[-1])
  
print("2.2) horizontal: " + str(horizontal) + " depth: "+ str(depth) + " aim: "+ str(aim) +" result: " + str(horizontal*depth))

