#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:19:50 2021

@author: ivagoel
"""

import izhikevich_cells as izh
import matplotlib.pyplot as plt

class ibCell(izh.izhCell):
    def __init__(self):
        super().__init__(4000)
        # Define Neuron Parameters
        self.celltype='Intrinsically Bursting Izhikevich' # Regular spiking
        self.C=150
        self.vr=-75
        self.vt=-45
        self.k=1.2
        self.a=0.01
        self.b=5
        self.c=-56
        self.d=130
        self.vpeak=50
    
if __name__=='__main__':
    myCell = ibCell()        
    myCell.simulate()
    izh.plotMyData(myCell)