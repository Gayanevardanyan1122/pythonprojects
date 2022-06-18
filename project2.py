def  cubicrt(x):
    """This function calculates the cubic root of x number"""
 root = 1
 while not guess_enough(root, x):
    root= improve(root, x)
    return root
 def guess_enough(root, target):
  if abs(root**3-target)<0.00001
    return True
   else:
   return False
  def improve(root,target):
    return ((target / (root ** 2)) + (2 * root)) / 3 
 def abs(x):
 """this function returns whole part of a number"""
	if x > 0:
		return x
	else:
		return -x
 print("the cubic root is:", cubicrt(11))
