if num < 0:
   print("no numbers")
elif num == 0:
   print("The factorial  0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
