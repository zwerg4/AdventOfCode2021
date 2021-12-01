with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

increased = 0
for i in range(1,len(lines)):
  if(lines[i-1] < lines[i]):
    increased+=1

print("1.1) " + str(increased))

increased = 0
for i in range(3,len(lines)):
  if((lines[i-3] + lines[i-2] + lines[i-1]) < (lines[i-2] + lines[i-1] + lines[i]) ):
    increased+=1

print("1.2) " + str(increased))