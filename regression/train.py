
import numpy as np
import pandas as pd
import sklearn as sk
from sklearn.linear_model import LinearRegression
from numpy import random





X = random.randint(100 , size=(10,3))
Y = random.randint(200 , size=(10,1))
model = LinearRegression().fit(X,Y)

def predictor(x):
    ' in thin function predict given value'
    
    pred = model.predict(x)
    return pred


