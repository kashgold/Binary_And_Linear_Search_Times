import time
import random
the_lengthy_number = 4

this_number = random.randint(1, the_lengthy_number)

the_other_numbers = list(range(1, the_lengthy_number + 1))

def O1010(the_other_numbers, this_number):
  guessed_num = False
  lower = 0
  upper = len(the_other_numbers)
  num_iter = 0
  while not guessed_num:
    num_iter +=1

    guess = round((lower+upper)/2)

    if guess < this_number:
      lower = guess
    elif guess > this_number:
      upper = guess
    elif guess == this_number:
      guessed_num = True
      break

  return guess, num_iter

start_time_binary = time.time()
snatched = O1010(the_other_numbers, this_number)[0]
end_time_binary = time.time()
print("Binary took: " + str(end_time_binary - start_time_binary))
print("\n\n")

def uh_linear_search(the_other_numbers, this_number):
  for i in the_other_numbers:
    if i == this_number:
      break
  return i

start_time_linear = time.time()
snatched = uh_linear_search(the_other_numbers, this_number)
end_time_linear = time.time()
print("Linear took: " + str(end_time_linear - start_time_linear))

print("\n\n")

linear_win = 0
binary_win = 0

two_empty_list = []
the_other_empty_list = []


for i in list(range(100)):
  this_number = random.randint(1, the_lengthy_number)

  the_other_numbers = list(range(1, the_lengthy_number + 1))

  start_time_binary = time.time()
  snatched = O1010(the_other_numbers, this_number)[0]
  end_time_binary = time.time()
  num_iter = O1010(the_other_numbers, this_number)[1]
  two_empty_list.append(num_iter)

  start_time_linear = time.time()
  snatched = uh_linear_search(the_other_numbers, this_number)
  end_time_linear = time.time()
  the_other_empty_list.append(snatched)

  binary = end_time_binary - start_time_binary
  linear = end_time_linear - start_time_linear

  if binary < linear:
    binary_win += 1
  elif binary > linear:
    linear_win += 1

the_blah_blah_blah = 0
not_so_silly_dummy_var = 0

for i in range(len(the_other_empty_list)):
  if two_empty_list[i] < the_other_empty_list[i]:
    the_blah_blah_blah += 1
  elif two_empty_list[i] > the_other_empty_list[i]:
    not_so_silly_dummy_var += 1

print("Binary Time Win: " +str(binary_win))


print("Linear Time Win: " +str(linear_win))

print("\n\n")

print("Binary Iteration Win: " +str(the_blah_blah_blah))


print("Linear Iteration Win: " +str(not_so_silly_dummy_var))
