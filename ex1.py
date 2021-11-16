import matplotlib.pyplot as plt

def mean_square_method_calc(number):
	number=str(number**2)
	if len(number)<8:
		add_zeros = 8-len(number)
		number = '0'*add_zeros+number
	av = len(number)//2
	output = number[av-2:av+2]
	return int(output)

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

def mean_square_method():
	max_period, max_j, max_random_numbers = [0], [0], []
	periods_list = []
	for j in range(1,10000):
		period = 0
		random_numbers = []
		random_number = j

		while period == len(random_numbers):	#looking for period
			random_number = mean_square_method_calc(random_number)	#generate random number
			random_numbers.append(random_number)	#store it
			period = find_similar(random_numbers[:])[1]	#check similar values

		periods_list.append(period)

		if period > max_period[0]:	#find max period
			max_period = [period]
			max_j = [j]
			max_random_numbers = [random_numbers]
		elif period == max_period[0]:
			max_period.append(period)
			max_j.append(j)
			max_random_numbers.append(random_numbers)

	print(max_random_numbers)
	print(max_period, ' max period')
	print(max_j, 'number providing the max period')

	plt.scatter(range(len(periods_list)), periods_list, s=5)
	plt.title('random seed generator length distribution')
	plt.ylabel('Period')
	plt.xlabel('Initial number')
	plt.grid()
	plt.savefig('length_distribution.png')
	plt.show()

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

def max_length_seq_calc(m, l):
	step = 0
	running = 1
	x = []
	x.append([])
	for i in range(m):
		x[step].append(1)
	while running:
		x.append([])
		for i in range(m):
			x[step+1].append(1)
		x[step+1][0] = int(x[step][l-1]!=x[step][m-1])
		for i in range(m-1):
			x[step+1][i+1] = x[step][i]	
		if x[0]==x[step+1]:
			running=False
		step+=1
	print(step, ' period')	
	for i in range(len(x)):
		print(x[i])
	return step

def max_length_seq():
	m=20
	periods_list = []
	for l in range(1,m):
		periods_list.append(max_length_seq_calc(m,l))
	plt.plot(range(1,m), periods_list)
	plt.title('max length sequence distribution')
	plt.ylabel('Period')
	plt.xlabel('l')
	plt.grid()
	plt.savefig('max_length_seq_distribution.png')
	plt.show()

# mean_square_method()
# deduction_method()
max_length_seq()