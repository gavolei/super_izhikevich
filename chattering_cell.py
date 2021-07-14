#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:20:41 2021

@author: ivagoel
"""

import izhikevich_cells as izh
import matplotlib.pyplot as plt

class chCell(izh.izhCell):
    def __init__(self):
        super().__init__(4000)
        # Define Neuron Parameters
        self.celltype='Intrinsically Bursting Izhikevich' # Regular spiking
        self.C=50
        self.vr=-60
        self.vt=-40
        self.k=1.5
        self.a=0.03
        self.b=1
        self.c=-40
        self.d=150
        self.vpeak=25
    
if __name__=='__main__':
    myCell = chCell()        
    myCell.simulate()
    izh.plotMyData(myCell)