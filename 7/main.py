from collections import defaultdict

with open("input.txt") as file:
    lines = file.readlines()

start_pos_input = lines[0].split(',')
start_po = []
for pos in start_pos_input:
  start_po.append(int(pos.strip()))

positions = defaultdict(int)
for x in start_po:
  positions[int(x)] += 1

fuels = defaultdict(int)
for pos in range(1,2000):
  for key in positions:
     fuels[pos - 1] += positions[key] * abs(key-pos)

print("7.1) min fuel used for: " + str(min(fuels, key=fuels.get)) + " fuel is: " + str(fuels[ min(fuels, key=fuels.get)]))

fuels2 = defaultdict(int)
fuels3 = defaultdict(int)
for pos in range(1,2000):
  for key in positions:
    #with RANGE, SLOW!!!!
    fuels2[pos - 1] += positions[key] * sum(range(abs(key-pos)+1))
    #as GAUSSIAN SUM FORMULA, MUUUUUUUUUUUUUUCH faster
    fuels3[pos - 1] += positions[key] * (((abs(key-pos) +1) * abs(key-pos) )/2)

print("7.2) min fuel used for: " + str(min(fuels2, key=fuels2.get)) + " fuel is: " + str(fuels2[ min(fuels2, key=fuels2.get)]))