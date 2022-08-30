
import numpy as np
import pandas as pd
import sklearn as sk
from sklearn.linear_model import LinearRegression
from numpy import random
import matplotlib.pyplot as plt





def predictor(X,Y,Z):

    ' in thin function predict given value'

    model = LinearRegression().fit(X,Y)
    
    pred = model.predict(Z)
    fig, ax = plt.subplots( nrows=1, ncols=1 )
    ax.plot(X, Y)
    fig.savefig('static/images/to.png')
    plt.close(fig) 

    return pred


