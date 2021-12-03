with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
gamma = []
epsilon = []
binary = [2048,1024,512,256,128,64,32,16,8,4,2,1]

for i in range(0,12):
  one = 0
  zero = 0
  for line in lines:
    if(int(line[i]) == 0):
      zero += 1
    else:
      one += 1
  if(one > zero):
    gamma.append(1)
  else:
    gamma.append(0)

gamma_value = 0
for i in range(0,len(gamma)):
  gamma_value += binary[i] * gamma[i]

for g in gamma:
  if g == 0:
    epsilon.append(1)
  else:
    epsilon.append(0)

epsilon_value = 0
for i in range(0,len(epsilon)):
  epsilon_value += binary[i] * epsilon[i]

print("gamma: " + str(gamma) + " val: " + str(gamma_value))
print("epsilon: " + str(epsilon) + " val: " + str(epsilon_value))
print("3.1) value: " + str(gamma_value * epsilon_value))


lines_new =  lines
lines_new_new = []
oxygen = []

for i in range(0,12):
  one = 0
  zero = 0
  for line in lines_new:
    if(int(line[i]) == 0):
      zero += 1
    else:
      one += 1
  if(one >= zero):
    for line in lines_new:
      if int(line[i]) == 1:
        lines_new_new.append(line)
  else:  
    for line in lines_new:
      if int(line[i]) == 0:
        lines_new_new.append(line)
  if len(lines_new_new) == 1:
    oxygen = lines_new_new
    print("oxygen:" + str(lines_new_new))
  else:
    lines_new = lines_new_new
    lines_new_new = []


lines_new =  lines
lines_new_new = []
co2 = []

for i in range(0,12):
  one = 0
  zero = 0
  for line in lines_new:
    if(int(line[i]) == 0):
      zero += 1
    else:
      one += 1
  if(one < zero):
    for line in lines_new:
      if int(line[i]) == 1:
        lines_new_new.append(line)
  else:  
    for line in lines_new:
      if int(line[i]) == 0:
        lines_new_new.append(line)
  if len(lines_new_new) == 1:
    co2 = lines_new_new
    print("co2:" + str(lines_new_new))
    break
  else:
    lines_new = lines_new_new
    lines_new_new = []


oxygen_value = 0
co2_value = 0
for i in range(0,12):
  oxygen_value += binary[i] * int(oxygen[0][i])
  co2_value += binary[i] * int(co2[0][i])

print("3.2 value: " + str(oxygen_value * co2_value))