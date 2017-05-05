
# coding: utf-8

# In[1]:

import random
import numpy as np


# In[8]:

class MChain(object):
    '''This is our Markov chain class'''
    
    def __init__(self,num_chains,tMat,state_space,steps,chains,time):
        #Need to initialize variables
        self.num_chains=num_chains
        self.tMat=tMat
        self.state_space=state_space
        self.steps=steps
        self.chains=chains
        self.time=time
        
    def run_discrete(self,num_chains,tMat,state_space,steps,chains):
        #run the chain
        
        for chain in range(0,num_chains):
            #randomly choose a state in the state space 
            current_state=random.choice(state_space)
            chains[chain].append(current_state)
            current_state_index=state_space.index(current_state)
            for _ in range (0,steps):
                proposal=random.choice(state_space)
                proposal_index=state_space.index(proposal)
                if tMat[current_state_index][proposal_index]==1:
                    current_state=proposal
                    chains[chain].append(current_state)
                    current_state_index=proposal_index
                elif tMat[current_state_index][proposal_index]==0:
                    chains[chain].append(current_state)
                else:
                    random_number=random.uniform(0,1)
                    if random_number <= tMat[current_state_index][proposal_index]:
                        current_state_index=proposal_index
                        chains[chain].append(current_state)
                    else:
                        chains[chain].append(current_state)
        return chains
    
    def clear(self):
        #clear the chain
        sampled_space=[]
        
    def summary(self,num_chains,chains):
        for chain in range(0,num_chains):
            chain_length=len(chains[chain])
            sunny_count=0
            rainy_count=0
            for _ in range(0,chain_length):
                if chains[chain][_] == 'Rainy':
                    rainy_count=rainy_count+1
                else:
                    sunny_count=sunny_count+1
            rainy_freq=rainy_count/sampled_length
            sunny_freq=sunny_count/sampled_length
        print ('The frequency of rainy for chain'+str(chain)+'is:'+str(rainy_freq))
        print ('The frequency of sunny for chain'+str(chain)+'is:'+str(sunny_freq))
        return 
            
    def forwardProb (self,num_chains,tMat,state_space,chains):
        '''Calculate the probability of observing the full set of states simulated 
        for a particular chains, assuming the chain went in the forward direction'''
        prob=1.0
        #For loop across iterations
        for chain in range(0,num_chains):
            chain_length=len(chains[chain])
            for _ in range(0,chain_length):
                if _==chain_length-1:
                    return prob
                else:
                    starting_state_spot=chains[chain][_]
                    next_state_spot=chains[chains][_+1]
                    start_index=state_space.index(starting_state)
                    next_state_index=state_space.index(next_state_spot)
                    prob *= tMat[start_index][next_state_index]
                    
            #Find the index of the state for the current iteration
            #Find the index of the state for the next iteration
            #Multiply overall probability by P(B|A)
            
        #Return the probability
        return prob
    
    def reverseProb(self,num_chains,tMat,state_space,chains):
        '''Calculate the probability of observing the full set of states simulated 
        for a particular chains, assuming the chain went in the reverse direction'''
        prob=1.0
        #For loop across iterations
        for chain in range(0,num_chains):
            chain_length=len(chains[chain])
            for _ in range(0,chain_length,-1):
                if chain_length==_:
                    return prob
                else:
                    starting_state_spot=chains[chain][_]
                    next_state_spot=chains[chains][_+1]
                    start_index=state_space.index(starting_state)
                    next_state_index=state_space.index(next_state_spot)
                    prob *= tMat[start_index][next_state_index]
                    
            #Find the index of the state for the current iteration
            #Find the index of the state for the next iteration
            #Multiply overall probability by P(B|A)
            
        #Return the probability
        return prob
    
    
    def marginalForwardProb(self,num_chains,tMat,state_space,steps,chains):
        '''Calculate the marginal probability of starting in one state and ending in another, consideringall possible 
        intermediates'''
        #Raise your Q-matrix (tMat), to the power of the number of iterations. You'll need
        #numpy.linalg.matrix_power() for this
        #Find the index of the starting state for the chain 
        
        #Find the index of the ending state for the chain
        
        #Look up P(E|S)
        
        #Return the relevant probability 
        
    def run_continuous(self,num_chains,tMat,state_space,time,chains):
        #run the chain
        
        for chain in range(0,num_chains):
            #randomly choose a state in the state space 
            current_state=random.numpy.gamma(1)
            chains[chain].append(current_state)
            current_state_index=state_space.index(current_state)
            for _ in range (0,time):
                proposal=random.choice(state_space)
                proposal_index=state_space.index(proposal)
                if tMat[current_state_index][proposal_index]==1:
                    current_state=proposal
                    chains[chain].append(current_state)
                    current_state_index=proposal_index
                elif tMat[current_state_index][proposal_index]==0:
                    chains[chain].append(current_state)
                else:
                    random_number=random.numpy.gamma(1)
                    if random_number <= tMat[current_state_index][proposal_index]:
                        current_state_index=proposal_index
                        chains[chain].append(current_state)
                    else:
                        chains[chain].append(current_state)
        return chains


# In[7]:

state_space=['Rainy','Sunny']
tMat=[[0,1],[0.2,0.8]]
steps=20
chains=10
num_chains=3
num_chains,tMat,state_space,steps,chains
chains=[[] for i in range (0,num_chains)]
test=MChain(num_chains,tMat,state_space,steps,chains)
test.run_discrete(test.num_chains,test.tMat,test.state_space,test.steps,test.chains)
test.forwardProb(test.num_chains,test.tMat,test.state_space,test.chains)


# In[ ]:



