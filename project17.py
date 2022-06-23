def sum(num1, num2, num3):
    """This function returns the sum of 3 umbers."""
    return num1 + num2 + num3
def map3(func, data1, data2, data3):
       """This function returns new list consist of the union of 3 lists."""
         res = [None] * len(data1)
         for ind in range(len(data1)):
              res[ind] = func(data1[ind], data2[ind], data3[ind])
         return res
      
print("the new list is:", map3(sum, data, data2, data3))
