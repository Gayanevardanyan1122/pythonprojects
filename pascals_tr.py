def  pascal(n, m):
     """This function returns the member of pascal's triangle  """
    return 1 if m in (1, n) else pascal(m-1, n-1) + pascal(m-1, n)
print pascal(3, 4)
