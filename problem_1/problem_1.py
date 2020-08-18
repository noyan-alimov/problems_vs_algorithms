def sqrt(number):
   """
   Calculate the floored square root of a number

   Args:
      number(int): Number to find the floored squared root
   Returns:
      int: Floored Square Root
   """
   try:
      int(number)
   except ValueError:
      return None

   if number < 0:
      return None
   
   if number == 0:
      return 0

   left = 1
   right = number

   while right > left + 1:
      mid = (right + left) // 2
      mid_square = mid * mid

      if mid_square > number:
         right = mid
      elif mid_square < number:
         left = mid
      else:
         return mid

   return left

print ("Pass" if  (None == sqrt(-9)) else "Fail")  # expect to return None because number is negative
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (None == sqrt('hello')) else "Fail")  # expect to return None because input is a string type
print ("Pass" if  (1 == sqrt(2)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")