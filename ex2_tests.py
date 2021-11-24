import matplotlib.pyplot as plt
from random_methods import *
import pandas as pd
import random

def calc_hi_sqr(num, num_theor):
	hi_sqr = 0
	for i in range(len(num)):	#calc hi_sqr criteria
		hi_sqr+=(num[i] - num_theor)**2/num_theor
	return round(hi_sqr,2)

def norm(func, max_val):
	max_func = max(func)
	for i in range(len(func)):
		func[i] /= max_func
	for i in range(len(func)):
		func[i] *= max_val
	return func

def find_probabilities(func):
	sum_func = sum(func)
	for i in range(len(func)):
		func[i] /= sum_func
	return func

def frequency_test(rand, method):
	k=100
	N=10**5
	num, num_freq=[], []
	num_theor=[]
	for i in range(k):	#init 
		num_freq.append(0)
		num_theor.append(N/k)
	for i in range(N):
		num.append(int(rand.random(0,k)))
		# num.append(rand.randint(0,k))
		if len(num_freq) > num[i]:
			num_freq[num[i]] += 1	#add a point to the value that we get here
	
	# print(num_freq, 'num_freq')
	hi_sqr = calc_hi_sqr(num_freq, N/k)
	hi_cr1 = 82.36
	hi_cr2 = 135.81
	if hi_cr1 < hi_sqr < hi_cr2:
		result = 'passed'
	else:
		result = 'failed'
	print(hi_cr1,'<', round(hi_sqr,2), '<',hi_cr2, method, result)

	plt.plot(range(len(num_theor)), num_theor, color='green', label='Theoretical')
	plt.scatter(range(len(num_freq)), num_freq, label='Experiment', color='orange')
	plt.fill_between(range(len(num_freq)),num_freq, alpha=0.5, color='orange')
	# data = pd.Series(num)
	# data.hist(bins=int(max(num)), label='Experiment')
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
		# randint = int(rand.randint(0,d))
		if randint < 10:
			u.append(randint)
	# u = norm(u, 9)
	# print(u)
	# for i in range(len(u)):
	# 	u[i] = int(u[i])
	i = 0
	while i < len(u)-1:
		z.append(int(str(u[i])+str(u[i+1])))	#46 im
		i += 2
	for i in range(len(z)):
		N_exp[z[i]] += 1	#add a point to the value that we get here
	# print(N_exp)
	hi_sqr = calc_hi_sqr(N_exp, N/200)	#calc hi
	hi_cr1 = 82.36
	hi_cr2 = 135.81
	if hi_cr1 < hi_sqr < hi_cr2:
		result = 'passed'
	else:
		result = 'failed'
	print(hi_cr1,'<', round(hi_sqr,2), '<',hi_cr2, method, result)

	plt.scatter(range(len(N_exp)), N_exp, label='Experiment', color='orange')
	plt.plot(range(len(N_theor)), N_theor, color='green', label='Theoretical')
	plt.fill_between(range(len(N_exp)),N_exp, alpha=0.5, color='orange')
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

	sum_cases = sum(cases)
	for i in range(len(cases)):	#calc probabilities of cases
		cases[i] /= sum_cases

	N_exp = []
	for i in range(len(cases)):
		N_exp.append(cases[i])
	# N_exp = find_probabilities(N_exp)	#normalize num_freq
	# print(N_exp, 'N_exp')
	# print(1/7)
	hi_sqr = calc_hi_sqr(N_exp, N/500000)	#calc hi
	hi_cr1 = 2.83
	hi_cr2 = 18.48
	if hi_cr1 < hi_sqr < hi_cr2:
		result = 'passed'
	else:
		result = 'failed'
	print(hi_cr1,'<', round(hi_sqr,2), '<',hi_cr2, method, result)

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

	plt.plot(P_xlabel, cases, label='Experiment', color='orange')
	plt.plot(P_xlabel, P_theor, color='green', label='Theoretical')
	plt.fill_between(P_xlabel,cases, alpha=0.5, color='orange')
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
		result = 'passed'
	else:
		result = 'failed'
	print(round(R_min,2), '<', R, '<', round(R_max,2), method, result)

def interval_test(rand, method):
	k = 100
	N = 10**5
	d = 1
	alpha = 0.9
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
				print('Sigma not found')
				return
			break		

	n = sigma**2/d**2/alpha
	# d_theor = (k*0.34)/(n*alpha)**0.5	
	# d_theor = round(d_theor,2)
	n = int(n)

	# average = []	#find av
	# running = True
	# for j in range(1, n):
	# 	average.append(0)
	# 	for i in range((j-1)*n,j*n):
	# 		if i < N:
	# 			average[j-1] += psi[i]/n
	# 		else:
	# 			running=False
	# 			break
	# 	if running==False:
	# 		del average[len(average)-1]
	# 		break

	d_exp = abs(sum(psi)/len(psi) - exp_val)
	d_cr = sigma/(n*alpha)**0.5
	if d_exp <= d_cr:
		print('Accepted, d_cr=', d_cr, method)
	else:
		print('Rejected, d_cr=', d_cr, method)

	print('alpha=', alpha,'; n=', n, '; d_exp=',d_exp)

	plt.plot(range(len(psi_freq)), psi_freq, label='Experiment', color='orange')
	plt.plot([exp_val]*2, [0,max(psi_freq)], label='exp val', color='green')
	plt.plot([sigma+exp_val]*2, [0,max(psi_freq)], label='sigma', color='red')
	plt.plot([exp_val-sigma]*2, [0,max(psi_freq)], color='red')
	# plt.plot(P_xlabel, P_theor, color='green', label='Theoretical')
	plt.fill_between(range(len(psi_freq)),psi_freq, alpha=0.5, color='orange')
	plt.title('Interval test: '+method+'. d='+str(d_cr)+', N='+str(N))
	plt.legend(loc='best')
	plt.ylabel('Probability')
	plt.grid()
	plt.savefig('Interval_test_'+method+'.png')
	plt.close()

	# counter = 0
	# for i in range(len(average)):
	# 	if exp_val-d <= average[i] <= exp_val+d:
	# 		counter += 1
	# alpha = 1-counter/len(average)

	# print(average, 'average')
	
	# print(exp_val, 'exp_val')


print('FREQUENCY TEST')
frequency_test(max_length_sequence(), 'max length sequence')
frequency_test(deduction_method(), 'deduction method')
# frequency_test(random, 'random')
frequency_test(mean_sqr_method(), 'mean square method')
print('\n SERIAL TEST')
serial_test(max_length_sequence(), 'max length sequence')
# serial_test(random, 'random')
serial_test(deduction_method(), 'deduction method')
serial_test(mean_sqr_method(), 'mean square method')
print('\n POKER TEST')
poker_test(max_length_sequence(), 'max length sequence')
poker_test(deduction_method(), 'deduction method')
poker_test(mean_sqr_method(), 'mean square method')
print('\n CORRELATION TEST')
correlation_test(max_length_sequence(), 'max length sequence')
correlation_test(deduction_method(), 'deduction method')
correlation_test(mean_sqr_method(), 'mean square method')
print('\n INTERVAL TEST')
interval_test(max_length_sequence(), 'max length sequence')
interval_test(deduction_method(), 'deduction method')
# interval_test(mean_sqr_method(), 'mean square method')

# print('\n MONOTONY CHECK')
# monotony_check(max_length_sequence(), 'max length sequence')
# monotony_check(deduction_method(), 'deduction method')
# monotony_check(mean_sqr_method(), 'mean square method')
