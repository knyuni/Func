def fizz_buzz(number):

	if number%15 == 0: 
  		return "Fizz Buzz"

  	elif number%5==0:
  		return "Buzz"

  	elif number%3==0:

	   return "Fizz"
 	else:
 	 	return number
 	
a=45
print (fizz_buzz(a))