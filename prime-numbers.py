def prime_numbers(count):
	n = 1000000
	i = 2
	result = []

	while i < n:
		flag = True


		for item in range(2, int(i**0.5)+1):
			if i % item == 0 and i != item: 
				flag = False
				break



			if flag:
				result.append(i)

		i += 1

print(result)



	
