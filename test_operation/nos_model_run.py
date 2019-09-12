# -*- coding: utf-8 -*-
"""
Created on Mon May 26th 2019

A script to run and post-process the Italy Calliope 20-node model based on a NOS (near-optimal solutions) logic

@author: F.Lombardi
"""
#%% Initialisation
import calliope
import numpy as np
import calliope.core.io


calliope.set_log_verbosity('INFO') #sets the level of verbosity of Calliope's operations

#%% 

model = calliope.Model('Model/model.yaml')
model.run(build_only=True)


