#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 16:54:31 2022

@author: shossain
"""
from gym.envs.registration import register

register(
    id = 'breastcancer-v0',
    entry_point = 'gym_breastcancer.envs:BreastCancerDCIS',
    kwargs = {}
    )
