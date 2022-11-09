def  iterative(n):
tmp=2
     while n >= 3:
        tmp+= (tmp- 1) + (tmp- 2)
        n-=1
      return tmp
 print iterative(5)
