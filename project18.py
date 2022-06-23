base = [10, 20, 30, 40, 50, 60, 70, 80, 90, 10]
exp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def map2(func, data1, data2):
     res = [None] * len(data1)
     for ind in range(len(data1)):
          res[ind] = func(data1[ind], data2[ind])
     return res
  
def pow(base, exp):
   if exp == 0 and base > 0:
       return 1
   if exp > 0 and base > 0:
       return base ** exp
   if base > 0 and exp < 0:
        return base ** (-exp)
   if base == 0 and  exp > 0:
        return 0
   if base == 0 and exp < 0:
        raise ValueException('the base can not be 0 if the base is negative number')
   raise ValuException("The base cant't be the negative number")

print("the new list is:", map2(pow, base, exp))
