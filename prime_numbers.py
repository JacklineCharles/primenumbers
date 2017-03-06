def prime_numbers(n): #creates a function prime_numbers
    l = [] #initializes the list
    if type(n) is int:
    	if n < 0:
    		return []
    	elif n > 0:
    		for num in range(2, n+1):
    			if all(num % i != 0 for i in range(2, num)):
    				l.append(num)
    		return l
    else:
    	raise TypeError("use an integer ")
    
print(primes(20))
#prints all the prime numbers to the test number.
