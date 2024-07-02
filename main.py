def max_num(a,b,c):
    return max([a,b,c])

def mult_list(lst):
  if len(lst) == 0:
    return 0
  prod = lst[0]
  if len(lst) > 1:
    for i in lst[1:]:
      prod = prod * i
  return prod

def rev_string(my_str):
    return my_str[::-1]

def num_within(x,a,b):
  return x in range(a,b+1)