# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 21:36:46 2023

@author: YOGB
"""

class Multiply():
    def __init__(self, coeff=1.0):
        self.coeff = coeff
    
    def Result(self, var1, var2):
        output = var1*var2*self.coeff
        return(output)