from collections import defaultdict

with open("input.txt") as file:
    lines = file.readlines()

jellys_input = lines[0].split(',')
jellys = []
for jelly in jellys_input:
  jellys.append(int(jelly.strip()))

jellys_2 = defaultdict(int)
for x in jellys:
  jellys_2[int(x)] += 1  

for day in range(0,80):
  new_jellys = []
  for i in range(0,len(jellys)):
    if jellys[i] == 0:
      jellys[i] = 6
      new_jellys.append(8)
    else:
      jellys[i] -= 1
  jellys = jellys + new_jellys
print("6.1) day: " + str(day + 1) + " fishes: " + str(len(jellys)))
## TOO SLOW

for day in range(0, 256):
  temp = defaultdict(int)
  temp[6], temp[8] = jellys_2[0], jellys_2[0]
  for y in range(1, 9):
    temp[y - 1] += jellys_2[y]  
  jellys_2 = {k:v for k,v in temp.items()}
print("6.2) day: " + str(day + 1) + " fishes: " + str(sum(jellys_2.values())))


