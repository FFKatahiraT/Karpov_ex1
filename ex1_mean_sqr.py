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

mean_square_method()