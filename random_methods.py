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
		self.x=[7,7]
		self.a=9
		self.c=7
		self.m=1024

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
		self.l = 15
		self.x = []	
		self.init_x()

	def init_x(self):
		for i in range(2):
			self.x.append([])
			for j in range(self.m):
				self.x[i].append(1)
		for i in range(1000):	#skip initial values
			self.random()

	def random(self, num_min=0, num_max=1):
		self.x[1][0] = int(self.x[0][self.l-1]!=self.x[0][self.m-1])
		for i in range(self.m-1):
			self.x[1][i+1] = self.x[0][i]
		self.x[0] = self.x[1][:]
		output=''
		for i in range(10):
			output+=str(self.x[1][i])
		output = int(output,2)
		output *= (num_max-num_min)/(2**10-1)	#bring the value to the defined range
		output += num_min
		return output