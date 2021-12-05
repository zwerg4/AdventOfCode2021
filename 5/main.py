import numpy as np

x1 = []
y1 = []
x2 = []
y2 = []

lines = []
field = np.zeros((991, 991)) 
print(field.shape)

with open("input.txt") as file:
    lines = file.readlines()

for line in lines:
  split = line.split('->')
  c1 = split[0].split(',')
  c2 = split[1].split(',')
  x1.append(int(c1[0].strip()))
  y1.append(int(c1[1].strip()))
  x2.append(int(c2[0].strip()))
  y2.append(int(c2[1].strip()))

for i in range(0,len(x1)):
  if x1[i] == x2[i]:
    if y1[i] > y2[i]:
      for j in range(y2[i],y1[i]+1):
        field[x1[i],j] += 1
    else:
      for j in range(y1[i],y2[i]+1):
        field[x1[i],j] += 1
  if y1[i] == y2[i]:
    if x1[i] > x2[i]:
      for j in range(x2[i],x1[i]+1):
        field[j,y1[i]] += 1
    else:
      for j in range(x1[i],x2[i]+1):
        field[j,y1[i]] += 1
    
double = 0
for x_ in range(0,991):
  for y_ in range(0,991):
    if field[x_,y_] > 1:
      double += 1

print("5.1) doubles: " + str(double))

for i in range(0,len(x1)):
  if x1[i] < x2[i] and y1[i] < y2[i]:
    j = 0
    while x1[i]+j <= x2[i] and y1[i]+j <= y2[i]:
      field[x1[i]+j, y1[i]+j] += 1
      j += 1
  elif x1[i] > x2[i] and y1[i] > y2[i]:
    j = 0
    while x1[i] >= x2[i]+j and y1[i] >= y2[i]+j:
      field[x2[i]+j,y2[i]+j] += 1
      j += 1
  elif x1[i] > x2[i] and y1[i] < y2[i]:
    j = 0
    while x1[i] >= x2[i]+j and y1[i]+j <= y2[i]:
      field[x2[i]+j,y1[i]+j] += 1
      j += 1
  elif x1[i] < x2[i] and y1[i] > y2[i]:
    j = 0
    while x1[i]+j <= x2[i] and y1[i] >= y2[i]+j:
      field[x1[i]+j,y2[i]+j] += 1
      j += 1

double = 0
for x_ in range(0,991):
  for y_ in range(0,991):
    if field[x_,y_] > 1:
      double += 1

print("5.2) doubles: " + str(double))