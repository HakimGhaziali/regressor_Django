
import numpy as np
import pandas as pd
import sklearn as sk
from sklearn.linear_model import LinearRegression
from numpy import random
import matplotlib.pyplot as plt





def predictor(X,Y,Z):

    ' in thin function predict given value'

    model = LinearRegression().fit(X,Y)
    sc = model.score(X, Y)
    coe = model.coef_
    inter = model.intercept_
    
    pred = model.predict(Z)
    fig, ax = plt.subplots( nrows=1, ncols=1 )
    sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
    ax.scatter(X, Y , color = '#88c999', alpha=0.5)
    ax.plot(X, model.predict(X) ,  ls = ':')
    fig.savefig('static/images/to.png')
    plt.close(fig) 

    Xd = pd.DataFrame(data = X)
    Yd = pd.DataFrame(data = Y)
    dt = pd.concat([Xd,Yd] , axis=1)

    
    return pred , coe , inter


