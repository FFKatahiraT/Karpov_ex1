def find_similar(numbers_set):
	period = len(numbers_set)
	similar=[]
	i=0
	counter = 0
	while i < len(numbers_set):
		num = numbers_set[i]
		del numbers_set[i]
		if num in numbers_set and num not in similar:
			similar.append(num)
		elif num in similar:
			period = counter
			break
		counter+=1
	return similar, period

def deduction_method_calc(x, a, c, m, quantity):
	for i in range(1, quantity):
		x.append((a*x[i-1]+c)%m)
	return x

def find_dividers(num):
	dividers=[]
	for i in range(2,num):
		if num%i==0:
			dividers.append(i)
	return dividers

def theorem1_first_condition(num1,num2):
	dividers1 = find_dividers(num1)
	dividers2 = find_dividers(num2)
	for divider in dividers1:
		if divider in dividers2:
			return False
	return True

def get_prime(size):
	prime_numbers = [1,2,3]
	if size>3:
		for i in range(3,size):
			for k in range(2,i):
				if i%k==0:	#not prime
					break
			else:
				prime_numbers.append(i)
	return prime_numbers

def theorem1_second_condition(a, m, prime_numbers):
	for i in range(1,len(prime_numbers)):
		p=prime_numbers[i]
		if m%p==0 and (a-1)%p==0:#(a-1)/p & m/p -- integers:
			return True 	
	return False
	
def theorem1_third_condition(a, m):
	if m%4==0:
		return True if (a-1)%4==0 else False
	return True

def check_theorem1(x,a,c,m, prime_numbers):
	quantity = 20
	x = deduction_method_calc(x,a,c,m,quantity)
	period = find_similar(x[:])[1]	#check similar values
	print('Theorem1:')
	print('c&m mutually prime:', theorem1_first_condition(c,m))
	print('(a-1)/p & m/p -- integers:', theorem1_second_condition(a,m,prime_numbers))
	print('(a-1)/4 -- int if m/4 -- int:', theorem1_third_condition(a,m))
	print(x, 'x')
	print(period, ' period\n')

def deduction_method():
	prime_numbers=get_prime(1000)
	check_theorem1([7],9,7,16, prime_numbers)
	check_theorem1([7],10,7,12, prime_numbers)
	check_theorem1([7],9,7,15, prime_numbers)
	check_theorem1([7],9,8,16, prime_numbers)
	# check_theorem1([7],9,7,12, prime_numbers)

deduction_method()