import numpy


def bingo(field_,draws_,best_amount_draws_,last_draw_):
  number_draw = 0
  new_best = False
  for draw in draws_:
    number_draw += 1
    for row_ in range(0,5):
      for col_ in range(0,5):
        if field_[row_][col_] == draw:
          field_[row_][col_] = 100
          if numpy.array_equal(field_[0], numpy.array([100,100,100,100,100])) or numpy.array_equal(field_[1], numpy.array([100,100,100,100,100])) or numpy.array_equal(field_[2], numpy.array([100,100,100,100,100])) or  numpy.array_equal(field_[3], numpy.array([100,100,100,100,100])) or numpy.array_equal(field_[4], numpy.array([100,100,100,100,100])) or numpy.array_equal(field_[:,0], numpy.array([100,100,100,100,100])) or numpy.array_equal(field_[:,1], numpy.array([100,100,100,100,100])) or numpy.array_equal(field_[:,2], numpy.array([100,100,100,100,100])) or numpy.array_equal(field_[:,3], numpy.array([100,100,100,100,100])) or numpy.array_equal(field_[:,4], numpy.array([100,100,100,100,100])):
            if(best_amount_draws_ < number_draw):
              best_amount_draws_ = number_draw
              last_draw_ = draw
              new_best = True
            #print(field)
           # print("best_number_draw: " + str(best_number_draw_) + " number_draw: " + str(number_draw))
            return best_amount_draws_,last_draw_,new_best




draws = [4,77,78,12,91,82,48,59,28,26,34,10,71,89,54,63,66,75,15,22,39,55,83,47,81,74,2,46,25,98,29,21,85,96,3,16,60,31,99,86,52,17,69,27,73,49,95,35,9,53,64,88,37,72,92,70,5,65,79,61,38,14,7,44,43,8,42,45,23,41,57,80,51,90,84,11,93,40,50,33,56,67,68,32,6,94,97,13,87,30,18,76,36,24,19,20,1,0,58,62]

#fields = []
field = numpy.empty((5, 5)) 

row = 0
col = 0

best_field = [] #NUMBER OF BEST FIELD IN FIELDS ARRAY
best_amount_draws = 0 #AMOUNT OF DRAWEN NUMBERS FOR BEST FIELD
last_draw = 0 #LAST DRAWEN NUMBER OF BETS FIELD
new_best = False
with open("input.txt") as file:
  lines = file.readlines()
  for line in lines:
    if line == '\n':
      #fields.append(field)
      col = 0
      row = 0
      best_amount_draws, last_draw, new_best = bingo(field,draws,best_amount_draws,last_draw)
      if new_best == True:
        best_field = field
        print("NEW WORST FOUND: " + str(best_amount_draws))
        print("last drawn: " + str(last_draw))
        print(best_field)
      new_best = False
    else:
      for num in line.split(' '):
        if len(num.strip()) != 0 : 
          field[row][col] = int(num.strip())
          col += 1
      col = 0
      row += 1