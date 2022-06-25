#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 10:43:18 2022

@author: shossain
"""

from distutils.core import setup
setup(
  name = 'gym_breastcancer',         
  packages = ['gym_breastcancer'],   
  version = '0.1',      
  license='MIT',        
  description = 'A breast cancer simulator for benchmarking Reinforcement Learning algorithms',   
  author = 'Shafayet Shariar Hossain',                   
  author_email = 'shossain1@usf.edu',      
  url = 'https://github.com/vadim0x60/heartpole',   
  download_url = 'https://github.com/vadim0x60/heartpole/archive/v_11.tar.gz',    
  keywords = ['Machine Learning', 'Reinforcement Learning', 'Healthcare'],   
  install_requires=[            
          'numpy',
          'gym',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Science/Research',      
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.6',
  ],
)