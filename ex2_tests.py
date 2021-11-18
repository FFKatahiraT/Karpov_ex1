import matplotlib.pyplot as plt
from random_methods import *
import pandas as pd

def calc_hi_sqr(num, num_theor):
	hi_sqr = 0
	for i in range(len(num)):	#calc hi_sqr criteria
		hi_sqr+=(num[i] - num_theor)**2/num_theor
	return hi_sqr

def norm(func):
	max_func = max(func)
	for i in range(len(func)):
		func[i] /= max_func
	return func

def find_probabilities(func):
	sum_func = sum(func)
	for i in range(len(func)):
		func[i] /= sum_func
	return func

def frequency_test(rand, method):
	k=10
	N=10**5
	num, num_freq=[], []
	num_theor=[]
	for i in range(k+1):	#init 
		num_freq.append(0)
		num_theor.append(N/k)
	for i in range(N):
		num.append(int(rand.random(0,k)))
		num_freq[num[i]] += 1	#add a point to the value that we get here
	
	num_freq = find_probabilities(num_freq)	#normalize num_freq
	# print(num_freq, 'N_exp')
	# print(1/k, 'N_theor')
	hi_sqr = calc_hi_sqr(num_freq, 1/k)

	print(hi_sqr, 'hi_sqr', method)
	plt.plot(range(len(num_theor)), num_theor, color='green', label='Theoretical')
	data = pd.Series(num)
	data.hist(bins=int(max(num)), label='Experiment')
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
	N_exp, N_theor = [], []
	for i in range(100):
		N_exp.append(0)
		N_theor.append(N/200)

	for i in range(N):
		randint = int(rand.random(0,d))
		if randint < 10:
			u.append(randint)
	i = 0
	while i < len(u)-1:
		z.append(int(str(u[i])+str(u[i+1])))	#46 im
		i += 2
	for i in range(len(z)):
		N_exp[z[i]] += 1	#add a point to the value that we get here
	N_exp = find_probabilities(N_exp)	#normalize num_freq
	# print(N_exp, 'N_exp')
	# print(N_theor[0], 'N_theor')
	hi_sqr = calc_hi_sqr(N_exp, 1/100)	#calc hi

	print('serial test', method, 'hi_sqr:', round(hi_sqr,2))
	data = pd.Series(z)
	data.hist(bins=int(max(z)), label='Experiment')
	plt.plot(range(100), N_theor, color='green', label='Theoretical')
	plt.title('Serial test: '+method+'. d='+str(d)+', N='+str(N))
	plt.legend(loc='best')
	plt.ylabel('Number of operations')
	plt.xlabel('Value')
	plt.grid()
	plt.savefig('serial_test_'+method+'.png')
	plt.close()

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
	N_exp = []
	for i in range(len(cases)):
		N_exp.append(cases[i])
	N_exp = find_probabilities(N_exp)	#normalize num_freq
	# print(N_exp, 'N_exp')
	# print(1/7)
	hi_sqr = calc_hi_sqr(N_exp, 1/7)	#calc hi

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

def interval_test(rand, method):
	k = 10
	N = 10**4
	d = 1
	alpha = 0.5
	psi, psi_freq = [], []
	exp_val = 0
	hi_sqr = 0
	sigma = 1
	for i in range(N):
		psi.append(int(rand.random(0,k)))

	for i in range(max(psi)+1):
		psi_freq.append(0)
	for i in range(N):
		psi_freq[psi[i]] += 1
	psi_freq = find_probabilities(psi_freq)
	for i in range(max(psi)+1):
		exp_val += psi_freq[i]*i#find exp val
	for i in range(int(exp_val)+1,max(psi)+1):
		if 0.33*sum(psi_freq) < sum(psi_freq[int(exp_val):i]) < 0.4*sum(psi_freq):
			sigma = i - exp_val
			if sigma == 0:
				print('Sigma error')
				sigma = 1
			break
	else:
		print('Sigma not found')

	n = sigma**2/d**2/alpha
	d_theor = (k*0.34)/(n*alpha)**0.5	
	n = int(n)
	if d_theor >= d:
		print('Accepted, d_theor=', round(d_theor,2))
	else:
		print('Rejected, d_theor=', round(d_theor,2))
	average = []	#find av
	running = True
	for j in range(1, n):
		average.append(0)
		for i in range((j-1)*n,j*n):
			if i < N:
				average[j-1] += psi[i]/n
			else:
				running=False
				break
		if running==False:
			del average[len(average)-1]
			break

	# counter = 0
	# for i in range(len(average)):
	# 	if exp_val-d <= average[i] <= exp_val+d:
	# 		counter += 1
	# alpha = 1-counter/len(average)

	# print(average, 'average')
	print(n, 'n')
	print(exp_val, 'exp_val')


print('FREQUENCY TEST')
frequency_test(max_length_sequence(), 'max length sequence')
frequency_test(deduction_method(), 'deduction method')
frequency_test(mean_sqr_method(), 'mean square method')
print('\n SERIAL TEST')
serial_test(max_length_sequence(), 'max length sequence')
serial_test(deduction_method(), 'deduction method')
serial_test(mean_sqr_method(), 'mean square method')
print('\n POKER TEST')
poker_test(max_length_sequence(), 'max length sequence')
poker_test(deduction_method(), 'deduction method')
poker_test(mean_sqr_method(), 'mean square method')
print('\n MONOTONY CHECK')
monotony_check(max_length_sequence(), 'max length sequence')
monotony_check(deduction_method(), 'deduction method')
monotony_check(mean_sqr_method(), 'mean square method')
print('\n CORRELATION TEST')
correlation_test(max_length_sequence(), 'max length sequence')
correlation_test(deduction_method(), 'deduction method')
correlation_test(mean_sqr_method(), 'mean square method')
print('\n INTERVAL TEST')
interval_test(max_length_sequence(), 'max length sequence')
interval_test(deduction_method(), 'deduction method')
interval_test(mean_sqr_method(), 'mean square method')
