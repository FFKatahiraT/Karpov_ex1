import matplotlib.pyplot as plt
from random_methods import *

def calc_hi(num, num_theor):
	hi_sqr = 0
	for i in range(len(num)):	#calc hi_sqr criteria
		hi_sqr+=(num[i] - num_theor)**2/num_theor
	return hi_sqr

def frequency_test(rand, method):
	k=100
	N=10**5
	num=[]
	num_theor=[]
	for i in range(k+1):	#init 
		num.append(0)
		num_theor.append(N/k)
	for i in range(N):
		num[int(rand.random(0,k))] += 1	#add a point to the value that we get here
	x=[]
	for i in range(k+1):	#init x axis
		x.append(i/k)
	hi_sqr = calc_hi(num, N/k)

	print(hi_sqr, 'hi_sqr', method)
	plt.plot(x, num, label='Experiment')
	plt.plot(x, num_theor, color='green', label='Theoretical')
	plt.title('Frequency test: '+method+'. k='+str(k)+', N='+str(N))
	plt.legend(loc='best')
	plt.ylabel('Number of operations')
	plt.xlabel('Value')
	plt.grid()
	plt.savefig('frequency_test_'+method+'.png')
	plt.close()

def serial_test(rand, method):
	d = 10
	N = 10**5
	u, z = [], []
	for i in range(N):
		u.append(int(rand.random(0,d)))
	i = 0
	while i < N:
		z.append(int(str(u[i])+str(u[i+1])))
		i += 2

	hi_sqr = calc_hi(z, N/200)

	print('serial test', method, 'hi_sqr:', round(hi_sqr,2))

def poker_test(rand, method):
	d = 10
	N = 10**5
	u, z = [], []
	hi_sqr = 0
	for i in range(N):
		u.append(int(rand.random(0,d)))
	i = 0
	while i < N:	#generate numbers
		z.append([])
		for j in range(5):
			z[i//5] += str(u[i+j])
		# print(z[i//5])
		i += 5
	cases=[0,0,0,0,0,0,0]	# 7 poker test cases
	for i in range(len(z)):
		coincidences = []
		for j in range(len(z[i])):
			coincidences.append(0)
			for k in range(len(z[i])):
				if z[i][j] == z[i][k]:
					coincidences[j] += 1
		# print(coincidences, 'coincidences')
		if sum(coincidences) == 5:	#add cases
			cases[0] += 1
		elif sum(coincidences) == 7:
			cases[1] += 1
		elif sum(coincidences) == 9:
			cases[2] += 1
		elif sum(coincidences) == 11:
			cases[3] += 1
		elif sum(coincidences) == 13:
			cases[4] += 1
		elif sum(coincidences) == 17:
			cases[5] += 1
		elif sum(coincidences) == 25:
			cases[6] += 1
	
	for i in range(len(z)):	#str to int
		num = ''
		for j in range(len(z[i])):
			num += (z[i][j])
		z[i] = int(num)
	hi_sqr = calc_hi(z, N/500000)	#calc hi

	sum_cases = sum(cases)
	for i in range(len(cases)):	#calc probabilities of cases
		cases[i] /= sum_cases

	P_theor = [0,0,0,0,0,0,0]
	P_theor[0] = (d-1)*(d-2)*(d-3)*(d-4)/d**4
	P_theor[1] = 10*(d-1)*(d-2)*(d-3)/d**4
	P_theor[2] = 15*(d-1)*(d-2)/d**4
	P_theor[3] = 10*(d-1)*(d-2)/d**4
	P_theor[4] = 10*(d-1)/d**4
	P_theor[5] = 5*(d-1)/d**4
	P_theor[6] = 1/d**4

	P_xlabel=[]
	for i in range(len(P_theor)):
		P_xlabel.append(r'$P_'+str(i+1)+r'$')
	print(hi_sqr, 'hi_sqr', method)
	plt.plot(P_xlabel, cases, label='Experiment')
	plt.plot(P_xlabel, P_theor, color='green', label='Theoretical')
	plt.title('Poker test: '+method+'. d='+str(d)+', N='+str(N))
	plt.legend(loc='best')
	plt.ylabel('Probability')
	plt.grid()
	plt.savefig('Poker_test_'+method+'.png')
	plt.close()
	
def monotony_check(rand, method):
	d = 10
	N = 10**4
	u, monotony = [], []
	hi_sqr = 0
	for i in range(N):
		u.append(int(rand.random(0,d)))

	sequence = 1
	for j in range(N-1):
		if u[j+1] <= u[j]:
			monotony.append(sequence)
			sequence = 1
		else:
			sequence += 1
	monotony.append(sequence)
	omega = [0,0,0,0,0,0]
	for j in range(len(omega)):
		for i in range(len(monotony)):	#calc number of similar intervals	
			if monotony[i] == j+1:
				omega[j] += 1
			elif monotony[i] > 6:
				omega[len(omega)-1] += 1
	a = []
	a.append([4529.4, 9044.9, 13568, 18091, 22615, 27892])	#t,exbq a coefficient
	a.append([0, 18097, 27139, 36187, 45234, 55789])
	a.append([0, 0, 40721, 54281, 67852, 83685])
	a.append([0, 0, 0, 72414, 90470, 111580])
	a.append([0, 0, 0, 0, 113262, 139476])
	a.append([0, 0, 0, 0, 0, 172860])
	b = [1/6, 5/24, 11/120, 19/720, 29/5040, 1/840]
	summ = 0
	for i in range(len(omega)):
		for j in range(len(omega)):
			summ += (omega[i]-N*b[i])*(omega[j]-N*b[j])*a[i][j]
	V = summ/N
	print(V, 'V', method)

def correlation_test(rand, method):
	d = 10**3
	N = 10**4
	x, y = [], []
	hi_sqr = 0
	for i in range(N):
		x.append(int(rand.random(0,d)))
		y.append(int(rand.random(0,d)))
	summ_xy, summ_x_sqr, summ_y_sqr = 0, 0, 0
	for i in range(N):
		summ_xy += x[i]*y[i]
		summ_x_sqr += x[i]**2
		summ_y_sqr += y[i]**2
	R = (N*summ_xy - sum(x)*sum(y))/((N*summ_x_sqr - sum(x)**2)*(N*N*summ_y_sqr - sum(y)**2))**0.5
	R_min = -1/(N-1) - 2/(N-1)*(N*(N-3)/N+1)**0.5
	R_max =  1/(N-1) + 2/(N-1)*(N*(N-3)/N+1)**0.5
	if R_min < R < R_max:
		print('correlation_test passed, R=', R)
	else:
		print('correlation_test failed, R=', R)


frequency_test(max_length_sequence(), 'max length sequence')
frequency_test(deduction_method(), 'deduction method')
frequency_test(mean_sqr_method(), 'mean square method')
print('')
serial_test(max_length_sequence(), 'max length sequence')
serial_test(deduction_method(), 'deduction method')
serial_test(mean_sqr_method(), 'mean square method')
print('')
poker_test(max_length_sequence(), 'max length sequence')
poker_test(deduction_method(), 'deduction method')
poker_test(mean_sqr_method(), 'mean square method')
print('')
monotony_check(max_length_sequence(), 'max length sequence')
monotony_check(deduction_method(), 'deduction method')
monotony_check(mean_sqr_method(), 'mean square method')
print('')
correlation_test(max_length_sequence(), 'max length sequence')
correlation_test(deduction_method(), 'deduction method')
correlation_test(mean_sqr_method(), 'mean square method')