#Number to find primes before
n = 30

#First for loop to go through all numbers up to n
for i in range(2, n+1):

	#Second for loop to fo through all possible divisors of i
    for j in range(2, i):

    	#Check if i is divisible by j
        if i % j == 0:

        	#If so break
            break

    #If for statement completes properly, print i
    else:
        print i,