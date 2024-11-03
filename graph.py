import streamlit as st
import pandas as pd
import numpy as np
from math import sin
from matplotlib import pyplot as plt
opt=st.sidebar.radio('Select Any Graph',options=('Line','Bar','H-Bar'))
if opt=='Line':
    x=np.linspace(0,10,100)
    fig=plt.figure()
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x),'--')
    st.write(fig)