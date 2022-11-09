def  fast_pow_iterative(m, n):
      if n == 1:
         return 1
      res = 1
      count = 0
      while res < n:
          res *= m
          count += 1
      return count
print fast_pow_iterative(4,3)
