
import numpy as np
import pandas as pd
import sklearn as sk
from sklearn.linear_model import LinearRegression
from numpy import random





def predictor(X,Y,Z):

    ' in thin function predict given value'

    model = LinearRegression().fit(X,Y)
    
    pred = model.predict(Z)
    return pred


