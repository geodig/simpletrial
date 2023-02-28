# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 21:40:37 2023

@author: YOGB
"""
import streamlit as st
from module.mod1 import Multiply

A = st.slider("var1:", min_value=0, max_value=10)
B = st.slider("var2:", min_value=0, max_value=10)

C = Multiply(coeff=2.0)
st.write("%.2f"%(C.Result(A,B)))

