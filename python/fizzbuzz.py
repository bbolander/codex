# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number
# and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.

for i in range(1, 100):
   div_3 = i % 3
   div_5 = i % 5
   if not div_3 and not div_5:
      print "FizzBuzz"
   elif not div_5:
      print "Buzz"
   elif not div_3:
      print "Fizz"
   else:
      print i
      
