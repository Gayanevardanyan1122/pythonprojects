def max(data):
   """ This function returns max member of list."""
   max1 = data[0]
   index = 1
   while index < len(data):
        if data[index] > max1:
            max1 = data[index]
        index += 1
    return max1
