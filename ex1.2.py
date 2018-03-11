def is_palindrome(string):
  """
  check if a number is a palindrome
"""
  check=False
  if string==string[::-1]:
    check=True
  return check



def check_palindrome():
  """
  Runs through all 6-digit numbers and checks the mentioned conditions.
   The function prints out the numbers that satisfy this condition. 
   
   Note: It should print out the first number (with a palindrome in its last 4 digits), 
   not all 4 "versions" of it.
"""



  numbers=[]
  for i in range(100000,999999):
    num1=str(i)[-4::1]
    check=is_palindrome(num1)
    if check:
      num2=str(i+1)[-5::1]
      check=is_palindrome(num2)
      if check:
        num3=str(i+2)[1:4:1]
        check=is_palindrome(num3)
        if check:
          num4=str(i+3)
          check=is_palindrome(num4)
          if check:
            numbers.append(i)
  return numbers          
        
    
a=check_palindrome()
print(a)

  
  