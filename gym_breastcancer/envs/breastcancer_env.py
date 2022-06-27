#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 16:59:39 2022

@author: shossain
"""
import gym
import numpy as np
import random

class BreastCancerDCIS(gym.Env):
    
    def __init__(self):
        
        '''
        I have 10 action space. Defined the action space from 0 to 9
        '''
        self.action_space = gym.spaces.Discrete(9)
        
        '''
        Feature space has 7 features. Therefore, the observation space
        defined as dictionary with each key as afeature
        
        '''
        
        self.observation_space = gym.spaces.Discrete(14)
        
        '''
        I want each trajectory to start at higher tumor value with
        some randomisation.
        
        '''
        # initial state
        
        self.state = 13 + random.randint(-1, 0)
        self.treatment_length = 60
        self.log = ''
        
        
        
    def step(self, action):
        
        # log the chosen action
        
        self.log += f'Chosen action: {action}\n'
        
        # log the state
        
        self.log += f'state: {self.state}\n'
        
        # load matrices
        transition_matrix = np.load('transition_matrix3.npy')
        reward_matrix = np.load('reward_matrix2.npy')
        
        # extract transition_state and rewards
        P = transition_matrix[action, self.state, :]
        states = np.arange(0,14)
        transition_state = np.random.choice(states, 1 ,replace = True, p=P)[0,]
        
        reward = reward_matrix[self.state,action]
        self.state = transition_state
        
        # log the transition state
        
        self.log += f'transition_state: {transition_state}\n'
        
        
        self.treatment_length -= 1
        
        if (self.state >= 0 and self.state <= 1) or (self.treatment_length == 0):
            done = True
        else:
            done = False
            
        info = {}
        
        return self.state, reward, done, info       
    
    def render(self, mode=None):
        print(self.log)
        self.log = ''
    
    def reset(self):
        self.state = 13 + random.randint(-1, 0)
        self.treatment_length = 60
        return self.state