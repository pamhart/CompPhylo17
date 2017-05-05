class MarkovChain(object):
	"""A discrete-state, continuous-time Markov chain
	"""
	def __init__(self,stateSpace,Q,startSeq=[],endSeq=[]):
		"""
		Initializing variables that are necessary for simulating a continuous-time Markov chains
			- state space
			- length of branches
			- Q matrix
			- exchangeability (from Q-mat)
			- equilibrium frequencies (from Q-mat)
			- number of sites
			- list of simulated states (or list of lists for >1 site)
			- list of waiting times (or list of lists for >1 site)
			- starting sequence (empty if simulating)
			- ending sequence (empty if simulating)
		"""
		self.stateSpace = stateSpace 	# self. = variables initializing for the argument; state space
		self.eq = eq					#equilibrium frequencies
		self.R = R						#exchangeability
		self.Q = []						#Q-matrix that can be built from eq and R
		self.brl = brl 					#branch lengths takes place of number of iterations from discrete
		self.nsites = nsites 			#nsites in continuous = nchains in discrete
		self.simStates = []				#list of simulated states
		self.waitTimes = []				#list of waiting times
		self.startSeq = startSeq		#starting sequence
		self.endSeq = endSeq			#ending sequence
		self.likelihood = 1				#overall likelihood
		
	def discSamp(self,states=[],probs=[]):
		"""
		Samples from an arbitrary discrete distrib. States and probs lists must be equal in length. Probs need to sum to 1
		"""
		r = random.random()
		cumulProb = 0
		index = 0
		for p in probs:
			cumulProb = cumulProb + p
			if r < cumulProb:
				return states[index]
			index += 1
		print("ERROR: Probabilities did not add to 1!")
	def createQ(self):
		""" 
		Create Q-matrix from equilibrium frequencies and exchangeabilities 
		"""
		numStates = len(self.stateSpace)		#number of states that we have
		Q = numpy.matrix(numpy.zeros(shape=(numStates,numStates)))
		for row in range(numStates):			#rows in Q-mat
			for col in range (numStates): 		#columns in Q-mat
				if (row != col):				#For A in row and C in column need R that's a to c, frequency of c
					Q[row,col] = self.eq[col]	#For every off diagonal, we are putting in the equilibrium freqs
		rIndex = 0
		for row in range(numStates):
			for col in range(numStates):
				if (col > row):
					Q[row,col] *= self.R[rIndex]
					rIndex += 1			
							
		rIndex = 0
		for col in range(numStates):
			for row in range(numStates):
				if (col < row):
					Q[row,col] *= self.R[rIndex]
					rIndex += 1					
		
		for state in range(numStates):
			Q[state,state] = ... ####***********STOPPED HERE
			
	def clear(self):
		"""
		Method to clear lists of simulated states and waiting times.
		"""
		self.simStates = []
		self.waitTimes = []
		self.likelihood = 1
		
	def run(self):
		"""
		Method to simulate the states sampled by a Markov Chain
		"""
		#Reset chains here to empty list of lists
		self.clear()

		#For loop across chains (we'll simulate chains one at a time);  loop across all our sites
		for site in range(self.nsites):
		 
			#Define starting sequence
			if (len(self.startSeq < site):                                       #length of sequence should be less than the sites until we finish the sequence
				self.startSeq[site] = self.discSamp(self.stateSpace,self.eq)