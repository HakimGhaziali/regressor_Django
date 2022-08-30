from django.shortcuts import render
from .train import predictor
# Create your views here.
from .forms import VariableForm
import numpy as np

def predict(request):

    if request.method == 'GET':

        form = VariableForm()

        return render(request ,  'home.html' , {'form': form})

    elif request.method == 'POST':

        form = VariableForm(request.POST)

        if form.is_valid():

            X_list=form.cleaned_data['X'].split(',')
            X_list = [int(i) for i in X_list]
            X= np.array((X_list))
            X= np.reshape(X , (-1,1))

            Y_list=form.cleaned_data['Y'].split(',')
            Y_list = [int(i) for i in Y_list]
            Y= np.array((Y_list))
            Y= np.reshape(Y , (-1,1))
            

            Z_list=form.cleaned_data['Z'].split(',')
            Z_list = [int(i) for i in Z_list]
            Z= np.array((Z_list))
            Z= np.reshape(Z , (-1,1))
            
            
            pre = predictor(X,Y,Z)
                 
            return render(request ,  'result.html' , {'pre': pre})

        

    


        






    


