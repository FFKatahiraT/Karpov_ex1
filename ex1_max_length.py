import matplotlib.pyplot as plt

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
	m=5
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

max_length_seq()