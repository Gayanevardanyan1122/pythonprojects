def recursive(n):
return n if n>3 else recursive_func(n - 1) + recursive_func(n - 2) + recursive_func(n - 3)
print recursive(10)
