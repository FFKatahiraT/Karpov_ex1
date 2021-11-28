import math

class mean_sqr_method:
	def __init__(self):
		self.seed = 6239

	def random(self, num_min=0, num_max=1):
		number=str(self.seed**2)
		if len(number)<8:
			add_zeros = 8-len(number)
			number = '0'*add_zeros+number
		av = len(number)//2
		output = int(number[av-2:av+2])
		self.seed = output
		output *= (num_max-num_min)/9999	#bring the value to the defined range
		output += num_min
		return output

class deduction_method:
	def __init__(self):
		self.x=[17,17]
		self.a=81
		self.c=131
		self.m=2**30
		self.init_x()

	def init_x(self):
		for i in range(100):
			output = self.random()

	def random(self, num_min=0, num_max=1):
		self.x[0] = self.x[1]
		self.x[1] = ((self.a*self.x[0]+self.c)%self.m)
		output = self.x[1]
		output *= (num_max-num_min)/(self.m-1)	#bring the value to the defined range
		output += num_min
		return output

class max_length_sequence:
	def __init__(self):
		self.m = 127
		self.l = 16
		self.x = []
		self.b_num = 32
		self.number_set = []
		self.init_x()

	def init_x(self):
		rand = deduction_method()
		intit_part_1 = self.m//3*2
		# intit_part_1 = self.m//2*2
		for i in range(2):
			self.x.append([1])
			for j in range(intit_part_1):
				self.x[i].append(int(rand.random()))
			for j in range(self.m-1-intit_part_1):
				self.x[i].append(1)
		for i in range(1000):	#skip initial values
			self.random()

	def generate_set(self):
		self.x[1][0] = int(self.x[0][self.l-1]!=self.x[0][self.m-1])
		for i in range(self.m-1):
			self.x[1][i+1] = self.x[0][i]
		self.x[0] = self.x[1][:]
		self.number_set = self.x[1][:]
		
	def random(self, num_min=0, num_max=1):
		if len(self.number_set) <= self.b_num:
			self.generate_set()
		output=''
		for i in range(self.b_num):
			output += str(self.number_set[i])
		self.number_set = self.number_set[self.b_num:]
		output = int(output,2)
		output *= (num_max-num_min)/(2**self.b_num-1)	#bring the value to the defined range
		output += num_min
		return output
		
class exp_distr():
	def __init__(self):
		self.lmb = 1000
		self.rand = deduction_method()

	def random(self, num_min=0, num_max=1):
		min_val = math.exp(-num_max*self.lmb)
		max_val =  math.exp(-num_min*self.lmb)
		rand = self.rand.random(min_val, max_val)
		output = -1/self.lmb*math.log(rand)
		return output