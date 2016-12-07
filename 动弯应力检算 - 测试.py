# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:52:20 2016

@author: zhanggaoyang
"""
import numpy as np
#所有数字均需写成浮点数，不能出现整数，出现整数会导致除法运算出错！
zhouzhong = 23.0#(t)
zhoushu = 3.0#(m)            
zhouju = 1.8#(m)
D = 30.0#(kN/mm)
a = 0.6#(m)
Ex = 210.0#(GPa)
Ix = 3217.0#(cm^4)
W1 = 396#(cm^3)
W2 = 339.4#(cm^3)
alpha = 0.42
beita_p = 0.15
f = 1.60
sigma_allow = 312.0#(MPa)
k = D / a#MPa
beita = (k / (4*Ex*Ix*10**7)) ** (1/4.0)
x1 = 0
x2 = zhouju*1*1000
x3 = zhouju*2*1000
if zhoushu < 2.5:
    M1 = (zhouzhong*10**4/2.0 * np.exp(-beita*x1)*(np.cos(beita*x1)-np.sin(beita*x1))) / (4*beita)
    M2 = (zhouzhong*10**4/2.0 * np.exp(-beita*x2)*(np.cos(beita*x2)-np.sin(beita*x2))) / (4*beita)
    M = M1 + M2
if 2.5 < zhoushu < 3.5:
    M1 = (zhouzhong*10**4/2.0 * np.exp(-beita*x1)*(np.cos(beita*x1)-np.sin(beita*x1))) / (4*beita)
    M2 = (zhouzhong*10**4/2.0 * np.exp(-beita*x2)*(np.cos(beita*x2)-np.sin(beita*x2))) / (4*beita)
    M3 = (zhouzhong*10**4/2.0 * np.exp(-beita*x3)*(np.cos(beita*x3)-np.sin(beita*x3))) / (4*beita)
    M11 = M1 + M2 + M3
    M22 = M1 + 2*M2
    M = np.max((M11,M22))
Md = M * (1 + alpha + beita_p) * f
sigma_1 = Md / W1 /1000.0
sigma_2 = Md / W2 /1000.0 
